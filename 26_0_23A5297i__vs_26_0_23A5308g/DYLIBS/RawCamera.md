## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

```diff

-1755.0.0.0.1
-  __TEXT.__text: 0x1db0e0
-  __TEXT.__auth_stubs: 0x1780
+1755.0.0.0.2
+  __TEXT.__text: 0x1db3d0
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__objc_methlist: 0x16e4
   __TEXT.__const: 0x14956
-  __TEXT.__gcc_except_tab: 0x2ca2c
+  __TEXT.__gcc_except_tab: 0x2cad8
   __TEXT.__oslogstring: 0xec0
   __TEXT.__cstring: 0xebee
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xb1e0
+  __TEXT.__unwind_info: 0xb1f8
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x4b9
   __TEXT.__objc_methname: 0x3755
   __TEXT.__objc_methtype: 0xbed
   __TEXT.__objc_stubs: 0x2d80
-  __DATA_CONST.__got: 0x9c0
+  __DATA_CONST.__got: 0x9d0
   __DATA_CONST.__const: 0x29b0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcf0
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x3978
-  __AUTH_CONST.__auth_got: 0xbd8
+  __DATA_CONST.__objc_arraydata: 0x3980
+  __AUTH_CONST.__auth_got: 0xbe8
   __AUTH_CONST.__const: 0x35900
   __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x48b0
-  __AUTH_CONST.__objc_arrayobj: 0x570
-  __AUTH_CONST.__objc_intobj: 0x39f0
+  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__objc_intobj: 0x3a20
   __AUTH_CONST.__objc_doubleobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x4d58
   __AUTH_CONST.__objc_floatobj: 0xc0

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG
   - /System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL
+  - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E71E54B1-5C01-3042-B202-331867BD6497
-  Functions: 6445
-  Symbols:   770
+  UUID: 81F83CC9-306C-3BA5-9785-93372D9ED08D
+  Functions: 6447
+  Symbols:   774
   CStrings:  7479
 
Symbols:
+ _CMPhotoDecompressionContainerCreateImageForIndex
+ _CMPhotoDecompressionContainerGetImageCount
+ _CMPhotoDecompressionSessionCreate
+ _CMPhotoDecompressionSessionCreateContainer
+ _CVPixelBufferGetDataSize
+ _kCMPhotoContainerFormatString_JFIF
+ _kCMPhotoDecompressionContainerOption_AllowedFormatsAndCodecs
+ _kCMPhotoDecompressionOption_OutputPixelFormat
- _CGImageGetBytesPerRow
- _CGImageGetHeight
- _CGImageGetWidth
- _xmlFree

```
