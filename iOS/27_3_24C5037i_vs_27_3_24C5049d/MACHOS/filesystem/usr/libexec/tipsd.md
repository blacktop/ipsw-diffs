## tipsd

> `/usr/libexec/tipsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
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
- `__DATA.__data`

```diff

-866.3.1.0.0
-  __TEXT.__text: 0x17e70
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0x2e80
+866.3.3.0.0
+  __TEXT.__text: 0x17f28
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_stubs: 0x2ec0
   __TEXT.__objc_methlist: 0xd88
   __TEXT.__const: 0x374
   __TEXT.__gcc_except_tab: 0x4bc
   __TEXT.__cstring: 0xe8c
-  __TEXT.__objc_methname: 0x3838
-  __TEXT.__oslogstring: 0x1755
+  __TEXT.__objc_methname: 0x3858
+  __TEXT.__oslogstring: 0x1768
   __TEXT.__objc_classname: 0x225
   __TEXT.__objc_methtype: 0x11f9
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA.__objc_const: 0xc70
-  __DATA.__objc_selrefs: 0xed0
+  __DATA.__objc_selrefs: 0xee0
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x660

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 492
-  Symbols:   403
-  CStrings:  927
+  Symbols:   404
+  CStrings:  930
 
Symbols:
+ _arc4random_uniform
Functions:
~ sub_100008b04 : 1268 -> 1404
~ sub_100016a0c -> sub_100016a94 : 260 -> 284
~ sub_100016b10 -> sub_100016bb0 : 128 -> 152
CStrings:
+ "Rollout bucket %ld"
+ "rolloutBucket"
+ "setRolloutBucket:"
```
