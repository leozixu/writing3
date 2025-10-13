class WritingProperty: #定义写作风格
    style: str | None = None
    words: str | None = None
    steps: str | None = None
    total: str | None = None
    def __init__(self, style, words,steps,total):
        self.style = style
        self.words = words
        self.steps = steps
        self.total = total