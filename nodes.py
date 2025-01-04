



class FluxParattentionNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "enable": ("BOOLEAN", {"default": True}),
                "num_gpus": ("INT", {"default": 1, "min": 1, "max": 8, "step": 1}),
            }
        }

    def run(self, enable, num_gpus):
        if enable:
            return {"num_gpus": num_gpus}
        else:
            return None






NODE_CLASS_MAPPINGS = {
    "FluxParattentionNode": FluxParattentionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxParattentionNode": "Flux Parattention",
}
