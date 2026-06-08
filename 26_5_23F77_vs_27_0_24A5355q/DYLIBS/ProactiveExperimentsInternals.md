## ProactiveExperimentsInternals

> `/System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals`

```diff

-1311.7.0.0.0
-  __TEXT.__text: 0x2084
-  __TEXT.__auth_stubs: 0x3a0
+1331.0.1.0.0
+  __TEXT.__text: 0x1f30
   __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x90
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__cstring: 0x1af
+  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__cstring: 0x1b2
   __TEXT.__oslogstring: 0x394
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0xb5d
-  __TEXT.__objc_methtype: 0x379
-  __TEXT.__objc_stubs: 0x6c0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x298
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x468
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 19FE1052-7EBE-3E7D-856F-DC37DBA430C9
+  UUID: F5954740-745D-3FC9-9B62-CB4636195B15
   Functions: 32
-  Symbols:   272
-  CStrings:  170
+  Symbols:   275
+  CStrings:  41
 
Symbols:
+ ___175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke.5
+ ___65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.32
+ ___block_literal_global.36
+ ___block_literal_global.89
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
- ___175+[PREXPCServerHelper shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:]_block_invoke.11
- ___65-[PREResponsesServerDelegate listener:shouldAcceptNewConnection:]_block_invoke.38
- ___block_literal_global.42
- ___block_literal_global.95
- _objc_autorelease
- _objc_release
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PREResponsesProtocol>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"_PASBundleIdResolver\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B40@0:8@16@24@32"
- "B80@0:8@16@24@32@40@?48@?56@?64@?72"
- "NSObject"
- "NSXPCListenerDelegate"
- "PREResponsesProtocol"
- "PREResponsesServerDelegate"
- "PREResponsesServerRequestHandler"
- "PREXPCServer"
- "PREXPCServerHelper"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_clientProcessName"
- "T@\"NSString\",R,C"
- "T@\"_PASBundleIdResolver\",&,N,V_bundleIdResolver"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_bundleIdResolver"
- "_clientProcessName"
- "_clientProxy"
- "_pas_mappedArrayWithTransform:"
- "_registerResponsesListener"
- "addObject:"
- "autorelease"
- "boolValue"
- "bundleIdResolver"
- "categoryId"
- "checkForAndLogTrueBooleanEntitlement:connection:serviceName:"
- "class"
- "clientProcessName"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "debugDescription"
- "description"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasTrueBooleanEntitlement:connection:"
- "hash"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithCategoryId:modelId:responseClassId:replySubgroupId:replyTextId:replyText:language:isCustomResponse:isRobotResponse:"
- "initWithMachServiceName:"
- "initWithObjects:"
- "initWithProcessIdentifier:"
- "initWithScore:label:"
- "interfaceWithProtocol:"
- "isCustomResponse"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRobotResponse"
- "label"
- "lang"
- "length"
- "listener:shouldAcceptNewConnection:"
- "modelId"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preResponseItemArrayFromQuickResponses:"
- "preResponseItemsForMessage:maximumResponses:conversationTurns:context:time:language:recipientHandles:modelFilePath:modelConfigPath:espressoBinFilePath:vocabFilePath:registerDisplayed:includeCustomResponses:includeResponsesToRobots:completion:"
- "predictForMessage:conversationTurns:language:plistPath:espressoBinPath:vocabPath:heads:completion:"
- "predictForMessage:conversationTurns:localeIdentifier:plistPath:espressoBinPath:vocabPath:heads:"
- "proactiveTrigger"
- "processIdentifier"
- "quickResponsesForMessage:context:time:maxResponses:locale:recipientHandles:chunkPath:plistPath:espressoBinFilePath:vocabFilePath:includeCustomResponses:includeResponsesToRobots:"
- "quickResponsesForMessage:conversationTurns:maxResponses:localeIdentifier:recipientHandles:chunkPath:plistPath:espressoBinFilePath:vocabFilePath:useContactNames:includeCustomResponses:includeResponsesToRobots:"
- "registerDisplayedQuickResponses:plistPath:vocabPath:"
- "registerPREXPCListeners"
- "registerResponse:position:isCanned:isUsingQuickResponses:locale:modelConfigPath:vocabPath:"
- "registerResponse:position:isCanned:isUsingQuickResponses:locale:plistPath:vocabPath:"
- "release"
- "replyTextId"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "score"
- "self"
- "semanticClassId"
- "setBundleIdResolver:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientProcessName:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectProxy:"
- "shouldAcceptConnection:serviceName:whitelistedServerInterface:requestHandler:validateConnection:setupClientProxy:interruptionHandler:invalidationHandler:"
- "stringWithUTF8String:"
- "styleGroupId"
- "superclass"
- "text"
- "v124@0:8@\"NSString\"16Q24@\"NSArray\"32@\"NSString\"40@\"NSDate\"48@\"NSString\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96B104B108B112@?<v@?@\"NSArray\"@\"NSError\">116"
- "v124@0:8@16Q24@32@40@48@56@64@72@80@88@96B104B108B112@?116"
- "v16@0:8"
- "v24@0:8@16"
- "v64@0:8@\"NSString\"16@\"NSNumber\"24B32B36@\"NSString\"40@\"NSString\"48@\"NSString\"56"
- "v64@0:8@16@24B32B36@40@48@56"
- "v80@0:8@\"NSString\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSArray\"64@?<v@?@\"NSDictionary\"@\"NSError\">72"
- "v80@0:8@16@24@32@40@48@56@64@?72"
- "valueForEntitlement:"
- "zone"

```
