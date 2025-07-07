## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-580.0.0.0.0
-  __TEXT.__text: 0x5764
+588.0.0.0.0
+  __TEXT.__text: 0x5844
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0x78

   __TEXT.__oslogstring: 0x548
   __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x1639
-  __TEXT.__objc_methtype: 0x50c
+  __TEXT.__objc_methname: 0x1667
+  __TEXT.__objc_methtype: 0x538
   __TEXT.__objc_stubs: 0x1000
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x378

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACB46C0C-3945-3E27-94F0-5CC4C4407CFC
+  UUID: F4243A1B-FC59-3E51-9BCE-DFEEA3D73760
   Functions: 183
-  Symbols:   806
-  CStrings:  368
+  Symbols:   810
+  CStrings:  367
 
Symbols:
+ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke.cold.2
+ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke.cold.2
+ _objc_msgSend$fetchAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:
+ _objc_msgSend$fetchHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:
- _objc_msgSend$fetchAllWebApplicationHistory:profileIdentifier:replyHandler:
- _objc_msgSend$fetchHistoryDuringInterval:webApplication:profileIdentifier:replyHandler:
Functions:
~ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke : 304 -> 412
~ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke : 300 -> 408
~ _OUTLINED_FUNCTION_4 : 16 -> 28
~ _OUTLINED_FUNCTION_5 : 24 -> 16
~ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke.cold.1 : 112 -> 144
~ -[STWebHistory deleteHistoryForURL:].cold.1 -> ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke.cold.2 : 84 -> 112
~ -[STWebHistory deleteHistoryForURL:].cold.2 -> -[STWebHistory deleteHistoryForURL:].cold.1 : 116 -> 92
~ ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.cold.1 -> -[STWebHistory deleteHistoryForURL:].cold.2 : 124 -> 116
~ ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17.cold.1 -> ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.cold.1 : 148 -> 124
CStrings:
+ "fetchAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "fetchHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSSet\"@\"NSError\">40"
+ "v56@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSSet\"@\"NSError\">48"
- "fetchAllWebApplicationHistory:profileIdentifier:replyHandler:"
- "fetchHistoryDuringInterval:webApplication:profileIdentifier:replyHandler:"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSSet\"@\"NSError\">40"

```
