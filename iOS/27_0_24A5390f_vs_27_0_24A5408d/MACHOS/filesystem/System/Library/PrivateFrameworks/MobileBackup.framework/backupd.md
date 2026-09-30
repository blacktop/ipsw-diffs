## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift5_proto`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3039.0.1.0.0
-  __TEXT.__text: 0x247b64
+3039.2.2.0.0
+  __TEXT.__text: 0x247bd4
   __TEXT.__auth_stubs: 0x32a0
-  __TEXT.__objc_stubs: 0x280e0
+  __TEXT.__objc_stubs: 0x28100
   __TEXT.__objc_methlist: 0x15ea4
   __TEXT.__const: 0x1820
   __TEXT.__objc_classname: 0x2140
-  __TEXT.__objc_methname: 0x3774a
+  __TEXT.__objc_methname: 0x3776a
   __TEXT.__objc_methtype: 0x65e6
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_typeref: 0xcfa

   __DATA_CONST.__auth_got: 0x1960
   __DATA_CONST.__got: 0xf30
   __DATA_CONST.__auth_ptr: 0x298
-  __DATA.__objc_const: 0x23740
-  __DATA.__objc_selrefs: 0xb7b0
-  __DATA.__objc_ivar: 0x1998
+  __DATA.__objc_const: 0x23780
+  __DATA.__objc_selrefs: 0xb7b8
+  __DATA.__objc_ivar: 0x19a0
   __DATA.__objc_data: 0x6b30
   __DATA.__data: 0x2378
   __DATA.__bss: 0x1938

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 8928
   Symbols:   1316
-  CStrings:  18401
+  CStrings:  18402
 
Functions:
~ sub_1000cbec0 : 496 -> 528
~ sub_1000cf2e8 -> sub_1000cf308 : 1032 -> 1056
~ sub_10011cd5c -> sub_10011cd94 : 496 -> 528
~ sub_10011f6c0 -> sub_10011f718 : 764 -> 788
CStrings:
+ "d2dBackgroundDisconnectTimeout"
+ "d2dFileTransferDisconnectTimeout"
- "d2dTransferDisconnectTimeout"
```
