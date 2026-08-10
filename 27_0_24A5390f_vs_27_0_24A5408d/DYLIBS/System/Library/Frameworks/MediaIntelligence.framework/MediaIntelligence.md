## MediaIntelligence

> `/System/Library/Frameworks/MediaIntelligence.framework/MediaIntelligence`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__cstring`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__AUTH.__objc_data`

```diff

-435.73.2.0.0
-  __TEXT.__text: 0x19854
+435.79.1.4.0
+  __TEXT.__text: 0x19a68
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x1788
-  __TEXT.__constg_swiftt: 0x9f8
-  __TEXT.__swift5_typeref: 0x892
-  __TEXT.__swift5_fieldmd: 0x67c
+  __TEXT.__const: 0x1780
+  __TEXT.__constg_swiftt: 0x9f0
+  __TEXT.__swift5_typeref: 0x8a6
+  __TEXT.__swift5_fieldmd: 0x694
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x333
+  __TEXT.__swift5_reflstr: 0x343
   __TEXT.__swift5_assocty: 0x2a0
   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__oslogstring: 0x524
+  __TEXT.__oslogstring: 0x4f4
   __TEXT.__cstring: 0x383
-  __TEXT.__swift5_capture: 0x74
+  __TEXT.__swift5_capture: 0x94
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x5c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5c0
-  __TEXT.__eh_frame: 0xa58
+  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__eh_frame: 0xa88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xa8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x260
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__objc_const: 0x450
+  __AUTH_CONST.__const: 0x10a0
+  __AUTH_CONST.__objc_const: 0x490
   __AUTH_CONST.__auth_got: 0x818
   __AUTH.__objc_data: 0x1a0
-  __AUTH.__data: 0x700
-  __DATA.__data: 0x470
+  __AUTH.__data: 0x708
+  __DATA.__data: 0x480
   __DATA.__bss: 0x1e00
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
-  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Vision.framework/Vision

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 546
-  Symbols:   552
-  CStrings:  50
+  Functions: 559
+  Symbols:   555
+  CStrings:  49
 
Symbols:
+ _CGImageDestinationAddImage
+ _CGImageDestinationCreateWithData
+ _CGImageDestinationFinalize
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_VNSession
+ _kCGImageDestinationImageMaxPixelSize
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImageDestinationOptimizeColorForSharing
+ _objc_msgSend$initWithURL:options:session:
+ _objc_msgSend$performBlockAndWait:
+ _objc_retain_x27
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x1
+ _swift_retain_x19
+ _swift_retain_x23
+ _swift_retain_x26
+ _symbolic Igh_
+ _symbolic So9VNSessionC
- _CGBitmapContextCreate
- _CGColorSpaceCreateDeviceRGB
- _CGContextSetInterpolationQuality
- _CVPixelBufferCreate
- _CVPixelBufferGetBaseAddress
- _CVPixelBufferGetBytesPerRow
- _CVPixelBufferGetDataSize
- _CVPixelBufferLockBaseAddress
- _CVPixelBufferUnlockBaseAddress
- ___CGBitmapContextCreate
- _kCFAllocatorDefault
- _kCVPixelBufferCGBitmapContextCompatibilityKey
- _kCVPixelBufferCGImageCompatibilityKey
- _kCVPixelBufferIOSurfacePropertiesKey
- _objc_msgSend$initWithURL:options:
CStrings:
+ "Failed to create image destination for face crop"
+ "Failed to finalize face crop encoding"
- "Failed to create CGContext for pixel buffer"
- "Failed to create CVPixelBuffer"
- "Scaling down face crop from %{public}fpx max side with factor %{public}f"
```
