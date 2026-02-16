## AXActionSheetUIServer

> `/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x10d8
+3191.19.0.0.0
+  __TEXT.__text: 0x11c0
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_methlist: 0x31c
   __TEXT.__const: 0x30

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23CA34EE-8F7F-3898-8086-2492B6987992
+  UUID: 7CCADB35-2130-3568-B8CE-515C19A8860E
   Functions: 19
   Symbols:   173
   CStrings:  189
Symbols:
+ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.362
+ ___block_literal_global.365
+ ___block_literal_global.398
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x25
- ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.323
- ___block_literal_global.326
- ___block_literal_global.359
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x8
Functions:
~ -[AXActionSheetUIServer _informClientOfChoice:] : 592 -> 620
~ ___47-[AXActionSheetUIServer _informClientOfChoice:]_block_invoke : 88 -> 92
~ -[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:] : 2084 -> 2176
~ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke : 272 -> 284
~ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.323 -> ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.362 : 152 -> 160
~ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke_4 : 124 -> 128
~ -[AXActionSheetUIServer desiredWindowLevelForContentViewController:userInteractionEnabled:] : 100 -> 104
~ -[AXActionSheetUIServer alertWithIdentifierDidDisappear:] : 196 -> 200
~ -[AXActionSheetUIServer alertWithIdentifierWasActivated:] : 396 -> 420
~ -[AXActionSheetUIServer setAlertIdentifier:] : 12 -> 64

```
