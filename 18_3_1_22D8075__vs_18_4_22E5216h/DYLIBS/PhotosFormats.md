## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-742.0.141.0.0
-  __TEXT.__text: 0xc6ee0
-  __TEXT.__auth_stubs: 0x1d80
-  __TEXT.__objc_methlist: 0x9c3c
-  __TEXT.__const: 0x2d50
-  __TEXT.__gcc_except_tab: 0x30f8
-  __TEXT.__cstring: 0xc7c8
-  __TEXT.__oslogstring: 0x6ed3
+750.11.101.0.0
+  __TEXT.__text: 0xc2b50
+  __TEXT.__auth_stubs: 0x1cb0
+  __TEXT.__objc_methlist: 0xaed8
+  __TEXT.__const: 0x2ce0
   __TEXT.__dlopen_cstrs: 0x1a4
-  __TEXT.__unwind_info: 0x2ed8
+  __TEXT.__gcc_except_tab: 0x3030
+  __TEXT.__cstring: 0xc4cd
+  __TEXT.__oslogstring: 0x6855
+  __TEXT.__unwind_info: 0x2ea0
   __TEXT.__objc_classname: 0x125e
-  __TEXT.__objc_methname: 0x1a1d3
+  __TEXT.__objc_methname: 0x1a223
   __TEXT.__objc_methtype: 0x4de0
-  __TEXT.__objc_stubs: 0xfc00
-  __DATA_CONST.__got: 0x1470
-  __DATA_CONST.__const: 0x27f8
+  __TEXT.__objc_stubs: 0xfc40
+  __DATA_CONST.__got: 0x1440
+  __DATA_CONST.__const: 0x27e0
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5760
+  __DATA_CONST.__objc_selrefs: 0x5820
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x7e0
-  __AUTH_CONST.__auth_got: 0xed8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x19b0
-  __AUTH_CONST.__cfstring: 0xba00
-  __AUTH_CONST.__objc_const: 0x13c48
+  __AUTH_CONST.__auth_got: 0xe70
+  __AUTH_CONST.__const: 0x1990
+  __AUTH_CONST.__cfstring: 0xba40
+  __AUTH_CONST.__objc_const: 0x11918
   __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_arrayobj: 0x330
   __AUTH_CONST.__objc_doubleobj: 0x1a0

   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xafc
   __DATA.__data: 0xe18
-  __DATA.__bss: 0x808
+  __DATA.__bss: 0x7e8
   __DATA_DIRTY.__objc_data: 0x2cb0
-  __DATA_DIRTY.__bss: 0xb08
+  __DATA_DIRTY.__bss: 0xb20
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4249
-  Symbols:   5993
-  CStrings:  7180
+  Functions: 4223
+  Symbols:   5965
+  CStrings:  7146
 
Symbols:
+ _CMPhotoComputeSSIMForPixelBuffer
+ _PFAppleArchiveEncryptedExtension
+ _PFAppleArchiveExtension
- _CFArrayGetCount
- _CFArrayGetTypeID
- _CFDictionaryGetValueIfPresent
- _CFGetAllocator
- _CFNumberCreate
- _CFNumberGetTypeID
- _CFNumberGetValue
- _CMPhotoSurfacePoolCreatePixelBuffer
- _CVBufferCopyAttachment
- _CVBufferSetAttachment
- _CVPixelBufferGetBaseAddressOfPlane
- _CVPixelBufferGetBytesPerRowOfPlane
- ___chkstk_darwin
- __dispatch_queue_attr_concurrent
- _dispatch_barrier_sync
- _kCMFormatDescriptionKey_CleanApertureHeightRational
- _kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational
- _kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational
- _kCMFormatDescriptionKey_CleanApertureWidthRational
- _kCMPhotoSurfacePoolOneShot
- _strcmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "Unable to open decryption input stream"
+ "aar"
+ "aea"
+ "decodeContentsToDirectoryURL:error:"
+ "setPreparesMediaDataForRealTimeConsumption:"
- "/AppleInternal/Library/BuildRoots/e2bbd88f-cdb1-11ef-a003-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "Boolean _floatFromRational(CFArrayRef, CGFloat *)"
- "ERROR: Unable to read num/den from rational array"
- "Failed condition 'CFArrayGetCount(ratArray) == 2', bailing from %s"
- "Failed condition 'CGRectContainsRect(currentTopLeftRect, topLeftRect)', bailing from %s"
- "Failed condition 'CVPixelBufferGetHeight(pbufA) == CVPixelBufferGetHeight(pbufB)', bailing from %s"
- "Failed condition 'CVPixelBufferGetWidth(pbufA) == CVPixelBufferGetWidth(pbufB)', bailing from %s"
- "Failed condition 'FigCFIsTypeOf(ratArray, CFArray)', bailing from %s"
- "Failed condition 'FigPhotoSizeIsEqual(clapA.size, clapB.size)', bailing from %s"
- "Failed condition 'FigPhotoSizeIsEqual(clapW.size, clapA.size)', bailing from %s"
- "Failed condition 'cropRect.origin.x < rect->size.width', bailing from %s"
- "Failed condition 'cropRect.origin.y < rect->size.height', bailing from %s"
- "Failed condition 'cropRect.size.height <= rect->size.height - cropRect.origin.y', bailing from %s"
- "Failed condition 'cropRect.size.width <= rect->size.width - cropRect.origin.x', bailing from %s"
- "Failed condition 'dict', bailing from %s"
- "Failed condition 'key', bailing from %s"
- "Failed condition 'number', bailing from %s"
- "Failed condition 'pixelBuffer != NULL', bailing from %s"
- "Failed condition 'queue', bailing from %s"
- "Invalid edge index: %d"
- "OSStatus FigPhotoApplyCropRectToRect(CGRect *, CGRect)"
- "OSStatus FigPhotoCreatePixelBufferCLAPDictionaryFromRect(CFAllocatorRef, CGSize, CGRect, CFDictionaryRef *)"
- "OSStatus FigPhotoSetPixelBufferCLAPFromRect(CVPixelBufferRef, CGRect, Boolean, Boolean)"
- "OSStatus _cfDictionarySetNumber(CFMutableDictionaryRef, CFStringRef, CFNumberType, void *)"
- "OSStatus _computeSSIMForBGRA(CVPixelBufferRef, CGRect, CVPixelBufferRef, CGRect, CVPixelBufferRef, int, double *)"
- "Unexpected error %ld, bailing from %s"
- "Unsupported pixel format for SSIM computation"
- "Warning: Unable to convert rational values from CLAP dictionary to floating point"
- "_computeSSIMForBGRA - clapA and clapB not the same"
- "_computeSSIMForBGRA - heightA and heightB not the same"
- "_computeSSIMForBGRA - widthA and widthB not the same"
- "com.apple.coremedia.psnr"
- "failed to create clap dictionary"
- "invalid index"
- "new top-left CLAP rect is too big to fit in existing rect"
- "not an array"
- "pixelBuffer not specified"
- "void PFImageMetricComputeSSIMForPixelBuffer(CVPixelBufferRef, CVPixelBufferRef, CGRect, CVPixelBufferRef, _Bool, double *, double *, double *)"
- "void _computeSSIMForPlane(CVPixelBufferRef, CGRect, CVPixelBufferRef, CGRect, CVPixelBufferRef, int, double *)"

```
