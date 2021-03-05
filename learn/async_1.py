# coding:utf-8

import os,random,time,asyncio

async def a():
    for i in range(10):
        print(i, 'a', os.getpid())
        await asyncio.sleep(random.random() * 2)

    return 'a function'

async def b():
    for i in range(10):
        print(i, 'b', os.getpid())
        await asyncio.sleep(random.random() * 2)

    return 'b function'

async def main():
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result[0], result[1])

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
    print('parent is %s' % os.getpid())
