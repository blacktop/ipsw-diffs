## com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x22f58
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_stubs: 0x6120
+720.4.101.0.0
+  __TEXT.__text: 0x22c84
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_stubs: 0x6100
   __TEXT.__objc_methlist: 0x1e6c
-  __TEXT.__const: 0x180
+  __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0xa78
-  __TEXT.__cstring: 0x2f52
+  __TEXT.__cstring: 0x2f66
   __TEXT.__objc_classname: 0x5a7
-  __TEXT.__objc_methname: 0x7dde
-  __TEXT.__objc_methtype: 0xd99
-  __TEXT.__oslogstring: 0x2e4b
+  __TEXT.__objc_methname: 0x7dd1
+  __TEXT.__objc_methtype: 0xd67
+  __TEXT.__oslogstring: 0x2e91
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__unwind_info: 0x820
-  __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x8c0
-  __DATA_CONST.__const: 0xa80
-  __DATA_CONST.__cfstring: 0x2480
+  __TEXT.__unwind_info: 0x828
+  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__cfstring: 0x2460
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x3530
-  __DATA.__objc_selrefs: 0x1c68
+  __DATA.__objc_selrefs: 0x1c60
   __DATA.__objc_ivar: 0x238
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x360

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 702
-  Symbols:   458
-  CStrings:  1910
+  Functions: 703
+  Symbols:   448
+  CStrings:  1908
 
Symbols:
+ _PFFigGetImageSourceImageIndexForContainerItemID
+ _kCGImageSourceAddHEIFContainerItemID
- _com_apple_photos_VideoConversionServiceVersionNumber
- _com_apple_photos_VideoConversionServiceVersionString
- _kCGImageDestinationMergeMetadata
- _kCGImagePropertyGroupImageDisparityAdjustment
- _kCGImagePropertyGroupImageIndexLeft
- _kCGImagePropertyGroupImageIndexRight
- _kCGImagePropertyGroupImageIsLeftImage
- _kCGImagePropertyGroupImageIsRightImage
- _kCGImagePropertyGroupIndex
- _kCGImagePropertyGroupType
- _kCGImagePropertyGroupTypeStereoPair
- _kCGImagePropertyGroups
CStrings:
+ "@\"NSDictionary\"16@?0@8"
+ "Output image at index %!t(MISSING)u is missing image property '%!{(MISSING)public}@' present in input image"
+ "Unable to create an image source from Fig outputData %!p(MISSING) of length %!t(MISSING)u to inspect for missing metadata properties."
+ "Unable to perform single image JPEG passthrough conversion for source %!@(MISSING)"
+ "Unexpected input (%!t(MISSING)u) / output (%!t(MISSING)u) image count mismatch"
+ "dataForSingleImageJPEGPassthroughConversionForImageSource:primaryImageProperties:"
+ "logMissingPropertiesInCMPhotoOutputData:comparedToProcessedSourceImagePropertiesByIndex:"
- ", "
- "@32@0:8Q16@24"
- "@48@0:8@16^{CGImageSource=}24Q32@40"
- "Adding metadata properties missed by Fig: [%!{(MISSING)public}@]"
- "Unable to apply metadata properties missed by Fig during passthrough conversion for %!@(MISSING)."
- "Unable to create an image source from Fig outputData (%!{(MISSING)public}@) to inspect for adding any missing metadata properties."
- "imageDataByAddingMissingPrimaryImageProperties:toImageDataSource:primaryImageIndex:inputImagePropertiesByIndex:"
- "stereoGroupInfoForImageIndex:containerImageGroups:"
- "unsignedIntegerValue"

```
