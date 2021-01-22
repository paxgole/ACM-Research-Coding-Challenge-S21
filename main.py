from dna_features_viewer import GraphicFeature, CircularGraphicRecord
features = [
    GraphicFeature(start=139, end=480, strand=+1, color="#98ce00", label="v2"),
    GraphicFeature(start=299, end=1075, strand=+1, color="#16e0bd", label="v1"),
    GraphicFeature(start=1072, end=1476, strand=-1, color="#78C3FB", label="c3"),
    GraphicFeature(start=1217, end=1624, strand=+1, color="#89A6FB", label="c2"),
    GraphicFeature(start=1533, end=2612, strand=+1, color="#98838F", label="c1")
           ]
circular_rec = CircularGraphicRecord(sequence_length=2766, features=features)
record, _ = circular_rec.plot(figure_width=4)
record.figure.savefig("TomatoCSVFeaturesCircularGraph.png", bbox_inches="tight")