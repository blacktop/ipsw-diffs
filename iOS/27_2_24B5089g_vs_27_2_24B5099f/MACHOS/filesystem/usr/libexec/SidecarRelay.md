## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
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

-412.2.0.0.0
-  __TEXT.__text: 0x83be0
+412.4.0.0.0
+  __TEXT.__text: 0x83c70
   __TEXT.__auth_stubs: 0x1ce0
   __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xb40

   __TEXT.__cstring: 0x14ed
   __TEXT.__oslogstring: 0x2602
   __TEXT.__swift5_capture: 0x3e64
-  __TEXT.__unwind_info: 0x2660
-  __TEXT.__eh_frame: 0x1020
+  __TEXT.__unwind_info: 0x2678
+  __TEXT.__eh_frame: 0x1068
   __DATA_CONST.__const: 0xc228
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x168

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xe78
-  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__auth_ptr: 0x640
   __DATA.__objc_const: 0x2ce0
   __DATA.__objc_selrefs: 0x828

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4571
-  Symbols:   774
+  Functions: 4574
+  Symbols:   773
   CStrings:  880
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
- _$sSL2leoiySbx_xtFZTj
CStrings:
+ "412.4"
- "412.2"
```
