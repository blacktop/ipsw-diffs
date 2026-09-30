## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0xdd5dc
+911.0.134.0.0
+  __TEXT.__text: 0xdd5cc
   __TEXT.__objc_methlist: 0xc740
   __TEXT.__const: 0x2da0
   __TEXT.__dlopen_cstrs: 0x43

   - /System/Library/PrivateFrameworks/CMPhoto.framework/Versions/A/CMPhoto
   - /System/Library/PrivateFrameworks/MMCS.framework/Versions/A/MMCS
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/Versions/A/PhotoFoundation
+  - /System/Library/PrivateFrameworks/Portrait.framework/Versions/A/Portrait
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4844
-  Symbols:   11552
+  Symbols:   11553
   CStrings:  2532
 
Symbols:
+ _objc_msgSend$setSupportsLandscapeConfiguration:
Functions:
~ -[PFPosterDynamicDeviceConfiguration initWithCoder:] : 668 -> 708
~ +[PFParallaxLayoutConfiguration configurationForScreenSize:screenScale:determinedConfiguration:orientation:] : 640 -> 600
~ -[PFPosterOrientedLayout layoutByUpdatingImageSize:] : 1736 -> 1720
```
