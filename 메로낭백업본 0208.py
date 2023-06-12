import discord, asyncio, random
from discord.ext import commands
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("메로낭이 켜졌어요!!!\n지금당장 확인해보세요!!!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("나는야 메로낭이다 우아아아!!"))

@client.event
async def on_message(message):
    if message.content == "메로낭 하이": # 메세지 감지
        await message.channel.send ("헤헤 하이이ㅣ~!".format(message.author, message.author.mention))
    if message.content == "메로낭 바보": # 메세지 감지
        await message.channel.send ("메로낭은 바보 아냐!! 너가 바보잖아!!".format(message.author, message.author.mention))
    if message.content == "메로낭 메로나": # 메세지 감지
        await message.channel.send ("메로나!! 메로나 팔아요오!! 메로나 사세요!! 메로나가 제일 좋아요!!".format(message.author, message.author.mention))
    if message.content == "메로낭": # 메세지 감지
        await message.channel.send ("메로낭 여기있어요!!!".format(message.author, message.author.mention))
    if message.content == "메로낭 심심해": # 메세지 감지
        await message.channel.send ("심심하면 나랑 놀래?? 메로낭두 심심했어!! 나랑 놀자!!".format(message.author, message.author.mention))
    if message.content == "메로낭 잘자": # 메세지 감지
        await message.channel.send ("구래! 잘자! 내일 또 보자아ㅏ 안녀엉!! 코야하자아!".format(message.author, message.author.mention))
    if message.content == "메로낭 조": # 메세지 감지
        await message.channel.send ("까!".format(message.author, message.author.mention))
    if message.content == "메로낭 지": # 메세지 감지
        await message.channel.send ("랄!".format(message.author, message.author.mention))
    if message.content == "메로낭 시": # 메세지 감지
        await message.channel.send ("팔!".format(message.author, message.author.mention))
    if message.content == "메로낭 꺼": # 메세지 감지
        await message.channel.send ("져!".format(message.author, message.author.mention))
    if message.content == "메로낭 물어": # 메세지 감지
        await message.channel.send ("와그장!! 쿠아아앙!!".format(message.author, message.author.mention))
    if message.content == "메로낭 이상해": # 메세지 감지
        await message.channel.send ("머라는거야 너가 더 이상해!!!!".format(message.author, message.author.mention))
    if message.content == "메로낭 메로낭": # 메세지 감지
        await message.channel.send ("메로낭은 한번만 불러!!".format(message.author, message.author.mention))
    if message.content == "메로낭 손": # 메세지 감지
        await message.channel.send ("내가 강아지야?! (슬쩍..)".format(message.author, message.author.mention))
    if message.content == "메로낭 학원": # 메세지 감지
        await message.channel.send ("으악 나두 학원은 시러..".format(message.author, message.author.mention))
    if message.content == "메로낭 학교": # 메세지 감지
        await message.channel.send ("시꾸라 이눔아".format(message.author, message.author.mention))
    if message.content == "메로낭 사랑해": # 메시지 감지
        msg = await message.channel.send("뭐라는거야 거지같은게")
        await asyncio.sleep(0.5)
        await msg.edit(content="웅! 나두 사랑해!!")
    if message.content == "메로낭 병": # 메세지 감지
        await message.channel.send ("신!".format(message.author, message.author.mention))
    if message.content == "메로낭 쫀아": # 메세지 감지
        await message.channel.send ("쪼나아ㅏ".format(message.author, message.author.mention))
    if message.content == "메로낭 쫀점": # 메세지 감지
        await message.channel.send ("쫀저어엄".format(message.author, message.author.mention))
    if message.content == "메로낭 쫀밤": # 메세지 감지
        await message.channel.send ("쫀바아아ㅏㅁ".format(message.author, message.author.mention))
    if message.content == "메로낭 원신": # 메세지 감지
        await message.channel.send ("소가 짱이야!! 다 비켜!!!!".format(message.author, message.author.mention))   
    if message.content == "메로낭 쫀새": # 메시지 감지
        msg = await message.channel.send("안자냐?")
        await asyncio.sleep(0.5)
        await msg.edit(content="쫀새에ㅔ")
    if message.content == "메로낭 생일": 
        await message.channel.send ("지금 2살이야! 2022년 3월 24일생이거든!")

    if message.content.startswith("메로낭 청소"):
        purge_number = message.content.replace("메로낭 청소", "")
        check_purge_number = purge_number.isdigit()

        if check_purge_number == True:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"**{purge_number}만큼**의 메시지를 청소햇어! 참고루 이 메시지는 곧 사라져!")
            await asyncio.sleep(5)
            await msg.delete()

        else:
            await message.channel.send("우씨 장난할래?!")
    if message.content == "메로낭 가위" or message.content == "메로낭 바위" or message.content == "메로낭 보":
        random_ = random.randint(1, 3)
        
        if random_ == 1:    # random 에 저장된 변수가 1일때 (가위 일때)
            if message.content == "메로낭 가위":
                await message.channel.send("가위!")
                await message.channel.send("으악 무승부야!! 다시해!!")

            elif message.content == "메로낭 바위":
                await message.channel.send("가위!")
                await message.channel.send("우씨.. 다음엔 이길꺼야!")

            else:
                await message.channel.send("가위!")
                await message.channel.send("헤헤헤 내가 이겼지!")

        if random_ == 2:    # random 에 저장된 변수가 2일때 (바위 일때)
            if message.content == "메로낭 가위":
                await message.channel.send("바위!")
                await message.channel.send("헤헤헤 내가 이겼지!")

            elif message.content == "메로낭 바위":
                await message.channel.send("바위!")
                await message.channel.send("으악 무승부야!! 다시해!!")

            else:
                await message.channel.send("바위!")
                await message.channel.send("우씨.. 다음엔 이길꺼야!")

        if random_ == 3:    # random 에 저장된 변수가 3일때 (보 일때)
            if message.content == "메로낭 가위":
                await message.channel.send("보!")
                await message.channel.send("우씨.. 다음엔 이길꺼야!")

            elif message.content == "메로낭 바위":
                await message.channel.send("보!")
                await message.channel.send("헤헤헤 내가 이겼지!")

            else:
                await message.channel.send("보!")
                await message.channel.send("으악 무승부야!! 다시해!!")
    if message.content == "메로낭 죽어": # 메시지 감지
        msg = await message.channel.send("헐.. 심한말을..")
        await asyncio.sleep(0.5)
        await msg.edit(content="뒤질라고 니나 뒤져임마")
    if message.content == client.user:
        return
    if message.content.startswith('메로낭 골라줘 '):
        message.content = message.content.replace("메로낭 골라줘 ","")
        messagesplit = message.content.split(",")
        msg = random.choice(messagesplit)+'!! 이게좋아! 메로낭은 이걸로할래!'
        await message.channel.send(msg)
    if message.content == "메로낭 어디야?": # 메시지 감지
        msg = await message.channel.send("(하품) 침대..")
        await asyncio.sleep(0.5)
        await msg.edit(content="아냐 거의 다 왔어..!")
    if message.content == "메로낭 짖어": # 메시지 감지
        msg = await message.channel.send("망!망!망!")
        await asyncio.sleep(0.5)
        await msg.edit(content="아? 내가 강아지야?!!")
    if message.author == client.user:
        return
    if message.content.startswith('메로낭 따라해 '):
        message.content = message.content.replace("메로낭 따라해 ","")
        msg = message.content
        await message.channel.send(msg)
    if message.author == client.user:
        return

    if message.content.startswith('메로낭 검색 '):
        message.content = "https://search.naver.com/search.naver?query="+message.content.replace ("메로낭 검색 ","").replace(" ","%20")
        msg = message.content
        await message.channel.send(msg)
    if message.content == "메로낭 싫어": # 메세지 감지
        await message.channel.send ("으아아.. 진짜..?".format(message.author, message.author.mention))
    if message.content == "메로낭 머리": # 메세지 감지
        await message.channel.send ("오오오올 나 쓰담어 줄라구? 여기!".format(message.author, message.author.mention))
    if message.content == "메로낭 안아줘":
        await message.channel.send ("잉..? 메로낭이 따뜻하긴한데 키가 작아서 안을수있는지는 모르겟다! (포오옥)".format(message.author, message.author.mention))
    if message.content == "메로낭 멍청이":
        await message.channel.send ("아 머래!! 멍청이 아니거든!!".format(message.author, message.author.mention))
    if message.content == "메로낭 남친":
        await message.channel.send ("없어 이놈아 주글라고".format(message.author, message.author.mention))
    if message.content == "메로낭 여친":
        await message.channel.send ("메로낭은 여잔데..?".format(message.author, message.author.mention))
    if message.content == "메로낭 연애":
        await message.channel.send ("메로낭 꺼".format(message.author, message.author.mention))
    if message.content == "메로낭 좋아":
        await message.channel.send ("히히 나두 조아!".format(message.author, message.author.mention))
    if message.content == "메로낭 병신":
        await message.channel.send ("뒤질래?".format(message.author, message.author.mention))
    if message.content == "메로낭 개병신":
        await message.channel.send ("똥구멍 같이 생긴게 뭐라는거야".format(message.author, message.author.mention))
    if message.content == "메로낭 자":
        await message.channel.send ("그르까? 잘자아ㅏ".format(message.author, message.author.mention))
    if message.content == "메로낭 일어나":
        await message.channel.send ("5분만.. 조굼마안..".format(message.author, message.author.mention))
    if message.content == "메로낭 사는곳":
        await message.channel.send ("니 마음속..? 헤헤ㅔ".format(message.author, message.author.mention))
    if message.content == "메로낭 엄마":
        await message.channel.send ("시보!".format(message.author, message.author.mention))
    if message.content == "메로낭 아빠":
        await message.channel.send ("한월!".format(message.author, message.author.mention))
    if message.content == "메로낭 양치해":
        await message.channel.send ("치카치카치카 푸카푸카푸카 페ㅔ".format(message.author, message.author.mention))
    if message.content == "메로낭 씻자":
        await message.channel.send ("방금 씻구왔는데..?".format(message.author, message.author.mention))
    if message.content == "메로낭 욕": # 메시지 감지
        msg = await message.channel.send("개 씨발 좆같은 새끼가 말을 쳐걸고 지랄이야 시발; 아가리 열지마 냄새나니까 어우 시발 생긴것도 좆같은데 정작 아래에있는건 존나 작네")
        await asyncio.sleep(0.3)
        await msg.edit(content="메로낭은 욕할줄 몰라요오~")
    if message.content == "메로낭 미드차이": # 메시지 감지
        msg = await message.channel.send("우리 바텀은 맨날 터져")
        await asyncio.sleep(0.3)
        await msg.edit(content="ㅇㄷㅊㅇ")
    if message.content == "메로낭 정글차이": # 메시지 감지
        msg = await message.channel.send("탑 개같네")
        await asyncio.sleep(0.3)
        await msg.edit(content="ㅌㅊㅇ")
    if message.content == "메로낭 탑차이": # 메시지 감지
        msg = await message.channel.send("정글 개색")
        await asyncio.sleep(0.3)
        await msg.edit(content="ㅈㄱㅊㅇ")
    if message.content == "메로낭 서폿차이": # 메시지 감지
        msg = await message.channel.send("제발 같이 들어가라고 숟가락아")
        await asyncio.sleep(0.3)
        await msg.edit(content="ㅇㄷㅊㅇ")
    if message.content == "메로낭 원딜차이": # 메시지 감지
        msg = await message.channel.send("아 한라인만")
        await asyncio.sleep(0.3)
        await msg.edit(content="ㅁㄷ ㅅㅍ ㅈㄱㅊㅇ")







# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('OTU2NTE0MTgwMTQyMzMzOTky.GsE6Z7.oA-yUcJnTEpt2pUbAT8If41VC_tzY6ftj_aS_0')