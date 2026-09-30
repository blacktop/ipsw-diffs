## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1e020
-  __TEXT.__auth_stubs: 0x7a0
+720.4.101.0.0
+  __TEXT.__text: 0x1dd54
+  __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_methlist: 0x1e00
-  __TEXT.__const: 0x120
+  __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0x6b4
-  __TEXT.__cstring: 0x4adf
-  __TEXT.__oslogstring: 0x22a9
-  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__cstring: 0x4af6
+  __TEXT.__oslogstring: 0x22ef
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methname: 0x65d9
-  __TEXT.__objc_methtype: 0xa4e
+  __TEXT.__objc_methname: 0x65ce
+  __TEXT.__objc_methtype: 0xa1c
   __TEXT.__objc_stubs: 0x4600
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0xa78
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0xaa0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f0
+  __DATA_CONST.__objc_selrefs: 0x14e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x4b8
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x2ea0
   __AUTH_CONST.__objc_const: 0x3570

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 699
-  Symbols:   1132
-  CStrings:  1671
+  Functions: 700
+  Symbols:   1119
+  CStrings:  1670
 
Symbols:
+ _PFFigGetImageSourceImageIndexForContainerItemID
+ _kCGImageSourceAddHEIFContainerItemID
- _MediaConversionServiceVersionNumber
- _MediaConversionServiceVersionString
- ___NSDictionary0__struct
- _kCGImageDestinationCreateHDRGainMap
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
- _kCGImageSourceDecodeRequest
- _kCGImageSourceDecodeToSDR
CStrings:
+ "@\"NSDictionary\"16@?0@8"
+ "Output image at index %!t(MISSING)u is missing image property '%!{(MISSING)public}@' present in input image"
+ "TB,N,V_forceFormatConversion"
+ "Unable to create an image source from Fig outputData %!p(MISSING) of length %!t(MISSING)u to inspect for missing metadata properties."
+ "Unable to perform single image JPEG passthrough conversion for source %!@(MISSING)"
+ "Unexpected input (%!t(MISSING)u) / output (%!t(MISSING)u) image count mismatch"
+ "dataForSingleImageJPEGPassthroughConversionForImageSource:primaryImageProperties:"
+ "logMissingPropertiesInCMPhotoOutputData:comparedToProcessedSourceImagePropertiesByIndex:"
- "@32@0:8Q16@24"
- "@48@0:8@16^{CGImageSource=}24Q32@40"
- "Adding metadata properties missed by Fig: [%!{(MISSING)public}@]"
- "TB,V_forceFormatConversion"
- "Unable to apply metadata properties missed by Fig during passthrough conversion for %!@(MISSING)."
- "Unable to create an image source from Fig outputData (%!{(MISSING)public}@) to inspect for adding any missing metadata properties."
- "imageDataByAddingMissingPrimaryImageProperties:toImageDataSource:primaryImageIndex:inputImagePropertiesByIndex:"
- "stereoGroupInfoForImageIndex:containerImageGroups:"
- "unsignedIntegerValue"

```
