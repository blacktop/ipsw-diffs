## TextGeneration

> `/System/Library/PrivateFrameworks/TextGeneration.framework/TextGeneration`

```diff

 8.0.0.0.0
-  __TEXT.__text: 0x4a8c
-  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__text: 0x46a8
   __TEXT.__objc_methlist: 0x700
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1ab
-  __TEXT.__gcc_except_tab: 0x29c
+  __TEXT.__cstring: 0x1bb
+  __TEXT.__gcc_except_tab: 0x298
   __TEXT.__oslogstring: 0x294
   __TEXT.__dlopen_cstrs: 0x6c
   __TEXT.__unwind_info: 0x1f8
-  __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0xe5a
-  __TEXT.__objc_methtype: 0x508
-  __TEXT.__objc_stubs: 0xac0
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x12b8
+  __AUTH_CONST.__weak_auth_got: 0x8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6D31D6D-296C-354A-A2BF-4237CCB01C40
-  Functions: 156
-  Symbols:   694
-  CStrings:  310
+  UUID: 2B82EBA1-119E-3DA9-BE80-FCA482E172AC
+  Functions: 154
+  Symbols:   692
+  CStrings:  60
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<TGITextGenerationInference>\""
- "@\"<TGITextGenerationInferenceSession>\""
- "@\"<TGTextGenerationSessionDelegate>\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"TGTextGenerationConfiguration\""
- "@\"TGTextGenerationDecodingPolicy\""
- "@\"TGTextGenerationOutputConstraint\""
- "@\"TGTextGenerationPrompt\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16d24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCopying"
- "NSMutableCopying"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<TGITextGenerationInference>\",R,V_textGeneration"
- "T@\"<TGITextGenerationInferenceSession>\",&,V_tgdSession"
- "T@\"<TGTextGenerationSessionDelegate>\",W,V_delegate"
- "T@\"NSMutableArray\",R,C,V_textFragments"
- "T@\"NSMutableDictionary\",R,V_callbackByExecutionUUID"
- "T@\"NSMutableDictionary\",R,V_operationByExecutionUUID"
- "T@\"NSMutableDictionary\",R,V_outputStreamByExecutionUUID"
- "T@\"NSNumber\",C,D"
- "T@\"NSNumber\",C,V_maxWordCount"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_workQueue"
- "T@\"NSSet\",R,C,V_resources"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,D"
- "T@\"NSString\",C,V_contextText"
- "T@\"NSString\",C,V_e5FunctionName"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_instructionText"
- "T@\"NSString\",R,C,V_text"
- "T@\"NSURL\",R,C,V_url"
- "T@\"NSUUID\",R,C"
- "T@\"NSUUID\",R,C,V_uuid"
- "T@\"TGTextGenerationConfiguration\",R,C,V_configuration"
- "T@\"TGTextGenerationDecodingPolicy\",C,D"
- "T@\"TGTextGenerationDecodingPolicy\",C,V_decodingPolicy"
- "T@\"TGTextGenerationOutputConstraint\",C,D"
- "T@\"TGTextGenerationOutputConstraint\",C,V_outputConstraint"
- "T@\"TGTextGenerationPrompt\",R,C,V_prompt"
- "TB,D,GshouldProduceOutputStream"
- "TB,GshouldProduceOutputStream,V_produceOutputStream"
- "TGMutableTextGenerationConfiguration"
- "TGMutableTextGenerationOperation"
- "TGMutableTextGenerationOutputConstraint"
- "TGMutableTextGenerationPrompt"
- "TGMutableTextGenerationResource"
- "TGTextGenerationConfiguration"
- "TGTextGenerationDecodingPolicy"
- "TGTextGenerationOperation"
- "TGTextGenerationOperationDelegate"
- "TGTextGenerationOutput"
- "TGTextGenerationOutputConstraint"
- "TGTextGenerationOutputStream"
- "TGTextGenerationPrompt"
- "TGTextGenerationResource"
- "TGTextGenerationSession"
- "TQ,R"
- "TQ,R,V_type"
- "Td,R,V_score"
- "Td,V_score"
- "URLForResource:withExtension:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_callbackByExecutionUUID"
- "_configuration"
- "_contextText"
- "_decodingPolicy"
- "_delegate"
- "_description"
- "_e5FunctionName"
- "_instructionText"
- "_lock"
- "_maxWordCount"
- "_operationByExecutionUUID"
- "_outputConstraint"
- "_outputStreamByExecutionUUID"
- "_produceOutputStream"
- "_prompt"
- "_resources"
- "_score"
- "_text"
- "_textFragments"
- "_textGeneration"
- "_tgdSession"
- "_type"
- "_url"
- "_uuid"
- "_workQueue"
- "addObject:"
- "addOutput:"
- "appendString:"
- "array"
- "autorelease"
- "bundleForClass:"
- "callbackByExecutionUUID"
- "cancelOperation:"
- "cancelOperationWithExecutionUUID:"
- "class"
- "configuration"
- "conformsToProtocol:"
- "contextText"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createSessionWithUUID:configuration:"
- "createTgdSessionSync"
- "createWithResourceDict:"
- "createWithUUID:"
- "d"
- "d16@0:8"
- "debugDescription"
- "defaultConfiguration"
- "defaultConfigurationUUID"
- "defaultDecodingPolicy"
- "defaultTextGeneration"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObjects:forKeys:count:"
- "didStartOperationWithExecutionUUID:"
- "enqueueOperation:"
- "enqueueOperationSync:"
- "errorWithDomain:code:userInfo:"
- "executeOperation:callback:"
- "executionUUIDForOperation:"
- "fileURLWithPath:"
- "hash"
- "init"
- "initWithConfiguration:"
- "initWithConfiguration:textGeneration:"
- "initWithInstructionText:"
- "initWithPrompt:"
- "initWithText:score:"
- "initWithType:"
- "initWithType:url:"
- "initWithUUID:resources:decodingPolicy:"
- "initWithUUIDString:"
- "initWithWorkQueue:"
- "intValue"
- "isEqual:"
- "isEqualToSet:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "maxWordCount"
- "modelConfiguration"
- "mostRecentTextUpdate"
- "mutableCopyWithZone:"
- "numberWithDouble:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operation:didUpdateOutputStream:"
- "operationByExecutionUUID"
- "operationWithExecutionUUID:didFailWithError:"
- "operationWithExecutionUUID:didFinishWithOutputs:"
- "operationWithExecutionUUID:didStreamOutput:"
- "outputConstraint"
- "outputStreamByExecutionUUID"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "produceOutputStream"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "session:didFailOperation:error:"
- "session:didFinishOperation:outputs:"
- "session:didStartOperation:"
- "session:operation:didUpdateOutputStream:"
- "set"
- "setContextText:"
- "setDecodingPolicy:"
- "setDelegate:"
- "setE5FunctionName:"
- "setMaxWordCount:"
- "setObject:forKeyedSubscript:"
- "setOutputConstraint:"
- "setProduceOutputStream:"
- "setScore:"
- "setTgdSession:"
- "shouldProduceOutputStream"
- "start"
- "string"
- "stringWithFormat:"
- "superclass"
- "textFragments"
- "textGeneration"
- "tgdSession"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v32@0:8@\"NSUUID\"16@\"NSArray\"24"
- "v32@0:8@\"NSUUID\"16@\"NSError\"24"
- "v32@0:8@\"NSUUID\"16@\"TGTextGenerationOutput\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "workQueue"
- "zone"
- "{TGITextGenerationInferenceModelConfiguration={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
