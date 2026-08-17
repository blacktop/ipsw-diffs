## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser`

```diff

-3600.31.21.0.0
-  __TEXT.__text: 0x116d10
-  __TEXT.__objc_methlist: 0x29ec
+3600.31.21.11.1
+  __TEXT.__text: 0x11766c
+  __TEXT.__objc_methlist: 0x2a94
   __TEXT.__const: 0x2d28
-  __TEXT.__gcc_except_tab: 0x1369c
-  __TEXT.__oslogstring: 0x7a0e
-  __TEXT.__cstring: 0xd315
+  __TEXT.__gcc_except_tab: 0x13798
+  __TEXT.__oslogstring: 0x7ace
+  __TEXT.__cstring: 0xd345
   __TEXT.__ustring: 0x112
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__swift5_typeref: 0x5c2

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x52c0
+  __TEXT.__unwind_info: 0x5300
   __TEXT.__eh_frame: 0xc90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2130
+  __DATA_CONST.__objc_selrefs: 0x21a8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x1ff8
   __DATA_CONST.__got: 0x730
   __AUTH_CONST.__const: 0x2f70
-  __AUTH_CONST.__cfstring: 0x12760
-  __AUTH_CONST.__objc_const: 0x4650
+  __AUTH_CONST.__cfstring: 0x12800
+  __AUTH_CONST.__objc_const: 0x46f8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b18
   __AUTH_CONST.__objc_arrayobj: 0x390

   __AUTH_CONST.__auth_got: 0x15d8
   __AUTH.__objc_data: 0x8e8
   __AUTH.__data: 0x448
-  __DATA.__objc_ivar: 0x30c
+  __DATA.__objc_ivar: 0x310
   __DATA.__data: 0x11b0
   __DATA.__bss: 0x1560
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4295
-  Symbols:   6863
-  CStrings:  3396
+  Functions: 4311
+  Symbols:   6885
+  CStrings:  3403
 
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
+ _OBJC_IVAR_$_QPAssetManager._locked_bulkPopulateShortCircuitCount
+ __OBJC_$_CLASS_METHODS_QPAssetManager(Testing)
+ ___50-[QPAssetManager _bulkPopulateForAssetSet:locale:]_block_invoke
+ ___60-[QPAssetManager _filePathsDictionaryForContentType:locale:]_block_invoke_2
+ ___62-[QPAssetManager(Testing) _test_bulkPopulateShortCircuitCount]_block_invoke
+ ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ _objc_msgSend$_bulkPopulateForAssetSet:locale:
+ _objc_msgSend$_cacheKeyForAssetSet:locale:contentType:
+ _objc_msgSend$_contentTypesForAssetSet:
+ _objc_msgSend$_isKnownContentType:forAssetSet:
+ _objc_msgSend$addEntriesFromDictionary:
- __OBJC_$_CLASS_METHODS_QPAssetManager
- __ZL18assetManagerLoggerv
- ___block_descriptor_64_ea8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
CStrings:
+ "[UAF] Unknown enumeratorTag %s for content type %s — skipping"
+ "[UAF] _bulkPopulateForAssetSet: no content descriptors registered for %s — BUG"
+ "[UAF] retrieveAssetSet: returned nil for %s locale %s — skipping bulk populate"
+ "assetName"
+ "contentType"
+ "enumeratorTag"
+ "flat"
+ "perLocale"
- "[UAF] Unknown content type: %s"
```
