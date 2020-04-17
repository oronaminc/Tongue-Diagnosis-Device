# Tongue-Diagnosis-Device
- [Device] RaspberryPi(Using Camera Tongue detection) & Arduino(Circular LED control)
- [Software] Pytorch(Disease classfication) and Opencv with python(Divide Tongue part & Analysis Tongue part)
- [Web Site] https://oronaminc.github.io/AI_Tongue/

# Function

1. In Device, Taking Pictrue in realtime video
2. In Device, Control Circular LED brightness
3. In Software, Classfication of Tongue Disease (using tongue state : red tongue/white tongue/pink tongue/little coated/white coated/yellow coated/Existence of tooth scar -> Disease Diagnosis)
4. In Software, Divide and Analysis Tongue part (Divide Tongue into Top/Bottom/Side/Center part and Divide coated part or not)

# HW Device(Arduino + RaspberryPI)
<div>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/68458958-634ac700-0247-11ea-8fc4-6dd6b43b6dc4.gif"/>
</div>

# Presentation

<div>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/68457812-83c55200-0244-11ea-8725-edebf24eee41.JPG"/>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/68457813-83c55200-0244-11ea-8982-352223972716.JPG"/>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/68457814-83c55200-0244-11ea-9705-68b4ad7acec7.JPG"/>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/68457810-83c55200-0244-11ea-9800-b74488bdca70.JPG"/>
</div> 


# Result Video Clip

<div>
  <p> - Device Video Clip</p>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/66882526-b2fdf000-f005-11e9-80f5-95da78d58809.gif"/>
  
  <p> - Website Video Clip</p>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/66881933-847f1580-f003-11e9-86bd-84b11912d8ee.gif"/>
</div>


## pip install

```python 3.5
(option) conda activate
pip3 install numpy
pip3 install cv2
pip3 install tesnorflow
pip3 install scipy
pip3 install scikit-learn
pip3 install keras
pip3 install matplotlib
pip3 install PIL

```
