## AXActionSheetUIServer

> `/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer`

```diff

-3148.15.26.0.0
+3180.6.1.0.0
   __TEXT.__text: 0x10d8
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_methlist: 0x314

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
+  - /System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2B66F9D-311D-3AEA-8E1B-1F2A32CEE65F
+  UUID: 5D1D4344-7CE7-3261-9EEA-2981962247AF
   Functions: 19
   Symbols:   173
   CStrings:  188
Symbols:
+ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.311
+ ___block_literal_global.314
+ ___block_literal_global.347
- ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.308
- ___block_literal_global.311
- ___block_literal_global.344

```
