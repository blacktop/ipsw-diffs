## CarPlayServices

> `/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices`

```diff

-309.5.6.0.0
-  __TEXT.__text: 0xb504
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xc10
+332.13.2.0.0
+  __TEXT.__text: 0xb810
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0xc20
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xaa2
+  __TEXT.__cstring: 0xa54
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__oslogstring: 0x8ff
+  __TEXT.__oslogstring: 0x948
   __TEXT.__unwind_info: 0x3e4
   __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methname: 0x28c3
-  __TEXT.__objc_methtype: 0x668
-  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_methname: 0x294d
+  __TEXT.__objc_methtype: 0x6ab
+  __TEXT.__objc_stubs: 0x1b40
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x678
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3e80
-  __DATA_CONST.__objc_selrefs: 0x8c0
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0xa40
+  __DATA_CONST.__objc_const: 0x3ea0
+  __DATA_CONST.__objc_selrefs: 0x8d8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x6f0
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x140
-  __DATA.__objc_superrefs: 0x60
   __DATA.__objc_ivar: 0x108
   __DATA.__data: 0x5c8
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06917DF6-26FA-33AB-8856-BBF2E4FA24C7
-  Functions: 344
-  Symbols:   1476
-  CStrings:  772
+  UUID: BF8A86DA-B668-345A-BAFE-333D83F7BD28
+  Functions: 347
+  Symbols:   1481
+  CStrings:  764
 
Symbols:
+ -[CRSAppHistoryController fetchDockAppForCategory:completion:]
+ -[CRSAppHistoryService fetchDockAppInCategory:completion:]
+ GCC_except_table27
+ _CRSVehicleSettingsIdentifier
+ _OBJC_CLASS_$_CRFeatureAvailability
+ ___31-[CRSAppHistoryController init]_block_invoke.28
+ ___31-[CRSAppHistoryController init]_block_invoke.31
+ ___58-[CRSAppHistoryService fetchDockAppInCategory:completion:]_block_invoke
+ ___62-[CRSAppHistoryController fetchDockAppForCategory:completion:]_block_invoke
+ ___71-[CRSInCallAssertionService listener:didReceiveConnection:withContext:]_block_invoke.71
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_literal_global.30
+ ___block_literal_global.33
+ _objc_msgSend$fetchDockAppInCategory:completion:
+ _objc_msgSend$supportedAirPlayFeaturesForVehicleIdentifier:
- GCC_except_table25
- _CRHardwareSupportedFeatures
- _OBJC_CLASS_$_NSConstantArray
- ___31-[CRSAppHistoryController init]_block_invoke.70
- ___31-[CRSAppHistoryController init]_block_invoke.73
- ___47+[CRSAppHistoryController availableFeatureKeys]_block_invoke
- ___71-[CRSInCallAssertionService listener:didReceiveConnection:withContext:]_block_invoke.70
- ___block_literal_global.72
- ___block_literal_global.75
- ___block_literal_global.81
- __unnamed_array_storage
- _availableFeatureKeys.__featureKeys
- _availableFeatureKeys.onceToken
CStrings:
+ "Received request for dock app in category %@."
+ "T@\"NSString\",?,R,C"
+ "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "available feature keys: %@"
+ "com.apple.AutoSettings"
+ "fetchDockAppForCategory:completion:"
+ "fetchDockAppInCategory:completion:"
+ "supportedAirPlayFeaturesForVehicleIdentifier:"
+ "v32@0:8Q16@?24"
- "altScreen"
- "cornerMasks"
- "enhancedSiri"
- "focusTransfer"
- "h.264Level5.1"
- "hevc"
- "mainBuffered"
- "uiContext"
- "viewAreas"

```
