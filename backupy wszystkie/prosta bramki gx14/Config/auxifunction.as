--get_inport_state 	获得输入端口的状态，只能返回false或true，不能用0来表示false。
--get_outport_state	获得输出端口的状态，只能返回false或true，不能用0来表示false。
--set_outport       设置输入端口状态，可以用0和1表示false和true
--start_process			程序开始
--sys_stop					程序停止
--run_gcode					执行G代码
--get_state					获取当前系统状态
--get_mode					获取当前系统模式
--get_page_row			获取当前的一级菜单项
--show_message			在警报栏显示信息
--show_message_box	以对话框方式显示信息
--get_lang_version	获取系统语言
--get_tool_index		获取当前刀具号
--is_bkref					是否已回原点
--set_mode					设置当前系统模式
--set_state					设置当前系统状态
--get_tick_count		获取当前计数器的计数
--get_rparam        获取#变量
--set_rparam        设置#变量

--系统的状态：IDLE_STATE，IDLE_STATE，ESTOP_STATE，RUN_STATE，PAUSING_STATE
--系统的模式：BKREF_MODE，AUTO_MODE，JOG_MODE，INC_MODE，MDI_MODE

--模式
BKREF_MODE = 0x0100;
AUTO_MODE = 0x0200;
JOG_MODE = 0x0300;
INC_MODE = 0x0400;
MDI_MODE = 0x0500;

--对话框返回值
IDOK = 1
IDCANCEL = 0

--状态
IDLE_STATE = 0x0001;
LOCK_STATE = 0x0002;
ESTOP_STATE = 0x0003;
RUN_STATE = 0x0004;
PAUSING_STATE = RUN_STATE + 1;

--手持盒LED状态灯 对应值是逻辑地址 逻辑地址如果发生变化其也应该变化
LED_RUN         = 19
LED_SPIN        = 20
LED_ALM         = 21
LED_GY18        = 22
LED_GY19        = 23
LED_GY20        = 24

s_szILLEGAL_ASSISTANTOPER = {"|E|非法操作！", "|E|Illegal Operation"};
s_szPROMPT_RUNSPINDLE = {"|E|系统处于紧停状态, 不能启动主轴!", "|E|Spindle can't be started while system is under E-stop state!"};
s_szPROMPT_STARTSPINDLE = {"|E|当前系统状态禁止启动主轴!", "|E|Spindle is forbidden to start in current system state!"};
s_szPROMPT_SPINDLEOFF = {"正在加工，真的停止主轴吗？", "It's machining now! Do you really intend to stop the spindle?"};

--220ms定时器				         
function ExIOFunction()
	--_bStartInport = get_inport_state(46)
	--_bStopInport = get_inport_state(47)
		
end

--K1按键
function AssistantK1Func()
	_bHasInport = get_outport_state(5);
	if _bHasInport then
		set_outport(5, 0);
	else
		set_outport(5, 1);
	end		
end

--K2按键
function AssistantK2Func()
	_bHasInport = get_outport_state(7);
	if _bHasInport then
		set_outport(7, 0);
	else
		set_outport(7, 1);
	end		
end

--此功能键目前只能在空闲状态下生效
--主轴启动
function axis_on()
	_state = get_state();
	_mode  = get_mode();
	_nLangVer = get_lang_version();
	if (_state == ESTOP_STATE) then
		show_message_box(s_szPROMPT_RUNSPINDLE[_nLangVer]);
		return;
	elseif (_state == RUN_STATE and (_mode == BKREF_MODE or _mode == MDI_MODE)) then
		show_message(s_szPROMPT_STARTSPINDLE[_nLangVer])
		return;			
	end
	
	set_outport(1, 1);
	set_outport(6, 1);	
end

--此功能键目前只能在空闲状态下生效
--主轴停止
function axis_off()
	_state = get_state();
	_mode  = get_mode();
	_nLangVer = get_lang_version();
	if ((get_outport_state(1) == 1) and (_state == RUN_STATE or _state == PAUSING_STATE)) then
		if show_message_box(s_szPROMPT_SPINDLEOFF[_nLangVer]) == IDCANCEL then;
			return;	
		end
	end
	
	set_outport(1, 0);
	set_outport(6, 0);	
end

--程序开始
function start_auxiop()
	return true
end

--程序停止
function stop_auxiop()
	return true
end

--断点继续
function resume_auxiop()
	return true
end

--提供10组自定义组合键
function AssistantShift1Func()
end

function AssistantShift2Func()
end

function AssistantShift3Func()
end

function AssistantShift4Func()
end

function AssistantShift5Func()
end

function AssistantShift6Func()
end

function AssistantShift7Func()
end

function AssistantShift8Func()
end

function AssistantShift9Func()
end

function AssistantShift10Func()
end

--LED显示 定时器调用
function on_led()
	_state = get_state();
	
	--RUN_LED
	if _state == RUN_STATE or _state == PAUSING_STATE then
		 set_outport(LED_RUN, 1)
	else
	   set_outport(LED_RUN, 0)
	end
	
	--SPIN_LED
	if get_outport_state(1) then
		 set_outport(LED_SPIN, 1)
	else
	   set_outport(LED_SPIN, 0)
	end
	
	--ALM_LED
	if _state == ESTOP_STATE then
		 set_outport(LED_ALM, 1)
	else
	   set_outport(LED_ALM, 0)
	end
	
	--GY18_LED
	if get_outport_state(5) then
		 set_outport(LED_GY18, 1)
	else
	   set_outport(LED_GY18, 0)
	end
	
	--GY19_LED
	if get_outport_state(6) then
		 set_outport(LED_GY19, 1)
	else
	   set_outport(LED_GY19, 0)
	end
	
	--GY20_LED
	if get_outport_state(7) then
		 set_outport(LED_GY20, 1)
	else
	   set_outport(LED_GY20, 0)
	end
end