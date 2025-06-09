## AccessibilitySettingsLoader

> `/System/Library/AccessibilityBundles/AccessibilitySettingsLoader.bundle/AccessibilitySettingsLoader`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x10b78
-  __TEXT.__auth_stubs: 0x760
+3180.6.1.0.0
+  __TEXT.__text: 0x10c58
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x111c
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x51c
-  __TEXT.__cstring: 0x20c2
-  __TEXT.__oslogstring: 0x64c
+  __TEXT.__cstring: 0x20d7
+  __TEXT.__oslogstring: 0x6a4
   __TEXT.__dlopen_cstrs: 0x6b0
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x740
   __TEXT.__objc_classname: 0x71c
-  __TEXT.__objc_methname: 0x2ee3
+  __TEXT.__objc_methname: 0x2f20
   __TEXT.__objc_methtype: 0xbbf
-  __TEXT.__objc_stubs: 0x1dc0
+  __TEXT.__objc_stubs: 0x1e00
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__const: 0x568
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd10
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x14e0
   __AUTH_CONST.__objc_const: 0x23a8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED29337A-B7C1-3C1F-98B0-88E8C3B0E729
-  Functions: 470
-  Symbols:   1990
-  CStrings:  1108
+  UUID: 3AFEC9DF-2049-34D7-808B-BD0D83A88062
+  Functions: 471
+  Symbols:   1961
+  CStrings:  1112
 
Symbols:
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table41
+ _AXGuestPassManager
+ _AXLogGuestPass
+ _AXProcessIsSpringBoard
+ __AXSGuestPassWasActiveAtSystemAppStartup
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.301
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.302
+ ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.303
+ ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.297
+ ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.297.cold.1
+ ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.297.cold.2
+ ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.297.cold.3
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.296
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.305
+ ___block_literal_global.313
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.343
+ ___block_literal_global.348
+ ___block_literal_global.379
+ ___block_literal_global.384
+ ___block_literal_global.521
+ ___block_literal_global.530
+ ___block_literal_global.851
+ ___block_literal_global.857
+ _objc_msgSend$endGuestPassSessionWithCompletionBlock:
+ _objc_msgSend$localizedDescription
- GCC_except_table15
- GCC_except_table28
- GCC_except_table40
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.298
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.299
- ___47-[AssistiveTouchHelper installKeyboardListener]_block_invoke.300
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.cold.1
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.cold.2
- ___70-[AccessibilitySettingsLoader _initializeDelayedAccessibilitySettings]_block_invoke.cold.3
- ___block_literal_global.276
- ___block_literal_global.287
- ___block_literal_global.288
- ___block_literal_global.292
- ___block_literal_global.293
- ___block_literal_global.302
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.318
- ___block_literal_global.320
- ___block_literal_global.325
- ___block_literal_global.334
- ___block_literal_global.336
- ___block_literal_global.376
- ___block_literal_global.381
- ___block_literal_global.518
- ___block_literal_global.524
- ___block_literal_global.848
- ___block_literal_global.854
- _objc_release_x28
CStrings:
+ "Ended guest pass because SB booted up while in guest pass state. Success: %d, error: %@"
+ "endGuestPassSessionWithCompletionBlock:"
+ "localizedDescription"
+ "v20@?0B8@\"NSError\"12"

```
