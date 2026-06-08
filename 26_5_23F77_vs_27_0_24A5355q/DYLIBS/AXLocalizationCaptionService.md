## AXLocalizationCaptionService

> `/System/Library/PrivateFrameworks/AXLocalizationCaptionService.framework/AXLocalizationCaptionService`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x468
-  __TEXT.__auth_stubs: 0x130
+3229.1.6.0.0
+  __TEXT.__text: 0x408
   __TEXT.__objc_methlist: 0x1e4
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x8b
-  __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0x4cc
-  __TEXT.__objc_methtype: 0x247
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__cstring: 0x8d
+  __TEXT.__unwind_info: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
-  __AUTH_CONST.__auth_got: 0xa0
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x260
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 065E3F87-3D9A-3DD2-A63E-D1DAC85AEAAB
-  Functions: 12
-  Symbols:   97
-  CStrings:  91
+  UUID: D3E84CAD-46E9-33ED-8FA5-956AE4AFA9F5
+  Functions: 11
+  Symbols:   98
+  CStrings:  8
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x22
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x23
+ _objc_retain_x4
- +[AXLocalizationCaptionService service].cold.1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ -[AXLocalizationCaptionService _clientIdentifier] : 164 -> 152
~ -[AXLocalizationCaptionService client] : 140 -> 132
~ +[AXLocalizationCaptionService _sendMessage:withIdentifier:errorHandler:] : 264 -> 260
~ ___73+[AXLocalizationCaptionService _sendMessage:withIdentifier:errorHandler:]_block_invoke : 168 -> 172
~ -[AXLocalizationCaptionService connectionWithServiceWasInterruptedForUserInterfaceClient:] : 120 -> 116
~ -[AXLocalizationCaptionService setClient:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "AXLocalizationCaptionService"
- "AXUIClientDelegate"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"AXUIClient\",&,N,V_client"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_client"
- "_clientIdentifier"
- "_sendMessage:withIdentifier:errorHandler:"
- "autorelease"
- "class"
- "client"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "debugDescription"
- "description"
- "hash"
- "initWithIdentifier:serviceBundleName:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localizationQACaptionMode"
- "mainAccessQueue"
- "numberWithInt:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "processInfo"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "service"
- "setClient:"
- "setDelegate:"
- "sharedInstance"
- "startService"
- "stopService"
- "stringWithFormat:"
- "superclass"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@16"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v40@0:8@16Q24@?32"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "zone"

```
