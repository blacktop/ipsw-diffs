## SpotlightKnowledge

> `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/Versions/A/SpotlightKnowledge`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0x14930
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0xc98
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x2c76
+2333.41.1.3.0
+  __TEXT.__text: 0x1577c
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_methlist: 0xd50
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x2cf6
   __TEXT.__oslogstring: 0x98e
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__objc_classname: 0x10e
-  __TEXT.__objc_methname: 0x2ffe
+  __TEXT.__objc_methname: 0x32c3
   __TEXT.__objc_methtype: 0x441
-  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_stubs: 0x24e0
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0xab0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc10
+  __DATA_CONST.__objc_selrefs: 0xc78
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x610
-  __AUTH_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__objc_arraydata: 0x6a0
+  __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x4c40
-  __AUTH_CONST.__objc_const: 0xd50
+  __AUTH_CONST.__cfstring: 0x4c80
+  __AUTH_CONST.__objc_const: 0xde0
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x9c
+  __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x8
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 457
-  Symbols:   1159
-  CStrings:  1255
+  Functions: 473
+  Symbols:   1189
+  CStrings:  1279
 
Symbols:
+ -[SKGAttributeProcessor getCachedEmbeddingCompletenessForBundle:completion:]
+ -[SKGAttributeProcessor launchUpgradeTasks]
+ -[SKGProcessor(DocUnderstandingUtils) needsSKGReindexerDocUnderstandingForRecord:bundleID:itemHasText:]
+ -[SKGProcessor(EmbeddingsUtils) isCJKLanguage:]
+ -[SKGProcessor(EmbeddingsUtils) needsSKGReindexerEmbeddingsForRecord:bundleID:itemHasText:]
+ -[SKGProcessor(EmbeddingsUtils) updateSKGReindexerEmbeddingAttributes:record:bundleID:itemHasText:]
+ -[SKGProcessor(SuggestedEventsUtils) needsSKGReindexerSuggestedEventsForRecord:bundleID:itemHasText:]
+ -[SKGProcessorConnection getCachedEmbeddingCompletenessForBundle:completion:]
+ -[SKGProcessorConnection launchUpgradeTasks]
+ -[SKGProcessorContext currentRedonationDate]
+ -[SKGProcessorContext maxJournalSizeWhenLowDiskSpace]
+ -[SKGProcessorContext redonationThrottleHorizonDate]
+ -[SKGProcessorContext setCurrentRedonationDate:]
+ -[SKGProcessorContext setMaxJournalSizeWhenLowDiskSpace:]
+ -[SKGProcessorContext setRedonationThrottleHorizonDate:]
+ GCC_except_table10
+ GCC_except_table17
+ GCC_except_table6
+ OBJC_IVAR_$_SKGProcessorContext._currentRedonationDate
+ OBJC_IVAR_$_SKGProcessorContext._maxJournalSizeWhenLowDiskSpace
+ OBJC_IVAR_$_SKGProcessorContext._redonationThrottleHorizonDate
+ _SILanguagesIsCJK
+ ___77-[SKGProcessorConnection getCachedEmbeddingCompletenessForBundle:completion:]_block_invoke
+ __block_literal_global.111
+ __block_literal_global.227
+ __block_literal_global.313
+ __block_literal_global.316
+ __block_literal_global.408
+ _objc_msgSend$copyLanguageFromRecord:
+ _objc_msgSend$getCachedEmbeddingCompletenessForBundle:completion:
+ _objc_msgSend$isCJKLanguage:
+ _objc_msgSend$launchUpgradeTasks
+ _objc_msgSend$needsSKGReindexerDocUnderstandingForRecord:bundleID:itemHasText:
+ _objc_msgSend$needsSKGReindexerEmbeddingsForRecord:bundleID:itemHasText:
+ _objc_msgSend$needsSKGReindexerSuggestedEventsForRecord:bundleID:itemHasText:
+ _objc_msgSend$updateSKGReindexerEmbeddingAttributes:record:bundleID:itemHasText:
+ _xpc_dictionary_get_double
+ docUnderstandingIncludeBundles.gDocumentUnderstandingIncludeBundles
- GCC_except_table16
- GCC_except_table5
- GCC_except_table9
- __block_literal_global.113
- __block_literal_global.229
- __block_literal_global.312
- __block_literal_global.315
- __block_literal_global.407
CStrings:
+ "SearchToolPhotosCrossBundleSearch"
+ "Tq,N,V_currentRedonationDate"
+ "Tq,N,V_maxJournalSizeWhenLowDiskSpace"
+ "Tq,N,V_redonationThrottleHorizonDate"
+ "_currentRedonationDate"
+ "_kMDItemUpdaterLastRequested"
+ "_kMDItemUpdaterRequestedCount"
+ "_maxJournalSizeWhenLowDiskSpace"
+ "_redonationThrottleHorizonDate"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProvider"
+ "completeness"
+ "currentRedonationDate"
+ "embeddingCompleteness"
+ "getCachedEmbeddingCompletenessForBundle:completion:"
+ "isCJKLanguage:"
+ "launchUpgradeTasks"
+ "maxJournalSizeWhenLowDiskSpace"
+ "needsSKGReindexerDocUnderstandingForRecord:bundleID:itemHasText:"
+ "needsSKGReindexerEmbeddingsForRecord:bundleID:itemHasText:"
+ "needsSKGReindexerSuggestedEventsForRecord:bundleID:itemHasText:"
+ "redonationThrottleHorizonDate"
+ "setCurrentRedonationDate:"
+ "setMaxJournalSizeWhenLowDiskSpace:"
+ "setRedonationThrottleHorizonDate:"
+ "updateSKGReindexerEmbeddingAttributes:record:bundleID:itemHasText:"
- "SearchToolCleanSlateDenseRetrieval"
- "com.apple.corespotlight.InternalTestsHost"
- "com.apple.corespotlight.TestsHost"

```
