## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0xd6824
+912.0.111.0.0
+  __TEXT.__text: 0xd6810
   __TEXT.__objc_methlist: 0xc8b8
   __TEXT.__const: 0x2db0
   __TEXT.__dlopen_cstrs: 0x1b7

   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
+  - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib
Functions:
~ -[PFPosterDynamicDeviceConfiguration initWithCoder:] : 624 -> 660
~ +[PFParallaxLayoutConfiguration configurationForScreenSize:screenScale:determinedConfiguration:orientation:] : 640 -> 600
~ -[PFPosterOrientedLayout layoutByUpdatingImageSize:] : 1724 -> 1708
```
