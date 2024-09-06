from file_handling import select_image_file, create_bar_graph, fetch_graphing_data, copy_file
from ocr import process_image, draw_translated_text, delete_saved_image 
from datalog import update_daily_data, separate_and_count_characters

# Buat button untuk milih gambar yang mau ditranslate
def pick_image_and_run_ocr(username): # butuh username dari login page
    image_path = select_image_file()
    while True:
        if image_path:
            break
    df2 = process_image(image_path)

    print(df2) # function ini bakal ngeprint dataframe, tolong bikin textbox buat ini

    saved_path = draw_translated_text(image_path, df2) # function ini bakal ngeshow gambar bikin box buat ini
    image_to_show = "./out_image/showfinalimage.jpg"
    copy_file(saved_path, image_to_show)

    characters, tstamps = separate_and_count_characters(df2)

    print("Translation Counts:", characters)
    print("Timestamps:", tstamps)

    try: 
        update_daily_data(username, tstamps, characters)
        print("Data has been updated successfully.")
    except:
        print("Error updating data.")

    x, y = fetch_graphing_data(username)
    create_bar_graph(x, y) # function ini bakal ngeshow grafik juga bikin box buat ini
    
    return saved_path


def save_image_decision(choice, saved_path): 
    if choice:
        print("Picture saved.")
    else:
        delete_saved_image(saved_path)

# Tolong buat ketika klik tombol buat pick image dan ngerun OCR, nanti setelah function itu selesai 
# bakal ada pop up yang nanya mau save gambar atau nggak, kalo iya nanti choice = 1, dan kalau gak 
# nanti choice = 0, lalu jalanin save_image_decision. Nah saved_path di function saved_image_decision 
# itu asalnya dari return function pick_image_and_run_ocr 

pathfiles = pick_image_and_run_ocr("admin1")
save_image_decision(0, pathfiles)
