## SpeakThisServices

> `/System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x15c8
-  __TEXT.__auth_stubs: 0x2a0
+3229.1.6.0.0
+  __TEXT.__text: 0x1414
   __TEXT.__objc_methlist: 0x34c
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x376
+  __TEXT.__cstring: 0x378
   __TEXT.__oslogstring: 0xfc
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x30
-  __TEXT.__objc_methname: 0xa55
-  __TEXT.__objc_methtype: 0x320
-  __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2a8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x400
   __AUTH_CONST.__objc_const: 0x300
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6094D21E-B281-3052-B3AD-02BEA48D32DF
-  Functions: 49
-  Symbols:   243
-  CStrings:  218
+  UUID: F27D8AC5-302B-3BDD-9DDA-1A6D6E4030DC
+  Functions: 44
+  Symbols:   237
+  CStrings:  75
 
Symbols:
+ ___block_literal_global.395
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- +[SpeakThisServices sharedInstance].cold.1
- -[SpeakThisServices userInterfaceClient:processMessageFromServer:withIdentifier:error:].cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- ___79-[SpeakThisServices connectionWithServiceWasInterruptedForUserInterfaceClient:]_block_invoke_2.cold.1
- ___block_literal_global.374
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ -[SpeakThisServices init] : 272 -> 280
~ ___25-[SpeakThisServices init]_block_invoke : 144 -> 140
~ -[SpeakThisServices _checkSpringBoardStarted] : 256 -> 252
~ -[SpeakThisServices speakThisWithOptions:errorHandler:] : 220 -> 212
~ -[SpeakThisServices speakThisWithOptions:useAppAtPoint:errorHandler:] : 332 -> 316
~ -[SpeakThisServices speakThisWithOptions:forAppWithBundleID:errorHandler:] : 252 -> 248
~ -[SpeakThisServices speakThisWithOptions:forSceneID:errorHandler:] : 252 -> 248
~ -[SpeakThisServices speakThisWithOptions:forAppWithBundleID:rootElementAccessibilityIdentifier:errorHandler:] : 276 -> 284
~ -[SpeakThisServices updateSpeakingRateTo:errorHandler:] : 220 -> 212
~ -[SpeakThisServices connectionWithServiceWasInterruptedForUserInterfaceClient:] : 296 -> 244
~ ___79-[SpeakThisServices connectionWithServiceWasInterruptedForUserInterfaceClient:]_block_invoke : 164 -> 160
~ ___79-[SpeakThisServices connectionWithServiceWasInterruptedForUserInterfaceClient:]_block_invoke_2 : 92 -> 136
~ -[SpeakThisServices userInterfaceClient:processMessageFromServer:withIdentifier:error:] : 140 -> 208
~ -[SpeakThisServices _clientIdentifier] : 164 -> 152
~ -[SpeakThisServices _client] : 140 -> 132
~ -[SpeakThisServices userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:] : 568 -> 488
~ -[SpeakThisServices _sendMessage:withIdentifier:errorHandler:completionHandler:] : 540 -> 492
~ ___80-[SpeakThisServices _sendMessage:withIdentifier:errorHandler:completionHandler:]_block_invoke : 328 -> 316
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "@?"
- "@?16@0:8"
- "AXUIClientDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSObject"
- "Q16@0:8"
- "SpeakThisServices"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,N,V_errorHandlerFromPriorShowControllerAttempt"
- "TB,N,V_systemAppReady"
- "TB,N,V_triedToShowSpeechControllerBeforeSBReady"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_checkSpringBoardStarted"
- "_client"
- "_clientIdentifier"
- "_descriptionForErrorCode:"
- "_descriptionForMessageIdentifier:"
- "_errorHandlerCallbacks"
- "_errorHandlerFromPriorShowControllerAttempt"
- "_sendMessage:withIdentifier:errorHandler:"
- "_sendMessage:withIdentifier:errorHandler:completionHandler:"
- "_sendMessageWithIdentifier:errorHandler:"
- "_systemAppReady"
- "_triedToShowSpeechControllerBeforeSBReady"
- "autorelease"
- "ax_errorWithDomain:code:description:"
- "class"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didCancelSpeakThisErrorHandler:"
- "errorHandlerFromPriorShowControllerAttempt"
- "fastForward:"
- "hash"
- "hideSpeechController:"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "integerValue"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "keyboardFrameWillUpdate:errorHandler:"
- "mainAccessQueue"
- "mutableCopy"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "pauseSpeaking:"
- "performAsynchronousWritingBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "processInfo"
- "release"
- "respondsToSelector:"
- "resumeSpeaking:"
- "retain"
- "retainCount"
- "rewind:"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "setDelegate:"
- "setErrorHandlerFromPriorShowControllerAttempt:"
- "setObject:forKeyedSubscript:"
- "setSystemAppReady:"
- "setTriedToShowSpeechControllerBeforeSBReady:"
- "sharedInstance"
- "showSpeechController"
- "showSpeechController:"
- "speakFaster:"
- "speakSlower:"
- "speakThisMessageKeyKBFrame"
- "speakThisWithOptions:errorHandler:"
- "speakThisWithOptions:forAppWithBundleID:errorHandler:"
- "speakThisWithOptions:forAppWithBundleID:rootElementAccessibilityIdentifier:errorHandler:"
- "speakThisWithOptions:forSceneID:errorHandler:"
- "speakThisWithOptions:useAppAtPoint:errorHandler:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "systemAppReady"
- "toggleSpeaking:"
- "triedToShowSpeechControllerBeforeSBReady"
- "updateSpeakingRateTo:errorHandler:"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8q16@?24"
- "v40@0:8@16Q24@?32"
- "v40@0:8q16@24@?32"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@?32@?40"
- "v48@0:8q16@24@32@?40"
- "v48@0:8q16{CGPoint=dd}24@?40"
- "zone"

```
