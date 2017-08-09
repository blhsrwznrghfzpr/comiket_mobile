# -*- coding: utf-8 -*-
#!/usr/bin/env python

def main():
    ### 設定 ↓↓↓
    # ダウンロードしたtsvファイル名
    data_tsv = 'sample.tsv'
    # 出力するファイル名
    outputfile = 'cXXtable_mobile.html'
    # 出力したHTMLページのタイトル
    page_title = 'CXX TRPGサークル頒布物一覧'
    # PCサイトのURL
    homepage_url = 'http://comiket-trpg.sakura.ne.jp/'
    ### 設定 ↑↑↑

    with open('data/' + data_tsv, 'r', encoding='utf-8') as f:
        data_title, data_content = f.read().split('\n',1)

    data = [line.split('\t') for line in data_content.split('\n')]

    with open('data/template/template.html', 'r', encoding='utf-8') as f:
        text = f.read()

    f = open(outputfile, 'w', encoding='utf-8')

    tbody_content = ''
    for one in data:
        tbody_content += '<tr>'
        for i, element in enumerate(one):
            if i == 9:
                if element != '':
                    if len(element) > 30:
                        element_title = element[:27]+'...'
                    else:
                        element_title = element
                    element = '<a href={0} target="_blank">{1}</a>'.format(element, element_title)
            tbody_content += '<td>{}</td>'.format(element)
        tbody_content += '</tr>'
    
    text = text.format(PAGE_TITLE=page_title, HOMEPAGE_URL=homepage_url, TBODY_CONTENT=tbody_content)
    f.write(text)
    f.close()
    return

if __name__ == '__main__':
    main()
    print("正常に動作しました")
    input()
