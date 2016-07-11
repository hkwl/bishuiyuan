__author__ = 'yangweidong'
from controller.system.showdata import ShowDtaView
from controller.system.showdata import ChangeStatusView
from controller.system.showdata import ShowBiShuiYuanView
def route(app):
    app.add_url_rule('/', view_func=ShowDtaView.as_view('ShowDtaView'), methods=['Post', 'GET'])
    app.add_url_rule('/status', view_func=ChangeStatusView.as_view('ChangeStatusView'), methods=['Post', 'GET'])
    app.add_url_rule('/list', view_func=ShowBiShuiYuanView.as_view('ShowBiShuiYuanView'), methods=['Post', 'GET'])
