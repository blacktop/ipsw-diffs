## backgroundassets.user

> `/usr/libexec/backgroundassets.user`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
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

-279.52.2.0.0
-  __TEXT.__text: 0x5938c
-  __TEXT.__auth_stubs: 0x1970
-  __TEXT.__objc_stubs: 0x7860
+279.60.2.0.0
+  __TEXT.__text: 0x594cc
+  __TEXT.__auth_stubs: 0x1960
+  __TEXT.__objc_stubs: 0x7840
   __TEXT.__objc_methlist: 0x3534
   __TEXT.__const: 0x1ae8
   __TEXT.__objc_classname: 0x84e
-  __TEXT.__objc_methtype: 0x19b2
+  __TEXT.__objc_methtype: 0x19a2
   __TEXT.__oslogstring: 0x6f94
   __TEXT.__cstring: 0x4230
-  __TEXT.__objc_methname: 0x9cde
+  __TEXT.__objc_methname: 0x9cce
   __TEXT.__gcc_except_tab: 0x14fc
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x428

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xcc8
+  __DATA_CONST.__auth_got: 0xcc0
   __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x360
   __DATA.__objc_const: 0x5a30
-  __DATA.__objc_selrefs: 0x21c0
+  __DATA.__objc_selrefs: 0x21b8
   __DATA.__objc_ivar: 0x3b8
   __DATA.__objc_data: 0x1210
   __DATA.__data: 0x12e8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1952
-  Symbols:   704
-  CStrings:  2620
+  Symbols:   703
+  CStrings:  2619
 
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
- _swift_retain_x27
Functions:
~ sub_1000027f8 : 2824 -> 2788
~ sub_100004678 -> sub_100004654 : 256 -> 260
~ sub_1000121e4 -> sub_1000121c4 : 384 -> 380
~ sub_100012928 -> sub_100012904 : 100 -> 96
~ sub_10001298c -> sub_100012964 : 116 -> 112
~ sub_100012cfc -> sub_100012cd0 : 1380 -> 1376
~ sub_10001329c -> sub_10001326c : 72 -> 68
~ sub_1000132e4 -> sub_1000132b0 : 2092 -> 2088
~ sub_100013b50 -> sub_100013b18 : 1448 -> 1440
~ sub_1000142a4 -> sub_100014264 : 596 -> 592
~ sub_1000147b0 -> sub_10001476c : 360 -> 356
~ sub_100014918 -> sub_1000148d0 : 564 -> 560
~ sub_100014b4c -> sub_100014b00 : 984 -> 980
~ sub_100015020 -> sub_100014fd0 : 292 -> 288
~ sub_100015144 -> sub_1000150f0 : 344 -> 340
~ sub_10001529c -> sub_100015244 : 424 -> 420
~ sub_100015444 -> sub_1000153e8 : 192 -> 188
~ sub_100015504 -> sub_1000154a4 : 296 -> 292
~ sub_10001562c -> sub_1000155c8 : 296 -> 292
~ sub_100015754 -> sub_1000156ec : 112 -> 108
~ sub_100015bb8 -> sub_100015b4c : 280 -> 276
~ sub_100015df0 -> sub_100015d80 : 348 -> 344
~ sub_100015f4c -> sub_100015ed8 : 404 -> 396
~ sub_10003dc1c -> sub_10003dba0 : 10724 -> 10964
~ sub_100042ef0 -> sub_100042f64 : 112 -> 124
~ sub_10004aa2c -> sub_10004aaac : 432 -> 460
~ sub_10004cdac -> sub_10004ce48 : 1820 -> 1836
~ sub_10005310c -> sub_1000531b8 : 11408 -> 11504
~ sub_100055fe8 -> sub_1000560f4 : 428 -> 456
~ sub_100056194 -> sub_1000562bc : 256 -> 280
CStrings:
+ "_resetAllowsCellularAccess"
+ "_resetAllowsConstrainedNetworkAccess"
+ "_resetAllowsExpensiveNetworkAccess"
+ "{os_unfair_recursive_lock_s=\"_os_unfair_recursive_lock_opaque\"[2I]}"
- "allowsCellularAccess"
- "allowsConstrainedNetworkAccess"
- "allowsExpensiveNetworkAccess"
- "setAllowsConstrainedNetworkAccess:"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
```
