## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

```diff

-1967.0.0.0.0
-  __TEXT.__text: 0x128164
-  __TEXT.__objc_methlist: 0xac9c
+1971.0.0.0.0
+  __TEXT.__text: 0x128474
+  __TEXT.__objc_methlist: 0xac94
   __TEXT.__const: 0x978
-  __TEXT.__gcc_except_tab: 0x41fc
-  __TEXT.__cstring: 0x313ac
-  __TEXT.__oslogstring: 0xfd9f
+  __TEXT.__gcc_except_tab: 0x42b4
+  __TEXT.__cstring: 0x31426
+  __TEXT.__oslogstring: 0xfcd3
   __TEXT.__dlopen_cstrs: 0x160f
   __TEXT.__ustring: 0x7e4
-  __TEXT.__unwind_info: 0x3358
+  __TEXT.__unwind_info: 0x3360
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x39d78
   __DATA_CONST.__got: 0x930
-  __AUTH_CONST.__const: 0x4340
+  __AUTH_CONST.__const: 0x4310
   __AUTH_CONST.__cfstring: 0x7f000
   __AUTH_CONST.__objc_const: 0x155e8
   __AUTH_CONST.__objc_intobj: 0x1170
   __AUTH_CONST.__objc_arrayobj: 0x11d18
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x226c8
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0x1bd0
   __DATA.__objc_ivar: 0xf0c
-  __DATA.__data: 0x4f0
-  __DATA.__bss: 0x770
+  __DATA.__data: 0x428
+  __DATA.__bss: 0x778
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5232
-  Symbols:   10534
-  CStrings:  17733
+  Functions: 5236
+  Symbols:   10537
+  CStrings:  17731
 
Symbols:
+ +[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]
+ GCC_except_table106
+ GCC_except_table111
+ GCC_except_table120
+ GCC_except_table128
+ GCC_except_table17
+ GCC_except_table200
+ GCC_except_table206
+ GCC_except_table67
+ GCC_except_table92
+ __49-[_PSBackgroundProcessingTask flushBookmarkCache]_block_invoke
+ __76+[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]_block_invoke
+ __PSPhotoLibraryAssertionCount
+ ___35-[_PSBackgroundProcessingTask init]_block_invoke
+ ___49-[_PSBackgroundProcessingTask flushBookmarkCache]_block_invoke
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke_2
+ ___64-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:]_block_invoke
+ ___72-[_PSBackgroundProcessingTask runLinkEnrichmentTaskWithExpirationCheck:]_block_invoke
+ ___76+[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:keepGoing:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e25_B16?0"NSManagedObject"8l
+ _objc_msgSend$_cd_compactNumberWithDouble:
+ _objc_msgSend$_cd_doubleValue
+ _objc_msgSend$updateInteractionWithPhotoFeatures:keepGoing:
- +[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:]
- -[_PSBoWEmbedding computeEmbeddingsForWordArrays:]
- GCC_except_table108
- GCC_except_table189
- GCC_except_table19
- GCC_except_table199
- GCC_except_table205
- GCC_except_table91
- ___35-[_PSPhotoLibraryAssertion dealloc]_block_invoke
- ___37-[_PSSuggester generatePSRTelemetry:]_block_invoke
- ___78-[_PSFamilyRecommender logFeedbackForFamilyRecommenderCallHasRecommendations:]_block_invoke
- ___block_descriptor_40_e8_32r_e25_B16?0"NSManagedObject"8l
- ___block_descriptor_40_e8_32s_e5_8?0l
- __pendingShutdownBlock
- _dispatch_block_cancel
- _objc_msgSend$letterCharacterSet
- _objc_msgSend$updateInteractionWithPhotoFeatures:
- _pthread_rwlock_rdlock
- _pthread_rwlock_trywrlock
- _pthread_rwlock_unlock
CStrings:
+ "Teardown _PSPhotoLibraryAssertion (will tell PhotoLibrary to shutdown)"
+ "Unable to find embedding for %{private}@"
+ "predictWithPredictionContext photo library retain for feedback processing"
+ "update interaction with photo features analysis queue"
- "@8@?0"
- "Cancelled pending PhotoLibrary shutdown (new assertion requested)"
- "Deferred _PSPhotoLibraryAssertion teardown (will tell PhotoLibrary to shutdown)"
- "Deferred _PSPhotoLibraryAssertion teardown skipped (assertion re-acquired)"
- "Teardown _PSPhotoLibraryAssertion (shutdown deferred by %.0fs)"
- "Unable to find embedding for %@"
```
