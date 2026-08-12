## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-540.1.0.0.0
-  __TEXT.__text: 0x6f68c
-  __TEXT.__objc_methlist: 0x9a78
+542.7.0.0.0
+  __TEXT.__text: 0x704bc
+  __TEXT.__objc_methlist: 0x9ac8
   __TEXT.__const: 0x552
-  __TEXT.__cstring: 0x5a26
-  __TEXT.__oslogstring: 0x34d6
+  __TEXT.__cstring: 0x5a76
+  __TEXT.__oslogstring: 0x36d6
   __TEXT.__gcc_except_tab: 0x9bc
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f70
+  __TEXT.__unwind_info: 0x1f98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4368
+  __DATA_CONST.__objc_selrefs: 0x43b8
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x348
-  __DATA_CONST.__got: 0x860
+  __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x5680
-  __AUTH_CONST.__objc_const: 0x21510
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x215a0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xa38
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x2050
   __DATA.__bss: 0x590
   __DATA.__common: 0x18

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3382
-  Symbols:   7883
-  CStrings:  1094
+  Functions: 3402
+  Symbols:   7939
+  CStrings:  1108
 
Symbols:
+ -[CPImageSet _iosurfaceFromImage:]
+ -[CPImageSet darkIOSurface]
+ -[CPImageSet darkPixelHash]
+ -[CPImageSet lightIOSurface]
+ -[CPImageSet lightPixelHash]
+ -[CPImageSet setDarkIOSurface:]
+ -[CPImageSet setDarkPixelHash:]
+ -[CPImageSet setLightIOSurface:]
+ -[CPImageSet setLightPixelHash:]
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CFDataGetBytePtr
+ _CFRelease
+ _CFRetain
+ _CGBitmapContextCreate
+ _CGColorSpaceCreateDeviceRGB
+ _CGColorSpaceRelease
+ _CGContextDrawImage
+ _CGContextRelease
+ _CGDataProviderCopyData
+ _CGImageGetBitsPerPixel
+ _CGImageGetBytesPerRow
+ _CGImageGetDataProvider
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _CGImageRelease
+ _CPImageFromIOSurface
+ _CPPixelHashForIOSurface
+ _CPPixelHashForImage
+ _CVPixelBufferCreate
+ _CVPixelBufferGetBaseAddress
+ _CVPixelBufferGetBytesPerRow
+ _CVPixelBufferGetIOSurface
+ _CVPixelBufferLockBaseAddress
+ _CVPixelBufferRelease
+ _CVPixelBufferUnlockBaseAddress
+ _IOSurfaceGetBaseAddress
+ _IOSurfaceGetBytesPerElement
+ _IOSurfaceGetBytesPerRow
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
+ _IOSurfaceLock
+ _IOSurfaceUnlock
+ _OBJC_IVAR_$_CPImageSet._darkIOSurface
+ _OBJC_IVAR_$_CPImageSet._darkPixelHash
+ _OBJC_IVAR_$_CPImageSet._lightIOSurface
+ _OBJC_IVAR_$_CPImageSet._lightPixelHash
+ _UICreateCGImageFromIOSurface
+ _kCFAllocatorDefault
+ _kCVPixelBufferCGBitmapContextCompatibilityKey
+ _kCVPixelBufferCGImageCompatibilityKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _objc_msgSend$CGImage
+ _objc_msgSend$_initWithIOSurface:scale:orientation:
+ _objc_msgSend$_iosurfaceFromImage:
+ _objc_msgSend$darkData
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$lightData
- -[CPImageSet computedHashAtInitialization]
- -[CPImageSet setComputedHashAtInitialization:]
- _OBJC_IVAR_$_CPImageSet._computedHashAtInitialization
CStrings:
+ "\t"
+ "CPImageSet: Failed to create CGContext for pixel buffer"
+ "CPImageSet: Failed to create CVPixelBuffer: %d"
+ "CPImageSet: Failed to get IOSurface from CVPixelBuffer"
+ "CPImageSet: both IOSurface and PNG data absent or unreadable; images will be nil"
+ "CPImageSet: encoding via PNG fallback (light surface=%@, dark surface=%@)"
+ "CPImageSet: image has no CGImage"
+ "CPImageSet: only one IOSurface decoded (light=%@, dark=%@); using available surface for both"
+ "CPImageSet: only one PNG decoded (light=%@, dark=%@); using available image for both"
+ "IOSurface"
+ "kCPDarkContentIOSurfaceKey"
+ "kCPLightContentIOSurfaceKey"
+ "nil"
+ "ok"
```
