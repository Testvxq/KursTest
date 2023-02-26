from enum import Enum 
 
class Gui(object) : 
 
  class WidgetType(Enum) : 
    PushButton = 0 
    ToolButton = 1 
    ProgressBar = 2 
    LineEdit = 3 
    Dial = 4 
    Slider = 5 
    CheckBox = 6 
    Label = 7 
    OpenFileButton = 8 
    ToolButtonWithLed = 9 
    ToolButtonWithProgress = 10 
    VerticalSlider = 11 
    HorizontalSlider = 12 
    DigitalIOControl = 13 
    AnalogIOControl = 14 
    CurrentGcodesWidget = 15 
    MdiLineWidget = 16 
    PythonConsole = 17 
    GCodeList = 18 
    SimGLWidget = 19 
    OffsetTable = 20 
    GroupBox = 21 
    Frame = 22 
    TabWidget = 23 
    ScrollArea = 24 
    Splitter = 25 
 
  def __init__(self, comm) : 
    self.comm = comm 
    self.createObjects() 
 
  def getIds(self) : 
    return [i for i in self.comm.sendAndWait( "gui_getWidgetsId:" ).split(";")] 
 
  class Widget(object) : 
 
    def __init__(self, name, comm) : 
      self.name = name 
      self.comm = comm 
 
    def getOutputs(self) : 
      return [] 
 
    def getAttributes(self) : 
      return [] 
 
    def executeOutput( self, outputName : str ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":" + outputName ) 
 
    def setAttribute( self, attribName : str, value ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":" + attribName + ":"+ type(value).__name__ +":" + str(value) ) 
 
    def getAttribute( self, attribName : str ) : 
      res = self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":" + attribName ) 
      pos = res.find(":") 
      if pos < 0: 
        raise "Attribute type error" 
      t = res[:pos] 
      val = res[pos+1:] 
      if t == "int": 
        return int(val) 
      elif t == "float": 
        return float(val) 
      elif t == "bool": 
        return bool(val) 
      elif t == "str": 
        return str(val) 
      else: 
        raise "Attribute type error" 
 
  class PushButton(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.PushButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "clicked", 
        "pressed", 
        "released", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeClickedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":clicked") 
 
    def executePressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":pressed") 
 
    def executeReleasedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":released") 
 
 
 
  class ToolButton(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "clicked", 
        "pressed", 
        "released", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeClickedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":clicked") 
 
    def executePressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":pressed") 
 
    def executeReleasedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":released") 
 
 
 
  class ProgressBar(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ProgressBar 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class LineEdit(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.LineEdit 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "returnPressed", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeReturnPressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":returnPressed") 
 
 
 
  class Dial(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Dial 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class Slider(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Slider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class CheckBox(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'checkboxstate', 'type' : 'bool'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.CheckBox 
 
 
    def setCheckboxState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":checkboxstate:" + "bool:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getCheckboxState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":checkboxstate") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "stateChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeStateChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":stateChanged") 
 
 
 
  class Label(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Label 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class OpenFileButton(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.OpenFileButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ToolButtonWithLed(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'ledstate', 'type' : 'bool'}, 
        {'name' : 'ledinterval', 'type' : 'int'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButtonWithLed 
 
 
    def setLedState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":ledstate:" + "bool:" + str(v)  ) 
 
    def setLedInterval( self, v : int ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":ledinterval:" + "int:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getLedState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":ledstate") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getLedInterval( self ) -> int : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":ledinterval") ) 
      resSplit = res.split(":") 
      return int(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ToolButtonWithProgress(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButtonWithProgress 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class VerticalSlider(Slider) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.VerticalSlider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class HorizontalSlider(Slider) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.HorizontalSlider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class DigitalIOControl(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
        {'name' : 'state', 'type' : 'bool'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.DigitalIOControl 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def setState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":state:" + "bool:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":state") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "stateChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeStateChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":stateChanged") 
 
 
 
  class AnalogIOControl(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.AnalogIOControl 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class CurrentGcodesWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.CurrentGcodesWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class MdiLineWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.MdiLineWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class PythonConsole(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.PythonConsole 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class GCodeList(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.GCodeList 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class SimGLWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.SimGLWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class OffsetTable(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.OffsetTable 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class GroupBox(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.GroupBox 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class Frame(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Frame 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class TabWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.TabWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ScrollArea(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ScrollArea 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class Splitter(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Splitter 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  def createObjects( self ) :
    self.frTopButtons = Gui.Frame("frTopButtons", self.comm)
    self.btnQuit = Gui.PushButton("btnQuit", self.comm)
    self.btnOpenGCode = Gui.OpenFileButton("btnOpenGCode", self.comm)
    self.btnEdit = Gui.PushButton("btnEdit", self.comm)
    self.btnSettings = Gui.PushButton("btnSettings", self.comm)
    self.btnRefAxes = Gui.PushButton("btnRefAxes", self.comm)
    self.btnProbing = Gui.PushButton("btnProbing", self.comm)
    self.btnTablePark = Gui.PushButton("btnTablePark", self.comm)
    self.btnXYZero = Gui.PushButton("btnXYZero", self.comm)
    self.PushButton_3 = Gui.PushButton("PushButton_3", self.comm)
    self.ToolButton_1 = Gui.ToolButton("ToolButton_1", self.comm)
    self.ToolButton_3 = Gui.ToolButton("ToolButton_3", self.comm)
    self.ToolButton_4 = Gui.ToolButton("ToolButton_4", self.comm)
    self.ToolButton_5 = Gui.ToolButton("ToolButton_5", self.comm)
    self.ToolButton_6 = Gui.ToolButton("ToolButton_6", self.comm)
    self.Label_1 = Gui.Label("Label_1", self.comm)
    self.frAxesAndOptions = Gui.Frame("frAxesAndOptions", self.comm)
    self.frAxesOptions = Gui.Frame("frAxesOptions", self.comm)
    self.cbShowAbsPos = Gui.CheckBox("cbShowAbsPos", self.comm)
    self.cbIgnoreSoftLimit = Gui.CheckBox("cbIgnoreSoftLimit", self.comm)
    self.CheckBox_1 = Gui.CheckBox("CheckBox_1", self.comm)
    self.Label_3 = Gui.Label("Label_3", self.comm)
    self.Label_2 = Gui.Label("Label_2", self.comm)
    self.lbSpacer = Gui.Label("lbSpacer", self.comm)
    self.frAxesPos = Gui.Frame("frAxesPos", self.comm)
    self.frPositionX = Gui.Frame("frPositionX", self.comm)
    self.lbPosX = Gui.Label("lbPosX", self.comm)
    self.edPosX = Gui.LineEdit("edPosX", self.comm)
    self.btnXZero = Gui.ToolButton("btnXZero", self.comm)
    self.frPositionY = Gui.Frame("frPositionY", self.comm)
    self.lbPosY = Gui.Label("lbPosY", self.comm)
    self.edPosY = Gui.LineEdit("edPosY", self.comm)
    self.btnYZero = Gui.ToolButton("btnYZero", self.comm)
    self.frPositionZ = Gui.Frame("frPositionZ", self.comm)
    self.lbPosZ = Gui.Label("lbPosZ", self.comm)
    self.edPosZ = Gui.LineEdit("edPosZ", self.comm)
    self.btnZZero = Gui.ToolButton("btnZZero", self.comm)
    self.frPositionA = Gui.Frame("frPositionA", self.comm)
    self.lbPosA = Gui.Label("lbPosA", self.comm)
    self.edPosA = Gui.LineEdit("edPosA", self.comm)
    self.btnAZero = Gui.ToolButton("btnAZero", self.comm)
    self.frPositionB = Gui.Frame("frPositionB", self.comm)
    self.lbPosB = Gui.Label("lbPosB", self.comm)
    self.edPosB = Gui.LineEdit("edPosB", self.comm)
    self.btnBZero = Gui.ToolButton("btnBZero", self.comm)
    self.frPositionC = Gui.Frame("frPositionC", self.comm)
    self.lbPosC = Gui.Label("lbPosC", self.comm)
    self.edPosC = Gui.LineEdit("edPosC", self.comm)
    self.btnCZero = Gui.ToolButton("btnCZero", self.comm)
    self.splCentral = Gui.Splitter("splCentral", self.comm)
    self.splToolGCodePython = Gui.Splitter("splToolGCodePython", self.comm)
    self.frToolAndGCode = Gui.Frame("frToolAndGCode", self.comm)
    self.frToolInfo = Gui.Frame("frToolInfo", self.comm)
    self.lbToolNr = Gui.Label("lbToolNr", self.comm)
    self.edToolNr = Gui.LineEdit("edToolNr", self.comm)
    self.lbToolOffsetNr = Gui.Label("lbToolOffsetNr", self.comm)
    self.edToolOffsetNr = Gui.LineEdit("edToolOffsetNr", self.comm)
    self.lbToolZOffset = Gui.Label("lbToolZOffset", self.comm)
    self.edToolZOffset = Gui.LineEdit("edToolZOffset", self.comm)
    self.lbToolDiameter = Gui.Label("lbToolDiameter", self.comm)
    self.edToolDiameter = Gui.LineEdit("edToolDiameter", self.comm)
    self.btnShowToolTable = Gui.PushButton("btnShowToolTable", self.comm)
    self.gcodeList = Gui.GCodeList("gcodeList", self.comm)
    self.pythonConsole = Gui.PythonConsole("pythonConsole", self.comm)
    self.mdiLine = Gui.MdiLineWidget("mdiLine", self.comm)
    self.tabCentral = Gui.TabWidget("tabCentral", self.comm)
    self.glPathView1 = Gui.SimGLWidget("glPathView1", self.comm)
    self.frGCodeInfo = Gui.Frame("frGCodeInfo", self.comm)
    self.lbGCodeName = Gui.Label("lbGCodeName", self.comm)
    self.lbRemainingTime = Gui.Label("lbRemainingTime", self.comm)
    self.GroupBox_1 = Gui.GroupBox("GroupBox_1", self.comm)
    self.lbAxisXOffset = Gui.Label("lbAxisXOffset", self.comm)
    self.edAxisXOffset = Gui.LineEdit("edAxisXOffset", self.comm)
    self.btnAxisXOffZero = Gui.PushButton("btnAxisXOffZero", self.comm)
    self.lbAxisYOffset = Gui.Label("lbAxisYOffset", self.comm)
    self.edAxisYOffset = Gui.LineEdit("edAxisYOffset", self.comm)
    self.btnAxisYOffZero = Gui.PushButton("btnAxisYOffZero", self.comm)
    self.lbAxisZOffset = Gui.Label("lbAxisZOffset", self.comm)
    self.edAxisZOffset = Gui.LineEdit("edAxisZOffset", self.comm)
    self.btnAxisZOffZero = Gui.PushButton("btnAxisZOffZero", self.comm)
    self.lbAxisAOffset = Gui.Label("lbAxisAOffset", self.comm)
    self.edAxisAOffset = Gui.LineEdit("edAxisAOffset", self.comm)
    self.btnAxisAOffZero = Gui.PushButton("btnAxisAOffZero", self.comm)
    self.lbAxisBOffset = Gui.Label("lbAxisBOffset", self.comm)
    self.edAxisBOffset = Gui.LineEdit("edAxisBOffset", self.comm)
    self.btnAxisBOffZero = Gui.PushButton("btnAxisBOffZero", self.comm)
    self.lbAxisCOffset = Gui.Label("lbAxisCOffset", self.comm)
    self.edAxisCOffset = Gui.LineEdit("edAxisCOffset", self.comm)
    self.btnAxisCOffZero = Gui.PushButton("btnAxisCOffZero", self.comm)
    self.btnOffsetZeroAll = Gui.ToolButton("btnOffsetZeroAll", self.comm)
    self.OffsetTable_1 = Gui.OffsetTable("OffsetTable_1", self.comm)
    self.scrollDiagPage = Gui.ScrollArea("scrollDiagPage", self.comm)
    self.gbSingleAxisRefButtons = Gui.GroupBox("gbSingleAxisRefButtons", self.comm)
    self.btnRefX = Gui.ToolButton("btnRefX", self.comm)
    self.btnRefY = Gui.ToolButton("btnRefY", self.comm)
    self.btnRefZ = Gui.ToolButton("btnRefZ", self.comm)
    self.btnRefA = Gui.ToolButton("btnRefA", self.comm)
    self.btnRefB = Gui.ToolButton("btnRefB", self.comm)
    self.btnRefC = Gui.ToolButton("btnRefC", self.comm)
    self.gbPathSimulation = Gui.GroupBox("gbPathSimulation", self.comm)
    self.btnSimCharts = Gui.PushButton("btnSimCharts", self.comm)
    self.btnSimView = Gui.PushButton("btnSimView", self.comm)
    self.gbDiagAnalogInputs = Gui.GroupBox("gbDiagAnalogInputs", self.comm)
    self.AnalogIOControl_4 = Gui.AnalogIOControl("AnalogIOControl_4", self.comm)
    self.AnalogIOControl_1 = Gui.AnalogIOControl("AnalogIOControl_1", self.comm)
    self.AnalogIOControl_2 = Gui.AnalogIOControl("AnalogIOControl_2", self.comm)
    self.AnalogIOControl_3 = Gui.AnalogIOControl("AnalogIOControl_3", self.comm)
    self.gbDiagAnalogOutputs = Gui.GroupBox("gbDiagAnalogOutputs", self.comm)
    self.AnalogIOControl_5 = Gui.AnalogIOControl("AnalogIOControl_5", self.comm)
    self.AnalogIOControl_6 = Gui.AnalogIOControl("AnalogIOControl_6", self.comm)
    self.lbMkSignals0 = Gui.Label("lbMkSignals0", self.comm)
    self.DigitalIOControl_20 = Gui.DigitalIOControl("DigitalIOControl_20", self.comm)
    self.DigitalIOControl_19 = Gui.DigitalIOControl("DigitalIOControl_19", self.comm)
    self.DigitalIOControl_21 = Gui.DigitalIOControl("DigitalIOControl_21", self.comm)
    self.DigitalIOControl_17 = Gui.DigitalIOControl("DigitalIOControl_17", self.comm)
    self.DigitalIOControl_18 = Gui.DigitalIOControl("DigitalIOControl_18", self.comm)
    self.DigitalIOControl_22 = Gui.DigitalIOControl("DigitalIOControl_22", self.comm)
    self.lbMkSignals1 = Gui.Label("lbMkSignals1", self.comm)
    self.DigitalIOControl_23 = Gui.DigitalIOControl("DigitalIOControl_23", self.comm)
    self.DigitalIOControl_24 = Gui.DigitalIOControl("DigitalIOControl_24", self.comm)
    self.DigitalIOControl_25 = Gui.DigitalIOControl("DigitalIOControl_25", self.comm)
    self.DigitalIOControl_26 = Gui.DigitalIOControl("DigitalIOControl_26", self.comm)
    self.DigitalIOControl_27 = Gui.DigitalIOControl("DigitalIOControl_27", self.comm)
    self.DigitalIOControl_28 = Gui.DigitalIOControl("DigitalIOControl_28", self.comm)
    self.lbMkSignals2 = Gui.Label("lbMkSignals2", self.comm)
    self.DigitalIOControl_29 = Gui.DigitalIOControl("DigitalIOControl_29", self.comm)
    self.DigitalIOControl_30 = Gui.DigitalIOControl("DigitalIOControl_30", self.comm)
    self.DigitalIOControl_31 = Gui.DigitalIOControl("DigitalIOControl_31", self.comm)
    self.DigitalIOControl_32 = Gui.DigitalIOControl("DigitalIOControl_32", self.comm)
    self.DigitalIOControl_33 = Gui.DigitalIOControl("DigitalIOControl_33", self.comm)
    self.DigitalIOControl_34 = Gui.DigitalIOControl("DigitalIOControl_34", self.comm)
    self.lbMkSignals3 = Gui.Label("lbMkSignals3", self.comm)
    self.DigitalIOControl_35 = Gui.DigitalIOControl("DigitalIOControl_35", self.comm)
    self.DigitalIOControl_36 = Gui.DigitalIOControl("DigitalIOControl_36", self.comm)
    self.DigitalIOControl_37 = Gui.DigitalIOControl("DigitalIOControl_37", self.comm)
    self.DigitalIOControl_38 = Gui.DigitalIOControl("DigitalIOControl_38", self.comm)
    self.DigitalIOControl_39 = Gui.DigitalIOControl("DigitalIOControl_39", self.comm)
    self.DigitalIOControl_40 = Gui.DigitalIOControl("DigitalIOControl_40", self.comm)
    self.lbMkSignals4 = Gui.Label("lbMkSignals4", self.comm)
    self.DigitalIOControl_41 = Gui.DigitalIOControl("DigitalIOControl_41", self.comm)
    self.DigitalIOControl_42 = Gui.DigitalIOControl("DigitalIOControl_42", self.comm)
    self.DigitalIOControl_43 = Gui.DigitalIOControl("DigitalIOControl_43", self.comm)
    self.DigitalIOControl_44 = Gui.DigitalIOControl("DigitalIOControl_44", self.comm)
    self.DigitalIOControl_45 = Gui.DigitalIOControl("DigitalIOControl_45", self.comm)
    self.DigitalIOControl_46 = Gui.DigitalIOControl("DigitalIOControl_46", self.comm)
    self.lbMkSignals5 = Gui.Label("lbMkSignals5", self.comm)
    self.DigitalIOControl_47 = Gui.DigitalIOControl("DigitalIOControl_47", self.comm)
    self.DigitalIOControl_48 = Gui.DigitalIOControl("DigitalIOControl_48", self.comm)
    self.DigitalIOControl_49 = Gui.DigitalIOControl("DigitalIOControl_49", self.comm)
    self.DigitalIOControl_50 = Gui.DigitalIOControl("DigitalIOControl_50", self.comm)
    self.DigitalIOControl_51 = Gui.DigitalIOControl("DigitalIOControl_51", self.comm)
    self.DigitalIOControl_52 = Gui.DigitalIOControl("DigitalIOControl_52", self.comm)
    self.gbDigInputs0to15 = Gui.GroupBox("gbDigInputs0to15", self.comm)
    self.ledIn8 = Gui.DigitalIOControl("ledIn8", self.comm)
    self.ledIn1 = Gui.DigitalIOControl("ledIn1", self.comm)
    self.ledIn9 = Gui.DigitalIOControl("ledIn9", self.comm)
    self.ledIn0 = Gui.DigitalIOControl("ledIn0", self.comm)
    self.ledIn7 = Gui.DigitalIOControl("ledIn7", self.comm)
    self.ledIn6 = Gui.DigitalIOControl("ledIn6", self.comm)
    self.ledIn5 = Gui.DigitalIOControl("ledIn5", self.comm)
    self.ledIn4 = Gui.DigitalIOControl("ledIn4", self.comm)
    self.ledIn3 = Gui.DigitalIOControl("ledIn3", self.comm)
    self.ledIn15 = Gui.DigitalIOControl("ledIn15", self.comm)
    self.ledIn14 = Gui.DigitalIOControl("ledIn14", self.comm)
    self.ledIn13 = Gui.DigitalIOControl("ledIn13", self.comm)
    self.ledIn12 = Gui.DigitalIOControl("ledIn12", self.comm)
    self.ledIn11 = Gui.DigitalIOControl("ledIn11", self.comm)
    self.ledIn10 = Gui.DigitalIOControl("ledIn10", self.comm)
    self.ledIn2 = Gui.DigitalIOControl("ledIn2", self.comm)
    self.gbDigInputs16to31 = Gui.GroupBox("gbDigInputs16to31", self.comm)
    self.ledDin24 = Gui.DigitalIOControl("ledDin24", self.comm)
    self.ledDin17 = Gui.DigitalIOControl("ledDin17", self.comm)
    self.ledDin25 = Gui.DigitalIOControl("ledDin25", self.comm)
    self.ledDin16 = Gui.DigitalIOControl("ledDin16", self.comm)
    self.ledDin23 = Gui.DigitalIOControl("ledDin23", self.comm)
    self.ledDin22 = Gui.DigitalIOControl("ledDin22", self.comm)
    self.ledDin21 = Gui.DigitalIOControl("ledDin21", self.comm)
    self.ledDin20 = Gui.DigitalIOControl("ledDin20", self.comm)
    self.ledDin19 = Gui.DigitalIOControl("ledDin19", self.comm)
    self.ledDin31 = Gui.DigitalIOControl("ledDin31", self.comm)
    self.ledDin30 = Gui.DigitalIOControl("ledDin30", self.comm)
    self.ledDin29 = Gui.DigitalIOControl("ledDin29", self.comm)
    self.ledDin28 = Gui.DigitalIOControl("ledDin28", self.comm)
    self.ledDin27 = Gui.DigitalIOControl("ledDin27", self.comm)
    self.ledDin26 = Gui.DigitalIOControl("ledDin26", self.comm)
    self.ledDin18 = Gui.DigitalIOControl("ledDin18", self.comm)
    self.gbDigOutputs0to15 = Gui.GroupBox("gbDigOutputs0to15", self.comm)
    self.DigitalIOControl_1 = Gui.DigitalIOControl("DigitalIOControl_1", self.comm)
    self.DigitalIOControl_2 = Gui.DigitalIOControl("DigitalIOControl_2", self.comm)
    self.DigitalIOControl_3 = Gui.DigitalIOControl("DigitalIOControl_3", self.comm)
    self.DigitalIOControl_4 = Gui.DigitalIOControl("DigitalIOControl_4", self.comm)
    self.DigitalIOControl_5 = Gui.DigitalIOControl("DigitalIOControl_5", self.comm)
    self.DigitalIOControl_6 = Gui.DigitalIOControl("DigitalIOControl_6", self.comm)
    self.DigitalIOControl_7 = Gui.DigitalIOControl("DigitalIOControl_7", self.comm)
    self.DigitalIOControl_8 = Gui.DigitalIOControl("DigitalIOControl_8", self.comm)
    self.DigitalIOControl_9 = Gui.DigitalIOControl("DigitalIOControl_9", self.comm)
    self.DigitalIOControl_10 = Gui.DigitalIOControl("DigitalIOControl_10", self.comm)
    self.DigitalIOControl_11 = Gui.DigitalIOControl("DigitalIOControl_11", self.comm)
    self.DigitalIOControl_12 = Gui.DigitalIOControl("DigitalIOControl_12", self.comm)
    self.DigitalIOControl_13 = Gui.DigitalIOControl("DigitalIOControl_13", self.comm)
    self.DigitalIOControl_14 = Gui.DigitalIOControl("DigitalIOControl_14", self.comm)
    self.DigitalIOControl_15 = Gui.DigitalIOControl("DigitalIOControl_15", self.comm)
    self.DigitalIOControl_16 = Gui.DigitalIOControl("DigitalIOControl_16", self.comm)
    self.PathView_1 = Gui.SimGLWidget("PathView_1", self.comm)
    self.PathView_2 = Gui.SimGLWidget("PathView_2", self.comm)
    self.PathView_3 = Gui.SimGLWidget("PathView_3", self.comm)
    self.PathView_4 = Gui.SimGLWidget("PathView_4", self.comm)
    self.btnStart = Gui.ToolButton("btnStart", self.comm)
    self.btnStop = Gui.ToolButton("btnStop", self.comm)
    self.btnPause = Gui.ToolButtonWithLed("btnPause", self.comm)
    self.btnRewind = Gui.ToolButton("btnRewind", self.comm)
    self.btnSpindle = Gui.ToolButtonWithProgress("btnSpindle", self.comm)
    self.btnFlood = Gui.ToolButtonWithLed("btnFlood", self.comm)
    self.btnMist = Gui.ToolButtonWithLed("btnMist", self.comm)
    self.btnEnable1 = Gui.ToolButtonWithLed("btnEnable1", self.comm)
    self.scrollRightPanel = Gui.ScrollArea("scrollRightPanel", self.comm)
    self.grJog = Gui.GroupBox("grJog", self.comm)
    self.cbKeyJogEnable = Gui.CheckBox("cbKeyJogEnable", self.comm)
    self.lbJogMode = Gui.Label("lbJogMode", self.comm)
    self.btnJogMode = Gui.ToolButton("btnJogMode", self.comm)
    self.lbJogStep = Gui.Label("lbJogStep", self.comm)
    self.edJogStep = Gui.LineEdit("edJogStep", self.comm)
    self.btnJogStepCycle = Gui.ToolButton("btnJogStepCycle", self.comm)
    self.slJogSpeed = Gui.HorizontalSlider("slJogSpeed", self.comm)
    self.btnJogSpeedSlow = Gui.ToolButton("btnJogSpeedSlow", self.comm)
    self.edJogSpeed = Gui.LineEdit("edJogSpeed", self.comm)
    self.btnJogSpeedFast = Gui.ToolButton("btnJogSpeedFast", self.comm)
    self.tabJog = Gui.TabWidget("tabJog", self.comm)
    self.frJogXYZ = Gui.Frame("frJogXYZ", self.comm)
    self.btnJogZPos = Gui.PushButton("btnJogZPos", self.comm)
    self.btnJogYPos = Gui.PushButton("btnJogYPos", self.comm)
    self.btnJogZNeg = Gui.PushButton("btnJogZNeg", self.comm)
    self.btnJogXPos = Gui.PushButton("btnJogXPos", self.comm)
    self.btnJogYNeg = Gui.PushButton("btnJogYNeg", self.comm)
    self.btnJogXNeg = Gui.PushButton("btnJogXNeg", self.comm)
    self.frJogABC = Gui.Frame("frJogABC", self.comm)
    self.btnJogANeg = Gui.PushButton("btnJogANeg", self.comm)
    self.btnJogBNeg = Gui.PushButton("btnJogBNeg", self.comm)
    self.btnJogCPos = Gui.PushButton("btnJogCPos", self.comm)
    self.btnJogCNeg = Gui.PushButton("btnJogCNeg", self.comm)
    self.btnJogBPos = Gui.PushButton("btnJogBPos", self.comm)
    self.btnJogAPos = Gui.PushButton("btnJogAPos", self.comm)
    self.grFro = Gui.GroupBox("grFro", self.comm)
    self.edFro = Gui.LineEdit("edFro", self.comm)
    self.btnFro150 = Gui.ToolButton("btnFro150", self.comm)
    self.btnFro125 = Gui.ToolButton("btnFro125", self.comm)
    self.btnFro100 = Gui.ToolButton("btnFro100", self.comm)
    self.btnFro50 = Gui.ToolButton("btnFro50", self.comm)
    self.btnFro25 = Gui.ToolButton("btnFro25", self.comm)
    self.slFro = Gui.VerticalSlider("slFro", self.comm)
    self.lbFeedrate = Gui.Label("lbFeedrate", self.comm)
    self.edFeedrate = Gui.LineEdit("edFeedrate", self.comm)
    self.lbOvFeedrate = Gui.Label("lbOvFeedrate", self.comm)
    self.edOvFeedrate = Gui.LineEdit("edOvFeedrate", self.comm)
    self.lbCurrFeedrate = Gui.Label("lbCurrFeedrate", self.comm)
    self.edCurrFeedrate = Gui.LineEdit("edCurrFeedrate", self.comm)
    self.grSro = Gui.GroupBox("grSro", self.comm)
    self.edSro = Gui.LineEdit("edSro", self.comm)
    self.btnSro150 = Gui.ToolButton("btnSro150", self.comm)
    self.btnSro125 = Gui.ToolButton("btnSro125", self.comm)
    self.btnSro100 = Gui.ToolButton("btnSro100", self.comm)
    self.btnSro50 = Gui.ToolButton("btnSro50", self.comm)
    self.btnSro25 = Gui.ToolButton("btnSro25", self.comm)
    self.slSro = Gui.VerticalSlider("slSro", self.comm)
    self.lbSpindleRpm = Gui.Label("lbSpindleRpm", self.comm)
    self.edSpindleRpm = Gui.LineEdit("edSpindleRpm", self.comm)
    self.lbSpindleOvRpm = Gui.Label("lbSpindleOvRpm", self.comm)
    self.edSpindleOvRpm = Gui.LineEdit("edSpindleOvRpm", self.comm)
    self.lbSpindleTrueRpm = Gui.Label("lbSpindleTrueRpm", self.comm)
    self.edSpindleTrueRpm = Gui.LineEdit("edSpindleTrueRpm", self.comm)
