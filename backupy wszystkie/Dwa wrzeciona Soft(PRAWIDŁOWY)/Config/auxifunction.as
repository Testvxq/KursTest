--get_inport_state 	�������˿ڵ�״̬��ֻ�ܷ���false��true��������0����ʾfalse��
--get_outport_state	�������˿ڵ�״̬��ֻ�ܷ���false��true��������0����ʾfalse��
--set_outport       ��������˿�״̬��������0��1��ʾfalse��true
--start_process			����ʼ
--sys_stop					����ֹͣ
--run_gcode					ִ��G����
--get_state					��ȡ��ǰϵͳ״̬
--get_mode					��ȡ��ǰϵͳģʽ
--get_page_row			��ȡ��ǰ��һ���˵���
--show_message			�ھ�������ʾ��Ϣ
--show_message_box	�ԶԻ���ʽ��ʾ��Ϣ
--get_lang_version	��ȡϵͳ����
--get_tool_index		��ȡ��ǰ���ߺ�
--is_bkref					�Ƿ��ѻ�ԭ��
--set_mode					���õ�ǰϵͳģʽ
--set_state					���õ�ǰϵͳ״̬
--get_tick_count		��ȡ��ǰ�������ļ���
--get_rparam        ��ȡ#����
--set_rparam        ����#����

--ϵͳ��״̬��IDLE_STATE��IDLE_STATE��ESTOP_STATE��RUN_STATE��PAUSING_STATE
--ϵͳ��ģʽ��BKREF_MODE��AUTO_MODE��JOG_MODE��INC_MODE��MDI_MODE

--ģʽ
BKREF_MODE = 0x0100;
AUTO_MODE = 0x0200;
JOG_MODE = 0x0300;
INC_MODE = 0x0400;
MDI_MODE = 0x0500;

--�Ի��򷵻�ֵ
IDOK = 1
IDCANCEL = 0

--״̬
IDLE_STATE = 0x0001;
LOCK_STATE = 0x0002;
ESTOP_STATE = 0x0003;
RUN_STATE = 0x0004;
PAUSING_STATE = RUN_STATE + 1;

--�ֳֺ�LED״̬�� ��Ӧֵ���߼���ַ �߼���ַ��������仯��ҲӦ�ñ仯
LED_RUN         = 19
LED_SPIN        = 20
LED_ALM         = 21
LED_GY18        = 22
LED_GY19        = 23
LED_GY20        = 24

s_szILLEGAL_ASSISTANTOPER = {"|E|�Ƿ�������", "|E|Illegal Operation"};
s_szPROMPT_RUNSPINDLE = {"|E|ϵͳ���ڽ�ͣ״̬, ������������!", "|E|Spindle can't be started while system is under E-stop state!"};
s_szPROMPT_STARTSPINDLE = {"|E|��ǰϵͳ״̬��ֹ��������!", "|E|Spindle is forbidden to start in current system state!"};
s_szPROMPT_SPINDLEOFF = {"���ڼӹ������ֹͣ������", "It's machining now! Do you really intend to stop the spindle?"};
s_szPROMPT_OPERATORFAILED = {"|F|ϵͳæ������ִ�е�ǰ������", "|F|System is busy, current operation fails!"};
s_szENSURE_SPINDLEON = {"ȷ�ϴ�����?", "Is confirm  open spindle"};

--220ms��ʱ��				         
function ExIOFunction()
	--_bStartInport = get_inport_state(46)
	--_bStopInport = get_inport_state(47)

	if (get_inport_state(17)) then
		set_outport(27, 1);
	else
		set_outport(27, 0);
	end
end

--K1����
function AssistantK1Func()
--	_bHasInport = get_outport_state(5);
--	if _bHasInport then
--		set_outport(5, 0);
--	else
--		set_outport(5, 1);
--	end	
	show_message_box("KLAWISZ K1");
	--run_gcode("G65 P16 L1");
end

--K2����
function AssistantK2Func()
--	_bHasInport = get_outport_state(7);
--	if _bHasInport then
--		set_outport(7, 0);
--	else
--		set_outport(7, 1);
--	end	
	show_message_box("KLAWISZ K2");
	--run_gcode("G65 P17 L1");
end

--�˹��ܼ�Ŀǰֻ���ڿ���״̬����Ч
--��������
function axis_on()
	_state = get_state();
	_mode  = get_mode();
	_nLangVer = get_lang_version();
	if (_state == ESTOP_STATE) then
		show_message_box(s_szPROMPT_RUNSPINDLE[_nLangVer]);
		return;
	elseif (_state == RUN_STATE and (_mode == BKREF_MODE or _mode == MDI_MODE)) then
		show_message(s_szPROMPT_OPERATECYLINDER[_nLangVer])
		return;			
	end
	
	if show_message_box(s_szENSURE_SPINDLEON[_nLangVer]) == IDCANCEL then;
		return;	
	end
	
	set_outport(1, 1);
	set_outport(6, 1);	
end

--�˹��ܼ�Ŀǰֻ���ڿ���״̬����Ч
--����ֹͣ
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

--�ṩ5���Զ�����ϼ�
function AssistantShift1Func()
	_nLangVer = get_lang_version();
	if get_state() ~= IDLE_STATE then
		show_message(s_szPROMPT_OPERATORFAILED[_nLangVer])
		return
	end

	if get_mode()~= JOG_MODE then
		return
	end
	
	if get_outport_state(25) then		
		set_outport(25, 0)
	else
		set_mode(MDI_MODE)
		set_outport(26, 0)
		set_outport(27, 0)
		run_gcode("N1 G53 G00 G90 Z=#CTUP;\r\nG906;\r\nG04 P200;\r\nG906;\r\n M901 H25 P1;\r\nG906;\r\nM903 H1")
	end
		
end

function AssistantShift2Func()
	_nLangVer = get_lang_version();
	if get_state() ~= IDLE_STATE then
		show_message(s_szPROMPT_OPERATORFAILED[_nLangVer])
		return
	end
	
	if get_mode()~= JOG_MODE then
		return
	end
	
	if get_outport_state(26) then
		set_outport(26, 0)
	else
		set_mode(MDI_MODE)
		set_outport(25, 0)
		set_outport(27, 0)
		run_gcode("N1 G53 G00 G90 Z=#CTUP;\r\nG906;\r\nG04 P200;\r\nG906;\r\n M901 H26 P1;\r\nG906;\r\nM903 H2")
	end
	
end

function AssistantShift3Func()
end

function AssistantShift4Func()
end

function AssistantShift5Func()
end

--LED��ʾ ��ʱ������
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
	if get_outport_state(25) then
		 set_outport(LED_GY18, 1)
	else
	   set_outport(LED_GY18, 0)
	end
	
	--GY19_LED
	if get_outport_state(26) then
		 set_outport(LED_GY19, 1)
	else
	   set_outport(LED_GY19, 0)
	end
	
	--GY20_LED
	if get_outport_state(27) then
		 set_outport(LED_GY20, 1)
	else
	   set_outport(LED_GY20, 0)
	end
end