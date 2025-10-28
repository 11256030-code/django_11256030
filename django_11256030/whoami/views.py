from django.shortcuts import render
from django.http import HttpResponse

def whoami(request):
    content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Who Am I</title>
        <style>
            body {
                font-family: "Microsoft JhengHei", "微軟正黑體", Arial, sans-serif;
                font-size: 24px;
                line-height: 1.6;
                margin: 40px;
            }
        </style>
    </head>
    <body>
        <div>
            台北商業大學<br><br>
            五專資管科<br><br>
            11256030<br><br>
            林沛穎
        </div>
    </body>
    </html>
    """
    return HttpResponse(content)
