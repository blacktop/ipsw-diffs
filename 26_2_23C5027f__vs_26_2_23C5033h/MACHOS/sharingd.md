## sharingd

> `/usr/libexec/sharingd`

```diff

-2094.30.26.2.3
-  __TEXT.__text: 0x72608c
+2094.30.32.2.1
+  __TEXT.__text: 0x726938
   __TEXT.__auth_stubs: 0x9cf0
-  __TEXT.__objc_stubs: 0x35160
-  __TEXT.__objc_methlist: 0x1fe5c
-  __TEXT.__cstring: 0x4ae2a
-  __TEXT.__objc_methname: 0x4aea3
+  __TEXT.__objc_stubs: 0x351e0
+  __TEXT.__objc_methlist: 0x1fee4
+  __TEXT.__cstring: 0x4ae6a
+  __TEXT.__objc_methname: 0x4af90
   __TEXT.__objc_classname: 0x2e89
-  __TEXT.__objc_methtype: 0xa5f8
+  __TEXT.__objc_methtype: 0xa650
   __TEXT.__const: 0x1cd10
   __TEXT.__gcc_except_tab: 0x6e4c
-  __TEXT.__oslogstring: 0x3ff23
+  __TEXT.__oslogstring: 0x3fef3
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
-  __TEXT.__swift5_typeref: 0xa828
-  __TEXT.__swift5_fieldmd: 0x9340
-  __TEXT.__constg_swiftt: 0xb678
+  __TEXT.__swift5_typeref: 0xa82e
+  __TEXT.__swift5_fieldmd: 0x9350
+  __TEXT.__constg_swiftt: 0xb6ac
   __TEXT.__swift5_builtin: 0x35c
   __TEXT.__swift5_reflstr: 0x7907
   __TEXT.__swift5_assocty: 0x1690
   __TEXT.__swift5_protos: 0x218
   __TEXT.__swift5_proto: 0x1678
-  __TEXT.__swift5_types: 0x968
+  __TEXT.__swift5_types: 0x96c
   __TEXT.__swift_as_entry: 0xfc8
   __TEXT.__swift5_capture: 0x53e4
   __TEXT.__swift_as_ret: 0xfd8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x16348
-  __TEXT.__eh_frame: 0x288d4
+  __TEXT.__unwind_info: 0x16380
+  __TEXT.__eh_frame: 0x289f4
   __DATA_CONST.__auth_got: 0x4e88
-  __DATA_CONST.__got: 0x3508
-  __DATA_CONST.__auth_ptr: 0x1960
-  __DATA_CONST.__const: 0x22a20
+  __DATA_CONST.__got: 0x3518
+  __DATA_CONST.__auth_ptr: 0x1980
+  __DATA_CONST.__const: 0x22a28
   __DATA_CONST.__cfstring: 0x19d60
-  __DATA_CONST.__objc_classlist: 0xf68
+  __DATA_CONST.__objc_classlist: 0xf70
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x740
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x16f8
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3cc78
-  __DATA.__objc_selrefs: 0x11420
+  __DATA.__objc_const: 0x3ccc8
+  __DATA.__objc_selrefs: 0x11468
   __DATA.__objc_ivar: 0x2b2c
-  __DATA.__objc_data: 0xb6a0
-  __DATA.__data: 0x1a9b0
+  __DATA.__objc_data: 0xb748
+  __DATA.__data: 0x1aa50
   __DATA.__bss: 0x17220
   __DATA.__common: 0xb38
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E01640FA-FA33-33A8-8F7D-70F3C5374E1C
-  Functions: 29109
-  Symbols:   4501
-  CStrings:  32273
+  UUID: 23A7F9EA-D5CC-344E-8DB6-A371C894486C
+  Functions: 29120
+  Symbols:   4502
+  CStrings:  32284
 
Symbols:
+ _$sSo9PDRDeviceC20PairedDeviceRegistryE25localPairingDataStorePathSSSgvg
+ _$sSo9PDRDeviceC20PairedDeviceRegistryE4nameSSSgvg
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeyDeviceNameString
- _NRDevicePropertyIsActive
- _NRDevicePropertyIsPaired
- _NRWatchOSVersionForRemoteDevice
CStrings:
+ "No active IDS device bluetooth identifier"
+ "_TtC16DaemoniOSLibrary22SDPairedDeviceRegistry"
+ "activeDeviceNameString"
+ "activeWatchDescription"
+ "activeWatchDeviceNameString"
+ "activeWatchIsPaired"
+ "activeWatchLocalPairingDataStorePath"
+ "activeWatchName"
+ "activeWatchPairingID"
+ "deviceForBluetoothID:"
+ "getActiveDevice"
+ "pairingIDForBluetoothIdentifier:"
+ "sdContactStore"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
+ "watchNameWithBluetoothIdentifier:"
- "No active NR device"
- "No active NR device for IDS device"
- "Watch supports new LTK model, not aborting."
- "deviceForIDSDevice:"
- "getAllDevices"
- "getAllDevicesWithArchivedDevices"
- "nanoRegistryDeviceForBluetoothIdentifier:"

```
