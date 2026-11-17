## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.60.14.0.1
-  __TEXT.__text: 0x600680
+1777.60.18.0.1
+  __TEXT.__text: 0x6067d8
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0x51791
-  __TEXT.__const: 0x124e94
-  __TEXT.__swift5_typeref: 0x14564
-  __TEXT.__swift5_reflstr: 0x135b8
-  __TEXT.__swift5_assocty: 0x7d40
-  __TEXT.__swift5_fieldmd: 0x1cf64
-  __TEXT.__constg_swiftt: 0x28bfc
-  __TEXT.__swift5_protos: 0x998
-  __TEXT.__swift5_proto: 0x3ebc
-  __TEXT.__swift5_types: 0x2534
-  __TEXT.__swift5_types2: 0x64
-  __TEXT.__swift5_builtin: 0x15b8
+  __TEXT.__cstring: 0x51cf1
+  __TEXT.__const: 0x125c94
+  __TEXT.__swift5_typeref: 0x14788
+  __TEXT.__swift5_reflstr: 0x137e8
+  __TEXT.__swift5_assocty: 0x8118
+  __TEXT.__swift5_fieldmd: 0x1d39c
+  __TEXT.__constg_swiftt: 0x29060
+  __TEXT.__swift5_protos: 0x9a0
+  __TEXT.__swift5_proto: 0x3fd0
+  __TEXT.__swift5_types: 0x2588
+  __TEXT.__swift5_types2: 0x78
+  __TEXT.__swift5_builtin: 0x161c
   __TEXT.__swift5_capture: 0x1068
   __TEXT.__objc_methtype: 0x111
   __TEXT.__swift5_mpenum: 0x3b8
   __TEXT.__swift_as_entry: 0x9bc
   __TEXT.__swift_as_ret: 0xb34
   __TEXT.__swift_as_cont: 0x1234
-  __TEXT.__oslogstring: 0xf3
+  __TEXT.__oslogstring: 0xd3
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0xb8
-  __TEXT.__eh_frame: 0x35fc0
+  __TEXT.__eh_frame: 0x36260
   __DATA.__TIGHTBEAM_VT: 0x8a0
   __DATA.__TIGHTBEAM: 0x238
-  __DATA.__const: 0x3ea98
-  __DATA.__data: 0x19238
+  __DATA.__const: 0x3f718
+  __DATA.__data: 0x19388
   __DATA.__mod_init_func: 0x40
-  __DATA.__ENDPOINTS: 0x1b291
-  __DATA.__auth_ptr: 0x24a8
+  __DATA.__ENDPOINTS: 0x1b6ad
+  __DATA.__auth_ptr: 0x2558
   __DATA.__DEVICETREE: 0x18
   __DATA.__shared_cache: 0x380
   __DATA.__MMIOREGS: 0x795

   __DATA.__mod_term_func: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x30
-  __DATA.__common: 0x71a
+  __DATA.__common: 0x73a
   __PDATA.__auth_ptr: 0x280
   __PDATA.__const: 0x6910
   __PDATA.__objc_imageinfo: 0x8

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 657
   Symbols:   1
-  CStrings:  7488
+  CStrings:  7515
 
CStrings:
+ " no sample from this sensor, still within first integration period, skipping..."
+ "AtomicLoadOrdering("
+ "AtomicStoreOrdering("
+ "AtomicUpdateOrdering("
+ "BUG IN XNU: concurrent calls to LogServer.getLogs()"
+ "BUG IN XNU: concurrent calls to RedactedLogServer.getLogs()"
+ "Builtin.FixedArray of %zd elements with stride %zu is too large to be representable\n"
+ "ExclaveIndicatorControllerComponent/ExclavesPlatform.swift"
+ "Failed to read GLTB"
+ "OSLogServerComponent/RedactedLogServer.swift"
+ "Siri activated mic: microphone allowed for longer than "
+ "Siri activated mic: no voice trigger service, microphone not allowed"
+ "Siri activated mic: recent voice trigger event detected"
+ "SiriActivatedMic = "
+ "Tried to build a Builtin.FixedArray without metadata for the element type"
+ "WordPair(first: "
+ "[StrictMode] .rampUp -> .steady"
+ "[StrictMode] Can't use pre-wake MIB. Reporting failure."
+ "[StrictMode] Disabling (enabledTs="
+ "[StrictMode] Enabling (ts="
+ "[StrictMode] Healthy. Disabling. MIB="
+ "acquiringAndReleasing"
+ "invalid rawValue for EXDisplayPipeSwapAnimationKind: "
+ "octopus_siri_activated_mic"
+ "policy-siri-activated-mic"
+ "sequentiallyConsistent"
+ "type bound to a value generic parameter"
+ "type where a Builtin.FixedArray count is required"
+ "unresolved Builtin.FixedArray element type"
- "MMIO read: addr=%p value=0x%llx"
- "[EIC] MMIO read: addr=%p value=0x%llx\n"
```
