ResTable = {
    ["langTable"] = {
        "CHN",
        "POL",
        "ENG",
    },
    ["szModule"] = "Interpolate",
    ["nVersion"] = "1.00",
["strTable"] = {

    [L"|F|不正确的命令行参数CFG：不完整引号"] = {
                   [L"CHN"] = L"|F|不正确的命令行参数CFG：不完整引号",
                   [L"POL"] = L"|F|Niedozwolony parametr komendy CFG: wymagany jest cudzyslow (\") ",
                   [L"ENG"] = L"|F|Illegal command line parameter CFG:a quotation mark(\") is needed",},

    [L"日志文件(%s)无法打开，请检查是否存在下列问题：\n\n  . 该文件具有只读属性\n  \
	   . 如果在网络环境下，用户是否有足够权限\n  . 磁盘访问出错"] = {
                   [L"CHN"] = L"日志文件(%s)无法打开，请检查是否存在下列问题：\n\n  . 该文件具有只读属性\n  \
	   . 如果在网络环境下，用户是否有足够权限\n  . 磁盘访问出错",
                   [L"POL"] = L"Nieudana proba otwarcia pliku dziennika (%s), Prosze sprawdz czy wystepuja nastepujace problemy: \n\n\
	   . Plik jest tylko do odczytu\n\
	   . Uzytkownik nie ma wystarczajacych uprawnien w otoczeniu sieciowym\n\
	   . Blad dostepu do dysku",
                   [L"ENG"] = L"Unable to open the log file(%s), Please check whether following problems exist: \n\n\
	   . The file is read-only\n\
	   . The user has not enough privilege under a network environment\n\
	   . Error accessing the disk",},

    [L"参数配置文件已经损坏，系统已经使用备份文件替换该参数配置文件。"] = {
                   [L"CHN"] = L"参数配置文件已经损坏，系统已经使用备份文件替换该参数配置文件。",
                   [L"POL"] = L"Plik konfiguracji parametrow zostal uszkodzony. System zastapil go plikiem .bak.",
                   [L"ENG"] = L"The parameter configuration file has already been corrupted. System has replaced it with the .bak file.",},

    [L"保存参数配置文件失败！文件名'%1!s!'，错误码(%2!d!)。错误原因可能是：\n\n  .文件格式不正确。解决方法：请手动删除该文件；\n  .文件只读。解决方法：请修改文件属性；\n  .用户没有写权限。解决方法：请与系统管理员联系。\n\n在完成上述修改后，然后重新启动程序，执行存储操作。如果错误持续出现请与系统供应商联系。\n\n\n(按<取消>键，不再重复提示此信息。)"] = {
                   [L"CHN"] = L"保存参数配置文件失败！文件名'%1!s!'，错误码(%2!d!)。错误原因可能是：\n\n  .文件格式不正确。解决方法：请手动删除该文件；\n  .文件只读。解决方法：请修改文件属性；\n  .用户没有写权限。解决方法：请与系统管理员联系。\n\n在完成上述修改后，然后重新启动程序，执行存储操作。如果错误持续出现请与系统供应商联系。\n\n\n(按<取消>键，不再重复提示此信息。)",
                   [L"POL"] = L"Nieudana proba zapisu pliku konfiguracji parametru! Nazwa pliku:'%1!s!', Kod Bledu(%2!d!). Przyczyny moga byc nastepujace: \n\
   \n\
   .Format pliku nie jest wlasciwy. ROZWIAZANIE: Usun plik;\n\
   .Plik tylko do odczytu. ROZWIAZANIE: Usun atrybut tylko do odczytu;\n\
   .Uzytkownik nie posiada wystarczajacych uprawnien. ROZWIAZANIE: Skontaktuj sie z administratorem sieci.\n\
   \n\
   Po wykonaniu powyzszych zmian zrestartuj aplikacje i zapisz plik. Jesli problem wciaz wystepuje skontaktuj sie z dostawca.\n\
   \n\
   (Nacisnij przycisk ANuluj aby uniknac pokazania ponownie tego okna dialogowego)",
                   [L"ENG"] = L"Fail to save the parameter configuration file! File Name:'%1!s!', Error Code(%2!d!). The reasons that may cause the problem are: \n\
   \n\
   .The file format is not right. SOLUTION: Delete the file;\n\
   .It is read-only. SOLUTION: Remove its read-only attribute;\n\
   .User has no enough privilege. SOLUTION: Please contact with the network administrator.\n\
   \n\
   After completing all the above corrections, restart the application and then save the file. If the problem occurs continuously, please contact with the software suppliers.\n\
   \n\
   (Press Cancel button to avoid showing this information box again)",},

    [L"%s 的值必须在 %s 到 %s 之间"] = {
                   [L"CHN"] = L"%s 的值必须在 %s 到 %s 之间",
                   [L"POL"] = L"Wartosc %s musi byc pomiedzy %s i %s",
                   [L"ENG"] = L"The value of %s must be between %s and %s",},

    [L"保存参数配置文件失败!请手动删除参数文件!"] = {
                   [L"CHN"] = L"保存参数配置文件失败!请手动删除参数文件!",
                   [L"POL"] = L"Nieudana proba zapisu pliku konfiguracji parametru! Prosze usunac plik ustawien;",
                   [L"ENG"] = L"Fail to save the parameter configuration file! Please delete the settings file;",},

    [L"|F|创建参数CFG指定的目录(%s)失败。"] = {
                   [L"CHN"] = L"|F|创建参数CFG指定的目录(%s)失败。",
                   [L"POL"] = L"|F|Nieudana proba stworzenia katalogu (%s) okreslonego poprzez komende CFG.",
                   [L"ENG"] = L"|F|Failure to create the directory(%s) specified by the command line parameter CFG.",},

    [L"\n错误原因："] = {
                   [L"CHN"] = L"\n错误原因：",
                   [L"POL"] = L"\nPrzyczyna bledu: ",
                   [L"ENG"] = L"\nError REASON: ",},

		[L"0"] = {
                   [L"CHN"] = L"0",
                   [L"POL"] = L"0",
                   [L"ENG"] = L"0",},
                                      
		[L"1"] = {
                   [L"CHN"] = L"1",
                   [L"POL"] = L"1",
                   [L"ENG"] = L"1",},
                   
		[L"2"] = {
                   [L"CHN"] = L"2",
                   [L"POL"] = L"2",
                   [L"ENG"] = L"2",},
                   
		[L"3"] = {
                   [L"CHN"] = L"3",
                   [L"POL"] = L"3",
                   [L"ENG"] = L"3",},
                   
		[L"4"] = {
                   [L"CHN"] = L"4",
                   [L"POL"] = L"4",
                   [L"ENG"] = L"4",},
                   
		[L"5"] = {
                   [L"CHN"] = L"5",
                   [L"POL"] = L"5",
                   [L"ENG"] = L"5",},
                   
		[L"6"] = {
                   [L"CHN"] = L"6",
                   [L"POL"] = L"6",
                   [L"ENG"] = L"6",},
                   
		[L"7"] = {
                   [L"CHN"] = L"7",
                   [L"POL"] = L"7",
                   [L"ENG"] = L"7",},
                   
		[L"8"] = {
                   [L"CHN"] = L"8",
                   [L"POL"] = L"8",
                   [L"ENG"] = L"8",},
                   
		[L"9"] = {
                   [L"CHN"] = L"9",
                   [L"POL"] = L"9",
                   [L"ENG"] = L"9",},
                   
		[L"."] = {
                   [L"CHN"] = L".",
                   [L"POL"] = L".",
                   [L"ENG"] = L".",},
                   
		[L"-"] = {
                   [L"CHN"] = L"-",
                   [L"POL"] = L"-",
                   [L"ENG"] = L"-",},
                                      
    [L"Shift"] = {
                   [L"CHN"] = L"Shift",
                   [L"POL"] = L"Shift",
                   [L"ENG"] = L"Shift",},
                   
    [L"OK"] = {
                   [L"CHN"] = L"OK",
                   [L"POL"] = L"OK",
                   [L"ENG"] = L"OK",},                   
                   
    [L"ESC"] = {
                   [L"CHN"] = L"ESC",
                   [L"POL"] = L"ESC",
                   [L"ENG"] = L"ESC",},                   
                   
    [L"左"] = {
                   [L"CHN"] = L"左",
                   [L"POL"] = L"Left",
                   [L"ENG"] = L"Left",},                   
                   
    [L"上"] = {
                   [L"CHN"] = L"上",
                   [L"POL"] = L"Up",
                   [L"ENG"] = L"Up",},
                                      
		[L"右"] = {
                   [L"CHN"] = L"右",
                   [L"POL"] = L"Right",
                   [L"ENG"] = L"Right",},
                                      
		[L"下"] = {
                   [L"CHN"] = L"下",
                   [L"POL"] = L"Down", 
                   [L"ENG"] = L"Down",},  
                                    
		[L"帮助"] = {
                   [L"CHN"] = L"帮助",
                   [L"POL"] = L"Help",
                   [L"ENG"] = L"Help",},
                                      
		[L"菜单"] = {
                   [L"CHN"] = L"菜单",
                   [L"POL"] = L"Menu",                   
                   [L"ENG"] = L"Menu",},                   
                   
    [L"开始"] = {
                   [L"CHN"] = L"开始",
                   [L"POL"] = L"Start",                 
                   [L"ENG"] = L"Start",},                   
                                     
		[L"暂停"] = {
                   [L"CHN"] = L"暂停",
                   [L"POL"] = L"Pause",
                   [L"ENG"] = L"Pause",},
                                      
		[L"停止"] = {
                   [L"CHN"] = L"停止",
                   [L"POL"] = L"Stop",                  
                   [L"ENG"] = L"Stop",},                   
                   
    [L"断点继续"] = {
                   [L"CHN"] = L"断点继续",
                   [L"POL"] = L"Resume",                 
                   [L"ENG"] = L"Resume",},                   
                   
    [L"主轴开"] = {
                   [L"CHN"] = L"主轴开",
                   [L"POL"] = L"SPIN-ON",                  
                   [L"ENG"] = L"SPIN-ON",},                   
                                     
		[L"主轴关"] = {
                   [L"CHN"] = L"主轴关",
                   [L"POL"] = L"SPIN-OFF",
                   [L"ENG"] = L"SPIN-OFF",},
                                      
		[L"主轴档位减"] = {
                   [L"CHN"] = L"主轴档位减",
                   [L"POL"] = L"SPIN-DOWN",                  
                   [L"ENG"] = L"SPIN-DOWN",},                   
                   
    [L"主轴档位增"] = {
                   [L"CHN"] = L"主轴档位增",
                   [L"POL"] = L"SPIN-UP",                  
                   [L"ENG"] = L"SPIN-UP",},                   
                                                         
		[L"高低速"] = {
                   [L"CHN"] = L"高低速",
                   [L"POL"] = L"Speed High",                  
                   [L"ENG"] = L"Speed High",},                   
                   
    [L"低速"] = {
                   [L"CHN"] = L"低速",
                   [L"POL"] = L"Speed Low",                 
                   [L"ENG"] = L"Speed Low",},                   
                   
    [L"倍率减"] = {
                   [L"CHN"] = L"倍率减",
                   [L"POL"] = L"MULT-DOWN",                  
                   [L"ENG"] = L"MULT-DOWN",},                   
                                     
		[L"倍率加"] = {
                   [L"CHN"] = L"倍率加",
                   [L"POL"] = L"MULT-UP",
                   [L"ENG"] = L"MULT-UP",},
                                      
		[L"对刀"] = {
                   [L"CHN"] = L"对刀",
                   [L"POL"] = L"Calibrate",                  
                   [L"ENG"] = L"Calibrate",},                   
                   
    [L"坐标系切换"] = {
                   [L"CHN"] = L"坐标系切换",
                   [L"POL"] = L"Coordinate",                   
                   [L"ENG"] = L"Coordinate",},                   
                                                                            
		[L"机械原点"] = {
                   [L"CHN"] = L"机械原点",
                   [L"POL"] = L"Home",
                   [L"ENG"] = L"Home",},
                                      
		[L"工件原点"] = {
                   [L"CHN"] = L"工件原点",
                   [L"POL"] = L"Origin",  
                   [L"ENG"] = L"Origin",},  
                                    
		[L"固定点"] = {
                   [L"CHN"] = L"固定点",
                   [L"POL"] = L"Fixed",
                   [L"ENG"] = L"Fixed",},
                                      
		[L"K1"] = {
                   [L"CHN"] = L"K1",
                   [L"POL"] = L"K1",                  
                   [L"ENG"] = L"K1",},                   
                   
    [L"K2"] = {
                   [L"CHN"] = L"K2",
                   [L"POL"] = L"K2",                 
                   [L"ENG"] = L"K2",},                   
                                     
		[L"微调"] = {
                   [L"CHN"] = L"微调",
                   [L"POL"] = L"Jiggle",
                   [L"ENG"] = L"Jiggle",},
                                      
		[L"首次对刀"] = {
                   [L"CHN"] = L"首次对刀",
                   [L"POL"] = L"Cut-First",                  
                   [L"ENG"] = L"Cut-First",},                   
                   
    [L"换刀对刀"] = {
                   [L"CHN"] = L"换刀对刀",
                   [L"POL"] = L"Cut-Second",                 
                   [L"ENG"] = L"Cut-Second",},                   
                                      
		[L"测刀具长度"] = {
                   [L"CHN"] = L"测刀具长度",
                   [L"POL"] = L"ToolLength",
                   [L"ENG"] = L"ToolLength",},  
                                    
		[L"手动松夹刀"] = {
                   [L"CHN"] = L"手动松夹刀",
                   [L"POL"] = L"ToolOnOff",
                   [L"ENG"] = L"ToolOnOff",},
                                      
		[L"当前加工文件信息"] = {
                   [L"CHN"] = L"当前加工文件信息",
                   [L"POL"] = L"CurFileInfo",                 
                   [L"ENG"] = L"CurFileInfo",},                   
                   
    [L"自定义 1"] = {
                   [L"CHN"] = L"自定义 1",
                   [L"POL"] = L"Custom 1",
                   [L"ENG"] = L"Custom 1",}, 
                                     
    [L"自定义 2"] = {
                   [L"CHN"] = L"自定义 2",
                   [L"POL"] = L"Custom 2",
                   [L"ENG"] = L"Custom 2",},
                        
		[L"自定义 3"] = {
                   [L"CHN"] = L"自定义 3",
                   [L"POL"] = L"Custom 3",
                   [L"ENG"] = L"Custom 3",},
                        
		[L"自定义 4"] = {
                   [L"CHN"] = L"自定义 4",
                   [L"POL"] = L"Custom 4",
                   [L"ENG"] = L"Custom 4",},
                        
		[L"自定义 5"] = {
                   [L"CHN"] = L"自定义 5",
                   [L"POL"] = L"Custom 5",
                   [L"ENG"] = L"Custom 5",},
                   
		[L"X-"] = {
                   [L"CHN"] = L"X-",
                   [L"POL"] = L"X-",
                   [L"ENG"] = L"X-",},     
                                                        
		[L"X+"] = {
                   [L"CHN"] = L"X+",
                   [L"POL"] = L"X+",
                   [L"ENG"] = L"X+",},  
                      
		[L"Y-"] = {
                   [L"CHN"] = L"Y-",
                   [L"POL"] = L"Y-",
                   [L"ENG"] = L"Y-",},   
                     
		[L"Y+"] = {
                   [L"CHN"] = L"Y+",
                   [L"POL"] = L"Y+",
                   [L"ENG"] = L"Y+",},   
                     
		[L"Z-"] = {
                   [L"CHN"] = L"Z-",
                   [L"POL"] = L"Z-",
                   [L"ENG"] = L"Z-",},  
                      
		[L"Z+"] = {
                   [L"CHN"] = L"Z+",
                   [L"POL"] = L"Z+",
                   [L"ENG"] = L"Z+",},  
                      
		[L"A-"] = {
                   [L"CHN"] = L"A-",
                   [L"POL"] = L"A-",
                   [L"ENG"] = L"A-",},  
                      
		[L"A+"] = {
                   [L"CHN"] = L"A+",
                   [L"POL"] = L"A+",
                   [L"ENG"] = L"A+",},   
                     
		[L"XY0"] = {
                   [L"CHN"] = L"XY0",
                   [L"POL"] = L"XY0",
                   [L"ENG"] = L"XY0",}, 
                       
		[L"X0"] = {
                   [L"CHN"] = L"X0",
                   [L"POL"] = L"X0",
                   [L"ENG"] = L"X0",},     
                                                                  
 		[L"Y0"] = {
                   [L"CHN"] = L"Y0",
                   [L"POL"] = L"Y0",
                   [L"ENG"] = L"Y0",},  
                                     
		[L"Z0"] = {
                   [L"CHN"] = L"Z0",
                   [L"POL"] = L"Z0",
                   [L"ENG"] = L"Z0",}, 
                                                        
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