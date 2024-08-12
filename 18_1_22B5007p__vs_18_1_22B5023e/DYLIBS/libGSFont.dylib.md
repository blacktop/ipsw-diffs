## libGSFont.dylib

> `/System/Library/PrivateFrameworks/FontServices.framework/libGSFont.dylib`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x800c
-  __TEXT.__auth_stubs: 0xae0
+137.0.0.0.0
+  __TEXT.__text: 0x82c0
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x8f2
+  __TEXT.__cstring: 0x92c
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__oslogstring: 0x15d
   __TEXT.__unwind_info: 0x218
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x6a8
-  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_methname: 0x6b7
+  __TEXT.__objc_stubs: 0x9a0
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__cfstring: 0xb60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__bss: 0xa8
-  __DATA_DIRTY.__bss: 0x98
+  __DATA.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/FontServices.framework/FontServices
+  - /System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib
   - /System/Library/PrivateFrameworks/FontServices.framework/libGSFontCache.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 137
-  Symbols:   361
-  CStrings:  190
+  Functions: 138
+  Symbols:   363
+  CStrings:  194
 
Symbols:
+ _CGFontGetParserFont
+ _FPFontCopyMetadata
+ _GSFontFileDescriptorForPath
- _OSAtomicCompareAndSwapPtrBarrier
CStrings:
+ "MTD_Typeface_info_PlatformDelivery"
+ "fileDescriptor"
+ "fontData"
+ "iOS-invisible"

```
