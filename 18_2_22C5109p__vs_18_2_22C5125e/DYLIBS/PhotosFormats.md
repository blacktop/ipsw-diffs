## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0xc6a10
-  __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0x9c24
+720.4.101.0.0
+  __TEXT.__text: 0xc6ed8
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_methlist: 0x9c2c
   __TEXT.__const: 0x2d50
-  __TEXT.__gcc_except_tab: 0x30c8
-  __TEXT.__cstring: 0xc785
-  __TEXT.__oslogstring: 0x6db8
+  __TEXT.__gcc_except_tab: 0x30f8
+  __TEXT.__cstring: 0xc7c8
+  __TEXT.__oslogstring: 0x6ed3
   __TEXT.__dlopen_cstrs: 0x1a4
-  __TEXT.__unwind_info: 0x2eb8
+  __TEXT.__unwind_info: 0x2ed8
   __TEXT.__objc_classname: 0x125e
-  __TEXT.__objc_methname: 0x1a12f
+  __TEXT.__objc_methname: 0x1a18c
   __TEXT.__objc_methtype: 0x4de0
-  __TEXT.__objc_stubs: 0xfba0
-  __DATA_CONST.__got: 0x1460
-  __DATA_CONST.__const: 0x27d0
+  __TEXT.__objc_stubs: 0xfbe0
+  __DATA_CONST.__got: 0x1470
+  __DATA_CONST.__const: 0x27f8
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5740
+  __DATA_CONST.__objc_selrefs: 0x5750
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x7e0
-  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH_CONST.__auth_got: 0xed8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x19b0
-  __AUTH_CONST.__cfstring: 0xb9e0
+  __AUTH_CONST.__cfstring: 0xba00
   __AUTH_CONST.__objc_const: 0x13c48
   __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_arrayobj: 0x330

   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xafc
   __DATA.__data: 0xe18
-  __DATA.__bss: 0x868
-  __DATA.__common: 0x8
+  __DATA.__bss: 0x808
   __DATA_DIRTY.__objc_data: 0x2cb0
-  __DATA_DIRTY.__bss: 0xac8
-  __DATA_DIRTY.__common: 0x8
+  __DATA_DIRTY.__bss: 0xb08
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4246
-  Symbols:   5987
-  CStrings:  7173
+  Functions: 4248
+  Symbols:   5992
+  CStrings:  7178
 
Symbols:
+ _AVSmartStyleSettingsGetSystemStyle
+ _AVSmartStyleSettingsSystemStyle
+ _PFFigCopyImageDataToURLWithUpdatedProperties
+ _PFFigGetImageSourceImageIndexForContainerItemID
+ _PFUserHasSetSmartStyle
+ _kCGImagePropertyHEIFContainerItemID
+ _kCGImageSourceAddHEIFContainerItemID
+ _kCMPhotoCompressionContainerDescription_ItemID
- _PFFigCopyImageDataWithProperties
- _PFFigCopyImageFileWithProperties
- _kCMPhotoCompressionContainerDescription_PrimaryImageHandle
- _kCMPhotoCompressionContainerOption_StripExistingMetadata
CStrings:
+ "/AppleInternal/Library/BuildRoots/ced2dcaf-948d-11ef-b50f-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "Error trying to read asset bundle at %!@(MISSING) (manifestFound: %!@(MISSING), metadataFound: %!@(MISSING), validMetadataVersion: %!@(MISSING)"
+ "IgnoreUnsupportedJPEGAuxiliaryImages"
+ "Image source image entries do not contain container item IDs, ensure the image source properties were copied with the kCGImageSourceAddHEIFContainerItemID option"
+ "Multi-image image source properties for source %!@(MISSING) do not contain file contents > images list, unable to map from CMPhoto to ImageIO indexes: %!@(MISSING)"
+ "stringByRemovingImageIoDotSuffixFromString:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
- "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "Invalid primary image index %!t(MISSING)d in container description, image count = %!t(MISSING)d"
- "Unexpected missing %!@(MISSING) key in container description"

```
