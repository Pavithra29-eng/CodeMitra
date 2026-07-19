"""
CodeMitra Knowledge Base
------------------------
Structured, beginner-friendly explanations for common Python errors,
available in English, Hindi, and Marathi.

Each error type maps to a dict of {language: {meaning, cause, solution}}.
"""

ERROR_DATABASE = {
    "SyntaxError": {
        "english": {
            "meaning": "Python could not understand the structure of your code.",
            "cause": "This usually happens due to a missing colon, bracket, quote, or incorrect indentation.",
            "solution": "Carefully check the line mentioned in the error for missing symbols like ':' , ')' , or quotes.",
        },
        "hindi": {
            "meaning": "Python आपके code की संरचना (structure) को समझ नहीं पाया।",
            "cause": "यह आमतौर पर कोई colon, bracket, quote छूट जाने या गलत indentation की वजह से होता है।",
            "solution": "Error में बताई गई line को ध्यान से देखें और ':' , ')' या quotes जैसे symbols की जांच करें।",
        },
        "marathi": {
            "meaning": "Python ला तुमच्या code ची रचना समजली नाही.",
            "cause": "हे सहसा colon, bracket, quote गाळल्यामुळे किंवा चुकीच्या indentation मुळे होते.",
            "solution": "Error मध्ये दिलेली line नीट तपासा आणि ':' , ')' किंवा quotes आहेत का ते बघा.",
        },
    },
    "NameError": {
        "english": {
            "meaning": "You are trying to use a variable or function that Python cannot find.",
            "cause": "The variable does not exist yet, or you used it before defining it, or misspelled it.",
            "solution": "Define the variable before using it, and check the spelling matches exactly.",
        },
        "hindi": {
            "meaning": "आप ऐसे variable या function का उपयोग कर रहे हैं जो Python को नहीं मिला।",
            "cause": "यह variable अभी मौजूद नहीं है, या आपने इसे define करने से पहले इस्तेमाल किया, या spelling गलत है।",
            "solution": "Variable को इस्तेमाल करने से पहले define करें और spelling को ठीक से जांचें।",
        },
        "marathi": {
            "meaning": "तुम्ही असा variable किंवा function वापरत आहात जो Python ला सापडत नाही.",
            "cause": "हा variable अजून अस्तित्वात नाही, किंवा तो define करण्यापूर्वी वापरला गेला, किंवा spelling चुकीची आहे.",
            "solution": "Variable वापरण्यापूर्वी तो define करा आणि spelling बरोबर आहे का ते तपासा.",
        },
    },
    "TypeError": {
        "english": {
            "meaning": "You performed an operation on a value of the wrong type.",
            "cause": "For example, trying to add a number and text together, or calling something that is not a function.",
            "solution": "Check the types of the values involved using type(), and convert them if needed (e.g., str(), int()).",
        },
        "hindi": {
            "meaning": "आपने गलत type की value पर कोई operation किया है।",
            "cause": "उदाहरण के लिए, number और text को एक साथ जोड़ने की कोशिश करना, या किसी ऐसी चीज़ को call करना जो function नहीं है।",
            "solution": "type() का उपयोग करके values के types जांचें, और जरूरत पड़ने पर str(), int() से convert करें।",
        },
        "marathi": {
            "meaning": "तुम्ही चुकीच्या type च्या value वर operation केले आहे.",
            "cause": "उदाहरणार्थ, number आणि text एकत्र जोडण्याचा प्रयत्न करणे, किंवा function नसलेल्या गोष्टीला call करणे.",
            "solution": "type() वापरून values चे types तपासा, आणि गरज असल्यास str(), int() ने convert करा.",
        },
    },
    "ValueError": {
        "english": {
            "meaning": "The value provided has the right type but is not appropriate.",
            "cause": "For example, trying to convert the text 'hello' into a number using int('hello').",
            "solution": "Check that the value you are passing is actually valid for the operation, and add validation if needed.",
        },
        "hindi": {
            "meaning": "दी गई value का type सही है, लेकिन value उपयुक्त (appropriate) नहीं है।",
            "cause": "उदाहरण के लिए, int('hello') का उपयोग करके text 'hello' को number में बदलने की कोशिश करना।",
            "solution": "जांचें कि आप जो value दे रहे हैं वह उस operation के लिए मान्य है, और जरूरत पड़ने पर validation जोड़ें।",
        },
        "marathi": {
            "meaning": "दिलेल्या value चा type बरोबर आहे, पण value योग्य नाही.",
            "cause": "उदाहरणार्थ, int('hello') वापरून 'hello' या text ला number मध्ये बदलण्याचा प्रयत्न करणे.",
            "solution": "तुम्ही देत असलेली value त्या operation साठी योग्य आहे का ते तपासा, आणि गरज असल्यास validation जोडा.",
        },
    },
    "IndexError": {
        "english": {
            "meaning": "You tried to access a position in a list (or sequence) that does not exist.",
            "cause": "This usually happens when the index number is equal to or greater than the length of the list.",
            "solution": "Check the length of the list with len() before accessing an index, and remember indexing starts at 0.",
        },
        "hindi": {
            "meaning": "आपने list (या sequence) में ऐसी position को access करने की कोशिश की जो मौजूद नहीं है।",
            "cause": "यह आमतौर पर तब होता है जब index number, list की length के बराबर या उससे ज्यादा होता है।",
            "solution": "किसी index को access करने से पहले len() से list की length जांचें, और याद रखें indexing 0 से शुरू होती है।",
        },
        "marathi": {
            "meaning": "तुम्ही list (किंवा sequence) मधील अशी position access करण्याचा प्रयत्न केला जी अस्तित्वात नाही.",
            "cause": "हे सहसा तेव्हा होते जेव्हा index number हा list च्या length इतका किंवा त्यापेक्षा जास्त असतो.",
            "solution": "index access करण्यापूर्वी len() ने list ची length तपासा, आणि लक्षात ठेवा indexing 0 पासून सुरू होते.",
        },
    },
    "KeyError": {
        "english": {
            "meaning": "You tried to access a dictionary key that does not exist.",
            "cause": "The key you used is either misspelled or was never added to the dictionary.",
            "solution": "Check the key spelling, or use dict.get('key') which returns None instead of crashing if the key is missing.",
        },
        "hindi": {
            "meaning": "आपने dictionary की ऐसी key को access करने की कोशिश की जो मौजूद नहीं है।",
            "cause": "आपने जो key इस्तेमाल की है वह या तो गलत spelling में है या dictionary में कभी जोड़ी ही नहीं गई।",
            "solution": "key की spelling जांचें, या dict.get('key') इस्तेमाल करें जो key न मिलने पर crash होने के बजाय None देता है।",
        },
        "marathi": {
            "meaning": "तुम्ही dictionary मधील अशी key access करण्याचा प्रयत्न केला जी अस्तित्वात नाही.",
            "cause": "तुम्ही वापरलेली key एकतर चुकीची spelling आहे किंवा dictionary मध्ये कधी जोडलीच गेली नाही.",
            "solution": "key ची spelling तपासा, किंवा dict.get('key') वापरा जे key न सापडल्यास crash होण्याऐवजी None देते.",
        },
    },
    "ZeroDivisionError": {
        "english": {
            "meaning": "You tried to divide a number by zero, which is mathematically undefined.",
            "cause": "The denominator (the number you are dividing by) turned out to be 0.",
            "solution": "Add a check to make sure the denominator is not zero before dividing.",
        },
        "hindi": {
            "meaning": "आपने किसी number को 0 से divide करने की कोशिश की, जो mathematically अपरिभाषित (undefined) है।",
            "cause": "जिस number से आप divide कर रहे थे (denominator), वह 0 निकला।",
            "solution": "Divide करने से पहले जांचें कि denominator 0 तो नहीं है।",
        },
        "marathi": {
            "meaning": "तुम्ही एखाद्या number ला 0 ने divide करण्याचा प्रयत्न केला, जे गणिती दृष्ट्या undefined आहे.",
            "cause": "तुम्ही ज्या number ने divide करत होता (denominator), तो 0 निघाला.",
            "solution": "Divide करण्यापूर्वी denominator 0 नाही ना याची खात्री करा.",
        },
    },
    "IndentationError": {
        "english": {
            "meaning": "The spacing (indentation) of your code is inconsistent or incorrect.",
            "cause": "Python uses indentation to know which lines belong together; mixing tabs/spaces or wrong spacing breaks this.",
            "solution": "Make sure all lines in the same block use the same number of spaces (usually 4), and avoid mixing tabs and spaces.",
        },
        "hindi": {
            "meaning": "आपके code की spacing (indentation) असंगत (inconsistent) या गलत है।",
            "cause": "Python indentation का उपयोग यह जानने के लिए करता है कि कौन सी lines साथ हैं; tabs/spaces मिक्स करने या गलत spacing से यह टूट जाता है।",
            "solution": "सुनिश्चित करें कि एक ही block की सभी lines में समान संख्या में spaces (आमतौर पर 4) हों, और tabs व spaces को मिक्स न करें।",
        },
        "marathi": {
            "meaning": "तुमच्या code ची spacing (indentation) विसंगत किंवा चुकीची आहे.",
            "cause": "कोणत्या lines एकत्र आहेत हे ओळखण्यासाठी Python indentation वापरतो; tabs/spaces मिक्स केल्याने किंवा चुकीच्या spacing मुळे हे बिघडते.",
            "solution": "एकाच block मधील सर्व lines मध्ये तितकेच spaces (साधारण 4) असल्याची खात्री करा, आणि tabs व spaces मिक्स करू नका.",
        },
    },
    "AttributeError": {
        "english": {
            "meaning": "You tried to use a property or method that does not exist on that object.",
            "cause": "This often happens due to a typo, or because the object is of a different type than you expected (e.g., None).",
            "solution": "Print the object with print(type(obj)) to confirm its type, and check the correct attribute/method name.",
        },
        "hindi": {
            "meaning": "आपने ऐसी property या method का उपयोग करने की कोशिश की जो उस object पर मौजूद ही नहीं है।",
            "cause": "यह अक्सर typo की वजह से होता है, या object आपकी अपेक्षा से अलग type का होता है (जैसे None)।",
            "solution": "print(type(obj)) से object का type confirm करें, और सही attribute/method name जांचें।",
        },
        "marathi": {
            "meaning": "तुम्ही अशी property किंवा method वापरण्याचा प्रयत्न केला जी त्या object वर अस्तित्वातच नाही.",
            "cause": "हे बऱ्याचदा typo मुळे होते, किंवा object तुमच्या अपेक्षेपेक्षा वेगळ्या type चा असतो (उदा. None).",
            "solution": "print(type(obj)) वापरून object चा type खात्री करा, आणि योग्य attribute/method name तपासा.",
        },
    },
    "FileNotFoundError": {
        "english": {
            "meaning": "Python could not find the file you are trying to open.",
            "cause": "The file path may be wrong, the file may not exist, or you are running the code from a different folder.",
            "solution": "Double-check the file name and path, and make sure the file exists in that location.",
        },
        "hindi": {
            "meaning": "Python को वह file नहीं मिली जिसे आप खोलने की कोशिश कर रहे हैं।",
            "cause": "File का path गलत हो सकता है, file मौजूद नहीं हो सकती, या आप code को किसी दूसरे folder से run कर रहे हैं।",
            "solution": "File का नाम और path दोबारा जांचें, और सुनिश्चित करें कि file उस location पर मौजूद है।",
        },
        "marathi": {
            "meaning": "तुम्ही उघडण्याचा प्रयत्न करत असलेली file Python ला सापडली नाही.",
            "cause": "File चा path चुकीचा असू शकतो, file अस्तित्वात नसू शकते, किंवा तुम्ही code वेगळ्या folder मधून run करत आहात.",
            "solution": "File चे नाव आणि path पुन्हा तपासा, आणि ती file त्या location वर आहे याची खात्री करा.",
        },
    },
}

GENERIC_EXPLANATION = {
    "english": {
        "meaning": "An error occurred while running your code.",
        "cause": "This error type is not yet in CodeMitra's knowledge base.",
        "solution": "Read the raw error message below carefully, and search the error type online for more details.",
    },
    "hindi": {
        "meaning": "आपका code चलाते समय एक error आई।",
        "cause": "यह error type अभी CodeMitra के knowledge base में नहीं है।",
        "solution": "नीचे दिए गए raw error message को ध्यान से पढ़ें, और अधिक जानकारी के लिए इस error type को online खोजें।",
    },
    "marathi": {
        "meaning": "तुमचा code चालवताना एक error आली.",
        "cause": "हा error type अजून CodeMitra च्या knowledge base मध्ये नाही.",
        "solution": "खाली दिलेला raw error message नीट वाचा, आणि अधिक माहितीसाठी हा error type online शोधा.",
    },
}

LANGUAGES = {
    "English": "english",
    "हिंदी (Hindi)": "hindi",
    "मराठी (Marathi)": "marathi",
}


def get_explanation(error_type: str, language_key: str) -> dict:
    """Return the explanation dict for a given error type and language."""
    lang = LANGUAGES.get(language_key, "english")
    if error_type in ERROR_DATABASE:
        return ERROR_DATABASE[error_type][lang]
    return GENERIC_EXPLANATION[lang]
