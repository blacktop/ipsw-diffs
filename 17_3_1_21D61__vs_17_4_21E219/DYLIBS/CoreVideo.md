## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-604.3.0.0.0
-  __TEXT.__text: 0x3725c
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__cstring: 0x79cc
+612.8.0.0.0
+  __TEXT.__text: 0x37680
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__cstring: 0x79ce
   __TEXT.__objc_databytes: 0x473
   __TEXT.__const: 0xf2b
-  __TEXT.__oslogstring: 0x93
+  __TEXT.__oslogstring: 0x29b
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0xae4
+  __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_methname: 0x181
   __TEXT.__objc_stubs: 0x1c0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x3740
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x44638
   __AUTH_CONST.__objc_dictobj: 0x16eb8
   __AUTH_CONST.__cfstring: 0x29a0

   __AUTH_CONST.__objc_arrayobj: 0x4320
   __AUTH_CONST.__const: 0x1a68
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_databytes: 0x300
   __AUTH.__data: 0x480
-  __DATA.__objc_classrefs: 0x10
-  __DATA.__data: 0x1f1
-  __DATA.__bss: 0x4f
+  __DATA.__data: 0x1c9
+  __DATA.__bss: 0x47
   __DATA.__common: 0xc
   __DATA_DIRTY.__const: 0x270
-  __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x250
+  __DATA_DIRTY.__data: 0x100
+  __DATA_DIRTY.__bss: 0x288
   __DATA_DIRTY.__common: 0x3c
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1330
-  Symbols:   4225
-  CStrings:  853
+  Functions: 1340
+  Symbols:   4246
+  CStrings:  861
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.1
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.2
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.3
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.4
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.5
+ __ZN17CVPixelBufferPool15initWithOptionsEPK14__CFDictionaryS2_Pi.cold.6
+ __ZN20CVPixelBufferBacking30initWithPixelBufferDescriptionEmmPvmmmPS0_PmS2_S2_PFvS0_PKvEPFvS0_S4_mmPS4_ES0_PK14__CFDictionarySC_P11__IOSurfaceSE_P10__CVBufferS2_Pi.cold.1
+ __ZN20CVPixelBufferBacking30initWithPixelBufferDescriptionEmmPvmmmPS0_PmS2_S2_PFvS0_PKvEPFvS0_S4_mmPS4_ES0_PK14__CFDictionarySC_P11__IOSurfaceSE_P10__CVBufferS2_Pi.cold.2
+ __os_log_error_impl
CStrings:
+ " (IOSurface ID 0x%llx (%s))"
+ "Cannot create CVPixelBufferPool with NULL pixelBufferAttributes."
+ "Cannot create CVPixelBufferPool with kCVPixelBufferHeightKey value (%lld) <= 0."
+ "Cannot create CVPixelBufferPool with kCVPixelBufferWidthKey value (%lld) <= 0."
+ "Cannot create CVPixelBufferPool with no kCVPixelBufferHeightKey."
+ "Cannot create CVPixelBufferPool with no kCVPixelBufferPixelFormatTypeKey."
+ "Cannot create CVPixelBufferPool with no kCVPixelBufferWidthKey."
+ "Invalid CVCustomMemoryLayoutCallBacks version (%lld)."
+ "Invalid CVCustomMemoryLayoutCallBacks."
- " (IOSurface ID 0x%x (%s))"

```
