import os
import fitz  # PyMuPDF
import google.generativeai as genai
from PIL import Image
import io
import time
from dotenv import load_dotenv

# 1. 환경 변수 로드 및 API 키 설정
load_dotenv()  # .env 파일에서 환경 변수를 불러옵니다.
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API 키를 찾을 수 없습니다. .env 파일에 GEMINI_API_KEY를 설정해 주세요.")

genai.configure(api_key=api_key)

# 이미지 인식에 빠르고 성능이 좋은 flash 모델을 사용합니다.
model = genai.GenerativeModel('gemini-2.5-flash')

def explain_ppt(pdf_path, output_md="lecture_notes.md"):
    print(f"[{pdf_path}] 분석을 시작합니다...")
    
    # PDF 파일 열기
    doc = fitz.open(pdf_path)
    full_notes = f"# PPT 상세 해설 노트\n\n"

    for page_num in range(len(doc)):
        print(f"-> 슬라이드 {page_num + 1}/{len(doc)} 처리 중...")
        
        # 2. PDF 페이지를 이미지로 변환
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes()))

        # 3. 모델에 전송할 프롬프트 설정
        prompt = """
        당신은 친절하고 똑똑한 대학 전공 튜터입니다. 
        첨부된 슬라이드의 핵심 개념을 추출하고, 학생이 완벽하게 이해할 수 있도록 
        '구체적이고 실생활에 가까운 예시'를 하나 이상 들어서 상세히 설명해 주세요.
        불필요한 인사말은 생략하고 바로 본론만 마크다운 형식으로 깔끔하게 정리해 주세요.
        """

        try:
            # 4. API 호출 (이미지 + 텍스트 프롬프트)
            response = model.generate_content([prompt, img])
            
            # 5. 결과물 누적
            full_notes += f"## Slide {page_num + 1}\n\n"
            full_notes += response.text + "\n\n---\n\n"
            
            # API Rate Limit(호출 제한) 방지를 위한 짧은 휴식
            time.sleep(2) 
            
        except Exception as e:
            print(f"슬라이드 {page_num + 1} 처리 중 오류 발생: {e}")
            full_notes += f"## Slide {page_num + 1}\n\n*오류 발생으로 해설을 생성하지 못했습니다.*\n\n---\n\n"

    # 6. 최종 결과를 Markdown 파일로 저장
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(full_notes)
        
    print(f"\n모든 작업이 완료되었습니다! [{output_md}] 파일을 확인해 주세요.")

# 실행 (본인의 PDF 파일명으로 수정하세요)
if __name__ == "__main__":
    #explain_ppt("CSED226/numpy.pdf", "CSED226/numpy.md")
    #explain_ppt("CSED226/pandas.pdf", "CSED226/pandas.md")
    explain_ppt("CSED226/pandasII.pdf", "CSED226/pandasII.md")
    #explain_ppt("CSED226/kNN.pdf", "CSED226/kNN.md")
    #explain_ppt("CSED226/diskANN.pdf", "CSED226/diskANN.md")
    #explain_ppt("CSED226/decisionTree.pdf", "CSED226/decisionTree.md")
    