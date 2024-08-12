## AISAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AISAccountNotificationPlugin.bundle/AISAccountNotificationPlugin`

```diff

-45.1.0.0.0
-  __TEXT.__text: 0x341c
+48.1.1.0.0
+  __TEXT.__text: 0x32ec
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x62
   __TEXT.__cstring: 0x350
   __TEXT.__constg_swiftt: 0x88
-  __TEXT.__swift5_typeref: 0x75
+  __TEXT.__swift5_typeref: 0x73
   __TEXT.__swift5_reflstr: 0x35
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_capture: 0x60
   __TEXT.__oslogstring: 0x232
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x130
+  __TEXT.__unwind_info: 0x128
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methname: 0x2d4
   __TEXT.__objc_methtype: 0x1f3
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 56
-  Symbols:   93
-  CStrings:  0
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 55
+  Symbols:   101
+  CStrings:  66
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "BufferPlaneAlignmentKey"
+ "_FigCaptureCompressedPixelFormatForPixelFormat"
+ "_FigCapturePixelFormatBytesPerPixel"
+ "_FigCapturePixelFormatIs422"
+ "_FigCapturePixelFormatIsTenBit"
+ "_FigCapturePlatformChipRevisionIdentifier"
+ "_FigCapturePlatformIOSurfaceWiringAssertionEnabled"
+ "_FigCapturePlatformIdentifier"
+ "_FigCapturePlatformSupportsHTPC16x8Compression"
+ "_FigCapturePlatformSupportsUniversalCompression"
+ "_FigCapturePlatformSupportsUniversalLossyCompression"
+ "_FigCaptureStreamGetClassID"
+ "_FigCaptureStreamGetFigBaseObject"
+ "_FigCaptureUncompressedPixelFormatForPixelFormat"
+ "_FigCaptureVideoStabilizationStrengthToString"
+ "_kCVDataBufferIOSurfaceWiringAssertionKey"
+ "_kCVDataBufferPoolAllocationThresholdKey"
+ "_kCVDataBufferPoolMaximumBufferAgeKey"
+ "_kCVDataBufferPoolNameKey"
+ "_kCVPixelBufferCacheModeKey"
+ "_kCVPixelBufferCustomMemoryLayoutCallbacksKey"
+ "_kCVPixelBufferExactBytesPerRowKey"
+ "_kCVPixelBufferExtendedPixelsFilledKey"
+ "_kCVPixelBufferFixedPointInvalidValueKey"
+ "_kCVPixelBufferFixedPointOffsetKey"
+ "_kCVPixelBufferIOSurfaceCoreAnimationCompatibilityHTPCOKKey"
+ "_kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey"
+ "_kCVPixelBufferIOSurfacePropertiesKey"
+ "_kCVPixelBufferMetalCompatibilityKey"
+ "_kCVPixelBufferOpenGLESCompatibilityKey"
+ "_kCVPixelBufferOpenGLESTextureCacheCompatibilityKey"
+ "_kCVPixelBufferPixelFormatDescriptionKey"
+ "_kCVPixelBufferPoolAllocationThresholdKey"
+ "_kCVPixelBufferPoolNameKey"
+ "_kCVPixelBufferPoolRequireIOSurfaceWithoutWiringAssertionYetKey"
+ "_kCVPixelBufferPreferRealTimeCacheModeIfEveryoneDoesKey"
+ "_kCVPixelBufferProResRAWKey_BlackLevel"
+ "_kCVPixelBufferProResRAWKey_ColorMatrix"
+ "_kCVPixelBufferProResRAWKey_GainFactor"
+ "_kCVPixelBufferProResRAWKey_MetadataExtension"
+ "_kCVPixelBufferProResRAWKey_RecommendedCrop"
+ "_kCVPixelBufferProResRAWKey_SenselSitingOffsets"
+ "_kCVPixelBufferProResRAWKey_WhiteBalanceBlueFactor"
+ "_kCVPixelBufferProResRAWKey_WhiteBalanceCCT"
+ "_kCVPixelBufferProResRAWKey_WhiteBalanceRedFactor"
+ "_kCVPixelBufferProResRAWKey_WhiteLevel"
+ "_kCVPixelBufferQDCompatibilityKey"
+ "_kCVPixelBufferRotationKey"
+ "_kCVPixelBufferVersatileBayerKey_BayerPattern"
+ "_kCVPixelFormatBitsPerComponent"
+ "_kCVPixelFormatBytesPerCompressedTileHeader"
+ "_kCVPixelFormatComponentRange"
+ "_kCVPixelFormatComponentRange_FullRange"
+ "_kCVPixelFormatComponentRange_VideoRange"
+ "_kCVPixelFormatComponentRange_WideRange"
+ "_kCVPixelFormatCompressedTileHeight"
+ "_kCVPixelFormatCompressedTileWidth"
+ "_kCVPixelFormatCompressionType"
+ "_kCVPixelFormatContainsBayer"
+ "_kCVPixelFormatContainsGrayscale"
+ "_kCVPixelFormatContainsRGB"
+ "_kCVPixelFormatContainsSenselArray"
+ "_kCVPixelFormatContainsYCbCr"
+ "_kCVPixelFormatOpenGLESCompatibility"
+ "elFormatVerticalSubsampling"
+ "iceGetNotificationCenter"

```
