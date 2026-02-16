## managedappsd

> `/usr/libexec/managedappsd`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x6d8
+59.100.16.0.0
+  __TEXT.__text: 0x818
   __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x42
-  __TEXT.__objc_methname: 0x13
   __TEXT.__oslogstring: 0x8c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0x66
+  __TEXT.__objc_methname: 0x13
   __TEXT.__unwind_info: 0x78
-  __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__auth_got: 0x100
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F63CC6F9-ED2E-3310-934B-4B0E840A5062
+  UUID: 39BDBA28-E9B7-3CA2-9936-B94F05A9C3C1
   Functions: 6
-  Symbols:   43
+  Symbols:   44
   CStrings:  10
 
Symbols:
+ _objc_release_x23
+ _objc_release_x25
- _$s20ManagedAppsInterface0aB12ServiceScopeO8rawValueSivg
Functions:
~ sub_100000c58 -> sub_100000ca8 : 724 -> 700
~ sub_100000f2c -> sub_100000f64 : 388 -> 552
~ sub_1000010b0 -> sub_10000118c : 368 -> 548

```
