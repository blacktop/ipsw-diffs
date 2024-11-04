## com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1ca2c
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x5280
+720.4.101.0.0
+  __TEXT.__text: 0x1c758
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_stubs: 0x5260
   __TEXT.__objc_methlist: 0x1794
-  __TEXT.__const: 0x140
+  __TEXT.__const: 0xdc
   __TEXT.__gcc_except_tab: 0x75c
-  __TEXT.__objc_methname: 0x6a21
-  __TEXT.__oslogstring: 0x2510
-  __TEXT.__cstring: 0x265f
+  __TEXT.__objc_methname: 0x6a14
+  __TEXT.__oslogstring: 0x2556
+  __TEXT.__cstring: 0x2673
   __TEXT.__objc_classname: 0x49d
-  __TEXT.__objc_methtype: 0xbdd
+  __TEXT.__objc_methtype: 0xbab
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__unwind_info: 0x688
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x880
-  __DATA_CONST.__cfstring: 0x1ea0
+  __TEXT.__unwind_info: 0x690
+  __DATA_CONST.__auth_got: 0x4d0
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__cfstring: 0x1e80
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x2978
-  __DATA.__objc_selrefs: 0x1808
+  __DATA.__objc_selrefs: 0x1800
   __DATA.__objc_ivar: 0x1c4
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x300

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 549
-  Symbols:   404
-  CStrings:  1617
+  Functions: 550
+  Symbols:   394
+  CStrings:  1615
 
Symbols:
+ _PFFigGetImageSourceImageIndexForContainerItemID
+ _kCGImageSourceAddHEIFContainerItemID
- _com_apple_photos_ImageConversionServiceVersionNumber
- _com_apple_photos_ImageConversionServiceVersionString
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
