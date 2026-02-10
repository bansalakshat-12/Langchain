from langchain.openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()

model = ChatOpenAI

class Review(TypedDict):
    summary : str
    sentiment : str

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("I have been a member of this gym for the past six months, and overall my experience has been excellent. The equipment is modern, well-maintained, and rarely out of order, which makes workouts smooth and uninterrupted. The trainers are knowledgeable and approachable, especially for beginners who may feel intimidated at first. They take time to explain exercises properly and correct posture, which has helped me avoid injuries. The gym environment is clean, spacious, and motivating, with good music and proper ventilation. I have noticed a significant improvement in my strength and stamina since joining. The flexible workout timings also make it easy to manage with a busy schedule. Overall, this gym offers great value for money and a supportive fitness environment.")

print(result)