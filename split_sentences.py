import re
import comfy

class ParagraphSplitter:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "max_paragraphs": ("INT", {"default": 10, "min": 1, "max": 10, "step": 1}),
            },
            "optional": {
                "delimiter": ("STRING", {"default": ";；", "multiline": False}),
            }
        }

    RETURN_TYPES = tuple(["STRING"] * 10)
    RETURN_NAMES = ("段落1", "段落2", "段落3", "段落4", "段落5", 
                   "段落6", "段落7", "段落8", "段落9", "段落10")
    FUNCTION = "split_paragraphs"
    CATEGORY = "text/processing"

    def split_paragraphs(self, text, max_paragraphs, delimiter=";；"):
        # 创建自定义分隔符正则表达式
        delimiter_pattern = '[' + re.escape(delimiter) + ']'
        
        # 分割段落
        raw_paragraphs = re.split(delimiter_pattern, text)
        paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]
        paragraphs = paragraphs[:max_paragraphs]
        
        # 填充结果到10个输出
        padded_paragraphs = paragraphs + [""] * (10 - len(paragraphs))
        return tuple(padded_paragraphs)

NODE_CLASS_MAPPINGS = {"ParagraphSplitter": ParagraphSplitter}
NODE_DISPLAY_NAME_MAPPINGS = {"ParagraphSplitter": "📝 段落分割器"}