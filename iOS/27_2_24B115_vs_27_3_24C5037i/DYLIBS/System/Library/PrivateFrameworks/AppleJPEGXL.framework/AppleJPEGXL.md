## AppleJPEGXL

> `/System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL`

```diff

-24.0.0.0.0
-  __TEXT.__text: 0x154ad0
+24.60.2.0.0
+  __TEXT.__text: 0x154aa4
   __TEXT.__const: 0x770d0
-  __TEXT.__cstring: 0xd6f
+  __TEXT.__cstring: 0xd8c
   __TEXT.__gcc_except_tab: 0x4d38
   __TEXT.__unwind_info: 0x2f60
   __TEXT.__eh_frame: 0x440

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x31a8
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__data: 0xc0

   __DATA_DIRTY.__bss: 0x340
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/ASRKit.framework/ASRKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2611
-  Symbols:   234
-  CStrings:  130
+  Symbols:   235
+  CStrings:  131
 
Symbols:
+ _asr_check_parser
Functions:
~ sub_2560c02dc -> sub_259e65334 : 1320 -> 1304
~ sub_2560c3d20 -> sub_259e68d68 : 300 -> 284
~ sub_2560c4914 -> sub_259e6994c : 380 -> 372
~ sub_2560c5014 -> sub_259e6a044 : 372 -> 360
~ sub_2560c52e8 -> sub_259e6a30c : 384 -> 372
~ sub_2560c55d4 -> sub_259e6a5ec : 384 -> 372
~ sub_2560c58c0 -> sub_259e6a8cc : 388 -> 372
~ sub_2560c9d88 -> sub_259e6ed84 : 976 -> 992
~ sub_2560ca640 -> sub_259e6f64c : 656 -> 668
~ sub_2560e0248 -> sub_259e85260 : 1248 -> 1316
~ sub_25612f2fc -> sub_259ed4358 : 11572 -> 11496
~ _JxlDecoderCreate : 716 -> 744
CStrings:
+ "com.apple.applejpegxl.libjxl"
```
