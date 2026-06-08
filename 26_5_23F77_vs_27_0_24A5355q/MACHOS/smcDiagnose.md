## smcDiagnose

> `/usr/libexec/smcDiagnose`

```diff

-141.0.0.0.0
-  __TEXT.__text: 0x3e6c
-  __TEXT.__auth_stubs: 0x280
+159.0.0.0.0
+  __TEXT.__text: 0x3df8
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x8c0
+  __TEXT.__cstring: 0x8c2
   __TEXT.__const: 0x1c
   __TEXT.__objc_methname: 0x154
-  __TEXT.__objc_classname: 0x10
+  __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methtype: 0x75
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x48
+  __TEXT.__unwind_info: 0x130
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0xf8
   __DATA.__objc_selrefs: 0xc0
   __DATA.__objc_ivar: 0xc

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C76F81E-F0E0-39FB-A27B-A6EA6BEF1C03
+  UUID: C319497D-876E-306C-85A4-6F1D9431AB85
   Functions: 58
-  Symbols:   56
+  Symbols:   58
   CStrings:  142
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000b80 : 96 -> 100
~ sub_100001184 -> sub_100001188 : 240 -> 244
~ sub_100001274 -> sub_10000127c : 436 -> 440
~ sub_100001604 -> sub_100001610 : 376 -> 356
~ sub_10000177c -> sub_100001774 : 196 -> 188
~ sub_100001840 -> sub_100001830 : 232 -> 220
~ sub_100001a0c -> sub_1000019f0 : 272 -> 264
~ sub_100001c20 -> sub_100001bfc : 272 -> 268
~ sub_100001e7c -> sub_100001e54 : 276 -> 264
~ sub_100002110 -> sub_1000020dc : 712 -> 720
~ sub_100002744 -> sub_100002718 : 136 -> 132
~ sub_100003fe8 -> sub_100003fb8 : 440 -> 444
~ sub_1000041a8 -> sub_10000417c : 160 -> 156
~ sub_100004248 -> sub_100004218 : 160 -> 156
~ sub_1000042e8 -> sub_1000042b4 : 56 -> 8
~ sub_100004320 -> sub_1000042bc : 128 -> 124
~ sub_1000043a0 -> sub_100004338 : 120 -> 116
~ sub_100004420 -> sub_1000043b4 : 96 -> 92
~ sub_100004480 -> sub_100004410 : 96 -> 92

```
