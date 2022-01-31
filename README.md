# Software developer salary prediction

[![heroku deployed](https://raw.githubusercontent.com/DenisOH/pyheroku-badge/master/img/deployed-plastic.svg)](https://salary-prediction-st.herokuapp.com/)

This repository consists of files required to deploy a ___Machine Learning Web App___ for salary prediction created with ___Streamlit___ and deployed on ___Heroku___ platform.

If you want to view the deployed model, click on the __heroku deployed__ button above or in the following link:<br />
Deployed at: _https://salary-prediction-st.herokuapp.com/_

The data are available from the 2021 stack overflow survey:
  [Download Full Data Set(CSV)](https://insights.stackoverflow.com/survey) 
   
   
## Reproducing this web app 
To recreate this web app on your own computer without deployment on heroku, do the following.

### Create conda environment
Firstly, we will create a conda environment called *myenv*
```
conda create -n myenv python=3.7.11
```
Secondly, we will login to the *myenv* environement
```
conda activate myenv
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/quartermaine/Salary-prediction-deploy/main/requirements.txt
```

Pip install libraries
```
pip install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/quartermaine/Salary-prediction-deploy/archive/refs/heads/main.zip

###  Launch the app

```
streamlit run app.py
```

<br />
<br />
<br />

![pic](https://github.com/quartermaine/Salary-prediction-deploy/blob/main/readme_recources/salary_app.png)

<!-- ![pic](https://github.com/quartermaine/Salary-prediction-deploy/blob/main/readme_recources/salary_app.png) -->

_**----- Important Note -----**_<br />
If the webapp is not working and you get the message as shown in the picture given below, it is occuring just because **free dynos for this particular month provided by Heroku have been completely used.** _You can access the webpage on 1st of the next month._<br />

![Heroku-Error](https://github.com/quartermaine/Salary-prediction-deploy/blob/main/readme_recources/application-error-heroku.png)

<!-- <img src="https://github.com/quartermaine/Salary-prediction-deploy/blob/main/readme_recources/application-error-heroku.png" width=80% height=80%> -->



