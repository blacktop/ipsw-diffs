## exclave_sharedcache

> `AssetData/boot/Firmware/image4/exclavecore_bundle.t8140.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__data`
- `__PDATA.__const`
- `__PDATA.__shared_cache`
- `__PDATA.__auth_ptr`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0x5d65fc
+  __TEXT.__text: 0x5d1840
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x49c21
-  __TEXT.__const: 0x117514
-  __TEXT.__swift5_typeref: 0x11d56
-  __TEXT.__swift5_reflstr: 0xf638
-  __TEXT.__swift5_assocty: 0x74a8
-  __TEXT.__swift5_fieldmd: 0x17db0
-  __TEXT.__constg_swiftt: 0x22bc8
-  __TEXT.__swift5_protos: 0x828
-  __TEXT.__swift5_proto: 0x3620
-  __TEXT.__swift5_types: 0x1e68
+  __TEXT.__cstring: 0x498d1
+  __TEXT.__const: 0x112864
+  __TEXT.__swift5_typeref: 0x11c20
+  __TEXT.__swift5_reflstr: 0xf458
+  __TEXT.__swift5_assocty: 0x7448
+  __TEXT.__swift5_fieldmd: 0x17b10
+  __TEXT.__constg_swiftt: 0x227e8
+  __TEXT.__swift5_protos: 0x818
+  __TEXT.__swift5_proto: 0x35a8
+  __TEXT.__swift5_types: 0x1e2c
   __TEXT.__swift5_types2: 0x44
   __TEXT.__swift5_builtin: 0x1360
   __TEXT.__objc_methtype: 0xb2
-  __TEXT.__swift5_capture: 0xd6c
+  __TEXT.__swift5_capture: 0xd3c
   __TEXT.__swift5_mpenum: 0x314
   __TEXT.__swift_as_entry: 0x974
   __TEXT.__swift_as_ret: 0xae4

   __TEXT.__swift5_replace: 0x0
   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
-  __TEXT.__chain_fixups: 0xb0
-  __TEXT.__eh_frame: 0x327e8
+  __TEXT.__chain_fixups: 0xa8
+  __TEXT.__eh_frame: 0x32530
   __DATA.__TIGHTBEAM_VT: 0x600
   __DATA.__TIGHTBEAM: 0x190
-  __DATA.__data: 0x13e10
-  __DATA.__const: 0x37670
+  __DATA.__data: 0x13ac8
+  __DATA.__const: 0x37098
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x174ed
-  __DATA.__auth_ptr: 0x1f40
+  __DATA.__ENDPOINTS: 0x13957
+  __DATA.__auth_ptr: 0x1ef0
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x268
   __DATA.__MMIOREGS: 0x795

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 23467
+  Functions: 23397
   Symbols:   1
-  CStrings:  6785
+  CStrings:  6768
 
CStrings:
- "$JgExclaveIndicatorController.AccessorySensorRequest"
- "Accessory      = "
- "Copy failed: ExclaveBufferArbiter threw unknown exception: "
- "Copy failed: buffer arbiter got out of bounds for size "
- "ExclaveBufferArbiter/ExclaveBufferArbiter_swift.swift"
- "ExclaveBufferArbiter/client.swift"
- "Invalid ArbitratedBuffer "
- "Missing buffer arbiter for health check enforcement"
- "Requested octopus_accessory_indicator_window exceeds maximum "
- "Unknown buffer type "
- "invalid rawValue for AccessorySensorType: "
- "invalid rawValue for ArbitratedBuffer: "
- "invalid rawValue for DeviceType: "
- "invalid rawValue for ExclaveBufferArbiter.Selector "
- "ms, clamping to max "
- "octopus_accessory_indicator_window"
- "policy-allow-accessory"
```
