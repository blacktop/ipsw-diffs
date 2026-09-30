## SidecarDisplayAgent

> `/usr/libexec/SidecarDisplayAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__cstring`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-400.40.0.0.0
-  __TEXT.__text: 0x9479c
-  __TEXT.__auth_stubs: 0x3110
+400.42.0.0.0
+  __TEXT.__text: 0x947d8
+  __TEXT.__auth_stubs: 0x3120
   __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x7bc
   __TEXT.__const: 0x5b2a
   __TEXT.__objc_methtype: 0x89e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3468
+  __TEXT.__constg_swiftt: 0x3470
   __TEXT.__swift5_typeref: 0x1b04
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_reflstr: 0x165a

   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__unwind_info: 0x2a38
+  __TEXT.__unwind_info: 0x2a30
   __TEXT.__eh_frame: 0x1aa4
   __DATA_CONST.__const: 0x9700
   __DATA_CONST.__cfstring: 0x140

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1898
+  __DATA_CONST.__auth_got: 0x18a0
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0xb18
   __DATA.__objc_const: 0x3e88
   __DATA.__objc_selrefs: 0xab8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xe60
-  __DATA.__data: 0x49f0
+  __DATA.__data: 0x4a00
   __DATA.__bss: 0x5eb0
   __DATA.__common: 0x218
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5349
-  Symbols:   1267
+  Symbols:   1268
   CStrings:  1092
 
Symbols:
+ _CGDisplayIsInMirrorSet
CStrings:
+ "400.42"
- "400.40"
```
