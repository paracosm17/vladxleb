from wagtail import blocks

class ExpeditionBlock(blocks.StructBlock):
    name = blocks.ChoiceBlock(choices=[
        ('A', 'Expedition A'),
        ('B', 'Expedition B'),
        ('C', 'Expedition C'),
        ('D', 'Expedition D'),
    ], required=True)
    gate = blocks.IntegerBlock()
    description = blocks.TextBlock(required=False)
    date = blocks.DateTimeBlock()
    completed = blocks.BooleanBlock(default=False, required=False)

    class Meta:
        template = 'blocks/expedition_block.html'
        icon = 'site'
        label = 'Expedition'
        