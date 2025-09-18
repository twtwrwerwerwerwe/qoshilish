# auto_join.py
# Telethon orqali ko‘p guruh/kanallarga qo‘shilish
# Python 3.7+
import asyncio
import time
from telethon import TelegramClient, errors, functions, types

# --- API MA'LUMOTLARI ---
api_id = 28197641   # o'zingizniki bilan almashtiring
api_hash = "690af6f573241c8d2b0bf468ca2b9d89"  # o'zingizniki bilan almashtiring
session_name = "join_session"

# --- LINKLAR VA ID'LAR RO'YXATI ---
links = [
    "https://t.me/Toshkent_bogdod_buvayda_taksi",
    "https://t.me/buvayda_toshkent_buvayda_taxi",
    "https://t.me/buvayda_toshkentttt",
    "https://t.me/bagdod_toshken",
    "https://t.me/toshkent_uyrat_dormancha",
    "https://t.me/Buvayda_Bogdod_Toshkent",
    "https://t.me/Bogdod_toshkent_rishton_taxil",
    "https://t.me/bagdod_rishton_qoqon_toshkent",
    "https://t.me/buvayda_toshkent_taksi2",
    "https://t.me/BUVAYDA_YANGIQORGON_Toshkentt",
    "https://t.me/rishton_bogdod_toshken_taxi",
    "https://t.me/buvayda_toshkent_rishton",
    "https://t.me/toshkenbogdodd",
    "https://t.me/rishton_toshkent_taksil",
    "https://t.me/Bogdod_toshkent_yangiqorgonbuvay",
    "https://t.me/Toshkent_Bogdod_Toshken",
    "https://t.me/toshkentrishtonbagdod",
    "https://t.me/bagdod_rishton_toshkent_qoqon",
    "https://t.me/RishtonGa",
    "https://t.me/Toshkent_Bagdod_toshken",
    "https://t.me/buvayda_bogdod_rishton_toshkend1",
    "https://t.me/Toshkent_zodyon_beshkapa",
    "https://t.me/toshkent_buvayda_bagdodd",
    "https://t.me/buvayda_toshkent_bogdod_toshkent",
    "https://t.me/Rishton_Buvayda_Toshkent_Bogdodi",
    "https://t.me/bagdod_toshkent_ta",
    "https://t.me/toshkent_rishton_taxi",
    "https://t.me/Rishton_Buvayda_Toshkent_Bogdod",
    "https://t.me/bogdod_toshkent_shafyorlar",
    "https://t.me/rishton_toshkent_bogdod_n1",
    "https://t.me/Toshkent_Rishton",
    "https://t.me/rishron_toshkent_rishton",
    "https://t.me/toshkent_bogdod_toshkent_taksi",
    "https://t.me/rishton_toshkent_bogdod_1",
    "https://t.me/Rishton_bogdodToshkent",
    "https://t.me/bagdod_buvayda0",
    "https://t.me/taxi_bogdod_toshken",
    "https://t.me/bagdod_toshkent_t",
    "https://t.me/toshkent_rishtonn",
    "https://t.me/Toshkent_Fargona_taxis",
    "https://t.me/sox_rishton",
    "1910120507",
    "https://t.me/toshkent_bogdod_rishton_buvayd",
    "2257001893",
    "https://t.me/RishtonBagdodToshkent",
    "https://t.me/RishtonToshkenttaxiii",
    "https://t.me/Rishton_Toshkent_Bogdod_Taksi_01",
    "https://t.me/Rishton_Toshkent_Rishton",
    "https://t.me/Toshkent_Rishton24",
    "https://t.me/RishtanTashkent",
    "2926180929",
    "3092807710",
    "4851400129",
    "https://t.me/Rishton_Bogdod_Toshkent_taksii",
    "https://t.me/Rishton_Toshkent2",
    "https://t.me/Rishton_Toshkent_taksii",
    "https://t.me/Vodiy_Toshkent_taxi_xizmatiN1",
    "https://t.me/TOSHKENT_RISHTON_TAXI_745",
    "https://t.me/rishton_toshkent_1",
    "1673082649",
    "https://t.me/taxichen",
    "https://t.me/Bogdodtoshkenttaksi1",
    "2335396180",
    "https://t.me/rishton_toshkent_24",
    "https://t.me/Rishton_Toshkent",
    "https://t.me/Toshkent_Rishton_258",
    "https://t.me/pitagkr",
    "https://t.me/ToshkentRishtonTaxi",
    "https://t.me/zohidontoshkent",
    "1373629932",
    "4928526140",
    "4659544802",
    "https://t.me/toshkent_bogdod_buvayda_taxi",
    "https://t.me/rishton_taxi_toshkent",
    "https://t.me/rishton_toshkent_bogdod_1234",
    "https://t.me/rishton_toshkent_bogdod_taxi_12"
]

# --- Qo‘shilish funksiyasi ---
async def join_groups():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    for item in links:
        try:
            if str(item).startswith("http"):
                entity = await client.get_entity(item)
            else:
                entity = types.PeerChannel(int(item))

            await client(functions.channels.JoinChannelRequest(entity))
            print(f"✅ Qo‘shildi: {item}")

        except errors.UserAlreadyParticipantError:
            print(f"♻️ Oldin qo‘shilgan: {item}")

        except errors.FloodWaitError as e:
            print(f"⏳ Limit: {e.seconds} soniya kutish kerak ({item})")
            time.sleep(e.seconds + 5)
            continue

        except Exception as ex:
            print(f"❌ Xato: {item} — {ex}")

        await asyncio.sleep(5)

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(join_groups())
