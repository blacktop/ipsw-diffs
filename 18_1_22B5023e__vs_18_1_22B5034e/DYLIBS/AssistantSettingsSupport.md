## AssistantSettingsSupport

> `/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettingsSupport`

```diff

-3401.10.3.1.2
-  __TEXT.__text: 0x41234
-  __TEXT.__auth_stubs: 0x1720
+3401.16.2.1.1
+  __TEXT.__text: 0x40a3c
+  __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_methlist: 0x21a4
-  __TEXT.__const: 0xbd0
-  __TEXT.__gcc_except_tab: 0x76c
-  __TEXT.__cstring: 0x5dba
+  __TEXT.__const: 0xbe0
+  __TEXT.__gcc_except_tab: 0x708
+  __TEXT.__cstring: 0x5b7a
   __TEXT.__oslogstring: 0x13d1
   __TEXT.__ustring: 0x4
-  __TEXT.__dlopen_cstrs: 0x47a
-  __TEXT.__swift5_typeref: 0x8ce
+  __TEXT.__dlopen_cstrs: 0x382
+  __TEXT.__swift5_typeref: 0x8ea
   __TEXT.__swift5_fieldmd: 0x208
   __TEXT.__constg_swiftt: 0x55c
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_capture: 0x194
-  __TEXT.__unwind_info: 0x1138
-  __TEXT.__eh_frame: 0xa88
-  __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x7ef1
-  __TEXT.__objc_methtype: 0xc01
-  __TEXT.__objc_stubs: 0x5fa0
-  __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0xd78
+  __TEXT.__unwind_info: 0x1108
+  __TEXT.__eh_frame: 0xac8
+  __TEXT.__objc_classname: 0x68f
+  __TEXT.__objc_methname: 0x80e9
+  __TEXT.__objc_methtype: 0xcb2
+  __TEXT.__objc_stubs: 0x61c0
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0xcd0
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e88
+  __DATA_CONST.__objc_selrefs: 0x1f00
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xba0
-  __AUTH_CONST.__auth_ptr: 0x418
-  __AUTH_CONST.__const: 0xad8
-  __AUTH_CONST.__cfstring: 0x3cc0
-  __AUTH_CONST.__objc_const: 0x4700
+  __AUTH_CONST.__auth_got: 0xba8
+  __AUTH_CONST.__auth_ptr: 0x420
+  __AUTH_CONST.__const: 0xab8
+  __AUTH_CONST.__cfstring: 0x3a20
+  __AUTH_CONST.__objc_const: 0x4720
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x15e0
   __AUTH.__data: 0x140
-  __DATA.__objc_ivar: 0x2c0
-  __DATA.__data: 0xc50
-  __DATA.__bss: 0x1010
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__data: 0xc60
+  __DATA.__bss: 0xfc0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/AssistantSettingsFoundation.framework/AssistantSettingsFoundation
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1409
-  Symbols:   1406
+  Functions: 1392
+  Symbols:   1382
   CStrings:  2279
 
Symbols:
+ _OBJC_CLASS_$_ASFSuggestionsController
+ _swift_stdlib_isStackAllocationSafe
+ _OBJC_CLASS_$_ASFAvailableSuggestionAppsController
+ _OBJC_CLASS_$_ASFLockScreenSuggestionManager
+ _swift_deallocClassInstance
+ _OBJC_CLASS_$_ASFAppClipsSuggestionsController
+ _kASFCSSpotlightPreferencesChangedNotification
- _NSSelectorFromString
- _SiriSettingsLockScreenDisabledKey
- _SiriSettingsBundleDisabledKey
- _CFPreferencesCopyValue
- _SiriSettingsShortcutsDisabledKey
- _ASTDisabledLockScreenBundles
- _kASTCSSpotlightPreferencesChangedNotification
- _SiriSettingsDuetExpertPrefsDomain
- _SiriSettingsShowInLookupEnabledKey
- _SiriSettingsAppDisabledKey
- _ASTSetLockScreenEnabled
- _SiriSettingsSuggestAppDisabledKey
CStrings:
+ "QuickType"
+ "suggestionsShowOnHomeScreenEnabledForBundleId:"
+ "setShowInSearchEnabled:"
+ "_appSettingsBundleIDs"
+ "_isCurrentSpecifierQuickTypeGesture"
+ "setSuggestionsSuggestAppEnabled:bundleId:"
+ "@\"ASFAppClipsSuggestionsController\""
+ "ASSISTANT_APPS_SETTINGS_ID"
+ "shouldPromptForDisable"
+ "_availableSuggestionAppsController"
+ "@\"ASFSuggestionsController\""
+ "\x06"
+ "_suggestionsController"
+ "GM_NO_NETWORK_WARNING_TITLE"
+ "setLockScreenEnabled:bundleId:"
+ "@\"ASFAvailableSuggestionAppsController\""
+ "showNetworkUnavailableAlert"
+ "ASSISTANT_APP_CLIPS_SETTINGS_ID"
+ "suggestionsSuggestAppEnabledForBundleId:"
+ "GM_NO_NETWORK_WARNING_MESSAGE_IPAD"
+ "setSuggestAppClipsEnabled:"
+ "isNetworkAvailable"
+ "setLearnFromAppClipsEnabled:"
+ "v32@0:8@\"NSNumber\"16@\"PSConfirmationSpecifier\"24"
+ "visibleBundleIds"
+ "@24@0:8@\"PSSpecifier\"16"
+ "suggestAppClipsEnabled"
+ "showInSearchEnabled"
+ "GM_NO_NETWORK_WARNING_MESSAGE"
+ "GM_NO_NETWORK_OK"
+ "learnFromAppClipsEnabled"
+ "\x01\x13"
+ "suggestionsNotificationEnabledForBundleId:"
+ "sharedController"
+ "_appClipsSuggestionsController"
+ "disabledLockScreenBundles"
+ "setSuggestionsShowOnHomeScreenEnabled:bundleId:"
+ "setSuggestionsNotificationsEnabled:bundleId:"
- "SPGetDisabledAppSet"
- "_disabledSpotlightShortcuts"
- "\x05\x13"
- "com.apple.spotlightui"
- "com.apple.app-clips"
- "SBSearchDisabledDomains"
- "SBSearchDisabledShortcuts"
- "com.apple.DocumentsApp"
- "SBSearchDisabledApps"
- "SharingPeopleSuggestionsDisabled"
- "suggestapp"
- "NSMutableSet *PSSPGetDisabledAppSet(BOOL)"
- "SuggestionsSuggestAppClips"
- "appsearch"
- "ShowInLookupEnabled"
- "_saveSuggestionsSuggestAppEnabled:"
- "com.apple.iCloudDriveApp"
- "_saveSuggestionsSuggestionNotificationsEnabled:"
- "ACTIVATION_PHRASE_GROUP_TITLE"
- "SBSearchDisabledBundles"
- "_loadDisabledShortcutsSet"
- "SBSearchSuggestAppDisabled"
- "_loadDisabledSuggestAppsSet"
- "com.apple.Sharing"
- "SuggestionsLearnFromAppClips"
- "initWithArray:"
- "_saveSuggestionsShowOnHomeScreenEnabled:"
- "AssistantAppClipSettingsController.m"
- "com.apple.application"
- "com.apple.spotlightui.prefschanged"
- "LockscreenSuggestionsDisabledBundles"
- "com.apple.CloudDocs.MobileDocumentsFileProvider"
- "appinlockscreen"
- "com.apple.duetexpertd"
- "AssistantDetailController.m"
- "shortcutssearch"
- "_disabledSuggestApps"

```
