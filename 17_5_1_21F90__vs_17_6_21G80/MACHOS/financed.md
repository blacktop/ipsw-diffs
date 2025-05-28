## financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

-144.37.1.0.0
-  __TEXT.__text: 0x1988
+144.41.2.0.0
+  __TEXT.__text: 0x1990
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__const: 0x3a
   __TEXT.__cstring: 0x3b6
   __TEXT.__oslogstring: 0x2b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x4a
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0x9c
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x168
   __DATA_CONST.__got: 0x40

   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
+  __DATA_CONST.__linkguard: 0xe
   __DATA.__objc_selrefs: 0x20
   __DATA.__data: 0xa0
   __DATA.__common: 0x1d0

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 79
-  Symbols:   83
+  Functions: 80
+  Symbols:   84
   CStrings:  26
 
Symbols:
+ __linkguard_init

```
