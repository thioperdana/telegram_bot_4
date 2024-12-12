import logging
from dotenv import dotenv_values

env = dotenv_values(".env")

# Membuat formatter untuk memformatkan log
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(f"{env['PROJECT_PATH']}{env['LOG_PATH']}sys_debug.log")
    ]
)

# Membuat logger untuk general
logger_general = logging.getLogger('general')
logger_general.setLevel(logging.DEBUG)
logger_general.propagate = False

# Membuat formatter untuk memformatkan log pada logger general
formatter_general = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Menambahkan handler ke logger general
handler_file_general = logging.FileHandler(f"{env['PROJECT_PATH']}{env['LOG_PATH']}debug.log")
handler_file_general.setFormatter(formatter_general)
logger_general.addHandler(handler_file_general)

# Menambahkan stream handler ke logger general
stream_handler_file_general = logging.StreamHandler()
stream_handler_file_general.setFormatter(formatter_general)
logger_general.addHandler(stream_handler_file_general)

# Membuat logger untuk error
logger_error = logging.getLogger('error')
logger_error.setLevel(logging.ERROR)
logger_error.propagate = False

# Membuat formatter untuk memformatkan log pada logger error
formatter_error = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Menambahkan handler ke logger error
handler_file_error = logging.FileHandler(f"{env['PROJECT_PATH']}{env['LOG_PATH']}error.log")
handler_file_error.setFormatter(formatter_error)
logger_error.addHandler(handler_file_error)

# Contoh penggunaan logger general dan logger error
if __name__ == "__main__":
    # Penggunaan logger general
    logger_general.info("Ini adalah informasi umum")
    logger_general.debug("Ini adalah debug umum")

    # Penggunaan logger error
    try:
        # Kode yang dapat menyebabkan error
        raise Exception("Terjadi kesalahan!")
    except Exception as e:
        logger_error.error(f"Error: {e}")