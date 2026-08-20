class GenerativeSocialCreativeAdVariationSynthesizerClient:
    def synthesize_variations(self, product_highlight: str, target_aspect_ratio: str = "9:16") -> dict:
        scenes = [
            {"scene_id": 1, "duration_s": 3, "visual": "Split-screen comparison problem vs solution", "caption": "Tired of boring manual tools?"},
            {"scene_id": 2, "duration_s": 7, "visual": "Close-up action demonstration with dynamic zoom", "caption": "Watch this autonomous skill do it in 2 seconds."},
            {"scene_id": 3, "duration_s": 5, "visual": "Customer review overlay with animated 5-star rating", "caption": "Grab yours before the flash sale ends!"}
        ]
        return {
            "storyboard_scenes": scenes,
            "estimated_ctr_pct": 5.4,
            "hook_intensity_score": 9.6
        }
