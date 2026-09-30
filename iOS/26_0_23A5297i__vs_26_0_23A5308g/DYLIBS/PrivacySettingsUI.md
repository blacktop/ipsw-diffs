## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1236.0.0.0.0
-  __TEXT.__text: 0x63fa0
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x413c
+1237.0.0.0.0
+  __TEXT.__text: 0x64044
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_methlist: 0x4144
   __TEXT.__const: 0x2e4
   __TEXT.__gcc_except_tab: 0x13b0
-  __TEXT.__cstring: 0x829a
+  __TEXT.__cstring: 0x82ba
   __TEXT.__oslogstring: 0x2c10
   __TEXT.__dlopen_cstrs: 0xf41
   __TEXT.__swift5_typeref: 0x188

   __TEXT.__unwind_info: 0x1740
   __TEXT.__eh_frame: 0x638
   __TEXT.__objc_classname: 0x99e
-  __TEXT.__objc_methname: 0xd36b
+  __TEXT.__objc_methname: 0xd3af
   __TEXT.__objc_methtype: 0x107d
-  __TEXT.__objc_stubs: 0xa240
+  __TEXT.__objc_stubs: 0xa2a0
   __DATA_CONST.__got: 0x968
   __DATA_CONST.__const: 0x1aa0
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3228
+  __DATA_CONST.__objc_selrefs: 0x3240
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__cfstring: 0x6e60
+  __AUTH_CONST.__cfstring: 0x6e80
   __AUTH_CONST.__objc_const: 0x6428
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 208BD920-0BFC-32F7-9A1B-4B3AF77AEB97
-  Functions: 2016
-  Symbols:   7040
-  CStrings:  4573
+  UUID: 7673B4A1-ABDE-39BD-A4E0-3310E973A663
+  Functions: 2017
+  Symbols:   7044
+  CStrings:  4580
 
Symbols:
+ -[PUIAccessoriesAppSpecificControllerViewController deviceSupportsMultitech:]
+ ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.452
+ ___69-[PUIAccessoriesAppSpecificControllerViewController refreshDADevices]_block_invoke.28
+ ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.915
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1001
+ ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.1002
+ ___block_literal_global.385
+ ___block_literal_global.984
+ _objc_msgSend$bluetoothIdentifier
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$deviceSupportsMultitech:
+ _objc_msgSend$wifiAwareDevicePairingID
- _PSSiriImage
- ___63-[DiagnosticDataController _loadDiagnosticsDataWithCompletion:]_block_invoke.449
- ___69-[PUIAccessoriesAppSpecificControllerViewController refreshDADevices]_block_invoke.20
- ___73-[PUIProblemReportingController shouldShowIdentityVerificationSpecifiers]_block_invoke.912
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.998
- ___77-[PUIProblemReportingController updateHealthRecordsPreferenceForSpecifierID:]_block_invoke.999
- ___block_literal_global.283
- ___block_literal_global.388
- ___block_literal_global.981
- _objc_msgSend$bluetoothOTAName
Functions:
~ -[PUIAccessoriesAppSpecificControllerViewController specifierForDevice:] : 380 -> 372
+ -[PUIAccessoriesAppSpecificControllerViewController deviceSupportsMultitech:]
~ -[PUILocationServicesAuthLevelCell getLazyIcon] : 672 -> 632
~ -[PUILocationServicesListController locationDetailSpecifiersWithDetailsMatching:] : 2828 -> 2904
CStrings:
+ "?"
+ "bluetoothIdentifier"
+ "bundleWithURL:"
+ "com.apple.graphic-icon.wifi"
+ "deviceSupportsMultitech:"
+ "wifiAwareDevicePairingID"
- "bluetoothOTAName"

```
