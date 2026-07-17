#for api, password, url, database url


class Config:

    #sqlalchemy sepcific
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://balaji:Balaji_123@localhost:3306/ems_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "12defndsgd"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"
    APP_NAME = "Employee Management System"