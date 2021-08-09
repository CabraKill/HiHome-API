from google.cloud import firestore
import threading
import signal
import sys
def signal_handler(sig, frame):
    print(' You pressed Ctrl+C!')
    sys.exit(0)

db = firestore.Client(project='home-dbb7e')

# db = firestore.Client()
# [START firestore_listen_query_snapshots]

# Create an Event for notifying main thread.
callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(col_snapshot, changes, read_time):
    for doc in col_snapshot:
        print(f'{doc.id} - {doc.get("timee")}')
    callback_done.set()

col_query = db.document(u'configs/last')#.where(u'state', u'==', u'CA')

# Watch the collection query
query_watch = col_query.on_snapshot(on_snapshot)
callback_done.wait()
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit <3')
while True:
    pass
query_watch.unsubscribe()
print("Done")