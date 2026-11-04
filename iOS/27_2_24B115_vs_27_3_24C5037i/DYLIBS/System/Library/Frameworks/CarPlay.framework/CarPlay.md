## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-552.7.1.0.0
-  __TEXT.__text: 0x6e064
-  __TEXT.__objc_methlist: 0x9b48
+553.9.3.0.0
+  __TEXT.__text: 0x6e368
+  __TEXT.__objc_methlist: 0x9b60
   __TEXT.__const: 0x562
-  __TEXT.__cstring: 0x5be6
-  __TEXT.__oslogstring: 0x3786
+  __TEXT.__cstring: 0x5cb6
+  __TEXT.__oslogstring: 0x37c6
   __TEXT.__gcc_except_tab: 0x934
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x2820
+  __TEXT.__unwind_info: 0x2838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f50
+  __DATA_CONST.__const: 0x1fa0
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4448
+  __DATA_CONST.__objc_selrefs: 0x4460
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__got: 0x878
   __AUTH_CONST.__const: 0xbe8
-  __AUTH_CONST.__cfstring: 0x5840
-  __AUTH_CONST.__objc_const: 0x218a0
+  __AUTH_CONST.__cfstring: 0x5880
+  __AUTH_CONST.__objc_const: 0x218d0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x98
-  __DATA.__objc_ivar: 0xa44
+  __DATA.__objc_ivar: 0xa48
   __DATA.__data: 0x2110
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2698

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3401
-  Symbols:   6397
-  CStrings:  1120
+  Functions: 3408
+  Symbols:   6405
+  CStrings:  1125
 
Symbols:
+ -[CPBarButton isSymbolImage]
+ -[CPBarButton setIsSymbolImage:]
+ -[CPNavigationManager _showRouteSharingPopoverIfNecessary]
+ -[CPTemplateApplicationDashboardScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:statusBarAxis:]
+ -[CPTemplateApplicationInstrumentClusterScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:statusBarAxis:]
+ -[CPTemplateApplicationScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:statusBarAxis:]
+ GCC_except_table108
+ GCC_except_table126
+ _CPAssertIfCurrentProcessHasMisconfiguredEntitlements
+ _OBJC_IVAR_$_CPBarButton._isSymbolImage
+ ___58-[CPNavigationManager _showRouteSharingPopoverIfNecessary]_block_invoke
+ ___58-[CPNavigationManager _showRouteSharingPopoverIfNecessary]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e19_B16?0"CRVehicle"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- -[CPNavigationManager _showRouteSharingPopoverIfNecessaryForVehicle:]
- -[CPTemplateApplicationDashboardScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:]
- -[CPTemplateApplicationInstrumentClusterScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:]
- -[CPTemplateApplicationScene _safeAreaInsetsForInterfaceOrientation:statusBarHidden:]
- GCC_except_table105
- GCC_except_table120
CStrings:
+ "-[CPNavigationManager _showRouteSharingPopoverIfNecessary]_block_invoke_2"
+ "B16@?0@\"CRVehicle\"8"
+ "CPBarButtonIsSymbolImage"
+ "Error fetching vehicles for route sharing popover: %@"
+ "The combination of \"com.apple.developer.carplay-audio\" and \"com.apple.developer.carplay-video\" entitlements is no longer supported."
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "-[CPNavigationManager _showRouteSharingPopoverIfNecessaryForVehicle:]"
```
