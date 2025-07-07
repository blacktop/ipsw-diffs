## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0x1901b4
+343.3.0.0.0
+  __TEXT.__text: 0x191324
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x19a10
-  __TEXT.__const: 0x480
-  __TEXT.__gcc_except_tab: 0x1b220
-  __TEXT.__cstring: 0x5a8f
-  __TEXT.__oslogstring: 0xb547
+  __TEXT.__objc_methlist: 0x19a38
+  __TEXT.__const: 0x4b0
+  __TEXT.__gcc_except_tab: 0x1b24c
+  __TEXT.__cstring: 0x5aca
+  __TEXT.__oslogstring: 0xb958
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf408
+  __TEXT.__unwind_info: 0xf430
   __TEXT.__objc_classname: 0x470b
-  __TEXT.__objc_methname: 0x1af10
+  __TEXT.__objc_methname: 0x1af88
   __TEXT.__objc_methtype: 0xdf6b
-  __TEXT.__objc_stubs: 0x127e0
-  __DATA_CONST.__got: 0xc88
-  __DATA_CONST.__const: 0x4028
+  __TEXT.__objc_stubs: 0x12840
+  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__const: 0x4050
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6718
+  __DATA_CONST.__objc_selrefs: 0x6738
   __DATA_CONST.__objc_superrefs: 0x10f8
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x9c0
-  __AUTH_CONST.__cfstring: 0x75e0
+  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__cfstring: 0x7620
   __AUTH_CONST.__objc_const: 0x2c170
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0xa2f8
   __DATA.__objc_ivar: 0x1154
   __DATA.__data: 0xa70
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0804E71D-16A1-3126-A335-B82A9884C2D1
-  Functions: 9900
-  Symbols:   33637
-  CStrings:  8963
+  UUID: C614B290-660B-35BE-9027-C554D3D1F3D0
+  Functions: 9916
+  Symbols:   33683
+  CStrings:  8994
 
Symbols:
+ +[_LTDLanguageAssetService _applyRequiredProgressUpdate:]
+ +[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]
+ +[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:].cold.1
+ +[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]
+ +[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:].cold.1
+ +[_LTDUAFAssetService _registerForAsset:options:progress:completion:]
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.347
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.347.cold.1
+ ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke.36
+ ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke_2
+ ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.339
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.373
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.45
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.46
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.47
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.48
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39.cold.2
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.305
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.31
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.34
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke_2
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.53
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.54
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.57
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.58
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.58.cold.1
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.58.cold.2
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.cold.1
+ ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke
+ ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke.35
+ ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke.35.cold.1
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.312
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.316
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.313
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.313.cold.1
+ ___74-[_LTSpeechTranslationAssetInfo purgeAssetUserInitiated:queue:completion:]_block_invoke.34
+ ___74-[_LTSpeechTranslationAssetInfo purgeAssetUserInitiated:queue:completion:]_block_invoke.34.cold.1
+ ___78-[_LTSpeechTranslationAssetInfo downloadAssetsUserInitiated:queue:completion:]_block_invoke.31
+ ___78-[_LTSpeechTranslationAssetInfo downloadAssetsUserInitiated:queue:completion:]_block_invoke.31.cold.1
+ ___block_descriptor_32_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32bs_e24_v16?0"_LTDAssetModel"8ls32l8
+ ___block_descriptor_56_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_80_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
+ ___block_literal_global.324
+ ___block_literal_global.33
+ ___block_literal_global.341
+ ___block_literal_global.342
+ ___block_literal_global.355
+ ___block_literal_global.38
+ ___block_literal_global.41
+ ___block_literal_global.43
+ ___block_literal_global.54
+ __syncInstalledLocales.retryGate
+ _kUAFPolicyUseCellular
+ _objc_msgSend$_applyRequiredProgressUpdate:
+ _objc_msgSend$_registerForAsset:options:progress:completion:
+ _objc_msgSend$_syncInstalledLocalesWithCompletion:
+ _objc_msgSend$_syncInstalledLocalesWithRetry:completion:
+ _objc_msgSend$completedPercent
+ _objc_msgSend$downloadWithOptions:progress:then:
- +[_LTDUAFAssetService _registerForAsset:progress:completion:]
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.348
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.348.cold.1
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.340
- ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.374
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.36
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.37
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.38
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.39
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30.cold.2
- ___61+[_LTDUAFAssetService _registerForAsset:progress:completion:]_block_invoke
- ___61+[_LTDUAFAssetService _registerForAsset:progress:completion:]_block_invoke_2
- ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.307
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.62
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.63
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.66
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67.cold.1
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67.cold.2
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.314
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.318
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.315
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.315.cold.1
- ___74-[_LTSpeechTranslationAssetInfo purgeAssetUserInitiated:queue:completion:]_block_invoke.28
- ___74-[_LTSpeechTranslationAssetInfo purgeAssetUserInitiated:queue:completion:]_block_invoke.28.cold.1
- ___78-[_LTSpeechTranslationAssetInfo downloadAssetsUserInitiated:queue:completion:]_block_invoke.25
- ___78-[_LTSpeechTranslationAssetInfo downloadAssetsUserInitiated:queue:completion:]_block_invoke.25.cold.1
- ___block_descriptor_40_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e24_v16?0"_LTDAssetModel"8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
- ___block_literal_global.32
- ___block_literal_global.338
- ___block_literal_global.343
- ___block_literal_global.356
- _objc_msgSend$_registerForAsset:progress:completion:
- _objc_msgSend$downloadWithReservation:useBattery:progress:then:
- _objc_msgSend$flushCache
CStrings:
+ "%{public}@ ASR Model local file URL %@: for taskHint: %{public}@"
+ "%{public}@ ASR Model locale: %{public}@ model: %@"
+ "Add languages %{public}@"
+ "Cache progress update: %{public}@ [%f] required: %{BOOL}i cancelled: %{BOOL}i"
+ "Found matching ASR asset: %@ in assets for locale: %{public}@"
+ "Models - sourceASR: %{BOOL}i, targetASR: %{BOOL}i, mt: %{BOOL}i, taskHint: %{public}@, sourceASRModel: %@, targetASRModel: %@"
+ "OVAD signaled while waiting for pending locale swap. Reseting pending swap and restart state for source: %@"
+ "Remove languages %{public}@"
+ "SiriTTS voice lookup failure: %@"
+ "Source"
+ "Sync install begin"
+ "Sync install but no on-device mode supported"
+ "Sync install query selected begin"
+ "Sync install query selected ended"
+ "Sync install set assets begin"
+ "Sync install set assets ended"
+ "Sync install set assets progress: %@"
+ "Sync installed begin"
+ "Sync installed ended"
+ "Sync retry attempt %zd begin"
+ "Sync retry attempt %zd dispatch after %zd sec"
+ "Sync retry attempt %zd ended"
+ "Sync retry attempt %zd ended with failure: %@"
+ "Sync retry exhausted attemps, no further attempts will be made for the active request"
+ "TTS asset lookup failed for %@"
+ "Target"
+ "UAF asset download failure due to network issue"
+ "UAF asset download failure: %@"
+ "UAF progress %{public}@ status: %zd [%f]"
+ "_applyRequiredProgressUpdate:"
+ "_registerForAsset:options:progress:completion:"
+ "_syncInstalledLocalesWithCompletion:"
+ "_syncInstalledLocalesWithRetry:completion:"
+ "completedPercent"
+ "downloadWithOptions:progress:then:"
+ "v250501"
- "Could not determine the Siri voice for asset: %@"
- "Models - sourceASR: %{BOOL}i, targetASR: %{BOOL}i, mt: %{BOOL}i"
- "TextToSpeech.VoiceResources"
- "_registerForAsset:progress:completion:"
- "downloadWithReservation:useBattery:progress:then:"
- "en_IN"
- "v230614"

```
