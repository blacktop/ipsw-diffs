## DemoApp

> `/Applications/DemoApp.app/DemoApp`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0xbf0
-  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__text: 0xbe4
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x464
-  __TEXT.__objc_classname: 0x59
+  __TEXT.__objc_classname: 0x57
   __TEXT.__objc_methname: 0xef8
   __TEXT.__objc_methtype: 0x99e
-  __TEXT.__cstring: 0x96
+  __TEXT.__cstring: 0x98
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x70
   __DATA.__objc_const: 0x5d8
   __DATA.__objc_selrefs: 0x3c0
   __DATA.__objc_ivar: 0x18

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2EE871E7-77F2-3D4D-8887-1CE766DCF79C
+  UUID: 6C2E92A0-A21C-3BF0-A0ED-494DA0EC1AE2
   Functions: 19
-  Symbols:   57
+  Symbols:   56
   CStrings:  234
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ sub_100000d8c : 84 -> 76
~ sub_100000de0 -> sub_100000dd8 : 100 -> 96
~ sub_100001138 -> sub_10000112c : 396 -> 404
~ sub_1000012c4 -> sub_1000012c0 : 76 -> 80
~ sub_100001310 : 440 -> 416
~ sub_1000014c8 -> sub_1000014b0 : 280 -> 288
~ sub_1000015e0 -> sub_1000015d0 : 308 -> 316
~ sub_100001768 -> sub_100001760 : 192 -> 196
~ sub_1000018f8 -> sub_1000018f4 : 60 -> 56
~ sub_100001934 -> sub_10000192c : 60 -> 56

```
