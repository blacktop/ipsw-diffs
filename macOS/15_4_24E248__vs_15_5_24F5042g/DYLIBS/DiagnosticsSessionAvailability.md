## DiagnosticsSessionAvailability

> `/System/Library/PrivateFrameworks/DiagnosticsSessionAvailability.framework/Versions/A/DiagnosticsSessionAvailability`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x221c
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x480
-  __TEXT.__oslogstring: 0x164
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x4de
-  __TEXT.__objc_methtype: 0x126
-  __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x58
+820.120.55.501.1
+  __TEXT.__text: 0x2400
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x138
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x594
+  __TEXT.__oslogstring: 0x132
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_classname: 0x54
+  __TEXT.__objc_methname: 0x5e9
+  __TEXT.__objc_methtype: 0x178
+  __TEXT.__objc_stubs: 0x440
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x100
-  __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x108
+  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__objc_const: 0x110
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 64
-  Symbols:   185
-  CStrings:  96
+  Functions: 67
+  Symbols:   192
+  CStrings:  107
 
Symbols:
+ +[DSDiagnosticsSessionAvailability logoutOptionsForAssistant:]
+ -[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]
+ -[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:].cold.1
+ -[DSDiagnosticsSessionAvailability _restartToDiagnosticsModeForAssistant:withCompletionHandler:]
+ -[DSDiagnosticsSessionAvailability _restartToDiagnosticsModeForAssistant:withCompletionHandler:].cold.1
+ -[DSDiagnosticsSessionAvailability _setDiagnosticsMode:forAssistant:withCompletionHandler:]
+ -[DSDiagnosticsSessionAvailability _setDiagnosticsMode:forAssistant:withCompletionHandler:].cold.1
+ -[DSDiagnosticsSessionAvailability restartToDiagnosticsModeForAssistantWithCompletionHandler:]
+ -[DSDiagnosticsSessionAvailability restartToDiagnosticsModeForAssistantWithCompletionHandler:].cold.1
+ GCC_except_table24
+ __63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.63
+ __63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.63.cold.1
+ __79-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]_block_invoke.43
+ __79-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]_block_invoke.47
+ __79-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]_block_invoke.47.cold.1
+ __79-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]_block_invoke.48
+ __91-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:forAssistant:withCompletionHandler:]_block_invoke.cold.1
+ ___79-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]_block_invoke
+ ___91-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:forAssistant:withCompletionHandler:]_block_invoke
+ ___96-[DSDiagnosticsSessionAvailability _restartToDiagnosticsModeForAssistant:withCompletionHandler:]_block_invoke
+ ___96-[DSDiagnosticsSessionAvailability _restartToDiagnosticsModeForAssistant:withCompletionHandler:]_block_invoke_2
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_41_e8_32bs_e25_v16?0^{__CFDictionary=}8l
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8l
+ __block_literal_global.62
+ __block_literal_global.65
+ _dispatch_async
+ _dispatch_get_global_queue
+ _objc_msgSend$_restartForAssistant:withCompletionHandler:
+ _objc_msgSend$_restartToDiagnosticsModeForAssistant:withCompletionHandler:
+ _objc_msgSend$_setDiagnosticsMode:forAssistant:withCompletionHandler:
+ _objc_msgSend$isVoiceOverEnabled
+ _objc_msgSend$logoutOptionsForAssistant:
+ _objc_msgSend$setDiagnosticsModeForAssistant:withVoiceOverEnabled:withCompletionHandler:
- -[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:]
- -[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:].cold.1
- -[DSDiagnosticsSessionAvailability _setDiagnosticsMode:withCompletionHandler:]
- -[DSDiagnosticsSessionAvailability _setDiagnosticsMode:withCompletionHandler:].cold.1
- GCC_except_table22
- GCC_except_table23
- __63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.52
- __63-[DSDiagnosticsSessionAvailability _setUpXPCConnectionIfNeeded]_block_invoke.52.cold.1
- __66-[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:]_block_invoke.40
- __66-[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:]_block_invoke.40.cold.1
- __78-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:withCompletionHandler:]_block_invoke.cold.1
- __82-[DSDiagnosticsSessionAvailability restartToDiagnosticsModeWithCompletionHandler:]_block_invoke_3.cold.1
- ___66-[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:]_block_invoke
- ___78-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:withCompletionHandler:]_block_invoke
- ___82-[DSDiagnosticsSessionAvailability restartToDiagnosticsModeWithCompletionHandler:]_block_invoke
- ___82-[DSDiagnosticsSessionAvailability restartToDiagnosticsModeWithCompletionHandler:]_block_invoke_2
- ___82-[DSDiagnosticsSessionAvailability restartToDiagnosticsModeWithCompletionHandler:]_block_invoke_3
- ___NSDictionary0__struct
- ___block_descriptor_40_e8_32bs_e25_v16?0^{__CFDictionary=}8l
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
- ___copy_helper_block_e8_32s40b
- ___destroy_helper_block_e8_32s40s
- __block_literal_global.51
- __block_literal_global.54
- _objc_msgSend$_restartWithCompletionHandler:
- _objc_msgSend$_setDiagnosticsMode:withCompletionHandler:
CStrings:
+ "-[DSDiagnosticsSessionAvailability _restartForAssistant:withCompletionHandler:]"
+ "-[DSDiagnosticsSessionAvailability _restartToDiagnosticsModeForAssistant:withCompletionHandler:]"
+ "-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:forAssistant:withCompletionHandler:]"
+ "-[DSDiagnosticsSessionAvailability restartToDiagnosticsModeForAssistantWithCompletionHandler:]"
+ "@20@0:8B16"
+ "RespUseIconForBundleID"
+ "_restartForAssistant:withCompletionHandler:"
+ "_restartToDiagnosticsModeForAssistant:withCompletionHandler:"
+ "_setDiagnosticsMode:forAssistant:withCompletionHandler:"
+ "com.apple.DiagnosticsModeAssistant"
+ "isVoiceOverEnabled"
+ "logoutOptionsForAssistant:"
+ "restartToDiagnosticsModeForAssistantWithCompletionHandler:"
+ "setDiagnosticsModeForAssistant:withVoiceOverEnabled:withCompletionHandler:"
+ "v32@0:8B16B20@?24"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "-[DSDiagnosticsSessionAvailability _restartWithCompletionHandler:]"
- "-[DSDiagnosticsSessionAvailability _setDiagnosticsMode:withCompletionHandler:]"
- "Failed to unset Diagnostics Mode boot command: %@"
- "_restartWithCompletionHandler:"
- "_setDiagnosticsMode:withCompletionHandler:"

```
