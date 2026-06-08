## AssistantTTSPlugin

> `/System/Library/Assistant/Plugins/AssistantTTSPlugin.assistantBundle/AssistantTTSPlugin`

```diff

-3520.7.1.0.0
-  __TEXT.__text: 0xc20
-  __TEXT.__auth_stubs: 0x1b0
+3600.8.1.0.0
+  __TEXT.__text: 0xb04
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x88
-  __TEXT.__cstring: 0x37
-  __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x7d
-  __TEXT.__objc_methname: 0x459
-  __TEXT.__objc_methtype: 0x1fc
-  __TEXT.__objc_stubs: 0x400
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__cstring: 0x39
+  __TEXT.__unwind_info: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__objc_const: 0x460
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4662EA5A-571B-371A-B93A-F3203E88B6F7
+  UUID: D436C929-641E-39CE-B014-7F804E7CF749
   Functions: 11
-  Symbols:   61
-  CStrings:  103
+  Symbols:   60
+  CStrings:  5
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x28
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x27
Functions:
~ sub_23936dca0 -> sub_23bf69ca0 : 920 -> 888
~ sub_23936e038 -> sub_23bf6a018 : 12 -> 124
~ sub_23936e044 -> sub_23bf6a094 : 64 -> 1116
~ sub_23936e08c -> sub_23bf6a4f8 : 1188 -> 12
~ sub_23936e530 -> sub_23bf6a504 : 124 -> 12
~ sub_23936e5ac -> sub_23bf6a510 : 12 -> 452
~ sub_23936e5b8 -> sub_23bf6a6d4 : 64 -> 176
~ sub_23936e600 -> sub_23bf6a78c : 188 -> 12
~ sub_23936e6bc -> sub_23bf6a798 : 516 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@\"SATTSEstimateTTSRequestDuration\""
- "@\"SATTSSpeechSynthesisStreaming\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AFServiceCommand"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"SATTSEstimateTTSRequestDuration\",&,N,V_request"
- "T@\"SATTSSpeechSynthesisStreaming\",&,N,V_streamObject"
- "TQ,R"
- "VSPluginTTSDurationEstimation"
- "VSPluginTTSForwardStreamHandler"
- "VSPluginTTSUnspeakableRangeHandler"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_request"
- "_streamObject"
- "addObject:"
- "array"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "description"
- "dictionary"
- "estimateDurationOfRequest:"
- "forwardStreamObject:"
- "gender"
- "genderFromString:"
- "hash"
- "init"
- "initWithDictionary:"
- "initWithLanguage:"
- "initWithLocale:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "locale"
- "localeWithLocaleIdentifier:"
- "numberWithDouble:"
- "objectForKeyedSubscript:"
- "parseStringWithFormat:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithCompletion:"
- "performWithCompletion:serviceHelper:"
- "performWithCompletion:serviceHelper:executionInfo:"
- "rangeValue"
- "release"
- "request"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setDurations:"
- "setGender:"
- "setHandleTTSCodes:"
- "setLanguageCode:"
- "setLength:"
- "setRequest:"
- "setResults:"
- "setStart:"
- "setStreamObject:"
- "setText:"
- "sharedInstance"
- "streamObject"
- "superclass"
- "texts"
- "unspeakableRangeOfText:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v32@0:8@?16@24"
- "v32@0:8@?<v@?@\"NSDictionary\">16@\"<AFServiceHelper>\"24"
- "v40@0:8@?16@24@32"
- "v40@0:8@?<v@?@\"NSDictionary\">16@\"<AFServiceHelper>\"24@\"AFCommandExecutionInfo\"32"
- "zone"

```
