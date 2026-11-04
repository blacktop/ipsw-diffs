## safetyalertsd

> `/usr/libexec/safetyalertsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-70.0.21.0.0
-  __TEXT.__text: 0xfd898
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_stubs: 0x3780
+70.0.27.0.0
+  __TEXT.__text: 0x10f630
+  __TEXT.__auth_stubs: 0x1200
+  __TEXT.__objc_stubs: 0x3a80
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__const: 0x9870
-  __TEXT.__cstring: 0x7a74
-  __TEXT.__gcc_except_tab: 0xf034
-  __TEXT.__oslogstring: 0x439b2
-  __TEXT.__objc_methname: 0x3e67
+  __TEXT.__const: 0xa340
+  __TEXT.__cstring: 0x8225
+  __TEXT.__gcc_except_tab: 0x10694
+  __TEXT.__oslogstring: 0x47722
+  __TEXT.__objc_methname: 0x40b8
   __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methtype: 0x1cdf
+  __TEXT.__objc_methtype: 0x1cd4
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4a88
-  __DATA_CONST.__const: 0x8988
-  __DATA_CONST.__cfstring: 0x7300
+  __TEXT.__unwind_info: 0x5008
+  __DATA_CONST.__const: 0x9130
+  __DATA_CONST.__cfstring: 0x75a0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x870
-  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__auth_got: 0x910
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x1248
-  __DATA.__objc_selrefs: 0x1268
+  __DATA.__objc_selrefs: 0x1328
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x448

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3611
-  Symbols:   470
-  CStrings:  5119
+  Functions: 3814
+  Symbols:   514
+  CStrings:  5363
 
Symbols:
+ _CFEqual
+ _CFErrorGetCode
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$__LTLanguageStatus
+ _OBJC_CLASS_$__LTLanguageStatusConfiguration
+ _OBJC_CLASS_$__LTTextTranslationRequest
+ _OBJC_CLASS_$__LTTranslator
+ _SecAccessControlCreateWithFlags
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecKeyCopyExternalRepresentation
+ _SecKeyCopyPublicKey
+ _SecKeyCreateDecryptedData
+ _SecKeyCreateEncryptedData
+ _SecKeyCreateRandomKey
+ _SecKeyIsAlgorithmSupported
+ __DefaultRuneLocale
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__119__shared_weak_count4lockEv
+ ___maskrune
+ _fdopen
+ _kSAOtherAlertsDescriptionNoRelay
+ _kSecAttrAccessControl
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrAccessibleAlwaysThisDeviceOnly
+ _kSecAttrApplicationTag
+ _kSecAttrIsPermanent
+ _kSecAttrKeyClassPrivate
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecAttrTokenID
+ _kSecAttrTokenIDSecureEnclave
+ _kSecClass
+ _kSecClassKey
+ _kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA256AESGCM
+ _kSecPrivateKeyAttrs
+ _kSecReturnRef
+ _kSecValueRef
+ _open_dprotected_np
+ _unlink
CStrings:
+ "\n\n- "
+ "\n- "
+ "%@\n\n%@"
+ "%@\n\n%@\n%@"
+ "(null)"
+ ".enc"
+ ".sa"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SafetyAlerts/Sources/Daemon/core/geoAlertCache/SAGeoAlertCacheManager.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SafetyAlerts/Sources/Daemon/core/preUnlockVault/SAPreUnlockGeoAlertVault.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SafetyAlerts/Sources/Daemon/framework/security/asymmetricKeyStore/SAAsymmetricKeyStore.mm"
+ "DeviceSupportsGenerativeModelSystems"
+ "Displayed"
+ "MACHINE_TRANSLATION"
+ "MACHINE_TRANSLATION_DESCRIPTION"
+ "MACHINE_TRANSLATION_SWITCH_STATE"
+ "MACHINE_TRANSLATION_SWITCH_VISIBLE"
+ "MachineTranslation"
+ "PendingGeoAlerts/"
+ "Received"
+ "SAAsymmetricKeyStore.mm"
+ "SAFETY_ALERTS_TRANSLATED_BY_IPHONE_TITLE"
+ "SAGeoAlertCacheManager.mm"
+ "SAPreUnlockGeoAlertVault.mm"
+ "TRANSLATION_SOURCE_LOCALE_ALLOWLIST"
+ "TRANSLATION_SUPPORTED_LANGUAGES"
+ "TRANSLATOR_TEST"
+ "UserChangedMachineTranslationSwitch"
+ "["
+ "] "
+ "alreadyInDeviceLanguage"
+ "arrayWithCapacity:"
+ "caseInsensitiveCompare:"
+ "com.apple.SafetyAlerts.translationStatus"
+ "com.apple.safetyalertsd.secureAlerts"
+ "contentsOfDirectoryAtPath:error:"
+ "daily"
+ "dataWithContentsOfFile:options:error:"
+ "de-DE"
+ "disabledByUser"
+ "distantPast"
+ "emptyDisplayText"
+ "entries"
+ "errorCode"
+ "es-ES"
+ "failed"
+ "false && \"#geoCache,cacheDir is empty\""
+ "false && \"#keyStore,fullApplicationTag,invalidConfig\""
+ "false && \"#preUnlockVault,keyStoreConfig,invalid\""
+ "false && \"#preUnlockVault,pendingDir is empty\""
+ "fileModificationDate"
+ "fr-FR"
+ "fullApplicationTag"
+ "initWithConfiguration:observations:"
+ "initWithSourceLocale:targetLocale:"
+ "initWithString:"
+ "initWithTaskHint:engineType:useDedicatedMachPort:"
+ "internalError"
+ "invalidLocale"
+ "it-IT"
+ "ja-JP"
+ "keyStoreConfig"
+ "ko-KR"
+ "latencyMs"
+ "locale"
+ "localeIdentifier"
+ "lt_bestMatchForPreferredLocales:fromSupportedLocales:"
+ "lt_localeWithLTIdentifier:"
+ "machineTranslationLearnMoreLink"
+ "machineTranslationSwitchState"
+ "machineTranslationSwitchVisible"
+ "missingLanguageTag"
+ "noInstalledModel"
+ "notAttempted"
+ "notSupportedByAssets"
+ "notificationActions"
+ "originalDisplayText"
+ "pairUnsupported"
+ "partiallyTranslated"
+ "preUnlockGeoAlert"
+ "preferredLocalizationsFromArray:forPreferences:"
+ "preferred_locale"
+ "pt-BR"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "saTranslationTimeout"
+ "safetyAlertTranslation"
+ "sameLanguage"
+ "senderName"
+ "setCacheDir"
+ "setForcedOfflineTranslation:"
+ "setOnDeviceEngineType:"
+ "setTaskHint:"
+ "setText:"
+ "setTextTranslationHandler:"
+ "setup"
+ "sortUsingComparator:"
+ "sourceLocale"
+ "sourceLocaleAllowlist"
+ "sourceNotAllowed"
+ "sourceNotSupported"
+ "string"
+ "supportedLanguages"
+ "switchOn"
+ "switchVisible"
+ "targetLocale"
+ "targetNotSupported"
+ "timedOut"
+ "timeoutSeconds"
+ "translate:useDedicatedTextMachPort:"
+ "translated"
+ "translatedDisplayText"
+ "translatedInstruction"
+ "translation"
+ "translatorError_"
+ "v32@?0@\"NSAttributedString\"8@\"_LTTranslationResult\"16@\"NSError\"24"
+ "zh-CN"
+ "zh-HK"
+ "zh-TW"
+ "zxx"
+ "{\"msg%{public}.0s\":\"#SAAlertDataMerger,mergeGeoAlertData\", \"alertHash\":%{private, location:escape_only}s, \"isSafetyAlertSource\":%{public}hhd, \"hasSAData\":%{public}hhd, \"hasCTData\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAAlertDataMerger,mergeGeoAlertData,noDataFromEitherSource\"}"
+ "{\"msg%{public}.0s\":\"#ch,states\", \"fDidReceivePublicToken\":%{public}hhd, \"fDidReceiveToken\":%{public}hhd, \"publicApnsPushTokenHex\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ch,topicTokens\", \"topic\":%{private, location:escape_only}s, \"topicApnsPushTokenHex\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#channel,received public push token\", \"token\":%{private, location:escape_only}@, \"publicApnsPushTokenHex\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#channel,received push token\", \"token\":%{private, location:escape_only}@, \"topicApnsPushTokenHex\":%{private, location:escape_only}s, \"topic\":%{private, location:escape_only}@, \"identifier\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#chmgr,channelAddOn invalid channel proxy\"}"
+ "{\"msg%{public}.0s\":\"#chsel,Safety Alerts init timedout\", \"timeout\":%{public}d, \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"isPhone\":%{private}d, \"isWatch\":%{private}d, \"forceOrDeferChannelUpdate\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,states\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu, \"country\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chsel,updateChannelListBasedOnType,\", \"type\":%{private}d, \"fCurrentChannels count\":%{private}d, \"fIgneousChannels count\":%{private}d, \"fOtherAlertsDitheredChannels count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,parseLocaleArrayPref,emptyPrefLocales\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,parseLocaleArrayPref,invalidPrefJSON\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,parseLocaleArrayPref,invalidPrefUTF8\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readSourceLocaleAllowlistFromAsset,notArray\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,fromAsset\", \"count\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,fromDefault\", \"count\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,fromPref\", \"count\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,invalidPref,fallingBackToAsset\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,locale\", \"locale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,nilConfig\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,nilDict\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,noSupportedLanguages\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationAsset,noTranslationKey\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationSourceLocaleAllowlist,fromAsset\", \"locales\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationSourceLocaleAllowlist,fromDefault\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationSourceLocaleAllowlist,fromPref\", \"locales\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationSourceLocaleAllowlist,invalidPref,fallingBackToAsset\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationTimeoutSeconds\", \"fromAsset\":%{public}d, \"clamped\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readTranslationTimeoutSeconds,absentOrInvalid,usingDefault\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,setting log\", \"machineTranslationSwitchVisible\":%{private}hhd, \"machineTranslationSwitchState\":%{private}hhd, \"machineTranslationLearnMoreLink\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,onSafetyAlertReceived,noLocation,deferAlert\", \"alert\":%{private, location:escape_only}s, \"isLocationValid\":%{public}hhd, \"remainingInit\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,onSafetyAlertReceived,pendingQueueFull,evictOldest\", \"alert\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,getGeoAlertData\", \"alertIdentifier\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,getGeoAlertData,success\", \"alertHash\":%{private, location:escape_only}s, \"isSafetyAlertSource\":%{public}hhd, \"hadSAData\":%{public}hhd, \"hadCTData\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,forwarding to GeneralSafetyAlertDisplay\", \"isWeaReceived\":%{public}hhd, \"hasLtBody\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,noSelectableInfoEntry\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,noTranslationNeeded\", \"infoEntryIndex\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,usingTopDeviceLocaleOnly\", \"availableLocaleCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onWeaDisplayedNotification,nullMessage,dropping\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onWeaDisplayedNotificationCb,nullMessage,dropping\"}"
+ "{\"msg%{public}.0s\":\"#daemon,refreshWeaReceivedFlag,weaAlreadyDisplayed\", \"matchedText\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,set settingsPreference\", \"isEarthquakeAlertsEnabled\":%{public}d, \"isOtherAlertsEnabled\":%{public}d, \"isAlwaysPlaySoundEnabled\":%{public}d, \"isImprovedAlertDeliveryEnabled\":%{public}d, \"isMachineTranslationEnabled\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#eff,collectEfficacyMetricForAlertType,isWeaReceived\", \"isWeaReceived\":%{private}d, \"hash\":%{private, location:escape_only}s, \"timestampSource\":%{private, location:escape_only}s, \"timestamp\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,alertDataForHash,found\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,alertDataForHash,noAlertsSection\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,alertDataForHash,noCacheFile\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,alertDataForHash,notFound\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,built_entry\", \"hash\":%{private, location:escape_only}s, \"language\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,completed\", \"processedEntries\":%{public}lu, \"builtEntries\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,invalidUTF8Language\", \"language\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,no_hash_computed,skipping\", \"language\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,processing_all_languages\", \"uid\":%{private, location:escape_only}s, \"infoEntriesCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,processing_entry\", \"language\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,using_long_text\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,using_text\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,buildEntries,using_wea_text\", \"hash\":%{private, location:escape_only}s, \"language\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,cacheAlert,cached_entry\", \"hash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,cacheAlert,deferPreUnlockFailed,openInMapsUnavailable\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,cacheAlert,deferredPreUnlock\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,cacheAlert,missingAlertHash,skippingEntry\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,cacheDir is empty\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,insertOrMergeEntry,incomingNotADictionary\", \"hash\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#geoCache,mergePendingAlertsAfterFirstUnlock,cacheDirNotSet,keepVault\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,parsePolygonalGeofencesFromGeometry,addedPolygon\", \"identifier\":%{private, location:escape_only}s, \"vertexCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,parsePolygonalGeofencesFromGeometry,invalidInput\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,parsePolygonalGeofencesFromGeometry,invalidPolygon,skippingEntire\", \"invalidLat\":\"%{private}0.6f\", \"invalidLon\":\"%{private}0.6f\", \"reason\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#geoCache,parsePolygonalGeofencesFromGeometry,noPolygons\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,parsePolygonalGeofencesFromGeometry,success\", \"polygonCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,pruneStaleEntries,completed\", \"removedCount\":%{public}lu, \"remainingCount\":%{public}lu, \"writeSucceeded\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#geoCache,readCacheFile,cacheDirNotSet\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,removeStaleFrom,completed\", \"removedCount\":%{public}lu, \"remainingCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,update,invalidArgs\", \"hasHash\":%{public}hhd, \"hasData\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateBatch,success\", \"batchCount\":%{public}lu, \"totalAlerts\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateBatch,writeFailed\", \"batchCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateSkippingStale\", \"offered\":%{public}lu, \"updated\":%{public}lu, \"expired\":%{public}lu, \"skipped\":%{public}lu, \"writeSucceeded\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateSkippingStale,entryMissingHash,skip\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateSkippingStale,nothingToWrite\", \"offered\":%{public}lu, \"expired\":%{public}lu, \"skipped\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,updateSkippingStale,writeFailed,openInMapsLost\", \"updated\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#geoCache,writeCacheFile,cacheDirNotSet\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,writeCacheFile,emptySerialization\"}"
+ "{\"msg%{public}.0s\":\"#geoCache,writeCacheFile,nilAlerts\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display,selectionOutOfRange\", \"infoEntryIndex\":%{public}d, \"infoEntryCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post\", \"uid\":%{private, location:escape_only}s, \"infoEntryIndex\":%{public}d, \"matchesDeviceLocale\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,firstEntryFallback\", \"infoEntryIndex\":%{public}d, \"infoLocale\":%{private, location:escape_only}s, \"serverPreferredLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,nativeLanguageMatch\", \"infoEntryIndex\":%{public}d, \"infoLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,no valid info entry found\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,noEntryHasDisplayText\", \"infoEntryCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,serverPreferredLocaleMatch\", \"infoEntryIndex\":%{public}d, \"infoLocale\":%{private, location:escape_only}s, \"serverPreferredLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,serverPreferredLocaleMatchesNoEntry\", \"serverPreferredLocale\":%{private, location:escape_only}s, \"infoEntryCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gsadisp,selectInfoEntry,skippingEntryWithNoDisplayText\", \"infoEntryIndex\":%{public}d, \"infoLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#keyStore,accessControlFailed\", \"cfError\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,copyPublicKeyFailed,discardedPrivateKey\", \"discarded\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#keyStore,create,invalidConfig\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,decrypt,noPrivateKey\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,decryptFailed\", \"cfError\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,deletePrivateKeyFailed\", \"status\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,deletePublicKeyFailed\", \"status\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,encrypt,derivePublicKeyFailed\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,encrypt,nilPlaintext\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,encrypt,noPublicKey,cannotDeriveWhileLocked\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,encrypt,repairedPublicKey\", \"repersisted\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#keyStore,encryptAlgoUnsupported\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,encryptFailed\", \"cfError\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,ensureKeyPair,regenerating\", \"couldNotCompareHalves\":%{public}hhd, \"hadPrivateKey\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#keyStore,ensureKeyPair,repairedPublicKey\", \"repaired\":%{public}hhd, \"wasIndeterminate\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#keyStore,fullApplicationTag,invalidConfig\", \"keyName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#keyStore,generateKeyPair,privateDeleteFailed,abort\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,generateKeyPair,publicDeleteFailed,abort\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,keyGenFailed\", \"cfError\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,keyPairState,copyPublicKeyFailed,indeterminate\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,keyPairState,exportFailed,indeterminate\", \"derivedError\":%{public}lld, \"storedError\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,persistPublicKey,nullKey\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,persistPublicKeyFailed\", \"status\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,persistPublicKeyFailed,discardedPrivateKey\", \"discarded\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#keyStore,privateKeyLookupFailed\", \"status\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,privateKeyNotFound\"}"
+ "{\"msg%{public}.0s\":\"#keyStore,publicKeyLookupFailed\", \"status\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#keyStore,publicKeyNotFound\"}"
+ "{\"msg%{public}.0s\":\"#notif,notificationActions\", \"actionCount\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#notif,notificationActions\", \"kMapsBundleIdentifier\":%{public, location:escape_only}s, \"mapsInstalled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#notif,notificationActions\", \"mapsActionTitle\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,added_translatedDisplayText_to_userInfo\"}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,added_translatedInstruction_to_userInfo\"}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,ltAttributionMissing\"}"
+ "{\"msg%{public}.0s\":\"#platformInfo\", \"deviceClass\":%{private, location:escape_only}s, \"iPhone\":%{private}hhd, \"iPod\":%{private}hhd, \"iPad\":%{private}hhd, \"watch\":%{private}hhd, \"appleTV\":%{private}hhd, \"homePod\":%{private}hhd, \"mac\":%{private}hhd, \"cellular\":%{private}hhd, \"dualSim\":%{private}hhd, \"cellularWatch\":%{private}hhd, \"wifiOnlyWatch\":%{private}hhd, \"internal\":%{private}hhd, \"supportedDevice\":%{private}hhd, \"supportedOSType\":%{private}hhd, \"supportedPlatform\":%{private}hhd, \"aop\":%{private}hhd, \"generativeModels\":%{private}hhd, \"tinkerWatch\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,capEvict\", \"fileKey\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,decryptFailed\", \"fileKey\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,deletePendingFileFailed\", \"fileKey\":%{private, location:escape_only}s, \"errno\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,drainComplete\", \"files\":%{public}lu, \"entries\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,emptyPayload,skipStore\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,encryptFailed,noKeyOrCryptoError\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,ensureKey,failed,featureDisabled\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,ensureKey,noKeyStore\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,entriesNotAnArray\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,entryNotADictionary\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,ignoringForeignFile\", \"name\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,invalidUid,skipStore\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,keyStoreConfig,invalid\", \"keyName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,listPendingFailed\", \"dir\":%{private, location:escape_only}s, \"errCode\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,noKeyStore,skipFlush\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,noKeyStore,skipStore\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,payloadNotADictionary\", \"fileKey\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,pendingDir is empty\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,pendingDirCreateFailed\", \"dir\":%{private, location:escape_only}s, \"errno\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,readFailed,drop\", \"fileKey\":%{private, location:escape_only}s, \"errCode\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,serializeFailed\"}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,storePendingAlert\", \"uid\":%{private, location:escape_only}s, \"ok\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#preUnlockVault,uidMismatch,drop\", \"fileKey\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ps,deleteFile,invalidPath\"}"
+ "{\"msg%{public}.0s\":\"#ps,open,invalidProtectionClass\", \"protectionClass\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,bestFitLocaleIndex,emptyRankedResult\"}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,bestFitLocaleIndex,unexpectedResult\", \"bestFitTag\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,filterSupportedLocales,droppedLegacyPair\", \"entry\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,getValidLocaleTags,isControlValue\", \"index\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,getValidLocaleTags,notUTF8\", \"index\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,selectTranslationLocales,entryMissingLanguageTag\"}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,selectTranslationLocales,selected\", \"sourceLocale\":%{private, location:escape_only}s, \"targetLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,selectTranslationLocales,sourceNotAllowed\", \"displayEntryLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,selectTranslationLocales,sourceNotSupported\", \"displayEntryLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saCommonUtils,selectTranslationLocales,targetIsSourceLanguage\", \"displayEntryLocale\":%{private, location:escape_only}s, \"deviceLocale\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getLTSwitchState\", \"fIsMachineTranslationSwitchState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguageLocales\", \"count\":%{public}d, \"locales\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguageLocales,invalidOverrideEntry\", \"value\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguageLocales,noValidOverrideEntries\", \"value\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguageLocales,override\", \"count\":%{public}d, \"locales\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"MachineTranslation\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,hasUserChangedMachineTranslationSwitch\", \"userChanged\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isLTSwitchVisible\", \"machineTranslationSwitchVisible MA\":%{public}hhd, \"deviceCapable\":%{public}hhd, \"machineTranslationSwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onUserSettingsUpdated\", \"fIsMachineTranslationSwitchState\":%{private}d, \"machineTranslationState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,setUserChangedMachineTranslationSwitch\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateESASettings\", \"machineTranslationStateOnDisk\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateUserPref,footerSelection\", \"earthquakeSwitchVisible\":%{public}hhd, \"otherAlertDescription\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\", \"machineTranslationState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saTranslator,create,usingTestTranslator\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,isLanguagePairSupported\", \"source\":%{private, location:escape_only}s, \"target\":%{private, location:escape_only}s, \"sourceMatch\":%{private, location:escape_only}s, \"targetMatch\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,isLanguagePairSupported,entered\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,isLanguagePairSupported,invalidLocale\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,isLanguagePairSupported,sameLanguage\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,translate,done\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,translate,entered\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,translate,error\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,translate,invalidLocale\"}"
+ "{\"msg%{public}.0s\":\"#saTranslatorProd,translate,locales\", \"source\":%{private, location:escape_only}s, \"target\":%{private, location:escape_only}s, \"resolvedSource\":%{private, location:escape_only}s, \"resolvedTarget\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#sa_util,isHashMatch,weaText,matched\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,onSafetyAlertTranslationStatus\", \"payload\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#stateDump,channel\", \"channelId\":%{private, location:escape_only}s, \"topic\":%{private, location:escape_only}s, \"topicApnsPushTokenHex\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#stateDump,channel\", \"publicApnsPushTokenHex\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#stateDump,machineTranslation,userModified\", \"machTranslation\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#stateDump,machineTranslationSwitches\", \"machTranslation\":%{private}hhd, \"machTranslationVis\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported\", \"deviceLocaleCount\":%{public}d, \"supportedLocaleCount\":%{public}d, \"sourceAllowlistCount\":%{public}d, \"displayEntryIndex\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported,badDisplayEntryIndex\", \"uid\":%{private, location:escape_only}s, \"displayEntryIndex\":%{public}d, \"infoEntryCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported,isLanguagePairSupported\", \"supported\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported,matchFound\", \"sourceLanguage\":%{private, location:escape_only}s, \"targetLanguage\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported,noDeviceLocales\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,determineIfTranslationSupported,noSupportedLocaleMatch\", \"deviceLocaleCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,displayAlertOnce,alreadyDisplayed,skipping\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,displayAlertOnce,shuttingDown,skipping\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,initialize\", \"hasTranslator\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,isTranslationAvailable,notEnabledByUser\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,isTranslationAvailable,notSupportedByAssets\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,onTranslationSupportChecked,afterTimeout,ignoring\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,onTranslationSupportChecked,notSupported,displayingNow\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,startTranslationTimeout\", \"uid\":%{private, location:escape_only}s, \"timeoutSeconds\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,startTranslationTimeout,timerCreateFailed,displayingNow\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,translationTimeout,expired,displayingUntranslated\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation\", \"uid\":%{private, location:escape_only}s, \"sourceLanguage\":%{private, location:escape_only}s, \"targetLanguage\":%{private, location:escape_only}s, \"translationCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,displayTextAfterTimeout,ignoring\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,emptyDisplayText,displayingNow\", \"uid\":%{private, location:escape_only}s, \"infoEntryIndex\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,instructionAfterTimeout,ignoring\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,noRecordedPlan\", \"uid\":%{private, location:escape_only}s, \"infoEntryIndex\":%{public}d, \"infoEntryCount\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,onTranslationCompleted,allDone\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,onTranslationCompleted,waiting\", \"translationsRemaining\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,translationError,displayText\", \"errorCode\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,translationError,instructionText\", \"errorCode\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,translationReceived,displayText\"}"
+ "{\"msg%{public}.0s\":\"#translationDisplay,triggerTranslation,translationReceived,instructionText\"}"
+ "{\"msg%{public}.0s\":\"delete file,\", \"file:\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"write invalid args\", \"hasPath\":%{public}hhd, \"hasData\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"write open failed\", \"filePath\":%{private, location:escape_only}s, \"protectionClass\":%{private}d, \"errno\":%{private}d}"
- "@20@0:8B16"
- "ch_config"
- "com.apple.aps.ardea.safetyalert"
- "com.apple.aps.buteo.safetyalert"
- "com.apple.aps.gyps.safetyalert"
- "com.apple.aps.gypstw.safetyalert"
- "com.apple.aps.locationd.safetyalert"
- "com.apple.aps.mantistw.safetyalert"
- "mp_channel"
- "notificationActionsWithAllFeatures:"
- "properties"
- "weaEnrichmentChannel"
- "{\"msg%{public}.0s\":\"#ch,states\", \"fDidReceivePublicToken\":%{public}hhd, \"fDidReceiveToken\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#channel,received public push token\", \"token\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#channel,received push token\", \"token\":%{private, location:escape_only}@, \"topic\":%{private, location:escape_only}@, \"identifier\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel\", \"livabiltyChannel\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#chsel,Safety Alerts init timedout\", \"timeout\":%{public}d, \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#chsel,ch\", \"channelListSize\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#chsel,getChannelFromMap\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#chsel,getChannelFromMap\", \"index\":%{public}d}"
- "{\"msg%{public}.0s\":\"#chsel,loadGeoChannelMaps\", \"geoChannelMapsSize\":%{public}d}"
- "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate, after livability\", \"fCurrentChannels Size\":%{public}ld}"
- "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate,Voters\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"channelMapsSize\":%{private}d, \"isParticipating\":%{public, location:escape_only}s, \"isPhone\":%{private}d, \"isWatch\":%{private}d, \"forceOrDeferChannelUpdate\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,states\", \"countrySupported\":%{public}hhd, \"lsOn\":%{public, location:escape_only}s, \"locAvailable\":%{public, location:escape_only}s, \"fIsAllowedByNetwork\":%{public, location:escape_only}s, \"channelMapAvailable\":%{public, location:escape_only}s, \"isCompanionNearby\":%{public, location:escape_only}s, \"isParticipating\":%{public, location:escape_only}s, \"channelListSize\":%{private}lu, \"country\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#chsel,updateChannelListBasedOnType,\", \"type\":%{private}d, \"fCurrentChannels count\":%{private}d, \"fIgneousChannels count\":%{private}d, \"fOtherAlertsDitheredChannels count\":%{private}d, \"fSAChannels count\":%{private}d, \"fLivabilityChannels count\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chsel,updateLivabilityChannels,precondition failed\"}"
- "{\"msg%{public}.0s\":\"#chsel,updateLivabilityChannels,state\", \"registerLivability\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,SA not supported on watch\"}"
- "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,precondition failed\"}"
- "{\"msg%{public}.0s\":\"#chsel,updateSAChannels,state\", \"isSaRegisterPreCheckPass\":%{public}hhd, \"isInCountry\":%{public}hhd, \"isParticipating\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#countryAssetConfig,getGeoChannelMaps,asset not defined\"}"
- "{\"msg%{public}.0s\":\"#ctsa,not valid wea\"}"
- "{\"msg%{public}.0s\":\"#daemon,#warning,onSafetyAlertReceived,noLocation,deferAlert\", \"alert\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,cached_entry\", \"hash\":%{private, location:escape_only}s, \"language\":%{private}d}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,completed\", \"processedEntries\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,no_hash_computed,skipping\", \"language\":%{private}d}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,processing_all_languages\", \"uid\":%{private, location:escape_only}s, \"infoEntriesCount\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,processing_entry\", \"language\":%{private}d}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,using_long_text\", \"hash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,cacheAlertDataForGeoAPI,using_text\", \"hash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,cleanupGeoAlertCache,completed\", \"removedCount\":%{public}lu, \"remainingCount\":%{public}lu, \"writeSucceeded\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemon,cleanupStaleAlerts,completed\", \"removedCount\":%{public}lu, \"remainingCount\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,getGeoAlertData\", \"alertHash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,getGeoAlertData,success\", \"alertHash\":%{private, location:escape_only}s, \"hadSAData\":%{public}hhd, \"hadCTData\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemon,getSafetyAlertDataFromStorage,failedToReadCache\"}"
- "{\"msg%{public}.0s\":\"#daemon,getSafetyAlertDataFromStorage,found\", \"hash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,getSafetyAlertDataFromStorage,noAlertsSection\"}"
- "{\"msg%{public}.0s\":\"#daemon,getSafetyAlertDataFromStorage,noCacheFile\"}"
- "{\"msg%{public}.0s\":\"#daemon,getSafetyAlertDataFromStorage,notFound\", \"hash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,mergeAlertData\", \"alertHash\":%{private, location:escape_only}s, \"hasSAData\":%{public}hhd, \"hasCTData\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemon,mergeAlertData,noDataFromEitherSource\"}"
- "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,forwarding to GeneralSafetyAlertDisplay\", \"isWeaReceived\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,weaAlreadyDisplayed\", \"matchedCmamLongText\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,parsePolygonalGeofencesFromGeometry,addedPolygon\", \"identifier\":%{private, location:escape_only}s, \"vertexCount\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,parsePolygonalGeofencesFromGeometry,invalidInput\"}"
- "{\"msg%{public}.0s\":\"#daemon,parsePolygonalGeofencesFromGeometry,invalidPolygon,skippingEntire\", \"invalidLat\":\"%{private}0.6f\", \"invalidLon\":\"%{private}0.6f\", \"reason\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,parsePolygonalGeofencesFromGeometry,noPolygons\"}"
- "{\"msg%{public}.0s\":\"#daemon,parsePolygonalGeofencesFromGeometry,success\", \"polygonCount\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,updateGeoAlertCache,success\", \"alertHash\":%{private, location:escape_only}s, \"totalAlerts\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#daemon,updateGeoAlertCache,writeFailed\", \"alertHash\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,emptyPath\"}"
- "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,emptySerialization\"}"
- "{\"msg%{public}.0s\":\"#daemon,writeGeoAlertCacheFile,nilCache\"}"
- "{\"msg%{public}.0s\":\"#daemonInterfaceProd,set settingsPreference\", \"isEarthquakeAlertsEnabled\":%{public}d, \"isOtherAlertsEnabled\":%{public}d, \"isAlwaysPlaySoundEnabled\":%{public}d, \"isImprovedAlertDeliveryEnabled\":%{public}d}"
- "{\"msg%{public}.0s\":\"#eff,collectEfficacyMetricForAlertType,isWeaReceived\", \"isWeaReceived\":%{private}d, \"hash\":%{private, location:escape_only}s, \"timestamp\":\"%{private}.2f\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFailSafe\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"asset\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"featuresSize\":%{public}d}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"featuresSize\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"index\":%{public}d}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary\", \"properties\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,asset nil\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,channelConfigIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,channelIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,elementIsNotDictionary\", \"index\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,feature\", \"feature\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,geometryFailed\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,invalid_features\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,noFeatureInAsset\"}"
- "{\"msg%{public}.0s\":\"#gcma,loadFromDictionary,propertiesIdObjectFailed\"}"
- "{\"msg%{public}.0s\":\"#gsadisp,display,no info entries\"}"
- "{\"msg%{public}.0s\":\"#gsadisp,post\", \"uid\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#gsadisp,post,no valid info entry found\"}"
- "{\"msg%{public}.0s\":\"#gsadisp,post,no_entry_found,fallback_to_first_entry\"}"
- "{\"msg%{public}.0s\":\"#notif,notificationActionsWithAllFeatures\", \"allFeatures\":%{private}hhd, \"actionCount\":%{private}d}"
- "{\"msg%{public}.0s\":\"#notif,notificationActionsWithAllFeatures\", \"kMapsBundleIdentifier\":%{public, location:escape_only}s, \"mapsInstalled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#notif,notificationActionsWithAllFeatures\", \"mapsActionTitle\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#platformInfo\", \"deviceClass\":%{private, location:escape_only}s, \"iPhone\":%{private}hhd, \"iPod\":%{private}hhd, \"iPad\":%{private}hhd, \"watch\":%{private}hhd, \"appleTV\":%{private}hhd, \"homePod\":%{private}hhd, \"mac\":%{private}hhd, \"cellular\":%{private}hhd, \"dualSim\":%{private}hhd, \"cellularWatch\":%{private}hhd, \"wifiOnlyWatch\":%{private}hhd, \"internal\":%{private}hhd, \"supportedDevice\":%{private}hhd, \"supportedOSType\":%{private}hhd, \"supportedPlatform\":%{private}hhd, \"aop\":%{private}hhd, \"tinkerWatch\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguage\", \"language\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguage,invalidOverrideFormat\", \"value\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getPreferredLanguage,override\", \"language\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#stateDump,channel\", \"channelId\":%{private, location:escape_only}s, \"topic\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"write invalid file path\"}"
- "{\"msg%{public}.0s\":\"write open failed\"}"
```
