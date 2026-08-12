## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x1a6db0
-  __TEXT.__objc_methlist: 0x1a2d8
-  __TEXT.__const: 0xa9a
-  __TEXT.__gcc_except_tab: 0x1b3d4
-  __TEXT.__cstring: 0x627b
-  __TEXT.__oslogstring: 0xd5e0
+388.0.0.0.0
+  __TEXT.__text: 0x1a9d1c
+  __TEXT.__objc_methlist: 0x1a390
+  __TEXT.__const: 0xaa0
+  __TEXT.__gcc_except_tab: 0x1b41c
+  __TEXT.__cstring: 0x639b
+  __TEXT.__oslogstring: 0xd880
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x342
+  __TEXT.__swift5_typeref: 0x34f
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__constg_swiftt: 0x154
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf9a8
+  __TEXT.__unwind_info: 0xfa40
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4420
+  __DATA_CONST.__const: 0x4510
   __DATA_CONST.__objc_classlist: 0x11d8
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b30
+  __DATA_CONST.__objc_selrefs: 0x6ba0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1120
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0xeb8
-  __AUTH_CONST.__const: 0x10a8
-  __AUTH_CONST.__cfstring: 0x7b20
-  __AUTH_CONST.__objc_const: 0x2d088
+  __DATA_CONST.__got: 0xef8
+  __AUTH_CONST.__const: 0x10c8
+  __AUTH_CONST.__cfstring: 0x7da0
+  __AUTH_CONST.__objc_const: 0x2d118
   __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__auth_got: 0xd00
   __AUTH.__objc_data: 0xa1c0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x11cc
-  __DATA.__data: 0xcb8
-  __DATA.__bss: 0x7a0
+  __DATA.__objc_ivar: 0x11e0
+  __DATA.__data: 0xd00
+  __DATA.__bss: 0x7d0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__data: 0x278
-  __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__data: 0x268
+  __DATA_DIRTY.__bss: 0x370
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10395
-  Symbols:   21207
-  CStrings:  2227
+  Functions: 10429
+  Symbols:   21259
+  CStrings:  2262
 
Symbols:
+ +[MTSchemaMTAppInvocationMetadata(LTTranslationAdditions) lt_initWithTranslateAppContext:resolvedLocalePair:]
+ +[_LTDLanguageAssetService _currentSyncSignatureFromAssets:]
+ +[_LTDUAFAssetService _catalogLookupThrottleEnabled]
+ +[_LTDUAFAssetService _startCatalogChangeObservationIfNeeded]
+ +[_LTDUAFAssetService _updateCatalogCooldownWithSubscribedCount:resolvedCount:catalog:]
+ +[_LTTranslationResult(Daemon) passthroughResultWithString:sanitizedString:locale:engineInfo:]
+ +[_LTTranslationResult(Daemon) resultWithLocale:translations:engineInfo:]
+ -[_LTActivityLogger _sendCommonEventForTask:appIdentifier:contentType:]
+ -[_LTActivityLogger beginCommonEventSession:appIdentifier:]
+ -[_LTActivityLogger beginCommonEventSession:appIdentifier:contentType:]
+ -[_LTActivityLogger endCommonEventSession]
+ -[_LTActivityLogger registerActivity:appIdentifier:]
+ -[_LTActivityLogger registerActivity:appIdentifier:contentType:]
+ -[_LTClientConnection _applyConnectionTrustToContext:]
+ -[_LTTranslationServer _registerTextActivityForContext:]
+ -[_LTTranslationServer _scheduleMessagingSessionReset]
+ -[_LTTranslationServer endCommonEventSession]
+ -[_LTTranslationServer registerActivity:appIdentifier:]
+ -[_LTTranslationServer registerActivity:appIdentifier:contentType:]
+ _LTDResolvedConferencingLocale
+ _LTDResolvedConferencingLocalePairWithSupportedLocales
+ _OBJC_IVAR_$__LTActivityLogger._activeCommonEventSessionHint
+ _OBJC_IVAR_$__LTActivityLogger._commonEventSessionLock
+ _OBJC_IVAR_$__LTClientConnection._canOverrideClientPID
+ _OBJC_IVAR_$__LTClientConnection._speechTaskHint
+ _OBJC_IVAR_$__LTTranslationServer._messagingSessionResetTimer
+ __LTPreferencesThrottleCatalogLookups
+ ___31+[_LTDUAFAssetService _catalog]_block_invoke
+ ___42-[_LTActivityLogger endCommonEventSession]_block_invoke
+ ___54-[_LTTranslationServer _scheduleMessagingSessionReset]_block_invoke
+ ___61+[_LTDUAFAssetService _startCatalogChangeObservationIfNeeded]_block_invoke
+ ___61+[_LTDUAFAssetService _startCatalogChangeObservationIfNeeded]_block_invoke_2
+ ___64-[_LTActivityLogger registerActivity:appIdentifier:contentType:]_block_invoke
+ ___71-[_LTActivityLogger beginCommonEventSession:appIdentifier:contentType:]_block_invoke
+ ___87+[_LTDUAFAssetService _updateCatalogCooldownWithSubscribedCount:resolvedCount:catalog:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32s_e5_B8?0ls32l8
+ ___block_descriptor_49_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __cachedCatalog
+ __catalogCooldownInterval
+ __catalogLookupSuppressed
+ __lastSyncedLocaleSignature
+ __localesWithVoice
+ __localesWithVoiceLock
+ __startCatalogChangeObservationIfNeeded.onceToken
+ _objc_msgSend$_applyConnectionTrustToContext:
+ _objc_msgSend$_catalogLookupThrottleEnabled
+ _objc_msgSend$_currentSyncSignatureFromAssets:
+ _objc_msgSend$_registerChangeHandler:
+ _objc_msgSend$_registerTextActivityForContext:
+ _objc_msgSend$_scheduleMessagingSessionReset
+ _objc_msgSend$_sendCommonEventForTask:appIdentifier:contentType:
+ _objc_msgSend$_startCatalogChangeObservationIfNeeded
+ _objc_msgSend$_updateCatalogCooldownWithSubscribedCount:resolvedCount:catalog:
+ _objc_msgSend$beginCommonEventSession:appIdentifier:
+ _objc_msgSend$beginCommonEventSession:appIdentifier:contentType:
+ _objc_msgSend$clearCachedValuesForStatusChangeLocked
+ _objc_msgSend$endCommonEventSession
+ _objc_msgSend$engineInfo
+ _objc_msgSend$initWithTranslation:alignments:engineInfo:
+ _objc_msgSend$lt_initWithTranslateAppContext:resolvedLocalePair:
+ _objc_msgSend$originatingProcessIdentifier
+ _objc_msgSend$passthroughResultWithString:sanitizedString:locale:engineInfo:
+ _objc_msgSend$registerActivity:appIdentifier:
+ _objc_msgSend$registerActivity:appIdentifier:contentType:
+ _objc_msgSend$resultWithLocale:translations:engineInfo:
+ _objc_msgSend$setEngineInfo:
+ _os_unfair_lock_assert_owner
+ _swift_allocError
+ _symbolic _____Sg 20TranslationInference0A9ModelInfoV
+ _symbolic _____Sg 20TranslationInference0A9ModelInfoV0C4TypeO
+ _symbolic _____Sg_ABt 20TranslationInference0A9ModelInfoV0C4TypeO
+ _symbolic _____y_____G s11_SetStorageC 10Foundation6LocaleV
- +[MTSchemaMTAppInvocationMetadata(LTTranslationAdditions) lt_initWithTranslateAppContext:]
- +[_LTDTTSAssetService _allTTSAssets]
- +[_LTTranslationResult(Daemon) passthroughResultWithString:sanitizedString:locale:]
- +[_LTTranslationResult(Daemon) resultWithLocale:translations:]
- -[_LTActivityLogger registerActivity:]
- -[_LTTranslationServer registerActivity:]
- __CLASS_METHODS__LTAIAdapterImplementation
- __IVARS__LTModelModalities
- ___36+[_LTDTTSAssetService _allTTSAssets]_block_invoke
- ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke_2
- ___block_descriptor_40_e28_"NSString"16?0"NSString"8l
- ___swift_destroy_boxed_opaque_existential_1
- __cachedTTSAssets
- _objc_msgSend$availableIdentifiers
- _objc_msgSend$initWithTranslation:alignments:
- _objc_msgSend$listAssetsOfTypes:matching:
- _objc_msgSend$lt_initWithTranslateAppContext:
- _objc_msgSend$passthroughResultWithString:sanitizedString:locale:
- _objc_msgSend$registerActivity:
- _objc_msgSend$resultWithLocale:translations:
- _swift_retain
- _symbolic _____ySSG s23_ContiguousArrayStorageC
- _symbolic _____y__________G 12ModelCatalog0B5AssetV AA016TranslateFMAssetC8MetadataV AA0deC8ContentsV
CStrings:
+ "2"
+ "Asset set changed but catalog still unresolved; keeping catalog lookup cooldown"
+ "B8@?0"
+ "Catalog cooldown check: subscribed=%lu resolved=%lu -> %{public}s"
+ "Connection can-override-client-pid: %{BOOL}i"
+ "Etiquette URL available for locale %{public}s"
+ "Failed to get etiquette URL: phrasebook asset unavailable"
+ "Healthy catalog rebuild resolved assets; clearing catalog lookup cooldown"
+ "Messages"
+ "Overriding client PID %d with originating PID %d"
+ "PT"
+ "PhoneCall"
+ "Skipping UAF catalog rebuild during lookup cooldown, returning cached catalog"
+ "Sync install no-op: signature unchanged"
+ "System"
+ "ThrottleCatalogLookups"
+ "UAF Asset in the _catalog (lookup throttle %{public}s)"
+ "UAF catalog lookup cooldown elapsed"
+ "UAF catalog resolved no assets while subscribed; suppressing lookups for %.0fs"
+ "UAF catalog resolved, cleared catalog lookup cooldown"
+ "action"
+ "automatic"
+ "button"
+ "clear"
+ "com.apple.translation.can-override-client-pid"
+ "disabled"
+ "enabled"
+ "identifierForDownloads"
+ "initiated_by"
+ "input_mode"
+ "intelligence.CommonEvent"
+ "is_saved_content"
+ "origin_surface"
+ "request_made"
+ "result_surface"
+ "source_app"
+ "sub_feature"
+ "suppress"
+ "|"
- "@\"NSString\"16@?0@\"NSString\"8"
- "Failed to get etiquette URL from phrasebook asset: %@"
- "UAF Asset in the _catalog"
- "a"
```
