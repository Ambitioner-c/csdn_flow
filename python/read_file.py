import json
import re

# # 文件存储在../data/2.html
# with open('../data/2.html', 'r') as f:
#     html = f.read()
#     # 通过正则表达式来匹配json内容
#     html_json = re.findall(r'>(\{.+?})<', html.replace('\n', '').replace(' ', ''))[0]
#
#     # 输出json对象
#     print(json.loads(html_json))

with open('../data/2.html', 'r') as f:
    html = f.read()
    old_html = html.replace('\n', '').replace(' ', '')

    # 通过正则表达式匹配'\uxxxx'，返回全部'\u'列表，生成u_list
    u_list = re.findall(r'(\\u\w+)', old_html)

    # 使用eval()函数执行字符串表达式（这里将'\uxxxx'视为字符串表达式），返回正常列表，生成n_list
    n_list = []
    for i in u_list:
        i = "u'" + i + "'"
        n_list.append(eval(i))

    # 遍历u_list和n_list，替换原html中的内容
    new_html = old_html
    for i in range(len(u_list)):
        new_html = new_html.replace(u_list[i], n_list[i])
    print(new_html)
