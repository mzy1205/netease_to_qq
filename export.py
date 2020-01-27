import json
import requests

host = 'https://music.163.com'
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '482',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '_ntes_nnid=cf2d5c750b4fc72d7b0dfe5425c8bcc5,1568892564596; _ntes_nuid=cf2d5c750b4fc72d7b0dfe5425c8bcc5; UM_distinctid=16d4948b518ce1-0a917098713177-38607501-13c680-16d4948b519c8f; __oc_uuid=560eea80-f5b3-11e9-b5b7-ddbe80cb1700; usertrack=ezq0J13NDY6ndWCgAxf0Ag==; vinfo_n_f_l_n3=99d9e963aa13bb8f.1.1.1568892564613.1568892651363.1576221409202; _iuqxldmzr_=32; WM_TID=fWrCqAYXy51BRVAAVBZ988xjKjvb3gEj; ntes_kaola_ad=1; JSESSIONID-WYYY=ZUwafG6RFNG%2BdDkrJPU6wyAei7ABmRefGVo6afrPmqg2YTzq7VqbPZ%5CnhlOY4yuKdlHamXjR9evbTSj%2BPNKX26sjjHHP%5C75ji6c0B%2FxXC%2BiEq2Mp6vZYX51vQX3wD8u%5CuHbcBqQoD2aVkh5jNJTqn1MPBbzTFwzi84hXqEpQNBAB8sPI%3A1580136225641; WM_NI=wG9pm%2FPYLo4e3FjkHg6XCmNTn7HmBeKRnIVVt%2BPvuyly8jzr0qUvh5C40jBkCHk854j4NahsmQdR18KC6tER1rFPX8NNBPxLIqH%2BfMfoD9EjAaXyTvDadTza3i5i%2BNuEeFo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1e149b4928cbbd37f86b08aa3d15a869f9fbbbb7af5b4faaef345f8a98295d62af0fea7c3b92ab599f791f02594878490b76ff19aa68ccb6df6888d8ecd60aee9888ec16f898ea2aad55eb8f5a097f873b0a7f88bf97af4af9b97eb3f81ec008bc1618198a5d9b840aaec8282eb79af8facb3b434899dfa95c85af3ae8ab1db348e928eb1fb488baf88cce547a6b18cdac86283bf989ad77e88bfacb5f96bf1b7fb8aaa46b79baba7ee37e2a3; MUSIC_U=1de27063ffb5b5080923ef177d5fd9f7f49d4df0e841c639fba0e5a5fa4b5f53ca9659a1fce7a9aeb3682e982b5507177955a739ab43dce1; __remember_me=true; __csrf=77e2b3ab8101f3bf37da55794823e804',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/user/home?id=94694187',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

playlist_uri = '/weapi/user/playlist?csrf_token='
params = {
    'params': 'mbGdRX/KuvtLKmtJCbRb9b/gx4VPwAlU1hP+r96913ayIf6UGYEtSt0dmbB41D1Hv5//S0vi7DnzyqcX4z2Md3rm0chaM1auwpKhcIeI89sy8Djk1yHbpWE6bE98A846bhfc9e7RVuj6LqaiVni53+JpR3r+frOrRQNYsuoC8V8CccQs5xFyjO4CdFugj4OBoZg2878ec2YDtMLbHDhPvOMSPOgK/IuTdCNon924PYk=',
    'encSecKey': 'c3fb7026e5ac3b756b3a51b5e9d6c707e88d69603048788646afd2457925a1476ff67f1159cf8cc697b027d3dfb68dfdbf877de464232f01877b829cb4bc3e58b4ef9541b5c8434def975d0cd8a1ff150ddef03456c99f20f7a3288f26c395a449a9e6b7bcb4c18167a32c682622460097d89ba70e2aeeafa050e4a23d1eba90'
}
playlist_res = requests.post(host + playlist_uri, params, headers=headers)
playlist = json.loads(playlist_res.text)['playlist']
