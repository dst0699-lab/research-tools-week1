# 简单词频统计小程序
def count_words(text):
    words = text.split()
    freq = {}
    for w in words:
        w = w.strip(",.?!").lower()
        if w:
            freq[w] = freq.get(w,0)+1
    return freq

if __name__ == "__main__":
    s = "hello world hello git hello github"
    res = count_words(s)
    print("词频统计结果：")
    for k,v in res.items():
        print(k, v)
