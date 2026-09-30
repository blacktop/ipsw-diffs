## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2622.0.1.0.0
-  __TEXT.__text: 0x3f6d78
-  __TEXT.__auth_stubs: 0x3fc0
-  __TEXT.__objc_methlist: 0x920
-  __TEXT.__gcc_except_tab: 0x1edb0
-  __TEXT.__const: 0x31438
-  __TEXT.__cstring: 0x78dfa
+2632.0.0.0.0
+  __TEXT.__text: 0x3f6d24
+  __TEXT.__auth_stubs: 0x3f80
+  __TEXT.__objc_methlist: 0x928
+  __TEXT.__gcc_except_tab: 0x1eeac
+  __TEXT.__const: 0x31428
+  __TEXT.__cstring: 0x78fbe
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0xd140
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x28c1
+  __TEXT.__objc_methname: 0x290a
   __TEXT.__objc_methtype: 0x1c6f
-  __TEXT.__objc_stubs: 0x2140
-  __DATA_CONST.__got: 0x5c8
+  __TEXT.__objc_stubs: 0x21e0
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0xf4b0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_selrefs: 0x918
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1ff8
+  __AUTH_CONST.__auth_got: 0x1fd8
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3c830
-  __AUTH_CONST.__cfstring: 0xda40
+  __AUTH_CONST.__const: 0x3c978
+  __AUTH_CONST.__cfstring: 0xd920
   __AUTH_CONST.__objc_const: 0x1248
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10

   __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x2c88
-  __DATA.__bss: 0x5370
-  __DATA.__common: 0x1f10
-  __DATA_DIRTY.__data: 0x178
+  __DATA.__data: 0x2bb8
+  __DATA.__bss: 0x5340
+  __DATA.__common: 0x1ee8
+  __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__common: 0xccb
-  __DATA_DIRTY.__bss: 0x6a8
+  __DATA_DIRTY.__common: 0xd03
+  __DATA_DIRTY.__bss: 0x6c8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13077
-  Symbols:   15442
-  CStrings:  12462
+  Functions: 13063
+  Symbols:   15431
+  CStrings:  12473
 
Symbols:
+ _kCGImagePropertyHEIFContainerItemID
+ _kCGImageSourceAddHEIFContainerItemID
+ _kCGImageSourceTiledDownsamplingMode
- _AnalyticsSendEventLazy
- ___kCFBooleanFalse
- _objc_release_x9
- _rootless_check_trusted
- _srandom
CStrings:
+ "    CMPhotoDetermineMIAFCompliantThumbnailMaxPixelSize: [session:%!p(MISSING)] size:%!u(MISSING) err:%!d(MISSING)\n"
+ "*** ERROR: CGImageSetHeadroom: %!f(MISSING) failed for image with %!s(MISSING) color space\n"
+ "*** ERROR: CGImageSetHeadroom: %!f(MISSING) failed for image with unnamed color space\n"
+ "*** ERROR: pluginUTI '%!s(MISSING)' does not match reader '%!s(MISSING)'\n"
+ "*** Gray - invalid bitsPerPixel [%!d(MISSING)]\n"
+ "*** ImageIO OOP %!s(MISSING) (%!s(MISSING)%!s(MISSING))\n"
+ "*** Indexed - invalid bitsPerPixel [%!d(MISSING)]\n"
+ "*** NOTE: CGImage with mask will be converted from %!d(MISSING)bpc to 8bpc\n"
+ "*** NOTE: dropping 'kCGImageSourceDecodeRequest' since 'kCGImageSourceIgnoreJPEGAuxImages' was requested\n"
+ "*** RGB - invalid bitsPerPixel [%!d(MISSING)]\n"
+ "-[HDRImageConverter_Metal commitAndWaitUntilCompleted:]_block_invoke"
+ "AmbientIlluminance"
+ "AmbientLightX"
+ "AmbientLightY"
+ "AmbientViewingEnvironment"
+ "B&I environment"
+ "CMPhotoDetermineMIAFCompliantThumbnailMaxPixelSize"
+ "ContainerItemID"
+ "ContentLightLevelInfo"
+ "DisplayPrimariesXB"
+ "DisplayPrimariesXG"
+ "DisplayPrimariesXR"
+ "DisplayPrimariesYB"
+ "DisplayPrimariesYG"
+ "DisplayPrimariesYR"
+ "IIOImageCreateWithImageAndMaskInterleaved"
+ "MasteringDisplayColorVolume"
+ "MaxContentLightLevel"
+ "MaxDisplayMasteringLuminance"
+ "MaxPicAverageLightLevel"
+ "MinDisplayMasteringLuminance"
+ "WhitePointX"
+ "WhitePointY"
+ "addCompletedHandler:"
+ "com.apple.SubcredentialUIService.SubcredentialInvitationMessagesExtension"
+ "com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension"
+ "com.apple.icloud.apps.messages.business.extension"
+ "commitAndWaitUntilCompleted:"
+ "disabled for "
+ "disabled for 3rd party app "
+ "env"
+ "error"
+ "ff"
+ "iMessageAppExtension"
+ "kCGImageSourceAddHEIFContainerItemID"
+ "kCGImageSourceTiledDownsamplingMode"
+ "kCMPhotoDecompressionContainerDescription_ItemID"
+ "kVTParavirtualizationTimeoutErr"
+ "not supported on this platform"
+ "permanently disabled for 3rd party app "
+ "setBackgroundGPUPriority:"
+ "status"
+ "temporary disabled for "
+ "v16@?0@\"<MTLCommandBuffer>\"8"
+ "••• ❓ UseHardwareAcceleration(%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING))  | %!s(MISSING):%!d(MISSING)\n"
+ "☀️ CommandBuffer %!p(MISSING) failed '%!s(MISSING)'"
+ "❌  failed to load 'CMPhotoDetermineMIAFCompliantThumbnailMaxPixelSize' "
+ "❌  failed to load 'kCMPhotoDecompressionContainerDescription_ItemID' "
- "*** ImageIO OOP %!s(MISSING) (env)\n"
- "*** ImageIO OOP diabled for B&I\n"
- "*** ImageIO OOP disabled (ff)\n"
- "*** ImageIO OOP disabled for '%!s(MISSING)'\n"
- "*** ImageIO OOP disabled for 3rd party app: '%!s(MISSING)'\n"
- "*** ImageIO OOP enabled\n"
- "*** ImageIO OOP not supported on this platform\n"
- "*** ImageIO OOP permanently disabled for 3rd party app: '%!s(MISSING)'\n"
- "*** ImageIO OOP temporary disabled for '%!s(MISSING)'\n"
- "*** invalid bitsPerPixel [%!d(MISSING)]\n"
- "@\"NSDictionary\"8@?0"
- "WidgetRenderer_Default"
- "bundleID"
- "com.apple"
- "com.apple.ImageIO.CGCopyIOSurface"
- "com.apple.ImageIO.CGCopyIOSurfaceSet"
- "com.apple.ImageIO.CGCopyImageBlockSetWithOptions"
- "com.apple.ImageIO.CGCopyImageTextureData"
- "com.apple.ImageIO.CGImageSourceCopyAuxiliaryDataInfoAtIndex"
- "com.apple.ImageIO.CGImageSourceCopyMetadataAtIndex"
- "com.apple.ImageIO.CGImageSourceCopyMetadataPropertiesAtIndex"
- "com.apple.ImageIO.CGImageSourceCopyProperties"
- "com.apple.ImageIO.CGImageSourceCopyPropertiesAtIndex"
- "com.apple.ImageIO.CGImageSourceCreateIOSurfaceAtIndex"
- "com.apple.ImageIO.CGImageSourceCreateImageAtIndex"
- "com.apple.ImageIO.CGImageSourceCreateIncremental"
- "com.apple.ImageIO.CGImageSourceCreateThumbnailAtIndex"
- "com.apple.ImageIO.CGImageSourceCreateWithData"
- "com.apple.ImageIO.CGImageSourceCreateWithDataProvider"
- "com.apple.ImageIO.CGImageSourceCreateWithURL"
- "com.apple.ImageIO.CGImageSourceGetCount"
- "com.apple.analyticsd"
- "com.apple.macpaint-image"
- "com.apple.pict"
- "com.sgi.sgi-image"
- "eventName"
- "fileFormat"
- "hw.memsize"
- "index"
- "isTrustedURL"
- "kCGImageHeadroom"
- "mach-lookup"
- "no-bundleID"
- "numberWithLong:"
- "public.svg"
- "public.xbitmap-image"
- "unknownFormat"

```
