## remoteappintentsd

> `/usr/libexec/remoteappintentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-41.0.45.0.0
-  __TEXT.__text: 0x73a58
+41.0.50.0.0
+  __TEXT.__text: 0x744f4
   __TEXT.__auth_stubs: 0x2ac0
   __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x3b4

   __TEXT.__swift5_fieldmd: 0x9ec
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x8a4
-  __TEXT.__oslogstring: 0x1bca
+  __TEXT.__oslogstring: 0x1d8a
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0xe0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__auth_got: 0x1568
-  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__auth_ptr: 0xaf0
   __DATA.__objc_const: 0x1628
   __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_data: 0x4a0
-  __DATA.__data: 0x2278
+  __DATA.__data: 0x2258
   __DATA.__bss: 0xe00
   __DATA.__common: 0x390
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2654
-  Symbols:   1100
-  CStrings:  562
+  Functions: 2663
+  Symbols:   1101
+  CStrings:  566
 
Symbols:
+ _$s18AppIntentsServices0bC0O10DeviceTypeO7unknownyA2EmFWC
CStrings:
+ "%sAllowing request: peer device type is unknown (model: %{public}s) but no MDM restrictions are active."
+ "%sDenying request: peer device type is unknown (model: %{public}s) and home device pairing is disabled by MDM."
+ "%sDenying request: peer device type is unknown (model: %{public}s) and paired watch connection is disabled by MDM."
+ "%sResolved peer device type %{public}s from Networking device model \"%{public}s\"."
```
