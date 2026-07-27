## icloudwebd

> `/usr/libexec/icloudwebd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-71.1.0.0.0
-  __TEXT.__text: 0x6f0e4
-  __TEXT.__auth_stubs: 0x1c20
+71.3.0.0.0
+  __TEXT.__text: 0x6f2a8
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_stubs: 0xe40
   __TEXT.__objc_methlist: 0x424
-  __TEXT.__const: 0x7460
-  __TEXT.__oslogstring: 0xd17
+  __TEXT.__const: 0x7450
+  __TEXT.__oslogstring: 0xd47
+  __TEXT.__swift5_typeref: 0x1df9
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1844
-  __TEXT.__swift5_typeref: 0x1df9
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_reflstr: 0x1692
   __TEXT.__swift5_fieldmd: 0x1d98

   __TEXT.__swift_as_ret: 0x1a0
   __TEXT.__swift5_mpenum: 0x104
   __TEXT.__swift5_capture: 0x684
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__unwind_info: 0x1be8
   __TEXT.__eh_frame: 0x3b50
-  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__auth_got: 0xe20
   __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__auth_ptr: 0x5c8
   __DATA_CONST.__const: 0x5df0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2288
-  Symbols:   810
-  CStrings:  670
+  Symbols:   811
+  CStrings:  671
 
Symbols:
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _exit
- _swift_errorInMain
CStrings:
+ "Failed to initialize SkyBridge daemon: %@"
```
