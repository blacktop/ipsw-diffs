## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-400.42.0.0.0
-  __TEXT.__text: 0x88c50
+412.4.0.0.0
+  __TEXT.__text: 0x88cf0
   __TEXT.__auth_stubs: 0x1a80
   __TEXT.__objc_stubs: 0x19c0
   __TEXT.__objc_methlist: 0xab0
-  __TEXT.__const: 0x49dd
+  __TEXT.__const: 0x49ec
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2034
   __TEXT.__swift5_typeref: 0x1d16

   __TEXT.__swift5_capture: 0x3e60
   __TEXT.__oslogstring: 0x2c31
   __TEXT.__cstring: 0x1669
-  __TEXT.__info_plist: 0x592
-  __TEXT.__unwind_info: 0x2698
-  __TEXT.__eh_frame: 0x1058
+  __TEXT.__info_plist: 0x591
+  __TEXT.__unwind_info: 0x26b0
+  __TEXT.__eh_frame: 0x10a0
   __DATA_CONST.__const: 0xc1e8
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x140

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xd48
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__auth_ptr: 0x650
   __DATA.__objc_const: 0x29b8
   __DATA.__objc_selrefs: 0x7d0

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4627
-  Symbols:   736
+  Functions: 4632
+  Symbols:   735
   CStrings:  874
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
- _$sSL2leoiySbx_xtFZTj
CStrings:
+ "412.4"
- "400.42"
```
