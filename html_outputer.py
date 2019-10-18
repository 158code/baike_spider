class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('out_put.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        # Python 默认编码格式是： Ascii
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()