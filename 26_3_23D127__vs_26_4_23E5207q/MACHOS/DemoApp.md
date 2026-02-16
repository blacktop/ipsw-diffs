## DemoApp

> `/Applications/DemoApp.app/DemoApp`

```diff

 45.0.0.0.0
-  __TEXT.__text: 0xba0
-  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__text: 0xbf0
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0x464
   __TEXT.__objc_classname: 0x59

   __TEXT.__cstring: 0x96
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x120

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE40CF0F-A918-3472-AD62-F2D62C134AEC
+  UUID: BE297251-6651-36C2-973A-E2E30938690B
   Functions: 19
-  Symbols:   56
+  Symbols:   57
   CStrings:  234
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
Functions:
~ sub_100000d8c : 76 -> 84
~ sub_100000dd8 -> sub_100000de0 : 96 -> 100
~ sub_100000e90 -> sub_100000e9c : 212 -> 220
~ sub_100000fb0 -> sub_100000fc4 : 360 -> 372
~ sub_100001118 -> sub_100001138 : 392 -> 396
~ sub_1000012ec -> sub_100001310 : 412 -> 440
~ sub_100001488 -> sub_1000014c8 : 288 -> 280
~ sub_1000015a8 -> sub_1000015e0 : 296 -> 308
~ sub_100001724 -> sub_100001768 : 188 -> 192
~ sub_1000018b0 -> sub_1000018f8 : 56 -> 60
~ sub_1000018e8 -> sub_100001934 : 56 -> 60

```
