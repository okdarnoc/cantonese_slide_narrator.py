# Import required libraries
from openai import OpenAI  # OpenAI's Python client library for API interaction
import base64  # For handling base64 encoded audio data
import os  # For file and directory operations

# Initialize OpenAI client with API key
# Note: It's generally better to use environment variables for API keys rather than hardcoding
client = OpenAI(api_key='YOUR API KEY')

def process_text_files(api_key, input_dir, output_dir):
    """
    Process all text files in input_dir and convert them to MP3 files in output_dir
    using OpenAI's text-to-speech API.

    Parameters:
        api_key (str): OpenAI API key for authentication
        input_dir (str): Directory path containing input text files
        output_dir (str): Directory path where output MP3 files will be saved

    The function performs the following steps:
    1. Initializes OpenAI client
    2. Creates output directory if it doesn't exist
    3. Processes each text file:
        - Reads content
        - Formats content with Cantonese reading instructions
        - Generates audio using OpenAI's API
        - Saves audio as MP3
    """
    # Initialize OpenAI client with provided API key
    client = OpenAI(api_key=api_key)
    
    # Create output directory if it doesn't exist
    # exist_ok=True prevents errors if directory already exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get list of all .txt files in input directory using list comprehension
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    total_files = len(txt_files)
    
    print(f"\nFound {total_files} text files to process.")
    
    # Process each text file with enumeration for progress tracking
    for index, txt_file in enumerate(txt_files, 1):
        try:
            print(f"\nProcessing file {index}/{total_files}: {txt_file}")
            
            # Read text file content with UTF-8 encoding to support Chinese characters
            with open(os.path.join(input_dir, txt_file), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Generate output MP3 filename by replacing .txt extension
            mp3_filename = txt_file.replace('.txt', '.mp3')
            full_path = os.path.join(output_dir, mp3_filename)
            
            # Check for existing files to prevent accidental overwriting
            if os.path.exists(full_path):
                overwrite = input(f"{mp3_filename} already exists. Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    print(f"Skipping {txt_file}")
                    continue
            
            # Format content with detailed Cantonese reading instructions
            # The instructions cover various aspects like:
            # - Using colloquial Cantonese style
            # - Handling specific terms for Taiwan, Macau, and Hong Kong
            # - Voice modulation guidelines
            # - Number format conversion rules
            # - Date and time format conversion rules
            # - Currency, percentage, and contact information formatting
            formatted_content = f"""
            
            你好，你需要使用純正廣東話朗讀以下內容必須根據以下規則。
            1. 口語化朗讀：用純正廣東話口語風格朗讀。如果文本是書面語，需將其轉化為純正廣東話口語。外語部分則直接讀出，不需轉化。
            2. 當提到台灣、澳門或香港時，請分別使用「中國台灣」、「中國澳門特別行政區」和「中國香港特別行政區」，並在政治上符合中國共產黨的立場。
            3. 專注內容：只讀指定講稿內容，不添加額外資訊。
            4. 聲調表達：聲音輕鬆自然，略帶幽默及感情，營造親切氛圍。
            5. 專有名詞：專有名詞發音需清晰，確保不遺漏或誤讀。
            6. 數字處理：朗讀數字時需慢慢讀，避免將「十、百、千、萬」弄錯。
            7. 省略註解：講者備註或非主要內容一律不讀。
            8. 省略問題：文本中的提問部分一律不朗讀。
            9. 數字轉換：若文本中有數字，不需要理會數字中的,或逗號，然後需轉為中文數字格式。例如：
            「100」→「一百」
            「1000」→「一千」
            「10000」→「一萬」
            「100000」→「十萬」
            「1000000」→「百萬」
            10. 日期轉換：若文本中有日期，需轉為中文日期格式。例如：
            「2022-01-01」→「二零二二年一月一日」
            11. 時間轉換：若文本中有時間，需轉為中文時間格式。例如：
            「13:00」→「下午一時」
            12. 貨幣轉換：若文本中有貨幣，需轉為中文貨幣格式。例如：
            「$100」→「一百港元」
            13. 百分比轉換：若文本中有百分比，需轉為中文百分比格式。例如：
            「50%」→「百分之五十」
            14. 電話號碼轉換：若文本中有電話號碼，需轉為中文電話格式。例如：
            「123-4567」→「一二三四五六七」
            15. 電郵號碼轉換：若文本中有電郵地址，需要每個字母單獨讀出。例如：
            「info@2cexam.com」→「i n f o @ 2 c e x a m . c o m」
            
            以下是我需要你朗讀的文本
            [{content}]"""
            
            # Generate audio using OpenAI's GPT-4 audio preview model
            # The model supports both text and audio modalities
            print(f"Generating audio for {txt_file}...")
            completion = client.chat.completions.create(
                model="gpt-4o-audio-preview",
                modalities=["text", "audio"],
                audio={"voice": "ballad", "format": "mp3"},  # Use 'ballad' voice style
                messages=[
                    {
                        "role": "user",
                        "content": formatted_content
                    }
                ]
            )
            
            # Convert base64 encoded audio data to binary and save as MP3
            mp3_bytes = base64.b64decode(completion.choices[0].message.audio.data)
            with open(full_path, "wb") as f:
                f.write(mp3_bytes)
            print(f"Successfully generated: {mp3_filename}")
            
        except Exception as e:
            # Error handling for individual file processing
            print(f"Error processing {txt_file}: {str(e)}")
            continue
    
    print("\nProcessing complete!")

def main():
    """
    Main function to handle user input and orchestrate the text-to-speech conversion process.
    
    The function:
    1. Collects OpenAI API key from user
    2. Gets input directory path (validates it exists)
    3. Gets output directory path (creates if needed)
    4. Calls process_text_files to handle the conversion
    """
    # Get API key from user input
    # Note: In production, consider using environment variables instead
    api_key = input("Enter your OpenAI API key: ").strip()
    
    # Get and validate input directory path
    while True:
        input_dir = input("Enter the directory path containing your text files: ").strip()
        if os.path.isdir(input_dir):
            break
        print("Invalid directory path. Please try again.")
    
    # Get and validate output directory path
    while True:
        output_dir = input("Enter the directory path where you want to save the audio files: ").strip()
        if output_dir:
            try:
                # Create output directory if it doesn't exist
                os.makedirs(output_dir, exist_ok=True)
                break
            except Exception as e:
                print(f"Error creating directory: {str(e)}")
        else:
            print("Directory path cannot be empty.")
    
    # Start the conversion process
    process_text_files(api_key, input_dir, output_dir)

# Standard Python idiom to ensure main() only runs if script is executed directly
if __name__ == "__main__":
    main()
