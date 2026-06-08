## Focus

> `/System/Library/PrivateFrameworks/Focus.framework/Focus`

```diff

-468.5.5.0.0
-  __TEXT.__text: 0x7be8
-  __TEXT.__auth_stubs: 0x3a0
+498.0.1.0.0
+  __TEXT.__text: 0x72f8
   __TEXT.__objc_methlist: 0x88c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x4c7
-  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__cstring: 0x4ce
+  __TEXT.__gcc_except_tab: 0x500
   __TEXT.__oslogstring: 0xc1d
-  __TEXT.__unwind_info: 0x378
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x1d80
-  __TEXT.__objc_methtype: 0x511
-  __TEXT.__objc_stubs: 0x1680
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x370
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x780
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0xb48
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x300
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/DoNotDisturbKit.framework/DoNotDisturbKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B384727-D58B-3B18-B8F6-E8787E4AB655
-  Functions: 195
-  Symbols:   820
-  CStrings:  471
+  UUID: 0725FB76-8A7D-351E-ABB3-66D62FFE7352
+  Functions: 194
+  Symbols:   821
+  CStrings:  110
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- GCC_except_table159
- _OUTLINED_FUNCTION_19
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
Functions:
~ __FocusUserDefaults : 84 -> 68
~ -[FCActivityManager _initWithIdentifier:] : 280 -> 272
~ +[FCActivityManager sharedActivityManager] : 84 -> 68
~ ___42+[FCActivityManager sharedActivityManager]_block_invoke : 144 -> 136
~ -[FCActivityManager availableActivities] : 196 -> 184
~ -[FCActivityManager activeActivity] : 80 -> 76
~ -[FCActivityManager defaultActivity] : 108 -> 104
~ -[FCActivityManager isDefaultConfiguration] : 136 -> 128
~ ___43-[FCActivityManager isDefaultConfiguration]_block_invoke : 196 -> 184
~ -[FCActivityManager localizedTerminationDescriptionForActiveActivity] : 648 -> 588
~ -[FCActivityManager setLifetimeDescriptionsUpdatingEnabled:] : 236 -> 232
~ -[FCActivityManager lifetimeOfActivity:] : 188 -> 172
~ -[FCActivityManager setActivity:active:withLifetime:reason:] : 304 -> 296
~ -[FCActivityManager isActivityLocalUserInitiated:] : 320 -> 300
~ -[FCActivityManager shouldActivityShowStatusPill:] : 356 -> 336
~ -[FCActivityManager promotedPlaceholderActivity:] : 184 -> 172
~ -[FCActivityManager suggestedActivityForLocation:] : 368 -> 336
~ -[FCActivityManager addObserver:] : 140 -> 132
~ -[FCActivityManager removeObserver:] : 140 -> 132
~ -[FCActivityManager modeSelectionService:didReceiveUpdatedActiveModeAssertion:stateUpdate:] : 352 -> 308
~ -[FCActivityManager modeSelectionService:didReceiveModesUpdate:] : 352 -> 304
~ -[FCActivityManager lifetimeDetailsProvider:didUpdateAvailableLifetimeDetails:] : 540 -> 536
~ -[FCActivityManager activitySuggestionClient:didSuggestConfiguredActivity:] : 240 -> 196
~ -[FCActivityManager didShowSuggestedActivity:location:] : 216 -> 196
~ -[FCActivityManager userDidSeeSuggestedActivity:location:] : 216 -> 196
~ -[FCActivityManager userDidAcceptSuggestedActivity:location:] : 216 -> 196
~ -[FCActivityManager userDidRejectSuggestedActivity:location:] : 216 -> 196
~ -[FCActivityManager _modeSelectionService] : 108 -> 96
~ -[FCActivityManager _lifetimeDetailsProvider] : 160 -> 148
~ -[FCActivityManager _stateService] : 108 -> 96
~ -[FCActivityManager _updateCreationDateOfActivity:] : 496 -> 436
~ -[FCActivityManager _updateActivitiesWithModes:] : 1608 -> 1564
~ ___48-[FCActivityManager _updateActivitiesWithModes:]_block_invoke : 108 -> 100
~ __FCSortRealizedAndPlaceholderActivities : 388 -> 392
~ -[FCActivityManager _availableActivities] : 368 -> 292
~ -[FCActivityManager _setAvailableActivities:] : 136 -> 124
~ -[FCActivityManager _invalidateActiveModeAssertion] : 92 -> 88
~ -[FCActivityManager _doesActivity:identifySameModeAsActivity:] : 164 -> 160
~ -[FCActivityManager _updateWithActiveModeAssertionIfNecessary:stateUpdate:] : 456 -> 396
~ -[FCActivityManager _updateActiveModeAssertionIfNecessary] : 324 -> 264
~ -[FCActivityManager _updateLifetimeForActiveActivity] : 576 -> 500
~ -[FCActivityManager _updateLifetimeForActiveActivityIfNecessary] : 120 -> 116
~ -[FCActivityManager _lifetimeForActiveActivity] : 72 -> 64
~ -[FCActivityManager _activityForATXActivityOrSuggestion:] : 348 -> 360
~ -[FCActivityManager _activityForModeIdentifier:] : 276 -> 264
~ ___48-[FCActivityManager _activityForModeIdentifier:]_block_invoke : 72 -> 68
~ -[FCActivityManager _activityForUniqueIdentifier:] : 268 -> 260
~ ___50-[FCActivityManager _activityForUniqueIdentifier:]_block_invoke : 72 -> 68
~ -[FCActivityManager _lifetimeForLifetimeDetailsIdentifier:ofActivity:] : 224 -> 216
~ ___70-[FCActivityManager _lifetimeForLifetimeDetailsIdentifier:ofActivity:]_block_invoke : 72 -> 68
~ -[FCActivityManager _updateActiveActivity:] : 436 -> 392
~ -[FCActivityManager _activeActivity] : 64 -> 56
~ -[FCActivityManager _setLifetimeForActiveActivity:] : 404 -> 360
~ -[FCActivityManager _setActiveActivity:withLifetime:reason:] : 1112 -> 1060
~ ___60-[FCActivityManager _setActiveActivity:withLifetime:reason:]_block_invoke : 624 -> 604
~ -[FCActivityManager _deactivateActivity:reason:] : 528 -> 476
~ -[FCActivityManager _updateActivity:withLifetimeDescriptions:] : 488 -> 444
~ -[FCActivityManager _updateActivity:withLifetimeDetails:] : 456 -> 440
~ -[FCActivityManager _updateActivity:withLifetimeDetailsCollection:] : 420 -> 428
~ -[FCActivityManager _updateLifetimesAlternativeDescription:forActivity:] : 356 -> 376
~ -[FCActivityManager _updateLifetimesAlternativeDescriptionForActivity:] : 356 -> 340
~ ___71-[FCActivityManager _updateLifetimesAlternativeDescriptionForActivity:]_block_invoke : 156 -> 152
~ -[FCActivityManager _updateLifetimesAlternativeDescriptionsForAvailableActivities] : 312 -> 308
~ -[FCActivityManager _isSyncedAssertion:] : 80 -> 72
~ -[FCActivityManager _activitySuggestionClient] : 116 -> 104
~ -[FCActivityManager _updateSuggestedActivity:forLocation:] : 740 -> 656
~ -[FCActivityManager _updateActivitySuggestion:] : 192 -> 188
~ -[FCActivityManager _localizedAutomaticDrivingTriggerDescriptionForPreference:] : 188 -> 180
~ -[FCActivityManager _drivingTriggerDidChange] : 320 -> 260
~ ___45-[FCActivityManager _drivingTriggerDidChange]_block_invoke : 84 -> 80
~ -[FCActivityManager _carDNDStatus] : 104 -> 96
~ -[FCActivityManager(Private) activityWithIdentifier:] : 420 -> 348
~ -[_FCActivity _setActivityCreationDate:] : 152 -> 148
~ -[_FCActivity _setActivityLifetimeDescriptions:] : 200 -> 196
~ -[_FCActivity _setActivityLifetimesAlternativeDescription:] : 172 -> 168
~ -[_FCActivity _updateMode:] : 112 -> 108
~ -[_FCActivity activityIdentifier] : 84 -> 76
~ -[_FCActivity activityUniqueIdentifier] : 84 -> 76
~ -[_FCActivity activityDisplayName] : 84 -> 76
~ -[_FCActivity activitySymbolImageName] : 84 -> 76
~ -[_FCActivity activityColorName] : 136 -> 120
~ -[_FCActivity activitySemanticType] : 60 -> 56
~ -[_FCActivity activityDetailText] : 204 -> 192
~ -[_FCActivity activitySettingsURL] : 84 -> 76
~ -[_FCActivity activitySetupURL] : 84 -> 76
~ -[_FCActivity isPlaceholder] : 60 -> 56
~ -[_FCActivity hash] : 60 -> 56
~ -[_FCActivity isEqual:] : 176 -> 180
~ -[_FCActivity description] : 204 -> 188
~ -[_FCActivity debugDescription] : 416 -> 380
~ -[_FCActivity copyWithZone:] : 168 -> 156
~ -[_FCActivityLifetime initWithLifetimeDetails:] : 108 -> 116
~ -[_FCActivityLifetime description] : 204 -> 188
~ -[FCActivityManager(DEPRECATED) setActiveActivity:reason:] : 152 -> 144
~ -[FCActivityManager(DEPRECATED) setActiveActivity:withLifetime:reason:] : 220 -> 208
~ -[FCActivityManager(DEPRECATED) promotePlaceholderActivity:] : 84 -> 80
~ ____FCSortActivities_block_invoke : 92 -> 88
~ _OUTLINED_FUNCTION_0 : 24 -> 32
~ _OUTLINED_FUNCTION_1 : 28 -> 20
~ _OUTLINED_FUNCTION_2 : 20 -> 44
~ _OUTLINED_FUNCTION_4 : 20 -> 32
~ _OUTLINED_FUNCTION_5 : 20 -> 12
~ _OUTLINED_FUNCTION_7 : 44 -> 12
~ _OUTLINED_FUNCTION_8 : 32 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 20
~ _OUTLINED_FUNCTION_11 : 12 -> 16
~ _OUTLINED_FUNCTION_12 : 16 -> 24
~ _OUTLINED_FUNCTION_13 : 16 -> 28
~ _OUTLINED_FUNCTION_14 : 20 -> 28
~ _OUTLINED_FUNCTION_15 : 32 -> 20
~ _OUTLINED_FUNCTION_16 : 24 -> 32
~ _OUTLINED_FUNCTION_17 : 16 -> 32
~ _OUTLINED_FUNCTION_18 : 20 -> 32
- _OUTLINED_FUNCTION_19
~ ___41-[FCActivityManager _initWithIdentifier:]_block_invoke.cold.1 : 136 -> 104
~ ___41-[FCActivityManager _initWithIdentifier:]_block_invoke.cold.2 : 136 -> 116
~ -[FCActivityManager setActivity:active:withLifetime:reason:].cold.1 : 128 -> 100
~ -[FCActivityManager _updateCreationDateOfActivity:].cold.1 : 136 -> 96
~ ___64-[FCActivityManager _notifyObserversOfAvailableActivitiesChange]_block_invoke.cold.1 : 188 -> 156
~ -[FCActivityManager(Private) activityWithIdentifier:].cold.1 : 64 -> 60
~ -[FCActivityManager _updateActiveModeAssertionIfNecessary].cold.1 : 64 -> 60
~ ___43-[FCActivityManager _updateActiveActivity:]_block_invoke_2.cold.1 : 188 -> 144
~ ___43-[FCActivityManager _updateActiveActivity:]_block_invoke.111.cold.1 : 188 -> 156
~ ___51-[FCActivityManager _setLifetimeForActiveActivity:]_block_invoke_2.cold.1 : 188 -> 144
~ -[FCActivityManager _setActiveActivity:withLifetime:reason:].cold.1 : 156 -> 96
~ ___60-[FCActivityManager _setActiveActivity:withLifetime:reason:]_block_invoke.cold.1 : 156 -> 124
~ -[FCActivityManager _deactivateActivity:reason:].cold.1 : 120 -> 96
~ -[FCActivityManager _deactivateActivity:reason:].cold.2 : 120 -> 96
~ -[FCActivityManager _deactivateActivity:reason:].cold.3 : 128 -> 100
~ ___65-[FCActivityManager _notifyObserversOfLifetimeChangeForActivity:]_block_invoke.cold.1 : 184 -> 140
~ -[FCActivityManager _updateActivity:withLifetimeDetailsCollection:].cold.1 : 128 -> 104
~ ___71-[FCActivityManager _updateLifetimesAlternativeDescriptionForActivity:]_block_invoke.cold.1 : 168 -> 160
~ ___58-[FCActivityManager _updateSuggestedActivity:forLocation:]_block_invoke_2.cold.1 : 144 -> 104
~ -[FCActivityManager _updateActivitySuggestion:].cold.1 : 120 -> 96
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<FCActivityDescribing>\""
- "@\"<FCActivityLifetimeDescribing>\""
- "@\"ATXActivitySuggestionClient\""
- "@\"CARAutomaticDNDStatus\""
- "@\"DNDLifetimeDetails\""
- "@\"DNDLifetimeDetailsProvider\""
- "@\"DNDMode\""
- "@\"DNDModeAssertion\""
- "@\"DNDModeSelectionService\""
- "@\"DNDStateService\""
- "@\"DNDStateUpdate\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ATXActivitySuggestionClientObserver"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "DEPRECATED"
- "DNDLifetimeDetailsProviderDelegate"
- "DNDModeSelectionServiceListener"
- "FCActivityDescribing"
- "FCActivityLifetimeDescribing"
- "FCActivityManager"
- "FCActivitySuggestionFeedbackAccepting"
- "NSCopying"
- "NSObject"
- "Private"
- "Q16@0:8"
- "T#,R"
- "T@\"<FCActivityDescribing>\",C,N,S_setDefaultActivity:,V_defaultActivity"
- "T@\"<FCActivityDescribing>\",R,C,N,V_activeActivity"
- "T@\"DNDLifetimeDetails\",R,C,N,G_dndLifetimeDetails,V_dndLifetimeDetails"
- "T@\"DNDMode\",C,G_dndMode,S_setDndMode:,V_dndMode"
- "T@\"NSArray\",C,N,S_setActivityLifetimeDescriptions:,V_activityLifetimeDescriptions"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_availableActivities"
- "T@\"NSDate\",C,N,S_setActivityCreationDate:,V_activityCreationDate"
- "T@\"NSDate\",R,C,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,S_setActivityLifetimesAlternativeDescription:,V_activityLifetimesAlternativeDescription"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSURL\",R,C,N"
- "T@\"NSUUID\",R,C,N"
- "TB,N,GisLifetimeDescriptionsUpdatingEnabled,V_lifetimeDescriptionsUpdatingEnabled"
- "TB,R,N"
- "TB,R,N,GisDefaultConfiguration"
- "TB,R,N,GisDrivingActivity"
- "TB,R,N,GisPlaceholder"
- "TB,R,N,GisSleepActivity"
- "TQ,R"
- "TQ,R,N"
- "Tq,R,N"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_FCActivity"
- "_FCActivityLifetime"
- "_activeActivity"
- "_activeLifetimeDetailsCollection"
- "_activeModeAssertion"
- "_activeModeAssertionIsValid"
- "_activeStateUpdate"
- "_activityCreationDate"
- "_activityForATXActivityOrSuggestion:"
- "_activityForModeIdentifier:"
- "_activityForUniqueIdentifier:"
- "_activityLifetimeDescriptions"
- "_activityLifetimesAlternativeDescription"
- "_activitySuggestionClient"
- "_allActivitiesByIdentifier"
- "_availableActivities"
- "_carDNDStatus"
- "_deactivateActivity:reason:"
- "_defaultActivity"
- "_dndLifetimeDetails"
- "_dndMode"
- "_doesActivity:identifySameModeAsActivity:"
- "_drivingTriggerDidChange"
- "_enumerateObserversRespondingToSelector:usingBlock:"
- "_identifier"
- "_initWithIdentifier:"
- "_invalidateActiveModeAssertion"
- "_isSyncedAssertion:"
- "_lifetimeDescriptionsUpdatingEnabled"
- "_lifetimeDetailsProvider"
- "_lifetimeForActiveActivity"
- "_lifetimeForLifetimeDetailsIdentifier:ofActivity:"
- "_lifetimeOfActiveActivity"
- "_localizedAutomaticDrivingTriggerDescriptionForPreference:"
- "_locationsToSuggestedActivitiesOrNull"
- "_modeSelectionService"
- "_notifyObserversOfAvailableActivitiesChange"
- "_notifyObserversOfLifetimeChangeForActivity:"
- "_observers"
- "_setActiveActivity:withLifetime:reason:"
- "_setActivityCreationDate:"
- "_setActivityLifetimeDescriptions:"
- "_setActivityLifetimesAlternativeDescription:"
- "_setAvailableActivities:"
- "_setDefaultActivity:"
- "_setDndMode:"
- "_setLifetimeForActiveActivity:"
- "_stateService"
- "_updateActiveActivity:"
- "_updateActiveModeAssertionIfNecessary"
- "_updateActivitiesWithModes:"
- "_updateActivity:withLifetimeDescriptions:"
- "_updateActivity:withLifetimeDetails:"
- "_updateActivity:withLifetimeDetailsCollection:"
- "_updateActivitySuggestion:"
- "_updateCreationDateOfActivity:"
- "_updateLifetimeForActiveActivity"
- "_updateLifetimeForActiveActivityIfNecessary"
- "_updateLifetimesAlternativeDescription:forActivity:"
- "_updateLifetimesAlternativeDescriptionForActivity:"
- "_updateLifetimesAlternativeDescriptionsForAvailableActivities"
- "_updateMode:"
- "_updateSuggestedActivity:forLocation:"
- "_updateSuggestedActivity:forLocations:"
- "_updateWithActiveModeAssertionIfNecessary:stateUpdate:"
- "activateModeWithDetails:error:"
- "activeActivity"
- "activeActivityDidChangeForManager:"
- "activeActivityLifetimeDidChangeForManager:"
- "activeModeAssertionWithError:"
- "activeModeDidChangeForManager:"
- "activitiesSettingsURL"
- "activityColorName"
- "activityCreationDate"
- "activityDetailText"
- "activityDisplayName"
- "activityIdentifier"
- "activityLifetimeDescriptions"
- "activityLifetimesAlternativeDescription"
- "activityManager:lifetimeDescriptionsDidChangeForActivity:"
- "activityManager:suggestedActivityDidChangeForLocation:"
- "activitySemanticType"
- "activitySettingsURL"
- "activitySetupURL"
- "activitySuggestionClient:didSuggestActivity:"
- "activitySuggestionClient:didSuggestConfiguredActivity:"
- "activitySuggestionClient:didSuggestSettingUpActivity:"
- "activitySuggestionClient:didSuggestTriggersForConfiguredActivity:"
- "activitySymbolImageName"
- "activityUniqueIdentifier"
- "activityWithIdentifier:"
- "addListener:withCompletionHandler:"
- "addObject:"
- "addObserver:"
- "allModesWithError:"
- "allObjects"
- "allValues"
- "autorelease"
- "availableActivities"
- "availableActivitiesDidChangeForManager:"
- "bs_firstObjectPassingTest:"
- "bundleForClass:"
- "bundleIdentifier"
- "class"
- "compare:"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "created"
- "currentCalendar"
- "currentSuggestion"
- "dealloc"
- "debugDescription"
- "defaultActivity"
- "defaultConfiguration"
- "defaultTintColorName"
- "description"
- "details"
- "deviceIdentifier"
- "didShowConfiguredActivitySuggestionWithSuggestionUUID:location:"
- "didShowSuggestedActivity:location:"
- "distantFuture"
- "dndLifetimeDetails"
- "dndMode"
- "dnd_defaultSettingsURL"
- "drivingActivity"
- "fetchAutomaticDNDTriggerPreferenceWithReply:"
- "formatDateAsAbbreviatedDayMonthWithTimeStyle:"
- "formatDateAsTimeStyle:"
- "hash"
- "hashTableWithOptions:"
- "identifier"
- "indexOfObjectPassingTest:"
- "init"
- "initWithArray:copyItems:"
- "initWithLifetimeDetails:"
- "initWithMode:"
- "initWithSuiteName:"
- "initWithUUIDString:"
- "initialize"
- "insertString:atIndex:"
- "integerValue"
- "invalidateModeAssertionWithUUID:error:"
- "isActivityLocalUserInitiated:"
- "isDateInToday:"
- "isDateInTomorrow:"
- "isDefaultConfiguration"
- "isDrivingActivity"
- "isEqual:"
- "isEqualToDate:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLifetimeDescriptionsUpdatingEnabled"
- "isMemberOfClass:"
- "isPlaceholder"
- "isProxy"
- "isSleepActivity"
- "length"
- "lifetimeDescriptionsUpdatingEnabled"
- "lifetimeDetailsForAssertionDetails:error:"
- "lifetimeDetailsProvider:didUpdateAvailableLifetimeDetails:"
- "lifetimeForLifetimeDetails:error:"
- "lifetimeIdentifier"
- "lifetimeMetadata"
- "lifetimeName"
- "lifetimeOfActivity:"
- "lifetimeUntilEndOfScheduleWithIdentifier:"
- "localizedStringForKey:value:table:"
- "localizedTerminationDescriptionForActiveActivity"
- "location"
- "mainBundle"
- "maxUIAddableModes"
- "maximumActivityCountForUserInterface"
- "metadata"
- "mode"
- "modeConfigurationForModeIdentifier:error:"
- "modeIdentifier"
- "modeSelectionService:didReceiveAvailableModesUpdate:"
- "modeSelectionService:didReceiveModesUpdate:"
- "modeSelectionService:didReceiveUpdatedActiveModeAssertion:stateUpdate:"
- "modeUUID"
- "mutableCopy"
- "name"
- "newActivityManager"
- "newActivityManagerWithIdentifier:"
- "null"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "options"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "placeholder"
- "promotePlaceholderActivity:"
- "promotePlaceholderWithModeIdentifier:error:"
- "promotedPlaceholderActivity:"
- "promotedPlaceholderWithModeIdentifier:error:"
- "q16@0:8"
- "queryCurrentStateWithError:"
- "rangeOfString:options:"
- "reason"
- "registerObserver:sendingInitialChangeNotification:"
- "release"
- "removeObject:"
- "removeObserver:"
- "resetLifetimeDetails"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "semanticType"
- "serviceForClientIdentifier:"
- "setActiveActivity:"
- "setActiveActivity:reason:"
- "setActiveActivity:withLifetime:reason:"
- "setActivity:active:reason:"
- "setActivity:active:withLifetime:reason:"
- "setDelegate:"
- "setIdentifier:"
- "setLifetime:"
- "setLifetimeDescriptionsUpdatingEnabled:"
- "setModeIdentifier:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setReason:"
- "settingsURL"
- "setupURL"
- "sharedActivityManager"
- "sharedInstance"
- "shouldActivityShowStatusPill:"
- "sleepActivity"
- "sortUsingFunction:context:"
- "source"
- "startUpdatingLifetimeDetailMetadata"
- "startUpdatingLifetimeDetails"
- "state"
- "stopUpdatingLifetimeDetailMetadata"
- "stopUpdatingLifetimeDetails"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "suggestedActivityFeedbackReceiver"
- "suggestedActivityForLocation:"
- "superclass"
- "supportsDiscreteLifetimes"
- "symbolImageName"
- "tintColorName"
- "userDidAcceptConfiguredActivitySuggestionWithSuggestionUUID:location:"
- "userDidAcceptSuggestedActivity:location:"
- "userDidRejectConfiguredActivitySuggestionWithSuggestionUUID:location:"
- "userDidRejectSuggestedActivity:location:"
- "userDidSeeConfiguredActivitySuggestionWithSuggestionUUID:location:"
- "userDidSeeSuggestedActivity:location:"
- "userVisibleTransitionDate"
- "userVisibleTransitionLifetimeType"
- "uuidString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v32@0:8:16@?24"
- "v32@0:8@\"<FCActivityDescribing>\"16q24"
- "v32@0:8@\"ATXActivitySuggestionClient\"16@\"ATXActivity\"24"
- "v32@0:8@\"ATXActivitySuggestionClient\"16@\"ATXActivitySetUpSuggestion\"24"
- "v32@0:8@\"ATXActivitySuggestionClient\"16@\"ATXActivitySuggestion\"24"
- "v32@0:8@\"ATXActivitySuggestionClient\"16@\"ATXActivityTriggerSuggestion\"24"
- "v32@0:8@\"DNDLifetimeDetailsProvider\"16@\"NSArray\"24"
- "v32@0:8@\"DNDModeSelectionService\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v36@0:8@16B24@28"
- "v40@0:8@\"DNDModeSelectionService\"16@\"DNDModeAssertion\"24@\"DNDStateUpdate\"32"
- "v40@0:8@16@24@32"
- "v44@0:8@16B24@28@36"
- "visibility"
- "zone"

```
