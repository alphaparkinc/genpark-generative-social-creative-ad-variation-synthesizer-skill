from client import GenerativeSocialCreativeAdVariationSynthesizerClient

def main():
    client = GenerativeSocialCreativeAdVariationSynthesizerClient()
    res = client.synthesize_variations("AI Autonomous Video Editing Studio")
    print(f"Hook Intensity: {res['hook_intensity_score']}/10")
    print(f"Estimated CTR: {res['estimated_ctr_pct']}%")
    print("Generated Storyboard Scenes:")
    for s in res["storyboard_scenes"]:
        print(f"  - [Scene {s['scene_id']}] ({s['duration_s']}s) {s['visual']} | Overlay: '{s['caption']}'")

if __name__ == "__main__":
    main()
