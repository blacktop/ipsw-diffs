## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-612.0.160.0.0
-  __TEXT.__text: 0x1d568
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x1d78
+622.0.130.0.0
+  __TEXT.__text: 0x1dbbc
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x1d98
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__cstring: 0x49f1
+  __TEXT.__gcc_except_tab: 0x498
+  __TEXT.__cstring: 0x4a2f
   __TEXT.__oslogstring: 0x22a9
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7d8
   __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methname: 0x63af
-  __TEXT.__objc_methtype: 0x9ed
-  __TEXT.__objc_stubs: 0x44e0
-  __DATA_CONST.__got: 0x2a8
+  __TEXT.__objc_methname: 0x6483
+  __TEXT.__objc_methtype: 0xa3a
+  __TEXT.__objc_stubs: 0x4540
+  __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xab0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x25b0
-  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_selrefs: 0x1498
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__cfstring: 0x2e00
+  __AUTH_CONST.__cfstring: 0x2e20
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__auth_got: 0x3e8
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x240
   __DATA.__objc_superrefs: 0x70
   __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x528
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__const: 0x120
+  __DATA_DIRTY.__const: 0xa0
   __DATA_DIRTY.__objc_const: 0xf30
   __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 687
-  Symbols:   2786
-  CStrings:  1641
+  Functions: 690
+  Symbols:   2808
+  CStrings:  1648
 
Symbols:
+ +[PAMediaConversionServiceImagingUtilities imageDataByAddingMissingPrimaryImageProperties:toImageDataSource:primaryImageIndex:inputImagePropertiesByIndex:]
+ +[PAMediaConversionServiceImagingUtilities imagePropertiesByImageIndexInImageSource:]
+ +[PAMediaConversionServiceImagingUtilities stereoGroupInfoForImageIndex:containerImageGroups:]
+ GCC_except_table55
+ GCC_except_table640
+ GCC_except_table645
+ GCC_except_table647
+ GCC_except_table660
+ ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke.95
+ ___NSDictionary0__struct
+ ___block_literal_global.408.893
+ ___block_literal_global.433
+ ___block_literal_global.478
+ ___block_literal_global.926
+ __unnamed_array_storage.1064
+ __unnamed_array_storage.969
+ _kCGImagePropertyGroupImageDisparityAdjustment
+ _kCGImagePropertyGroupImageIndexLeft
+ _kCGImagePropertyGroupImageIndexRight
+ _kCGImagePropertyGroupImageIsLeftImage
+ _kCGImagePropertyGroupImageIsRightImage
+ _kCGImagePropertyGroupIndex
+ _kCGImagePropertyGroupType
+ _kCGImagePropertyGroupTypeStereoPair
+ _kCGImagePropertyGroups
+ _lstat
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$imageDataByAddingMissingPrimaryImageProperties:toImageDataSource:primaryImageIndex:inputImagePropertiesByIndex:
+ _objc_msgSend$imagePropertiesByImageIndexInImageSource:
+ _objc_msgSend$stereoGroupInfoForImageIndex:containerImageGroups:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table637
- GCC_except_table639
- GCC_except_table644
- GCC_except_table657
- _CGImageDestinationSetProperties
- ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke.92
- ___block_literal_global.402
- ___block_literal_global.408.796
- ___block_literal_global.442
- ___block_literal_global.830
- __unnamed_array_storage.873
- __unnamed_array_storage.964
- _objc_msgSend$attributesOfItemAtPath:error:
- _objc_msgSend$fileSize
CStrings:
+ "@24@0:8^{CGImageSource=}16"
+ "@32@0:8Q16@24"
+ "@48@0:8@16^{CGImageSource=}24Q32@40"
+ "Unexpected non-nil service connection during connection setup"
+ "fileSystemRepresentation"
+ "imageDataByAddingMissingPrimaryImageProperties:toImageDataSource:primaryImageIndex:inputImagePropertiesByIndex:"
+ "imagePropertiesByImageIndexInImageSource:"
+ "stereoGroupInfoForImageIndex:containerImageGroups:"
+ "unsignedIntegerValue"
- "attributesOfItemAtPath:error:"
- "fileSize"

```
