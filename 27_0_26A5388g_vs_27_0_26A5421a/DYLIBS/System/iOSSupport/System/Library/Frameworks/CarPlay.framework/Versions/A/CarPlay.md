## CarPlay

> `/System/iOSSupport/System/Library/Frameworks/CarPlay.framework/Versions/A/CarPlay`

```diff

-540.2.0.0.0
-  __TEXT.__text: 0x5cb50
-  __TEXT.__objc_methlist: 0x8fb0
+542.8.0.0.0
+  __TEXT.__text: 0x5d95c
+  __TEXT.__objc_methlist: 0x9000
   __TEXT.__const: 0x35a
-  __TEXT.__cstring: 0x52c6
-  __TEXT.__oslogstring: 0x221e
+  __TEXT.__cstring: 0x5306
+  __TEXT.__oslogstring: 0x242e
   __TEXT.__gcc_except_tab: 0x79c
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_typeref: 0x7f

   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1c18
+  __TEXT.__unwind_info: 0x1c40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c30
+  __DATA_CONST.__objc_selrefs: 0x3c80
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x340
-  __DATA_CONST.__got: 0x658
+  __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0x1f570
+  __AUTH_CONST.__cfstring: 0x5300
+  __AUTH_CONST.__objc_const: 0x1f600
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x9f8
+  __DATA.__objc_ivar: 0xa04
   __DATA.__data: 0x1940
   __DATA.__bss: 0x310
   __DATA.__common: 0x18

   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
+  - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3072
-  Symbols:   7084
-  CStrings:  941
+  Functions: 3092
+  Symbols:   7141
+  CStrings:  955
 
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
+ OBJC_IVAR_$_CPImageSet._darkIOSurface
+ OBJC_IVAR_$_CPImageSet._darkPixelHash
+ OBJC_IVAR_$_CPImageSet._lightIOSurface
+ OBJC_IVAR_$_CPImageSet._lightPixelHash
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
+ _UICreateCGImageFromIOSurface
+ ___kCFBooleanTrue
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
- OBJC_IVAR_$_CPImageSet._computedHashAtInitialization
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
