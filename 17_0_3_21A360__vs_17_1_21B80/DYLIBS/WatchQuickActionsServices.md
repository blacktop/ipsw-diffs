## WatchQuickActionsServices

> `/System/Library/PrivateFrameworks/WatchQuickActionsServices.framework/WatchQuickActionsServices`

```diff

-137.0.0.0.0
-  __TEXT.__text: 0xa2e8
-  __TEXT.__auth_stubs: 0x590
+141.0.2.0.0
+  __TEXT.__text: 0xa628
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_methlist: 0x6bc
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x4b6
-  __TEXT.__oslogstring: 0x9df
+  __TEXT.__cstring: 0x466
+  __TEXT.__oslogstring: 0xa92
   __TEXT.__gcc_except_tab: 0x170
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x37c
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x1f7
-  __TEXT.__objc_methname: 0x22ba
+  __TEXT.__objc_methname: 0x22d6
   __TEXT.__objc_methtype: 0x7e6
-  __TEXT.__objc_stubs: 0x1b60
+  __TEXT.__objc_stubs: 0x1b80
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1010
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x7e8
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x600
+  __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_const: 0x2c0
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x108

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B92B221D-C63D-3B9B-AAA4-5377B5CFEB78
-  Functions: 232
-  Symbols:   1048
+  UUID: 105CE7A9-0D9D-341C-AE74-26F9F2DD6BEE
+  Functions: 236
+  Symbols:   1056
   CStrings:  639
 
Symbols:
+ -[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:].cold.1
+ -[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:].cold.2
+ _OUTLINED_FUNCTION_2
+ ___58-[WQAOverlayCoordinator _mainQueue_showUIForQuickActions:]_block_invoke.24
+ ___66-[WatchQuickActionsServices _handleAppDidBecomeActiveNotification]_block_invoke.320
+ ___66-[WatchQuickActionsServices registerQuickActions:startupCallback:]_block_invoke.325
+ ___69-[WatchQuickActionsServices _handleAppDidEnterBackgroundNotification]_block_invoke.322
+ ___70-[WQAOverlayCoordinator animateConfirmationForQuickAction:completion:]_block_invoke_3.7
+ ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke.38
+ ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke_2.42
+ ___95-[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:]_block_invoke.330
+ ___block_literal_global.292
+ ___block_literal_global.313
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.419
+ ___block_literal_global.421
+ ___block_literal_global.423
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.440
+ _objc_msgSend$numberWithUnsignedInteger:
- ___58-[WQAOverlayCoordinator _mainQueue_showUIForQuickActions:]_block_invoke.23
- ___66-[WatchQuickActionsServices _handleAppDidBecomeActiveNotification]_block_invoke.326
- ___66-[WatchQuickActionsServices registerQuickActions:startupCallback:]_block_invoke.331
- ___69-[WatchQuickActionsServices _handleAppDidEnterBackgroundNotification]_block_invoke.328
- ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke.37
- ___80-[WQAOverlayCoordinator _mainQueue_showHintsWithPrimaryQuickActions:completion:]_block_invoke_2.41
- ___95-[WatchQuickActionsServices userInterfaceClient:processMessageFromServer:withIdentifier:error:]_block_invoke.336
- ___block_literal_global.298
- ___block_literal_global.319
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.425
- ___block_literal_global.427
- ___block_literal_global.429
- ___block_literal_global.439
- ___block_literal_global.441
- ___block_literal_global.446
- _objc_retain_x4
CStrings:
+ "Localizable-elton"
+ "[%@<%p>] title=%@, hostingView=[%@<%p>], id=\"%@\""
+ "[%@<%p>] title=%@, id=\"%@\""
+ "client error: %@"
+ "numberWithUnsignedInteger:"
+ "process async message: %@, identifier: %@"
+ "process message: %@, identifier: %@"
+ "received performed gesture and action from server: %@"
+ "send async message: %@, identifier: %@"
+ "send message: %@, identifier: %@"
- "Localizable"
- "PrimaryQuickAction"
- "SecondaryQuickAction"
- "UnknownQuickActionType(%li)"
- "[%@<%p>] type=%@, title=%@, hostingView=[%@<%p>], id=\"%@\""
- "[%@<%p>] type=%@, title=%@, id=\"%@\""
- "received performed action from server: %@"

```
