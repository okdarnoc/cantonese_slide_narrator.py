# CantoneseVoice: Intelligent Text-to-Speech Converter for Cantonese Content

CantoneseVoice is a sophisticated Python application that converts text files into natural-sounding Cantonese speech using OpenAI's advanced text-to-speech API. The program specializes in handling Cantonese text with intelligent formatting rules, making it perfect for creating audio content for educational materials, podcasts, or accessibility purposes.

## Features

- **Batch Processing**: Convert multiple text files to MP3 format in one operation
- **Smart Text Processing**: Automatically handles various text formats including:
  - Numbers and currencies
  - Dates and times
  - Email addresses and phone numbers
  - Percentages and measurements
- **Natural Cantonese Speech**: Implements sophisticated reading rules for authentic Cantonese pronunciation
- **Colloquial Style**: Automatically converts formal written Chinese to colloquial Cantonese speech patterns
- **Customizable Output**: Choose your preferred output directory for organized audio file management
- **Error Handling**: Robust error management with clear feedback for failed conversions
- **File Safety**: Prevents accidental overwriting of existing audio files

## Prerequisites

- Python 3.6 or higher
- OpenAI API key with access to GPT-4 audio preview model
- Internet connection for API access
- Sufficient disk space for audio files

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/cantonese-voice.git
cd cantonese-voice
```

2. Install required packages:
```bash
pip install openai
```

3. Set up your OpenAI API key (recommended to use environment variables):
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

1. Prepare your text files:
   - Save them in UTF-8 encoding
   - Place them in a single directory
   - Use .txt extension

2. Run the program:
```bash
python cantonese_slide_narrator.py
```

3. Follow the prompts:
   - Enter your OpenAI API key (if not set in environment)
   - Specify input directory containing text files
   - Choose output directory for MP3 files

## Text Formatting Guidelines

The program follows these rules when converting text to speech:

1. **Numbers**:
   - "100" → "一百"
   - "1000" → "一千"
   - "10000" → "一萬"

2. **Dates**:
   - "2022-01-01" → "二零二二年一月一日"

3. **Times**:
   - "13:00" → "下午一時"

4. **Currency**:
   - "$100" → "一百港元"

5. **Contact Information**:
   - Email addresses are spelled out letter by letter
   - Phone numbers are read digit by digit

## Error Handling

The program provides clear error messages for common issues:
- Invalid directory paths
- File access permissions
- API connection problems
- File encoding issues

## Limitations

- Maximum text file size depends on OpenAI API limits
- Internet connection required for conversion
- API key must have access to GPT-4 audio preview model
- Processing time varies based on text length and API response time

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the text-to-speech API
- Contributors to the project
- Feedback from the Cantonese-speaking community

## Contact

For questions and support, please open an issue in the GitHub repository or contact the maintainers directly.

---

**Note**: This project is not affiliated with OpenAI. All API usage is subject to OpenAI's terms of service and pricing.
