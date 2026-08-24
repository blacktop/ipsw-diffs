## exclave_sharedcache

> `AssetData/boot/Firmware/image4/exclavecore_bundle.t6050.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
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
-  __TEXT.__text: 0x54f494
+  __TEXT.__text: 0x54a6d8
   __TEXT.__lcxx_override: 0x34c
-  __TEXT.__cstring: 0x44711
-  __TEXT.__const: 0x10f124
-  __TEXT.__swift5_typeref: 0xf610
-  __TEXT.__swift5_reflstr: 0xb668
-  __TEXT.__swift5_assocty: 0x6d90
-  __TEXT.__swift5_fieldmd: 0x1349c
-  __TEXT.__constg_swiftt: 0x1e154
-  __TEXT.__swift5_protos: 0x6e4
-  __TEXT.__swift5_proto: 0x2ec4
-  __TEXT.__swift5_types: 0x19dc
+  __TEXT.__cstring: 0x443c1
+  __TEXT.__const: 0x10a474
+  __TEXT.__swift5_typeref: 0xf4da
+  __TEXT.__swift5_reflstr: 0xb488
+  __TEXT.__swift5_assocty: 0x6d30
+  __TEXT.__swift5_fieldmd: 0x131fc
+  __TEXT.__constg_swiftt: 0x1dd74
+  __TEXT.__swift5_protos: 0x6d4
+  __TEXT.__swift5_proto: 0x2e4c
+  __TEXT.__swift5_types: 0x19a0
   __TEXT.__swift5_types2: 0x40
   __TEXT.__swift5_builtin: 0x10e0
   __TEXT.__objc_methtype: 0xb2
-  __TEXT.__swift5_capture: 0xc6c
+  __TEXT.__swift5_capture: 0xc3c
   __TEXT.__swift5_mpenum: 0x238
   __TEXT.__swift_as_entry: 0x96c
   __TEXT.__swift_as_ret: 0xae0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xa8
-  __TEXT.__eh_frame: 0x2e084
+  __TEXT.__eh_frame: 0x2ddcc
   __DATA.__TIGHTBEAM_VT: 0x540
   __DATA.__TIGHTBEAM: 0x168
-  __DATA.__data: 0x10250
-  __DATA.__const: 0x304b0
+  __DATA.__data: 0xff08
+  __DATA.__const: 0x2fed8
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x174ed
-  __DATA.__auth_ptr: 0x1830
+  __DATA.__ENDPOINTS: 0x13957
+  __DATA.__auth_ptr: 0x17e0
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x268
   __DATA.__MMIOREGS: 0x795

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 21503
+  Functions: 21433
   Symbols:   1
-  CStrings:  6302
+  CStrings:  6285
 
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
