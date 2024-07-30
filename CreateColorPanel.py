#------------------------------------------------------------------------------------------------------------
# This python script is for creating Jupyter Notebook that display color board table markdown.
# Author: Runquanye
# Date: 2024 / 07
#------------------------------------------------------------------------------------------------------------

import nbformat as nbf

# Create a new notebook object
nb = nbf.v4.new_notebook()


title = '# <center><span style="color:#0392cf"><b>Color Set Collections</b></span></center>'
description = '<b>Description:</b> Here are some of my favourite colour set collections. Hope you like it.\n\n---'

section_tag = '## <span style="color:#ff6453"><b>颜色标签表</b></span>'
table_header = "| No | Color | Text Sample | Text Highlight | Text Over White |"
table_align = "|:----:|:---:|:---:|:---:|:---:|"
text_sample = "样例文案 abcd <b>ABCD</b> <i>1234</i>"

color_set = {
    "Four_Color_Set" : {
        1 : ["#ff6453", "#ff8253", "#ffac53", "#ffe353"]
    },
    "Five_Color_Set" : {
        1 : ["#ee4035", "#f37736", "#fdf498", "#7bc043", "#0392cf"],
        2 : ["#7dde92", "#8bb879", "#e1de69", "#b6be6f", "#9aea6b"],
        3 : ["#47c68b", "#d39f74", "#abd14c", "#f1afaf", "#e7ef92"],
        4 : ["#d9ed92", "#b5e48c", "#99d98c", "#76c893", "#52b69a"],
        5 : ["#fffa85", "#fcd238", "#ff7f50", "#eb655b", "#58b849"],
        6 : ["#e7e47d", "#b69649", "#8edc62", "#5aaa31", "#479396"],
        7 : ["#ff4e50", "#f57758", "#eca061", "#e2c969", "#d8f271"],
        8 : ["#423f3f", "#336b8b", "#83984d", "#f0b51f", "#ea700b"],
        9 : ["#22d3ee", "#f87171", "#facc15", "#e879f9", "#4ade80"]
    },
    "Six_Color_Set" : {
        1 : ["#f9acdf", "#f7c98b", "#dbfb78", "#abf28c", "#90dcf2", "#e181ea"],
        2 : ["#f83361", "#fb4e01", "#e9f109", "#06ad40", "#0271bc", "#350450"],
        3 : ["#dfe801", "#f73560", "#008d26", "#0065bf", "#280439", "#fe4807"],
    },
    "Other_Color_Set" : {
        1 : ["#fe5e9d", "#f9662d", "#5e22a0", "#38a879", "#51cbf4", "#314cd2", "#f63933", "#1f2227"],
        2 : ["#bc908f", "#bc9690", "#e9ccd0", "#a89ea6", "#8c94c0", "#89a6a4", "#7767a7", "#829fcc", "#88a498", "#a99787", "#e88b93", "#99888e"]
    }
}

def createSpanTag(text, colorHEX=None, background=None):
    return f'''<span{f' style="{f"color:{colorHEX};" if colorHEX else ""}{f" background:{background};" if background else ""}"' if colorHEX or background else ''}> {text} </span>'''

def createColorTable(colorList):
    table_content = ""
    if colorList:
        table_content = "\n\n" + table_header + "\n" + table_align + "\n"
        for i in range(len(colorList)):
            table_content += f"| {createSpanTag(text = i+1)} | {createSpanTag(text = colorList[i], colorHEX=colorList[i])} | {createSpanTag(text = text_sample, colorHEX=colorList[i])} | {createSpanTag(text = text_sample, background = colorList[i])} | {createSpanTag(text = text_sample, colorHEX = colorList[i], background = 'white')} |\n"
        # table_content += "\n---"
    return table_content


# Add cells to the notebook
nb['cells'] = [
    nbf.v4.new_markdown_cell(title + "\n\n" + description),
    nbf.v4.new_markdown_cell(section_tag)
]

# Create the color table and append to the notebook.

for (key, val) in color_set.items():
    # create section header markdown
    newCell = nbf.v4.new_markdown_cell("### " + "<b>" + createSpanTag(text=key.replace('_'," "), colorHEX="#58b849") + "</b>")
    # Append the new Markdown cell to the notebook
    nb.cells.append(newCell)
    for (subK, cSet) in val.items():
        newCell = nbf.v4.new_markdown_cell(createColorTable(cSet))
        nb.cells.append(newCell)
    nb.cells.append(nbf.v4.new_markdown_cell("---"))

# Save the modified notebook
with open('ColorPanel.ipynb', 'w+', encoding='utf-8') as f:
    nbf.write(nb, f)

print("\tSucceeded! Saved as 'ColorPanel.ipynb'")
