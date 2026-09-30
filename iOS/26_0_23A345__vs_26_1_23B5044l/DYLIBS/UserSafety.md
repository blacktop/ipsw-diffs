## UserSafety

> `/System/Library/PrivateFrameworks/UserSafety.framework/UserSafety`

```diff

-125.0.3.1.0
-  __TEXT.__text: 0x3a90
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x2d0
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x231
-  __TEXT.__oslogstring: 0x229
-  __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0xb0a
-  __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__objc_classlist: 0x30
+129.0.0.0.0
+  __TEXT.__text: 0x1a3c
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_methlist: 0x210
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0xed
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_classname: 0x68
+  __TEXT.__objc_methname: 0x6bd
+  __TEXT.__objc_methtype: 0x1a6
+  __TEXT.__objc_stubs: 0x560
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x128
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x448
-  __DATA.__objc_ivar: 0x14
+  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__objc_const: 0x378
+  __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x18
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3036AFF1-422C-3AFA-9F80-622E3D2FCEAD
-  Functions: 99
-  Symbols:   407
-  CStrings:  166
+  UUID: D1120D31-6519-3C20-8AD7-C1C2089D9C6B
+  Functions: 56
+  Symbols:   261
+  CStrings:  105
 
Symbols:
- -[USMediaAnalysisService .cxx_destruct]
- -[USMediaAnalysisService _newImageClassificationRequest]
- -[USMediaAnalysisService _newVideoClassificationRequest]
- -[USMediaAnalysisService _processMADResults:requestID:error:request:]
- -[USMediaAnalysisService _processMADResults:requestID:error:request:].cold.1
- -[USMediaAnalysisService _processMADResults:requestID:error:request:].cold.2
- -[USMediaAnalysisService _processMADResults:requestID:error:request:].cold.3
- -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:]
- -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:].cold.1
- -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:].cold.2
- -[USMediaAnalysisService _processMADResults:requestID:error:videoRequest:].cold.3
- -[USMediaAnalysisService dealloc]
- -[USMediaAnalysisService initWithMADService:]
- -[USMediaAnalysisService init]
- -[USMediaAnalysisService isSensitiveCGImage:withOrientation:completionHandler:]
- -[USMediaAnalysisService isSensitiveImage:completionHandler:]
- -[USMediaAnalysisService isSensitiveImageWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:]
- -[USMediaAnalysisService isSensitiveVideoFile:useBlastdoor:progressHandler:completionHandler:]
- -[USMediaAnalysisService isSensitiveVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:]
- -[USMediaAnalysisService service]
- -[USMediaAnalysisService setService:]
- GCC_except_table0
- GCC_except_table12
- GCC_except_table14
- GCC_except_table19
- GCC_except_table20
- GCC_except_table3
- GCC_except_table7
- GCC_except_table9
- _MediaAnalysisServicesLibrary
- _MediaAnalysisServicesLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_SCAnalytics
- _OBJC_CLASS_$_USMediaAnalysisService
- _OBJC_IVAR_$_USMediaAnalysisService._service
- _OBJC_METACLASS_$_USMediaAnalysisService
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- __Block_object_dispose
- __OBJC_$_INSTANCE_METHODS_USMediaAnalysisService
- __OBJC_$_INSTANCE_VARIABLES_USMediaAnalysisService
- __OBJC_$_PROP_LIST_USMediaAnalysisService
- __OBJC_CLASS_RO_$_USMediaAnalysisService
- __OBJC_METACLASS_RO_$_USMediaAnalysisService
- __Unwind_Resume
- ___104-[USMediaAnalysisService isSensitiveImageWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:]_block_invoke
- ___120-[USMediaAnalysisService isSensitiveVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:]_block_invoke
- ___120-[USMediaAnalysisService isSensitiveVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:]_block_invoke_2
- ___61-[USMediaAnalysisService isSensitiveImage:completionHandler:]_block_invoke
- ___79-[USMediaAnalysisService isSensitiveCGImage:withOrientation:completionHandler:]_block_invoke
- ___94-[USMediaAnalysisService isSensitiveVideoFile:useBlastdoor:progressHandler:completionHandler:]_block_invoke
- ___94-[USMediaAnalysisService isSensitiveVideoFile:useBlastdoor:progressHandler:completionHandler:]_block_invoke_2
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___MediaAnalysisServicesLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40bs_e11_v20?0i8d12ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48r_e20_v20?0i8"NSError"12ls32l8r48l8s40l8
- ___getMADImageSafetyClassificationRequestClass_block_invoke
- ___getMADImageSafetyClassificationRequestClass_block_invoke.cold.1
- ___getMADServiceClass_block_invoke
- ___getMADServiceClass_block_invoke.cold.1
- ___getMADVideoSafetyClassificationRequestClass_block_invoke
- ___getMADVideoSafetyClassificationRequestClass_block_invoke.cold.1
- ___objc_personality_v0
- __os_log_error_impl
- __os_log_impl
- __sl_dlopen
- _abort_report_np
- _audit_stringMediaAnalysisServices
- _free
- _getMADImageSafetyClassificationRequestClass.softClass
- _getMADServiceClass.softClass
- _getMADVideoSafetyClassificationRequestClass.softClass
- _objc_alloc_init
- _objc_getClass
- _objc_msgSend$_newImageClassificationRequest
- _objc_msgSend$_newVideoClassificationRequest
- _objc_msgSend$_processMADResults:requestID:error:request:
- _objc_msgSend$_processMADResults:requestID:error:videoRequest:
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$cancelAllRequests
- _objc_msgSend$client
- _objc_msgSend$collectMediaAnalysisServiceEvent::
- _objc_msgSend$count
- _objc_msgSend$error
- _objc_msgSend$firstObject
- _objc_msgSend$initWithMADService:
- _objc_msgSend$performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:
- _objc_msgSend$performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:
- _objc_msgSend$performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:
- _objc_msgSend$performRequests:onImageURL:withIdentifier:completionHandler:
- _objc_msgSend$performRequests:videoURL:identifier:progressHandler:completionHandler:
- _objc_msgSend$results
- _objc_msgSend$service
- _objc_msgSend$setRequiresBlastdoor:
- _objc_msgSend$sharedInstance
- _objc_release_x25
- _objc_retainAutorelease
- _os_log_type_enabled
CStrings:
- ""
- "%s"
- "@\"MADService\""
- "@44@0:8^B16i24@28@36"
- "MAD request(%d) failed with error: %@"
- "MAD request(%d) returns error: %@"
- "MAD request(%d) returns following results: (%d, '%@')"
- "MAD request(%d) returns unexpected number of results %lu"
- "MAD request(%d) with Image's LocalIdentifier started"
- "MAD request(%d) with cgImage has started"
- "MAD request(%d) with imageURL started"
- "MAD request(%d) with video's LocalIdentifier started"
- "MAD request(%d) with videoURL started"
- "MAD video request(%d) failed with error: %@"
- "MAD video request(%d) returns error: %@"
- "MAD video request(%d) returns unexpected number of results %lu"
- "MADImageSafetyClassificationRequest"
- "MADService"
- "MADService request has failed with request error"
- "MADService video request has failed with request error"
- "MADVideoSafetyClassificationRequest"
- "T@\"MADService\",&,N,V_service"
- "USMediaAnalysisService"
- "Unable to find class %s"
- "Unexpected results from MADService"
- "Unexpected video results from MADService"
- "_newImageClassificationRequest"
- "_newVideoClassificationRequest"
- "_processMADResults:requestID:error:request:"
- "_processMADResults:requestID:error:videoRequest:"
- "_service"
- "arrayWithObjects:count:"
- "cancelAllRequests"
- "collectMediaAnalysisServiceEvent::"
- "count"
- "dealloc"
- "error"
- "firstObject"
- "initWithMADService:"
- "isSensitiveCGImage:withOrientation:completionHandler:"
- "isSensitiveImage:completionHandler:"
- "isSensitiveImageWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:"
- "isSensitiveVideoFile:useBlastdoor:progressHandler:completionHandler:"
- "isSensitiveVideoWithLocalIdentifier:fromPhotoLibraryWithURL:progressHandler:completionHandler:"
- "performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:"
- "performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:"
- "performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:"
- "performRequests:onImageURL:withIdentifier:completionHandler:"
- "performRequests:videoURL:identifier:progressHandler:completionHandler:"
- "results"
- "service"
- "setRequiresBlastdoor:"
- "setService:"
- "sharedInstance"
- "softlink:r:path:/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices"
- "v20@?0i8@\"NSError\"12"
- "v20@?0i8d12"

```
