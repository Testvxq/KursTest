ResTable = {
    ["langTable"] = {
        "CHN",
        "POL",
        "ENG",
    },
    ["szModule"] = "Interpolate",
    ["nVersion"] = "1.00",
["strTable"] = {

    [L"|E|代码解释器忙，当前加工状态不能执行该操作"] = {
                   [L"CHN"] = L"|E|代码解释器忙，当前加工状态不能执行该操作",
                   [L"POL"] = L"|E|Analizator jest zajety, operacja ta nie moze zostac zrealizowana w aktualnym stanie",
                   [L"ENG"] = L"|E|The parser is busy, this operation is unavailable in current state",},

    [L"|E|驱动错误：运动控制卡硬件中断设置失败"] = {
                   [L"CHN"] = L"|E|驱动错误：运动控制卡硬件中断设置失败",
                   [L"POL"] = L"|E|Blad Sterownika: Karta kontroli ruchu nie mogla zostac ustawiona w wyniku przerwania",
                   [L"ENG"] = L"|E|Driver Error: Motion control card setting fails due to interruption",},
                   
    [L"从备份文件恢复动态参数文件失败，错误码：%d\n"] = {
                   [L"CHN"] = L"从备份文件恢复动态参数文件失败，错误码：%d\n",
                   [L"POL"] = L"|S|Nieudane odzyskanie pliku .dyn z pliku .bak. Kod bledu:%d\n",
                   [L"ENG"] = L"|S|Fail to recover .dyn file from .bak file. ErrorCode:%d\n",},

    [L"|W|丝杠补偿数据读入失败"] = {
                   [L"CHN"] = L"|W|丝杠补偿数据读入失败",
                   [L"POL"] = L"|W|Nieudana proba odczytu axeserr.dat",
                   [L"ENG"] = L"|W|Unable to read axeserr.dat properly",},

    [L"|W|读入动态数据文件(%s)错误：%s。"] = {
                   [L"CHN"] = L"|W|读入动态数据文件(%s)错误：%s。",
                   [L"POL"] = L"|W|Odczyt z pliku danych dynamicznych (%s) blad: %s.",
                   [L"ENG"] = L"|W|Read in the dynamic data file(%s) error: %s.",},

    [L"|E|驱动错误：内存不足"] = {
                   [L"CHN"] = L"|E|驱动错误：内存不足",
                   [L"POL"] = L"|E|Blad sterownika: Brak dostatecznej ilosci pamieci",
                   [L"ENG"] = L"|E|Driver Error: No enough memory",},

    [L"[%[^]]]"] = {
                   [L"CHN"] = L"[%[^]]]",
                   [L"POL"] = L"[%[^]]]",
                   [L"ENG"] = L"[%[^]]]",},

    [L"更新轴误差数据文件成功!"] = {
                   [L"CHN"] = L"更新轴误差数据文件成功!",
                   [L"POL"] = L"Udana atualizacja pliku bledu osi!",
                   [L"ENG"] = L"Update axis error data file successfully!",},

    [L"|E|主轴转速百分比范围超限"] = {
                   [L"CHN"] = L"|E|主轴转速百分比范围超限",
                   [L"POL"] = L"|E|Procentowy stopien obrotow wrzeciona poza zakresem",
                   [L"ENG"] = L"|E|Out of limit of spindle RPM percentage",},
                   
    [L"系统检测到某些参数配置不正确，请删除配置文件并重新配置参数"] = {
                   [L"CHN"] = L"系统检测到某些参数配置不正确，请删除配置文件并重新配置参数",
                   [L"POL"] = L"System wykryl niewlasciwa konfiguracje parametrow. Prosze o usuniecie pliku i ponowna konfiguracje.",
                   [L"ENG"] = L"System detects some inaccurate parameter configurations which need to reconfigure.Please delete the file and configure the parameters again.",},

    [L"|M|读取注册信息失败!"] = {
                   [L"CHN"] = L"|M|读取注册信息失败!",
                   [L"POL"] = L"|M|Nieudana proba odczytania informacji dot. rejestracji!",
                   [L"ENG"] = L"|M|Fail to read registration info!",},

    [L"|W|上次操作尚未结束，不能执行本操作"] = {
                   [L"CHN"] = L"|W|上次操作尚未结束，不能执行本操作",
                   [L"POL"] = L"|W|Nieudana proba wykonania dzialania, poniewaz poprzednie nie zostalo dokonczone",
                   [L"ENG"] = L"|W|Unable to perform the action because the last one has not completed yet",},

    [L"|E|驱动错误：非法的轴号"] = {
                   [L"CHN"] = L"|E|驱动错误：非法的轴号",
                   [L"POL"] = L"|E|Blad sterownika: Niedozwolony numer osi",
                   [L"ENG"] = L"|E|Driver Error: Illegal axis number",},

    [L"没有找到合适的硬件设备，是否使用仿真版？"] = {
                   [L"CHN"] = L"没有找到合适的硬件设备，是否使用仿真版？",
                   [L"POL"] = L"Brak sprzetu, uzyc sterownika symulacji?",
                   [L"ENG"] = L"No hardware is found, use simu driver instead?",},

    [L"|E|驱动错误：传入参数错误"] = {
                   [L"CHN"] = L"|E|驱动错误：传入参数错误",
                   [L"POL"] = L"|E|Blad sterownika: Bledny import parametru.",
                   [L"ENG"] = L"|E|Driver Error: Something is wrong with parameter import.",},

    [L"|E|进给百分比范围超限"] = {
                   [L"CHN"] = L"|E|进给百分比范围超限",
                   [L"POL"] = L"|E|Poza zakresem posuwu",
                   [L"ENG"] = L"|E|Out of limit of feedrate percentage",},

    [L"|F|软件试用期已过，请与供应商联系"] = {
                   [L"CHN"] = L"|F|软件试用期已过，请与供应商联系",
                   [L"POL"] = L"|F|Waznosc aplikacji wygasla. Prosze skontaktowac sie z dostawca",
                   [L"ENG"] = L"|F|The application probation is expired. Please contact with the supplier",},

    [L"|F|创建内核定时器失败"] = {
                   [L"CHN"] = L"|F|创建内核定时器失败",
                   [L"POL"] = L"|F|Nieudana proba stworzenia licznika jadra",
                   [L"ENG"] = L"|F|Unable to create a kernel timer",},

    [L"|E|行程限位开关触发"] = {
                   [L"CHN"] = L"|E|行程限位开关触发",
                   [L"POL"] = L"|E|Ogranicznik Krancowy Wlaczony",
                   [L"ENG"] = L"|E|Limit Switch On",},

    [L"|E|不正确的参数设置。参数(名称%s)超出范围。"] = {
                   [L"CHN"] = L"|E|不正确的参数设置。参数(名称%s)超出范围。",
                   [L"POL"] = L"|E|Niewlasciwe ustawienie parametru! Parametr (name%s) jest poza zakresem.",
                   [L"ENG"] = L"|E|Incorrect parameter setting! The Parameter (name%s) is out of the range.",},

    [L"|W|驱动警告：内部忙"] = {
                   [L"CHN"] = L"|W|驱动警告：内部忙",
                   [L"POL"] = L"|W|Ostrzezenie sterownika",
                   [L"ENG"] = L"|W|Driver Warning: Inner busy",},
                   
    [L"初始化硬件失败!"] = {
                   [L"CHN"] = L"初始化硬件失败!",
                   [L"POL"] = L"Nieudana proba uruchomienia sprzetu!",
                   [L"ENG"] = L"Fail to initialize the hardware!",},

    [L"|E|驱动错误：操作系统内核错误"] = {
                   [L"CHN"] = L"|E|驱动错误：操作系统内核错误",
                   [L"POL"] = L"|E|Blad Sterownika: Wystapily bledy jadra systemu",
                   [L"ENG"] = L"|E|Driver Error: There are OS kernel errors",},
                   
    [L"|E|驱动错误：无效的机器状态(MODESTATE)"] = {
                   [L"CHN"] = L"|E|驱动错误：无效的机器状态(MODESTATE)",
                   [L"POL"] = L"|E|Blad sterownika: Niewlasciwy tryb",
                   [L"ENG"] = L"|E|Driver Error: Invalid mode-state",},

    [L"|E|主轴转速范围超限"] = {
                   [L"CHN"] = L"|E|主轴转速范围超限",
                   [L"POL"] = L"|E|Predkosc obrotowa wrzeciona poza zakresem",
                   [L"ENG"] = L"|E|Out of range of spindle RPM",},
                   
    [L"确定更新轴误差数据文件？"] = {
                   [L"CHN"] = L"确定更新轴误差数据文件？",
                   [L"POL"] = L"Czy jestes pewny, ze chcesz aktualizowac plik osi ?",
                   [L"ENG"] = L"Are you sure to update the axis error file ?",},

    [L"|E|紧停按钮没有释放或者存在其它报警点"] = {
                   [L"CHN"] = L"|E|紧停按钮没有释放或者存在其它报警点",
                   [L"POL"] = L"|E|Stop Awaryjny zostal wcisniety (zablokowany)",
                   [L"ENG"] = L"|E|EMERGENCY-STOP Button is pressed(locked) or there are other alarm points",},

    [L"|F|内部错误：没有足够内存，建议关闭一些其它应用程序，或者退出本系统"] = {
                   [L"CHN"] = L"|F|内部错误：没有足够内存，建议关闭一些其它应用程序，或者退出本系统",
                   [L"POL"] = L"|F|Blad wewnetrzny: Brak dostatecznej ilosci pamiei. Prosze zamknij pozostale aplikacje lub wylacz system",
                   [L"ENG"] = L"|F|Internal Error: No Enough Memory. Please close other applications or exit from this system",},

    [L"拷贝轴误差数据文件失败!"] = {
                   [L"CHN"] = L"拷贝轴误差数据文件失败!",
                   [L"POL"] = L"Nieudana operacja kopiowania, blad osi w pliku!",
                   [L"ENG"] = L"Fail to copy axis error data file!",},

    [L"|E|驱动错误：驱动程序版本不兼容"] = {
                   [L"CHN"] = L"|E|驱动错误：驱动程序版本不兼容",
                   [L"POL"] = L"|E|Blad sterownika: Wersja sterownika jest niekompatybilna.",
                   [L"ENG"] = L"|E|Driver Error: Version of the driver is not compatible",},

    [L"|W|丝杠补偿数据(行%d)：数据格式或者轴名称不正确"] = {
                   [L"CHN"] = L"|W|丝杠补偿数据(行%d)：数据格式或者轴名称不正确",
                   [L"POL"] = L"|W|BLAD AXESERR.DAT (wiersz %d): Niewlasciwy format danych lub nazwa osi",
                   [L"ENG"] = L"|W|AXESERR.DAT ERROR(row %d): Invalid data format or axis name",},

    [L"|E|加工程序运行错误（第%d行）："] = {
                   [L"CHN"] = L"|E|加工程序运行错误（第%d行）：",
                   [L"POL"] = L"|E|Blad uruchomienia pliku NC (linia %d): ",
                   [L"ENG"] = L"|E|NC file running error(line %d): ",},

    [L"|E|系统错误：%08X (请将此错误代码告诉供应商以便查找错误)"] = {
                   [L"CHN"] = L"|E|系统错误：%08X (请将此错误代码告诉供应商以便查找错误)",
                   [L"POL"] = L"|E|Blad systemowy: %08X,(prosze wyslij kod bledu dostawcy)",
                   [L"ENG"] = L"|E|System Error: %08X,(please send the error code to the supplier to search for the error)",},

    [L"|E|驱动错误：当前不支持的功能"] = {
                   [L"CHN"] = L"|E|驱动错误：当前不支持的功能",
                   [L"POL"] = L"|E|Blad sterownika: Nieobslugiwana funkcja",
                   [L"ENG"] = L"|E|Driver Error: Unsupported function",},

    [L"|M|加工文件信息文件加载失败!"] = {
                   [L"CHN"] = L"|M|加工文件信息文件加载失败!",
                   [L"POL"] = L"|M|Nieudana proba wczytania programu!",
                   [L"ENG"] = L"|M|Fail to load the info file of machining file!",},

    [L"|E|驱动错误：无效的UPDATEBOOL命令"] = {
                   [L"CHN"] = L"|E|驱动错误：无效的UPDATEBOOL命令",
                   [L"POL"] = L"|E|Blad sterownika: Niepoprawna komenda UPDATEBOOL",
                   [L"ENG"] = L"|E|Driver Error: Illegal UPDATEBOOL command",},

    [L"|E|驱动错误：无效的NCCMD结构"] = {
                   [L"CHN"] = L"|E|驱动错误：无效的NCCMD结构",
                   [L"POL"] = L"|E|Blad sterownika: Niepoprawna struktura NCCMD",
                   [L"ENG"] = L"|E|Driver Error: Invalid NCCMD structure",},

    [L"没有找到轴误差数据文件!"] = {
                   [L"CHN"] = L"没有找到轴误差数据文件!",
                   [L"POL"] = L" Blad braku osi w pliku!",
                   [L"ENG"] = L" No axis error file was found!",},

    [L"|M|程序在上次非正常退出"] = {
                   [L"CHN"] = L"|M|程序在上次非正常退出",
                   [L"POL"] = L"|M|Ostatnie wyjscie z aplikacji nie bylo poprawne.",
                   [L"ENG"] = L"|M|The last exit from the application is abnormal.",},

    [L"|W|当前加工模式并非增量模式，请切换到增量模式后，再执行该指令"] = {
                   [L"CHN"] = L"|W|当前加工模式并非增量模式，请切换到增量模式后，再执行该指令",
                   [L"POL"] = L"|W|To nie jest tryb INC. Przelacz do trybu INC a nastepnie wykonaj kod ponownie",
                   [L"ENG"] = L"|W|Not INC Mode. Please switch to INC mode then perform the code again",},

    [L"|F|硬件操作失败，强烈建议重新启动程序，并检查硬件故障"] = {
                   [L"CHN"] = L"|F|硬件操作失败，强烈建议重新启动程序，并检查硬件故障",
                   [L"POL"] = L"|F|Blad sprzetowy. Prosze zrestartuj aplikacje a nastepnie sprawdz sprzet",
                   [L"ENG"] = L"|F|Hardware Failure. Please restart the application and then check the hardware",},

    [L"|E|驱动错误：运动控制卡硬件没有正确初始化"] = {
                   [L"CHN"] = L"|E|驱动错误：运动控制卡硬件没有正确初始化",
                   [L"POL"] = L"|E|Blad sterownika: Urzadzenie nie zostalo poprawnie uruchomione",
                   [L"ENG"] = L"|E|Driver Error: The device is not initialized properly",},
                   
    [L"|E|端口处在锁定状态！"] = {
                   [L"CHN"] = L"|E|端口处在锁定状态！",
                   [L"POL"] = L"|E|Blad sterownika: Port zostal zablokowany.",
                   [L"ENG"] = L"|E|Driver Error: The Port has been locked.",},
                   
    [L"|W|丝杠补偿数据(行%d)：数据项格式不正确"] = {
                   [L"CHN"] = L"|W|丝杠补偿数据(行%d)：数据项格式不正确",
                   [L"POL"] = L"|W|BLAD AXESERR.DAT (wiersz %d): Niepoprawny format danych",
                   [L"ENG"] = L"|W|AXESERR.DAT ERROR(row %d): Invalid data item format",},

    [L"系统自启动任务执行失败"] = {
                   [L"CHN"] = L"系统自启动任务执行失败",
                   [L"POL"] = L"Automatyczne uruchamianie zadan nie udalo sie uruchomic.",
                   [L"ENG"] = L"System self-starting task fails to execute.",},
                   
    [L"启动Adapter工作线程失败!"] = {
                   [L"CHN"] = L"启动Adapter工作线程失败!",
                   [L"POL"] = L"|W|Nieudane uruchomienie zadan",
                   [L"ENG"] = L"|W|Startup Adapter task fails",},

    [L"|F|向加工代码解释器发送命令失败"] = {
                   [L"CHN"] = L"|F|向加工代码解释器发送命令失败",
                   [L"POL"] = L"|F|Nieudane wyslanie komendy do interpretera",
                   [L"ENG"] = L"|F|Fail to send a command to the code interpreter",},

    [L"|F|驱动错误：运动控制卡自检错误，或者其不存在"] = {
                   [L"CHN"] = L"|F|驱动错误：运动控制卡自检错误，或者其不存在",
                   [L"POL"] = L"|F|Blad sterownika: Blad karty kontroli ruchulub jej brak.",
                   [L"ENG"] = L"|F|Driver Error: Something is wrong with self-check of the motion control card or it doesn’t exist.",},

    [L"|F|创建加工代码解释器失败"] = {
                   [L"CHN"] = L"|F|创建加工代码解释器失败",
                   [L"POL"] = L"|F|Niemozliwe stworzenie kodu z interpretera",
                   [L"ENG"] = L"|F|Unable to create the code interpreter",},

    [L"|M|程序在上次非正常退出，非正常退出时加工文件名称'%s'!"] = {
                   [L"CHN"] = L"|M|程序在上次非正常退出，非正常退出时加工文件名称'%s'!",
                   [L"POL"] = L"|M|Ostatnie wyjscie z aplikacji nie bylo poprawne, nazwa pliku to '%s'!",
                   [L"ENG"] = L"|M|The last exit from the application is abnormal, and the processing file name is '%s'!",},

    [L"|M|更改工件坐标[G%d]: "] = {
                   [L"CHN"] = L"|M|更改工件坐标[G%d]: ",
                   [L"POL"] = L"|M|Zmien aktualne wspolrzedne czesci [G%d]: ",
                   [L"ENG"] = L"|M|Change the current work-piece coordinate[G%d]: ",},

    [L"|M|文件'%s'紧停终止"] = {
                   [L"CHN"] = L"|M|文件'%s'紧停终止",
                   [L"POL"] = L"|M|Plik '%s' zostal nagle przerwany",
                   [L"ENG"] = L"|M|File '%s' is emergently stopped",},

    [L"|F|加工代码解释器响应超时，发送命令可能失败"] = {
                   [L"CHN"] = L"|F|加工代码解释器响应超时，发送命令可能失败",
                   [L"POL"] = L"|F|Komenda moze nie zostac wyslana poprzez opoznienie interpretera.",
                   [L"ENG"] = L"|F|Command may fail to send out due to response timeout of code interpreter.",},

    [L"|F|创建、打开或者读写文件失败"] = {
                   [L"CHN"] = L"|F|创建、打开或者读写文件失败",
                   [L"POL"] = L"|F|Niemozliwe stworzenie, otwarcie lub dostep do pliku",
                   [L"ENG"] = L"|F|Unable to create, open or access a file",},
                   
    [L"|M|文件'%s'正常完毕"] = {
                   [L"CHN"] = L"|M|文件'%s'正常完毕",
                   [L"POL"] = L"|M|Plik '%s' zostal zakonczony pomyslnie.",
                   [L"ENG"] = L"|M|File '%s' is completed successfully",},

    [L"|M|更新剩余时间失败!"] = {
                   [L"CHN"] = L"|M|更新剩余时间失败!",
                   [L"POL"] = L"|M|Nie udalo sie wykonac aktualizacji!",
                   [L"ENG"] = L"|M|Fail to update remaining days!",},

    [L""] = {
                   [L"CHN"] = L"",
                   [L"POL"] = L"",
                   [L"ENG"] = L"",},
                   
    [L"|M|文件'%s'异常终止"] = {
                   [L"CHN"] = L"|M|文件'%s'异常终止",
                   [L"POL"] = L"|M|Plik '%s' nieoczekiwanie został zamknięty",
                   [L"ENG"] = L"|M|File '%s' is unexpectedly aborted",},

    [L"加工文件读取异常"] = {
                   [L"CHN"] = L"加工文件读取异常",
                   [L"POL"] = L"Nie mozna odczytac pliku.",
                   [L"ENG"] = L"Fail to read process file.",},


    [L"二进制文件..."] = {
                   [L"CHN"] = L"二进制文件...",
                   [L"POL"] = L"plik binarny...",
                   [L"ENG"] = L"binary file...",},
                   
    [L"|W|丝杠补偿数据(行%d)：不能识别的数据单位或数据格式不正确"] = {
                   [L"CHN"] = L"|W|丝杠补偿数据(行%d)：不能识别的数据单位或数据格式不正确",
                   [L"POL"] = L"|W|BLAD AXESERR.DAT (wiersz %d): Nierozpoznane dane lub niewlasciwy format danych",
                   [L"ENG"] = L"|W|AXESERR.DAT ERROR(row %d): Unrecognized data unit or invalid data format",},


    [L"|F|您使用的是非法软件，请打电话举报：021-33587550"] = {
                   [L"CHN"] = L"|F|您使用的是非法软件，请打电话举报：021-33587550",
                   [L"POL"] = L"|F|Aplikacja, ktorej uzywasz nie jest legalna, dzwon pod numer 15 838 10 60",
                   [L"ENG"] = L"|F|The application you used is illegal, Please call +8621-33587550 for report",},

    [L"是否用缺省G00速度和Gxx速度屏蔽文件中速度"] = {
                   [L"CHN"] = L"是否用缺省G00速度和Gxx速度屏蔽文件中速度",
                   [L"POL"] = L"Czy uzywac domyslnie predkosci G00 i Gxx zamiast podanej w programie",
                   [L"ENG"] = L"Whether to use default G00 speed and Gxx speed instead of file speed",},

    [L"刀具长度"] = {
                   [L"CHN"] = L"刀具长度",
                   [L"POL"] = L"Dlugosc Narzedzia",
                   [L"ENG"] = L"Length Of Tool",},
                   
    [L"|W|当前加工状态不能执行该操作"] = {
                   [L"CHN"] = L"|W|当前加工状态不能执行该操作",
                   [L"POL"] = L"|W|Operacja ta nie moze zostac wykonana w aktualnym stanie!",
                   [L"ENG"] = L"|W|This operation can’t be executed under current status!",},

    [L"|W|驱动警告：当前不在紧停状态"] = {
                   [L"CHN"] = L"|W|驱动警告：当前不在紧停状态",
                   [L"POL"] = L"|W|Blad sterownika: Nie jest wlaczony stop awaryjny",
                   [L"ENG"] = L"|W|Driver Warning: It is not in emergency state now",},

    [L"换刀延时"] = {
                   [L"CHN"] = L"换刀延时",
                   [L"POL"] = L"Czas opoznienia dla wymiany narzedzia",
                   [L"ENG"] = L"Delay time for tool change",},

    [L"IJK编程时起点和终点半径最大容差"] = {
                   [L"CHN"] = L"IJK编程时起点和终点半径最大容差",
                   [L"POL"] = L"Tolerancja maksymalnego promienia pomiedzy punktem poczatkowym a koncowym przy programowaniu z wykorzystaniem IJK",
                   [L"ENG"] = L"The maximum radius tolerance between the start point and the end point during IJK programming",},

    [L"换刀上位"] = {
                   [L"CHN"] = L"换刀上位",
                   [L"POL"] = L"Gorna pozycja wymiany narzedzia",
                   [L"ENG"] = L"Tool change upper position",},

    [L"G00是否不受倍率开关控制"] = {
                   [L"CHN"] = L"G00是否不受倍率开关控制",
                   [L"POL"] = L"G00 nie jest kontrolowane poprzez przelacznik procentowy predkosci",
                   [L"ENG"] = L"G00 is not controlled by override switch",},

    [L"系统类型和平台不匹配!"] = {
                   [L"CHN"] = L"系统类型和平台不匹配!",
                   [L"POL"] = L"Rodzaj systemu nie pasuje do platformy sprzetowej!",
                   [L"ENG"] = L"System type does not match with hardware platform!",},

    [L"使用Z的下刀速度"] = {
                   [L"CHN"] = L"使用Z的下刀速度",
                   [L"POL"] = L"Uzyj predkosci opusczania osi Z",
                   [L"ENG"] = L"Use Z down speed",},

    [L"|E|内部错误：数据流解包错误"] = {
                   [L"CHN"] = L"|E|内部错误：数据流解包错误",
                   [L"POL"] = L"|E|Blad wewnetrzny: Blad rozpakowywania danych",
                   [L"ENG"] = L"|E|Internal Error: Unpacking Data-stream Error",},
                   
    [L"空行程移动时抬刀高度"] = {
                   [L"CHN"] = L"空行程移动时抬刀高度",
                   [L"POL"] = L"Wysokosc podniesienia narzedzia podczas przejazdow szybkich",
                   [L"ENG"] = L"Tool lifting height in rapid traverse",},

    [L"进给倍率对步进和连续进给倍率有效"] = {
                   [L"CHN"] = L"进给倍率对步进和连续进给倍率有效",
                   [L"POL"] = L"Posuw wlasciwy dla przejazdu krokowego i szeregowego",
                   [L"ENG"] = L"Feedrate is valid for stepping and serial",},

    [L"|M|文件'%s'中断终止"] = {
                   [L"CHN"] = L"|M|文件'%s'中断终止",
                   [L"POL"] = L"|M|File '%s' zmuszony do zatrzymania",
                   [L"ENG"] = L"|M|File '%s' is forced to stop",},
                   
    [L"加工结束后提示"] = {
                   [L"CHN"] = L"加工结束后提示",
                   [L"POL"] = L"Komunikat po zakonczeniu obrobki",
                   [L"ENG"] = L"Prompt after machining ends",},

    [L"Y为旋转轴的脉冲当量"] = {
                   [L"CHN"] = L"Y为旋转轴的脉冲当量",
                   [L"POL"] = L"Impulsy dla osi obrotowej Y",
                   [L"ENG"] = L"Pulse equivalent of Y revolving axis",},

    [L"刀具%d"] = {
                   [L"CHN"] = L"刀具%d",
                   [L"POL"] = L"Narzedzie %d",
                   [L"ENG"] = L"Tool %d",},

    [L"回机械原点X轴速度"] = {
                   [L"CHN"] = L"回机械原点X轴速度",
                   [L"POL"] = L"Predkosc X podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"X Speed in backing to reference point",},

    [L"|F|内部错误：创建或使用系统对象失败，建议重新启动本系统"] = {
                   [L"CHN"] = L"|F|内部错误：创建或使用系统对象失败，建议重新启动本系统",
                   [L"POL"] = L"|F|Blad wewnetrzny: Nieudana proba stworzenia obiektu systemowego. Prosze zrestartowac ta aplikacje",
                   [L"ENG"] = L"|F|Internal Error: Fail to Create/Use System Object. Please restart this application",},

    [L"旋转轴以mm为计量单位"] = {
                   [L"CHN"] = L"旋转轴以mm为计量单位",
                   [L"POL"] = L"MM jako jednostka dla osi obrotowej",
                   [L"ENG"] = L"MM as revolving axis unit",},

    [L"短线段最高速度限速长度"] = {
                   [L"CHN"] = L"短线段最高速度限速长度",
                   [L"POL"] = L"Dlugosc dla limitu max predkosci",
                   [L"ENG"] = L"Length for Limit Max velocity",},

    [L"反向间隙补偿有效"] = {
                   [L"CHN"] = L"反向间隙补偿有效",
                   [L"POL"] = L"Uruchomiona kompensacja",
                   [L"ENG"] = L"Backlash compensation valid",},

    [L"Gxx速度"] = {
                   [L"CHN"] = L"Gxx速度",
                   [L"POL"] = L"Predkosc Gxx",
                   [L"ENG"] = L"Gxx Speed",},

    [L"对刀块厚度"] = {
                   [L"CHN"] = L"对刀块厚度",
                   [L"POL"] = L"Grubosc plytki kalibrujacej",
                   [L"ENG"] = L"Cali Block Thickness",},

    [L"Z轴最大速度"] = {
                   [L"CHN"] = L"Z轴最大速度",
                   [L"POL"] = L"Max. predkosc osi Z",
                   [L"ENG"] = L"Max. Z-axis Speed",},

    [L"固定点的Z轴坐标"] = {
                   [L"CHN"] = L"固定点的Z轴坐标",
                   [L"POL"] = L"Wspolrzedna osi Z ustalonego punktu",
                   [L"ENG"] = L"The Z axis coordinate of The Fixed Point",},

    [L"修改刀库容量后需重启方可设置对应的刀具坐标"] = {
                   [L"CHN"] = L"修改刀库容量后需重启方可设置对应的刀具坐标",
                   [L"POL"] = L"Wymagany jest Restart aby ustalic wspolrzedne narzedzia po zmianie pojemnosci magazynka",
                   [L"ENG"] = L"Restart is needed to set related cutter coordinates after modifying tool magazine capacity",},

    [L"起跳速度"] = {
                   [L"CHN"] = L"起跳速度",
                   [L"POL"] = L"Predkosc Poczatkowa",
                   [L"ENG"] = L"Startup Speed",},

    [L"对刀参数"] = {
                   [L"CHN"] = L"对刀参数",
                   [L"POL"] = L"Tool Cali Parameters",
                   [L"ENG"] = L"Tool Cali Parameters",},

    [L"循环加工时间间隔"] = {
                   [L"CHN"] = L"循环加工时间间隔",
                   [L"POL"] = L"Interwal powtorzen",
                   [L"ENG"] = L"Recycle interval",},

    [L"工件偏置"] = {
                   [L"CHN"] = L"工件偏置",
                   [L"POL"] = L"Odsuniecie Przedmiotu obrabianego",
                   [L"ENG"] = L"Workpiece offset",},

    [L"抬刀高度"] = {
                   [L"CHN"] = L"抬刀高度",
                   [L"POL"] = L"Wysokosc podniesienia narzedzia",
                   [L"ENG"] = L"Tool lifting height",},

    [L"粗定位阶段Z轴速度"] = {
                   [L"CHN"] = L"粗定位阶段Z轴速度",
                   [L"POL"] = L"Predkosc Z w zgrubnym pozycjonowaniu",
                   [L"ENG"] = L"Z Speed in coarse positioning",},

    [L"刀间距"] = {
                   [L"CHN"] = L"刀间距",
                   [L"POL"] = L"Krok narzedzia",
                   [L"ENG"] = L"Tool step",},

    [L"G00使用100%进给倍率"] = {
                   [L"CHN"] = L"G00使用100%进给倍率",
                   [L"POL"] = L"Pelny posuw dla G00",
                   [L"ENG"] = L"Full feedrate for G00",},

    [L"空程速度"] = {
                   [L"CHN"] = L"空程速度",
                   [L"POL"] = L"Predkosc biegu jalowego",
                   [L"ENG"] = L"Dry running Speed",},

    [L"主轴初始档位"] = {
                   [L"CHN"] = L"主轴初始档位",
                   [L"POL"] = L"Domyslny poziom wrzeciona",
                   [L"ENG"] = L"Spindle default level",},

    [L"Plt单位"] = {
                   [L"CHN"] = L"Plt单位",
                   [L"POL"] = L"Jednostka Plt",
                   [L"ENG"] = L"Plt Unit",},

    [L"Plt文件翻译参数"] = {
                   [L"CHN"] = L"Plt文件翻译参数",
                   [L"POL"] = L"Parametry translacji pliku Plt",
                   [L"ENG"] = L"Plt file translation parameters",},

    [L"是否使用S形算法"] = {
                   [L"CHN"] = L"是否使用S形算法",
                   [L"POL"] = L"Czy uzywac algorytmu S",
                   [L"ENG"] = L"Whether to use type S algorithm",},

    [L"短线段最高速度限速有效"] = {
                   [L"CHN"] = L"短线段最高速度限速有效",
                   [L"POL"] = L"Maks. limit predkosci dla malych linii",
                   [L"ENG"] = L"Limit Max velocity for small lines",},

    [L"加工速度"] = {
                   [L"CHN"] = L"加工速度",
                   [L"POL"] = L"Predkosc obrobki",
                   [L"ENG"] = L"Machining Speed",},

    [L"短线段最高速度限速参考加速度"] = {
                   [L"CHN"] = L"短线段最高速度限速参考加速度",
                   [L"POL"] = L"Przyspieszenie dla max limitu predkosci",
                   [L"ENG"] = L"Reference Acc for Limit Max velocity",},

    [L"换刀参数"] = {
                   [L"CHN"] = L"换刀参数",
                   [L"POL"] = L"Parametry wymiany narzedzia",
                   [L"ENG"] = L"Tool change parameters",},

    [L"Y轴机械坐标"] = {
                   [L"CHN"] = L"Y轴机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe osi Y",
                   [L"ENG"] = L"Y-axis MachinCoor",},

    [L"G73_G83退刀量"] = {
                   [L"CHN"] = L"G73_G83退刀量",
                   [L"POL"] = L"Wielkosc powrotu G73_G83",
                   [L"ENG"] = L"G73_G83 retract amount",},

    [L"圆弧增量模式有效表示圆心坐标是相对起点，否则相对于工件原点"] = {
                   [L"CHN"] = L"圆弧增量模式有效表示圆心坐标是相对起点，否则相对于工件原点",
                   [L"POL"] = L"Jesli jest wlaczona, wspolrzedne srodka luku sa wzgledem punktu poczatkowego ukladu wspolrzednych przedmiotu obrabianego.",
                   [L"ENG"] = L"If it is valid,the arc center coordinates are relative to the start point.Otherwise they are relative to workpiece origin.",},

    [L"对刀抬刀高度"] = {
                   [L"CHN"] = L"对刀抬刀高度",
                   [L"POL"] = L"Wysokosc po kalibracji narzedzia",
                   [L"ENG"] = L"Height Aft Calibrate Tool",},

    [L"圆弧半径公差"] = {
                   [L"CHN"] = L"圆弧半径公差",
                   [L"POL"] = L"Arc Radius Tolerance",
                   [L"ENG"] = L"Arc Radius Tolerance",},

    [L"转角光顺处理方式"] = {
                   [L"CHN"] = L"转角光顺处理方式",
                   [L"POL"] = L"Corner Trace Pretreatment Options",
                   [L"ENG"] = L"Corner Trace Pretreatment Options",},

    [L"圆弧加工最小速度"] = {
                   [L"CHN"] = L"圆弧加工最小速度",
                   [L"POL"] = L"Min. predkosc obrobki okregow",
                   [L"ENG"] = L"Circular processing Min. speed",},

    [L"参考圆速度"] = {
                   [L"CHN"] = L"参考圆速度",
                   [L"POL"] = L"Predkosc okregu wzorcowego",
                   [L"ENG"] = L"Reference circle speed",},

    [L"加工结束是否停止主轴"] = {
                   [L"CHN"] = L"加工结束是否停止主轴",
                   [L"POL"] = L"Czy zatrzymac wrzeciono po zakonczeniu programu",
                   [L"ENG"] = L"Whether to stop spindle at end",},

    [L"参考圆半径"] = {
                   [L"CHN"] = L"参考圆半径",
                   [L"POL"] = L"Promien okregu wzorcowego",
                   [L"ENG"] = L"Reference circle radius",},

    [L"定位过程中机床开始减速时离目标位置的距离"] = {
                   [L"CHN"] = L"定位过程中机床开始减速时离目标位置的距离",
                   [L"POL"] = L"Jest to odleglosc, z ktorej narzedzie zaczyna zwalniac podczas dojazdu do pozycji docelowej.",
                   [L"ENG"] = L"It is the distance from where the machine tool begins to decelerate to the target position during positioning.",},

    [L"粗定位阶段Z轴方向"] = {
                   [L"CHN"] = L"粗定位阶段Z轴方向",
                   [L"POL"] = L"Kierunek osi Z podczas zgrubnego pozycjonowania",
                   [L"ENG"] = L"Z direction in coarse positioning",},

    [L"旋转轴最大速度"] = {
                   [L"CHN"] = L"旋转轴最大速度",
                   [L"POL"] = L"Max. predkosc osi obrotowej",
                   [L"ENG"] = L"Max. speed of revolving axis",},

    [L"单位是: 转/分钟"] = {
                   [L"CHN"] = L"单位是: 转/分钟",
                   [L"POL"] = L"Jednostka jest obrot/min",
                   [L"ENG"] = L"The unit is revolution/min",},

    [L"循环加工ENG文件的次数"] = {
                   [L"CHN"] = L"循环加工ENG文件的次数",
                   [L"POL"] = L"Liczba cykli obrobki ENG",
                   [L"ENG"] = L"Cycle times of ENG processing",},

    [L"旋转加工速度"] = {
                   [L"CHN"] = L"旋转加工速度",
                   [L"POL"] = L"Predkosc obrobki osi obrotowej",
                   [L"ENG"] = L"Machining speed of revolving",},

    [L"旋转轴加速度"] = {
                   [L"CHN"] = L"旋转轴加速度",
                   [L"POL"] = L"Przyspieszenie osi obrotowej",
                   [L"ENG"] = L"Acceleration speed of revolving axis",},

    [L"否"] = {
                   [L"CHN"] = L"否",
                   [L"POL"] = L"Nie",
                   [L"ENG"] = L"NO",},

    [L"旋转轴起跳速度"] = {
                   [L"CHN"] = L"旋转轴起跳速度",
                   [L"POL"] = L"Predkosc poczatkowa osi obrotowej",
                   [L"ENG"] = L"Startup speed of revolving axis",},

    [L"旋转工件半径"] = {
                   [L"CHN"] = L"旋转工件半径",
                   [L"POL"] = L"Promien obrotu przedmiotu obrabianego",
                   [L"ENG"] = L"Revolving workpiece radius",},

    [L"进入刀库前减速位置Z轴机械坐标"] = {
                   [L"CHN"] = L"进入刀库前减速位置Z轴机械坐标",
                   [L"POL"] = L"Wspolrzedna osi Z zwalniania przed wejsciem do magazynka narzedzi",
                   [L"ENG"] = L"Z coordinate of deceleration position before entering tool magazine",},

    [L"否：度；是：毫米"] = {
                   [L"CHN"] = L"否：度；是：毫米",
                   [L"POL"] = L"0: Stopien；1: mm",
                   [L"ENG"] = L"0: Degree；1: mm",},

    [L"是表示使用S形算法进行插补"] = {
                   [L"CHN"] = L"是表示使用S形算法进行插补",
                   [L"POL"] = L"“Uzycie algorytmu S dla interpolacji",
                   [L"ENG"] = L"“True” indicates using type S algorithm for interpolation",},

    [L"固定对刀块Y机械坐标"] = {
                   [L"CHN"] = L"固定对刀块Y机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe Y plytki kalibrujacej",
                   [L"ENG"] = L"Y mechanical Coor of fixed Cali block",},

    [L"轴输出方向"] = {
                   [L"CHN"] = L"轴输出方向",
                   [L"POL"] = L"Kierunek wyjscia osi",
                   [L"ENG"] = L"Axis output direction",},

    [L"退刀量"] = {
                   [L"CHN"] = L"退刀量",
                   [L"POL"] = L"Wielkosc odsuniecia",
                   [L"ENG"] = L"Retract amount",},

    [L"Y轴是否是数控转台"] = {
                   [L"CHN"] = L"Y轴是否是数控转台",
                   [L"POL"] = L"Czy Y jest osia obrotowa",
                   [L"ENG"] = L"Whether Y to be CNC turntable",},

    [L"Y轴为旋转轴"] = {
                   [L"CHN"] = L"Y轴为旋转轴",
                   [L"POL"] = L"Wlacz Y jako os obrotowa",
                   [L"ENG"] = L"Enable Y as revolving axis",},

    [L"[三维切割]每次到工件表面才进行阀门操作"] = {
                   [L"CHN"] = L"[三维切割]每次到工件表面才进行阀门操作",
                   [L"POL"] = L"[Frezowanie trzyosiowe] Wykonaj operacje tylko na powierzchni przedmiotu obrabianego",
                   [L"ENG"] = L"[Three dimensional cutting] Execute the valve operation only on the surface of workpiece",},

    [L"前瞻线段数"] = {
                   [L"CHN"] = L"前瞻线段数",
                   [L"POL"] = L"Numer linii",
                   [L"ENG"] = L"Predicted segment No.",},

    [L"换刀前置点X轴坐标"] = {
                   [L"CHN"] = L"换刀前置点X轴坐标",
                   [L"POL"] = L"Wspolrzedna X pozycji dla wymiany narzedzia",
                   [L"ENG"] = L"X coordinate of tool change ahead position",},

    [L"将Y设置为旋转轴时，Y轴的的脉冲当量"] = {
                   [L"CHN"] = L"将Y设置为旋转轴时，Y轴的的脉冲当量",
                   [L"POL"] = L"Jednostka impulsow osi Y ustawionej jako os obrotowa",
                   [L"ENG"] = L"Y Revolving Pulse Unit when Y is set to be revolving axis",},

    [L"立即有效"] = {
                   [L"CHN"] = L"立即有效",
                   [L"POL"] = L"Natychmiast",
                   [L"ENG"] = L"Instant",},

    [L"重启有效"] = {
                   [L"CHN"] = L"重启有效",
                   [L"POL"] = L"Restart",
                   [L"ENG"] = L"Restart",},

    [L"指定刀补的类型: 1、一般模式，2、求交模式，3、插入模式"] = {
                   [L"CHN"] = L"指定刀补的类型: 1、一般模式，2、求交模式，3、插入模式",
                   [L"POL"] = L"Okresl typ kompensacji narzedzia: 1 Normalny, 2 Przecinanie Type, 3 Wkladanie",
                   [L"ENG"] = L"Specify the Cutter Compensation Type : 1 Normal Type, 2 Intersect Type, 3 Insert Type",},

    [L"换刀提示有效则遇到换刀指令时暂停并提示换刀"] = {
                   [L"CHN"] = L"换刀提示有效则遇到换刀指令时暂停并提示换刀",
                   [L"POL"] = L"Jesli funkcja ta jest wlaczona, system uruchomi pauze i wyswietli komunikat operatorowi aby wymienil narzedzie w momencie wystapienia komendy wymiany w programie",
                   [L"ENG"] = L"If this function is valid, system will pause and prompt operator to change the tool when tool change command is encountered",},

    [L"在加工Eng文件时遇到换刀暂停并提示换刀"] = {
                   [L"CHN"] = L"在加工Eng文件时遇到换刀暂停并提示换刀",
                   [L"POL"] = L"Zostanie uruchomiona pauza i wyswietlony komunikat o wymianie narzedzi podczas obrobki pliku Eng",
                   [L"ENG"] = L"Machine will pause and prompt tool change when tool change command is encountered in machining Eng file",},

    [L"G01下刀时使用设置的下刀速度"] = {
                   [L"CHN"] = L"G01下刀时使用设置的下刀速度",
                   [L"POL"] = L"Uzyj okreslonej predkosci G01 znizania narzedzia",
                   [L"ENG"] = L"Use specified G01 tool down speed",},

    [L"X 轴公共偏置"] = {
                   [L"CHN"] = L"X 轴公共偏置",
                   [L"POL"] = L"Wspolne odsuniecie osi X",
                   [L"ENG"] = L"X-axis public offset",},

    [L"Z轴偏置"] = {
                   [L"CHN"] = L"Z轴偏置",
                   [L"POL"] = L"Odsuniecie osi Z",
                   [L"ENG"] = L"Z-axis offset",},

    [L"加工前是否回机械原点"] = {
                   [L"CHN"] = L"加工前是否回机械原点",
                   [L"POL"] = L"Czy wrocic do maszynowego punktu zerowego przed rozpoczeciem obrobki",
                   [L"ENG"] = L"Whether to back to mechanical origin before machining",},

    [L"Y 轴公共偏置"] = {
                   [L"CHN"] = L"Y 轴公共偏置",
                   [L"POL"] = L"Wspolne odsuniecie osi Y",
                   [L"ENG"] = L"Y-axis public offset",},

    [L"使用缺省主轴转速"] = {
                   [L"CHN"] = L"使用缺省主轴转速",
                   [L"POL"] = L"Uzyj domyslnej predkosci wrzeciona",
                   [L"ENG"] = L"Use default spindle speed",},

    [L"回机械原点X轴方向"] = {
                   [L"CHN"] = L"回机械原点X轴方向",
                   [L"POL"] = L"Kierunek osi X podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"X direction in backing to reference point",},

    [L"Z 轴公共偏置"] = {
                   [L"CHN"] = L"Z 轴公共偏置",
                   [L"POL"] = L"Wspolne odsuniecie osi Z",
                   [L"ENG"] = L"Z-axis public offset",},

    [L"Z轴行程上下限"] = {
                   [L"CHN"] = L"Z轴行程上下限",
                   [L"POL"] = L"Zakres limitu gornego i dolnego dla osi Z przestrzeni roboczej",
                   [L"ENG"] = L"Z-Axis workbench range upper and lower limit",},

    [L"Y轴行程上下限"] = {
                   [L"CHN"] = L"Y轴行程上下限",
                   [L"POL"] = L"Zakres limitow gornego i dolnego przestrzeni roboczej osi Y",
                   [L"ENG"] = L"Y-Axis workbench range upper and lower limit",},

    [L"X轴行程上下限"] = {
                   [L"CHN"] = L"X轴行程上下限",
                   [L"POL"] = L"Zakres limitu gornego i dolnego dla osi X przestrzeni roboczej",
                   [L"ENG"] = L"X-Axis workbench range upper and lower limit",},

    [L"加工前回机械原点"] = {
                   [L"CHN"] = L"加工前回机械原点",
                   [L"POL"] = L"Powrot do punktu zerowego przed obrobka",
                   [L"ENG"] = L"Back to reference point before machining",},

    [L"X轴机械坐标"] = {
                   [L"CHN"] = L"X轴机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe osi X",
                   [L"ENG"] = L"X-axis MachinCoor",},

    [L"当前使用的刀具号"] = {
                   [L"CHN"] = L"当前使用的刀具号",
                   [L"POL"] = L"Aktualnie uzywany numer narzedzia",
                   [L"ENG"] = L"Currently being used Tool No.",},

    [L"换刀上位Z轴机械坐标"] = {
                   [L"CHN"] = L"换刀上位Z轴机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe CT_up dla osi Z",
                   [L"ENG"] = L"Z mechanical coordinate of CT_up",},

    [L"退刀点"] = {
                   [L"CHN"] = L"退刀点",
                   [L"POL"] = L"Punkt powrotu",
                   [L"ENG"] = L"Retract Point",},

    [L"反向间隙"] = {
                   [L"CHN"] = L"反向间隙",
                   [L"POL"] = L"Luz",
                   [L"ENG"] = L"Backlash",},

    [L"刀具%dX轴机械坐标"] = {
                   [L"CHN"] = L"刀具%dX轴机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe X narzedzia %d",
                   [L"ENG"] = L"X-axis MachinCoor of tool %d",},

    [L"回机械原点Y轴速度"] = {
                   [L"CHN"] = L"回机械原点Y轴速度",
                   [L"POL"] = L"Predkosc Y podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"Y Speed in backing to reference point",},

    [L"机床在换刀过程中水平移动进出刀库所用的速度"] = {
                   [L"CHN"] = L"机床在换刀过程中水平移动进出刀库所用的速度",
                   [L"POL"] = L"Predkosc uzywana podczas wymiany narzedzia w magazynku.",
                   [L"ENG"] = L"In machine tool change, the speed is used for traversing in /out tool magazine.",},

    [L"主轴转速"] = {
                   [L"CHN"] = L"主轴转速",
                   [L"POL"] = L"Predkosc wrzeciona",
                   [L"ENG"] = L"Spindle Speed",},

    [L"水平移动进出刀库速度"] = {
                   [L"CHN"] = L"水平移动进出刀库速度",
                   [L"POL"] = L"Predkosc wjazdu/wyjazdu wymiany narzedzi",
                   [L"ENG"] = L"Traversing speed in/ out tool magazine",},

    [L"进入刀库前减速位置Y轴机械坐标"] = {
                   [L"CHN"] = L"进入刀库前减速位置Y轴机械坐标",
                   [L"POL"] = L"Wspolrzedne Y pozycji zwalniania przed wejsciem do magazynka narzedzi",
                   [L"ENG"] = L"Y coordinate of deceleration position before entering tool magazine",},

    [L"Z轴上位下位速度"] = {
                   [L"CHN"] = L"Z轴上位下位速度",
                   [L"POL"] = L"Predkosc CTup i CTdown dla osi Z",
                   [L"ENG"] = L"Z-axis CTup and CTdown speed",},

    [L"换刀下位"] = {
                   [L"CHN"] = L"换刀下位",
                   [L"POL"] = L"Dolna pozycja wymiany narzędzi",
                   [L"ENG"] = L"Tool change lower position",},

    [L"换刀时主轴移动速度"] = {
                   [L"CHN"] = L"换刀时主轴移动速度",
                   [L"POL"] = L"Predkosc obr. wrzeciona w wymianie narzedzi",
                   [L"ENG"] = L"Spindle speed in tool change",},

    [L"换刀移动速度"] = {
                   [L"CHN"] = L"换刀移动速度",
                   [L"POL"] = L"Predkosc wymiany narzedzi",
                   [L"ENG"] = L"Tool change speed",},

    [L"使用缺省速度"] = {
                   [L"CHN"] = L"使用缺省速度",
                   [L"POL"] = L"Uzyj Domyslnej Predkosci",
                   [L"ENG"] = L"UseDefaultSpeed",},

    [L"换刀前置点Z轴坐标"] = {
                   [L"CHN"] = L"换刀前置点Z轴坐标",
                   [L"POL"] = L"Wspolrzedna Z pozycji narzedzia podcza wymiany",
                   [L"ENG"] = L"Z coordinate of tool change ahead position",},

    [L"Z进刀选择"] = {
                   [L"CHN"] = L"Z进刀选择",
                   [L"POL"] = L"Z down option",
                   [L"ENG"] = L"Z down option",},

    [L"机床在换刀过程中Z轴上刀位下刀位所用的速度"] = {
                   [L"CHN"] = L"机床在换刀过程中Z轴上刀位下刀位所用的速度",
                   [L"POL"] = L"Parametry CTup i CTdown predkosci osi Z podczas wymiany narzedzia",
                   [L"ENG"] = L"Z-axis CTup and CTdown speed in tool change",},

    [L"换刀前置点Y轴坐标"] = {
                   [L"CHN"] = L"换刀前置点Y轴坐标",
                   [L"POL"] = L"Wspolrzedna Y pozycji wymiany narzedzia",
                   [L"ENG"] = L"Y coordinate of tool change ahead position",},

    [L"等待主轴达到最大转速的延时"] = {
                   [L"CHN"] = L"等待主轴达到最大转速的延时",
                   [L"POL"] = L"Opoznienie podczas osiagania maksymalnej predkosci wrzeciona",
                   [L"ENG"] = L"Time Delay in reaching max. spindle speed",},

    [L"主轴启动停止时间"] = {
                   [L"CHN"] = L"主轴启动停止时间",
                   [L"POL"] = L"Czas uruchomienia/wylaczenia wrzeciona",
                   [L"ENG"] = L"Spindle start/stop time",},

    [L"进入刀库前减速位置X轴机械坐标"] = {
                   [L"CHN"] = L"进入刀库前减速位置X轴机械坐标",
                   [L"POL"] = L"Wspolrzedna X zwalniania przed dojazdem do magazynka narzedzi",
                   [L"ENG"] = L"X coordinate of deceleration position before entering tool magazine",},

    [L"dxf文件为公制尺寸"] = {
                   [L"CHN"] = L"dxf文件为公制尺寸",
                   [L"POL"] = L"uzyj wartosci metrycznych dla pliku dxf",
                   [L"ENG"] = L"use dxf file as metric size",},

    [L"刀具直径磨损量"] = {
                   [L"CHN"] = L"刀具直径磨损量",
                   [L"POL"] = L"Srednica zuzycia",
                   [L"ENG"] = L"Wear In Diameter",},

    [L"刀具%dY轴机械坐标"] = {
                   [L"CHN"] = L"刀具%dY轴机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe osi Y dla narzedzia %d",
                   [L"ENG"] = L"Y-axis MachinCoor of tool %d",},

    [L"当前刀具号"] = {
                   [L"CHN"] = L"当前刀具号",
                   [L"POL"] = L"Aktualny numer narzedzia",
                   [L"ENG"] = L"Current     tool number",},

    [L"Y轴反向间隙"] = {
                   [L"CHN"] = L"Y轴反向间隙",
                   [L"POL"] = L"Luz osi Y",
                   [L"ENG"] = L"Backlash of Y-axis",},

    [L"Z轴脉冲当量"] = {
                   [L"CHN"] = L"Z轴脉冲当量",
                   [L"POL"] = L"Impulsy osi Z",
                   [L"ENG"] = L"Z-Axis Pulse Equivalent",},

    [L"Y轴脉冲当量"] = {
                   [L"CHN"] = L"Y轴脉冲当量",
                   [L"POL"] = L"Impulsy osi Y",
                   [L"ENG"] = L"Y-Axis Pulse Equivalent",},

    [L"加工结束后的主轴动作"] = {
                   [L"CHN"] = L"加工结束后的主轴动作",
                   [L"POL"] = L"Dzialanie wrzeciona po zakonczeniu obrobki",
                   [L"ENG"] = L"The Action of Spindle After Process",},

    [L"回机械原点Z轴方向"] = {
                   [L"CHN"] = L"回机械原点Z轴方向",
                   [L"POL"] = L"Kierunek osi Z podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"Z direction in backing to reference point",},

    [L"换刀下位Z轴机械坐标"] = {
                   [L"CHN"] = L"换刀下位Z轴机械坐标",
                   [L"POL"] = L"Wspolrzedme maszynowe os Z dla CT_down",
                   [L"ENG"] = L"Z mechanical coordinate of CT_down",},

    [L"暂停时停止主轴"] = {
                   [L"CHN"] = L"暂停时停止主轴",
                   [L"POL"] = L"Wylacz wrzeciona podczas pauzy",
                   [L"ENG"] = L"Stop Spindle While Pausing",},

    [L"X轴脉冲当量"] = {
                   [L"CHN"] = L"X轴脉冲当量",
                   [L"POL"] = L"Impulsy osi X",
                   [L"ENG"] = L"X-Axis Pulse Equivalent",},

    [L"深孔加工方式"] = {
                   [L"CHN"] = L"深孔加工方式",
                   [L"POL"] = L"Rodzaj wiercenia glebokich otworow",
                   [L"ENG"] = L"Deep hole machining manner",},

    [L"使用Eng选刀加工"] = {
                   [L"CHN"] = L"使用Eng选刀加工",
                   [L"POL"] = L"Wybor narzedzia dla obrobki pliku ENG",
                   [L"ENG"] = L"Select tool for ENG file to be machined",},

    [L"加工深孔的方式：0、往复排屑；1、高速往复排屑"] = {
                   [L"CHN"] = L"加工深孔的方式：0、往复排屑；1、高速往复排屑",
                   [L"POL"] = L"Deep hole machining manner:0: Reciprocating chip removal;1:highspeed reciprocating chip removal",
                   [L"ENG"] = L"Deep hole machining manner:0: Reciprocating chip removal;1:highspeed reciprocating chip removal",},

    [L"最大转弯加速度(mm/s^2)"] = {
                   [L"CHN"] = L"最大转弯加速度(mm/s^2)",
                   [L"POL"] = L"Maksymalne przyspieszenie zmiany kierunku (mm/s^2)",
                   [L"ENG"] = L"Max Turning acceleration(mm/s^2)",},

    [L"定位过程中刀具接近工件时的进给速度"] = {
                   [L"CHN"] = L"定位过程中刀具接近工件时的进给速度",
                   [L"POL"] = L"Posuw narzedzia podczas dojazdu do przedmiotu obrabianego",
                   [L"ENG"] = L"Feed speed of cutter when approaching the workpiece during positioning",},

    [L"换刀提示"] = {
                   [L"CHN"] = L"换刀提示",
                   [L"POL"] = L"Komunikat wymiany narzedzia",
                   [L"ENG"] = L"Tool change prompt",},

    [L"系统检测到某些参数配置不正确，需要重新配置参数。请立即到'系统参数'窗口检查和重新设置参数！\n\
	\n\
	错误：　　　参数值超出允许范围。\n\
	参数名称：　%s\n"] = {
                   [L"CHN"] = L"系统检测到某些参数配置不正确，需要重新配置参数。请立即到'系统参数'窗口检查和重新设置参数！\n\
	\n\
	错误：　　　参数值超出允许范围。\n\
	参数名称：　%s\n",
                   [L"POL"] = L"System wykryl niewlasciwa konfiguracje parametrow, ktore wymagaja ponownego ustawienia.\
	prosze przejsc do “parametrow systemowych” aby sprawdzic i zresetowac parametry.\n\
	\n\
	Blad: wartosc jest poza zakresem.\n\
	Nazwa Parametru: %s.\n",
                   [L"ENG"] = L"System detects some inaccurate parameter configurations which need to reconfigure.\
	Please turn to “system parameters” window to check and reset parameters.\n\
	\n\
	Error: the value is out of the range.\n\
	Parameter Name: %s.\n",},
	
    [L"旋转轴脉冲当量"] = {
                   [L"CHN"] = L"旋转轴脉冲当量",
                   [L"POL"] = L"Impulsy osi obrotowej",
                   [L"ENG"] = L"Per pulse rev axis",},

    [L"定期自动启动润滑油泵"] = {
                   [L"CHN"] = L"定期自动启动润滑油泵",
                   [L"POL"] = L"Otwieraj okresowo pompe smarowania",
                   [L"ENG"] = L"Open lubrication pump periodically",},

    [L"是否用缺省主轴转速屏蔽文件中S指令"] = {
                   [L"CHN"] = L"是否用缺省主轴转速屏蔽文件中S指令",
                   [L"POL"] = L"Czy uzywac domyslnej predkosci wrzeciona zamiast podanej w programie komenda S",
                   [L"ENG"] = L"Whether to use default spindle speed instead of S command in file",},

    [L"强制认定dxf文件为公制尺寸"] = {
                   [L"CHN"] = L"强制认定dxf文件为公制尺寸",
                   [L"POL"] = L"Zmus do traktowania wymiarow pliku dxf jak file as metric size",
                   [L"ENG"] = L"force to regard dxf file as metric size",},

    [L"使用高速往复排屑方式钻深孔时每次进给后的回退量"] = {
                   [L"CHN"] = L"使用高速往复排屑方式钻深孔时每次进给后的回退量",
                   [L"POL"] = L"Odleglosc powrotu po posuwie podczas wiercenia glebokich otworow",
                   [L"ENG"] = L"The retract amount after feeding when drilling deep hole in high speed reciprocating chip removal manner",},

    [L"旋转轴配置"] = {
                   [L"CHN"] = L"旋转轴配置",
                   [L"POL"] = L"Konfiguracja osi obrotowej",
                   [L"ENG"] = L"Revolving axis configuration",},

    [L"底部加工有效"] = {
                   [L"CHN"] = L"底部加工有效",
                   [L"POL"] = L"Obrobka dna",
                   [L"ENG"] = L"Bottom machining valid",},

    [L"每次加工一个形状，直到该形状加工完成后再加工下一个"] = {
                   [L"CHN"] = L"每次加工一个形状，直到该形状加工完成后再加工下一个",
                   [L"POL"] = L"Podczas obrobki jednego ksztaltu maszyna nie przesunie sie do obrbki kolejnego dopoki nie skonczy aktualnego.",
                   [L"ENG"] = L"In machining one shape,the machine will not move to process the next one until this one is finished.",},

    [L"形状独立加工有效"] = {
                   [L"CHN"] = L"形状独立加工有效",
                   [L"POL"] = L"Obrobka pojedynczych ksztaltow",
                   [L"ENG"] = L"Shape separate processing_ valid",},

    [L"固定对刀块Z机械坐标"] = {
                   [L"CHN"] = L"固定对刀块Z机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe osi Z dla stalego czujnika dlugosci narzedzia",
                   [L"ENG"] = L"Z mechanical Coor of fixed Cali block",},

    [L"用DXF中的首点作为零点"] = {
                   [L"CHN"] = L"用DXF中的首点作为零点",
                   [L"POL"] = L"Uzyj pierwszego punktu DXF jako punktu zerowego",
                   [L"ENG"] = L"Use first point in DXF as zero point",},

    [L"补偿参数"] = {
                   [L"CHN"] = L"补偿参数",
                   [L"POL"] = L"Parametry kompensacji",
                   [L"ENG"] = L"Compensation parameters",},

    [L"Z轴能达到的最大速度"] = {
                   [L"CHN"] = L"Z轴能达到的最大速度",
                   [L"POL"] = L"Maksymalna predkosc osi Z.",
                   [L"ENG"] = L"It is the maximum speed Z-axis can achieve.",},

    [L"G00速度"] = {
                   [L"CHN"] = L"G00速度",
                   [L"POL"] = L"Predkosc G00",
                   [L"ENG"] = L"G00 Speed",},

    [L"最大加速度(mm/s^2)"] = {
                   [L"CHN"] = L"最大加速度(mm/s^2)",
                   [L"POL"] = L"Max Przyspieszenie Osiowe (mm/s^2)",
                   [L"ENG"] = L"Max Axis acceleration(mm/s^2)",},

    [L"使用首点作为零点"] = {
                   [L"CHN"] = L"使用首点作为零点",
                   [L"POL"] = L"Uzyj pierwszego punktu jako punktu zerowego",
                   [L"ENG"] = L"Use first point as zero point",},

    [L"刀具长度磨损量"] = {
                   [L"CHN"] = L"刀具长度磨损量",
                   [L"POL"] = L"Zuzycie dlugosci narzedzia",
                   [L"ENG"] = L"Wear In Tool Length",},

    [L"转角容差"] = {
                   [L"CHN"] = L"转角容差",
                   [L"POL"] = L"Corner Tolerance",                
                   [L"ENG"] = L"Corner Tolerance",},

    [L"Z步长"] = {
                   [L"CHN"] = L"Z步长",
                   [L"POL"] = L"Dlugosc kroku Z",
                   [L"ENG"] = L"ZStepLength",},

    [L"XY步长"] = {
                   [L"CHN"] = L"XY步长",
                   [L"POL"] = L"Dlugosc Kroku XY",
                   [L"ENG"] = L"XYStepLength",},

    [L"加工深度"] = {
                   [L"CHN"] = L"加工深度",
                   [L"POL"] = L"Glebokosc obrobki",
                   [L"ENG"] = L"processing depth",},

    [L"是"] = {
                   [L"CHN"] = L"是",
                   [L"POL"] = L"TAK",
                   [L"ENG"] = L"YES",},

    [L"暂停时抬刀量"] = {
                   [L"CHN"] = L"暂停时抬刀量",
                   [L"POL"] = L"Odsuniecie osi Z przy Pauzie",
                   [L"ENG"] = L"Pause Z offset",},

    [L"配置G01下刀时的下刀速度"] = {
                   [L"CHN"] = L"配置G01下刀时的下刀速度",
                   [L"POL"] = L"Konfiguruj Predkosc Opuszczania Narzedzia G01",
                   [L"ENG"] = L"Configure G01 Tool Down Speed",},

    [L"主轴状态数"] = {
                   [L"CHN"] = L"主轴状态数",
                   [L"POL"] = L"Bieg wrzeciona nr.",
                   [L"ENG"] = L"Spindle states no.",},

    [L"循环加工次数"] = {
                   [L"CHN"] = L"循环加工次数",
                   [L"POL"] = L"Liczba cykli",
                   [L"ENG"] = L"Recycle Times",},

    [L"Dxf文件翻译参数"] = {
                   [L"CHN"] = L"Dxf文件翻译参数",
                   [L"POL"] = L"Parametry translacji pliku Dxf",
                   [L"ENG"] = L"Dxf file translation parameters",},

    [L"Y轴回退距离"] = {
                   [L"CHN"] = L"Y轴回退距离",
                   [L"POL"] = L"Odleglosc odsunieciaosi Y",
                   [L"ENG"] = L"Retract distance of Y-axis",},

    [L"0:不动; 1:回固定点; 2:回工件原点"] = {
                   [L"CHN"] = L"0:不动; 1:回固定点; 2:回工件原点",
                   [L"POL"] = L"0:Stop; 1:Powrot do ust. punktu; 2:Powrot do punktu zerowego przedmiotu obrabianego",
                   [L"ENG"] = L"0:Stop; 1:Back to Fixed Point; 2:Back to Workpiece Origin",},

    [L"Y轴工作范围下限"] = {
                   [L"CHN"] = L"Y轴工作范围下限",
                   [L"POL"] = L"Dolny limit zakresu przestrzeni roboczej dla osi Y",
                   [L"ENG"] = L"Y-Axis workbench range lower limit",},

    [L"Z轴工作范围下限"] = {
                   [L"CHN"] = L"Z轴工作范围下限",
                   [L"POL"] = L"Dolny limit zakresu przestrzeni roboczej dla osi Z",
                   [L"ENG"] = L"Z-Axis workbench range lower limit",},

    [L"机床最大速度"] = {
                   [L"CHN"] = L"机床最大速度",
                   [L"POL"] = L"Maksymalna Predkosc",
                   [L"ENG"] = L"Max Speed",},

    [L"加工结束后亮红灯进行提示"] = {
                   [L"CHN"] = L"加工结束后亮红灯进行提示",
                   [L"POL"] = L"Czerwona lampa po zakonczeniu obrobki",
                   [L"ENG"] = L"Red lamp on after machining ends",},

    [L"圆弧增量模式有效"] = {
                   [L"CHN"] = L"圆弧增量模式有效",
                   [L"POL"] = L"Wlacz tryb przyrostowy IJK",
                   [L"ENG"] = L"Enable IJK increment mode",},

    [L"机床启动后开启润滑油泵的时间间隔"] = {
                   [L"CHN"] = L"机床启动后开启润滑油泵的时间间隔",
                   [L"POL"] = L"Interwal uruchamiania opmpy smarowania po uruchominiu maszyny",
                   [L"ENG"] = L"The interval of starting lubrication pump after machine startup",},

    [L"Z轴螺距"] = {
                   [L"CHN"] = L"Z轴螺距",
                   [L"POL"] = L"Skok sruby osi Z",
                   [L"ENG"] = L"Z-axis screw pitch",},

    [L"二维文件加工深度"] = {
                   [L"CHN"] = L"二维文件加工深度",
                   [L"POL"] = L"Glebokosc obrobki pliku 2D",
                   [L"ENG"] = L"2D file machining depth",},

    [L"粗定位阶段X轴方向"] = {
                   [L"CHN"] = L"粗定位阶段X轴方向",
                   [L"POL"] = L"Kierunek osi X podczas zgrubnego pozycjonowania",
                   [L"ENG"] = L"X direction in coarse positioning",},

    [L"Y轴螺距"] = {
                   [L"CHN"] = L"Y轴螺距",
                   [L"POL"] = L"Skok sruby osi Y",
                   [L"ENG"] = L"Y-axis screw pitch",},

    [L"刀具直径"] = {
                   [L"CHN"] = L"刀具直径",
                   [L"POL"] = L"Srednica narzedzia",
                   [L"ENG"] = L"Diameter Of Tool",},

    [L"回机械原点Y轴方向"] = {
                   [L"CHN"] = L"回机械原点Y轴方向",
                   [L"POL"] = L"Kierunek Y podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"Y direction in backing to reference point",},

    [L"刀具补偿类型"] = {
                   [L"CHN"] = L"刀具补偿类型",
                   [L"POL"] = L"Okresl typ kompensacji narzedzia",
                   [L"ENG"] = L"Specify The Type of Tool Compensation",},

    [L"刀具补偿有效"] = {
                   [L"CHN"] = L"刀具补偿有效",
                   [L"POL"] = L"Kompensacja promienia",
                   [L"ENG"] = L"Turn On Radius Compensation",},

    [L"主轴最大转速"] = {
                   [L"CHN"] = L"主轴最大转速",
                   [L"POL"] = L"Maks. predkosc wrzeciona",
                   [L"ENG"] = L"Max. spindle Speed",},

    [L"X轴"] = {
                   [L"CHN"] = L"X轴",
                   [L"POL"] = L"Os X",
                   [L"ENG"] = L"X-Axis",},

    [L"Y轴"] = {
                   [L"CHN"] = L"Y轴",
                   [L"POL"] = L"Os Y",
                   [L"ENG"] = L"Y-Axis",},

    [L"Z轴"] = {
                   [L"CHN"] = L"Z轴",
                   [L"POL"] = L"Os Z",
                   [L"ENG"] = L"Z-Axis",},

    [L"工作范围下限"] = {
                   [L"CHN"] = L"工作范围下限",
                   [L"POL"] = L"Dolny limit powierzchni roboczej",
                   [L"ENG"] = L"Workbench range lower limit",},

    [L"刀具补偿"] = {
                   [L"CHN"] = L"刀具补偿",
                   [L"POL"] = L"Kompensacja narzedzia",
                   [L"ENG"] = L"Tool Compensation",},

    [L"刀库容量"] = {
                   [L"CHN"] = L"刀库容量",
                   [L"POL"] = L"Pojemnosc magazynka narzedzi",
                   [L"ENG"] = L"Tool magazi-ne capacity",},

    [L"停止时停止主轴"] = {
                   [L"CHN"] = L"停止时停止主轴",
                   [L"POL"] = L"Zatrzymaj Wrzeciono przy zatrzymaniu programu",
                   [L"ENG"] = L"Stop Spindle While Stopping",},

    [L"X轴工作范围上限"] = {
                   [L"CHN"] = L"X轴工作范围上限",
                   [L"POL"] = L"Gorny limit przestrzeni roboczej osi X",
                   [L"ENG"] = L"X-Axis workbench range upper limit",},

    [L"X轴反向间隙"] = {
                   [L"CHN"] = L"X轴反向间隙",
                   [L"POL"] = L"Luz osi X",
                   [L"ENG"] = L"Backlash of X-axis",},

    [L"Z轴工作范围上限"] = {
                   [L"CHN"] = L"Z轴工作范围上限",
                   [L"POL"] = L"Gorny limit przestrzeni roboczej osi Z",
                   [L"ENG"] = L"Z-Axis workbench range upper limit",},

    [L"Y轴工作范围上限"] = {
                   [L"CHN"] = L"Y轴工作范围上限",
                   [L"POL"] = L"Gorny limit przestrzeni roboczej osi Y",
                   [L"ENG"] = L"Y-Axis workbench range upper limit",},

    [L"紧停后是否取消回机械原点标志"] = {
                   [L"CHN"] = L"紧停后是否取消回机械原点标志",
                   [L"POL"] = L"Czy anulowac powrot do punktu zerowego po stopie awaryjnym",
                   [L"ENG"] = L"Whether to cancel the mark of backing to the reference point after E-stop",},

    [L"丝杠误差补偿有效"] = {
                   [L"CHN"] = L"丝杠误差补偿有效",
                   [L"POL"] = L"Blad kompensacji sruby",
                   [L"ENG"] = L"Lead screw error compensation valid",},

    [L"加加速度"] = {
                   [L"CHN"] = L"加加速度",
                   [L"POL"] = L"Ped",
                   [L"ENG"] = L"Jerk",},

    [L"进给倍率对手动有效"] = {
                   [L"CHN"] = L"进给倍率对手动有效",
                   [L"POL"] = L"Wartosc posuwu wlasciwa dla trybu recznego",
                   [L"ENG"] = L"Feedrate is valid for manual mode",},

    [L"回机械原点参数"] = {
                   [L"CHN"] = L"回机械原点参数",
                   [L"POL"] = L"Parametr powrotu do maszynowego punktu zerowego",
                   [L"ENG"] = L"Back to mechanical origin parameter",},

    [L"刀具%d补偿参数"] = {
                   [L"CHN"] = L"刀具%d补偿参数",
                   [L"POL"] = L"Narzedzia %d Parametr Kompensacji",
                   [L"ENG"] = L"Cutter %d Compensation Parameter",},

    [L"Z轴回退距离"] = {
                   [L"CHN"] = L"Z轴回退距离",
                   [L"POL"] = L"Odleglosc odsuniecia osi Z",
                   [L"ENG"] = L"Retract distance of Z-axis",},

    [L"衔接速度前瞻距离"] = {
                   [L"CHN"] = L"衔接速度前瞻距离",
									 [L"POL"] = L"Connect Speed Look Ahead Distance.",
                   [L"ENG"] = L"Connect Speed Look Ahead Distance.",},

    [L"计算连接速度时的最大前瞻线段数"] = {
                   [L"CHN"] = L"计算连接速度时的最大前瞻线段数",
                   [L"POL"] = L"Max. Predicted segment No.in calculating connection speed ",
                   [L"ENG"] = L"Max. Predicted segment No.in calculating connection speed ",},

    [L"Z轴下刀速度"] = {
                   [L"CHN"] = L"Z轴下刀速度",
                   [L"POL"] = L"Predkosc opuszczania osi Z",
                   [L"ENG"] = L"Z down speed",},

    [L"配置文件不存在，或者版本不兼容！请删除配置文件并重新配置参数。"] = {
                   [L"CHN"] = L"配置文件不存在，或者版本不兼容！请删除配置文件并重新配置参数。",
                   [L"POL"] = L"Plik konfiguracyjny nie istnieje lub nie jest kompatybilny. Prosze usun plik i skonfiguruj parametry ponownie.",
                   [L"ENG"] = L"The configuration file does not exist or is not compatible. Please delete the file and configure the parameters again.",},

    [L"手动低速"] = {
                   [L"CHN"] = L"手动低速",
                   [L"POL"] = L"Niska predkosc trybu recznego",
                   [L"ENG"] = L"Manual Low Speed",},

    [L"润滑油泵的开启时间"] = {
                   [L"CHN"] = L"润滑油泵的开启时间",
                   [L"POL"] = L"Czas otwarcia pompy smarowania",
                   [L"ENG"] = L"Opening time of lubrication pump",},

    [L"最大转弯加速度"] = {
                   [L"CHN"] = L"最大转弯加速度",
                   [L"POL"] = L"Maks. Przyspieszenie przy zmianie kierunku",
                   [L"ENG"] = L"Max Turning Acceleration",},

    [L"减速距离"] = {
                   [L"CHN"] = L"减速距离",
                   [L"POL"] = L"Odleglosc zwalniania osi Z",
                   [L"ENG"] = L"Z Deceleration Distance",},

    [L"回机械原点Z轴速度"] = {
                   [L"CHN"] = L"回机械原点Z轴速度",
                   [L"POL"] = L"Predkosc Z podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"Z Speed in backing to reference point",},

    [L"单轴加速度"] = {
                   [L"CHN"] = L"单轴加速度",
                   [L"POL"] = L"Przyspieszenie poj. osi",
                   [L"ENG"] = L"Signle Axis Acc",},

    [L"粗定位阶段Y轴方向"] = {
                   [L"CHN"] = L"粗定位阶段Y轴方向",
                   [L"POL"] = L"Kierunek osi Y podczas zgrubnego pozycjonowania",
                   [L"ENG"] = L"Y direction in coarse positioning",},

    [L"粗定位阶段X轴速度"] = {
                   [L"CHN"] = L"粗定位阶段X轴速度",
                   [L"POL"] = L"Predkosc osi X podczas zgrubnego pozycjonowania",
                   [L"ENG"] = L"X Speed in coarse positioning",},

    [L"Z轴反向间隙"] = {
                   [L"CHN"] = L"Z轴反向间隙",
                   [L"POL"] = L"Luz osi Z",
                   [L"ENG"] = L"Backlash of Z-axis",},

    [L"退刀点高度"] = {
                   [L"CHN"] = L"退刀点高度",
                   [L"POL"] = L"Wysokosc punktu odsuniecia",
                   [L"ENG"] = L"Retract Point Height",},

    [L"定时释放润滑油的时间"] = {
                   [L"CHN"] = L"定时释放润滑油的时间",
                   [L"POL"] = L"Czas dla okresowego smarowania",
                   [L"ENG"] = L"Time for periodical lubrication release",},

    [L"Z的接近速度"] = {
                   [L"CHN"] = L"Z的接近速度",
                   [L"POL"] = L"Predkosc dojazdu osi Z",
                   [L"ENG"] = L"Z Approach Speed",},

    [L"Eng文件翻译参数"] = {
                   [L"CHN"] = L"Eng文件翻译参数",
                   [L"POL"] = L"Parametry translacji pliku Eng",
                   [L"ENG"] = L"Eng file translation parameters",},

    [L"各轴脉冲当量"] = {
                   [L"CHN"] = L"各轴脉冲当量",
                   [L"POL"] = L"Impulsy dla poszczegolnych osi",
                   [L"ENG"] = L"Pulse Equivalent of Each Axis",},

    [L"轨迹平滑时间"] = {
                   [L"CHN"] = L"轨迹平滑时间",
                   [L"POL"] = L"Czas wygladzania sciezki",
                   [L"ENG"] = L"Path Smoothing Time",},

    [L"X轴螺距"] = {
                   [L"CHN"] = L"X轴螺距",
                   [L"POL"] = L"Skok sruby osi X",
                   [L"ENG"] = L"X-axis screw pitch",},

    [L"固定点的Y轴坐标"] = {
                   [L"CHN"] = L"固定点的Y轴坐标",
                   [L"POL"] = L"Wspolrzedne osi Y ustalonego punktu",
                   [L"ENG"] = L"The Y axis coordinate of The Fixed Point",},

    [L"X轴输出方向"] = {
                   [L"CHN"] = L"X轴输出方向",
                   [L"POL"] = L"Kierunek wyjscia osi X",
                   [L"ENG"] = L"X-Axis output direction",},

    [L"Y轴输出方向"] = {
                   [L"CHN"] = L"Y轴输出方向",
                   [L"POL"] = L"Kierunek wyjscia osi Y",
                   [L"ENG"] = L"Y-Axis output direction",},

    [L"Z轴输出方向"] = {
                   [L"CHN"] = L"Z轴输出方向",
                   [L"POL"] = L"Kierunek wyjscia osi Z",
                   [L"ENG"] = L"Z-Axis output direction",},

    [L"主轴能达到的最大转速"] = {
                   [L"CHN"] = L"主轴能达到的最大转速",
                   [L"POL"] = L"AKtual. Max. predkosc wrzeciona",
                   [L"ENG"] = L"Actual Max. spindle Speed",},

    [L"开启自动润滑油功能"] = {
                   [L"CHN"] = L"开启自动润滑油功能",
                   [L"POL"] = L"Otworz automatyczne smarowanie",
                   [L"ENG"] = L"Open auto lubrication",},

    [L"粗定位阶段Y轴速度"] = {
                   [L"CHN"] = L"粗定位阶段Y轴速度",
                   [L"POL"] = L"Predkosc Y podczas pozycjonowania zgrubnego",
                   [L"ENG"] = L"Y Speed in coarse positioning",},

    [L"工作台范围"] = {
                   [L"CHN"] = L"工作台范围",
                   [L"POL"] = L"Przestrzen robocza",
                   [L"ENG"] = L"Work Area",},

    [L"X轴工作范围下限"] = {
                   [L"CHN"] = L"X轴工作范围下限",
                   [L"POL"] = L"Dolny limit zakresu przestrzeni roboczej dla osi X",
                   [L"ENG"] = L"X-Axis workbench range lower limit",},

    [L"X轴回退距离"] = {
                   [L"CHN"] = L"X轴回退距离",
                   [L"POL"] = L"Odleglosc odsuniecia osi X",
                   [L"ENG"] = L"Retract distance of X-axis",},

    [L"固定点的X轴坐标"] = {
                   [L"CHN"] = L"固定点的X轴坐标",
                   [L"POL"] = L"Wspolrzedna X ustalonego punktu",
                   [L"ENG"] = L"The X axis coordinate of The Fixed Point",},

    [L"Y轴回机械原点后的回退距离"] = {
                   [L"CHN"] = L"Y轴回机械原点后的回退距离",
                   [L"POL"] = L"Odleglosc odsuniecia osi Y podczas powrotu do punktu zerowego",
                   [L"ENG"] = L"Retract distance of Y-axis after backing to mechanical origin",},

    [L"X轴回机械原点后的回退距离"] = {
                   [L"CHN"] = L"X轴回机械原点后的回退距离",
                   [L"POL"] = L"Wielkosc odsuniecia osi X po powrocie do punktu zerowego",
                   [L"ENG"] = L"Retract distance of X-axis after backing to mechanical origin",},

    [L"Z轴回机械原点后的回退距离"] = {
                   [L"CHN"] = L"Z轴回机械原点后的回退距离",
                   [L"POL"] = L"Odleglosc odsuniecia osi Z po powrocie do punktu zerowego",
                   [L"ENG"] = L"Retract distance of Z-axis after backing to mechanical origin",},

    [L"手动高速"] = {
                   [L"CHN"] = L"手动高速",
                   [L"POL"] = L"Wysoka Predkosc Trybu Recznego",
                   [L"ENG"] = L"Manual High Speed",},

    [L"X轴偏置"] = {
                   [L"CHN"] = L"X轴偏置",
                   [L"POL"] = L"Odsuniecie osi X",
                   [L"ENG"] = L"X-axis offset",},

    [L"Y轴偏置"] = {
                   [L"CHN"] = L"Y轴偏置",
                   [L"POL"] = L"Odsuniecie osi Y",
                   [L"ENG"] = L"Y-axis offset",},

    [L"固定对刀块X机械坐标"] = {
                   [L"CHN"] = L"固定对刀块X机械坐标",
                   [L"POL"] = L"Wspolrzedne maszynowe osi X dla stalego czujnika dlugosci narzedzia",
                   [L"ENG"] = L"X mechanical Coor of fixed Cali block",},

    [L"在加工Eng文件时，需要循环加工的次数"] = {
                   [L"CHN"] = L"在加工Eng文件时，需要循环加工的次数",
                   [L"POL"] = L"Wymagana liczba cykli podczas przetwarzania pliku ENG.",
                   [L"ENG"] = L"Needed cycle processing times when doing processing of ENG file.",},

    [L"工作范围上限"] = {
                   [L"CHN"] = L"工作范围上限",
                   [L"POL"] = L"Gorny zakres przestrzeni roboczej",
                   [L"ENG"] = L"Workbench range upper limit",},

    [L"开启润滑油泵时间间隔"] = {
                   [L"CHN"] = L"开启润滑油泵时间间隔",
                   [L"POL"] = L"Interwal otwarcia pompy smarowania",
                   [L"ENG"] = L"Interval of opening lubrication pump",},
}
}
function GetLanguageString()
	lua_table = ResTable["strTable"][StringKey()]
	if lua_table == nil then
		return L"NoTable"
	else
		lua_string = lua_table[LanguageKey()]
		if lua_string == nil then
			return L"NoString"
		else
			return lua_string
		end
	end
end

function GetLanguageTotal()
	lang_table = ResTable["langTable"]
	langInfo_table = ResTable["langInfoTable"]
	count = 0
	if lang_table then
		for i,v in pairs(lang_table) do
			count = count + 1
			AddName(v)
			AddInfo(langInfo_table[v])
		end
	end
	return count
end

function GetModuleName()
	return ResTable["szModule"]
end

function GetVersion()
	return ResTable["nVersion"] 
end
