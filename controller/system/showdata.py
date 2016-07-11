#! /usr/bin/python
# enconding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import jsonify, request
from flask.views import MethodView
from flask import render_template
from dal.infrastructure.bishuiyuan import BiShuiYuan
from common.createredis import send_data
import redis

__author__ = 'yangweidong'



class ShowBiShuiYuanView(MethodView):
    def get(self):
        psize = request.args.get('psize', 20, type=int)
        pindex = request.args.get('pindex', 1, type=int)
        rows = BiShuiYuan.select().order_by(BiShuiYuan.create_time.desc()).paginate(pindex, psize)
        count = BiShuiYuan.select().count()
        pagecount = count / psize + (1 if (count % psize) > 0 else 0)
        return render_template('/system/bishuiyuan_list.html', rows=rows, psize=psize, pindex=pindex,pagecount=pagecount)

class ChangeStatusView(MethodView):
    def post(self):
        send_status = request.form.get("send_status")
        print send_status
        send_data(send_status)
        return jsonify({'success':'ok'})

class ShowDtaView(MethodView):
    def get(self):
        return render_template("data.html")

    def post(self):
        dic = {}
        re = redis.StrictRedis(host="123.56.201.7", port=6379)
        da = re.get("bishuiyuandate")
        #re.flushall()
        print da
        tds=eval(da)["tds"]
        print tds
        water=eval(da)["water"]
        create_time = eval(da)["create_time"]
        dic["tds"] = tds
        dic["water"] =water
        dic["create_time"] = create_time
        return jsonify({'success':'ok','ret':dic })
