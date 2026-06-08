## AssistantSettingsFoundation

> `/System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/AssistantSettingsFoundation`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x6da0
-  __TEXT.__auth_stubs: 0x3f0
+3600.49.31.1.6
+  __TEXT.__text: 0x67e0
   __TEXT.__objc_methlist: 0x638
   __TEXT.__const: 0x10e
-  __TEXT.__cstring: 0xa12
+  __TEXT.__cstring: 0xa32
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x44
   __TEXT.__dlopen_cstrs: 0x160

   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methname: 0x13dc
-  __TEXT.__objc_methtype: 0x18f
-  __TEXT.__objc_stubs: 0xe00
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x2e0
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x208
+  __DATA_CONST.__got: 0xb0
   __AUTH_CONST.__const: 0x138
-  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__cfstring: 0x960
   __AUTH_CONST.__objc_const: 0x978
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x60

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6987B900-677B-3FD7-B8BE-78A5FEDF144D
+  UUID: 624940FC-47AB-3EC1-8E71-92EA9F7504FE
   Functions: 196
-  Symbols:   705
-  CStrings:  414
+  Symbols:   711
+  CStrings:  185
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_AssistantSettingsFoundation
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[ASFApplicationSupplier applicationForBundleId:] : 176 -> 172
~ -[ASFApplication initWithBundleId:localizedName:] : 144 -> 152
~ -[ASFApplication compareByName:] : 120 -> 112
~ +[ASFAvailableSuggestionAppsController sharedController] : 312 -> 260
~ -[ASFAvailableSuggestionAppsController initWithApplicationSupplier:] : 108 -> 116
~ -[ASFAvailableSuggestionAppsController visibleApps] : 344 -> 336
~ -[ASFAvailableSuggestionAppsController visibleBundleIds] : 88 -> 84
~ +[ASFAssistantMetrics sharedMetrics] : 84 -> 68
~ +[ASFAssistantMetrics didVisit] : 76 -> 72
~ +[ASFAssistantMetrics didEnableSiriConfirmed:source:] : 120 -> 116
~ +[ASFAssistantMetrics didDisableSiriConfirmed:source:] : 120 -> 116
~ +[ASFAssistantMetrics didStartEnrollment:] : 92 -> 88
~ +[ASFAssistantMetrics didToggle:on:] : 120 -> 116
~ +[ASFAssistantMetrics didDetailVisit:] : 104 -> 100
~ -[ASFAssistantMetrics __onOffProperty] : 232 -> 216
~ _getPETEventPropertyClass : 220 -> 224
~ -[ASFAssistantMetrics __confirmedTrueFalseProperty] : 232 -> 216
~ -[ASFAssistantMetrics __toggleTrackerNameProperty] : 252 -> 236
~ -[ASFAssistantMetrics __detailToggleTrackerNameProperty] : 272 -> 256
~ -[ASFAssistantMetrics __siriSourceProperty] : 244 -> 228
~ -[ASFAssistantMetrics __foundInAppsProperty] : 272 -> 256
~ -[ASFAssistantMetrics __visitTracker] : 116 -> 108
~ _getPETScalarEventTrackerClass : 220 -> 224
~ -[ASFAssistantMetrics __enableSiriTracker] : 280 -> 260
~ -[ASFAssistantMetrics __disableSiriTracker] : 280 -> 260
~ -[ASFAssistantMetrics __toggleTracker] : 280 -> 260
~ -[ASFAssistantMetrics __startEnrollmentTracker] : 244 -> 228
~ -[ASFAssistantMetrics __detailVisitTracker] : 116 -> 108
~ -[ASFAssistantMetrics __detailVisitFoundInAppsTracker] : 244 -> 228
~ -[ASFAssistantMetrics __detailToggleFoundInAppsTracker] : 308 -> 284
~ -[ASFAssistantMetrics __detailToggleSearchTracker] : 244 -> 228
~ -[ASFAssistantMetrics __detailToggleSiriKitTracker] : 244 -> 228
~ _doAsync : 92 -> 88
~ ___31-[ASFAssistantMetrics logVisit]_block_invoke : 80 -> 76
~ -[ASFAssistantMetrics logEnableSiriConfirmed:source:] : 160 -> 152
~ ___53-[ASFAssistantMetrics logEnableSiriConfirmed:source:]_block_invoke : 240 -> 228
~ -[ASFAssistantMetrics logDisableSiriConfirmed:source:] : 160 -> 152
~ ___54-[ASFAssistantMetrics logDisableSiriConfirmed:source:]_block_invoke : 240 -> 228
~ ___42-[ASFAssistantMetrics logStartEnrollment:]_block_invoke : 188 -> 180
~ -[ASFAssistantMetrics logToggle:on:] : 160 -> 152
~ ___36-[ASFAssistantMetrics logToggle:on:]_block_invoke : 240 -> 228
~ ___38-[ASFAssistantMetrics logDetailVisit:]_block_invoke : 304 -> 288
~ -[ASFAssistantMetrics logDetailToggle:bundleId:on:] : 188 -> 200
~ ___51-[ASFAssistantMetrics logDetailToggle:bundleId:on:]_block_invoke : 424 -> 404
~ +[ASFAppClipsSuggestionsController sharedController] : 84 -> 68
~ -[ASFAppClipsSuggestionsController init] : 512 -> 504
~ -[ASFAppClipsSuggestionsController initWithDisabledSpotlightBundles:disabledSpotlightApps:] : 144 -> 152
~ +[ASFLockScreenSuggestionManager sharedInstance] : 84 -> 68
~ -[ASFLockScreenSuggestionManager disabledLockScreenBundles] : 228 -> 212
~ -[ASFLockScreenSuggestionManager _serializedBundles] : 140 -> 136
~ +[ASFSuggestionsController sharedController] : 84 -> 68
~ -[ASFSuggestionsController init] : 80 -> 76
~ -[ASFSuggestionsController initWithLockScreenSuggestionManager:] : 116 -> 124
~ -[ASFSuggestionsController _loadApps] : 580 -> 560
~ -[ASFSuggestionsController _loadDisabledShortcutsSet] : 104 -> 100
~ -[ASFSuggestionsController _loadDisabledSuggestAppsSet] : 104 -> 100
~ -[ASFSuggestionsController setSuggestionsNotificationsEnabled:bundleId:] : 160 -> 152
~ +[ASFController sharedController] : 312 -> 260
~ -[ASFController init] : 164 -> 156
~ -[ASFController assistantIsEnabled] : 60 -> 56
~ -[ASFController setAssistantIsEnabled:] : 184 -> 172
~ -[ASFController isVoiceTriggerEnabled] : 60 -> 56
~ -[ASFController alwaysShowRecognizedSpeech] : 208 -> 160
~ -[ASFController setAlwaysShowRecognizedSpeech:] : 216 -> 168
~ -[ASFController siriResponseShouldAlwaysPrint] : 208 -> 160
~ -[ASFController setSiriResponseShouldAlwaysPrint:] : 216 -> 168
~ -[ASFController useDeviceSpeakerForTTS] : 208 -> 160
~ -[ASFController setUseDeviceSpeakerForTTS:] : 216 -> 168
~ -[ASFController isCallHangUpEnabled] : 208 -> 160
~ -[ASFController setCallHangUpEnabled:] : 216 -> 168
~ -[ASFController isAnnounceNotificationEnabled] : 240 -> 188
~ -[ASFController setAnnounceNotificationEnabled:] : 272 -> 220
~ -[ASFController isSpokenNotificationSkipTriggerlessReplyConfirmationEnabled] : 208 -> 160
~ -[ASFController setSpokenNotificationSkipTriggerlessReplyConfirmationEnabled:] : 216 -> 168
~ -[ASFController isAnnounceNotificationEnabledForPlatform:] : 368 -> 308
~ -[ASFController setAnnounceNotificationEnabledForPlatform:annouceNotificationEnabled:] : 472 -> 412
~ -[ASFController getAllNotificationApps] : 536 -> 520
~ -[ASFController getAllNotificationAppIds] : 344 -> 336
~ -[ASFController isAnnounceNotificationEnabledForApp:] : 324 -> 264
~ -[ASFController setAnnounceNotificationEnabledForApp:annouceNotificationEnabled:] : 364 -> 304
~ -[ASFController siriSuggestionClients] : 500 -> 504
~ -[ASFController setLearningForApp:enabled:] : 248 -> 240
~ -[ASFController setShowSuggestionsInApp:enabled:] : 264 -> 252
~ sub_2478196ec -> sub_24e136284 : 152 -> 156
~ sub_247819784 -> sub_24e136320 : 160 -> 164
~ sub_247819824 -> sub_24e1363c4 : 108 -> 112
~ sub_247819994 -> sub_24e136538 : 152 -> 156
~ sub_247819a2c -> sub_24e1365d4 : 160 -> 164
~ sub_247819acc -> sub_24e136678 : 108 -> 112
CStrings:
+ "com.apple.Passbook"
- ".cxx_destruct"
- "@\"<ASFLockScreenSuggestionManaging>\""
- "@\"AFPreferences\""
- "@\"ASFApplicationSupplier\""
- "@\"NSMutableSet\""
- "@\"NSMutableSet\"16@0:8"
- "@\"NSString\""
- "@\"PETEventProperty\""
- "@\"PETScalarEventTracker\""
- "@\"VTPreferences\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "ASFAppClipsSuggestionsController"
- "ASFApplication"
- "ASFApplicationSupplier"
- "ASFAssistantMetrics"
- "ASFAvailableSuggestionAppsController"
- "ASFController"
- "ASFLockScreenSuggestionManager"
- "ASFLockScreenSuggestionManaging"
- "ASFSuggestionsController"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8q16"
- "T@\"<ASFNotificationSettingsCenter>\",R,N"
- "T@\"AFPreferences\",R,N,V_afPreferences"
- "T@\"ASFApplicationSupplier\",R,N,V_applicationSupplier"
- "T@\"NSString\",C,N,V_bundleId"
- "T@\"NSString\",C,N,V_localizedName"
- "T@\"VTPreferences\",R,N,V_voiceTriggerPreferences"
- "__confirmedTrueFalseProperty"
- "__detailToggleFoundInAppsTracker"
- "__detailToggleSearchTracker"
- "__detailToggleSiriKitTracker"
- "__detailToggleTrackerNameProperty"
- "__detailVisitFoundInAppsTracker"
- "__detailVisitTracker"
- "__disableSiriTracker"
- "__enableSiriTracker"
- "__foundInAppsProperty"
- "__loadDisabledShortcuts"
- "__loadDisabledSuggestApps"
- "__onOffProperty"
- "__siriSourceProperty"
- "__startEnrollmentTracker"
- "__toggleTracker"
- "__toggleTrackerNameProperty"
- "__visitTracker"
- "_afPreferences"
- "_allVisibleAppBundleIds"
- "_applicationSupplier"
- "_bundleId"
- "_confirmedTrueFalseProperty"
- "_detailToggleFoundInAppsTracker"
- "_detailToggleSearchTracker"
- "_detailToggleSiriKitTracker"
- "_detailToggleTrackerNameProperty"
- "_detailVisitFoundInAppsTracker"
- "_detailVisitTracker"
- "_disableSiriTracker"
- "_disabledLockScreenBundleIds"
- "_disabledLockScreenBundles"
- "_disabledSpotlightApps"
- "_disabledSpotlightBundles"
- "_disabledSpotlightShortcuts"
- "_disabledSuggestApps"
- "_enableSiriTracker"
- "_foundInAppsProperty"
- "_loadApps"
- "_loadDisabledShortcutsSet"
- "_loadDisabledSuggestAppsSet"
- "_localizedName"
- "_lockScreenSuggestionManager"
- "_onOffProperty"
- "_serializedBundles"
- "_siriSourceProperty"
- "_startEnrollmentTracker"
- "_synchronizeDisabledSpotlightApps"
- "_synchronizeLockScreenPreferences"
- "_toggleTracker"
- "_toggleTrackerNameProperty"
- "_visitTracker"
- "_voiceTriggerPreferences"
- "addObject:"
- "afPreferences"
- "allNotificationSources"
- "allObjects"
- "alwaysShowRecognizedSpeech"
- "announceNotificationsOnBuiltInSpeakerEnabled"
- "announceNotificationsOnHearingAidsEnabled"
- "announcementCarPlaySetting"
- "announcementHeadphonesSetting"
- "announcementSetting"
- "applicationForBundleId:"
- "applicationSupplier"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "assistantIsEnabled"
- "boolValue"
- "canUseVoiceTriggerDuringPhoneCall"
- "committedValue"
- "compare:"
- "compareByName:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentNotificationSettingsCenter"
- "description"
- "didDetailToggle:bundleId:on:"
- "didDetailVisit:"
- "didDisableSiriConfirmed:source:"
- "didEnableSiriConfirmed:source:"
- "didStartEnrollment:"
- "didToggle:on:"
- "didVisit"
- "disabledLockScreenBundles"
- "displayName"
- "getAllNotificationAppIds"
- "getAllNotificationApps"
- "hardwareButtonAssistantIsEnabled"
- "init"
- "initWithApplicationSupplier:"
- "initWithArray:"
- "initWithBundleId:localizedName:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithDisabledSpotlightBundles:disabledSpotlightApps:"
- "initWithFeatureId:event:registerProperties:"
- "initWithLockScreenSuggestionManager:"
- "initWithObjects:"
- "isAnnounceNotificationEnabled"
- "isAnnounceNotificationEnabledForApp:"
- "isAnnounceNotificationEnabledForPlatform:"
- "isCallHangUpEnabled"
- "isEqual:"
- "isEqualToString:"
- "isHiddenFromSettings"
- "isLearningEnabledForApp:"
- "isShowSuggestionsEnabledInApp:"
- "isSpokenNotificationSkipTriggerlessReplyConfirmationEnabled"
- "isValidValue:"
- "isVoiceTriggerEnabled"
- "learnFromAppClipsEnabled"
- "localizedName"
- "logDetailToggle:bundleId:on:"
- "logDetailVisit:"
- "logDisableSiriConfirmed:source:"
- "logEnableSiriConfirmed:source:"
- "logStartEnrollment:"
- "logToggle:on:"
- "logVisit"
- "mutableCopy"
- "notificationSettings"
- "notificationSettingsCenter"
- "notificationSourceWithIdentifier:"
- "notificationSystemSettings"
- "numberWithBool:"
- "propertyWithName:possibleValues:"
- "q16@0:8"
- "q24@0:8@16"
- "quickTypeGestureEnabled"
- "removeObject:"
- "replaceNotificationSettings:forNotificationSourceIdentifier:"
- "set"
- "setAlwaysShowRecognizedSpeech:"
- "setAnnounceNotificationEnabled:"
- "setAnnounceNotificationEnabledForApp:annouceNotificationEnabled:"
- "setAnnounceNotificationEnabledForPlatform:annouceNotificationEnabled:"
- "setAnnounceNotificationsOnBuiltInSpeakerEnabled:"
- "setAnnounceNotificationsOnHearingAidsEnabled:"
- "setAnnouncementHeadphonesSetting:"
- "setAnnouncementSetting:"
- "setAssistantIsEnabled:"
- "setBundleId:"
- "setCallHangUpEnabled:"
- "setCanUseVoiceTriggerDuringPhoneCall:"
- "setHardwareButtonAssistant:"
- "setLearnFromAppClipsEnabled:"
- "setLearningForApp:enabled:"
- "setLocalizedName:"
- "setLockScreenEnabled:bundleId:"
- "setNotificationSystemSettings:"
- "setQuickTypeGestureEnabled:"
- "setShowInSearchEnabled:"
- "setShowSuggestionsInApp:enabled:"
- "setSiriResponseShouldAlwaysPrint:"
- "setSpokenNotificationSkipTriggerlessReplyConfirmation:"
- "setSpokenNotificationSkipTriggerlessReplyConfirmationEnabled:"
- "setSuggestAppClipsEnabled:"
- "setSuggestionsNotificationsEnabled:bundleId:"
- "setSuggestionsShowOnHomeScreenEnabled:bundleId:"
- "setSuggestionsSuggestAppEnabled:bundleId:"
- "setTypeToSiriEnabled:"
- "setUseDeviceSpeakerForTTS:"
- "setWithArray:"
- "setWithCapacity:"
- "sharedController"
- "sharedInstance"
- "sharedMetrics"
- "sharedPreferences"
- "showInSearchEnabled"
- "siriResponseShouldAlwaysPrint"
- "siriSuggestionClients"
- "sourceIdentifier"
- "sourceSettings"
- "spokenNotificationSkipTriggerlessReplyConfirmation"
- "stringWithFormat:"
- "suggestAppClipsEnabled"
- "suggestionsNotificationEnabledForBundleId:"
- "suggestionsShowOnHomeScreenEnabledForBundleId:"
- "suggestionsSuggestAppEnabledForBundleId:"
- "synchronize"
- "trackEventWithPropertyValues:"
- "typeToSiriIsEnabled"
- "useDeviceSpeakerForTTS"
- "userPresentedValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v28@0:8B16@\"NSString\"20"
- "v28@0:8B16@20"
- "v28@0:8q16B24"
- "v36@0:8@16@24B32"
- "visibleApps"
- "visibleBundleIds"
- "voiceTriggerEnabled"
- "voiceTriggerPreferences"

```
