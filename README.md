# ESBR-Game-Rating-Prediction-using-SVM

![xx](https://github.com/H8-Assignments-Bay/p1---ftds006---m2-hafidzali04/blob/58ec0d540e85ec1c2b50119b74b930e3d9bbea18/Screenshot%202022-01-13%20204248.png)
_Milestones ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 1._

---
## WEB

- Link web dapat diakses di (https://esbr-predict.herokuapp.com/)


Video Games Rating By 'ESRB':
Predict the ESRB rating for games based on the content that the game rated on.
## Data yang digunakan
https://www.kaggle.com/imohtn/video-games-rating-by-esrb
Data Description:

* This data contains the name for 1895 games with 34 of ESRB rating content with the name and console as features for each game.
* A single data point is represented as a binary value 0-1 for Console and a binary vector for the features of ESRB content.
### Data Review

|Feature |Type |Description |Keys|
|--- |--- |--- |--- |
title	| string |Name of the game.|----|
console |	int	| The console on which the game was released. |	0 = PS4 , 1 = PS4 & Xbox_one|
Alcohol_Reference |	int |	Reference to and/or images of alcoholic beverages.|	0 = no, 1 = yes|
Animated_Blood |	int |	Discolored and/or unrealistic depictions of blood.|	0 = no, 1 = yes|
Blood	| int |	Depictions of blood.	| 0 = no, 1 = yes|
BloodandGore |	int |	Depictions of blood or the mutilation of body parts.|	 0 = no, 1 = yes|
Cartoon_Violence |	int |	Violent actions involving cartoon-like situations and characters. |	0 = no, 1 = yes|
Crude_Humor |	int |	Depictions or dialogue involving vulgar antics, including "bathroom" humor.| 	0 = no, 1 = yes|
DrugRe_ference |	int	| Reference to and/or images of illegal drugs. |	0 = no, 1 = yes
Fantasy_Violence|	int|	Violent actions of a fantasy nature, involving human or non-human characters in situations easily distinguishable from real life.|	0 = no, 1 = yes
Intense_Violence |	int |	Graphic and realistic-looking depictions of physical conflict. May involve extreme and/or realistic blood, gore, weapons, and depictions of human injury and death. |	0 = no, 1 = yes
Language |	int |	Moderate use of profanity.	0 = no, 1 = yes
Lyrics |	int |	References to profanity, sexuality, violence, alcohol, or drug use in music.|	0 = no, 1 = yes
Mature_Humor	| int |	Depictions or dialogue involving "adult" humor, including sexual references.	|0 = no, 1 = yes
Mild_Blood	|int	|Some blood.|	0 = no, 1 = yes
MildCartoonViolence	|int|	Some violent actions involving cartoon.|	0 = no, 1 = yes
MildFantasyViolence	|int|	Some violent actions of a fantasy nature.|	0 = no, 1 = yes
Mild_Language	|int|	Mild to moderate use of profanity.	|0 = no, 1 = yes
Mild_Lyrics	|int|	Mild References to profanity, sexuality, violence, alcohol, or drug use in music.|	0 = no, 1 = yes
MildSuggestiveThemes	|int|	some provocative references or materials|	0 = no, 1 = yes
Mild_Violence	|int|	Some scenes involving aggressive conflict.	0 = no, 1 = yes
No_Descriptors	|int|	No content descriptors. |	0 = no, 1 = yes
Nudity	|int|	Graphic or prolonged depictions of nudity.|	0 = no, 1 = yes
Partial_Nudity |	int|	Brief and/or mild depictions of nudity.	|0 = no, 1 = yes
Sexual_Content	|int|	Non-explicit depictions of sexual behavior, possibly including partial nudity.|	0 = no, 1 = yes
Sexual_Themes	|int|	References to sex or sexuality.|	0 = no, 1 = yes
Simulated_Gambling	|int|	Player can gamble without betting or wagering real cash or currency.	|0 = no, 1 = yes
Strong_Language	|int|	Explicit and/or frequent use of profanity.|	0 = no, 1 = yes
StrongSexualContent	|int|	Explicit and/or frequent depictions of sexual behavior, possibly including nudity.|	0 = no, 1 = yes
Suggestive_Themes	|int|	Provocative references or materials.|	0 = no, 1 = yes
UseofAlcohol	|int|	The consumption of alcoholic beverages.	0 = no, 1 = yes
UseofDrugsandAlcohol |int|	The consumption of alcoholic and drugs beverages.	|0 = no, 1 = yes
Violence	|int|	Scenes involving aggressive conflict. May contain bloodless dismemberment.|	0 = no, 1 = yes
ESRB_rating	|string|	rating: E - ET - T - M |	 E , ET , T , M 

### ESRB rating description:

|ESRB_rating |	Description |
|---|---|
E	| Everyone|
ET	| Early Teen 10+|
T	| Teen 13+|
M	| Mature 17+|
