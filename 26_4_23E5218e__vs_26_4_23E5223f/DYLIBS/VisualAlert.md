## VisualAlert

> `/System/Library/PrivateFrameworks/VisualAlert.framework/VisualAlert`

```diff

-3191.23.0.0.0
-  __TEXT.__text: 0xbe70
-  __TEXT.__auth_stubs: 0x540
+3191.24.0.0.0
+  __TEXT.__text: 0xbedc
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x1e0
   __TEXT.__cstring: 0x1aa2
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__unwind_info: 0x300
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_classname: 0x24f
-  __TEXT.__objc_methname: 0x1b77
+  __TEXT.__objc_methname: 0x1b6f
   __TEXT.__objc_methtype: 0x30f
-  __TEXT.__objc_stubs: 0x15e0
-  __DATA_CONST.__got: 0x128
+  __TEXT.__objc_stubs: 0x1600
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x740
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x1460
-  __AUTH_CONST.__objc_const: 0xf78
+  __AUTH_CONST.__objc_const: 0xf58
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libAXSafeCategoryBundle.dylib

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43D8EAA3-88AD-3997-836B-FAFDE4C3519B
+  UUID: 26D2B40F-78B4-3542-B3C4-314B91CD1D3F
   Functions: 208
   Symbols:   909
   CStrings:  711
Symbols:
+ _OBJC_CLASS_$_AVSystemController
+ ___63-[AXVisualAlertManager _startForAlertTypes:cameraTorchManager:]_block_invoke.729
+ ___block_literal_global.902
+ ___block_literal_global.934
+ ___block_literal_global.943
+ ___block_literal_global.946
+ ___block_literal_global.961
+ _objc_msgSend$getSilentMode
- _BKSHIDServicesGetRingerState
- _OBJC_IVAR_$_AXVisualAlertManager._isRingerSwitchSilent
- ___63-[AXVisualAlertManager _startForAlertTypes:cameraTorchManager:]_block_invoke.728
- ___block_literal_global.901
- ___block_literal_global.933
- ___block_literal_global.942
- ___block_literal_global.945
- ___block_literal_global.960
Functions:
~ -[AXVisualAlertManager _startForAlertTypes:cameraTorchManager:] : 3340 -> 3372
~ -[AXVisualAlertManager _beginVisualAlertForType:repeat:skipAutomaticStopOnUserInteraction:bundleId:] : 4492 -> 4516
~ -[AXVisualAlertManager _handleRingerSwitchToggled] : 644 -> 696
CStrings:
+ "getSilentMode"
- "_isRingerSwitchSilent"

```
