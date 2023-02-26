ResTable = {
    ["langTable"] = {
        "CHN",
        "POL",
        "ENG",
    },
    ["szModule"] = "Interpolate",
    ["nVersion"] = "1.00",
["strTable"] = {

    [L"否"] = {
                   [L"CHN"] = L"否",
                   [L"POL"] = L"Nie",
                   [L"ENG"] = L"No",},

    [L"  系统退出!"] = {
                   [L"CHN"] = L"  系统退出!",
                   [L"POL"] = L"Zamykanie systemu!",
                   [L"ENG"] = L"System quit!",},

    [L"输入厂商密码："] = {
                   [L"CHN"] = L"输入厂商密码：",
                   [L"POL"] = L"Wprowadz haslo producenta:",
                   [L"ENG"] = L"Input manufactu-rer password:",},

    [L"输入操作员密码："] = {
                   [L"CHN"] = L"输入操作员密码：",
                   [L"POL"] = L"Wprowadz haslo operatora:",
                   [L"ENG"] = L"Input operator  password:",},

    [L"输入制造商密码："] = {
                   [L"CHN"] = L"输入制造商密码：",
                   [L"POL"] = L"Wprowadz haslo dewelopera:",
                   [L"ENG"] = L"Input developer password:",},

    [L"  值："] = {
                   [L"CHN"] = L"  值：",
                   [L"POL"] = L"Wartosc:",
                   [L"ENG"] = L"Value:",},

    [L"|M|系统退出"] = {
                   [L"CHN"] = L"|M|系统退出",
                   [L"POL"] = L"|M|Zamykanie systemu",
                   [L"ENG"] = L"|M|System quit",},

    [L"单位："] = {
                   [L"CHN"] = L"单位：",
                   [L"POL"] = L"Jednostka :",
                   [L"ENG"] = L"Unit :",},

    [L"描述："] = {
                   [L"CHN"] = L"描述：",
                   [L"POL"] = L"Spec.:",
                   [L"ENG"] = L"Spec.:",},

    [L"是"] = {
                   [L"CHN"] = L"是",
                   [L"POL"] = L"Tak",
                   [L"ENG"] = L"Yes",},

    [L"密码输入错误！"] = {
                   [L"CHN"] = L"密码输入错误！",
                   [L"POL"] = L"Wprowadzono bledne haslo!",
                   [L"ENG"] = L"Wrong Passw-ord Entered!",},
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