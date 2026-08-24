## ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-624.0.4.0.0
-  __TEXT.__text: 0x7bbd4
-  __TEXT.__auth_stubs: 0x2ab0
+624.0.13.0.0
+  __TEXT.__text: 0x7a6c0
+  __TEXT.__auth_stubs: 0x2a80
   __TEXT.__objc_stubs: 0x25a0
   __TEXT.__objc_methlist: 0xbcc
-  __TEXT.__const: 0x8648
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__objc_methname: 0x29d5
-  __TEXT.__oslogstring: 0x2dab
-  __TEXT.__cstring: 0x1c30
-  __TEXT.__objc_classname: 0x492
-  __TEXT.__objc_methtype: 0x932
-  __TEXT.__swift5_typeref: 0x1810
-  __TEXT.__swift5_fieldmd: 0x1308
-  __TEXT.__constg_swiftt: 0xfe4
-  __TEXT.__swift5_reflstr: 0x6e0
-  __TEXT.__swift5_capture: 0x8e4
-  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__const: 0x8518
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__objc_methname: 0x2a3f
+  __TEXT.__oslogstring: 0x2cbb
+  __TEXT.__cstring: 0x1d00
+  __TEXT.__objc_classname: 0x482
+  __TEXT.__objc_methtype: 0x912
+  __TEXT.__swift5_typeref: 0x1792
+  __TEXT.__swift5_fieldmd: 0x1294
+  __TEXT.__constg_swiftt: 0xf98
+  __TEXT.__swift5_reflstr: 0x6c0
+  __TEXT.__swift5_capture: 0x888
+  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x598
-  __TEXT.__swift5_types: 0x194
-  __TEXT.__swift_as_entry: 0x7c
-  __TEXT.__swift_as_ret: 0x90
-  __TEXT.__swift_as_cont: 0xc0
+  __TEXT.__swift5_types: 0x18c
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_ret: 0x8c
+  __TEXT.__swift_as_cont: 0xb8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_mpenum: 0x3c
-  __TEXT.__unwind_info: 0x1da8
-  __TEXT.__eh_frame: 0x2260
-  __DATA_CONST.__const: 0x4238
-  __DATA_CONST.__cfstring: 0xe40
+  __TEXT.__swift5_mpenum: 0x2c
+  __TEXT.__unwind_info: 0x1d60
+  __TEXT.__eh_frame: 0x21d0
+  __DATA_CONST.__const: 0x4060
+  __DATA_CONST.__cfstring: 0xea0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1568
+  __DATA_CONST.__auth_got: 0x1550
   __DATA_CONST.__got: 0xb68
   __DATA_CONST.__auth_ptr: 0x8e8
-  __DATA.__objc_const: 0x33e0
+  __DATA.__objc_const: 0x3088
   __DATA.__objc_selrefs: 0xb40
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xcb8
-  __DATA.__data: 0x2178
+  __DATA.__data: 0x20a8
   __DATA.__bss: 0xb540
   __DATA.__common: 0x208
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2570
-  Symbols:   1179
-  CStrings:  979
+  Functions: 2532
+  Symbols:   1176
+  CStrings:  983
 
Symbols:
+ _$s10Foundation4DateV3nowACvgZ
- _$sScS12ContinuationV13onTerminationyAB0C0Oyx__GYbcSgvs
- _$sScSMa
- _$sScS_15bufferingPolicy_ScSyxGxm_ScS12ContinuationV09BufferingB0Oyx__GyADyx_GXEtcfC
- _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
CStrings:
+ "%s Apple audio device: %{private}s"
+ "%s Enumeration complete, %ld Apple accessory device(s) found"
+ "%s.%s: %s"
+ "%s.%s: starting loadWarranty for serial %{private}s"
+ "%s: loadWarranty completed with %{private}s"
+ "Clearing cache before check-in (--no-cache)"
+ "Dismissing all follow-up items"
+ "Internal command action result: %s"
+ "Internal command check-in failed: %@"
+ "Internal command check-in succeeded. Actions: %ld"
+ "Triggering immediate check-in with trigger: %s"
+ "com.apple.ndoagent.pairingFilter"
+ "dismissAllFollowUps"
+ "enumeratePairedAccessories()"
+ "getCoverageInfoForSerialNumber: received XPC request for serial %{private}@ with policy %lu"
+ "getCoverageInfoForSerialNumber: warranty fetch completed for serial %{private}@ (data=%@, error=%{private}@)"
+ "hasKnownAppleAccessories()"
+ "maybeCheckInAfterBluetoothPairingDetection(_:)"
+ "maybeCheckInAfterBluetoothPairingDetectionWithHandler:"
+ "ndoagent/NDOAgentSwiftHelpers.swift"
+ "ndoagent/NDODevicePairingFilter.swift"
+ "ndoagent/NDOWarrantyPropertiesLoader.swift"
+ "nil"
+ "non-nil"
+ "none"
- "%s Apple audio device found: %{private}s serial=%{private}s"
- "%s Apple audio device lost: %{private}s"
- "%s Apple audio device unpaired, triggering check-in"
- "%s CBDiscovery activation failed: %s"
- "%s CBDiscovery active"
- "%s Device already known, skipping check-in"
- "%s Device found with no identifier, skipping"
- "%s Device lost with no identifier, skipping"
- "%s Device was not tracked, skipping check-in"
- "%s Event stream ended"
- "%s Initial enumeration complete, %ld Apple audio device(s) known"
- "%s New Apple audio device paired, triggering check-in"
- "%s Still enumerating existing devices, skipping check-in"
- "%s Still enumerating, skipping check-in for lost device"
- "%s.%s DeviceEvent continuation terminated. Invalidating CBDiscovery"
- "%s.%s Found device is not an Apple audio accessory, skipping"
- "%s.%s Lost device is not an Apple audio accessory, skipping"
- "activateDiscovery()"
- "com.apple.ndoagent.pairingMonitor"
- "ndoagent/NDOPairingMonitor.swift"
- "startAccessoryPairingObserverWithCheckInHandler:"
```
