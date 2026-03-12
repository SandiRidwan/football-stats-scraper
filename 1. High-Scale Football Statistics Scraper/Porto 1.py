import os
import time
import zipfile
import io
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- DAFTAR LIGA (LENGKAP) ---
LEAGUE_URLS = [
    # Top 5 Europe
    "https://fbref.com/en/comps/9/stats/Premier-League-Stats",
    "https://fbref.com/en/comps/12/stats/La-Liga-Stats",
    "https://fbref.com/en/comps/20/stats/Bundesliga-Stats",
    "https://fbref.com/en/comps/11/stats/Serie-A-Stats",
    "https://fbref.com/en/comps/13/stats/Ligue-1-Stats",
    # Second Tier & Other Europe
    "https://fbref.com/en/comps/23/stats/Eredivisie-Stats",
    "https://fbref.com/en/comps/32/stats/Primeira-Liga-Stats",
    "https://fbref.com/en/comps/37/stats/Belgian-Pro-League-Stats",
    "https://fbref.com/en/comps/10/stats/Championship-Stats",
    "https://fbref.com/en/comps/14/stats/2-Bundesliga-Stats",
    "https://fbref.com/en/comps/17/stats/Serie-B-Stats",
    "https://fbref.com/en/comps/18/stats/Ligue-2-Stats",
    # Americas & Asia
    "https://fbref.com/en/comps/22/stats/Major-League-Soccer-Stats",
    "https://fbref.com/en/comps/24/stats/Serie-A-Stats",
    "https://fbref.com/en/comps/31/stats/Liga-MX-Stats",
    "https://fbref.com/en/comps/21/stats/Super-Lig-Stats",
    "https://fbref.com/en/comps/25/stats/J1-League-Stats",
]

FOLDER_NAME = "FBRef_Team_Stats_Pack"
ZIP_NAME = "FBRef_Data_Archive.zip"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

def clean_headers(df):
    """Merapikan MultiIndex Header FBRef menjadi Single Header yang bersih"""
    if isinstance(df.columns, pd.MultiIndex):
        new_cols = []
        for col in df.columns.values:
            lvl_0 = str(col[0])
            lvl_1 = str(col[1])
            
            # Jika level atas Unnamed, gunakan level bawah saja (misal: 'Squad')
            if "Unnamed" in lvl_0 or "level_0" in lvl_0:
                new_cols.append(lvl_1)
            # Jika level atas dan bawah sama, gunakan satu saja
            elif lvl_0 == lvl_1:
                new_cols.append(lvl_1)
            # Selain itu gabungkan (misal: 'Performance_Gls')
            else:
                new_cols.append(f"{lvl_0}_{lvl_1}")
        df.columns = new_cols
    
    # Ganti spasi dengan underscore dan hilangkan baris baru
    df.columns = [str(c).strip().replace(' ', '_').replace('\n', '') for c in df.columns]
    return df

def start_grab():
    # Menggunakan Chrome v145 (sesuai settingan stabil Anda sebelumnya)
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=145)
    
    file_count = 0
    
    try:
        for url in LEAGUE_URLS:
            try:
                league_name = url.split('/')[-1].replace('-Stats', '')
                print(f"Mengakses {league_name}...")
                
                driver.get(url)
                
                # Tunggu tabel benar-benar muncul
                WebDriverWait(driver, 25).until(
                    EC.presence_of_element_located((By.TAG_NAME, "table"))
                )
                time.sleep(5) # Memberi waktu rendering script internal FBRef
                
                html_content = driver.page_source
                all_tables = pd.read_html(io.StringIO(html_content))
                
                t_idx = 0
                for df in all_tables:
                    # 1. Rapikan Header
                    df = clean_headers(df)
                    
                    # 2. Filter Ketat: Hanya Team Stats (Ada 'Squad', bukan data Player/Match)
                    cols_str = " ".join(df.columns).lower()
                    has_squad = 'squad' in cols_str
                    has_player = 'player' in cols_str
                    is_match = 'score' in cols_str or 'attendance' in cols_str

                    if has_squad and not has_player and not is_match:
                        t_idx += 1
                        filename = f"{league_name}_Team_Stats_{t_idx}.csv"
                        path = os.path.join(FOLDER_NAME, filename)
                        
                        df.to_csv(path, index=False)
                        file_count += 1
                        print(f"   [OK] Tersimpan: {filename}")

            except Exception as e:
                print(f"   [SKIP] Error pada {url}: {e}")
            
            # Jeda 10 detik agar IP aman dari blokir
            time.sleep(10)

        # --- PROSES ZIP ---
        if file_count > 0:
            print(f"\nMengompresi {file_count} file ke ZIP...")
            with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in os.listdir(FOLDER_NAME):
                    zipf.write(os.path.join(FOLDER_NAME, file), arcname=file)
            print(f"✅ SELESAI! File ZIP siap di: {os.path.abspath(ZIP_NAME)}")
        else:
            print("❌ Tidak ada file yang berhasil diunduh.")

    finally:
        driver.quit()

if __name__ == "__main__":
    start_grab()