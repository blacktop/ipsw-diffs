## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser`

```diff

-3600.31.21.11.1
-  __TEXT.__text: 0x113de4
-  __TEXT.__objc_methlist: 0x2a94
-  __TEXT.__const: 0x2d28
-  __TEXT.__gcc_except_tab: 0x13798
-  __TEXT.__oslogstring: 0x7ace
-  __TEXT.__cstring: 0xd345
+3605.7.1.0.0
+  __TEXT.__text: 0x1139f8
+  __TEXT.__objc_methlist: 0x29ec
+  __TEXT.__const: 0x2d48
+  __TEXT.__gcc_except_tab: 0x13708
+  __TEXT.__oslogstring: 0x7a5e
+  __TEXT.__cstring: 0xd355
   __TEXT.__ustring: 0x112
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__swift5_typeref: 0x5c2

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5af8
+  __TEXT.__unwind_info: 0x5ad0
   __TEXT.__eh_frame: 0xc90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x21a8
+  __DATA_CONST.__objc_selrefs: 0x2130
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x1ff8
   __DATA_CONST.__got: 0x730
   __AUTH_CONST.__const: 0x2f70
-  __AUTH_CONST.__cfstring: 0x12800
-  __AUTH_CONST.__objc_const: 0x46f8
+  __AUTH_CONST.__cfstring: 0x127a0
+  __AUTH_CONST.__objc_const: 0x4650
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b18
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x15d8
+  __AUTH_CONST.__auth_got: 0x15e0
   __AUTH.__objc_data: 0x8e8
   __AUTH.__data: 0x448
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x30c
   __DATA.__data: 0x11b0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x738

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4297
-  Symbols:   6885
-  CStrings:  3403
+  Functions: 4287
+  Symbols:   6871
+  CStrings:  3399
 
Symbols:
+ GCC_except_table140
+ GCC_except_table195
+ GCC_except_table247
+ _CFStringCompareWithOptions
+ __OBJC_$_CLASS_METHODS_QPAssetManager
+ __ZL18assetManagerLoggerv
+ __ZN2QP13isHomeDaypartENS_22QPDateComponentsPeriodE
+ __ZN2QP25getHomeDaypartOffsetHoursENS_22QPDateComponentsPeriodE
+ __ZN2QPL14endsWithWordCIEPK10__CFStringlS2_
+ __ZNK2QP19ParserConfiguration17languageIsEnglishEv
+ __ZNK2QP19ParserConfiguration29embeddingStringMaskForArgTypeE15QUIntentArgType
+ __ZNK2QP19ParserConfiguration30embeddingStringExcludesArgTypeE15QUIntentArgType
+ ___block_descriptor_64_ea8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- +[QPAssetManager _contentTypesForAssetSet:]
- +[QPAssetManager _isKnownContentType:forAssetSet:]
- +[QPAssetManager(Testing) _test_assetNameEmbedding]
- +[QPAssetManager(Testing) _test_assetNameGeo]
- +[QPAssetManager(Testing) _test_assetNameQueryParser]
- +[QPAssetManager(Testing) _test_assetNameQueryUnderstanding]
- +[QPAssetManager(Testing) _test_assetNameSFC]
- +[QPAssetManager(Testing) _test_assetNameSafety]
- +[QPAssetManager(Testing) _test_assetSetQueryParserOverrides]
- +[QPAssetManager(Testing) _test_assetSetQueryParser]
- -[QPAssetManager _bulkPopulateForAssetSet:locale:]
- -[QPAssetManager _cacheKeyForAssetSet:locale:contentType:]
- -[QPAssetManager(Testing) _test_bulkPopulateForAssetSet:locale:]
- -[QPAssetManager(Testing) _test_bulkPopulateShortCircuitCount]
- GCC_except_table193
- GCC_except_table244
- _OBJC_IVAR_$_QPAssetManager._locked_bulkPopulateShortCircuitCount
- __OBJC_$_CLASS_METHODS_QPAssetManager(Testing)
- ___50-[QPAssetManager _bulkPopulateForAssetSet:locale:]_block_invoke
- ___60-[QPAssetManager _filePathsDictionaryForContentType:locale:]_block_invoke_2
- ___62-[QPAssetManager(Testing) _test_bulkPopulateShortCircuitCount]_block_invoke
- ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- _objc_msgSend$_bulkPopulateForAssetSet:locale:
- _objc_msgSend$_cacheKeyForAssetSet:locale:contentType:
- _objc_msgSend$_contentTypesForAssetSet:
- _objc_msgSend$_isKnownContentType:forAssetSet:
- _objc_msgSend$addEntriesFromDictionary:
CStrings:
+ "(InRange(_%@%@%@, %d, 23) || InRange(_%@%@%@, 0, %d))"
+ "[QPNLU][qid=%ld][DateGround][LegacyParser] Skipping non-date lexeme type=%s flag=%u"
+ "[UAF] Unknown content type: %s"
+ "a person"
- "[UAF] Unknown enumeratorTag %s for content type %s — skipping"
- "[UAF] _bulkPopulateForAssetSet: no content descriptors registered for %s — BUG"
- "[UAF] retrieveAssetSet: returned nil for %s locale %s — skipping bulk populate"
- "assetName"
- "contentType"
- "enumeratorTag"
- "flat"
- "perLocale"
```
