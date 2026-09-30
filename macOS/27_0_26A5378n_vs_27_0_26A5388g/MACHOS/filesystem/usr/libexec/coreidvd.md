## coreidvd

> `/usr/libexec/coreidvd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-9.36.0.0.0
-  __TEXT.__text: 0x382a4c
+9.38.0.0.0
+  __TEXT.__text: 0x382ad4
   __TEXT.__auth_stubs: 0x8260
   __TEXT.__objc_stubs: 0x3ba0
   __TEXT.__objc_methlist: 0x124c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__auth_got: 0x4138
-  __DATA_CONST.__got: 0x3008
+  __DATA_CONST.__got: 0x3010
   __DATA_CONST.__auth_ptr: 0x1ad0
   __DATA.__objc_const: 0xbca8
   __DATA.__objc_selrefs: 0x14f0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 11387
-  Symbols:   4021
+  Symbols:   4022
   CStrings:  4730
 
Symbols:
+ _$s11CBORLibrary10COSE_Sign1V13CoreIDVSharedE19fromHexOrBinaryDataAC10Foundation0J0V_tKcfC
+ _$s7CoreIDV27MobileDocumentReaderSessionC5ErrorV4CodeO15documentExpiredyA2GmFWC
- _$s11CBORLibrary10COSE_Sign1V13CoreIDVSharedE11fromHexDataAC10Foundation0H0V_tKcfC
Functions:
~ sub_1001e9a04 : 5928 -> 6064
```
