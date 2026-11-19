## trace

> `/usr/bin/trace`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-706.0.2.0.0
-  __TEXT.__text: 0x15f44
+706.40.6.0.0
+  __TEXT.__text: 0x15ef4
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x5c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x358
   __DATA.__objc_const: 0x180
   __DATA.__objc_selrefs: 0x50
-  __DATA.__data: 0x488
+  __DATA.__data: 0x480
   __DATA.__common: 0x861b8
   __DATA.__bss: 0x15d0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 433
-  Symbols:   429
+  Symbols:   428
   CStrings:  259
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
- _$sSL2leoiySbx_xtFZTj
Functions:
~ sub_100009148 : 7632 -> 7552
```
