## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

-1510.120.2.0.0
-  __TEXT.__text: 0xb48c
-  __TEXT.__auth_stubs: 0x600
+1566.0.0.0.0
+  __TEXT.__text: 0xadf0
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x15e0
-  __TEXT.__cstring: 0x196e
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x1568
+  __TEXT.__cstring: 0x1854
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x1262
   __TEXT.__objc_methtype: 0x24a
   __TEXT.__oslogstring: 0x6c6
-  __TEXT.__dlopen_cstrs: 0x91
+  __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__cfstring: 0xc80
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x110
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 876FB57F-D83E-392F-8D37-6A231B2377F8
-  Functions: 174
+  UUID: ED819698-043B-300B-A513-C52EFC20FBAE
+  Functions: 167
   Symbols:   163
-  CStrings:  529
+  CStrings:  517
 
Symbols:
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_MLModelConfiguration
- _objc_getClass
- _objc_retain_x9
CStrings:
- "Class getMLModelClass()_block_invoke"
- "Class getMLModelConfigurationClass()_block_invoke"
- "MLModel"
- "MLModelConfiguration"
- "Unable to find class %s"
- "bind:buffer: error=%s\n"
- "const char *soft_espresso_get_status_string(espresso_return_status_t)"
- "espresso_get_status_string"
- "softlink:r:path:/System/Library/Frameworks/CoreML.framework/CoreML"
- "void *CoreMLLibrary()"

```
