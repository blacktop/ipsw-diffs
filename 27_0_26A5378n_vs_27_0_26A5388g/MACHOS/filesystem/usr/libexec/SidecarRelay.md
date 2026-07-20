## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-400.39.0.0.0
-  __TEXT.__text: 0x8ca70
+400.40.0.0.0
+  __TEXT.__text: 0x8cd10
   __TEXT.__auth_stubs: 0x1a80
-  __TEXT.__objc_stubs: 0x19a0
+  __TEXT.__objc_stubs: 0x19c0
   __TEXT.__objc_methlist: 0xab0
-  __TEXT.__const: 0x49cd
+  __TEXT.__const: 0x49dd
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2034
-  __TEXT.__swift5_typeref: 0x1d04
+  __TEXT.__swift5_typeref: 0x1d16
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0xe2a
   __TEXT.__swift5_fieldmd: 0x132c

   __TEXT.__objc_classname: 0x925
   __TEXT.__objc_methtype: 0xecf
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__objc_methname: 0x22d9
+  __TEXT.__objc_methname: 0x22e9
   __TEXT.__swift5_capture: 0x3e60
   __TEXT.__oslogstring: 0x2c31
   __TEXT.__cstring: 0x1669

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xd48
-  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__auth_ptr: 0x650
   __DATA.__objc_const: 0x29b8
-  __DATA.__objc_selrefs: 0x7c8
+  __DATA.__objc_selrefs: 0x7d0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1420
-  __DATA.__data: 0x3508
+  __DATA.__data: 0x3518
   __DATA.__bss: 0x5730
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4622
-  Symbols:   735
-  CStrings:  873
+  Symbols:   736
+  CStrings:  874
 
Symbols:
+ _RPOptionStatusFlags
CStrings:
+ "400.40"
+ "initWithUnsignedLongLong:"
- "400.39"
```
