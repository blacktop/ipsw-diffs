## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-345.0.0.0.0
-  __TEXT.__text: 0x1902d8
+348.1.0.0.0
+  __TEXT.__text: 0x190d8c
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x199b0
-  __TEXT.__const: 0x440
-  __TEXT.__gcc_except_tab: 0x1b2a4
-  __TEXT.__cstring: 0x5a73
-  __TEXT.__oslogstring: 0xb933
+  __TEXT.__objc_methlist: 0x199f0
+  __TEXT.__const: 0x450
+  __TEXT.__gcc_except_tab: 0x1b308
+  __TEXT.__cstring: 0x5a8a
+  __TEXT.__oslogstring: 0xbb83
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf3f0
+  __TEXT.__unwind_info: 0xf410
   __TEXT.__objc_classname: 0x470b
-  __TEXT.__objc_methname: 0x1ae42
+  __TEXT.__objc_methname: 0x1aec9
   __TEXT.__objc_methtype: 0xdf6b
-  __TEXT.__objc_stubs: 0x126e0
+  __TEXT.__objc_stubs: 0x12760
   __DATA_CONST.__got: 0xc98
-  __DATA_CONST.__const: 0x3ec0
+  __DATA_CONST.__const: 0x3ee8
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x66d0
+  __DATA_CONST.__objc_selrefs: 0x66f8
   __DATA_CONST.__objc_superrefs: 0x10f8
-  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x7600
+  __AUTH_CONST.__const: 0xa60
+  __AUTH_CONST.__cfstring: 0x7620
   __AUTH_CONST.__objc_const: 0x2c150
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8

   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0xa2f8
   __DATA.__objc_ivar: 0x1154
-  __DATA.__data: 0xa70
-  __DATA.__bss: 0x110
+  __DATA.__data: 0xa68
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xc58
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7540FDFB-DAAF-35F5-9F45-3C5CC72AA76D
-  Functions: 9887
-  Symbols:   33602
-  CStrings:  8972
+  UUID: 08B6A923-8668-3892-94D5-00BCF1F934AD
+  Functions: 9898
+  Symbols:   33638
+  CStrings:  8989
 
Symbols:
+ +[_LTDASRAssetService cancelDeferredUnsubscribeTimer]
+ +[_LTDASRAssetService deferredUnsubscribeAssets]
+ +[_LTDASRAssetService deferredUnsubscribeAssets].cold.1
+ +[_LTDASRAssetService deferredUnsubscribe]
+ +[_LTDASRAssetService updateDeferredUnsubscribeTimer]
+ +[_LTDASRAssetService updateDeferredUnsubscribeTimer].cold.1
+ -[_LTOfflineTranslationEngine _performCancelRecognition:]
+ __LTOSLogAssetObservation
+ __LTOSLogAssetObservation.cold.1
+ __LTOSLogAssetObservation.log
+ __LTOSLogAssetObservation.onceToken
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.316
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.341
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.341.cold.1
+ ___48+[_LTDASRAssetService deferredUnsubscribeAssets]_block_invoke
+ ___53+[_LTDASRAssetService updateDeferredUnsubscribeTimer]_block_invoke
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.364
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.299
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.338
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.339
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.333
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353.cold.1
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.309
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.310
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.311
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.317
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.312
+ ____LTOSLogAssetObservation_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_literal_global.294
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.308
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.329
+ ___block_literal_global.344
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.40
+ __deferredUnsubscribeTimer
+ __subscriptionLock
+ _deferredUnsubscribeAssets._deferredUnsubscribeAssets
+ _deferredUnsubscribeAssets.onceToken
+ _objc_msgSend$_performCancelRecognition:
+ _objc_msgSend$cancelDeferredUnsubscribeTimer
+ _objc_msgSend$deferredUnsubscribe
+ _objc_msgSend$deferredUnsubscribeAssets
+ _objc_msgSend$updateDeferredUnsubscribeTimer
- +[_LTDASRAssetService _subscribe:progress:completion:].cold.1
- ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.313
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.338
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.338.cold.1
- ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.361
- ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.296
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.335
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.336
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.330
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.350
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.350.cold.1
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.306
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.307
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.308
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.314
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.309
- ___block_literal_global.296
- ___block_literal_global.301
- ___block_literal_global.305
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.316
- ___block_literal_global.320
- ___block_literal_global.338
- ___block_literal_global.341
- ___block_literal_global.346
- _objc_msgSend$cancelRecognition:
CStrings:
+ "ASR assets purging timer fired"
+ "ASR unsubscribe for %{public}@"
+ "AssetObservation"
+ "Canceling recognition in offline translation engine"
+ "Cancelling language observations for client %{public}@; identifier: %{public}@"
+ "Cancelling status updates because disconnecting from client %{public}@; identifier: %{public}@"
+ "Deliver Stashed Barrier Streaming Speech Result: %p"
+ "Starting language observations for client %{private}@; trusted: %{BOOL}i; taskHint: %{public}@; identifier: %{public}@"
+ "Stopping language observations for client %{public}@; taskHint: %{public}@; identifier: %{public}@"
+ "Updating ASR assets purging timer"
+ "_performCancelRecognition:"
+ "cancelDeferredUnsubscribeTimer"
+ "deferredUnsubscribe"
+ "deferredUnsubscribeAssets"
+ "updateDeferredUnsubscribeTimer"
+ "zh_TW"

```
