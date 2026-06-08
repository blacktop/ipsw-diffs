## DiagnosticsSessionAvailability

> `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/DiagnosticsSessionAvailability`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0x12b0
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0xd0
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x357
+1351.0.0.0.0
+  __TEXT.__text: 0x109c
+  __TEXT.__objc_methlist: 0xd4
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__cstring: 0x345
   __TEXT.__oslogstring: 0xe0
-  __TEXT.__unwind_info: 0xc0
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x3cf
-  __TEXT.__objc_methtype: 0xef
-  __TEXT.__objc_stubs: 0x2e0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xf8
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe0
-  __AUTH_CONST.__const: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x80
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0xf0
+  __AUTH_CONST.__objc_const: 0xe8
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 485A7118-BADC-36EE-BB8C-B021CC6ED03B
-  Functions: 42
-  Symbols:   190
-  CStrings:  79
+  UUID: CC581F9B-03EE-38A2-86DE-41A38A2BBF60
+  Functions: 37
+  Symbols:   180
+  CStrings:  30
 
Symbols:
+ -[DSDiagnosticsSessionAvailability dealloc]
+ -[DSDiagnosticsSessionAvailability openDiagnosticsAppWithCompletionHandler:]
+ -[DSDiagnosticsSessionAvailability openDiagnosticsAppWithCompletionHandler:].cold.1
+ GCC_except_table16
+ ___63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.32
+ ___76-[DSDiagnosticsSessionAvailability openDiagnosticsAppWithCompletionHandler:]_block_invoke
+ ___76-[DSDiagnosticsSessionAvailability openDiagnosticsAppWithCompletionHandler:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.31
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$invalidate
+ _objc_msgSend$openDiagnosticsAppWithCompletionHandler:
+ _objc_msgSendSuper2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- -[DSDiagnosticsSessionAvailability _openDiagnosticsAppWithCompletionHandler:]
- -[DSDiagnosticsSessionAvailability _openDiagnosticsAppWithCompletionHandler:].cold.1
- GCC_except_table14
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- __Block_object_dispose
- ___57-[DSDiagnosticsSessionAvailability enhancedLoggingStatus]_block_invoke
- ___57-[DSDiagnosticsSessionAvailability enhancedLoggingStatus]_block_invoke.28
- ___57-[DSDiagnosticsSessionAvailability enhancedLoggingStatus]_block_invoke.cold.1
- ___63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.38
- ___63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.38.cold.1
- ___77-[DSDiagnosticsSessionAvailability _openDiagnosticsAppWithCompletionHandler:]_block_invoke
- ___77-[DSDiagnosticsSessionAvailability _openDiagnosticsAppWithCompletionHandler:]_block_invoke.cold.1
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32r_e18_v16?0"NSNumber"8lr32l8
- ___block_literal_global.27
- ___block_literal_global.37
- ___block_literal_global.40
- _objc_autoreleaseReturnValue
- _objc_msgSend$_openDiagnosticsAppWithCompletionHandler:
- _objc_msgSend$getEnhancedLoggingStatusWithCompletionHandler:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
CStrings:
+ "-[DSDiagnosticsSessionAvailability openDiagnosticsAppWithCompletionHandler:]"
- "-[DSDiagnosticsSessionAvailability _openDiagnosticsAppWithCompletionHandler:]"
- ".cxx_destruct"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "DSDiagnosticsSessionAvailability"
- "DSDiagnosticsSessionAvailabilityServiceProtocol"
- "T@\"NSXPCConnection\",&,V_connection"
- "Tq,R,N"
- "URLWithString:"
- "_connection"
- "_getSessionStatusWithTicketNumber:timeout:completionHandler:"
- "_openDiagnosticsAppWithCompletionHandler:"
- "_setUpXPCConnectionIfNeeded"
- "activate"
- "connection"
- "dictionaryWithObjects:forKeys:count:"
- "enhancedLoggingStatus"
- "errorWithDomain:code:userInfo:"
- "getEnhancedLoggingStatusWithCompletionHandler:"
- "getSessionStatusWithCompletionHandler:"
- "getSessionStatusWithTicketNumber:completionHandler:"
- "getSessionStatusWithTicketNumber:timeout:completionHandler:"
- "getSessionStatusWithTimeout:completionHandler:"
- "initWithServiceName:"
- "integerValue"
- "interfaceWithProtocol:"
- "numberWithDouble:"
- "openApplication:withOptions:completion:"
- "openApplicationForSessionStatus:completionHandler:"
- "optionsWithDictionary:"
- "q16@0:8"
- "remoteObjectProxyWithErrorHandler:"
- "serviceWithDefaultShellEndpoint"
- "setConnection:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "sharedInstance"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v16@?0@\"NSNumber\"8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSNumber\">16"
- "v32@0:8@16@?24"
- "v32@0:8d16@?24"
- "v32@0:8q16@?24"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24@?32"

```
