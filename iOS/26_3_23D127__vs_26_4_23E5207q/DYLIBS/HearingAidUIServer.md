## HearingAidUIServer

> `/System/Library/AccessibilityBundles/HearingAidUIServer.axuiservice/HearingAidUIServer`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x1c58
-  __TEXT.__auth_stubs: 0x1d0
+3191.19.0.0.0
+  __TEXT.__text: 0x1e58
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_methlist: 0x3cc
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0x18e
   __TEXT.__gcc_except_tab: 0x24
   __TEXT.__dlopen_cstrs: 0x69
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methname: 0x1067
   __TEXT.__objc_methtype: 0x46c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x610

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41C46F52-B8F7-3BB7-A6FD-016197C26703
+  UUID: 19DE29A0-354A-38C0-9284-832CC5BAC684
   Functions: 42
-  Symbols:   316
+  Symbols:   319
   CStrings:  261
 
Symbols:
+ ___block_literal_global.352
+ ___block_literal_global.371
+ _objc_autorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x23
- ___block_literal_global.313
- ___block_literal_global.332
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
Functions:
~ -[AXHearingAidDisplayController dismissWithCompletion:] : 248 -> 272
~ -[AXHearingAidDisplayController didMoveToParentViewController:] : 336 -> 356
~ ___63-[AXHearingAidDisplayController didMoveToParentViewController:]_block_invoke : 112 -> 120
~ -[AXHearingAidDisplayController setModuleUIController:] : 20 -> 80
~ -[AXUltronStatusProviderViewController viewDidLoad] : 2024 -> 2184
~ -[AXUltronStatusProviderViewController updateDisplay:confidence:] : 288 -> 284
~ ___65-[AXUltronStatusProviderViewController updateDisplay:confidence:]_block_invoke : 232 -> 236
~ -[HearingAidUIServer setNewDisplayController:] : 484 -> 516
~ -[HearingAidUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:] : 1188 -> 1240
~ ___83-[HearingAidUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke : 84 -> 88
~ ___83-[HearingAidUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke_3 : 200 -> 212
~ -[HearingAidUIServer desiredWindowLevelForContentViewController:userInteractionEnabled:] : 100 -> 104
~ -[HearingAidUIServer createUserNotificationRequest:] : 368 -> 400
~ -[HearingAidUIServer setDisplayController:] : 12 -> 64
~ -[HearingAidUIServer setDisableSystemGestureAssertion:] : 12 -> 64

```
