import os
import requests
from flask import *

app = Flask(__name__)


host = 'https://lblogs-1254016670.cos-website.ap-guangzhou.myqcloud.com'


# 是否重定向。
def judge(argv: str):
    if argv == '':
        return False
    if '.' not in argv:
        return False
    if argv.lower().endswith(('.html', '.htm')):
        return False
    return True


@app.route('/', methods=["GET", ])
def r():
    return requests.get(host).content


@app.route('/<s1>', methods=["GET", ])
def r1(s1):
    target = host + "/%s" % (s1,)
    if judge(s1):
        return redirect(target)
    return requests.get(target).content


@app.route('/<s1>/<s2>', methods=["GET", ])
def r2(s1, s2):
    target = host + "/%s/%s" % (s1, s2)
    if judge(s2):
        return redirect(target)
    return requests.get(target).content


@app.route('/<s1>/<s2>/<s3>', methods=["GET", ])
def r3(s1, s2, s3):
    target = host + "/%s/%s/%s" % (s1, s2, s3)
    if judge(s3):
        return redirect(target)
    return requests.get(target).content


@app.route('/<s1>/<s2>/<s3>/<s4>', methods=["GET", ])
def r4(s1, s2, s3, s4):
    target = host + "/%s/%s/%s/%s" % (s1, s2, s3, s4)
    if judge(s4):
        return redirect(target)
    return requests.get(target).content


@app.route('/<s1>/<s2>/<s3>/<s4>/<s5>', methods=["GET", ])
def r5(s1, s2, s3, s4, s5):
    target = host + "/%s/%s/%s/%s/%s" % (s1, s2, s3, s4, s5)
    if judge(s5):
        return redirect(target)
    return requests.get(target).content


@app.route('/<s1>/<s2>/<s3>/<s4>/<s5>/<s6>', methods=["GET", ])
def r6(s1, s2, s3, s4, s5, s6):
    target = host + "/%s/%s/%s/%s/%s/%s" % (s1, s2, s3, s4, s5, s6)
    if judge(s6):
        return redirect(target)
    return requests.get(target).content


if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get('PORT', '5000')), debug=False)

