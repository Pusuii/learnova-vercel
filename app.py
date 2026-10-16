"""Titik masuk Learnova.

Jalankan:   python app.py
Reset data: python app.py --reset      (hapus database & unggahan, buat ulang data demo)
"""
import os
import shutil
import sys

from learnova import create_app

if "--reset" in sys.argv:
    inst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "instance")
    for name in ("learnova.db", "learnova.db-wal", "learnova.db-shm"):
        path = os.path.join(inst, name)
        if os.path.exists(path):
            os.remove(path)
    shutil.rmtree(os.path.join(inst, "uploads"), ignore_errors=True)
    print("Database dan unggahan direset.")

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    print("\n  Learnova berjalan di http://%s:%d\n" % (host, port))
    app.run(host=host, port=port, debug=debug)
