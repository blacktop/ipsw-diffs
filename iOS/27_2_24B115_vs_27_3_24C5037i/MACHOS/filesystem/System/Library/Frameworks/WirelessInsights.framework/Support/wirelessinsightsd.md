## wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-370.0.0.0.0
-  __TEXT.__text: 0x33e410
+376.0.0.0.0
+  __TEXT.__text: 0x33e674
   __TEXT.__auth_stubs: 0x4fd0
-  __TEXT.__objc_stubs: 0xfc80
+  __TEXT.__objc_stubs: 0xfca0
   __TEXT.__init_offsets: 0x2bc
   __TEXT.__objc_methlist: 0x794c
-  __TEXT.__gcc_except_tab: 0x2ad88
+  __TEXT.__gcc_except_tab: 0x2ad94
   __TEXT.__const: 0x18113
   __TEXT.__cstring: 0x1623b
-  __TEXT.__oslogstring: 0x2f7b2
-  __TEXT.__objc_methname: 0x18bac
+  __TEXT.__oslogstring: 0x2f892
+  __TEXT.__objc_methname: 0x18bdc
   __TEXT.__objc_classname: 0x1c4e
-  __TEXT.__objc_methtype: 0x45ea
+  __TEXT.__objc_methtype: 0x45fa
   __TEXT.__swift5_typeref: 0x2662
   __TEXT.__swift5_capture: 0x1d04
   __TEXT.__constg_swiftt: 0x4074

   __DATA_CONST.__got: 0x1408
   __DATA_CONST.__auth_ptr: 0x768
   __DATA.__objc_const: 0x14720
-  __DATA.__objc_selrefs: 0x4598
+  __DATA.__objc_selrefs: 0x45a0
   __DATA.__objc_ivar: 0xa30
   __DATA.__objc_data: 0x5568
   __DATA.__data: 0x67a8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14520
+  Functions: 14521
   Symbols:   2059
-  CStrings:  10475
+  CStrings:  10479
 
CStrings:
+ "376"
+ "376~199"
+ "@28@0:8B16^@20"
+ "PLMNBandwidthManager:Download failed, but no experiment/rollout is active. Therefore, the failure is expected, not sending telemetry"
+ "PLMNBandwidthManager:Failed to retrieve level. OTA active: %{BOOL}d"
+ "Telephony vendor not supported, not initializing"
+ "filePathForActiveTreatmentWithIsOTAActive:error:"
- "370"
- "370~259"
- "PLMNBandwidthManager:Failed to retrieve level"
```
