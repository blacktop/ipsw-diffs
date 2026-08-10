## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-1967.0.0.0.0
-  __TEXT.__text: 0x128e34
-  __TEXT.__objc_methlist: 0xaed4
+1971.0.0.0.0
+  __TEXT.__text: 0x129170
+  __TEXT.__objc_methlist: 0xaecc
   __TEXT.__const: 0x988
-  __TEXT.__gcc_except_tab: 0x49d8
-  __TEXT.__cstring: 0x315b4
-  __TEXT.__oslogstring: 0x11318
+  __TEXT.__gcc_except_tab: 0x4a90
+  __TEXT.__cstring: 0x31634
+  __TEXT.__oslogstring: 0x1124c
   __TEXT.__dlopen_cstrs: 0x19c8
   __TEXT.__ustring: 0xb22
-  __TEXT.__unwind_info: 0x35c8
+  __TEXT.__unwind_info: 0x35d8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_arrayobj: 0x11d60
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x22858
-  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0x1db0
   __DATA.__objc_ivar: 0xf34
-  __DATA.__data: 0x4f0
-  __DATA.__bss: 0xb40
+  __DATA.__data: 0x428
+  __DATA.__bss: 0xb48
   __DATA_DIRTY.__objc_data: 0x1950
   __DATA_DIRTY.__bss: 0x520
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5363
-  Symbols:   10774
-  CStrings:  17939
+  Functions: 5367
+  Symbols:   10780
+  CStrings:  17938
 
Symbols:
+ +[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table146
+ GCC_except_table162
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table207
+ GCC_except_table33
+ GCC_except_table70
+ GCC_except_table91
+ GCC_except_table98
+ __PSPhotoLibraryAssertionCount
+ ___35-[_PSBackgroundProcessingTask init]_block_invoke
+ ___49-[_PSBackgroundProcessingTask flushBookmarkCache]_block_invoke
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke_2
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke_3
+ ___64-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:]_block_invoke
+ ___72-[_PSBackgroundProcessingTask runLinkEnrichmentTaskWithExpirationCheck:]_block_invoke
+ ___76+[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]_block_invoke
+ ___76+[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e25_B16?0"NSManagedObject"8lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ _objc_msgSend$_cd_compactNumberWithDouble:
+ _objc_msgSend$_cd_doubleValue
+ _objc_msgSend$updateInteractionWithPhotoFeatures:keepGoing:
+ _sharedMADService._pasOnceToken3
- +[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:]
- -[_PSBoWEmbedding computeEmbeddingsForWordArrays:]
- GCC_except_table107
- GCC_except_table143
- GCC_except_table161
- GCC_except_table198
- GCC_except_table206
- GCC_except_table90
- ___35-[_PSPhotoLibraryAssertion dealloc]_block_invoke
- ___37-[_PSSuggester generatePSRTelemetry:]_block_invoke
- ___78-[_PSFamilyRecommender logFeedbackForFamilyRecommenderCallHasRecommendations:]_block_invoke
- ___block_descriptor_40_e8_32r_e25_B16?0"NSManagedObject"8lr32l8
- ___block_descriptor_40_e8_32s_e5_8?0ls32l8
- __pendingShutdownBlock
- _dispatch_block_cancel
- _objc_msgSend$letterCharacterSet
- _objc_msgSend$updateInteractionWithPhotoFeatures:
- _pthread_rwlock_rdlock
- _pthread_rwlock_trywrlock
- _pthread_rwlock_unlock
- _sharedMADService._pasOnceToken5
CStrings:
+ "Teardown _PSPhotoLibraryAssertion (will tell PhotoLibrary to shutdown)"
+ "Unable to find embedding for %{private}@"
+ "predictWithPredictionContext photo library retain for feedback processing"
+ "update interaction with photo features analysis queue"
- "Cancelled pending PhotoLibrary shutdown (new assertion requested)"
- "Deferred _PSPhotoLibraryAssertion teardown (will tell PhotoLibrary to shutdown)"
- "Deferred _PSPhotoLibraryAssertion teardown skipped (assertion re-acquired)"
- "Teardown _PSPhotoLibraryAssertion (shutdown deferred by %.0fs)"
- "Unable to find embedding for %@"
```
