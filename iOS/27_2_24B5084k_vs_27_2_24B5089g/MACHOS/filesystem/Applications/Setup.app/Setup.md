## Setup

> `/Applications/Setup.app/Setup`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5411.103.0.0.0
-  __TEXT.__text: 0x2444e8
+5411.104.0.0.0
+  __TEXT.__text: 0x2445fc
   __TEXT.__auth_stubs: 0x28f0
   __TEXT.__objc_stubs: 0x293c0
-  __TEXT.__objc_methlist: 0x1dc20
+  __TEXT.__objc_methlist: 0x1dc28
   __TEXT.__dlopen_cstrs: 0x179c
   __TEXT.__const: 0x3658
   __TEXT.__objc_classname: 0x5c0c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12340
+  Functions: 12341
   Symbols:   1530
   CStrings:  14880
 
Functions:
~ sub_10005ff18 : 856 -> 900
+ sub_10015fba8
```
