from pylsl import resolve_byprop, StreamInlet

results = []
while not results:
    results = resolve_byprop('name','markerStreamName')
inlet = StreamInlet(results[0])

# Read samples
while 1:
    data, timeStamp = inlet.pull_sample()
    print(data, timeStamp)

