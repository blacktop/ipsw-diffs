## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-300.0.5.0.0
-  __TEXT.__text: 0x24744c
-  __TEXT.__auth_stubs: 0x3200
+300.0.6.0.0
+  __TEXT.__text: 0x244ca8
+  __TEXT.__auth_stubs: 0x3220
   __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x293c
+  __TEXT.__objc_methlist: 0x2944
   __TEXT.__objc_classname: 0x48b
   __TEXT.__objc_methname: 0x6ca0
   __TEXT.__objc_methtype: 0x2d4a
-  __TEXT.__const: 0x26e08
-  __TEXT.__cstring: 0x15d86
-  __TEXT.__swift5_typeref: 0x1315e
-  __TEXT.__constg_swiftt: 0x100e4
-  __TEXT.__swift5_reflstr: 0xa1e3
-  __TEXT.__swift5_fieldmd: 0xac78
+  __TEXT.__const: 0x26da8
+  __TEXT.__cstring: 0x15866
+  __TEXT.__swift5_typeref: 0x130fe
+  __TEXT.__constg_swiftt: 0x100ac
+  __TEXT.__swift5_reflstr: 0xa1a3
+  __TEXT.__swift5_fieldmd: 0xac6c
   __TEXT.__swift5_builtin: 0x604
-  __TEXT.__swift5_assocty: 0xfc0
-  __TEXT.__swift5_capture: 0x37c8
-  __TEXT.__oslogstring: 0x1db8
-  __TEXT.__swift5_proto: 0x2268
+  __TEXT.__swift5_assocty: 0xfa8
+  __TEXT.__swift5_capture: 0x3798
+  __TEXT.__oslogstring: 0x2298
+  __TEXT.__swift5_proto: 0x2260
   __TEXT.__swift5_types: 0xa70
   __TEXT.__swift5_protos: 0x318
   __TEXT.__swift5_mpenum: 0x174
   __TEXT.__swift_as_entry: 0xc0
   __TEXT.__swift_as_ret: 0xc0
-  __TEXT.__unwind_info: 0x78a0
-  __TEXT.__eh_frame: 0x7450
-  __DATA_CONST.__auth_got: 0x1908
+  __TEXT.__unwind_info: 0x76f8
+  __TEXT.__eh_frame: 0x7390
+  __DATA_CONST.__auth_got: 0x1918
   __DATA_CONST.__got: 0xe38
-  __DATA_CONST.__auth_ptr: 0x1be8
-  __DATA_CONST.__const: 0x1a680
+  __DATA_CONST.__auth_ptr: 0x1bf0
+  __DATA_CONST.__const: 0x1a5d0
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x18430
+  __DATA.__objc_const: 0x18410
   __DATA.__objc_selrefs: 0x1cf8
   __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x2f90
-  __DATA.__data: 0x19070
-  __DATA.__bss: 0x3a630
-  __DATA.__common: 0x800
+  __DATA.__objc_data: 0x2f50
+  __DATA.__data: 0x19010
+  __DATA.__bss: 0x3a5a0
+  __DATA.__common: 0x820
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C30CD7B1-3B6D-3981-A4B7-A6EE35AD2E71
-  Functions: 11568
-  Symbols:   1539
+  UUID: 003EE6EB-DA94-362F-8F3D-68313017CFFB
+  Functions: 11552
+  Symbols:   1542
   CStrings:  4197
 
Symbols:
+ _$s2os6LoggerVMn
+ _$sScP4highScPvgZ
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
CStrings:
+ "### %s already initiated token sync?"
+ "### Device found in cache, replacing...\n  Identity: %s\n  HandoffDevice:%s"
+ "### Error sharing token %@"
+ "### Failed to exchange tokens with %s: %@"
+ "### Failed to replace device: %@"
+ "### Failed to update device, replacing... error=%@"
+ "%s %@"
+ "%s: identity=%s"
+ "%s: rpCLDevice=%@"
+ "%s: type=%s, rpCLDevice=%@"
+ "After activation FOUND %ld rpCLDevices"
+ "Attaching CBDevice: %@"
+ "BT devices changed (throttled)"
+ "DONE exchanging tokens with %s"
+ "FOUND %s"
+ "Invalidating"
+ "LOST %s"
+ "No existing HandoffDevice for %@"
+ "No rapportDeviceType?"
+ "Received peer token from %s"
+ "Retry interval for %s: %s"
+ "START exchanging ranging tokens with %s"
+ "UPDATED %s"
+ "Unsupported rapport error code %d"
+ "createHandoffDevice(with:)"
+ "nonRPCLDeviceIdentityFound(_:)"
+ "reactivationRetrier"
+ "rpCLDeviceFound(_:)"
+ "rpCLDeviceLost(_:)"
- "\n  HandoffDevice:"
- " already initiated token sync?"
- " devices out of "
- "### Device found in cache, replacing...\n  Identity: "
- "### ERROR: 'nextIdentity' is nil"
- "### Error sharing token "
- "### Failed to combine identities: "
- "### Failed to exchange tokens with "
- "### No device found for identity: "
- "$__lazy_storage_$_reactivationRetrier"
- "(Throttled) BT devices changed"
- "? Existing identity found"
- "After activation FOUND MERGED ("
- "After activation FOUND RAW ("
- "Cached identity updated "
- "DONE exchanging tokens with "
- "No existing HandoffDevice for "
- "RAPPORT DEVICE FOUND "
- "Received peer token from "
- "Retry interval for "
- "START exchanging ranging tokens with "
- "Unsupported rapport error code "
- "identityStorage"
- "invalidateHandoffDevice(_:): device="
- "lockedReplacement(transform:)"
- "nonRPCLDeviceIdentityFound(_:): identity="
- "rpCLDeviceFound(_:): type="
- "rpCLDeviceLost(_:): rpCLDevice="
- "rpIdentified(_:): identity="

```
