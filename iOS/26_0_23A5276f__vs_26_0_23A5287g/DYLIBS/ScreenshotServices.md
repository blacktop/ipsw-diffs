## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x1bcdc
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x23ec
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x1b78
-  __TEXT.__oslogstring: 0xf7f
-  __TEXT.__gcc_except_tab: 0x39c
+408.1.0.0.0
+  __TEXT.__text: 0x1c7a4
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x2404
+  __TEXT.__const: 0x3d8
+  __TEXT.__cstring: 0x1bec
+  __TEXT.__oslogstring: 0x1189
+  __TEXT.__gcc_except_tab: 0x3a0
   __TEXT.__dlopen_cstrs: 0x4ae
   __TEXT.__unwind_info: 0xa70
   __TEXT.__objc_classname: 0x81e
-  __TEXT.__objc_methname: 0x613c
-  __TEXT.__objc_methtype: 0xf4f
-  __TEXT.__objc_stubs: 0x56e0
+  __TEXT.__objc_methname: 0x61da
+  __TEXT.__objc_methtype: 0xfb4
+  __TEXT.__objc_stubs: 0x5740
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0xa78
+  __DATA_CONST.__const: 0xa90
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a80
+  __DATA_CONST.__objc_selrefs: 0x1a90
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x1a40
-  __AUTH_CONST.__objc_const: 0x48d0
+  __AUTH_CONST.__cfstring: 0x1ac0
+  __AUTH_CONST.__objc_const: 0x4900
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x238
+  __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0x6e0
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0xb90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C94BA907-D418-3F0A-B749-0AEAEBE8EB7F
-  Functions: 904
-  Symbols:   3688
-  CStrings:  1894
+  UUID: 66C1A3BE-AD53-36D6-AA66-844BCC50F5F9
+  Functions: 910
+  Symbols:   3705
+  CStrings:  1921
 
Symbols:
+ -[SSEnvironmentDescription screenshotsWindowSafeAreaInsets]
+ -[SSEnvironmentDescription setScreenshotsWindowSafeAreaInsets:]
+ -[SSScreenCapturer _preheatAndTakeScreenshotIfPossibleWithOptionsCollection:presentationOptions:appleInternalOptions:].cold.1
+ -[SSScreenCapturer preheatWithPresentationOptions:].cold.1
+ _MGIsDeviceOneOfType
+ _NSStringFromUIEdgeInsets
+ _OBJC_IVAR_$_SSEnvironmentDescription._screenshotsWindowSafeAreaInsets
+ _UIEdgeInsetsFromString
+ __SSHDRCaptureSupported
+ __SSVisualIntelligenceV2EnabledIgnoringOrientation
+ ___block_descriptor_48_e8_32s40bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls40l8s32l8
+ ___block_literal_global.130
+ _objc_msgSend$potentialEDRHeadroom
+ _objc_msgSend$screenshotsWindow
+ _objc_msgSend$screenshotsWindowSafeAreaInsets
+ _objc_msgSend$setScreenshotsWindowSafeAreaInsets:
- GCC_except_table32
- ___block_descriptor_48_e8_32s40bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8s40l8
- ___block_literal_global.92
- _objc_msgSend$interfaceOrientation
CStrings:
+ "Attempting to activate remote view controller"
+ "Disabled"
+ "Enabled"
+ "PIP %@ due to existing preferences setting"
+ "PIP %@ due to now existing feature preferences"
+ "PresentationModeAutomatic resolved to effectivePresentationMode: %@"
+ "SSEnvironmentDescriptionScreenshotsWindowSafeAreaInsetsKey"
+ "T{UIEdgeInsets=dddd},N,V_screenshotsWindowSafeAreaInsets"
+ "VIV2 disabled due to VK supportedAnalysisTypes"
+ "VIV2 disabled due to feature flag disabled"
+ "VIV2 disabled due to incompatible device idiom"
+ "VIV2 disabled due to landscape orientation"
+ "VIV2 disabled due to locked device"
+ "VIV2 disabled due to not being in SSSProcess"
+ "VIV2 enabled checks passed."
+ "_screenshotsWindowSafeAreaInsets"
+ "effectivePresentationMode: %@"
+ "potentialEDRHeadroom"
+ "screenshots window safe area insets: %@"
+ "screenshotsWindowSafeAreaInsets"
+ "setScreenshotsWindowSafeAreaInsets:"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
+ "{UIEdgeInsets=dddd}16@0:8"
- "interfaceOrientation"

```
