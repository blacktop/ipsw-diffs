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
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-71.1.0.0.0
-  __TEXT.__text: 0x6971c
-  __TEXT.__auth_stubs: 0x1f10
+71.3.0.0.0
+  __TEXT.__text: 0x698f4
+  __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x534
-  __TEXT.__const: 0x7160
-  __TEXT.__oslogstring: 0xe37
+  __TEXT.__const: 0x7150
+  __TEXT.__oslogstring: 0xe67
+  __TEXT.__swift5_typeref: 0x2019
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x1740
-  __TEXT.__swift5_typeref: 0x2019
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_reflstr: 0x15ad
   __TEXT.__swift5_fieldmd: 0x1cb8

   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0xf90
+  __DATA_CONST.__auth_got: 0xf98
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__auth_ptr: 0x598
   __DATA.__objc_const: 0x15e8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2271
-  Symbols:   839
-  CStrings:  721
+  Symbols:   840
+  CStrings:  722
 
Symbols:
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _exit
- _swift_errorInMain
CStrings:
+ "Failed to initialize SkyBridge daemon: %@"
```
