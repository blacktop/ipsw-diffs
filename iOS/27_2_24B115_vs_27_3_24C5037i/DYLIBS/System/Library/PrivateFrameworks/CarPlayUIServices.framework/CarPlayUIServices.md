## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-591.6.1.0.0
-  __TEXT.__text: 0x37d4c
-  __TEXT.__objc_methlist: 0x3bec
+592.7.0.0.0
+  __TEXT.__text: 0x383ec
+  __TEXT.__objc_methlist: 0x3c3c
   __TEXT.__const: 0xfa4
-  __TEXT.__oslogstring: 0x1a14
-  __TEXT.__cstring: 0x1b03
-  __TEXT.__gcc_except_tab: 0x4a4
+  __TEXT.__oslogstring: 0x1a64
+  __TEXT.__cstring: 0x1b33
+  __TEXT.__gcc_except_tab: 0x4b4
   __TEXT.__swift5_typeref: 0x6b6
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__constg_swiftt: 0x840

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1768
+  __TEXT.__unwind_info: 0x1790
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c90
+  __DATA_CONST.__objc_selrefs: 0x1cc0
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x720
   __AUTH_CONST.__const: 0x1280
-  __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x12968
+  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__objc_const: 0x129b8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__auth_got: 0x978
   __AUTH.__objc_data: 0x670
   __AUTH.__data: 0x668
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_ivar: 0x39c
   __DATA.__data: 0x1828
   __DATA.__common: 0x140
   __DATA_DIRTY.__objc_data: 0x1f80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1742
-  Symbols:   3053
-  CStrings:  399
+  Functions: 1751
+  Symbols:   3067
+  CStrings:  400
 
Symbols:
+ -[CRSUICAPackageView _observeInterfaceStyle]
+ -[CRSUICAPackageView setLightModeState:darkModeState:animated:]
+ -[CRSUIClusterThemeManager _getLightModeState:darkModeState:forThemeWallpaper:]
+ -[CRSUIClusterThemeManager _themeWallpaperForWallpaper:]
+ -[CRSUIClusterThemeManager getPackageURL:lightModeState:darkModeState:forWallpaper:]
+ -[CRSUIStatusBarStyleAssertion initForAutomakerPunchthroughWithInterfaceStyle:punchthroughHidesDockBackground:]
+ -[CRSUIStatusBarStyleAssertion punchthroughHidesDockBackground]
+ -[CRSUIStatusBarStyleAssertion setPunchthroughHidesDockBackground:]
+ -[CRSUIStatusBarStyleAssertionData punchthroughHidesDockBackground]
+ -[CRSUIStatusBarStyleAssertionData setPunchthroughHidesDockBackground:]
+ -[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithInterfaceStyle:punchthroughHidesDockBackground:fenceHandle:animationSettings:]
+ -[CRSUIStatusBarStyleService punchthroughHidesDockBackground]
+ _CRSUIBannerIncomingCallProviderIdentifierKey
+ _OBJC_IVAR_$_CRSUICAPackageView._observesInterfaceStyle
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertion._punchthroughHidesDockBackground
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertionData._punchthroughHidesDockBackground
+ ___148-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithInterfaceStyle:punchthroughHidesDockBackground:fenceHandle:animationSettings:]_block_invoke
+ ___148-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithInterfaceStyle:punchthroughHidesDockBackground:fenceHandle:animationSettings:]_block_invoke_2
+ ___61-[CRSUIStatusBarStyleService punchthroughHidesDockBackground]_block_invoke
+ ___63-[CRSUICAPackageView setLightModeState:darkModeState:animated:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e37_"NSString"16?0"UITraitCollection"8ls32l8s40l8
+ _objc_autorelease
- -[CRSUIStatusBarStyleAssertion initForAutomakerPunchthrough]
- -[CRSUIStatusBarStyleAssertionData isAutomakerPunchthrough]
- -[CRSUIStatusBarStyleAssertionData setAutomakerPunchthrough:]
- -[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]
- -[CRSUIStatusBarStyleService isAutomakerPunchthrough]
- _OBJC_IVAR_$_CRSUIStatusBarStyleAssertionData._automakerPunchthrough
- ___101-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]_block_invoke
- ___101-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]_block_invoke_2
CStrings:
+ "!Q"
+ "Acquiring assertion for automaker punch through, interface style: %d, hides dock background: %d"
+ "CRSUIBannerIncomingCallProviderIdentifierKey"
+ "Received automaker punchthrough override request! Style: %@, hides dock background: %@"
- "!A"
- "Acquiring assertion for automaker punch through"
- "Received automaker punchthrough override request!"
```
