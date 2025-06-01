## PhotosFileProvider

> `/Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/PhotosFileProvider`

```diff

-608.1.119.0.0
-  __TEXT.__text: 0x339c
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x8
-  __TEXT.__objc_methname: 0xd0d
-  __TEXT.__oslogstring: 0x70d
-  __TEXT.__cstring: 0x2b8
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0xcc
-  __TEXT.__unwind_info: 0xcc
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__cfstring: 0x2c0
+612.0.160.0.0
+  __TEXT.__text: 0x3a34
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x184
+  __TEXT.__const: 0x10
+  __TEXT.__objc_methname: 0xe01
+  __TEXT.__oslogstring: 0x73d
+  __TEXT.__cstring: 0x2f6
+  __TEXT.__objc_classname: 0x44
+  __TEXT.__objc_methtype: 0xe8
+  __TEXT.__unwind_info: 0xd4
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x370
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_classrefs: 0xe0
+  __DATA.__objc_const: 0x3a0
+  __DATA.__objc_selrefs: 0x3a0
+  __DATA.__objc_classrefs: 0xf0
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics

   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41A35363-DA7E-3B63-8683-564746FC92BE
-  Functions: 36
-  Symbols:   107
-  CStrings:  236
+  UUID: C648ACE8-7CBB-3F1D-83DE-3722D6DACF1D
+  Functions: 41
+  Symbols:   116
+  CStrings:  249
 
Symbols:
+ _CFRelease
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithURL
+ _CGImageDestinationFinalize
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_PHImageManager
+ _OBJC_CLASS_$_PHImageRequestOptions
+ _PHImageErrorKey
+ _PXPhotosFileProviderURLQueryItemThumbnailSizeKey
+ _UTTypeJPEG
+ _objc_retain_x9
- _objc_retain_x24
- _objc_retain_x27
CStrings:
+ "\x12\"\x11"
+ "Failed to saved file to URL (%@) with error: %@"
+ "Failed to write image ref"
+ "Tq,R,N,V_thumbnailSize"
+ "_markURLAsPurgable:completionHandler:"
+ "_saveImageRef:toURL:completionHandler:"
+ "_thumbnailSize"
+ "requestNewCGImageForAsset:targetSize:contentMode:options:resultHandler:"
+ "setDeliveryMode:"
+ "setNetworkAccessAllowed:"
+ "thumbnailSize"
+ "v24@?0^{CGImage=}8@\"NSDictionary\"16"
+ "v40@0:8^{CGImage=}16@24@?32"
- "\x12#"

```
