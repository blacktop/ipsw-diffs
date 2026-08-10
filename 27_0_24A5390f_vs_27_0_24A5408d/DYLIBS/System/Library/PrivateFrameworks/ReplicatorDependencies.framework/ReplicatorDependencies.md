## ReplicatorDependencies

> `/System/Library/PrivateFrameworks/ReplicatorDependencies.framework/ReplicatorDependencies`

### Sections with Same Size but Changed Content

- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-173.0.0.0.0
-  __TEXT.__text: 0x29a94
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__const: 0x1e94
-  __TEXT.__swift5_typeref: 0xc00
-  __TEXT.__swift5_reflstr: 0x838
-  __TEXT.__swift5_assocty: 0x1b0
-  __TEXT.__constg_swiftt: 0x1118
-  __TEXT.__swift5_fieldmd: 0xa6c
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x148
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__oslogstring: 0x11a1
-  __TEXT.__cstring: 0x511
-  __TEXT.__swift5_capture: 0x47c
+176.0.0.0.0
+  __TEXT.__text: 0x29c5c
+  __TEXT.__objc_methlist: 0x314
+  __TEXT.__const: 0x1ce4
+  __TEXT.__swift5_typeref: 0xbb8
+  __TEXT.__swift5_reflstr: 0x898
+  __TEXT.__swift5_assocty: 0x180
+  __TEXT.__constg_swiftt: 0x111c
+  __TEXT.__swift5_fieldmd: 0xa5c
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_proto: 0x130
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__oslogstring: 0x11e1
+  __TEXT.__cstring: 0x5e1
+  __TEXT.__swift5_capture: 0x4cc
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x18
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0xb58
+  __TEXT.__unwind_info: 0xb40
   __TEXT.__eh_frame: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2120
-  __AUTH_CONST.__objc_const: 0x1288
-  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0x21e8
+  __AUTH_CONST.__objc_const: 0x12c8
+  __AUTH_CONST.__auth_got: 0xba0
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x38
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x1910
+  __DATA.__data: 0x530
+  __DATA.__bss: 0x1610
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x360
   __DATA_DIRTY.__data: 0x1008
   __DATA_DIRTY.__bss: 0x900
   __DATA_DIRTY.__common: 0x30

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/LocalStatusKit.framework/LocalStatusKit
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1190
-  Symbols:   653
-  CStrings:  114
+  Functions: 1188
+  Symbols:   638
+  CStrings:  119
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ __INSTANCE_METHODS__TtC22ReplicatorDependencies22IDSPairedDeviceMonitor
+ _objc_msgSend$bluetoothIdentifier
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidBecomeInactive
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _NRPairedDeviceRegistryPairedDeviceDidChangeVersionDarwinNotification
- _NRPairedDeviceRegistryWatchDidBecomeActiveDarwinNotification
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- __OBJC_$_INSTANCE_METHODS__TtC22ReplicatorDependencies22IDSPairedDeviceMonitor(ReplicatorDependencies)
- _associated conformance So18NSNotificationNameaSHSCSQ
- _associated conformance So18NSNotificationNameas20_SwiftNewtypeWrapperSCSY
- _associated conformance So18NSNotificationNameas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$deviceForNRDevice:fromIDSDevices:
- _objc_retain_x27
- _symbolic $ss21_ObjectiveCBridgeableP
- _symbolic So8NSStringC
- _symbolic _____ So18NSNotificationNamea
- _type_layout_string So18NSNotificationNamea
CStrings:
+ "Watch paired, will check for pairing change"
+ "Watch unpaired, will check for pairing change"
+ "com.apple.nanoregistry.devicedidpair"
+ "com.apple.nanoregistry.devicedidunpair"
+ "com.apple.nanoregistry.paireddevicedidchangeversion"
+ "com.apple.nanoregistry.watchdidbecomeactive"
- "No NanoRegistry singleton"
```
