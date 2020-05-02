import aiohttp
import asyncio
import sys


async def fetch(url, json):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json) as response:
            await asyncio.sleep(1)
            text = await response.text()
            code = int(text[0])
            text = text[1:]
            print(text)
            sys.exit(code)
            return code

if __name__ == '__main__':
    cmd = sys.argv[1]
    text = ''
    while True:
        try:
            s = input()
            text += s + '\n'
        except EOFError as e:
            break

    loop = asyncio.get_event_loop()
    #loop.run_until_complete(fetch('http://localhost:8080/', json={'str_inp': text, 'cmd': cmd}))
    loop.run_until_complete(fetch('http://3.249.45.70:8080/', json={'str_inp': text, 'cmd': cmd}))
