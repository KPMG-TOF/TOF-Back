# fast api 사용
## API 명세
### main
- GET: /api/v1/main/analysis/{ref_id}  
- response
  ```
    {
      "info": {
          "company": "sso",
          "industry": "dev",
          "cost": 12342,
          "title": "2024-1학기-융합필수-교과목-개설-여부2024.01.30.-17시-기준_공지.xlsx"
      },
      "summary": {
          "size": 5453,
          "start_date": "2024-02-03T00:07:41.508158",
          "end_date": "2024-02-03T00:07:41.508158",
          "subject": [
              "클라우드가 필요함",
              "클라우드가 궁금함",
              "어쩌구"
          ],
          "requirement": [
              "보안이 필요함",
              "보안이 궁금함",
              "어쩌구"
          ]
      },
      "reference": [
          {
              "rfp_id": 2,
              "title": "fake ref",
              "end_date": "2024-02-03T00:53:59.488754",
              "manager": "sso",
              "similarity": 44
          }
      ],
      "tasks": {
          "priority": [
              {
                  "order": 2,
                  "title": "priority"
              }
          ],
          "competivity": [
              {
                  "order": 941,
                  "title": "competivity"
              },
              {
                  "order": 603,
                  "title": "competivity"
              },
              {
                  "order": 460,
                  "title": "competivity"
              },
              {
                  "order": 665,
                  "title": "competivity"
              }
          ],
          "workforce": [
              {
                  "count": 910,
                  "category": "workforce"
              },
              {
                  "count": 225,
                  "category": "workforce"
              },
              {
                  "count": 290,
                  "category": "workforce"
              }
          ]
      }
  
  ```  

  대부분 임의의 값  
  -> OCR 또는 AI를 이용해 추출 필요  

### upload rfp
- POST: /api/v1/upload/rfp
- Content-Type: multipart/form-data
- response: 아직 없음

