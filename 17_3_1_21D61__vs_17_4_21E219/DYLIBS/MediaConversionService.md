## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-630.0.150.0.0
-  __TEXT.__text: 0x1dbbc
+646.1.102.0.0
+  __TEXT.__text: 0x1dc94
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x1d98
+  __TEXT.__objc_methlist: 0x1dd0
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x498
   __TEXT.__cstring: 0x4a2f
   __TEXT.__oslogstring: 0x22a9
   __TEXT.__unwind_info: 0x7d8
   __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methname: 0x6483
-  __TEXT.__objc_methtype: 0xa3a
-  __TEXT.__objc_stubs: 0x4540
+  __TEXT.__objc_methname: 0x654d
+  __TEXT.__objc_methtype: 0xa3d
+  __TEXT.__objc_stubs: 0x4560
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0xab0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x25b0
-  __DATA_CONST.__objc_selrefs: 0x1498
+  __DATA_CONST.__objc_const: 0x2610
+  __DATA_CONST.__objc_selrefs: 0x14c0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x4c8
   __AUTH_CONST.__cfstring: 0x2e20
   __AUTH_CONST.__objc_const: 0x0

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x3e8
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x240
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x200
+  __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x528
   __DATA.__bss: 0x30
   __DATA_DIRTY.__const: 0xa0

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B01873B6-9FA4-398B-8CEF-9C25DDB33276
-  Functions: 690
-  Symbols:   2808
-  CStrings:  2017
+  UUID: 0AE893F0-9D08-3988-911A-B53C3273349A
+  Functions: 695
+  Symbols:   2821
+  CStrings:  2027
 
Symbols:
+ +[PAMediaConversionServiceImagingUtilities imagePropertiesByImageIndexInImageSource:processedWithMetadataPolicy:]
+ -[PHMediaFormatConversionSource checkForIsHDR]
+ -[PHMediaFormatConversionSource didCheckForIsHDR]
+ -[PHMediaFormatConversionSource markIsHDRAsCheckedWithValue:]
+ -[PHMediaFormatConversionSource setDidCheckForIsHDR:]
+ -[PHMediaFormatConversionSource setIsHDR:]
+ GCC_except_table319
+ GCC_except_table321
+ GCC_except_table323
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table329
+ GCC_except_table444
+ GCC_except_table452
+ GCC_except_table562
+ GCC_except_table564
+ GCC_except_table650
+ GCC_except_table652
+ GCC_except_table665
+ _OBJC_IVAR_$_PHMediaFormatConversionSource._didCheckForIsHDR
+ _OBJC_IVAR_$_PHMediaFormatConversionSource._isHDR
+ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke.104
+ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke_2.105
+ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.87
+ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.90
+ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.93
+ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.95
+ ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke.96
+ ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke.858
+ ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.792
+ ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.736
+ ___block_literal_global.410
+ ___block_literal_global.419
+ ___block_literal_global.451
+ ___block_literal_global.851
+ __unnamed_array_storage.894
+ __unnamed_array_storage.974
+ _objc_msgSend$imagePropertiesByImageIndexInImageSource:processedWithMetadataPolicy:
+ _objc_msgSend$markIsHDRAsCheckedWithValue:
- +[PAMediaConversionServiceImagingUtilities imagePropertiesByImageIndexInImageSource:]
- GCC_except_table314
- GCC_except_table316
- GCC_except_table318
- GCC_except_table320
- GCC_except_table322
- GCC_except_table324
- GCC_except_table439
- GCC_except_table447
- GCC_except_table557
- GCC_except_table559
- GCC_except_table640
- GCC_except_table642
- GCC_except_table660
- ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke.101
- ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke_2.104
- ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.85
- ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.89
- ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.91
- ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.94
- ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke.95
- ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke.846
- ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.780
- ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.724
- ___block_literal_global.408.893
- ___block_literal_global.433
- ___block_literal_global.478
- ___block_literal_global.926
- __unnamed_array_storage.1064
- __unnamed_array_storage.969
- _objc_msgSend$imagePropertiesByImageIndexInImageSource:
CStrings:
+ "@32@0:8^{CGImageSource=}16@24"
+ "T@\"NSSet\",?,R"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_didCheckForIsHDR"
+ "TB,N,V_isHDR"
+ "_didCheckForIsHDR"
+ "_isHDR"
+ "checkForIsHDR"
+ "didCheckForIsHDR"
+ "imagePropertiesByImageIndexInImageSource:processedWithMetadataPolicy:"
+ "markIsHDRAsCheckedWithValue:"
+ "setDidCheckForIsHDR:"
+ "setIsHDR:"
- "@24@0:8^{CGImageSource=}16"
- "T@\"NSSet\",R"
- "imagePropertiesByImageIndexInImageSource:"

```
