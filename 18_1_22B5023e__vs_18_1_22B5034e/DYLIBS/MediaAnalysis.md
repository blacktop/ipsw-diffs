## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-285.2.1.0.0
-  __TEXT.__text: 0x3f7814
+285.5.2.0.0
+  __TEXT.__text: 0x400a4c
   __TEXT.__auth_stubs: 0x3570
-  __TEXT.__objc_methlist: 0x193f4
-  __TEXT.__const: 0x13f98
-  __TEXT.__gcc_except_tab: 0x5272c
-  __TEXT.__cstring: 0x1e5c3
-  __TEXT.__oslogstring: 0x23eab
+  __TEXT.__objc_methlist: 0x1942c
+  __TEXT.__const: 0x13fa8
+  __TEXT.__gcc_except_tab: 0x57cbc
+  __TEXT.__cstring: 0x1e643
+  __TEXT.__oslogstring: 0x241db
   __TEXT.__dlopen_cstrs: 0x579
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x9c

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xfbf8
+  __TEXT.__unwind_info: 0xfc88
   __TEXT.__eh_frame: 0x1e0
   __TEXT.__objc_classname: 0x3b6e
-  __TEXT.__objc_methname: 0x38a21
+  __TEXT.__objc_methname: 0x38b8b
   __TEXT.__objc_methtype: 0xca8e
-  __TEXT.__objc_stubs: 0x26480
+  __TEXT.__objc_stubs: 0x264e0
   __DATA_CONST.__got: 0x18d8
-  __DATA_CONST.__const: 0x5e10
+  __DATA_CONST.__const: 0x5e40
   __DATA_CONST.__objc_classlist: 0x1078
   __DATA_CONST.__objc_catlist: 0x198
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb710
+  __DATA_CONST.__objc_selrefs: 0xb750
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xdb0
   __DATA_CONST.__objc_arraydata: 0x1060
   __AUTH_CONST.__auth_got: 0x1ad0
   __AUTH_CONST.__auth_ptr: 0x108
-  __AUTH_CONST.__const: 0x55f8
-  __AUTH_CONST.__cfstring: 0x14880
-  __AUTH_CONST.__objc_const: 0x353b0
+  __AUTH_CONST.__const: 0x5618
+  __AUTH_CONST.__cfstring: 0x148c0
+  __AUTH_CONST.__objc_const: 0x353d0
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_doubleobj: 0x400
   __AUTH_CONST.__objc_intobj: 0x2aa8

   __AUTH.__thread_bss: 0x9c9
   __DATA.__objc_ivar: 0x2f78
   __DATA.__data: 0x1898
-  __DATA.__bss: 0x919
+  __DATA.__bss: 0x929
   __DATA.__common: 0x3b9
   __DATA_DIRTY.__objc_data: 0xa4c0
   __DATA_DIRTY.__data: 0x188
-  __DATA_DIRTY.__bss: 0x868
+  __DATA_DIRTY.__bss: 0x860
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15162
-  Symbols:   19006
-  CStrings:  17327
+  Functions: 15176
+  Symbols:   19021
+  CStrings:  17356
 
Symbols:
+ _VCPLogInstance
+ _VCPKeyValueOCRAnalysisLastGatingIncludedFetchTimestamp
CStrings:
+ "_countFailuresWithAssetBatch:database:taskID:"
+ "MediaAnalyzer : use maxSimilarityDiff = %!f(MISSING)"
+ "[%!@(MISSING)] Cancelled during queryProgressDetail"
+ "common"
+ "Image embedding not available. Compute image caption w/o re-using image embedding"
+ "faceTorsoprint"
+ "[%!@(MISSING)] Failed to fetch processed assets - %!@(MISSING)"
+ "_scanPhotoLibrary:taskID:statistics:cancelOrExtendTimeoutBlock:"
+ "Failed to perform face-torso printing - %!@(MISSING)"
+ "Failed to generate valid face-torso representation %!@(MISSING) (faceprint: %!@(MISSING)valid - torsoprint: %!@(MISSING)valid)"
+ "Generated face-torso representation %!@(MISSING) (faceprint: %!@(MISSING)valid - torsoprint: %!@(MISSING)valid)"
+ "Failed to configure torso printing (%!@(MISSING))"
+ "Failed to query KeyValueStore"
+ "Cancelled during _scanPhotoLibrary"
+ "countAllAssetsForTaskID:photoLibrary:error:"
+ "vcp_assetCountForTaskID:withPriority:"
+ "_queryProgressDetailExpress:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
+ "Parsed a value without key specified; skipping this value"
+ "in"
+ "Cancelled during _queryProgressDetailExpress"
+ "_countMediaAnalysisWithAssetBatch:database:analyzedCount:completeAnalyzedCount:partialAnalyzedCount:"
+ "Failed to configure torso detection (%!@(MISSING))"
+ "[%!@(MISSING)] Failed to query total asset count - scene threshold %!f(MISSING) - %!@(MISSING)"
+ "loadKeyValues"
+ "getMaxSimilarityDiffFor1UP"
+ "vcp_processedAssetCountForTaskID:"
+ "Associated torso: %!@(MISSING)"
+ "countProcessedAssetsForTaskID:photoLibrary:error:"
+ "%!@(MISSING) Person only has 1 face %!@(MISSING) - return that face as key face"
+ "getMinSimilarityHighRecall"
+ "vcp_processedAssetCountForTaskID:withPriority:"
+ "_countAnalysisWithAssetBatch:taskID:"
+ "queryImagePriority1MCEnableDateWithPhotoLibraryURL:reply:"
+ "%!@(MISSING) Face %!@(MISSING) is already picked by user as keyFace of another person"
+ "queryProgressDetail:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
+ "SELECT key, value FROM KeyValueStore;"
+ "[MediaAnalysis] embedding 1-up timeranges [%!f(MISSING), %!f(MISSING)], score %!f(MISSING)"
+ "queryAnalysisProgress:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
+ "queryCachedFaceAnalysisProgress:photoLibrary:"
+ "reportProgressForPhotoLibrary:taskID:logMessage:cancelOrExtendTimeoutBlock:"
+ "-[VCPDatabaseReader loadKeyValues]"
+ "Providing personalization with face-torso print - %!@(MISSING)"
+ "Query progress: unsupport taskID %!l(MISSING)u"
+ "OCRAnalysisLastGatingIncludedFetchTimestamp"
+ "Embedding size mismatch (current embedding size in byte: %!l(MISSING)u, expected size in byte with float: %!l(MISSING)u) analyzeEmbedding only supports VCPMUBBRevision_V4 and VCPMUBBRevision_V5"
+ "_vipStatusForPhotoLibrary:type:"
- "MediaAnalyzer : use minSimilarityDiff = %!f(MISSING)"
- "_countMediaAnalysisWithAssetBatch:andDatabase:analyzedCount:completeAnalyzedCount:partialAnalyzedCount:"
- "_queryProgressDetailExpress:forPhotoLibrary:andTaskID:extendedTimeoutBlock:"
- "countAllAssetsForTaskID:withPhotoLibrary:error:"
- "_scanPhotoLibrary:withTaskID:statistics:andExtendTimeoutBlock:"
- "_countAnalysisWithAssetBatch:andDatabase:andTaskID:"
- "reportProgressForPhotoLibrary:taskID:logMessage:withExtendTimeoutBlock:"
- "Embedding size mismatch (current embedding size in byte: %!l(MISSING)u, expected size in byte with float: %!l(MISSING)u) analyzeEmbedding only supports VCPMUBBRevision_V3 and VCPMUBBRevision_V4"
- "[%!@(MISSING)] Failed to query total asset count - scene threshold %!f(MISSING): %!s(MISSING)\n"
- "getMinSimilarityDiffFor1UP"
- "_countFailuresWithAssetBatch:andDatabase:andTaskID:"
- "[%!@(MISSING)] Failed to fetch processed assets: %!@(MISSING)"
- "getMinSimilarityOneToken"
- "Query progress: unsupport taskID %!l(MISSING)u - %!@(MISSING)"
- "Failed to perform face printing"
- "countProcessedAssetsForTaskID:withPhotoLibrary:error:"
- "_vipStatusForPhotoLibrary:andType:"

```
