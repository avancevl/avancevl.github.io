import os
from bs4 import BeautifulSoup
import frontmatter
import yaml
from shutil import copyfile


# 讀取./_config.yml參數設定
config_f = open('./_config.yml', "r", encoding="utf-8")
_config = list(yaml.load_all(config_f, Loader=yaml.FullLoader))
locales = _config[0]['locales']
setlang = []
for item in locales:
    setlang.append(locales[item]['lang'])
c_i18n = _config[0]['i18n']
mainPath = c_i18n['mainPath']
tag = c_i18n['tag']
attrname = c_i18n['attrname']
falias = c_i18n['falias']
default_lang = c_i18n['default_lang']
job_form = {}
for item in _config[0]:
    for lang in setlang:
        key = "job_form_url_"+lang
        if key in _config[0].keys():
            job_form[key] = key
        else:
            defalul_job_url = "job_form_url_"+default_lang
            job_form[key] = defalul_job_url


def setlangFile(metadata, value, lang_content):
    article = []
    # print(document_data)
    if "locales" in metadata:
        if value in metadata['locales']:
            post_title = metadata['locales'][value]['title']
            post_description = metadata['locales'][value]['description']
        else:
            # 使用default lang_mate
            post_title = metadata['title']
            post_description = metadata['description']
    else:
        # 使用default lang_mate
        post_title = metadata['title']
        post_description = metadata['description']

    lang_metadata = [
        '---',
        'layout: ' + metadata['layout'],
        'title: ' + post_title,
        'lang: ' + value,
        'description: ' + post_description,
        '---\n\n'
    ]
    # data = list(yaml.load_all(f, Loader=yaml.FullLoader))
    story = '\n'.join(lang_metadata)
    # print(data)
    article.append(story)
    article.append(lang_content[value])
    return article


def rfileDate(filepath, setlang, tag, attrname):
    """
    讀取目錄資料夾檔案，使用標籤參數拆分

    Args:
        filepath: 檔案目錄
        setlang: 檔案語言list[]
        tag: 標籤 a
        attrname: 指定查詢標籤參數 name
    Returns:
        使用查詢到的標籤參數值返回dict
        {
            'zh-tw': [string, string],
            'zh-cn': [string, string],
            'zh-tw': [string, string]
        }
    """
    f = open(filepath, "r", encoding="utf-8")
    soup = BeautifulSoup(f, 'html.parser')
    # print("Parse .md file metadata as filepath------>"+filepath)
    try:
        fileMdload = frontmatter.load(filepath)
        metadata = fileMdload.metadata
    except:
        print("Oops!  Parse "+ filepath  +" file error.  Please check if the format is correct, and do not use tab symbols in metadata...")
    
    content = frontmatter.load(filepath).content
    # print(content)
    # print(post.keys(), 'keys')
    # 內容標籤值與設定值(語系)是否存在
    langname = []
    for lang in soup.find_all(tag):
        for name in setlang:
            if lang.get(attrname) == name:
                langname.append(name)
    lang_content = {}
    if not langname:
        # empty lang tag
        lang_content = {default_lang: content}

    else:
        for value in langname:
            now_lag_index = langname.index(value)
            finds = soup.find(tag, {attrname: value}).prettify()
            now_lang_tag = finds.replace('\n', '')
            # print(content)
            # re.search(r'^<a name=[\"|']zh-cn[\"|']>[\s\S]</a>'',content)
            now_lang_index = content.find(now_lang_tag) + len(now_lang_tag)
            # print(now_lang_index)
            if now_lag_index + 1 < len(langname):
                next_lang = langname[now_lag_index + 1]
                next_lang_tag = soup.find(tag, {
                    attrname: next_lang
                }).prettify().replace('\n', '')
                next_lang_index = content.find(next_lang_tag)
                lang_content[value] = content[now_lang_index:next_lang_index]
            else:
                lang_content[value] = content[now_lang_index:len(content)]

    # print(lang_content)

    article_lang = {}
    if not langname:
        article_lang[default_lang] = setlangFile(
            metadata, default_lang, lang_content)
    else:
        for value in langname:
            article_lang[value] = setlangFile(metadata, value, lang_content)
    return article_lang


def resetLangfMeta(article_lang, key, lang, job_lang):
    metadatas = yaml.load(
        article_lang[key][0].replace("---", ""), Loader=yaml.FullLoader)

    lang_metadata = [
        '---',
        'layout: ' + metadatas['layout'],
        'title: ' + metadatas['title'],
        'lang: ' + lang,
        'description: ' + metadatas['description'],
        '---\n\n'
    ]
    story = '\n'.join(lang_metadata)
    job_form_url = job_form["job_form_url_"+job_lang]
    article = article_lang[key][1].replace("job_form_url", job_form_url)
    return story+article


def creatFiles(article_lang, path, filename, falias):
    """
    Args:
        article_lang:  標籤參數如語系區分的資料
            {
                'zh-tw': [string, string],
                'zh-cn': [string, string],
                'zh-tw': [string, string]
            }
        path: 輸入相對檔案路徑 "/index.md"
        filename: 輸出的資料名稱
        fname: 輸出的資料夾主別名目綠 "_pages"
    """
    # if filename == "product.md":
    #     print(article_lang)
    for key in setlang:
        """
        如果指定目錄不存在就建立目錄
        要不然的話就直接開檔案
        """
        _path = "./" + falias + "/" + key + "/" + path
        filepath = os.path.join(_path, filename)
        # if filepath == './_pages/en/\engineering/amp.md':
        print("creat file to ===>'" + filepath + "'")

        if not os.path.isdir(_path):
            os.makedirs(_path)
        with open(filepath, "w", encoding="utf-8") as fp:
            if key in article_lang.keys():  # [tw ,cn]
                # print("setlang1:"+key)
                fp.write(resetLangfMeta(
                    article_lang, key, key, key))
            else:
                if key == default_lang:
                    # print("setlang2:"+key)
                    # default en
                    # no default lang tag <a name="en"/>
                    # use next lang content to default lang.md
                    for key2 in setlang:  # [en,tw,cn]
                        # print("setlang:"+key2)
                        if key2 in article_lang.keys():  # [tw ,cn]
                            fp.write(resetLangfMeta(
                                article_lang, key2, default_lang, default_lang))
                            break

                else:
                    # no article_lang key. Set default lang content to this file.md
                    if key in article_lang.keys():
                        # print("setlang3:"+key)
                        fp.write(resetLangfMeta(
                            article_lang, default_lang, key, default_lang))
                    else:
                        # print("setlang4:"+key)
                        # no default lang <a name="en"> and no lang article_lang key
                        # [en,tw,cn] find next lang set to defaut lang
                        for key2 in setlang:
                            # print("setlang:"+key2)
                            if key2 in article_lang.keys():  # [tw ,cn]
                                # print("setlang4:"+key2)
                                fp.write(resetLangfMeta(
                                    article_lang, key2, key, default_lang))

                                break


print("Find the data directory============================================>")
if not os.path.isdir("./"+falias):  # not _page folder mkdir
    os.makedirs("./"+falias)
# walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
allList = os.walk(mainPath)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList:
    #   列出目前讀取到的路徑
    # print("path：", root)
    #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
    # print("directory：", dirs)
    #   列出在這個路徑下讀取到的所有檔案
    # print("files：", files)

    for i in files:
        if os.path.splitext(root + '/' + i)[-1] == '.md':
            filepath = os.path.join(root, i)
            filename = i

            path = root.replace(mainPath+'/', "") if root != mainPath else ""
            
            article_lang = rfileDate(filepath, setlang, tag, attrname)

            creatFiles(article_lang, path, filename, falias)
# 首頁預設語系
# 檢查的檔案
print("move files to _defalut (website defalut lang pages)==================================================>")
# rmtree('./_default')
df_filepath = "./" + falias + "/" + default_lang
allList_page = os.walk(df_filepath)
# 列出所有子目錄與子目錄底下所有的檔案
for root, dirs, files in allList_page:
    for i in files:
        if os.path.splitext(os.path.join(root, i))[-1] == '.md':
            this_file = os.path.join(root, i)
            # print("root:"+root)
            # print(root.replace(
            #     df_filepath, "./_default/"))
            move_path = root.replace(
                df_filepath, "./_default") if root == df_filepath else root.replace(df_filepath, "./_default")
            move_file = os.path.join(
                move_path, i) if move_path != "./_default/" else "./_default/"+i
            # print("this_file:"+this_file)
            # print("move_path:"+move_path)
            print(this_file+" ===move_file===> "+move_file)
            if not os.path.isdir(move_path):
                os.makedirs(move_path)
            copyfile(this_file, move_file)

print("Completed successfully!============================================================>")
