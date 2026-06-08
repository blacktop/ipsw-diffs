## AXSpeakFingerManager

> `/System/Library/PrivateFrameworks/AXSpeakFingerManager.framework/AXSpeakFingerManager`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x1680
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x48c
+3229.1.6.0.0
+  __TEXT.__text: 0x1458
+  __TEXT.__objc_methlist: 0x4ac
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__cstring: 0x175
+  __TEXT.__cstring: 0x179
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x100
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x10fe
-  __TEXT.__objc_methtype: 0x5e0
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x428
+  __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0xc0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x558
+  __AUTH_CONST.__objc_const: 0x588
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x180
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A8250AF-9AAD-33D8-B536-F3620AD4A867
-  Functions: 48
-  Symbols:   292
-  CStrings:  274
+  UUID: 4D2BCE2C-24EA-3165-BFFD-2457C8D48963
+  Functions: 50
+  Symbols:   298
+  CStrings:  43
 
Symbols:
+ -[AXSpeakFingerManager lastDisplayID]
+ -[AXSpeakFingerManager setLastDisplayID:]
+ -[AXSpeakFingerManager speakElementAtLocation:displayID:]
+ GCC_except_table42
+ _OBJC_IVAR_$_AXSpeakFingerManager._lastDisplayID
+ ___block_literal_global.5
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$elementAtCoordinate:withVisualPadding:displayID:
+ _objc_msgSend$lastDisplayID
+ _objc_msgSend$setLastDisplayID:
+ _objc_msgSend$speakElementAtLocation:displayID:
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
+ _speakElementAtLocation:displayID:.LastSpeechTime
- GCC_except_table2
- _AXSpeakFingerBundle.cold.1
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_msgSend$elementAtCoordinate:withVisualPadding:
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x24
- _objc_retain_x28
- _speakElementAtLocation:.LastSpeechTime
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"24@0:8Q16"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXElement\""
- "@\"AXOrator\""
- "@\"AXUIClient\""
- "@\"NSArray\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16Q24@\"NSString\"32^@40"
- "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
- "@\"NSMutableArray\""
- "@\"NSSet\"24@0:8Q16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@\"UIImpactFeedbackGenerator\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "AXOratorDelegate"
- "AXUIClientDelegate"
- "AXUIService"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"AXElement\",&,N,V_currentSpeakFingerElement"
- "T@\"AXOrator\",&,N,V_orator"
- "T@\"NSArray\",&,N,V_elementsForUnitTests"
- "T@\"NSMutableArray\",&,N,V_stateUpdateBlocks"
- "T@\"NSString\",&,N,V_lastSpeakUnderFingerPhrase"
- "T@\"NSString\",&,N,V_springBoardActionHandlerId"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"UIImpactFeedbackGenerator\",&,N,V_hapticGenerator"
- "TB,N,V_inUnitTestMode"
- "TB,N,V_unitTestSpeaking"
- "TQ,N,V_speakFingerState"
- "TQ,R"
- "T{CGPoint=dd},N,V_lastTouchPoint"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_currentSpeakFingerElement"
- "_elementsForUnitTests"
- "_hapticGenerator"
- "_inUnitTestMode"
- "_lastSpeakUnderFingerPhrase"
- "_lastTouchPoint"
- "_orator"
- "_removeFocusRingForElement:"
- "_speakFingerState"
- "_speakFingerStateChanged"
- "_springBoardActionHandlerId"
- "_stateUpdateBlocks"
- "_unitTestSpeaking"
- "_updateFocusRingForWebElement:remove:"
- "_voiceOverDisplayManagerClient"
- "accessQueueForProcessingMessageWithIdentifier:"
- "array"
- "autorelease"
- "axSafelyAddObject:"
- "boolWithAXAttribute:"
- "bundleForClass:"
- "class"
- "conformsToProtocol:"
- "connectionWillBeInterruptedForClientWithIdentifier:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "content"
- "convertPath:fromContextId:"
- "convertRect:fromContextId:"
- "count"
- "currentSpeakFingerElement"
- "d28@0:8@16B24"
- "dealloc"
- "debugDescription"
- "description"
- "desiredWindowLevelForContentViewController:userInteractionEnabled:"
- "dictionary"
- "elementAtCoordinate:withVisualPadding:"
- "elementsForUnitTests"
- "enumerateObjectsUsingBlock:"
- "fingerWasLiftedInSpeakUnderFingerMode"
- "getLastSpeakUnderFingerPhrase"
- "hapticGenerator"
- "hasAllTraits:"
- "hasAnyTraits:"
- "hash"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "identifier"
- "ignoreLogging"
- "impactOccurred"
- "inUnitTestMode"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "initWithStyle:"
- "isAccessibleElement"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
- "isSpeaking"
- "label"
- "lastSpeakUnderFingerPhrase"
- "lastTouchPoint"
- "length"
- "localizedStringForKey:value:table:"
- "messageWithIdentifierRequiresWritingBlock:"
- "messageWithIdentifierShouldBeProcessedAsynchronously:"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "orator"
- "orator:willSpeakRange:ofContent:"
- "oratorDidCancelSpeaking:"
- "oratorDidChangeSpeakingRate:"
- "oratorDidFinishSpeaking:"
- "oratorDidPauseSpeaking:"
- "oratorDidResumeSpeaking:"
- "oratorDidStartSpeaking:"
- "oratorShouldFetchNextElements:shouldScrollOpaqueProviderIfNecessary:"
- "performAction:withValue:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "possibleRequiredEntitlementsForProcessingMessageWithIdentifier:"
- "processInitializationMessage:"
- "processMessage:withIdentifier:fromClientWithIdentifier:error:"
- "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:completion:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
- "registerBlockForStateChange:"
- "registerSpringBoardActionHandler:withIdentifierCallback:"
- "release"
- "removeActionHandler:"
- "requiredEntitlementForProcessingMessageWithIdentifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "server"
- "serviceTypeForClientWithIdentifier:"
- "serviceWasFullyInitialized"
- "setAudioSessionInactiveTimeout:"
- "setContent:"
- "setCurrentSpeakFingerElement:"
- "setCursorFrame:withPath:withContextId:element:forceRefresh:animated:"
- "setDelegate:"
- "setElementsForUnitTests:"
- "setHapticGenerator:"
- "setInUnitTestMode:"
- "setLastSpeakUnderFingerPhrase:"
- "setLastTouchPoint:"
- "setObject:forKeyedSubscript:"
- "setOrator:"
- "setSpeakFingerState:"
- "setSpeakingContext:"
- "setSpringBoardActionHandlerId:"
- "setStateUpdateBlocks:"
- "setUnitTestSpeaking:"
- "sharedInstance"
- "speakElementAtLocation:"
- "speakFingerState"
- "speakUnderFingerModeFinishedTalking"
- "speakUnderFingerModeStarted"
- "springBoardActionHandlerId"
- "startSpeakingWithPreferredLanguage:error:"
- "stateUpdateBlocks"
- "stopSpeaking:"
- "stringWithAXAttribute:"
- "superclass"
- "systemWideElement"
- "uiElement"
- "unitTestSpeaking"
- "userEventOccurred"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "userManuallyExitedSpeakUnderFingerMode"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AXOrator\"16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8@\"AXOrator\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8{CGPoint=dd}16"
- "v48@0:8@\"AXOrator\"16{_NSRange=QQ}24@\"NSString\"40"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSDictionary\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8@16{_NSRange=QQ}24@40"
- "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16Q24@32i40@?44"
- "v76@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16^{CGPath=}48I56@60B68B72"
- "value"
- "windowContextId"
- "zone"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"

```
