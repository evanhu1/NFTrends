import tweepy
import requests
import json

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAG9QVAEAAAAAcRh%2FeO02pG2M4s8RIvtlPgM6lp0%3D6nwkftkEKO76N6FnLW2rclYJULiB9HWjoOjvVw6Se0vQ9BqRql')

top30names = ["Doodles", "CryptoPunks", "Bored Ape Yacht Club", "JUNGLE FREAKS BY TROSLEY", "Kaiju Kingz", "Party Ape | Billionaire Club", "Boonji Project", "CrypToadz by GREMPLIN", "MekaVerse", "HeadDAO", "Party Degenerates", "Cool Cats NFT", "Mutant Ape Yacht Club", "Revenants by Alethea AI", "Metasaurs by Dr. DMT", "iNFT Personality Pod Sale", "MutantCats", "ALPACADABRAZ", "CyberKongz", "THE SHIBOSHIS", "Creature World NFT", "CreatureToadz", "ASM AIFA Genesis", "The Doge Pound", "Parallel Alpha", "DOGESOUNDCLUB MATES", "GalacticApes", "Bears Deluxe", "OG:Crystals", "HalloweenBears"]
top30urls = ["https://lh3.googleusercontent.com/7B0qai02OdHA8P_EOVK672qUliyjQdQDGNrACxs7WnTgZAkJa_wWURnIFKeOh5VTf8cfTqW3wQpozGedaC9mteKphEOtztls02RlWQ=s130",  "https://lh3.googleusercontent.com/BdxvLseXcfl57BiuQcQYdJ64v-aI8din7WPk0Pgo3qQFhAUH-B6i-dCqqc_mCkRIzULmwzwecnohLhrcH8A9mpWIZqA7ygc52Sr81hE=s130",  "https://lh3.googleusercontent.com/Ju9CkWtV-1Okvf45wo8UctR-M9He2PjILP0oOvxE89AyiPPGtrR3gysu1Zgy0hjd2xKIgjJJtWIc0ybj4Vd7wv8t3pxDGHoJBzDB=s100”, “https://lh3.googleusercontent.com/9ElHIcK8dZ3fOxLLVA1KKNuN7AVmNvFycX4jK3f_GvDhTrkCgh4hBJAiXGf8UsBSWlJU9lpSrtPtCfNHDp08ChZ7Tx_LDXbiT65t=s100", "https://lh3.googleusercontent.com/bQvXzE_Pn8SwA-xqlfhFKDRi_0QZn9uXDYkQ-E7-C-B6KXkg4-GkQuBOjanhLBqURzkdkEL7XbFrUz6ICD1l02TgN_2IB4HtHpAL=s100", "https://lh3.googleusercontent.com/XuNPbnt2IMjSrzmTEd8aZZyJRh2KQr2kauOB0IlvCcoPPzS7vSLvYzbDzVDFZS5M7aMIjyJ5FSf1zO8Y5k3NZvrLu4cqoWjlMAxe=s100", "https://lh3.googleusercontent.com/M5eV3dgE01GIJbt7VZ-Vx4B2Xo42RaFXGT3R-ynrwmrqDEAoq1MacTZlRgYuSPHk6jD73X1l18H5CIg0ZPy7xUSA-p_1GsSWQT9cLuQ=s100", "https://lh3.googleusercontent.com/iofetZEyiEIGcNyJKpbOafb_efJyeo7QOYnTog8qcQJhqoBU-Vu9l3lXidZhXOAdu6dj4fzWW6BZDU5vLseC-K03rMMu-_j2LvwcbHo=s100", "https://lh3.googleusercontent.com/6CS0frnjPEpvJ8hE3OG6_TbJFEC5YYThnZMdLTTmW-Z91lyYAJkPA7-ou2uE-b_J-cBUBeqWkI4HYKHEiu2PAyCT6wkYKzoeCyuy=s100", "https://lh3.googleusercontent.com/JRXwsJJ0RexPHPd1jQf88efrIsepmn6URx9GyTGd9pba6S-7xJj3fXh5uIdeKjbi2AkBS-8Gsp1gU-LKIOhfi8Z3zYH894bN0yofxhk=s100", "https://lh3.googleusercontent.com/wSM3rM8ayMBVChhgqvpcYif28chYOToZ-CasN0MEG1RekrH-PQ0g2xerw8IvHBMIsgzR8VqGW_YtX_w_LfDTY7SpTf74x4iRexjr=s100", "https://lh3.googleusercontent.com/LIov33kogXOK4XZd2ESj29sqm_Hww5JSdO7AFn5wjt8xgnJJ0UpNV9yITqxra3s_LMEW1AnnrgOVB_hDpjJRA1uF4skI5Sdi_9rULi8=s100", "https://lh3.googleusercontent.com/lHexKRMpw-aoSyB1WdFBff5yfANLReFxHzt1DOj_sg7mS14yARpuvYcUtsyyx-Nkpk6WTcUPFoG53VnLJezYi8hAs0OxNZwlw6Y-dmI=s100", "https://lh3.googleusercontent.com/0LsJSNxzhiXQ-8TqwrMEJZuLgQnDTEweihqp32L_dXpkywpCIK4o8Fgs9JZDduK1Oj5Ek_xlBqd5lMIJoxSnWRi-GaknxnHINmy2H7Y=s100", "https://lh3.googleusercontent.com/xvqA-v_fQM5TE3CmJIpSTdFu4cmTeVpwRWeuLf4VdTBW0_ji9K91BirQWcshvGqlCAyMSwrrp8e-JSLp5YUHErAak0l3kXYBOdKfQak=s100", "https://lh3.googleusercontent.com/0LsJSNxzhiXQ-8TqwrMEJZuLgQnDTEweihqp32L_dXpkywpCIK4o8Fgs9JZDduK1Oj5Ek_xlBqd5lMIJoxSnWRi-GaknxnHINmy2H7Y=s100", "https://lh3.googleusercontent.com/Cg3lUE2P3X7MhSKMROVOjvHkeNw_IWvH8aEyyK3hi9Rxh9d4eyxR6u7KEwRcpBKYq00WPjyYRdyyIdal8TOvsAZfYbeH8IfoZRUw=s100", "https://lh3.googleusercontent.com/wB2-qmC6w8Yc825fyDxaWkbNrhCNprGtJZOdNuigC1XiA0gMHcPxt-Dbr5iYzdu8_2252MdyuDk5JcOG-tQWNLHvdRaRgICf2H988A=s100", "https://lh3.googleusercontent.com/LIpf9z6Ux8uxn69auBME9FCTXpXqSYFo8ZLO1GaM8T7S3hiKScHaClXe0ZdhTv5br6FE2g5i-J5SobhKFsYfe6CIMCv-UfnrlYFWOM4=s100", "https://lh3.googleusercontent.com/9G_SbzGpWnId_ouP-rsTfv1UIeSaaayelyZVyo7eVETYp2uDXDXeH82Yvw4AchRHuKSrixHhGQ7ri5UUepQLaK9BpwhMH1yjImnXHA=s100", "https://lh3.googleusercontent.com/PkMdNUr4UsEq5RLvAm721Ja5QGAijunAVDMz0hfRuyHQn853TRQzKL4aTFBgWPoy-nWlYA3hXzAm7flCmKn7Z9p2HN0GJxAtAixB4g=s100", "https://lh3.googleusercontent.com/wvlGZLaD6Pl1FozAi0ih4wkMW9vn_72VDrfvZk3h48kNSOdY-CynzrWRHJfuBS7CTi0wGc_sxr9kp-_DWbhpGzmaAX7ZQLtXjJ5-8g=s100", "https://lh3.googleusercontent.com/1zBGv7flcBW0Kh8lRdJlZxmiP6F7hPel2XHVFGJDytrz4IBveQPR7B6DSrGMSkxCw1LErUWYVAOPUIvgVDaUOzEcaoEpx9BOpOE98NE=s100", "https://lh3.googleusercontent.com/uNkBbVvg7wyRjspsooFtYYbRHFHFISntxwijLRskjGhplP8A3Iz_4ApLU_yLp9BW-Ai0yUWC50A138IGUkII55QWRT7g12qmSRTlbA=s100", "https://lh3.googleusercontent.com/nxaymgd9aJIzLXb0r3oLO0VCMFi0Zex1ubTmEYekEKwOVq1YijOULDeT1qCjk71OTsQW47zmvZ2ZuycXorgu6WA6Wosc6CiOuVnAXGk=s100", "https://lh3.googleusercontent.com/y4VVdjizSv0nw5k9QUCiXxPAjaZ7qT2ueXYXgzMe5X2KZz5cd1s-8l7sNM3E6uRLIEcdOC9UYHgKHbp-t3N_lcuZcCB-YG4V9N65ww=s100", "https://lh3.googleusercontent.com/fy46-MlNjZMR1NCTNAgmh9e97SNffpSBkwd0HpL9XTBfRt6-GvjTytWHoN9Pzmbw83TbRzo8nGgZ32QbVVMYnrmBb2vM6_6_3yXv=s100", "https://lh3.googleusercontent.com/InPgClcuGiNA5TdEGTu7zuGSv1LDJ54L_sC49G7fqJ0YawDcdmN78t7iShcrbyQ_sdoUyjyBAoXVMTKaaf9OP8ekDyBaEEWJMiDbi8M=s100", "https://lh3.googleusercontent.com/PaM_tFDNK4SBoo73VtX2mjqtb5pG1jbcioMW2CUntcFbY8aA1l1vhAKOn7jYlykkuk7JLCZFvPo7vbiN7xotzQUYab18i4tl1Wk3_A=s100", "https://lh3.googleusercontent.com/L6kw5mCsBs3iXQ9noufMDh4VBmrig73VyguCLkz6T-mc6MbqOMs8MeNpTSg71IBqkjWoYZpYagNQM2yn2yqGOtFRd7FW6-2yWkAk3H4=s100"]
top30descriptions = ["A community-driven collectibles project featuring art by Burnt Toast. Doodles come in a joyful range of colors, traits and sizes with a collection size of 10,000. Each Doodle allows its owner to vote for experiences and activations paid for by the Doodles Community Treasury.", "CryptoPunks launched as a fixed set of 10,000 items in mid-2017 and became one of the inspirations for the ERC-721 standard. They have been featured in places like The New York Times, Christie’s of London, Art|Basel Miami, and The PBS NewsHour.", "The Bored Ape Yacht Club is a collection of 10,000 unique Bored Ape NFTs— unique digital collectibles living on the Ethereum blockchain. Your Bored Ape doubles as your Yacht Club membership card, and grants access to members-only benefits, the first of which is access to THE BATHROOM, a collaborative graffiti board. Future areas and perks can be unlocked by the community through roadmap activation. Visit www.BoredApeYachtClub.com for more details.", "Jungle Freaks is a collection of 100% HAND DRAWN FREAKS by legendary Hustler Mag Cartoonist George Trosley. These 10,000 Freaks live and breathe on the Ethereum blockchain.\nThe year is 2077, humanity is gone and the zombies have overrun the cities and seized a lot of the military stockpiles. However, they didn’t count on the genetically enhanced ferocity and cunning traits of the gorilla regime. The Gorilla oasis stronghold is under attack but they will never surrender.", "3,333 Genesis Kaiju Kingz created by Augminted Labs to protect the metaverse. The community is all about growth and providing a place for the future of web3 to learn, build, and conquer. Join the Kingz and live forever as a legend. 6666 babies to accompany them.", "The BILLIONAIRE CLUB is a private collection of 10 000 billionaire apes NFTs—unique digital collectibles. Earlier this year, a mysterious force coming from another galaxy summoned the most influential people on planet Earth to a secret party. Acquiring one of them will give you access to an ever-growing community of investors and entrepreneurs.", "Boonji Project, launched on the Ethereum blockchain, is a collection of unique digital non-fungible tokens created by world-renowned artist Brendan Murphy. Your Boonji Avatar NFT not only serves as a piece of collectible digital artwork, but also as a passport that allows you to travel through an unexplored galaxy with the Boonji Spaceman.", "CrypToadz are a collection 6969 small amphibious creatures trying to escape the tyrannical rule of the Evil King Gremplin. Created by Gremplin, with a small bit of help from his friends.", "The MekaVerse is a collection of 8,888 generative Mekas inspired by the Japanese Anime universe.\nIn the distant future, drivers fight in a world divided into 4 Factions. Originals Meka, Mirage, F9, and Gadians are the Titans who rule this planet. Which Faction are you going to join?", "10,000 nouns needing head on the Ethereum blockchain. Each Head grants access to the exclusive DAO community and voting rights over the DAO's assets.", "Party Degenerates are a collection of 10,000 NFTs representing the rebellious spirit of those who choose to celebrate life, rather than merely living it.\nThey are professional misfits, have a big heart, like to party, and are crazy enough to think they can change the world. They have flown under the radar, searching for like-minded creatives, artists, musicians, builders, and believers who dare to express their truth in a society that increasingly values rules and conformity.", "Cool Cats is a collection of 9,999 randomly generated and stylistically curated NFTs that exist on the Ethereum Blockchain. Cool Cat holders can participate in exclusive events such as NFT claims, raffles, community giveaways, and more. Remember, all cats are cool, but some are cooler than others.", "The MUTANT APE YACHT CLUB is a collection of up to 20,000 Mutant Apes that can only be created by exposing an existing Bored Ape to a vial of MUTANT SERUM or by minting a Mutant Ape in the public sale.", "One hundred intelligent NFTs (iNFTs), depicting historical and cultural icons, reborn. From Nikola Tesla to Napoleon to Cleopatra, the world’s greatest minds are now brought to life as Intelligent NFTs. iNFTs are a powerful new medium that not only seek to advance the utilities of NFTs but also unlock new economic, creative, and social possibilities. The Revenants are the first iNFTs on Noah’s Ark, an Intelligent Metaverse created by Alethea AI.", "Metasaurs by Dr. DMT is a collection of 9,999 unique Metasaurs living on the Ethereum blockchain, this time, forever...", "A Personality Pod enables you to power your NFT with AI, turning it into an intelligent NFT (iNFT). Once your NFT is fused with a Pod, you can not only create a unique, on-chain and evolving AI-generated personality for your NFT, but also offer powerful AI Services within the world’s first Intelligent Metaverse: Noah’s Ark.", "9,999 cats mutated by a disease on the Ethereum blockchain. Each Mutant Cat grants access to the exclusive DAO community and voting rights over the DAO's assets. OWNER COUNT: Currently, the owners statistic shown by OpenSea is inaccurate for this collection. The real number including staked Mutant Cat holders is nearly 5k.", "ALPACADABRAZ are a unique alpaca subspecies that have been living in a long undiscovered paradise. One unfortunate day, they were captured by farmers who abused the ALPACADABRAZ' special abilities. Luckily, some ALPACADABRAZ managed to escape and survive, unfortunately over 9000 ALPACADABRAZ weren’t so lucky. The living alpacas are full of animations, while the deceased alpacas are now stored as jpegs forever.", "Welcome to an alternate reality, where evolution took a different route and weird apes roam the earth. Some appear normal. Some look weird. And some are just damn cool! Every CyberKong is unique and owns randomized items with different rarities. A few are super rare and even animated! Maybe some of them look familiar!", "SHIBOSHIS are 10,000 lovable Shiba Inu generated Non Fungible Tokens (NFTS) eternally written on the Ethereum blockchain. These Shibs have varying traits that make each unique and collectible (for instance Laser Eyes or Party Hat). Furthermore, each trait corresponds to an enhancement of the base ShibaStrength of the Shiboshi in our upcoming Shiboshi Game. You’ll be able to purchase, and trade these SHIBOSHIS here and at ShibaSwap without fees. These are the official SHIBOSHIS of the Shiba Inu decentralized community as seen on Forbes, Wall St. Journal, Fortune, CNN, MSNBC and just about everywhere else. Beware of scams.", "Welcome to The Creature World. You have arrived in a nearby magical dimension of love, divine intervention, and possibility. 10,000 unique Creatures are here to guide you on this journey. Follow their lead. Created with love by NYC-based artist Danny Cole.", "CreatureToadz is the first crossover project between two independently successful NFT communities, Creatures and CrypToadz. The art was made from scratch to ensure perfect stylistic marriage between the two.", "The world's first Non-Fungible Intelligence premiere by Altered State Machine.\n10,000 unique Genesis Boxes; with 1 unique Artificial Intelligence ASM Brain and 4 unique AIFA All-Stars in each box.\nArtifical Intelligence Football Association (AIFA) is a decentralised Play-To-Earn game. Starring the genesis of intelligent NFTs, or... NFIs.\nAt the Great Unboxing, your All-Stars will emerge with random attributes. You'll have a limited one-time power to reconfigure each one! Break open your box and create your team, to your vision.\nThe ASM Genesis Brain contained in every box will be part of a platform for the creation and training of A.I. Agents, owned and traded as NFTs.", "The Doge Pound is 10,000 art pieces carefully chosen by Professor Elon. A unique digital collection of diverse NFTs lying on Ethereum Blockchain. Each one is thoughtfully designed, specifically picked, and impeccably shaped. Join us on our adventure and have a good time. Having a Doge Token grants you creative and commercial rights, as well as inclusion in the community.", "Sci-fi collectable card game with NFTs.", "Doge Sound Club is a social gathering of NFT collectors operated by governance based on NFT. MATES, which is used as a membership card and voting right of Doge Sound Club, is the first bulk avatar art in Korea and was created by a computer program. All 10,000 are different, and each has its own charm. Choose your cute avatar and use it as your KakaoTalk or Twitter profile! It will be the first step in transforming your reality into a game!", "Where it all started: Genesis", "Bears Deluxe has arrived! 6,900 (nice) algorithmically generated bears. All art drawn by hand, 24px format.", "Explore the remarkable world of Organic Growth: Crystal Reef, 10301 unique NFT collectibles that transform and grow every time they are purchased from another collector. This revolutionary digital art project is a collaboration between artists Michael Joo (ASomatica) and Danil Krivoruchko (Myshli).\nThe facets and contours of each OG:Crystal are generated algorithmically, the product of each owner’s crypto wallet history as well as myriad combinations of crystalline structures.\nTwo months after the initial sale date or seven generations of growth, every OG:Crystal will be “locked” and any new transactions will not influence shape, structure, or rarity.", "Halloween Bears are a collection of 10,000 randomly generated NFT on Ethereum Blockchain. Stealth launched on 12th of October 2021. The bears are living in a harmony through DAO, allowing its far distant cousins to seek asylum. The team will work endlessly to expand its safe haven and innovate the project features and utility. Be part of the Bears and make a difference."]
names = top30names
urls = top30urls
descriptions = top30descriptions

counts = dict()
collectionDataArray = []
tweetDataArray = []

twitterQueryCounter = 0

loop = 1
openseaLimit = 20  #300 is the max
twitterLimit = 20

for i in range(loop):
    offset = openseaLimit*i
    openseaURL = "https://api.opensea.io/api/v1/collections?offset=" + str(offset) + "&limit=" + str(openseaLimit)
    openseaAPI = requests.request("GET", openseaURL)

    text = openseaAPI.text

    collectionNames = []
    collectionURLs = []
    collectionDescriptions = []

    for i in range(len(text) - 14):
        if text[i:i+7] == "\"name\":":
            name = ""
            j = 8
            while text[i + j] != "\"":
                name += text[i + j]
                j += 1
            if len(name) < 19 or name[:19] != 'Untitled Collection':
                collectionNames.add(name)
            else:
                collectionURLs.pop()
                collectionDescriptions.pop()

        if text[i:i+12] == "\"image_url\":":
            url = ""
            j = 13
            while text[i + j] != "\"":
                url += text[i + j]
                j += 1
            collectionURLs.append(url)

        if text[i:i+14] == "\"description\":":
            description = ""
            j = 15
            if text[i + 14] != "n":
                while text[i + j] != "\"":
                    description += text[i + j]
                    j += 1
            collectionDescriptions.append(description)
            
    names += collectionNames
    urls += collectionURLs
    descriptions += collectionDescriptions

    for i in range(min(len(names), len(urls), len(descriptions))):
        if twitterQueryCounter == 450:
            break

        colData = dict()
        colData["collection_name"] = names[i]
        colData["img_url"] = urls[i]
        colData["description"] = descriptions[i]

        query = "NFT " + "\"" + names[i] + "\""

        count = 0

        for tweet in tweepy.Paginator(client.search_recent_tweets, query, tweet_fields=['created_at', 'public_metrics'], max_results=100).flatten(limit=twitterLimit):
            twtData = dict()
            twtData["collection_name"] = names[i]
            twtData["time"] = "hi"
            twtData["text"] = tweet.text
            twtData.update(tweet.public_metrics)
            tweetDataArray.append(twtData)
            count += 1
            twitterQueryCounter += 1
        if count != 0:
            counts[names[i]] = count
            collectionDataArray.append(colData)
    
    if twitterQueryCounter == 450:
        break

    names = []
    urls = []
    descriptions = []

countsURL = "http://127.0.0.1:5000"
collectionsURL = "http://127.0.0.1:5000"
dataURL = "http://127.0.0.1:5000"

requests.post(countsURL + "/api/analytic", json=json.dumps(counts))

for collection in collectionDataArray:
    requests.post(collectionsURL + "/api/nft_collections", json=json.dumps(collection))

for data in tweetDataArray:
    requests.post(dataURL + "/api/data", json=json.dumps(data))