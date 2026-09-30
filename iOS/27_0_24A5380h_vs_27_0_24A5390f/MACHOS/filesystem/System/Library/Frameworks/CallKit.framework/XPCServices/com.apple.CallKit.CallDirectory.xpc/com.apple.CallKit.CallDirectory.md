## com.apple.CallKit.CallDirectory

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-145.100.7.2.1
-  __TEXT.__text: 0x21f9c
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x2a20
+147.100.5.2.1
+  __TEXT.__text: 0x21b00
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_stubs: 0x2920
   __TEXT.__objc_methlist: 0x1744
   __TEXT.__const: 0x420
-  __TEXT.__cstring: 0x84b
-  __TEXT.__objc_methname: 0x40b9
+  __TEXT.__cstring: 0x823
+  __TEXT.__objc_methname: 0x4011
   __TEXT.__objc_classname: 0x4cc
   __TEXT.__objc_methtype: 0xeeb
   __TEXT.__gcc_except_tab: 0x2f4

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__unwind_info: 0x788
   __TEXT.__eh_frame: 0x560
   __DATA_CONST.__const: 0xb50
   __DATA_CONST.__cfstring: 0x340

   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x90
   __DATA.__objc_const: 0x2968
-  __DATA.__objc_selrefs: 0xda8
+  __DATA.__objc_selrefs: 0xd88
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x840
-  __DATA.__data: 0x7a8
+  __DATA.__data: 0x7a0
   __DATA.__bss: 0x110
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 754
-  Symbols:   248
-  CStrings:  1013
+  Symbols:   246
+  CStrings:  1008
 
Symbols:
+ _swift_release_x24
- _OBJC_CLASS_$_NSUserDefaults
- _swift_getObjCClassFromMetadata
- _swift_release_x28
Functions:
~ sub_100019800 : 152 -> 124
~ sub_100019898 -> sub_10001987c : 148 -> 124
~ sub_10001a7bc -> sub_10001a788 : 708 -> 696
~ sub_10001aa80 -> sub_10001aa40 : 3572 -> 3352
~ sub_10001b9ac -> sub_10001b890 : 5528 -> 4928
~ sub_10001d074 -> sub_10001cd00 : 4000 -> 3940
~ sub_10001e014 -> sub_10001dc64 : 388 -> 372
~ sub_10001e198 -> sub_10001ddd8 : 4400 -> 4332
~ sub_10002160c -> sub_100021208 : 400 -> 244
~ sub_100021ed4 -> sub_100021a34 : 16 -> 76
~ sub_100021ee4 -> sub_100021a80 : 28 -> 16
~ sub_100021f00 -> sub_100021a90 : 20 -> 28
~ sub_100021f14 -> sub_100021aac : 84 -> 20
~ sub_100021f68 -> sub_100021ac0 : 72 -> 84
CStrings:
- "boolForKey:"
- "initWithType:endpoint:issuer:bearerToken:featureId:privacyProxyFailOpen:useUserTierTokenKey:fetchConfigViaProxy:"
- "instancesRespondToSelector:"
- "livecalleridProfileEnabled"
- "standardUserDefaults"
```
