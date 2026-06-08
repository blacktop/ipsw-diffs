## usbctelemetryd

> `/usr/libexec/usbctelemetryd`

```diff

 5.0.0.0.0
-  __TEXT.__text: 0x1164
-  __TEXT.__auth_stubs: 0x210
+  __TEXT.__text: 0x10cc
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0xf0
-  __TEXT.__cstring: 0x2dd
+  __TEXT.__cstring: 0x2e0
   __TEXT.__oslogstring: 0xac
-  __TEXT.__objc_classname: 0x28
+  __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methname: 0x203
   __TEXT.__objc_methtype: 0x82
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x40
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_const: 0x2a0
   __DATA.__objc_selrefs: 0xa0
   __DATA.__objc_ivar: 0x18

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77D3A544-A23F-3B22-B98E-4035168D13B1
+  UUID: 4F65366F-D1D4-369B-9EDC-7D2D4C84BF32
   Functions: 26
-  Symbols:   46
+  Symbols:   47
   CStrings:  140
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000aa8 : 592 -> 588
~ sub_100000cf8 -> sub_100000cf4 : 124 -> 120
~ sub_100000de8 -> sub_100000de0 : 208 -> 204
~ sub_100000f8c -> sub_100000f80 : 364 -> 352
~ sub_1000010f8 -> sub_1000010e0 : 252 -> 248
~ sub_100001268 -> sub_10000124c : 804 -> 756
~ sub_100001598 -> sub_10000154c : 1024 -> 960
~ sub_1000019d4 -> sub_100001948 : 304 -> 292

```
