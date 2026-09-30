## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-355.2.0.0.0
-  __TEXT.__text: 0x19480c
+355.4.0.0.0
+  __TEXT.__text: 0x196578
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x19c30
-  __TEXT.__const: 0x450
-  __TEXT.__gcc_except_tab: 0x1b370
-  __TEXT.__cstring: 0x5c47
-  __TEXT.__oslogstring: 0xc399
+  __TEXT.__objc_methlist: 0x19db8
+  __TEXT.__const: 0x4b0
+  __TEXT.__gcc_except_tab: 0x1b3f0
+  __TEXT.__cstring: 0x5dc0
+  __TEXT.__oslogstring: 0xc562
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf4b8
-  __TEXT.__objc_classname: 0x4748
-  __TEXT.__objc_methname: 0x1b2a0
-  __TEXT.__objc_methtype: 0xdfac
-  __TEXT.__objc_stubs: 0x12aa0
+  __TEXT.__unwind_info: 0xf530
+  __TEXT.__objc_classname: 0x477b
+  __TEXT.__objc_methname: 0x1b70d
+  __TEXT.__objc_methtype: 0xdfe8
+  __TEXT.__objc_stubs: 0x12d60
   __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0x3ff8
-  __DATA_CONST.__objc_classlist: 0x1198
+  __DATA_CONST.__const: 0x4018
+  __DATA_CONST.__objc_classlist: 0x11a8
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67e8
-  __DATA_CONST.__objc_superrefs: 0x1108
-  __DATA_CONST.__objc_arraydata: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x68c0
+  __DATA_CONST.__objc_superrefs: 0x1118
+  __DATA_CONST.__objc_arraydata: 0x3f0
   __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x77e0
-  __AUTH_CONST.__objc_const: 0x2c470
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0x7a20
+  __AUTH_CONST.__objc_const: 0x2c788
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH.__objc_data: 0xa398
-  __DATA.__objc_ivar: 0x117c
+  __AUTH.__objc_data: 0xa438
+  __DATA.__objc_ivar: 0x11a4
   __DATA.__data: 0xa68
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x158
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 390CBC89-DEC7-3F96-8766-9EFAD42A4BD0
-  Functions: 9976
-  Symbols:   33873
-  CStrings:  9103
+  UUID: 997B65AE-965E-387F-9A4C-2FCCDCF7CE87
+  Functions: 10035
+  Symbols:   34057
+  CStrings:  9202
 
Symbols:
+ +[_LTDAssetAnalytics shared]
+ +[_LTDLanguageAssetService _installedLocales]
+ +[_LTDUAFAssetService _deferredTimerQueue]
+ +[_LTDUAFAssetService _deferredTimerQueue].cold.1
+ -[_LTDAssetAnalytics .cxx_destruct]
+ -[_LTDAssetAnalytics _init]
+ -[_LTDAssetAnalytics analyticsDataForLocaleIdentifier:completionTime:connectionType:downloadOutcome:downloadTriggerSource:hasClientReportedError:]
+ -[_LTDAssetAnalytics createEventWithNSLocale:connectionType:downloadTriggerSource:]
+ -[_LTDAssetAnalytics createEventWithNSLocale:connectionType:downloadTriggerSource:].cold.1
+ -[_LTDAssetAnalytics getEventWithNSLocale:]
+ -[_LTDAssetAnalytics getEventWithNSLocale:].cold.1
+ -[_LTDAssetAnalytics markEventsAsRetriedForLocales:]
+ -[_LTDAssetAnalytics sendEventToAnalytics:]
+ -[_LTDAssetAnalytics sendEventToAnalytics:].cold.1
+ -[_LTDAssetAnalytics sendEventsToAnalytics:]
+ -[_LTDAssetDownloadAnalyticsEvent .cxx_destruct]
+ -[_LTDAssetDownloadAnalyticsEvent _timeoutEvent]
+ -[_LTDAssetDownloadAnalyticsEvent completionTime]
+ -[_LTDAssetDownloadAnalyticsEvent connectionType]
+ -[_LTDAssetDownloadAnalyticsEvent didRetry]
+ -[_LTDAssetDownloadAnalyticsEvent downloadOutcome]
+ -[_LTDAssetDownloadAnalyticsEvent downloadTriggerSource]
+ -[_LTDAssetDownloadAnalyticsEvent hasClientReportedError]
+ -[_LTDAssetDownloadAnalyticsEvent initWithNSLocale:connectionType:downloadTriggerSource:]
+ -[_LTDAssetDownloadAnalyticsEvent localeIdentifier]
+ -[_LTDAssetDownloadAnalyticsEvent setCompletionTime:]
+ -[_LTDAssetDownloadAnalyticsEvent setConnectionType:]
+ -[_LTDAssetDownloadAnalyticsEvent setDidRetry:]
+ -[_LTDAssetDownloadAnalyticsEvent setDownloadOutcome:]
+ -[_LTDAssetDownloadAnalyticsEvent setDownloadTriggerSource:]
+ -[_LTDAssetDownloadAnalyticsEvent setHasClientReportedError:]
+ -[_LTDAssetDownloadAnalyticsEvent startTimer]
+ -[_LTDAssetDownloadAnalyticsEvent stopTimerWithOutcome:hasClientReportedError:localeIdentifier:]
+ -[_LTOfflineAssetManager updateAssetSymLinksForLocalePairs:]
+ -[_LTOfflineAssetManager updateAssetSymLinksForLocalePairs:].cold.1
+ -[_LTOfflineTranslationEngine _loadTranslatorForTask:].cold.2
+ -[_LTSpeechTranslationAssetInfo assetManager]
+ _OBJC_CLASS_$__LTDAssetAnalytics
+ _OBJC_CLASS_$__LTDAssetDownloadAnalyticsEvent
+ _OBJC_IVAR_$__LTDAssetAnalytics._localeAnalyticsMap
+ _OBJC_IVAR_$__LTDAssetAnalytics._lock
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._completionTime
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._connectionType
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._didRetry
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._downloadOutcome
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._downloadTriggerSource
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._hasClientReportedError
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._localeIdentifier
+ _OBJC_IVAR_$__LTDAssetDownloadAnalyticsEvent._startTime
+ _OBJC_METACLASS_$__LTDAssetAnalytics
+ _OBJC_METACLASS_$__LTDAssetDownloadAnalyticsEvent
+ __LTDAssetAnalyticStringForDownloadOutcome
+ __LTDAssetAnalyticStringForDownloadOutcome.cold.1
+ __LTDAssetAnalyticStringForDownloadOutcome.downloadOutcomeStringMap
+ __LTDAssetAnalyticStringForDownloadOutcome.onceToken
+ __LTDAssetAnalyticsLocaleFromLocaleIdentifier
+ __LTDAssetAnalyticsLocaleFromLocaleIdentifier.cold.1
+ __LTDAssetAnalyticsLocaleFromLocaleIdentifier.localeIdentifierMap
+ __LTDAssetAnalyticsLocaleFromLocaleIdentifier.onceToken
+ __LTOSLogAnalytics
+ __LTOSLogAnalytics.cold.1
+ __LTOSLogAnalytics.log
+ __LTOSLogAnalytics.onceToken
+ __LTTaskHintToLTDAssetAnalyticsDownloadTriggerSource
+ __OBJC_$_CLASS_METHODS__LTDAssetAnalytics
+ __OBJC_$_CLASS_PROP_LIST__LTDAssetAnalytics
+ __OBJC_$_INSTANCE_METHODS__LTDAssetAnalytics
+ __OBJC_$_INSTANCE_METHODS__LTDAssetDownloadAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES__LTDAssetAnalytics
+ __OBJC_$_INSTANCE_VARIABLES__LTDAssetDownloadAnalyticsEvent
+ __OBJC_$_PROP_LIST__LTDAssetDownloadAnalyticsEvent
+ __OBJC_$_PROP_LIST__LTSpeechTranslationAssetInfo
+ __OBJC_CLASS_RO_$__LTDAssetAnalytics
+ __OBJC_CLASS_RO_$__LTDAssetDownloadAnalyticsEvent
+ __OBJC_METACLASS_RO_$__LTDAssetAnalytics
+ __OBJC_METACLASS_RO_$__LTDAssetDownloadAnalyticsEvent
+ ___109-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:]_block_invoke.33
+ ___28+[_LTDAssetAnalytics shared]_block_invoke
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.361
+ ___42+[_LTDUAFAssetService _deferredTimerQueue]_block_invoke
+ ___43-[_LTDAssetAnalytics getEventWithNSLocale:]_block_invoke
+ ___43-[_LTDAssetAnalytics sendEventToAnalytics:]_block_invoke
+ ___43-[_LTDAssetAnalytics sendEventToAnalytics:]_block_invoke.15
+ ___45+[_LTDLanguageAssetService _installedLocales]_block_invoke
+ ___45-[_LTDAssetDownloadAnalyticsEvent startTimer]_block_invoke
+ ___52-[_LTDAssetAnalytics markEventsAsRetriedForLocales:]_block_invoke
+ ___52-[_LTDAssetAnalytics markEventsAsRetriedForLocales:]_block_invoke.6
+ ___52-[_LTDAssetAnalytics markEventsAsRetriedForLocales:]_block_invoke.cold.1
+ ___53+[_LTDLanguageAssetService addLanguages:useCellular:]_block_invoke
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.53
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.54
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.55
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.56
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.44
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.44.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.44.cold.2
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.41
+ ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.41.cold.1
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.34
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.37
+ ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.67
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.38
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.38.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.400
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.400.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.401
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.100
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.100.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.100.cold.2
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.117
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.97
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.118
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.96
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.64
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.64.cold.1
+ ___83-[_LTDAssetAnalytics createEventWithNSLocale:connectionType:downloadTriggerSource:]_block_invoke
+ ___83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.55
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.75
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.75.cold.1
+ ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.60
+ ____LTDAssetAnalyticStringForDownloadOutcome_block_invoke
+ ____LTDAssetAnalyticsLocaleFromLocaleIdentifier_block_invoke
+ ____LTOSLogAnalytics_block_invoke
+ ___block_descriptor_32_e31_16?0"_LTLanguageAssetModel"8l
+ ___block_descriptor_64_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_literal_global.127
+ ___block_literal_global.337
+ ___block_literal_global.364
+ ___block_literal_global.375
+ ___block_literal_global.43
+ ___block_literal_global.48
+ ___block_literal_global.52
+ ___block_literal_global.69
+ ___block_literal_global.75
+ ___block_literal_global.76
+ __deferredTimerQueue._queue
+ __deferredTimerQueue.onceToken
+ _objc_msgSend$_deferredTimerQueue
+ _objc_msgSend$_init
+ _objc_msgSend$_timeoutEvent
+ _objc_msgSend$analyticsDataForLocaleIdentifier:completionTime:connectionType:downloadOutcome:downloadTriggerSource:hasClientReportedError:
+ _objc_msgSend$assetManager
+ _objc_msgSend$completionTime
+ _objc_msgSend$connectionType
+ _objc_msgSend$createEventWithNSLocale:connectionType:downloadTriggerSource:
+ _objc_msgSend$didRetry
+ _objc_msgSend$downloadOutcome
+ _objc_msgSend$downloadTriggerSource
+ _objc_msgSend$getEventWithNSLocale:
+ _objc_msgSend$hasClientReportedError
+ _objc_msgSend$initWithNSLocale:connectionType:downloadTriggerSource:
+ _objc_msgSend$markEventsAsRetriedForLocales:
+ _objc_msgSend$sendEventToAnalytics:
+ _objc_msgSend$setDidRetry:
+ _objc_msgSend$setDownloadOutcome:
+ _objc_msgSend$setHasClientReportedError:
+ _objc_msgSend$startTimer
+ _objc_msgSend$stopTimerWithOutcome:hasClientReportedError:localeIdentifier:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$updateAssetSymLinksForLocalePairs:
+ _shared.sharedInstance
- -[_LTOfflineAssetManager updateSpeechTranslationAssetSymLinks:]
- -[_LTOfflineAssetManager updateSpeechTranslationAssetSymLinks:].cold.1
- ___109-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:]_block_invoke.32
- ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.358
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.49
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.50
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.51
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.52
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.43.cold.2
- ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.40
- ___61+[_LTDLanguageAssetService syncInstalledLocalesOnAssetUpdate]_block_invoke.40.cold.1
- ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.33
- ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke.36
- ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.66
- ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.37
- ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.37.cold.1
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.397
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.397.cold.1
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.398
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.115
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.91
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.96
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.98
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99.cold.2
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.117
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.95
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.63
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.63.cold.1
- ___83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.54
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.74
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.74.cold.1
- ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.58
- ___block_descriptor_56_e8_32bs40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_literal_global.346
- ___block_literal_global.35
- ___block_literal_global.361
- ___block_literal_global.369
- ___block_literal_global.44
- ___block_literal_global.65
- ___block_literal_global.68
- ___block_literal_global.71
- _objc_msgSend$updateSpeechTranslationAssetSymLinks:
CStrings:
+ " : "
+ "%{public}@"
+ "@16@?0@\"_LTLanguageAssetModel\"8"
+ "@40@0:8@16Q24Q32"
+ "@60@0:8@16d24Q32Q40Q48B56"
+ "Analytics"
+ "Asset analytic event aborted due to unexpected nil-locale"
+ "Asset analytic event create has unexpected nil-locale"
+ "Asset analytic event fetch has unexpected nil-locale"
+ "Asset analytic retry event [%{public}@]"
+ "Asset analytic retry mark skip due unexpected nil-locale"
+ "Asset download error"
+ "AssetDownloadMetrics"
+ "Attempting to heal symlinks for locale pair %{public}@"
+ "Download complete for language %@, completion time: %.3f"
+ "Downloaded with no retries"
+ "Downloaded with retries"
+ "Event timeout"
+ "Started download timer for language %@"
+ "Status Mismatch"
+ "T@\"NSString\",R,C,N,V_localeIdentifier"
+ "T@\"_LTDAssetAnalytics\",R,N"
+ "T@\"_LTOfflineAssetManager\",R,N,V_assetManager"
+ "TB,N,V_didRetry"
+ "TB,N,V_hasClientReportedError"
+ "TQ,N,V_connectionType"
+ "TQ,N,V_downloadOutcome"
+ "TQ,N,V_downloadTriggerSource"
+ "Td,N,V_completionTime"
+ "Timeout occurred for language %@"
+ "Translation daemon shutdown"
+ "User cancelled"
+ "_LTDAssetAnalytics"
+ "_LTDAssetDownloadAnalyticsEvent"
+ "_completionTime"
+ "_connectionType"
+ "_deferredTimerQueue"
+ "_didRetry"
+ "_downloadOutcome"
+ "_downloadTriggerSource"
+ "_hasClientReportedError"
+ "_init"
+ "_installedLocales"
+ "_localeAnalyticsMap"
+ "_localeIdentifier"
+ "_timeoutEvent"
+ "analyticsDataForLocaleIdentifier:completionTime:connectionType:downloadOutcome:downloadTriggerSource:hasClientReportedError:"
+ "ar_AE"
+ "assetLocale"
+ "assetManager"
+ "com.apple.translationd.deferredTimerQueue"
+ "completionTime"
+ "connectionType"
+ "createEventWithNSLocale:connectionType:downloadTriggerSource:"
+ "didRetry"
+ "downloadOutcome"
+ "downloadTriggerSource"
+ "getEventWithNSLocale:"
+ "hasClientReportedError"
+ "initWithNSLocale:connectionType:downloadTriggerSource:"
+ "markEventsAsRetriedForLocales:"
+ "ru_RU"
+ "sendEventToAnalytics:"
+ "sendEventsToAnalytics:"
+ "setCompletionTime:"
+ "setConnectionType:"
+ "setDidRetry:"
+ "setDownloadOutcome:"
+ "setDownloadTriggerSource:"
+ "setHasClientReportedError:"
+ "startTimer"
+ "stopTimerWithOutcome:hasClientReportedError:localeIdentifier:"
+ "th_TH"
+ "timeIntervalSinceReferenceDate"
+ "updateAssetSymLinksForLocalePairs:"
+ "v36@0:8Q16B24@28"
- "updateSpeechTranslationAssetSymLinks:"

```
