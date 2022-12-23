A playground to demonstrate basic python skills

To install:
  gh repo clone supraxylon/Flask-playground
  cd ./Flask-playground

To run the app locally:
  .venv\Scripts\activate.bat
  flask --app app run

To run in Debug mode on a trusted network (Enables remote debugging but also allows users in the same network to run arbitrary code on your machine.):
  .venv\Scripts\activate.bat
  flask --app app --debug run
