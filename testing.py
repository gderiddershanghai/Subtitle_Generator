
import os
import wave

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

assembly_api_key  = os.getenv('ASSEMBLYAI_API_KEY')
