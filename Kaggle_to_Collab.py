#Downloading Dataset from Kaggle to Collab


                            #Step 1:In Collab Run below
! pip install kaggle

! mkdir ~/.kaggle

! cp kaggle.json ~/.kaggle/

! chmod 600 ~/.kaggle/kaggle.json

#Step 2:Run
#Note:-d gti-upm/leapgestrecog is api key of dataset that you wanna work on.
!kaggle datasets download -d gti-upm/leapgestrecog
