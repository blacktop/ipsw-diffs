## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/Versions/A/QueryParser`

```diff

-3600.31.21.0.0
-  __TEXT.__text: 0x11fdfc
-  __TEXT.__objc_methlist: 0x29ec
-  __TEXT.__const: 0x2d38
-  __TEXT.__gcc_except_tab: 0x138ac
-  __TEXT.__oslogstring: 0x7a0e
-  __TEXT.__cstring: 0xd475
+3605.8.1.0.0
+  __TEXT.__text: 0x121498
+  __TEXT.__objc_methlist: 0x2a94
+  __TEXT.__const: 0x2d48
+  __TEXT.__gcc_except_tab: 0x13af8
+  __TEXT.__oslogstring: 0x7bee
+  __TEXT.__cstring: 0xd525
   __TEXT.__ustring: 0x112
   __TEXT.__swift5_typeref: 0x5c2
   __TEXT.__constg_swiftt: 0x5f0

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5368
+  __TEXT.__unwind_info: 0x53c8
   __TEXT.__eh_frame: 0xc90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2118
+  __DATA_CONST.__objc_selrefs: 0x21a8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x1ff8
-  __DATA_CONST.__got: 0x780
-  __AUTH_CONST.__const: 0x4be0
-  __AUTH_CONST.__cfstring: 0x12880
-  __AUTH_CONST.__objc_const: 0x4650
+  __DATA_CONST.__got: 0x788
+  __AUTH_CONST.__const: 0x4c10
+  __AUTH_CONST.__cfstring: 0x129e0
+  __AUTH_CONST.__objc_const: 0x46f8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b18
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1478
+  __AUTH_CONST.__auth_got: 0x1480
   __AUTH_CONST.__auth_ptr: 0x210
   __AUTH.__objc_data: 0x8e8
   __AUTH.__data: 0x448
-  __DATA.__objc_ivar: 0x30c
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x11b0
   __DATA.__bss: 0x1510
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4409
-  Symbols:   7139
-  CStrings:  3402
+  Functions: 4432
+  Symbols:   7170
+  CStrings:  3419
 
Symbols:
+ +[QPAssetManager _contentTypesForAssetSet:]
+ +[QPAssetManager _isKnownContentType:forAssetSet:]
+ +[QPAssetManager(Testing) _test_assetNameEmbedding]
+ +[QPAssetManager(Testing) _test_assetNameGeo]
+ +[QPAssetManager(Testing) _test_assetNameQueryParser]
+ +[QPAssetManager(Testing) _test_assetNameQueryUnderstanding]
+ +[QPAssetManager(Testing) _test_assetNameSFC]
+ +[QPAssetManager(Testing) _test_assetNameSafety]
+ +[QPAssetManager(Testing) _test_assetSetQueryParserOverrides]
+ +[QPAssetManager(Testing) _test_assetSetQueryParser]
+ -[QPAssetManager _bulkPopulateForAssetSet:locale:]
+ -[QPAssetManager _cacheKeyForAssetSet:locale:contentType:]
+ -[QPAssetManager(Testing) _test_bulkPopulateForAssetSet:locale:]
+ -[QPAssetManager(Testing) _test_bulkPopulateShortCircuitCount]
+ OBJC_IVAR_$_QPAssetManager._locked_bulkPopulateShortCircuitCount
+ _CFStringCompareWithOptions
+ _OBJC_CLASS_$_RBSAcquisitionCompletionAttribute
+ __50-[QPAssetManager _bulkPopulateForAssetSet:locale:]_block_invoke
+ __OBJC_$_CLASS_METHODS_QPAssetManager(Testing)
+ __ZN2QP13isHomeDaypartENS_22QPDateComponentsPeriodE
+ __ZN2QP25getHomeDaypartOffsetHoursENS_22QPDateComponentsPeriodE
+ __ZN2QPL14endsWithWordCIEPK10__CFStringlS2_
+ __ZNK2QP19ParserConfiguration17languageIsEnglishEv
+ __ZNK2QP19ParserConfiguration29embeddingStringMaskForArgTypeE15QUIntentArgType
+ __ZNK2QP19ParserConfiguration30embeddingStringExcludesArgTypeE15QUIntentArgType
+ ___50-[QPAssetManager _bulkPopulateForAssetSet:locale:]_block_invoke
+ ___57-[QPAssetManager _systemAssetPathsForContentType:locale:]_block_invoke_2
+ ___62-[QPAssetManager(Testing) _test_bulkPopulateShortCircuitCount]_block_invoke
+ ___block_descriptor_56_ea8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0l
+ ___copy_helper_block_ea8_32s40s48r56r
+ ___destroy_helper_block_ea8_32s40s48r56r
+ _objc_msgSend$_bulkPopulateForAssetSet:locale:
+ _objc_msgSend$_cacheKeyForAssetSet:locale:contentType:
+ _objc_msgSend$_contentTypesForAssetSet:
+ _objc_msgSend$_isKnownContentType:forAssetSet:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$attributeWithCompletionPolicy:
+ _objc_msgSend$consistencyToken
+ _objc_msgSend$isLatestConsistencyToken:
- GCC_except_table151
- GCC_except_table168
- GCC_except_table199
- GCC_except_table256
- _ZL18assetManagerLoggerv
- __57-[QPAssetManager _systemAssetPathsForContentType:locale:]_block_invoke
- __OBJC_$_CLASS_METHODS_QPAssetManager
- __ZL18assetManagerLoggerv
- ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8l
CStrings:
+ "(InRange(_%@%@%@, %d, 23) || InRange(_%@%@%@, 0, %d))"
+ "UAFAssetAccess"
+ "[QPNLU][qid=%ld][DateGround][LegacyParser] Skipping non-date lexeme type=%s flag=%u"
+ "[UAF] Asset set changed during enumeration for %s locale %s — discarding"
+ "[UAF] Failed to acquire scoped RBS assertion: %s"
+ "[UAF] Timed out waiting for UAF flock release; skipping enumeration (%s locale %s)"
+ "[UAF] UAFAssetAccess unavailable, using FinishTaskUninterruptable: %s"
+ "[UAF] Unknown enumeratorTag %s for content type %s — skipping"
+ "[UAF] _bulkPopulateForAssetSet: no content descriptors registered for %s — BUG"
+ "[UAF] retrieveAssetSet: returned nil for %s locale %s — skipping bulk populate"
+ "a person"
+ "assetName"
+ "com.apple.UnifiedAssetFramework"
+ "contentType"
+ "directory"
+ "entryKey"
+ "enumeratorTag"
+ "flat"
+ "perLocale"
- "[UAF] Failed to acquire scoped RBS assertion; skipping OTA retrieval this call: %s"
- "[UAF] Unknown content type: %s"
```
