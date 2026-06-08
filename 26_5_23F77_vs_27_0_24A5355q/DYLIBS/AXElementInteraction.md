## AXElementInteraction

> `/System/Library/PrivateFrameworks/AXElementInteraction.framework/AXElementInteraction`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x1444
-  __TEXT.__auth_stubs: 0x360
+3229.1.6.0.0
+  __TEXT.__text: 0x1530
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x1b9
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x3d
-  __TEXT.__objc_methname: 0x83e
-  __TEXT.__objc_methtype: 0x2cb
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x78
+  __TEXT.__cstring: 0x1be
+  __TEXT.__unwind_info: 0xe8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x310
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0xc0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A47CBDA1-BF5D-3D67-BD18-072A41BD69B3
-  Functions: 36
-  Symbols:   231
-  CStrings:  171
+  UUID: F959FA26-21BA-34B7-90EF-087C89A5E560
+  Functions: 35
+  Symbols:   229
+  CStrings:  39
 
Symbols:
+ GCC_except_table29
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.388
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
- +[AXElementInteractionManager sharedManager].cold.1
- GCC_except_table6
- ___block_literal_global.347
- ___block_literal_global.352
- ___block_literal_global.367
- _objc_retain
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ __axEventHandler : 216 -> 220
~ -[AXElementInteractionManager _registerForAXNotifications:] : 192 -> 304
~ ___50-[AXElementInteractionManager _handleScreenChange]_block_invoke : 84 -> 80
~ -[AXElementInteractionManager _allowDelegateToDecideElement:] : 212 -> 196
~ -[AXElementInteractionManager initializeFocus] : 464 -> 436
~ -[AXElementInteractionManager focusedElement] : 56 -> 8
~ -[AXElementInteractionManager _highlightElement:] : 288 -> 276
~ -[AXElementInteractionManager _moveToElement:] : 180 -> 168
~ -[AXElementInteractionManager _moveFocusByHitTesting:] : 1188 -> 1480
~ ___54-[AXElementInteractionManager _moveFocusByHitTesting:]_block_invoke : 192 -> 184
~ -[AXElementInteractionManager _clientIdentifier] : 164 -> 152
~ -[AXElementInteractionManager _client] : 140 -> 132
~ ___72-[AXElementInteractionManager _sendMessage:withIdentifier:errorHandler:]_block_invoke : 216 -> 212
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXElementInteractionManagerDelegate>\""
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXElement\""
- "@\"AXUIClient\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "AXElementInteractionManager"
- "AXUIClientDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AXElementInteractionManagerDelegate>\",W,N,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_displayCursor"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__AXObserver=}"
- "_allowDelegateToDecideElement:"
- "_axEventObserver"
- "_client"
- "_clientIdentifier"
- "_delegate"
- "_displayCursor"
- "_focusedElement"
- "_handleLayoutChange"
- "_handleScreenChange"
- "_highlightElement:"
- "_initializeAXObserver"
- "_interactionEnabled"
- "_moveFocusByHitTesting:"
- "_moveToElement:"
- "_registerForAXNotifications:"
- "_sendMessage:withIdentifier:errorHandler:"
- "_sendMessageWithIdentifier:errorHandler:"
- "applicationOrientation"
- "autorelease"
- "axElementInteraction:shouldMoveToElement:"
- "axElementInteractionManagerScreenChanged:"
- "ax_errorWithDomain:code:description:"
- "class"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "currentApplications"
- "debugDescription"
- "delegate"
- "description"
- "dictionary"
- "displayCursor"
- "elementAtCoordinate:withVisualPadding:"
- "endInteractionMode"
- "firstElementInApplicationForFocus"
- "firstObject"
- "focusedElement"
- "hash"
- "i20@0:8B16"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "initializeFocus"
- "isAccessibleElement"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isValid"
- "mainAccessQueue"
- "nextElementsWithCount:"
- "numberWithInt:"
- "performActivate"
- "performDirectionalNavigation:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "press"
- "processIdentifier"
- "processInfo"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scrollToVisible"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "setDelegate:"
- "setDisplayCursor:"
- "setObject:forKeyedSubscript:"
- "sharedManager"
- "startInteractionMode"
- "stringWithFormat:"
- "superclass"
- "systemApplication"
- "systemWideAXUIElement"
- "systemWideElement"
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
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v32@0:8Q16@?24"
- "v40@0:8@16Q24@?32"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "windowContextId"
- "zone"

```
