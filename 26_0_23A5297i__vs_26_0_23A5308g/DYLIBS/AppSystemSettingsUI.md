## AppSystemSettingsUI

> `/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI`

```diff

-19.0.0.0.0
-  __TEXT.__text: 0x2a348
+20.0.0.0.0
+  __TEXT.__text: 0x2a3c8
   __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_methlist: 0xf14
+  __TEXT.__objc_methlist: 0xf1c
   __TEXT.__const: 0x1078
   __TEXT.__gcc_except_tab: 0x348
-  __TEXT.__cstring: 0x29fc
+  __TEXT.__cstring: 0x2a0c
   __TEXT.__oslogstring: 0x886
   __TEXT.__ustring: 0x114
   __TEXT.__constg_swiftt: 0x5a0

   __TEXT.__unwind_info: 0x980
   __TEXT.__eh_frame: 0x250
   __TEXT.__objc_classname: 0x1d7
-  __TEXT.__objc_methname: 0x3b26
+  __TEXT.__objc_methname: 0x3b5b
   __TEXT.__objc_methtype: 0x1188
-  __TEXT.__objc_stubs: 0x2920
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x4a0
+  __TEXT.__objc_stubs: 0x2960
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0x4a8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x1088
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xb30
   __AUTH_CONST.__const: 0xa70
-  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__cfstring: 0x1580
   __AUTH_CONST.__objc_const: 0x1918
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8C31EC91-1B4B-357A-A2CC-39E35F5B3CB0
-  Functions: 811
-  Symbols:   1759
-  CStrings:  1225
+  UUID: B43FB757-F13E-378E-8061-0C22A801FF9C
+  Functions: 812
+  Symbols:   1764
+  CStrings:  1230
 
Symbols:
+ -[PSAccessoriesListController deviceSupportsMultitech:]
+ ___47-[PSAccessoriesListController refreshDADevices]_block_invoke.67
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_AppSystemSettingsUI
+ _objc_msgSend$bluetoothIdentifier
+ _objc_msgSend$deviceSupportsMultitech:
+ _objc_msgSend$wifiAwareDevicePairingID
- _PSTableCellSubtitleTextKey
- ___47-[PSAccessoriesListController refreshDADevices]_block_invoke.62
- _objc_msgSend$bluetoothOTAName
Functions:
~ -[PSAccessoriesListController specifierForDevice:] : 380 -> 372
+ -[PSAccessoriesListController deviceSupportsMultitech:]
CStrings:
+ "bluetoothIdentifier"
+ "com.apple.graphic-icon.wifi"
+ "deviceSupportsMultitech:"
+ "wifiAwareDevicePairingID"
- "bluetoothOTAName"

```
