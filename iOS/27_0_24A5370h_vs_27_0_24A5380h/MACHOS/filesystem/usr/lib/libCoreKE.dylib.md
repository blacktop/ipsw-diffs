## libCoreKE.dylib

> `/usr/lib/libCoreKE.dylib`

```diff

-  __TEXT.__text: 0x15a5e7c
+  __TEXT.__text: 0x15a413c
   __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0x80
-  __TEXT.__const: 0xdf004
+  __TEXT.__const: 0xdeaf4
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x25ca
+  __TEXT.__cstring: 0x2639
   __TEXT.__objc_methname: 0x5b
-  __TEXT.__unwind_info: 0xc10
+  __TEXT.__unwind_info: 0xc20
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__const: 0x1d678
+  __DATA_CONST.__const: 0x17b68
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_selrefs: 0x20
-  __DATA.__data: 0x5348
+  __DATA.__data: 0x5d20
   __DATA.__bss: 0x71
-  __DATA.__common: 0xc40
+  __DATA.__common: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 820
+  Functions: 821
   Symbols:   179
-  CStrings:  394
+  CStrings:  396
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x23
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s cccurve25519 failed: small-order point used%s\n"
+ "generate_wrapping_key_curve25519"

```
