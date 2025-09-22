## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-350.1.0.0.0
-  __TEXT.__text: 0x19337c
+353.3.0.0.0
+  __TEXT.__text: 0x193658
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x19bc0
   __TEXT.__const: 0x450
   __TEXT.__gcc_except_tab: 0x1b308
-  __TEXT.__cstring: 0x5ad7
-  __TEXT.__oslogstring: 0xc0da
+  __TEXT.__cstring: 0x5af4
+  __TEXT.__oslogstring: 0xc15d
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf448
+  __TEXT.__unwind_info: 0xf450
   __TEXT.__objc_classname: 0x4749
-  __TEXT.__objc_methname: 0x1b178
+  __TEXT.__objc_methname: 0x1b19f
   __TEXT.__objc_methtype: 0xdfac
-  __TEXT.__objc_stubs: 0x12940
+  __TEXT.__objc_stubs: 0x12980
   __DATA_CONST.__got: 0xca0
   __DATA_CONST.__const: 0x3f50
   __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6790
+  __DATA_CONST.__objc_selrefs: 0x67a0
   __DATA_CONST.__objc_superrefs: 0x1108
-  __DATA_CONST.__objc_arraydata: 0x230
+  __DATA_CONST.__objc_arraydata: 0x2a0
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x7680
+  __AUTH_CONST.__const: 0xac0
+  __AUTH_CONST.__cfstring: 0x7700
   __AUTH_CONST.__objc_const: 0x2c470
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xc8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27F12F27-99C8-3274-89F0-B5ABF9F4E610
-  Functions: 9945
-  Symbols:   33782
-  CStrings:  9048
+  UUID: F61BD88B-43B4-3C7B-BF8D-C97C3EA44AA8
+  Functions: 9951
+  Symbols:   33798
+  CStrings:  9063
 
Symbols:
+ +[_LTDAssetService registerAssetSetUpdateHandler]
+ +[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]
+ ___49+[_LTDAssetService registerAssetSetUpdateHandler]_block_invoke
+ ___49+[_LTDAssetService registerAssetSetUpdateHandler]_block_invoke.396
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.48
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.49
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.50
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.41.cold.2
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.38
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.38.cold.1
+ ___block_literal_global.395
+ ___block_literal_global.398
+ ___block_literal_global.403
+ ___block_literal_global.43
+ _objc_msgSend$describeObservations:
+ _objc_msgSend$registerAssetSetUpdateHandler
+ _objc_msgSend$syncInstalledLocalesOnAssetUpdate
- +[_LTDLanguageAssetCache _normalizeUpdateFromObservation:toObservation:]
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.44
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.45
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.46
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.2
- ___block_literal_global.394
- ___block_literal_global.42
- ___block_literal_global.53
- _objc_msgSend$_normalizeUpdateFromObservation:toObservation:
CStrings:
+ "ASR asset update event"
+ "Obsv xpcmsg [%@]"
+ "Sync on asset update begin"
+ "Sync on asset update failure: %@"
+ "Sync on asset update succeeded"
+ "bti-messages"
+ "bti-speech"
+ "describeObservations:"
+ "nl_NL"
+ "pt"
+ "registerAssetSetUpdateHandler"
+ "syncInstalledLocalesOnAssetUpdate"
+ "tr_TR"
- "_normalizeUpdateFromObservation:toObservation:"
- "messaging"

```
