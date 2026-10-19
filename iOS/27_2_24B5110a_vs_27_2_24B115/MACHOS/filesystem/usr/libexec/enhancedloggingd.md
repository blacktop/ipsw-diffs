## enhancedloggingd

> `/usr/libexec/enhancedloggingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 277.42.1.0.0
-  __TEXT.__text: 0xb0418
+  __TEXT.__text: 0xb039c
   __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x3420
+  __TEXT.__objc_stubs: 0x3400
   __TEXT.__objc_methlist: 0x1434
   __TEXT.__const: 0x583c
   __TEXT.__cstring: 0x305d
-  __TEXT.__objc_methname: 0x4bfd
+  __TEXT.__objc_methname: 0x4bed
   __TEXT.__objc_classname: 0x4d7
   __TEXT.__objc_methtype: 0x11fb
   __TEXT.__oslogstring: 0x3176

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__auth_got: 0x11e0
-  __DATA_CONST.__got: 0xa90
+  __DATA_CONST.__got: 0xa88
   __DATA_CONST.__auth_ptr: 0x618
   __DATA.__objc_const: 0x2718
-  __DATA.__objc_selrefs: 0x1040
+  __DATA.__objc_selrefs: 0x1038
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x8d8
   __DATA.__data: 0x2bc8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3024
-  Symbols:   1034
-  CStrings:  1427
+  Symbols:   1033
+  CStrings:  1426
 
Symbols:
- _AKSeedBuildHeaderKey
Functions:
~ sub_100047dd0 : 3536 -> 3412
CStrings:
- "shouldHideSeedBuildHeader"
```
