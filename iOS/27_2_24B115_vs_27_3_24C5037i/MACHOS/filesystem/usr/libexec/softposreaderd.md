## softposreaderd

> `/usr/libexec/softposreaderd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-51.5.0.0.0
-  __TEXT.__text: 0x40df3c
+52.2.0.0.0
+  __TEXT.__text: 0x40e2e4
   __TEXT.__auth_stubs: 0x42c0
   __TEXT.__objc_stubs: 0x2080
   __TEXT.__objc_methlist: 0xe7c

   __TEXT.__swift5_typeref: 0x24cc
   __TEXT.__cstring: 0x11b7b
   __TEXT.__objc_methtype: 0x1525
-  __TEXT.__oslogstring: 0xd11e
+  __TEXT.__oslogstring: 0xd17e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x7984
   __TEXT.__swift5_proto: 0xcdc

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 6171
   Symbols:   1692
-  CStrings:  3606
+  CStrings:  3609
 
Functions:
~ sub_100069cc4 : 15824 -> 16088
~ sub_1000d1b7c -> sub_1000d1c84 : 576 -> 420
~ sub_10012bff8 -> sub_10012c064 : 324 -> 360
~ sub_10013ccc0 -> sub_10013cd50 : 5148 -> 5504
~ sub_1001c2660 -> sub_1001c2854 : 4908 -> 5308
~ sub_100234f68 -> sub_1002352ec : 5592 -> 5628
CStrings:
+ "Error validating time token: %@"
+ "NFC antenna is not present"
+ "NFC hardware not supported"
```
