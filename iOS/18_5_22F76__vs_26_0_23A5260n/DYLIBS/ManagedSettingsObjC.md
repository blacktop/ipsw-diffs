## ManagedSettingsObjC

> `/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC`

```diff

-242.4.10.0.0
-  __TEXT.__text: 0x2293c
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x3204
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__cstring: 0xe65
-  __TEXT.__oslogstring: 0x162d
-  __TEXT.__unwind_info: 0xc88
-  __TEXT.__objc_classname: 0xa14
-  __TEXT.__objc_methname: 0x5d8a
-  __TEXT.__objc_methtype: 0xed4
-  __TEXT.__objc_stubs: 0x1f00
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0x888
-  __DATA_CONST.__objc_classlist: 0x2d8
-  __DATA_CONST.__objc_protolist: 0x80
+257.0.0.0.0
+  __TEXT.__text: 0x2a1f4
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0x3e2c
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__cstring: 0x1184
+  __TEXT.__oslogstring: 0x1610
+  __TEXT.__unwind_info: 0xf38
+  __TEXT.__objc_classname: 0xd20
+  __TEXT.__objc_methname: 0x688b
+  __TEXT.__objc_methtype: 0x1078
+  __TEXT.__objc_stubs: 0x2420
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__objc_classlist: 0x388
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1578
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a0
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x6d90
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH.__objc_data: 0xc8
-  __DATA.__objc_ivar: 0x274
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x600
-  __DATA_DIRTY.__objc_data: 0x1ba8
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x1778
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x218
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0x8748
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x2f8
+  __DATA.__data: 0x7e0
+  __DATA.__bss: 0x690
+  __DATA_DIRTY.__objc_data: 0x1ea0
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2466C0D9-4922-361F-B6D7-8935BB620267
-  Functions: 1120
-  Symbols:   3971
-  CStrings:  1740
+  UUID: E9ACE60D-4FFF-337C-B1A1-6B77EFB5C249
+  Functions: 1363
+  Symbols:   4785
+  CStrings:  1950
 
Symbols:
+ +[MOAudioAccessorySettingsGroup denyTemporaryPairingMetadata]
+ +[MOAudioAccessorySettingsGroup groupName]
+ +[MOAudioAccessorySettingsGroup temporaryPairingConfigurationMetadata]
+ +[MOAudioAccessoryTemporaryPairingConfiguration(Persistence) initializeWithPersistableValue:]
+ +[MOAudioAccessoryTemporaryPairingConfiguration(Persistence) isValidPersistableRepresentation:]
+ +[MOBookmark(Persistence) initializeWithPersistableValue:]
+ +[MOBookmark(Persistence) isValidPersistableRepresentation:]
+ +[MOBookmarkSource(Persistence) initializeWithPersistableValue:]
+ +[MOBookmarkSource(Persistence) isValidPersistableRepresentation:]
+ +[MOBookmarkSource(PersistenceInternal) bookmarkSourceArrayFromPersistedArray:]
+ +[MOBookmarkSource(PersistenceInternal) persistableArrayFromBookmarkSourceArray:]
+ +[MODiagnosticsCollector collectDiagnosticsWithOneTimeConnection:outError:]
+ +[MOEffectiveSettingsStore collectDiagnosticsWithOutError:]
+ +[MOEffectiveSettingsStore(EventStream) startObservingChangesWithHandler:]
+ +[MOEffectiveSettingsStore(EventStream) subscribeForChangesInGroups:eventName:]
+ +[MOEyeReliefSettingsGroup forceScreenDistanceOnMetadata]
+ +[MOEyeReliefSettingsGroup groupName]
+ +[MOInternalLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:]
+ +[MOInternalLocalSettingsStore storesForSharedContainer:oneTimeConnection:]
+ +[MOManagedSettingsSystemAgentConnection newConnection]
+ +[MOManagedSettingsSystemAgentConnection newInterface]
+ +[MOManagedSettingsSystemAgentConnection oneTimeConnection]
+ +[MOManagedSettingsSystemAgentPublisherConnection newAgentInterface]
+ +[MOManagedSettingsSystemAgentPublisherConnection newClientInterface]
+ +[MOManagedSettingsSystemAgentPublisherConnection newConnectionWithExportedObject:]
+ +[MOMediaSettingsGroup denyMediaPurchaseMetadata]
+ +[MOSafariSettingsGroup denyJavaScriptMetadata]
+ +[MOSafariSettingsGroup denyPopupsMetadata]
+ +[MOSafariSettingsGroup denySummaryMetadata]
+ +[MOSafariSettingsGroup forceFraudWarningMetadata]
+ +[MOSafariSettingsGroup managedBookmarksMetadata]
+ +[MOSafariSettingsGroup newTabStartPageMetadata]
+ +[MOSubscriptionCenter systemCenter]
+ +[MOSubscriptionCenter systemCenter].cold.1
+ +[MOSubscriptionCenter userCenter]
+ +[MOSubscriptionCenter userCenter].cold.1
+ +[MOSystemAudioAccessorySettingsGroup denyTemporaryPairingMetadata]
+ +[MOSystemAudioAccessorySettingsGroup groupName]
+ +[MOSystemAudioAccessorySettingsGroup temporaryPairingConfigurationMetadata]
+ +[MOSystemBatchSettingsStore storeWithName:sharedContainer:]
+ +[MOSystemEffectiveSettingsStore collectDiagnosticsWithOutError:]
+ +[MOSystemEffectiveSettingsStore new]
+ +[MOSystemEffectiveSettingsStore publisherForGroups:]
+ +[MOSystemEffectiveSettingsStore setOfActiveRestrictionUUIDs]
+ +[MOSystemEffectiveSettingsStore(EventStream) startObservingChangesWithHandler:]
+ +[MOSystemEffectiveSettingsStore(EventStream) subscribeForChangesInGroups:eventName:]
+ +[MOSystemLocalSettingsStore deleteStoresWithStoreNames:]
+ +[MOSystemLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:]
+ +[MOSystemLocalSettingsStore new]
+ +[MOSystemLocalSettingsStore storesForSharedContainer:]
+ +[MOSystemLocalSettingsStore stores]
+ +[MOSystemLocations effectiveSettingsDirectory]
+ +[MOSystemLocations effectiveSettingsPath]
+ +[MOSystemLocations sharedDirectory]
+ +[MOSystemLocations systemGroupContainerWithGroupIdentifier:]
+ +[MOSystemLocations systemGroupContainerWithGroupIdentifier:].cold.1
+ +[MOSystemSettingsStore createSettingsStoreErrorWithCode:]
+ +[MOUnpairingTime hourPolicyWithHour:]
+ +[MOUnpairingTime nonePolicy]
+ +[MOUnpairingTime(Persistence) initializeWithPersistableValue:]
+ +[MOUnpairingTime(Persistence) isValidPersistableRepresentation:]
+ +[MOWebNewPage extensionPageWithIdentifier:]
+ +[MOWebNewPage homepageWithURL:]
+ +[MOWebNewPage startPage]
+ +[MOWebNewPage(Persistence) initializeWithPersistableValue:]
+ +[MOWebNewPage(Persistence) isValidPersistableRepresentation:]
+ -[MOArraySettingMetadata _combine:with:]
+ -[MOArraySettingMetadata combineOperator]
+ -[MOArraySettingMetadata combinePersistableValue:with:]
+ -[MOArraySettingMetadata defaultValue]
+ -[MOArraySettingMetadata initWithSettingName:defaultArray:combineOperator:maximumCount:isPublic:scope:isPrivacySensitive:]
+ -[MOArraySettingMetadata maximumCount]
+ -[MOArraySettingMetadata persistableValueFromValue:]
+ -[MOArraySettingMetadata sanitizePersistableValue:]
+ -[MOArraySettingMetadata valueFromPersistableValue:]
+ -[MOAudioAccessorySettingsGroup denyTemporaryPairing]
+ -[MOAudioAccessorySettingsGroup setDenyTemporaryPairing:]
+ -[MOAudioAccessorySettingsGroup setTemporaryPairingConfiguration:]
+ -[MOAudioAccessorySettingsGroup temporaryPairingConfiguration]
+ -[MOAudioAccessoryTemporaryPairingConfiguration .cxx_destruct]
+ -[MOAudioAccessoryTemporaryPairingConfiguration hash]
+ -[MOAudioAccessoryTemporaryPairingConfiguration initWithUnpairingTime:]
+ -[MOAudioAccessoryTemporaryPairingConfiguration isEqual:]
+ -[MOAudioAccessoryTemporaryPairingConfiguration unpairingTime]
+ -[MOAudioAccessoryTemporaryPairingConfiguration(Persistence) persistableValue]
+ -[MOBatchSettingsStore internalStore]
+ -[MOBookmark .cxx_destruct]
+ -[MOBookmark children]
+ -[MOBookmark copyWithZone:]
+ -[MOBookmark hash]
+ -[MOBookmark initWithTitle:children:]
+ -[MOBookmark initWithTitle:url:]
+ -[MOBookmark isDirectory]
+ -[MOBookmark isEqual:]
+ -[MOBookmark title]
+ -[MOBookmark url]
+ -[MOBookmark(Persistence) persistableValue]
+ -[MOBookmarkSource .cxx_destruct]
+ -[MOBookmarkSource children]
+ -[MOBookmarkSource copyWithZone:]
+ -[MOBookmarkSource hash]
+ -[MOBookmarkSource initWithSourceIdentifier:title:children:]
+ -[MOBookmarkSource isEqual:]
+ -[MOBookmarkSource sourceIdentifier]
+ -[MOBookmarkSource title]
+ -[MOBookmarkSource(Persistence) persistableValue]
+ -[MOBookmarkSourceArraySettingMetadata _combine:with:]
+ -[MOBookmarkSourceArraySettingMetadata combinePersistableValue:with:]
+ -[MOBookmarkSourceArraySettingMetadata defaultValue]
+ -[MOBookmarkSourceArraySettingMetadata persistableValueFromValue:]
+ -[MOBookmarkSourceArraySettingMetadata reduceValues:intoExistingValues:]
+ -[MOBookmarkSourceArraySettingMetadata sanitizePersistableValue:]
+ -[MOBookmarkSourceArraySettingMetadata valueFromPersistableValue:]
+ -[MOEffectivePublisher initWithInterestedGroups:subscriptionCenter:]
+ -[MOEyeReliefSettingsGroup forceScreenDistanceOn]
+ -[MOEyeReliefSettingsGroup setForceScreenDistanceOn:]
+ -[MOInternalBatchSettingsStore .cxx_destruct]
+ -[MOInternalBatchSettingsStore active]
+ -[MOInternalBatchSettingsStore clearAllSettings]
+ -[MOInternalBatchSettingsStore clearCurrentConnectionAndInvalidate:]
+ -[MOInternalBatchSettingsStore commitChanges]
+ -[MOInternalBatchSettingsStore connectionClass]
+ -[MOInternalBatchSettingsStore connectionLock]
+ -[MOInternalBatchSettingsStore container]
+ -[MOInternalBatchSettingsStore currentConnection]
+ -[MOInternalBatchSettingsStore dealloc]
+ -[MOInternalBatchSettingsStore deleteStore]
+ -[MOInternalBatchSettingsStore fullReplacement]
+ -[MOInternalBatchSettingsStore getCurrentSettings]
+ -[MOInternalBatchSettingsStore getCurrentStoreProperties]
+ -[MOInternalBatchSettingsStore initWithName:sharedContainer:sensitivityChecker:connectionClass:]
+ -[MOInternalBatchSettingsStore name]
+ -[MOInternalBatchSettingsStore persistableValueForSetting:inGroup:]
+ -[MOInternalBatchSettingsStore persistableValueForSettingKey:]
+ -[MOInternalBatchSettingsStore persistenceRecordIdentifier]
+ -[MOInternalBatchSettingsStore removePersistableValueForSetting:inGroup:]
+ -[MOInternalBatchSettingsStore removePersistableValueForSettingKey:]
+ -[MOInternalBatchSettingsStore removedSettings]
+ -[MOInternalBatchSettingsStore sensitivityChecker]
+ -[MOInternalBatchSettingsStore setActive:]
+ -[MOInternalBatchSettingsStore setContainer:]
+ -[MOInternalBatchSettingsStore setCurrentConnection:]
+ -[MOInternalBatchSettingsStore setFullReplacement:]
+ -[MOInternalBatchSettingsStore setName:]
+ -[MOInternalBatchSettingsStore setPersistableValue:forSetting:inGroup:]
+ -[MOInternalBatchSettingsStore setPersistableValue:forSettingKey:]
+ -[MOInternalBatchSettingsStore setPersistenceRecordIdentifier:]
+ -[MOInternalBatchSettingsStore setRemovedSettings:]
+ -[MOInternalBatchSettingsStore setSyncToWatch:]
+ -[MOInternalBatchSettingsStore setUpdatedProperties:]
+ -[MOInternalBatchSettingsStore setUpdatedSettings:]
+ -[MOInternalBatchSettingsStore settingsLock]
+ -[MOInternalBatchSettingsStore settingsReader]
+ -[MOInternalBatchSettingsStore settingsWriter]
+ -[MOInternalBatchSettingsStore syncToWatch]
+ -[MOInternalBatchSettingsStore updatedProperties]
+ -[MOInternalBatchSettingsStore updatedSettings]
+ -[MOInternalBatchSettingsStore xpcConnection]
+ -[MOInternalLocalSettingsStore .cxx_destruct]
+ -[MOInternalLocalSettingsStore active]
+ -[MOInternalLocalSettingsStore clearAllSettings]
+ -[MOInternalLocalSettingsStore clearCurrentConnectionAndInvalidate:]
+ -[MOInternalLocalSettingsStore connectionClass]
+ -[MOInternalLocalSettingsStore connectionLock]
+ -[MOInternalLocalSettingsStore container]
+ -[MOInternalLocalSettingsStore currentConnection]
+ -[MOInternalLocalSettingsStore dealloc]
+ -[MOInternalLocalSettingsStore deleteStore]
+ -[MOInternalLocalSettingsStore getStoreProperties]
+ -[MOInternalLocalSettingsStore initWithName:sharedContainer:sensitivityChecker:connectionClass:]
+ -[MOInternalLocalSettingsStore name]
+ -[MOInternalLocalSettingsStore persistableValueForSetting:inGroup:]
+ -[MOInternalLocalSettingsStore persistableValueForSettingKey:]
+ -[MOInternalLocalSettingsStore persistenceRecordIdentifier]
+ -[MOInternalLocalSettingsStore removePersistableValueForSetting:inGroup:]
+ -[MOInternalLocalSettingsStore removePersistableValueForSettingKey:]
+ -[MOInternalLocalSettingsStore sensitivityChecker]
+ -[MOInternalLocalSettingsStore setActive:]
+ -[MOInternalLocalSettingsStore setContainer:]
+ -[MOInternalLocalSettingsStore setCurrentConnection:]
+ -[MOInternalLocalSettingsStore setName:]
+ -[MOInternalLocalSettingsStore setPersistableValue:forSetting:inGroup:]
+ -[MOInternalLocalSettingsStore setPersistableValue:forSettingKey:]
+ -[MOInternalLocalSettingsStore setPersistenceRecordIdentifier:]
+ -[MOInternalLocalSettingsStore setSyncToWatch:]
+ -[MOInternalLocalSettingsStore settingsReader]
+ -[MOInternalLocalSettingsStore settingsWriter]
+ -[MOInternalLocalSettingsStore syncToWatch]
+ -[MOInternalLocalSettingsStore updateStoreProperties:]
+ -[MOInternalLocalSettingsStore xpcConnection]
+ -[MOLocalSettingsStore internalStore]
+ -[MOMediaSettingsGroup denyMediaPurchase]
+ -[MOMediaSettingsGroup setDenyMediaPurchase:]
+ -[MOSafariSettingsGroup denyJavaScript]
+ -[MOSafariSettingsGroup denyPopups]
+ -[MOSafariSettingsGroup denySummary]
+ -[MOSafariSettingsGroup forceFraudWarning]
+ -[MOSafariSettingsGroup managedBookmarks]
+ -[MOSafariSettingsGroup newTabStartPage]
+ -[MOSafariSettingsGroup setDenyJavaScript:]
+ -[MOSafariSettingsGroup setDenyPopups:]
+ -[MOSafariSettingsGroup setDenySummary:]
+ -[MOSafariSettingsGroup setForceFraudWarning:]
+ -[MOSafariSettingsGroup setManagedBookmarks:]
+ -[MOSafariSettingsGroup setNewTabStartPage:]
+ -[MOSettingsStore audioAccessory]
+ -[MOSettingsStore eyeRelief]
+ -[MOSettingsStore initWithReader:writer:]
+ -[MOSubscriptionCenter connectionClass]
+ -[MOSubscriptionCenter initWithConnectionClass:]
+ -[MOSystemAudioAccessorySettingsGroup denyTemporaryPairing]
+ -[MOSystemAudioAccessorySettingsGroup setDenyTemporaryPairing:]
+ -[MOSystemAudioAccessorySettingsGroup setTemporaryPairingConfiguration:]
+ -[MOSystemAudioAccessorySettingsGroup temporaryPairingConfiguration]
+ -[MOSystemBatchSettingsStore .cxx_destruct]
+ -[MOSystemBatchSettingsStore active]
+ -[MOSystemBatchSettingsStore clearAllSettings]
+ -[MOSystemBatchSettingsStore commitChanges]
+ -[MOSystemBatchSettingsStore deleteStore]
+ -[MOSystemBatchSettingsStore initWithName:sharedContainer:]
+ -[MOSystemBatchSettingsStore internalStore]
+ -[MOSystemBatchSettingsStore setActive:]
+ -[MOSystemBatchSettingsStore setSyncToWatch:]
+ -[MOSystemBatchSettingsStore syncToWatch]
+ -[MOSystemEffectiveSettingsStore dealloc]
+ -[MOSystemEffectiveSettingsStore init]
+ -[MOSystemEffectiveSettingsStore persistableValueForSetting:inGroup:]
+ -[MOSystemEffectiveSettingsStore persistableValueForSettingKey:]
+ -[MOSystemEffectiveSettingsStore persistableValueForSettingKey:].cold.1
+ -[MOSystemEffectiveSettingsStore settingsReader]
+ -[MOSystemLocalSettingsStore .cxx_destruct]
+ -[MOSystemLocalSettingsStore active]
+ -[MOSystemLocalSettingsStore batchUpdate:]
+ -[MOSystemLocalSettingsStore clearAllSettings]
+ -[MOSystemLocalSettingsStore deleteStore]
+ -[MOSystemLocalSettingsStore initWithName:]
+ -[MOSystemLocalSettingsStore initWithName:sharedContainer:]
+ -[MOSystemLocalSettingsStore initWithSharedContainer:]
+ -[MOSystemLocalSettingsStore init]
+ -[MOSystemLocalSettingsStore internalStore]
+ -[MOSystemLocalSettingsStore setActive:]
+ -[MOSystemLocalSettingsStore setSyncToWatch:]
+ -[MOSystemLocalSettingsStore syncToWatch]
+ -[MOSystemSettingsStore .cxx_destruct]
+ -[MOSystemSettingsStore audioAccessory]
+ -[MOSystemSettingsStore hasSensitiveDataInSettings:]
+ -[MOSystemSettingsStore initWithReader:writer:]
+ -[MOSystemSettingsStore metadataForSettingKey:]
+ -[MOSystemSettingsStore metadataForSettingKey:].cold.1
+ -[MOSystemSettingsStore setValue:forSettingKey:outError:]
+ -[MOSystemSettingsStore setValue:forSettingKey:outError:].cold.1
+ -[MOSystemSettingsStore setValue:forSettingKey:outError:].cold.2
+ -[MOSystemSettingsStore setValue:forSettingKey:outError:].cold.3
+ -[MOSystemSettingsStore settingsReader]
+ -[MOSystemSettingsStore settingsWriter]
+ -[MOSystemSettingsStore valueForSettingKey:]
+ -[MOSystemSettingsStore valueForSettingKey:].cold.1
+ -[MOSystemSettingsStore valueForSettingKey:].cold.2
+ -[MOSystemSettingsStore valueForUndefinedKey:]
+ -[MOSystemSettingsStore valueForUndefinedKey:].cold.1
+ -[MOTemporaryPairingConfigurationSettingMetadata _combine:with:]
+ -[MOTemporaryPairingConfigurationSettingMetadata combineOperator]
+ -[MOTemporaryPairingConfigurationSettingMetadata combinePersistableValue:with:]
+ -[MOTemporaryPairingConfigurationSettingMetadata defaultValue]
+ -[MOTemporaryPairingConfigurationSettingMetadata initWithSettingName:defaultConfiguration:combineOperator:isPublic:scope:isPrivacySensitive:]
+ -[MOTemporaryPairingConfigurationSettingMetadata persistableValueFromValue:]
+ -[MOTemporaryPairingConfigurationSettingMetadata sanitizePersistableValue:]
+ -[MOTemporaryPairingConfigurationSettingMetadata valueFromPersistableValue:]
+ -[MOUnpairingTime .cxx_destruct]
+ -[MOUnpairingTime hash]
+ -[MOUnpairingTime hour]
+ -[MOUnpairingTime initWithPolicy:hour:]
+ -[MOUnpairingTime isEqual:]
+ -[MOUnpairingTime policy]
+ -[MOUnpairingTime(Persistence) persistableValue]
+ -[MOWebDomain bookmark]
+ -[MOWebDomain initWithDomain:bookmark:]
+ -[MOWebNewPage .cxx_destruct]
+ -[MOWebNewPage extensionIdentifier]
+ -[MOWebNewPage hash]
+ -[MOWebNewPage homepageURL]
+ -[MOWebNewPage initWithPageType:homepageURL:extensionIdentifier:]
+ -[MOWebNewPage isEqual:]
+ -[MOWebNewPage pageType]
+ -[MOWebNewPage(Persistence) persistableValue]
+ -[MOWebNewPageSettingMetadata _combine:with:]
+ -[MOWebNewPageSettingMetadata combineOperator]
+ -[MOWebNewPageSettingMetadata combinePersistableValue:with:]
+ -[MOWebNewPageSettingMetadata defaultValue]
+ -[MOWebNewPageSettingMetadata initWithSettingName:defaultWebNewPage:combineOperator:isPublic:scope:isPrivacySensitive:]
+ -[MOWebNewPageSettingMetadata persistableValueFromValue:]
+ -[MOWebNewPageSettingMetadata sanitizePersistableValue:]
+ -[MOWebNewPageSettingMetadata valueFromPersistableValue:]
+ GCC_except_table17
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ _MOEffectiveSettingsGroupAudioAccessory
+ _MOEffectiveSettingsGroupEyeRelief
+ _MOPersistenceKeyBookmark
+ _MOPersistenceKeyChildren
+ _MOPersistenceKeyExtensionIdentifier
+ _MOPersistenceKeyHomepageURL
+ _MOPersistenceKeyHour
+ _MOPersistenceKeyPageType
+ _MOPersistenceKeyPolicy
+ _MOPersistenceKeySourceIdentifier
+ _MOPersistenceKeyTitle
+ _MOPersistenceKeyURL
+ _MOPersistenceKeyUnpairingTime
+ _MOSettingsGroupNameAudioAccessory
+ _MOSettingsGroupNameEyeRelief
+ _MOSystemClientRestrictionUUIDBase
+ _OBJC_CLASS_$_MOArraySettingMetadata
+ _OBJC_CLASS_$_MOAudioAccessorySettingsGroup
+ _OBJC_CLASS_$_MOAudioAccessoryTemporaryPairingConfiguration
+ _OBJC_CLASS_$_MOBookmark
+ _OBJC_CLASS_$_MOBookmarkSource
+ _OBJC_CLASS_$_MOBookmarkSourceArraySettingMetadata
+ _OBJC_CLASS_$_MODiagnosticsCollector
+ _OBJC_CLASS_$_MOEyeReliefSettingsGroup
+ _OBJC_CLASS_$_MOInternalBatchSettingsStore
+ _OBJC_CLASS_$_MOInternalLocalSettingsStore
+ _OBJC_CLASS_$_MOManagedSettingsSystemAgentConnection
+ _OBJC_CLASS_$_MOManagedSettingsSystemAgentPublisherConnection
+ _OBJC_CLASS_$_MOSystemAudioAccessorySettingsGroup
+ _OBJC_CLASS_$_MOSystemBatchSettingsStore
+ _OBJC_CLASS_$_MOSystemEffectiveSettingsStore
+ _OBJC_CLASS_$_MOSystemLocalSettingsStore
+ _OBJC_CLASS_$_MOSystemLocations
+ _OBJC_CLASS_$_MOSystemSettingsStore
+ _OBJC_CLASS_$_MOTemporaryPairingConfigurationSettingMetadata
+ _OBJC_CLASS_$_MOUnpairingTime
+ _OBJC_CLASS_$_MOWebNewPage
+ _OBJC_CLASS_$_MOWebNewPageSettingMetadata
+ _OBJC_IVAR_$_MOArraySettingMetadata._combineOperator
+ _OBJC_IVAR_$_MOArraySettingMetadata._maximumCount
+ _OBJC_IVAR_$_MOAudioAccessoryTemporaryPairingConfiguration._unpairingTime
+ _OBJC_IVAR_$_MOBatchSettingsStore._internalStore
+ _OBJC_IVAR_$_MOBookmark._children
+ _OBJC_IVAR_$_MOBookmark._title
+ _OBJC_IVAR_$_MOBookmark._url
+ _OBJC_IVAR_$_MOBookmarkSource._children
+ _OBJC_IVAR_$_MOBookmarkSource._sourceIdentifier
+ _OBJC_IVAR_$_MOBookmarkSource._title
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._connectionClass
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._connectionLock
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._container
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._currentConnection
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._fullReplacement
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._name
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._persistenceRecordIdentifier
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._removedSettings
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._sensitivityChecker
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._settingsLock
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._updatedProperties
+ _OBJC_IVAR_$_MOInternalBatchSettingsStore._updatedSettings
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._connectionClass
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._connectionLock
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._container
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._currentConnection
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._name
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._persistenceRecordIdentifier
+ _OBJC_IVAR_$_MOInternalLocalSettingsStore._sensitivityChecker
+ _OBJC_IVAR_$_MOLocalSettingsStore._internalStore
+ _OBJC_IVAR_$_MOSettingsStore._audioAccessory
+ _OBJC_IVAR_$_MOSettingsStore._eyeRelief
+ _OBJC_IVAR_$_MOSettingsStore._settingsReader
+ _OBJC_IVAR_$_MOSettingsStore._settingsWriter
+ _OBJC_IVAR_$_MOSubscriptionCenter._connectionClass
+ _OBJC_IVAR_$_MOSystemBatchSettingsStore._internalStore
+ _OBJC_IVAR_$_MOSystemLocalSettingsStore._internalStore
+ _OBJC_IVAR_$_MOSystemSettingsStore._audioAccessory
+ _OBJC_IVAR_$_MOSystemSettingsStore._settingsReader
+ _OBJC_IVAR_$_MOSystemSettingsStore._settingsWriter
+ _OBJC_IVAR_$_MOTemporaryPairingConfigurationSettingMetadata._combineOperator
+ _OBJC_IVAR_$_MOUnpairingTime._hour
+ _OBJC_IVAR_$_MOUnpairingTime._policy
+ _OBJC_IVAR_$_MOWebDomain._bookmark
+ _OBJC_IVAR_$_MOWebNewPage._extensionIdentifier
+ _OBJC_IVAR_$_MOWebNewPage._homepageURL
+ _OBJC_IVAR_$_MOWebNewPage._pageType
+ _OBJC_IVAR_$_MOWebNewPageSettingMetadata._combineOperator
+ _OBJC_METACLASS_$_MOArraySettingMetadata
+ _OBJC_METACLASS_$_MOAudioAccessorySettingsGroup
+ _OBJC_METACLASS_$_MOAudioAccessoryTemporaryPairingConfiguration
+ _OBJC_METACLASS_$_MOBookmark
+ _OBJC_METACLASS_$_MOBookmarkSource
+ _OBJC_METACLASS_$_MOBookmarkSourceArraySettingMetadata
+ _OBJC_METACLASS_$_MODiagnosticsCollector
+ _OBJC_METACLASS_$_MOEyeReliefSettingsGroup
+ _OBJC_METACLASS_$_MOInternalBatchSettingsStore
+ _OBJC_METACLASS_$_MOInternalLocalSettingsStore
+ _OBJC_METACLASS_$_MOManagedSettingsSystemAgentConnection
+ _OBJC_METACLASS_$_MOManagedSettingsSystemAgentPublisherConnection
+ _OBJC_METACLASS_$_MOSystemAudioAccessorySettingsGroup
+ _OBJC_METACLASS_$_MOSystemBatchSettingsStore
+ _OBJC_METACLASS_$_MOSystemEffectiveSettingsStore
+ _OBJC_METACLASS_$_MOSystemLocalSettingsStore
+ _OBJC_METACLASS_$_MOSystemLocations
+ _OBJC_METACLASS_$_MOSystemSettingsStore
+ _OBJC_METACLASS_$_MOTemporaryPairingConfigurationSettingMetadata
+ _OBJC_METACLASS_$_MOUnpairingTime
+ _OBJC_METACLASS_$_MOWebNewPage
+ _OBJC_METACLASS_$_MOWebNewPageSettingMetadata
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_CLASS_METHODS_MOAudioAccessorySettingsGroup
+ __OBJC_$_CLASS_METHODS_MOAudioAccessoryTemporaryPairingConfiguration(Persistence)
+ __OBJC_$_CLASS_METHODS_MOBookmark(Persistence)
+ __OBJC_$_CLASS_METHODS_MOBookmarkSource(Persistence|PersistenceInternal)
+ __OBJC_$_CLASS_METHODS_MODiagnosticsCollector
+ __OBJC_$_CLASS_METHODS_MOEffectiveSettingsStore(EventStream)
+ __OBJC_$_CLASS_METHODS_MOEyeReliefSettingsGroup
+ __OBJC_$_CLASS_METHODS_MOInternalLocalSettingsStore
+ __OBJC_$_CLASS_METHODS_MOManagedSettingsSystemAgentConnection
+ __OBJC_$_CLASS_METHODS_MOManagedSettingsSystemAgentPublisherConnection
+ __OBJC_$_CLASS_METHODS_MOSystemAudioAccessorySettingsGroup
+ __OBJC_$_CLASS_METHODS_MOSystemBatchSettingsStore
+ __OBJC_$_CLASS_METHODS_MOSystemEffectiveSettingsStore(EventStream)
+ __OBJC_$_CLASS_METHODS_MOSystemLocalSettingsStore
+ __OBJC_$_CLASS_METHODS_MOSystemLocations
+ __OBJC_$_CLASS_METHODS_MOSystemSettingsStore
+ __OBJC_$_CLASS_METHODS_MOUnpairingTime(Persistence)
+ __OBJC_$_CLASS_METHODS_MOWebNewPage(Persistence)
+ __OBJC_$_CLASS_PROP_LIST_MOAudioAccessorySettingsGroup
+ __OBJC_$_CLASS_PROP_LIST_MOEyeReliefSettingsGroup
+ __OBJC_$_CLASS_PROP_LIST_MOLocatable
+ __OBJC_$_CLASS_PROP_LIST_MOSystemAudioAccessorySettingsGroup
+ __OBJC_$_CLASS_PROP_LIST_MOSystemLocalSettingsStore
+ __OBJC_$_CLASS_PROP_LIST_MOSystemLocations
+ __OBJC_$_INSTANCE_METHODS_MOArraySettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOAudioAccessorySettingsGroup
+ __OBJC_$_INSTANCE_METHODS_MOAudioAccessoryTemporaryPairingConfiguration(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOBookmark(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOBookmarkSource(Persistence|PersistenceInternal)
+ __OBJC_$_INSTANCE_METHODS_MOBookmarkSourceArraySettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOEyeReliefSettingsGroup
+ __OBJC_$_INSTANCE_METHODS_MOInternalBatchSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOInternalLocalSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOSystemAudioAccessorySettingsGroup
+ __OBJC_$_INSTANCE_METHODS_MOSystemBatchSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOSystemEffectiveSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOSystemLocalSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOSystemSettingsStore
+ __OBJC_$_INSTANCE_METHODS_MOTemporaryPairingConfigurationSettingMetadata
+ __OBJC_$_INSTANCE_METHODS_MOUnpairingTime(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOWebNewPage(Persistence)
+ __OBJC_$_INSTANCE_METHODS_MOWebNewPageSettingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOArraySettingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOAudioAccessoryTemporaryPairingConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_MOBookmark
+ __OBJC_$_INSTANCE_VARIABLES_MOBookmarkSource
+ __OBJC_$_INSTANCE_VARIABLES_MOInternalBatchSettingsStore
+ __OBJC_$_INSTANCE_VARIABLES_MOInternalLocalSettingsStore
+ __OBJC_$_INSTANCE_VARIABLES_MOSystemBatchSettingsStore
+ __OBJC_$_INSTANCE_VARIABLES_MOSystemLocalSettingsStore
+ __OBJC_$_INSTANCE_VARIABLES_MOSystemSettingsStore
+ __OBJC_$_INSTANCE_VARIABLES_MOTemporaryPairingConfigurationSettingMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MOUnpairingTime
+ __OBJC_$_INSTANCE_VARIABLES_MOWebNewPage
+ __OBJC_$_INSTANCE_VARIABLES_MOWebNewPageSettingMetadata
+ __OBJC_$_PROP_LIST_MOArraySettingMetadata
+ __OBJC_$_PROP_LIST_MOAudioAccessorySettingsGroup
+ __OBJC_$_PROP_LIST_MOBookmarkSourceArraySettingMetadata
+ __OBJC_$_PROP_LIST_MOEyeReliefSettingsGroup
+ __OBJC_$_PROP_LIST_MOInternalBatchSettingsStore
+ __OBJC_$_PROP_LIST_MOInternalLocalSettingsStore
+ __OBJC_$_PROP_LIST_MOLocations
+ __OBJC_$_PROP_LIST_MOSystemAudioAccessorySettingsGroup
+ __OBJC_$_PROP_LIST_MOSystemBatchSettingsStore
+ __OBJC_$_PROP_LIST_MOSystemLocalSettingsStore
+ __OBJC_$_PROP_LIST_MOSystemLocations
+ __OBJC_$_PROP_LIST_MOSystemSettingsStore
+ __OBJC_$_PROP_LIST_MOTemporaryPairingConfigurationSettingMetadata
+ __OBJC_$_PROP_LIST_MOWebNewPageSettingMetadata
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MOLocatable
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MOManagedSettingsConnection
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MOManagedSettingsPublisherConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOManagedSettingsProxy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOLocatable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOManagedSettingsConnection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOManagedSettingsProxy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MOManagedSettingsPublisherConnection
+ __OBJC_$_PROTOCOL_REFS_MOLocatable
+ __OBJC_$_PROTOCOL_REFS_MOManagedSettingsProxy
+ __OBJC_$_PROTOCOL_REFS_MOManagedSettingsSystemAgent
+ __OBJC_CLASS_PROTOCOLS_$_MOAudioAccessoryTemporaryPairingConfiguration(Persistence)
+ __OBJC_CLASS_PROTOCOLS_$_MOBookmark(Persistence)
+ __OBJC_CLASS_PROTOCOLS_$_MOBookmarkSource(Persistence|PersistenceInternal)
+ __OBJC_CLASS_PROTOCOLS_$_MOInternalBatchSettingsStore
+ __OBJC_CLASS_PROTOCOLS_$_MOInternalLocalSettingsStore
+ __OBJC_CLASS_PROTOCOLS_$_MOLocations
+ __OBJC_CLASS_PROTOCOLS_$_MOManagedSettingsAgentConnection
+ __OBJC_CLASS_PROTOCOLS_$_MOManagedSettingsAgentPublisherConnection
+ __OBJC_CLASS_PROTOCOLS_$_MOManagedSettingsSystemAgentConnection
+ __OBJC_CLASS_PROTOCOLS_$_MOManagedSettingsSystemAgentPublisherConnection
+ __OBJC_CLASS_PROTOCOLS_$_MOSystemEffectiveSettingsStore
+ __OBJC_CLASS_PROTOCOLS_$_MOSystemLocations
+ __OBJC_CLASS_PROTOCOLS_$_MOUnpairingTime(Persistence)
+ __OBJC_CLASS_PROTOCOLS_$_MOWebNewPage(Persistence)
+ __OBJC_CLASS_RO_$_MOArraySettingMetadata
+ __OBJC_CLASS_RO_$_MOAudioAccessorySettingsGroup
+ __OBJC_CLASS_RO_$_MOAudioAccessoryTemporaryPairingConfiguration
+ __OBJC_CLASS_RO_$_MOBookmark
+ __OBJC_CLASS_RO_$_MOBookmarkSource
+ __OBJC_CLASS_RO_$_MOBookmarkSourceArraySettingMetadata
+ __OBJC_CLASS_RO_$_MODiagnosticsCollector
+ __OBJC_CLASS_RO_$_MOEyeReliefSettingsGroup
+ __OBJC_CLASS_RO_$_MOInternalBatchSettingsStore
+ __OBJC_CLASS_RO_$_MOInternalLocalSettingsStore
+ __OBJC_CLASS_RO_$_MOManagedSettingsSystemAgentConnection
+ __OBJC_CLASS_RO_$_MOManagedSettingsSystemAgentPublisherConnection
+ __OBJC_CLASS_RO_$_MOSystemAudioAccessorySettingsGroup
+ __OBJC_CLASS_RO_$_MOSystemBatchSettingsStore
+ __OBJC_CLASS_RO_$_MOSystemEffectiveSettingsStore
+ __OBJC_CLASS_RO_$_MOSystemLocalSettingsStore
+ __OBJC_CLASS_RO_$_MOSystemLocations
+ __OBJC_CLASS_RO_$_MOSystemSettingsStore
+ __OBJC_CLASS_RO_$_MOTemporaryPairingConfigurationSettingMetadata
+ __OBJC_CLASS_RO_$_MOUnpairingTime
+ __OBJC_CLASS_RO_$_MOWebNewPage
+ __OBJC_CLASS_RO_$_MOWebNewPageSettingMetadata
+ __OBJC_LABEL_PROTOCOL_$_MOLocatable
+ __OBJC_LABEL_PROTOCOL_$_MOManagedSettingsConnection
+ __OBJC_LABEL_PROTOCOL_$_MOManagedSettingsProxy
+ __OBJC_LABEL_PROTOCOL_$_MOManagedSettingsPublisherConnection
+ __OBJC_LABEL_PROTOCOL_$_MOManagedSettingsSystemAgent
+ __OBJC_METACLASS_RO_$_MOArraySettingMetadata
+ __OBJC_METACLASS_RO_$_MOAudioAccessorySettingsGroup
+ __OBJC_METACLASS_RO_$_MOAudioAccessoryTemporaryPairingConfiguration
+ __OBJC_METACLASS_RO_$_MOBookmark
+ __OBJC_METACLASS_RO_$_MOBookmarkSource
+ __OBJC_METACLASS_RO_$_MOBookmarkSourceArraySettingMetadata
+ __OBJC_METACLASS_RO_$_MODiagnosticsCollector
+ __OBJC_METACLASS_RO_$_MOEyeReliefSettingsGroup
+ __OBJC_METACLASS_RO_$_MOInternalBatchSettingsStore
+ __OBJC_METACLASS_RO_$_MOInternalLocalSettingsStore
+ __OBJC_METACLASS_RO_$_MOManagedSettingsSystemAgentConnection
+ __OBJC_METACLASS_RO_$_MOManagedSettingsSystemAgentPublisherConnection
+ __OBJC_METACLASS_RO_$_MOSystemAudioAccessorySettingsGroup
+ __OBJC_METACLASS_RO_$_MOSystemBatchSettingsStore
+ __OBJC_METACLASS_RO_$_MOSystemEffectiveSettingsStore
+ __OBJC_METACLASS_RO_$_MOSystemLocalSettingsStore
+ __OBJC_METACLASS_RO_$_MOSystemLocations
+ __OBJC_METACLASS_RO_$_MOSystemSettingsStore
+ __OBJC_METACLASS_RO_$_MOTemporaryPairingConfigurationSettingMetadata
+ __OBJC_METACLASS_RO_$_MOUnpairingTime
+ __OBJC_METACLASS_RO_$_MOWebNewPage
+ __OBJC_METACLASS_RO_$_MOWebNewPageSettingMetadata
+ __OBJC_PROTOCOL_$_MOLocatable
+ __OBJC_PROTOCOL_$_MOManagedSettingsConnection
+ __OBJC_PROTOCOL_$_MOManagedSettingsProxy
+ __OBJC_PROTOCOL_$_MOManagedSettingsPublisherConnection
+ __OBJC_PROTOCOL_$_MOManagedSettingsSystemAgent
+ __OBJC_PROTOCOL_REFERENCE_$_MOManagedSettingsSystemAgent
+ ___34+[MOSubscriptionCenter userCenter]_block_invoke
+ ___36+[MOSubscriptionCenter systemCenter]_block_invoke
+ ___39-[MOSettingMetadata responsibleClients]_block_invoke.4
+ ___39-[MOSettingMetadata responsibleClients]_block_invoke.4.cold.1
+ ___43+[MOSafariSettingsGroup denyPopupsMetadata]_block_invoke
+ ___43-[MOInternalLocalSettingsStore deleteStore]_block_invoke
+ ___43-[MOInternalLocalSettingsStore deleteStore]_block_invoke.16
+ ___43-[MOInternalLocalSettingsStore deleteStore]_block_invoke.16.cold.1
+ ___43-[MOInternalLocalSettingsStore deleteStore]_block_invoke.cold.1
+ ___44+[MOSafariSettingsGroup denySummaryMetadata]_block_invoke
+ ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke
+ ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.16
+ ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.16.cold.1
+ ___45-[MOInternalBatchSettingsStore commitChanges]_block_invoke.cold.1
+ ___45-[MOInternalBatchSettingsStore xpcConnection]_block_invoke
+ ___45-[MOInternalBatchSettingsStore xpcConnection]_block_invoke_2
+ ___45-[MOInternalLocalSettingsStore xpcConnection]_block_invoke
+ ___45-[MOInternalLocalSettingsStore xpcConnection]_block_invoke_2
+ ___47+[MOSafariSettingsGroup denyJavaScriptMetadata]_block_invoke
+ ___48+[MOSafariSettingsGroup newTabStartPageMetadata]_block_invoke
+ ___48-[MOInternalLocalSettingsStore clearAllSettings]_block_invoke
+ ___48-[MOInternalLocalSettingsStore clearAllSettings]_block_invoke.13
+ ___48-[MOInternalLocalSettingsStore clearAllSettings]_block_invoke.13.cold.1
+ ___48-[MOInternalLocalSettingsStore clearAllSettings]_block_invoke.cold.1
+ ___49+[MOMediaSettingsGroup denyMediaPurchaseMetadata]_block_invoke
+ ___49+[MOSafariSettingsGroup managedBookmarksMetadata]_block_invoke
+ ___50+[MOSafariSettingsGroup forceFraudWarningMetadata]_block_invoke
+ ___50-[MOInternalBatchSettingsStore getCurrentSettings]_block_invoke
+ ___50-[MOInternalBatchSettingsStore getCurrentSettings]_block_invoke.11
+ ___50-[MOInternalBatchSettingsStore getCurrentSettings]_block_invoke.11.cold.1
+ ___50-[MOInternalBatchSettingsStore getCurrentSettings]_block_invoke.11.cold.2
+ ___50-[MOInternalBatchSettingsStore getCurrentSettings]_block_invoke.cold.1
+ ___50-[MOInternalLocalSettingsStore getStoreProperties]_block_invoke
+ ___50-[MOInternalLocalSettingsStore getStoreProperties]_block_invoke.8
+ ___50-[MOInternalLocalSettingsStore getStoreProperties]_block_invoke.8.cold.1
+ ___50-[MOInternalLocalSettingsStore getStoreProperties]_block_invoke.8.cold.2
+ ___50-[MOInternalLocalSettingsStore getStoreProperties]_block_invoke.cold.1
+ ___52-[MOSystemSettingsStore hasSensitiveDataInSettings:]_block_invoke
+ ___53-[MOBatchSettingsStore initWithName:sharedContainer:]_block_invoke
+ ___53-[MOLocalSettingsStore initWithName:sharedContainer:]_block_invoke
+ ___54-[MOInternalLocalSettingsStore updateStoreProperties:]_block_invoke
+ ___54-[MOInternalLocalSettingsStore updateStoreProperties:]_block_invoke.11
+ ___54-[MOInternalLocalSettingsStore updateStoreProperties:]_block_invoke.11.cold.1
+ ___54-[MOInternalLocalSettingsStore updateStoreProperties:]_block_invoke.cold.1
+ ___57+[MOEyeReliefSettingsGroup forceScreenDistanceOnMetadata]_block_invoke
+ ___57-[MOInternalBatchSettingsStore getCurrentStoreProperties]_block_invoke
+ ___57-[MOInternalBatchSettingsStore getCurrentStoreProperties]_block_invoke.8
+ ___57-[MOInternalBatchSettingsStore getCurrentStoreProperties]_block_invoke.8.cold.1
+ ___57-[MOInternalBatchSettingsStore getCurrentStoreProperties]_block_invoke.8.cold.2
+ ___57-[MOInternalBatchSettingsStore getCurrentStoreProperties]_block_invoke.cold.1
+ ___59+[MOManagedSettingsSystemAgentConnection oneTimeConnection]_block_invoke
+ ___59-[MOSystemBatchSettingsStore initWithName:sharedContainer:]_block_invoke
+ ___59-[MOSystemLocalSettingsStore initWithName:sharedContainer:]_block_invoke
+ ___61+[MOAudioAccessorySettingsGroup denyTemporaryPairingMetadata]_block_invoke
+ ___62-[MOInternalLocalSettingsStore persistableValueForSettingKey:]_block_invoke
+ ___62-[MOInternalLocalSettingsStore persistableValueForSettingKey:]_block_invoke.22
+ ___62-[MOInternalLocalSettingsStore persistableValueForSettingKey:]_block_invoke.22.cold.1
+ ___62-[MOInternalLocalSettingsStore persistableValueForSettingKey:]_block_invoke.cold.1
+ ___66-[MOInternalLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke
+ ___66-[MOInternalLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.23
+ ___66-[MOInternalLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.23.cold.1
+ ___66-[MOInternalLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.cold.1
+ ___67+[MOSystemAudioAccessorySettingsGroup denyTemporaryPairingMetadata]_block_invoke
+ ___68-[MOEffectivePublisher initWithInterestedGroups:subscriptionCenter:]_block_invoke
+ ___68-[MOEffectivePublisher initWithInterestedGroups:subscriptionCenter:]_block_invoke_2
+ ___68-[MOInternalLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke
+ ___68-[MOInternalLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.24
+ ___68-[MOInternalLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.24.cold.1
+ ___68-[MOInternalLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.cold.1
+ ___70+[MOAudioAccessorySettingsGroup temporaryPairingConfigurationMetadata]_block_invoke
+ ___74+[MOEffectiveSettingsStore(EventStream) startObservingChangesWithHandler:]_block_invoke
+ ___75+[MODiagnosticsCollector collectDiagnosticsWithOneTimeConnection:outError:]_block_invoke
+ ___75+[MODiagnosticsCollector collectDiagnosticsWithOneTimeConnection:outError:]_block_invoke.2
+ ___75+[MODiagnosticsCollector collectDiagnosticsWithOneTimeConnection:outError:]_block_invoke.2.cold.1
+ ___75+[MODiagnosticsCollector collectDiagnosticsWithOneTimeConnection:outError:]_block_invoke.cold.1
+ ___75+[MOInternalLocalSettingsStore storesForSharedContainer:oneTimeConnection:]_block_invoke
+ ___75+[MOInternalLocalSettingsStore storesForSharedContainer:oneTimeConnection:]_block_invoke.19
+ ___75+[MOInternalLocalSettingsStore storesForSharedContainer:oneTimeConnection:]_block_invoke.19.cold.1
+ ___75+[MOInternalLocalSettingsStore storesForSharedContainer:oneTimeConnection:]_block_invoke.cold.1
+ ___76+[MOSystemAudioAccessorySettingsGroup temporaryPairingConfigurationMetadata]_block_invoke
+ ___80+[MOSystemEffectiveSettingsStore(EventStream) startObservingChangesWithHandler:]_block_invoke
+ ___93+[MOInternalLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:]_block_invoke
+ ___93+[MOInternalLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:]_block_invoke.18
+ ___93+[MOInternalLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:]_block_invoke.18.cold.1
+ ___93+[MOInternalLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:]_block_invoke.cold.1
+ ___MOSettingsGroupNamesFromXPCEvent_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32s_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e17_B16?0"NSArray"8lw32l8
+ ___block_descriptor_48_e8_32s40r_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e16_v16?0"NSUUID"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e27_v24?0"NSURL"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e59_v24?0"<MOEffectiveApplicationSettingsProxy>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e42_v24?0"<MOBlameFinderProxy>"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v24?0"<MOManagedSettingsProxy>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s40l8s48l8r56l8r64l8
+ _container_system_group_path_for_identifier
+ _denyJavaScriptMetadata.metadata
+ _denyJavaScriptMetadata.onceToken
+ _denyMediaPurchaseMetadata.metadata
+ _denyMediaPurchaseMetadata.onceToken
+ _denyPopupsMetadata.metadata
+ _denyPopupsMetadata.onceToken
+ _denySummaryMetadata.metadata
+ _denySummaryMetadata.onceToken
+ _denyTemporaryPairingMetadata.metadata
+ _denyTemporaryPairingMetadata.metadata.28
+ _denyTemporaryPairingMetadata.onceToken
+ _denyTemporaryPairingMetadata.onceToken.29
+ _forceFraudWarningMetadata.metadata
+ _forceFraudWarningMetadata.onceToken
+ _forceScreenDistanceOnMetadata.metadata
+ _forceScreenDistanceOnMetadata.onceToken
+ _free
+ _kDefaultStoreName
+ _managedBookmarksMetadata.metadata
+ _managedBookmarksMetadata.onceToken
+ _newTabStartPageMetadata.metadata
+ _newTabStartPageMetadata.onceToken
+ _objc_msgSend$active
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$bookmark
+ _objc_msgSend$bookmarkSourceArrayFromPersistedArray:
+ _objc_msgSend$children
+ _objc_msgSend$clearAllSettings
+ _objc_msgSend$collectDiagnosticsWithOneTimeConnection:outError:
+ _objc_msgSend$collectDiagnosticsWithReplyHandler:
+ _objc_msgSend$combineOperator
+ _objc_msgSend$deleteStore
+ _objc_msgSend$deleteStoresWithStoreNames:sharedContainer:
+ _objc_msgSend$deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:
+ _objc_msgSend$effective
+ _objc_msgSend$extensionIdentifier
+ _objc_msgSend$extensionPageWithIdentifier:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$homepageURL
+ _objc_msgSend$homepageWithURL:
+ _objc_msgSend$hour
+ _objc_msgSend$hourPolicyWithHour:
+ _objc_msgSend$initWithConnectionClass:
+ _objc_msgSend$initWithDomain:bookmark:
+ _objc_msgSend$initWithInterestedGroups:subscriptionCenter:
+ _objc_msgSend$initWithName:sharedContainer:sensitivityChecker:connectionClass:
+ _objc_msgSend$initWithPageType:homepageURL:extensionIdentifier:
+ _objc_msgSend$initWithPolicy:hour:
+ _objc_msgSend$initWithSettingName:defaultArray:combineOperator:maximumCount:isPublic:scope:isPrivacySensitive:
+ _objc_msgSend$initWithSettingName:defaultConfiguration:combineOperator:isPublic:scope:isPrivacySensitive:
+ _objc_msgSend$initWithSettingName:defaultWebNewPage:combineOperator:isPublic:scope:isPrivacySensitive:
+ _objc_msgSend$initWithSourceIdentifier:title:children:
+ _objc_msgSend$initWithTitle:children:
+ _objc_msgSend$initWithTitle:url:
+ _objc_msgSend$initWithUnpairingTime:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$pageType
+ _objc_msgSend$persistableArrayFromBookmarkSourceArray:
+ _objc_msgSend$reduceValues:intoExistingValues:
+ _objc_msgSend$sensitivityChecker
+ _objc_msgSend$setActive:
+ _objc_msgSend$setSyncToWatch:
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$startPage
+ _objc_msgSend$storesForSharedContainer:oneTimeConnection:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$syncToWatch
+ _objc_msgSend$systemCenter
+ _objc_msgSend$systemGroupContainerWithGroupIdentifier:
+ _objc_msgSend$title
+ _objc_msgSend$unpairingTime
+ _objc_msgSend$url
+ _objc_msgSend$userCenter
+ _systemCenter._sharedCenter
+ _systemCenter.onceToken
+ _temporaryPairingConfigurationMetadata.metadata
+ _temporaryPairingConfigurationMetadata.metadata.30
+ _temporaryPairingConfigurationMetadata.onceToken
+ _temporaryPairingConfigurationMetadata.onceToken.31
+ _userCenter._sharedCenter
+ _userCenter.onceToken
- +[MOLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:recordIdentifier:]
- +[MOSettingsStore createSettingsDirectoryAtURL:]
- +[MOSettingsStore createSettingsDirectoryAtURL:].cold.1
- +[MOSettingsStore directoryAttributes]
- +[MOSettingsStore directoryAttributes].cold.1
- +[MOSettingsStore fileAttributes]
- +[MOSettingsStore fileAttributes].cold.1
- +[MOSettingsStore saveSettings:toURL:]
- +[MOSettingsStore saveSettings:toURL:].cold.1
- +[MOSettingsStore saveSettings:toURL:].cold.2
- +[MOSettingsStore saveSettings:toURL:].cold.3
- +[MOSubscriptionCenter sharedCenter]
- +[MOSubscriptionCenter sharedCenter].cold.1
- -[MOBatchSettingsStore clearCurrentConnectionAndInvalidate:]
- -[MOBatchSettingsStore connectionLock]
- -[MOBatchSettingsStore container]
- -[MOBatchSettingsStore currentConnection]
- -[MOBatchSettingsStore dealloc]
- -[MOBatchSettingsStore fullReplacement]
- -[MOBatchSettingsStore getCurrentSettings]
- -[MOBatchSettingsStore getCurrentStoreProperties]
- -[MOBatchSettingsStore name]
- -[MOBatchSettingsStore persistableValueForSetting:inGroup:]
- -[MOBatchSettingsStore persistableValueForSettingKey:]
- -[MOBatchSettingsStore persistenceRecordIdentifier]
- -[MOBatchSettingsStore removePersistableValueForSetting:inGroup:]
- -[MOBatchSettingsStore removePersistableValueForSettingKey:]
- -[MOBatchSettingsStore removedSettings]
- -[MOBatchSettingsStore setContainer:]
- -[MOBatchSettingsStore setCurrentConnection:]
- -[MOBatchSettingsStore setFullReplacement:]
- -[MOBatchSettingsStore setName:]
- -[MOBatchSettingsStore setPersistableValue:forSetting:inGroup:]
- -[MOBatchSettingsStore setPersistableValue:forSettingKey:]
- -[MOBatchSettingsStore setPersistenceRecordIdentifier:]
- -[MOBatchSettingsStore setRemovedSettings:]
- -[MOBatchSettingsStore setUpdatedProperties:]
- -[MOBatchSettingsStore setUpdatedSettings:]
- -[MOBatchSettingsStore settingsLock]
- -[MOBatchSettingsStore settingsReader]
- -[MOBatchSettingsStore settingsWriter]
- -[MOBatchSettingsStore updatedProperties]
- -[MOBatchSettingsStore updatedSettings]
- -[MOBatchSettingsStore xpcConnection]
- -[MOEffectivePublisher initWithInterestedGroups:]
- -[MOEffectiveSettingsStore settingsReader]
- -[MOLocalSettingsStore clearCurrentConnectionAndInvalidate:]
- -[MOLocalSettingsStore connectionLock]
- -[MOLocalSettingsStore container]
- -[MOLocalSettingsStore currentConnection]
- -[MOLocalSettingsStore dealloc]
- -[MOLocalSettingsStore getStoreProperties]
- -[MOLocalSettingsStore name]
- -[MOLocalSettingsStore persistableValueForSetting:inGroup:]
- -[MOLocalSettingsStore persistableValueForSettingKey:]
- -[MOLocalSettingsStore persistenceRecordIdentifier]
- -[MOLocalSettingsStore removePersistableValueForSetting:inGroup:]
- -[MOLocalSettingsStore removePersistableValueForSettingKey:]
- -[MOLocalSettingsStore setContainer:]
- -[MOLocalSettingsStore setCurrentConnection:]
- -[MOLocalSettingsStore setName:]
- -[MOLocalSettingsStore setPersistableValue:forSetting:inGroup:]
- -[MOLocalSettingsStore setPersistableValue:forSettingKey:]
- -[MOLocalSettingsStore setPersistenceRecordIdentifier:]
- -[MOLocalSettingsStore settingsReader]
- -[MOLocalSettingsStore settingsWriter]
- -[MOLocalSettingsStore updateStoreProperties:]
- -[MOLocalSettingsStore xpcConnection]
- -[MOSettingsStore initStore]
- -[MOSubscriptionCenter init]
- GCC_except_table14
- GCC_except_table18
- GCC_except_table26
- GCC_except_table29
- GCC_except_table31
- GCC_except_table33
- GCC_except_table38
- _NSFileGroupOwnerAccountName
- _NSFileOwnerAccountName
- _NSFilePosixPermissions
- _OBJC_CLASS_$_NSFileManager
- _OBJC_IVAR_$_MOBatchSettingsStore._connectionLock
- _OBJC_IVAR_$_MOBatchSettingsStore._container
- _OBJC_IVAR_$_MOBatchSettingsStore._currentConnection
- _OBJC_IVAR_$_MOBatchSettingsStore._fullReplacement
- _OBJC_IVAR_$_MOBatchSettingsStore._name
- _OBJC_IVAR_$_MOBatchSettingsStore._persistenceRecordIdentifier
- _OBJC_IVAR_$_MOBatchSettingsStore._removedSettings
- _OBJC_IVAR_$_MOBatchSettingsStore._settingsLock
- _OBJC_IVAR_$_MOBatchSettingsStore._updatedProperties
- _OBJC_IVAR_$_MOBatchSettingsStore._updatedSettings
- _OBJC_IVAR_$_MOLocalSettingsStore._connectionLock
- _OBJC_IVAR_$_MOLocalSettingsStore._container
- _OBJC_IVAR_$_MOLocalSettingsStore._currentConnection
- _OBJC_IVAR_$_MOLocalSettingsStore._name
- _OBJC_IVAR_$_MOLocalSettingsStore._persistenceRecordIdentifier
- __OBJC_$_CLASS_METHODS_MOEffectiveSettingsStore
- __OBJC_$_CLASS_PROP_LIST_MOSettingsStore
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MOManagedSettingsAgent
- __OBJC_$_PROTOCOL_METHOD_TYPES_MOManagedSettingsAgent
- __OBJC_CLASS_PROTOCOLS_$_MOBatchSettingsStore
- __OBJC_CLASS_PROTOCOLS_$_MOLocalSettingsStore
- ___33+[MOSettingsStore fileAttributes]_block_invoke
- ___36+[MOSubscriptionCenter sharedCenter]_block_invoke
- ___37-[MOBatchSettingsStore commitChanges]_block_invoke
- ___37-[MOBatchSettingsStore commitChanges]_block_invoke.17
- ___37-[MOBatchSettingsStore commitChanges]_block_invoke.17.cold.1
- ___37-[MOBatchSettingsStore commitChanges]_block_invoke.cold.1
- ___37-[MOBatchSettingsStore xpcConnection]_block_invoke
- ___37-[MOBatchSettingsStore xpcConnection]_block_invoke_2
- ___37-[MOLocalSettingsStore xpcConnection]_block_invoke
- ___37-[MOLocalSettingsStore xpcConnection]_block_invoke_2
- ___38+[MOSettingsStore directoryAttributes]_block_invoke
- ___39-[MOSettingMetadata responsibleClients]_block_invoke.3
- ___39-[MOSettingMetadata responsibleClients]_block_invoke.3.cold.1
- ___40-[MOLocalSettingsStore clearAllSettings]_block_invoke
- ___40-[MOLocalSettingsStore clearAllSettings]_block_invoke.15
- ___40-[MOLocalSettingsStore clearAllSettings]_block_invoke.15.cold.1
- ___40-[MOLocalSettingsStore clearAllSettings]_block_invoke.cold.1
- ___42-[MOBatchSettingsStore getCurrentSettings]_block_invoke
- ___42-[MOBatchSettingsStore getCurrentSettings]_block_invoke.12
- ___42-[MOBatchSettingsStore getCurrentSettings]_block_invoke.12.cold.1
- ___42-[MOBatchSettingsStore getCurrentSettings]_block_invoke.12.cold.2
- ___42-[MOBatchSettingsStore getCurrentSettings]_block_invoke.cold.1
- ___42-[MOLocalSettingsStore getStoreProperties]_block_invoke
- ___42-[MOLocalSettingsStore getStoreProperties]_block_invoke.10
- ___42-[MOLocalSettingsStore getStoreProperties]_block_invoke.10.cold.1
- ___42-[MOLocalSettingsStore getStoreProperties]_block_invoke.10.cold.2
- ___42-[MOLocalSettingsStore getStoreProperties]_block_invoke.cold.1
- ___46-[MOLocalSettingsStore updateStoreProperties:]_block_invoke
- ___46-[MOLocalSettingsStore updateStoreProperties:]_block_invoke.13
- ___46-[MOLocalSettingsStore updateStoreProperties:]_block_invoke.13.cold.1
- ___46-[MOLocalSettingsStore updateStoreProperties:]_block_invoke.cold.1
- ___49+[MOLocalSettingsStore storesForSharedContainer:]_block_invoke
- ___49+[MOLocalSettingsStore storesForSharedContainer:]_block_invoke.20
- ___49+[MOLocalSettingsStore storesForSharedContainer:]_block_invoke.20.cold.1
- ___49+[MOLocalSettingsStore storesForSharedContainer:]_block_invoke.cold.1
- ___49-[MOBatchSettingsStore getCurrentStoreProperties]_block_invoke
- ___49-[MOBatchSettingsStore getCurrentStoreProperties]_block_invoke.9
- ___49-[MOBatchSettingsStore getCurrentStoreProperties]_block_invoke.9.cold.1
- ___49-[MOBatchSettingsStore getCurrentStoreProperties]_block_invoke.9.cold.2
- ___49-[MOBatchSettingsStore getCurrentStoreProperties]_block_invoke.cold.1
- ___49-[MOEffectivePublisher initWithInterestedGroups:]_block_invoke
- ___49-[MOEffectivePublisher initWithInterestedGroups:]_block_invoke_2
- ___54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke
- ___54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.23
- ___54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.23.cold.1
- ___54-[MOLocalSettingsStore persistableValueForSettingKey:]_block_invoke.cold.1
- ___58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke
- ___58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.24
- ___58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.24.cold.1
- ___58-[MOLocalSettingsStore setPersistableValue:forSettingKey:]_block_invoke.cold.1
- ___60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke
- ___60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.25
- ___60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.25.cold.1
- ___60-[MOLocalSettingsStore removePersistableValueForSettingKey:]_block_invoke.cold.1
- ___84+[MOLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:recordIdentifier:]_block_invoke
- ___84+[MOLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:recordIdentifier:]_block_invoke.18
- ___84+[MOLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:recordIdentifier:]_block_invoke.18.cold.1
- ___84+[MOLocalSettingsStore deleteStoresWithStoreNames:sharedContainer:recordIdentifier:]_block_invoke.cold.1
- ___block_descriptor_32_e16_v16?0"NSUUID"8l
- ___block_descriptor_40_e8_32s_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40r_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48s56s_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e46_v24?0"<MOManagedSettingsAgent>"8"NSError"16ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.49
- __os_log_default
- _directoryAttributes.directoryAttributes
- _directoryAttributes.onceToken
- _fileAttributes.directoryAttributes
- _fileAttributes.onceToken
- _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _objc_msgSend$dataWithPropertyList:format:options:error:
- _objc_msgSend$defaultManager
- _objc_msgSend$deleteStoresWithStoreNames:sharedContainer:recordIdentifier:
- _objc_msgSend$directoryAttributes
- _objc_msgSend$fileAttributes
- _objc_msgSend$init
- _objc_msgSend$initWithInterestedGroups:
- _objc_msgSend$numberWithShort:
- _objc_msgSend$path
- _objc_msgSend$setAttributes:ofItemAtPath:error:
- _objc_msgSend$sharedCenter
- _objc_msgSend$writeToFile:options:error:
- _sharedCenter._sharedCenter
- _sharedCenter.onceToken
CStrings:
+ "@\"MOAudioAccessorySettingsGroup\""
+ "@\"MOEyeReliefSettingsGroup\""
+ "@\"MOInternalBatchSettingsStore\""
+ "@\"MOInternalLocalSettingsStore\""
+ "@\"MOSystemAudioAccessorySettingsGroup\""
+ "@\"MOUnpairingTime\""
+ "@\"NSMutableArray\""
+ "@\"NSNumber\""
+ "@\"NSURL\"16@0:8"
+ "@\"NSXPCConnection\"16@0:8"
+ "@\"NSXPCConnection\"24@0:8@\"<MOManagedSettingsSubscriberProxy>\"16"
+ "@\"NSXPCInterface\"16@0:8"
+ "@24@0:8#16"
+ "@24@0:8^@16"
+ "@32@0:8q16@24"
+ "@48@0:8@16@24@?32#40"
+ "B16@?0@\"NSArray\"8"
+ "Collecting diagnostics"
+ "Error getting system group container for %{public}@: %llu"
+ "Getting current settings for store with container “%{public}@” and name “%{public}@”"
+ "Got system group container path from MCM for %{public}@: %{public}s"
+ "MOArraySettingMetadata"
+ "MOAudioAccessorySettingsGroup"
+ "MOAudioAccessoryTemporaryPairingConfiguration"
+ "MOBookmark"
+ "MOBookmarkSource"
+ "MOBookmarkSourceArraySettingMetadata"
+ "MODiagnosticsCollector"
+ "MOEyeReliefSettingsGroup"
+ "MOInternalBatchSettingsStore"
+ "MOInternalLocalSettingsStore"
+ "MOLocatable"
+ "MOManagedSettingsConnection"
+ "MOManagedSettingsProxy"
+ "MOManagedSettingsPublisherConnection"
+ "MOManagedSettingsSystemAgent"
+ "MOManagedSettingsSystemAgentConnection"
+ "MOManagedSettingsSystemAgentPublisherConnection"
+ "MOSystemAudioAccessorySettingsGroup"
+ "MOSystemBatchSettingsStore"
+ "MOSystemEffectiveSettingsStore"
+ "MOSystemLocalSettingsStore"
+ "MOSystemLocations"
+ "MOSystemSettingsStore"
+ "MOTemporaryPairingConfigurationSettingMetadata"
+ "MOUnpairingTime"
+ "MOWebNewPage"
+ "MOWebNewPageSettingMetadata"
+ "PersistenceInternal"
+ "Successfully collected diagnostics. URL: %@"
+ "T#,R,N,V_connectionClass"
+ "T@\"<MOSettingsReader>\",R,W,V_settingsReader"
+ "T@\"<MOSettingsWriter>\",R,W,V_settingsWriter"
+ "T@\"MOAudioAccessorySettingsGroup\",R,N,V_audioAccessory"
+ "T@\"MOAudioAccessoryTemporaryPairingConfiguration\",&,N"
+ "T@\"MOAudioAccessoryTemporaryPairingConfiguration\",R,N"
+ "T@\"MOBookmarkSourceArraySettingMetadata\",R,N"
+ "T@\"MOEyeReliefSettingsGroup\",R,N,V_eyeRelief"
+ "T@\"MOInternalBatchSettingsStore\",R,N,V_internalStore"
+ "T@\"MOInternalLocalSettingsStore\",R,N,V_internalStore"
+ "T@\"MOSystemAudioAccessorySettingsGroup\",R,N,V_audioAccessory"
+ "T@\"MOTemporaryPairingConfigurationSettingMetadata\",R,N"
+ "T@\"MOUnpairingTime\",R,V_unpairingTime"
+ "T@\"MOWebNewPage\",&,N"
+ "T@\"MOWebNewPage\",R,N"
+ "T@\"MOWebNewPageSettingMetadata\",R,N"
+ "T@\"NSArray\",&,N"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,V_children"
+ "T@\"NSMutableArray\",R,V_children"
+ "T@\"NSNumber\",R,V_hour"
+ "T@\"NSString\",R,V_bookmark"
+ "T@\"NSString\",R,V_extensionIdentifier"
+ "T@\"NSString\",R,V_homepageURL"
+ "T@\"NSString\",R,V_sourceIdentifier"
+ "T@\"NSString\",R,V_title"
+ "T@\"NSString\",R,V_url"
+ "T@?,R,N,V_sensitivityChecker"
+ "Tq,R,V_pageType"
+ "Unable to trigger diagnostics. Error: %{public}@"
+ "_audioAccessory"
+ "_bookmark"
+ "_children"
+ "_connectionClass"
+ "_extensionIdentifier"
+ "_eyeRelief"
+ "_homepageURL"
+ "_hour"
+ "_internalStore"
+ "_pageType"
+ "_sensitivityChecker"
+ "_sourceIdentifier"
+ "_unpairingTime"
+ "_url"
+ "arrayByAddingObjectsFromArray:"
+ "audioAccessory"
+ "bookmark"
+ "bookmarkSourceArrayFromPersistedArray:"
+ "children"
+ "collectDiagnosticsWithOneTimeConnection:outError:"
+ "collectDiagnosticsWithOutError:"
+ "collectDiagnosticsWithReplyHandler:"
+ "com.apple.ManagedConfiguration.ManagedSettingsExtension.system"
+ "com.apple.ManagedConfiguration.ManagedSettingsExtension.user"
+ "com.apple.ManagedSettings.system"
+ "com.apple.ManagedSettings.system.effective-settings.changed"
+ "com.apple.ManagedSettingsAgent.system"
+ "com.apple.ManagedSettingsAgent.system.publisher"
+ "connectionClass"
+ "deleteStoresWithStoreNames:sharedContainer:oneTimeConnection:"
+ "denyJavaScript"
+ "denyJavaScriptMetadata"
+ "denyMediaPurchase"
+ "denyMediaPurchaseMetadata"
+ "denyPopups"
+ "denyPopupsMetadata"
+ "denySummary"
+ "denySummaryMetadata"
+ "denyTemporaryPairing"
+ "denyTemporaryPairingMetadata"
+ "extensionIdentifier"
+ "extensionPageWithIdentifier:"
+ "eyeRelief"
+ "fileURLWithPath:"
+ "forceFraudWarning"
+ "forceFraudWarningMetadata"
+ "forceScreenDistanceOn"
+ "forceScreenDistanceOnMetadata"
+ "homepageURL"
+ "homepageWithURL:"
+ "hour"
+ "hourPolicyWithHour:"
+ "initWithConnectionClass:"
+ "initWithDomain:bookmark:"
+ "initWithInterestedGroups:subscriptionCenter:"
+ "initWithName:sharedContainer:sensitivityChecker:connectionClass:"
+ "initWithPageType:homepageURL:extensionIdentifier:"
+ "initWithPolicy:hour:"
+ "initWithSettingName:defaultArray:combineOperator:maximumCount:isPublic:scope:isPrivacySensitive:"
+ "initWithSettingName:defaultConfiguration:combineOperator:isPublic:scope:isPrivacySensitive:"
+ "initWithSettingName:defaultWebNewPage:combineOperator:isPublic:scope:isPrivacySensitive:"
+ "initWithSourceIdentifier:title:children:"
+ "initWithTitle:children:"
+ "initWithTitle:url:"
+ "initWithUnpairingTime:"
+ "intValue"
+ "internalStore"
+ "isDirectory"
+ "isEqualToArray:"
+ "isEqualToNumber:"
+ "managedBookmarks"
+ "managedBookmarksMetadata"
+ "newTabStartPage"
+ "newTabStartPageMetadata"
+ "pageType"
+ "persistableArrayFromBookmarkSourceArray:"
+ "reduceValues:intoExistingValues:"
+ "sensitivityChecker"
+ "setDenyJavaScript:"
+ "setDenyMediaPurchase:"
+ "setDenyPopups:"
+ "setDenySummary:"
+ "setDenyTemporaryPairing:"
+ "setForceFraudWarning:"
+ "setForceScreenDistanceOn:"
+ "setManagedBookmarks:"
+ "setNewTabStartPage:"
+ "setTemporaryPairingConfiguration:"
+ "sourceIdentifier"
+ "startPage"
+ "storesForSharedContainer:oneTimeConnection:"
+ "stringWithCString:encoding:"
+ "systemCenter"
+ "systemGroupContainerWithGroupIdentifier:"
+ "systemgroup.com.apple.managedsettings"
+ "temporaryPairingConfiguration"
+ "temporaryPairingConfigurationMetadata"
+ "unpairingTime"
+ "url"
+ "userCenter"
+ "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
+ "v24@?0@\"<MOBlameFinderProxy>\"8@\"NSError\"16"
+ "v24@?0@\"<MOEffectiveApplicationSettingsProxy>\"8@\"NSError\"16"
+ "v24@?0@\"<MOEffectiveShieldSettingsProxy>\"8@\"NSError\"16"
+ "v24@?0@\"<MOManagedSettingsProxy>\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "\xf0\xf0\""
- "B32@0:8@16@24"
- "Failed to create plist data. error: %{public}@"
- "Failed to set attributes of file at path: %{public}@ error: %{public}@"
- "Failed to write plist data to path: %{public}@ error: %{public}@"
- "Gettting current settings for store with container “%{public}@” and name “%{public}@”"
- "T@\"<MOSettingsReader>\",R,W"
- "T@\"<MOSettingsWriter>\",R,W"
- "Unable to create settings directory: %{public}@"
- "Writing plist data to path: %{public}@"
- "com.apple.ManagedConfiguration.ManagedSettingsExtension"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createSettingsDirectoryAtURL:"
- "dataWithPropertyList:format:options:error:"
- "defaultManager"
- "deleteStoresWithStoreNames:sharedContainer:recordIdentifier:"
- "directoryAttributes"
- "fileAttributes"
- "initStore"
- "initWithInterestedGroups:"
- "mobile"
- "numberWithShort:"
- "path"
- "saveSettings:toURL:"
- "setAttributes:ofItemAtPath:error:"
- "sharedCenter"
- "v24@?0@\"<MOManagedSettingsAgent>\"8@\"NSError\"16"
- "writeToFile:options:error:"

```
