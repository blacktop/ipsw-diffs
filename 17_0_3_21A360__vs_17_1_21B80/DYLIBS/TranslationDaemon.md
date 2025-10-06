## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-249.2.0.0.0
-  __TEXT.__text: 0x18bbb4
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x188bc
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x4c8f
-  __TEXT.__oslogstring: 0x85f1
-  __TEXT.__gcc_except_tab: 0x19bc0
+252.2.1.0.0
+  __TEXT.__text: 0x18db74
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x18a74
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x4e72
+  __TEXT.__oslogstring: 0x8893
+  __TEXT.__gcc_except_tab: 0x19c38
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0xf9c4
+  __TEXT.__unwind_info: 0xfa70
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x4806
-  __TEXT.__objc_methname: 0x181b1
-  __TEXT.__objc_methtype: 0xde85
-  __TEXT.__objc_stubs: 0x10080
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x3378
-  __DATA_CONST.__objc_classlist: 0x11c8
+  __TEXT.__objc_classname: 0x4858
+  __TEXT.__objc_methname: 0x18769
+  __TEXT.__objc_methtype: 0xe022
+  __TEXT.__objc_stubs: 0x104c0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x3428
+  __DATA_CONST.__objc_classlist: 0x11e0
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fca8
-  __DATA_CONST.__objc_selrefs: 0x5ba0
+  __DATA_CONST.__objc_const: 0x1ff08
+  __DATA_CONST.__objc_selrefs: 0x5cf0
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__objc_const: 0xc890
-  __AUTH_CONST.__cfstring: 0x6780
+  __AUTH_CONST.__objc_const: 0xc9f8
+  __AUTH_CONST.__cfstring: 0x6960
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH.__objc_data: 0xa870
-  __DATA.__objc_classrefs: 0x10d8
-  __DATA.__objc_superrefs: 0x1158
-  __DATA.__objc_ivar: 0x10a0
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH.__objc_data: 0xa960
+  __DATA.__objc_classrefs: 0x10f0
+  __DATA.__objc_superrefs: 0x1170
+  __DATA.__objc_ivar: 0x10d0
   __DATA.__data: 0x8f0
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4409C142-2D5D-3930-9B30-D18AE5A5F5A2
-  Functions: 10175
-  Symbols:   32384
-  CStrings:  8068
+  UUID: 0E715300-78A4-3FCD-9A54-7AFB6EF0CA80
+  Functions: 10225
+  Symbols:   32573
+  CStrings:  8186
 
Symbols:
+ +[NSString(VS4CC) vs_stringFrom4CC:]
+ +[_LTAudioDecoder sharedInstance]
+ +[_LTDAssetService _forceOneTimeCatalogRefresh]
+ +[_LTDAssetService _isObsoleteCatalogType:]
+ +[_LTDAssetService _isObsoleteCatalogType:].cold.1
+ +[_LTDAssetService _serviceProviderForAssetType:]
+ +[_LTDAssetService _serviceProviderForAssetType:].cold.1
+ +[_LTDAssetService _test_resetForceOneTimeCatalogRefresh]
+ +[_LTDAssetService assetProviderFixture]
+ +[_LTDAssetService assetTypeForAssetIdentifier:].cold.1
+ +[_LTDAssetService setAssetProviderFixture:]
+ +[_LTDContinuationOperation continuationOperationWithBlock:]
+ +[_LTDLanguageAssetService _availableAssetsWithCompletion:]
+ +[_LTDLanguageAssetService _installedAssetsWithCompletion:]
+ +[_LTDLanguageAssetService _languageAssetFilterDescription:]
+ +[_LTDLanguageAssetService _languageAssetFilterFromOptions:]
+ +[_LTDLanguageAssetService _languageAssetFilterFromOptions:].cold.1
+ +[_LTDLanguageAssetService _languageAssetFilterFromOptions:].cold.2
+ +[_LTDLanguageAssetService _selectedAssetsWithCompletion:]
+ +[_LTWordTimingInfo(Daemon) extraBytesFromUTF8ToUTF16With:totalLength:begin:end:]
+ +[_LTWordTimingInfo(Daemon) extraBytesFromUTF8ToUTF16With:totalLength:begin:end:].cold.1
+ +[_LTWordTimingInfo(Daemon) utf16TimingInfoWithUTF8Range:withText:]
+ +[_LTWordTimingInfo(Daemon) wordTimingInfoFromArray:text:]
+ +[_LTWordTimingInfo(Daemon) wordTimingWithTextRangeInfoFrom:wordTimingInfo:]
+ -[_LTAudioDecoder _audioDecoderFrom:to:]
+ -[_LTAudioDecoder _audioDecoderFrom:to:].cold.1
+ -[_LTAudioDecoder beginChunkDecoderForStreamDescription:]
+ -[_LTAudioDecoder dealloc]
+ -[_LTAudioDecoder decodeChunk:outError:]
+ -[_LTAudioDecoder decodeChunks:from:to:outError:]
+ -[_LTAudioDecoder endChunkDecoding]
+ -[_LTDContinuationOperation cancel]
+ -[_LTDContinuationOperation dealloc]
+ -[_LTDContinuationOperation dealloc].cold.1
+ -[_LTDContinuationOperation initWithContinuationBlock:]
+ -[_LTDContinuationOperation initWithContinuationBlock:].cold.1
+ -[_LTDContinuationOperation isAsynchronous]
+ -[_LTDContinuationOperation isCancelled]
+ -[_LTDContinuationOperation isFinished]
+ -[_LTDContinuationOperation operationTimeout]
+ -[_LTDContinuationOperation setAsynchronous:]
+ -[_LTDContinuationOperation setCancelled:]
+ -[_LTDContinuationOperation setFinished:]
+ -[_LTDContinuationOperation setOperationTimeout:]
+ -[_LTDContinuationOperation start]
+ -[_LTDContinuationOperation start].cold.1
+ -[_LTDLanguageAssetCache isReadyForFilter:]
+ -[_LTDLanguageAssetCache markReadyForFilter:]
+ -[_LTDLanguageAssetCache readyFilterSet]
+ -[_LTDLanguageAssetCache setReadyFilterSet:]
+ -[_LTDSELFLoggingFrameworkRequest isResponseReceivedEventSent]
+ -[_LTDSELFLoggingFrameworkRequest setIsResponseReceivedEventSent:]
+ -[_LTDTranslationOperationScheduler .cxx_destruct]
+ -[_LTDTranslationOperationScheduler initWithQueue:]
+ -[_LTDTranslationOperationScheduler offlineOperationTimeout]
+ -[_LTDTranslationOperationScheduler scheduleOperation:route:]
+ -[_LTDTranslationOperationScheduler scheduleOperation:route:].cold.1
+ -[_LTDTranslationOperationScheduler scheduleOperation:route:].cold.2
+ -[_LTDTranslationOperationScheduler scheduleOperationWithRoute:block:]
+ -[_LTDTranslationOperationScheduler setOfflineOperationTimeout:]
+ -[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:]
+ -[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:].cold.1
+ -[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:].cold.2
+ -[_LTServerSpeakSession _playback:context:completion:audioStartHandler:].cold.4
+ -[_LTServerSpeakSession _playback:context:completion:audioStartHandler:].cold.5
+ _AudioConverterReset
+ _CFStringCreateWithCString
+ _OBJC_CLASS_$_NSBlockOperation
+ _OBJC_CLASS_$__LTAudioDecoder
+ _OBJC_CLASS_$__LTDContinuationOperation
+ _OBJC_CLASS_$__LTDTranslationOperationScheduler
+ _OBJC_IVAR_$__LTAudioDecoder._decoder
+ _OBJC_IVAR_$__LTAudioDecoder._fromASBD
+ _OBJC_IVAR_$__LTAudioDecoder._toASBD
+ _OBJC_IVAR_$__LTDContinuationOperation._isAsynchronous
+ _OBJC_IVAR_$__LTDContinuationOperation._isCancelled
+ _OBJC_IVAR_$__LTDContinuationOperation._isFinished
+ _OBJC_IVAR_$__LTDContinuationOperation._lock
+ _OBJC_IVAR_$__LTDContinuationOperation._operationTimeout
+ _OBJC_IVAR_$__LTDLanguageAssetCache._readyFilterSet
+ _OBJC_IVAR_$__LTDSELFLoggingFrameworkRequest._isResponseReceivedEventSent
+ _OBJC_IVAR_$__LTDTranslationOperationScheduler._offlineEngineQueue
+ _OBJC_IVAR_$__LTDTranslationOperationScheduler._offlineOperationTimeout
+ _OBJC_IVAR_$__LTDTranslationOperationScheduler._onlineEngineQueue
+ _OBJC_IVAR_$__LTServerSpeakSession._converter
+ _OBJC_IVAR_$__LTTranslationServer._translationEngineScheduler
+ _OBJC_METACLASS_$_NSBlockOperation
+ _OBJC_METACLASS_$__LTAudioDecoder
+ _OBJC_METACLASS_$__LTDContinuationOperation
+ _OBJC_METACLASS_$__LTDTranslationOperationScheduler
+ _VSCreate4CCString
+ __DefaultRuneLocale
+ __LTAudioFormat48khzPCM
+ __LTTranslationInternalErrorDomain
+ __OBJC_$_CATEGORY_NSString_$_VS4CC
+ __OBJC_$_CLASS_METHODS_NSString(VS4CC|LTStatistics)
+ __OBJC_$_CLASS_METHODS__LTAudioDecoder
+ __OBJC_$_CLASS_METHODS__LTDContinuationOperation
+ __OBJC_$_INSTANCE_METHODS_NSString(VS4CC|LTStatistics)
+ __OBJC_$_INSTANCE_METHODS__LTAudioDecoder
+ __OBJC_$_INSTANCE_METHODS__LTDContinuationOperation
+ __OBJC_$_INSTANCE_METHODS__LTDTranslationOperationScheduler
+ __OBJC_$_INSTANCE_VARIABLES__LTAudioDecoder
+ __OBJC_$_INSTANCE_VARIABLES__LTDContinuationOperation
+ __OBJC_$_INSTANCE_VARIABLES__LTDTranslationOperationScheduler
+ __OBJC_$_PROP_LIST__LTDContinuationOperation
+ __OBJC_$_PROP_LIST__LTDTranslationOperationScheduler
+ __OBJC_CLASS_RO_$__LTAudioDecoder
+ __OBJC_CLASS_RO_$__LTDContinuationOperation
+ __OBJC_CLASS_RO_$__LTDTranslationOperationScheduler
+ __OBJC_METACLASS_RO_$__LTAudioDecoder
+ __OBJC_METACLASS_RO_$__LTDContinuationOperation
+ __OBJC_METACLASS_RO_$__LTDTranslationOperationScheduler
+ ___107-[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:]_block_invoke
+ ___33+[_LTAudioDecoder sharedInstance]_block_invoke
+ ___34-[_LTDContinuationOperation start]_block_invoke
+ ___34-[_LTDContinuationOperation start]_block_invoke.cold.1
+ ___40-[_LTAudioDecoder decodeChunk:outError:]_block_invoke
+ ___40-[_LTAudioDecoder decodeChunk:outError:]_block_invoke.cold.1
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.40
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.40.cold.1
+ ___46-[_LTDLanguageAssetCache assetsFilteredUsing:]_block_invoke
+ ___46-[_LTDLanguageAssetCache assetsFilteredUsing:]_block_invoke_2
+ ___48+[_LTDAssetService assetsForLocales:completion:]_block_invoke.66
+ ___48+[_LTDAssetService assetsForLocales:completion:]_block_invoke.cold.1
+ ___55-[_LTDContinuationOperation initWithContinuationBlock:]_block_invoke
+ ___55-[_LTDContinuationOperation initWithContinuationBlock:]_block_invoke_2
+ ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.33
+ ___58+[_LTDLanguageAssetService _selectedAssetsWithCompletion:]_block_invoke
+ ___59+[_LTDLanguageAssetService _availableAssetsWithCompletion:]_block_invoke
+ ___59+[_LTDLanguageAssetService _availableAssetsWithCompletion:]_block_invoke.cold.1
+ ___59+[_LTDLanguageAssetService _installedAssetsWithCompletion:]_block_invoke
+ ___59+[_LTDLanguageAssetService _installedAssetsWithCompletion:]_block_invoke.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24.cold.2
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.31
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.31.cold.1
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.33
+ ___63+[_LTDAssetService downloadAssets:options:progress:completion:]_block_invoke.13
+ ___65-[_LTTranslationServer translateSentence:withContext:completion:]_block_invoke.20
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.16
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.21
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.21.cold.1
+ ___67-[_LTTranslationServer startSpeechTranslationWithContext:delegate:]_block_invoke.37
+ ___76+[_LTWordTimingInfo(Daemon) wordTimingWithTextRangeInfoFrom:wordTimingInfo:]_block_invoke
+ ___78-[_LTTranslationServer startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.29
+ ___79-[_LTOnlineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.250
+ ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.22
+ ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.22.cold.1
+ ___block_descriptor_40_e8_32s_e25_v24?0"_LTAudioData"8d16ls32l8
+ ___block_descriptor_40_e8_32s_e31_B16?0"_LTLanguageAssetModel"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40bs_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40bs_e42_v24?0"_LTTranslationResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e86_i32?0^I8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16^^{AudioStreamPacketDescription}24lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs_e14_v16?0?<v?>8ls32l8s48l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e44_v24?0"FTTextToSpeechResponse"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e14_v16?0?<v?>8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e33_v32?0"FTWordTimingInfo"8Q16^B24lr56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56w_e14_v16?0?<v?>8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72w_e14_v16?0?<v?>8lw72l8s32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72w_e14_v16?0?<v?>8lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___maskrune
+ __assetProviderFixture
+ __hasForcedOneTimeCatalogRefresh
+ __unnamed_array_storage.240
+ _objc_msgSend$_audioDecoderFrom:to:
+ _objc_msgSend$_availableAssetsWithCompletion:
+ _objc_msgSend$_createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:
+ _objc_msgSend$_forceOneTimeCatalogRefresh
+ _objc_msgSend$_installedAssetsWithCompletion:
+ _objc_msgSend$_isObsoleteCatalogType:
+ _objc_msgSend$_languageAssetFilterDescription:
+ _objc_msgSend$_languageAssetFilterFromOptions:
+ _objc_msgSend$_selectedAssetsWithCompletion:
+ _objc_msgSend$_serviceProviderForAssetType:
+ _objc_msgSend$addExecutionBlock:
+ _objc_msgSend$addOperation:
+ _objc_msgSend$beginChunkDecoderForStreamDescription:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$continuationOperationWithBlock:
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$decodeChunk:outError:
+ _objc_msgSend$decodeChunks:from:to:outError:
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$endChunkDecoding
+ _objc_msgSend$extraBytesFromUTF8ToUTF16With:totalLength:begin:end:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$initWithContinuationBlock:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$isAsynchronous
+ _objc_msgSend$isReadyForFilter:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$lt_filterUsingBlock:
+ _objc_msgSend$markReadyForFilter:
+ _objc_msgSend$sampleIndex
+ _objc_msgSend$scheduleOperation:route:
+ _objc_msgSend$scheduleOperationWithRoute:block:
+ _objc_msgSend$setFinished:
+ _objc_msgSend$setOperationTimeout:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setStartTime:
+ _objc_msgSend$setTextRange:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$startTime
+ _objc_msgSend$textRange
+ _objc_msgSend$ttsAudioStarted:duration:
+ _objc_msgSend$utf16TimingInfoWithUTF8Range:withText:
+ _objc_msgSend$vs_stringFrom4CC:
+ _objc_msgSend$willChangeValueForKey:
+ _objc_msgSend$wordTimingInfo
+ _objc_msgSend$wordTimingInfoFromArray:text:
+ _objc_msgSend$wordTimingWithTextRangeInfoFrom:wordTimingInfo:
+ _sharedInstance.sSharedInstance
+ _snprintf
- +[_LTDAssetService initialize]
- +[_LTDAssetService needsCatalogRefresh].cold.1
- +[_LTDAssetService serviceProviderForAsset:]
- +[_LTDAssetService serviceProviderForAssetIdentifier:]
- +[_LTDAssetService serviceProviderForAssetType:]
- +[_LTDAssetService serviceProvider]
- +[_LTDAssetService setServiceProvider:]
- +[_LTDLanguageAssetService assetsWithCompletion:]
- +[_LTDLanguageAssetService availableAssetsWithCompletion:]
- +[_LTDLanguageAssetService filterAssets:options:]
- +[_LTDLanguageAssetService installedAssetsWithCompletion:]
- +[_LTDLanguageAssetService selectedAssetsWithCompletion:]
- +[_LTWordTimingInfo(Daemon) wordTimingInfoFromArray:]
- -[_LTDLanguageAssetCache _hardReset]
- -[_LTDLanguageAssetCache assetForIdentifier:createIfNotFound:]
- -[_LTDLanguageAssetCache isHot]
- -[_LTDLanguageAssetCache setIsHot:]
- -[_LTOnlineTranslationEngine _translateParagraph:index:context:completion:]
- -[_LTOnlineTranslationEngine _translateParagraph:index:context:completion:].cold.1
- -[_LTOnlineTranslationEngine _translateParagraph:index:context:completion:].cold.2
- _OBJC_IVAR_$__LTDLanguageAssetCache._isHot
- _OBJC_IVAR_$__LTOnlineTranslationEngine._sendQueue
- _OBJC_IVAR_$__LTOnlineTranslationEngine._service
- __OBJC_$_CATEGORY_NSString_$_LTStatistics
- __OBJC_$_INSTANCE_METHODS_NSString(LTStatistics)
- ___31-[_LTDLanguageAssetCache reset]_block_invoke
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.36
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.36.cold.1
- ___48+[_LTDAssetService assetsForLocales:completion:]_block_invoke_2
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.4
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.4.cold.1
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.5
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.5.cold.1
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.6
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.6.cold.1
- ___49+[_LTDLanguageAssetService assetsWithCompletion:]_block_invoke.cold.1
- ___53+[_LTWordTimingInfo(Daemon) wordTimingInfoFromArray:]_block_invoke
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.28
- ___57+[_LTDLanguageAssetService assetsWithOptions:completion:]_block_invoke
- ___57+[_LTDLanguageAssetService assetsWithOptions:completion:]_block_invoke.cold.1
- ___57+[_LTDLanguageAssetService selectedAssetsWithCompletion:]_block_invoke
- ___58+[_LTDLanguageAssetService availableAssetsWithCompletion:]_block_invoke
- ___58+[_LTDLanguageAssetService availableAssetsWithCompletion:]_block_invoke.cold.1
- ___58+[_LTDLanguageAssetService installedAssetsWithCompletion:]_block_invoke
- ___58+[_LTDLanguageAssetService installedAssetsWithCompletion:]_block_invoke.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.20
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.20.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.20.cold.2
- ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.29
- ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.29.cold.1
- ___63+[_LTDAssetService downloadAssets:options:progress:completion:]_block_invoke.9
- ___65-[_LTTranslationServer translateSentence:withContext:completion:]_block_invoke.19
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.12
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.17
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.17.cold.1
- ___67-[_LTTranslationServer startSpeechTranslationWithContext:delegate:]_block_invoke.31
- ___75-[_LTOnlineTranslationEngine _translateParagraph:index:context:completion:]_block_invoke
- ___78-[_LTTranslationServer startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.27
- ___79-[_LTOnlineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.251
- ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.21
- ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.21.cold.1
- ___block_descriptor_32_e26_16?0"FTWordTimingInfo"8l
- ___block_descriptor_40_e8_32w_e29_v24?0"NSArray"8"NSError"16lw32l8
- ___block_descriptor_48_e8_32bs_e27_v24?0"NSURL"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32bs_e42_v24?0"_LTTranslationResult"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8lw32l8
- ___block_descriptor_56_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_56_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_ea8_32s40s48bs_e44_v24?0"FTTextToSpeechResponse"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_72_e8_32bs40r48r56r64r_e5_v8?0lr40l8r48l8r56l8r64l8s32l8
- ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s56l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
- __serviceProvider
- __unnamed_array_storage.241
- _objc_msgSend$_hardReset
- _objc_msgSend$_translateParagraph:index:context:completion:
- _objc_msgSend$assetForIdentifier:createIfNotFound:
- _objc_msgSend$assetsWithCompletion:
- _objc_msgSend$availableAssetsWithCompletion:
- _objc_msgSend$filterAssets:options:
- _objc_msgSend$initWithFTWordTimingInfo:
- _objc_msgSend$initWithLocale:
- _objc_msgSend$isHot
- _objc_msgSend$selectedAssetsWithCompletion:
- _objc_msgSend$serviceProviderForAsset:
- _objc_msgSend$serviceProviderForAssetIdentifier:
- _objc_msgSend$setTimestamp:
- _objc_msgSend$wordTimingInfoFromArray:
CStrings:
+ "\n"
+ "\v\x13"
+ "%d"
+ ".available"
+ ".installed"
+ ".selected"
+ "0x%x"
+ "@\"AVAudioConverter\""
+ "@\"_LTDTranslationOperationScheduler\""
+ "@112@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24{AudioStreamBasicDescription=dIIIIIIII}64^@104"
+ "@20@0:8i16"
+ "@32@0:8q16@?24"
+ "@56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
+ "Asset options contains multiple filter options including installed, will only use installed"
+ "Asset options contains multiple filter options including selected, will only use selected"
+ "B16@?0@\"_LTLanguageAssetModel\"8"
+ "B24@0:8Q16"
+ "Continuation operation dealloc: %p"
+ "Continuation operation encountered wait timeout event"
+ "Continuation operation finish: %p"
+ "Continuation operation initialized: %p"
+ "Continuation operation start: %p"
+ "Converted %ld bytes to %ld bytes"
+ "Could not create Opus decoder: %{public}@"
+ "Could not finish decoding, res %@"
+ "Decoding to PCM 48kHz failed: %@"
+ "Detected obsolete catalog type: %{public}@"
+ "Duration: %f. Total number of frames: %ld"
+ "Enqueued %{public}@ audio buffer at sample title: %.2f, size: %zu"
+ "Failed to create opus decoder"
+ "Failed to refresh catalog"
+ "Language asset service received state request with filter %{public}@"
+ "No config asset found while resolving assets for locales"
+ "No config asset in result from async catalog request"
+ "No config asset in result from sync catalog request"
+ "No implementation, should only be called on concrete service providers"
+ "No service provider defined for asset type: %{public}@"
+ "Only expecting to get 1 packet at a time, not %lu"
+ "Opus"
+ "Out of word boundary: %ld is greater than %ld"
+ "PCM"
+ "Pre-decode packet count: %ld. Post-decode packet count: %ld"
+ "Q24@0:8Q16"
+ "Q48@0:8r*16Q24Q32Q40"
+ "TB,GisAsynchronous,SsetAsynchronous:"
+ "TB,GisFinished,SsetFinished:"
+ "TB,N,V_isResponseReceivedEventSent"
+ "TQ,N,V_readyFilterSet"
+ "Td,V_offlineOperationTimeout"
+ "Td,V_operationTimeout"
+ "Translation operation scheduled as concurrent: %p"
+ "Translation operation scheduled as serial: %p"
+ "VS4CC"
+ "^{OpaqueAudioConverter=}96@0:8{AudioStreamBasicDescription=dIIIIIIII}16{AudioStreamBasicDescription=dIIIIIIII}56"
+ "_LTAudioDecoder"
+ "_LTDContinuationOperation"
+ "_LTDTranslationOperationScheduler"
+ "_audioDecoderFrom:to:"
+ "_availableAssetsWithCompletion:"
+ "_converter"
+ "_createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:"
+ "_decoder"
+ "_forceOneTimeCatalogRefresh"
+ "_fromASBD"
+ "_installedAssetsWithCompletion:"
+ "_isAsynchronous"
+ "_isFinished"
+ "_isObsoleteCatalogType:"
+ "_isResponseReceivedEventSent"
+ "_languageAssetFilterDescription:"
+ "_languageAssetFilterFromOptions:"
+ "_offlineEngineQueue"
+ "_offlineOperationTimeout"
+ "_onlineEngineQueue"
+ "_operationTimeout"
+ "_readyFilterSet"
+ "_selectedAssetsWithCompletion:"
+ "_serviceProviderForAssetType:"
+ "_test_resetForceOneTimeCatalogRefresh"
+ "_toASBD"
+ "_translationEngineScheduler"
+ "addExecutionBlock:"
+ "addOperation:"
+ "assetProviderFixture"
+ "beginChunkDecoderForStreamDescription:"
+ "characterIsMember:"
+ "com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech"
+ "continuationOperationWithBlock:"
+ "decimalDigitCharacterSet"
+ "decodeChunk:outError:"
+ "decodeChunks:from:to:outError:"
+ "decoder gave us %d bytes bytes but we really only expected %d"
+ "didChangeValueForKey:"
+ "endChunkDecoding"
+ "extraBytesFromUTF8ToUTF16With:totalLength:begin:end:"
+ "getBytes:range:"
+ "initWithContinuationBlock:"
+ "initWithLength:"
+ "initWithQueue:"
+ "isAsynchronous"
+ "isReadyForFilter:"
+ "isResponseReceivedEventSent"
+ "lengthOfBytesUsingEncoding:"
+ "lt_filterUsingBlock:"
+ "markReadyForFilter:"
+ "offlineOperationTimeout"
+ "operationTimeout"
+ "readyFilterSet"
+ "sampleIndex"
+ "scheduleOperation:route:"
+ "scheduleOperationWithRoute:block:"
+ "setAssetProviderFixture:"
+ "setAsynchronous:"
+ "setFinished:"
+ "setIsResponseReceivedEventSent:"
+ "setOfflineOperationTimeout:"
+ "setOperationTimeout:"
+ "setQualityOfService:"
+ "setReadyFilterSet:"
+ "setStartTime:"
+ "setTextRange:"
+ "setUnderlyingQueue:"
+ "silencePosteriorGeneratorProcessorIsFinished:"
+ "startTime"
+ "textRange"
+ "ttsAudioStarted:duration:"
+ "utf16TimingInfoWithUTF8Range:withText:"
+ "v16@?0@?<v@?>8"
+ "v24@0:8@\"EARCaesuraSilencePosteriorGenerator\"16"
+ "v24@?0@\"_LTAudioData\"8d16"
+ "v32@0:8@\"NSArray\"16d24"
+ "v32@?0@\"FTWordTimingInfo\"8Q16^B24"
+ "vs_stringFrom4CC:"
+ "willChangeValueForKey:"
+ "wordTimingInfoFromArray:text:"
+ "wordTimingWithTextRangeInfoFrom:wordTimingInfo:"
- "\t"
- "\r\x13"
- "@\"FTMtService\""
- "@16@?0@\"FTWordTimingInfo\"8"
- "Catalog refresh is not required"
- "Data length: %lu"
- "Enqueued audio buffer at sample title: %.2f, size: %zu"
- "Language asset service received state request"
- "Language asset service state block error %@"
- "Language asset service state failed %@"
- "Language asset service state of available assets failed %@"
- "Language asset service state of installed assets failed %@"
- "Language asset service state of selected assets failed %@"
- "No configAsset in catalog, nothing to download!"
- "TB,V_isHot"
- "_hardReset"
- "_isHot"
- "_sendQueue"
- "_service"
- "_translateParagraph:index:context:completion:"
- "assetForIdentifier:createIfNotFound:"
- "assetsWithCompletion:"
- "availableAssetsWithCompletion:"
- "filterAssets:options:"
- "initWithLocale:"
- "isHot"
- "selectedAssetsWithCompletion:"
- "serviceProvider"
- "serviceProviderForAsset:"
- "serviceProviderForAssetIdentifier:"
- "serviceProviderForAssetType:"
- "setIsHot:"
- "setServiceProvider:"
- "ttsProgressed:"
- "v24@0:8@\"_LTWordTimingInfo\"16"
- "wordTimingInfoFromArray:"

```
