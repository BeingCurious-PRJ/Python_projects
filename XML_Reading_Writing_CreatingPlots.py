import xml.etree.ElementTree as ET
from datetime import date
from lxml import etree as et
import plotly.graph_objects as go

# example of data as variables to be fed to xml structure
data_date = date.today()
length_1 = 4567.456
length_2 = 3654.675
delta = length_2 - length_1
length_3 = 3746.4745
length_4 = 4735.9878
length_5 = 4756.987

# CREATING XML FILE FROM EXTRACTED GEO DATA IN KM
# getting new data into a tree element structure, to be appended
main_root = ET.Element("MAIN_DATA")
sub_root = ET.Element("Sub_Data1")
main_root.append(sub_root)

m1 = ET.SubElement(sub_root, "Download")
m1.set("Date", str(data_date))

b1 = ET.SubElement(m1, "sub_element1")
b1.set("field1", str(length_2))
b1.set("field2", str(length_1))
# b2.text ="PROD"

b2 = ET.SubElement(m1, "sub_element2")
b2.set("field1", str(length_3))

b3 = ET.SubElement(m1, "sub_element3")
b3.set("field1", str(delta))

b4 = ET.SubElement(m1, "sub_element4")
b4.set("field1", str(length_5))
b4.set("field2", str(length_4))

tree = ET.ElementTree(main_root)

# SAVING AS A TESTFILE IN DESKTOP
with open(r"C:\Users\user1\Desktop\testfile.xml", "wb") as files:  # path with a filename where the xml data is to be
    # saved
    tree.write(files)

# Once an xml file with specific structure is created, comment out the above code for saving/writing new xml file
# A sample xml file structure as per the code above is given in the 'wiki'
# New variables could instead be fed into the structure and appended by the code below

# APPENDING THE EXISTING XML FILE WITH NEW DATA
my_xml = ET.parse(r"C:\Users\user1\Desktop\testfile.xml")  # path of the xml file to be appended
sub_group_element = my_xml.find('.//MCI_HCI_Trends')  # xpath approach to get to a node
new_element = m1
sub_group_element.append(new_element)
new_tree = ET.tostring(my_xml.getroot())
with open(r"C:\Users\user1\Desktop\NDS_Data.xml", "wb") as files:
    files.write(new_tree)

# ################################getting the xml data as different lists to plot######################################
tree_to_plot = et.parse(r"C:\Users\user1\Desktop\NDS_Data.xml")
download_elements = tree_to_plot.xpath('//Download')

delta_list = []
date_list = []
length1_list = []
length2_list = []
length3_list = []
length4_list = []
length5_list = []
# mci1 = elem.getchildren()[0].getchildren() ..double get children if a node has a list
# for m in mci1:
# dt_delta.append(())
for elem in download_elements:
    sub_element1 = elem.getchildren()[0]
    sub_element2 = elem.getchildren()[1]
    sub_element3 = elem.getchildren()[2]
    sub_element4 = elem.getchildren()[3]

    delta_list.append(sub_element3.attrib.get('field1'))
    date_list.append(elem.attrib.get('Date'))
    length1_list.append(sub_element1.attrib.get('field2'))
    length2_list.append(sub_element1.attrib.get('field1'))
    length3_list.append(sub_element2.attrib.get('field1'))
    length4_list.append(sub_element4.attrib.get('field2'))
    length5_list.append(sub_element4.attrib.get('field1'))

# date_list_float.append(float(elem.attrib.get('Date')))

# ##########################################interactive plots with plotly#############################################
# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(
    x=date_list,
    y=length1_list,
    name="MCI1_CIT",
    text=length1_list,
    yaxis="y1",
))
fig.add_trace(go.Scatter(
    x=date_list,
    y=length2_list,
    name="MCI1_PROD",
    text=length2_list,
    yaxis="y2",
))
fig.add_trace(go.Scatter(
    x=date_list,
    y=length4_list,
    name="MCI3_CIT",
    text=length4_list,
    yaxis="y3",
))
fig.add_trace(go.Scatter(
    x=date_list,
    y=length5_list,
    name="MCI3_PROD",
    text=length5_list,
    yaxis="y4",
))
fig.add_trace(go.Scatter(
    x=date_list,
    y=length3_list,
    name="HCI",
    text=length3_list,
    yaxis="y5",
))
fig.add_trace(go.Scatter(
    x=date_list,
    y=delta_list,
    name="Delta_MCI1",
    text=delta_list,
    yaxis="y6",
))
# style all the traces
fig.update_traces(
    hoverinfo="name+x+text",
    line={"width": 0.7},
    marker={"size": 8},
    mode="lines+markers",
    showlegend=False
)
# Add shapes
fig.update_layout(
    shapes=[
        dict(
            fillcolor="rgba(73, 160, 80, 0.1)",  # 63, 81, 181, 0.2       ...  76, 175, 80, 0.1
            line={"width": 0},
            type="rect",  # circle, path, line, rect
            x0=date_list[0],
            x1=date_list[len(date_list) - 1],
            xref="x",
            y0=0,
            y1=0.95,
            yref="paper"
        )
    ]
)

# Update axes
fig.update_layout(
    xaxis=dict(
        autorange=True,
        range=[date_list[0], date_list[len(date_list) - 1]],
        rangeslider=dict(
            autorange=True,
            range=[date_list[0], date_list[len(date_list) - 1]]
        ),
        type="date"
    ),
    yaxis=dict(
        anchor="x",
        autorange=True,
        domain=[0, 0.2],
        linecolor="#673ab7",
        mirror=True,
        range=[min(length1_list), max(length1_list)],
        showline=True,
        side="left",
        tickfont={"color": "#673ab7"},
        tickmode="auto",
        ticks="",
        title="MCI1_CIT",
        titlefont={"color": "#673ab7"},
        type="linear",
        zeroline=True
    ),
    yaxis2=dict(
        anchor="x",
        autorange=True,
        domain=[0.2, 0.4],
        linecolor="#E91E63",
        mirror=True,
        range=[min(length2_list), max(length2_list)],
        showline=True,
        side="left",
        tickfont={"color": "#E91E63"},
        tickmode="auto",
        ticks="",
        title="MCI1_PROD",
        titlefont={"color": "#E91E63"},
        type="linear",
        zeroline=False
    ),
    yaxis3=dict(
        anchor="x",
        autorange=True,
        domain=[0.4, 0.6],
        linecolor="#795548",
        mirror=True,
        range=[min(length4_list), max(length4_list)],
        showline=True,
        side="right",
        tickfont={"color": "#795548"},
        tickmode="auto",
        ticks="",
        title="MCI3_CIT",
        titlefont={"color": "#795548"},
        type="linear",
        zeroline=False
    ),
    yaxis4=dict(
        anchor="x",
        autorange=True,
        domain=[0.6, 0.8],
        linecolor="#607d8b",
        mirror=True,
        range=[min(length5_list), max(length5_list)],
        showline=True,
        side="right",
        tickfont={"color": "#607d8b"},
        tickmode="auto",
        ticks="",
        title="MCI3_PROD",
        titlefont={"color": "#607d8b"},
        type="linear",
        zeroline=False
    ),
    yaxis5=dict(
        anchor="x",
        autorange=True,
        domain=[0.8, 0.9],
        linecolor="#2196F3",
        mirror=True,
        range=[min(length3_list), max(length3_list)],
        showline=True,
        side="left",
        tickfont={"color": "#2196F3"},
        tickmode="auto",
        ticks="",
        title="HCI",
        titlefont={"color": "#2196F3"},
        type="linear",
        zeroline=False
    ),
    yaxis6=dict(
        anchor="x",
        autorange=True,
        domain=[0.9, 1],
        linecolor="#3c1009",
        mirror=True,
        range=[min(delta_list), max(delta_list)],
        showline=True,
        side="right",
        tickfont={"color": "#3c1009"},
        tickmode="auto",
        ticks="",
        title="Delta_MCI1",
        titlefont={"color": "#3c1009"},
        type="linear",
        zeroline=False
    )
)

# Update layout
fig.update_layout(
    dragmode="zoom",
    hovermode="x",
    legend=dict(traceorder="normal"),  # "reversed", "grouped", "reversed+grouped", "normal"
    height=900,
    template="plotly_white",
    margin=dict(
        t=100,
        b=100
    ),
)
fig.show()

#   Default template: 'plotly'
#    Available templates:
#        ['ggplot2', 'seaborn', 'simple_white', 'plotly',
#         'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
#         'ygridoff', 'gridon', 'none']
