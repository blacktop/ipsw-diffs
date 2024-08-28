## AssistantSettingsFoundation

> `/System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/AssistantSettingsFoundation`

```diff

-3401.10.3.1.2
-  __TEXT.__text: 0x3600
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x2b8
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x5dc
-  __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__dlopen_cstrs: 0x68
+3401.16.2.1.1
+  __TEXT.__text: 0x5c84
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x618
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x9ec
+  __TEXT.__gcc_except_tab: 0x68
   __TEXT.__oslogstring: 0x44
-  __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methname: 0xb7b
-  __TEXT.__objc_methtype: 0xbf
-  __TEXT.__objc_stubs: 0x8a0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__dlopen_cstrs: 0x160
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methname: 0x13b1
+  __TEXT.__objc_methtype: 0x18e
+  __TEXT.__objc_stubs: 0xe00
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
-  __AUTH_CONST.__auth_got: 0x148
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x328
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x40
-  __DATA.__bss: 0x28
+  __DATA_CONST.__objc_selrefs: 0x500
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__objc_const: 0x968
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__data: 0x60
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
+  - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 75
-  Symbols:   135
-  CStrings:  190
+  Functions: 153
+  Symbols:   262
+  CStrings:  341
 
Symbols:
+ _OBJC_CLASS_$_ASFAppClipsSuggestionsController
+ _OBJC_CLASS_$_ASFApplication
+ _OBJC_CLASS_$_NSMutableSet
+ _CFPreferencesCopyAppValue
+ _SiriSettingsBundleDisabledKey
+ _SiriSettingsSharingDomain
+ _SiriSettingsShowInLookupEnabledKey
+ _CFPreferencesCopyValue
+ _OBJC_CLASS_$_NSString
+ _OBJC_METACLASS_$_ASFAvailableSuggestionAppsController
+ _OBJC_METACLASS_$_ASFApplicationSupplier
+ _objc_setProperty_nonatomic_copy
+ _CFNotificationCenterPostNotification
+ _dlerror
+ _SiriSettingsSharingPeopleSuggestionsPref
+ _OBJC_METACLASS_$_ASFLockScreenSuggestionManager
+ _notify_post
+ _SiriSettingsAppDisabledKey
+ _SiriSettingsSpotlightUIPrefsDomain
+ _SiriSettingsDuetExpertPrefsDomain
+ _SiriSettingsLockScreenDisabledKey
+ _objc_opt_new
+ _OBJC_METACLASS_$_ASFAppClipsSuggestionsController
+ _SiriSettingsDomainDisabledKey
+ _SiriSettingsSuggestAppDisabledKey
+ _kASFCSSpotlightPreferencesChangedNotification
+ _OBJC_CLASS_$_ASFApplicationSupplier
+ _OBJC_CLASS_$_ASFSuggestionsController
+ _OBJC_METACLASS_$_ASFApplication
+ _SiriSettingsShortcutsDisabledKey
+ _CFPreferencesSynchronize
+ _OBJC_CLASS_$_LSApplicationRecord
+ _objc_retain_x19
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _OBJC_CLASS_$_ASFLockScreenSuggestionManager
+ _OBJC_METACLASS_$_ASFSuggestionsController
+ _objc_msgSendSuper2
+ _OBJC_CLASS_$_NSSet
+ _kCFPreferencesCurrentUser
+ _dlsym
+ _kCFPreferencesAnyHost
+ _objc_opt_isKindOfClass
+ _CFPreferencesSetAppValue
+ _OBJC_CLASS_$_ASFAvailableSuggestionAppsController
+ _OBJC_CLASS_$_NSNumber
+ _objc_opt_class
- _objc_release_x26
CStrings:
+ "T@\"AFPreferences\",R,N,V_afPreferences"
+ "_bundleId"
+ "SuggestionsSuggestAppClips"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "visibleApps"
+ "_applicationSupplier"
+ "com.apple.Sharing"
+ "com.apple.spotlightui"
+ "__loadDisabledSuggestApps"
+ "setQuickTypeGestureEnabled:"
+ "setSuggestAppClipsEnabled:"
+ "setSuggestionsSuggestAppEnabled:bundleId:"
+ "appsearch"
+ "@\"NSMutableSet\""
+ "com.apple.duetexpertd"
+ "numberWithBool:"
+ "_lockScreenSuggestionManager"
+ "initWithArray:"
+ "SBSCopyDisplayIdentifiers"
+ "_localizedName"
+ "init"
+ "softlink:r:path:/System/Library/PrivateFrameworks/Search.framework/Search"
+ "LockscreenSuggestionsDisabledBundles"
+ "SPGetDisabledAppSet"
+ "setSuggestionsNotificationsEnabled:bundleId:"
+ "SBSearchDisabledShortcuts"
+ "com.apple.app-clips"
+ "typeToSiriIsEnabled"
+ "\x02"
+ "com.apple.suggestions"
+ "com.apple.store.Jolly"
+ "@32@0:8@16@24"
+ "com.apple.duetexpertd.prefschanged"
+ "q24@0:8@16"
+ "_serializedBundles"
+ "AppCanShowSiriSuggestionsBlacklist"
+ "SBSearchDisabledDomains"
+ "_loadApps"
+ "_synchronizeDisabledSpotlightApps"
+ "initWithApplicationSupplier:"
+ "initWithBundleId:localizedName:"
+ "quickTypeGestureEnabled"
+ "setTypeToSiriEnabled:"
+ "com.apple.suggestions.settingsChanged"
+ "isLearningEnabledForApp:"
+ "T@\"<ASFNotificationSettingsCenter>\",R,N"
+ "count"
+ "setWithCapacity:"
+ "SBSearchDisabledApps"
+ "_loadDisabledSuggestAppsSet"
+ "com.apple.iBooks"
+ "localizedName"
+ "setLearnFromAppClipsEnabled:"
+ "ASFApplication"
+ "boolValue"
+ "SBSearchDisabledBundles"
+ "_allVisibleAppBundleIds"
+ "setBundleId:"
+ "suggestionsNotificationEnabledForBundleId:"
+ "@\"NSMutableSet\"16@0:8"
+ "applicationSupplier"
+ "isShowSuggestionsEnabledInApp:"
+ "_disabledLockScreenBundles"
+ "compareByName:"
+ "containsObject:"
+ "initWithObjects:"
+ "suggestapp"
+ "_loadDisabledShortcutsSet"
+ "appinlockscreen"
+ "com.apple.iCloudDriveApp"
+ "sharedInstance"
+ "_disabledSpotlightApps"
+ "com.apple.Home"
+ "learnFromAppClipsEnabled"
+ "shortcutssearch"
+ "T@\"NSString\",C,N,V_localizedName"
+ "com.apple.DocumentsApp"
+ "com.apple.spotlightui.prefschanged"
+ "isEqual:"
+ "setShowSuggestionsInApp:enabled:"
+ "SiriCanLearnFromAppBlacklist"
+ "applicationForBundleId:"
+ "setWithArray:"
+ "\x03"
+ "ASFApplicationSupplier"
+ "__loadDisabledShortcuts"
+ "_disabledSpotlightBundles"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "set"
+ "setSuggestionsShowOnHomeScreenEnabled:bundleId:"
+ "SPGetDisabledBundleSet"
+ "com.apple.application"
+ "getAllNotificationAppIds"
+ "\x06"
+ "SharingPeopleSuggestionsDisabled"
+ "SuggestionsLearnFromAppClips"
+ "T@\"NSString\",C,N,V_bundleId"
+ "description"
+ "setShowInSearchEnabled:"
+ "compare:"
+ "ASFAppClipsSuggestionsController"
+ "T@\"ASFApplicationSupplier\",R,N,V_applicationSupplier"
+ "T@\"VTPreferences\",R,N,V_voiceTriggerPreferences"
+ "_afPreferences"
+ "_voiceTriggerPreferences"
+ "ASFLockScreenSuggestionManaging"
+ "afPreferences"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "suggestionsShowOnHomeScreenEnabledForBundleId:"
+ "setLearningForApp:enabled:"
+ "@\"<ASFLockScreenSuggestionManaging>\""
+ "@24@0:8@16"
+ "ASFLockScreenSuggestionManager"
+ "_disabledSuggestApps"
+ "voiceTriggerPreferences"
+ "@\"VTPreferences\""
+ "ASFAvailableSuggestionAppsController"
+ "disabledLockScreenBundles"
+ "setLockScreenEnabled:bundleId:"
+ "+[ASFAvailableSuggestionAppsController sharedController]"
+ "displayName"
+ "initWithLockScreenSuggestionManager:"
+ "showInSearchEnabled"
+ "suggestAppClipsEnabled"
+ "@\"AFPreferences\""
+ "allObjects"
+ "com.apple.reminders"
+ "initWithDisabledSpotlightBundles:disabledSpotlightApps:"
+ "siriSuggestionClients"
+ "stringWithFormat:"
+ "SBSearchSuggestAppDisabled"
+ "suggestionsSuggestAppEnabledForBundleId:"
+ "removeObject:"
+ "com.apple.tips"
+ "@\"NSString\""
+ "ASFApplication(bundleId:%!@(MISSING), localizedName:%!@(MISSING))"
+ "ASFSuggestionsController"
+ "com.apple.mobilesafari"
+ "visibleBundleIds"
+ "_disabledLockScreenBundleIds"
+ "com.apple.podcasts"
+ "notificationSettingsCenter"
+ "ShowInLookupEnabled"
+ "\x01"
+ "@\"ASFApplicationSupplier\""
+ "arrayWithArray:"
+ "_disabledSpotlightShortcuts"
+ "com.apple.mobilephone"
+ "setLocalizedName:"
+ "_synchronizeLockScreenPreferences"
+ "v28@0:8B16@\"NSString\"20"
- "array"

```
