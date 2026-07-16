#for api, password, url, database url


class Config:

    #sqlalchemy sepcific
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "12defndsgd"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"
    APP_NAME = "Employee Management System"