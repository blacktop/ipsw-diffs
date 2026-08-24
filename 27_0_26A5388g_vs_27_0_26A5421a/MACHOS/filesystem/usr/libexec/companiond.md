## companiond

> `/usr/libexec/companiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-524.0.38.0.0
-  __TEXT.__text: 0x72548
-  __TEXT.__auth_stubs: 0x26d0
-  __TEXT.__objc_stubs: 0x2f40
+524.0.56.0.0
+  __TEXT.__text: 0x72b98
+  __TEXT.__auth_stubs: 0x26f0
+  __TEXT.__objc_stubs: 0x2f80
   __TEXT.__objc_methlist: 0x2270
-  __TEXT.__objc_methname: 0x4855
-  __TEXT.__swift5_typeref: 0xb7d
+  __TEXT.__objc_methname: 0x4885
+  __TEXT.__swift5_typeref: 0xb99
   __TEXT.__swift5_fieldmd: 0x7d8
   __TEXT.__objc_classname: 0x9d5
   __TEXT.__objc_methtype: 0x11fc
-  __TEXT.__const: 0x1f2e
+  __TEXT.__const: 0x1f3e
   __TEXT.__constg_swiftt: 0x7dc
   __TEXT.__swift5_reflstr: 0x762
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_protos: 0x4
   __TEXT.__gcc_except_tab: 0xf18
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x1ba0
+  __TEXT.__unwind_info: 0x1b90
   __TEXT.__eh_frame: 0x41c8
   __DATA_CONST.__const: 0x1f48
   __DATA_CONST.__cfstring: 0x1280

   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x1378
+  __DATA_CONST.__auth_got: 0x1388
   __DATA_CONST.__got: 0xaa0
   __DATA_CONST.__auth_ptr: 0x578
   __DATA.__objc_const: 0x6020
-  __DATA.__objc_selrefs: 0x1010
+  __DATA.__objc_selrefs: 0x1020
   __DATA.__objc_ivar: 0x318
   __DATA.__objc_data: 0x15c0
-  __DATA.__data: 0x1c20
+  __DATA.__data: 0x1c30
   __DATA.__bss: 0x2370
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1889
-  Symbols:   1099
-  CStrings:  1486
+  Functions: 1890
+  Symbols:   1101
+  CStrings:  1488
 
Symbols:
+ _swift_initStackObject
+ _swift_setDeallocating
CStrings:
+ "initWithUnsignedLongLong:"
+ "numberWithUnsignedLongLong:"
```
