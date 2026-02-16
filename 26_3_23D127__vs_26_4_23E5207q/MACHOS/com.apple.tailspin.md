## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0x618
-  __TEXT.__auth_stubs: 0x230
+250.0.0.0.0
+  __TEXT.__text: 0x65c
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x8c
   __TEXT.__oslogstring: 0xfe
   __TEXT.__objc_methname: 0x5a
-  __TEXT.__unwind_info: 0x78
-  __DATA.__auth_got: 0x120
+  __TEXT.__unwind_info: 0x70
+  __DATA.__auth_got: 0x128
   __DATA.__got: 0x18
   __DATA.__const: 0x48
   __DATA.__cfstring: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 42D29CBC-D4F5-39D6-A94F-7810BDEDE9C2
+  UUID: 198A7746-44E9-34FB-A7BA-5BDF5D42843C
   Functions: 7
-  Symbols:   46
+  Symbols:   47
   CStrings:  22
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
Functions:
~ _init_tailspin : 1152 -> 1188
~ sub_ce8 -> sub_d0c : 68 -> 84
~ sub_d2c -> sub_d60 : 96 -> 112

```
