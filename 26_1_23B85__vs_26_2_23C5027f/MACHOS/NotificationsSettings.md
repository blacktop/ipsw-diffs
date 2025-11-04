## NotificationsSettings

> `/System/Library/PreferenceBundles/NotificationsSettings.bundle/NotificationsSettings`

```diff

-270.1.10.0.0
-  __TEXT.__text: 0x30734
+270.2.5.0.0
+  __TEXT.__text: 0x33a14
   __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_stubs: 0x5800
-  __TEXT.__objc_methlist: 0x2144
-  __TEXT.__const: 0x794
+  __TEXT.__objc_stubs: 0x5b60
+  __TEXT.__objc_methlist: 0x22a4
+  __TEXT.__const: 0x7b4
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__objc_methname: 0x7267
-  __TEXT.__cstring: 0x30b6
-  __TEXT.__objc_classname: 0x6b5
-  __TEXT.__objc_methtype: 0xdd5
-  __TEXT.__oslogstring: 0x232
+  __TEXT.__objc_methname: 0x76d4
+  __TEXT.__cstring: 0x35f6
+  __TEXT.__objc_classname: 0x6e0
+  __TEXT.__objc_methtype: 0xdf1
+  __TEXT.__oslogstring: 0x972
   __TEXT.__swift5_typeref: 0x5d2
-  __TEXT.__swift5_reflstr: 0x277
+  __TEXT.__swift5_reflstr: 0x287
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__constg_swiftt: 0x220
-  __TEXT.__swift5_fieldmd: 0x1d8
+  __TEXT.__swift5_fieldmd: 0x1e4
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x13c
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0xc88
+  __TEXT.__unwind_info: 0xcc8
   __TEXT.__eh_frame: 0x318
   __DATA_CONST.__auth_got: 0x8d8
-  __DATA_CONST.__got: 0x620
+  __DATA_CONST.__got: 0x670
   __DATA_CONST.__auth_ptr: 0x188
-  __DATA_CONST.__const: 0x1330
-  __DATA_CONST.__cfstring: 0x2d60
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0x1390
+  __DATA_CONST.__cfstring: 0x3000
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x1b0
-  __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA.__objc_const: 0x53f8
-  __DATA.__objc_selrefs: 0x1c58
-  __DATA.__objc_ivar: 0x17c
-  __DATA.__objc_data: 0x8a8
+  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_arrayobj: 0x120
+  __DATA.__objc_const: 0x5558
+  __DATA.__objc_selrefs: 0x1d68
+  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_data: 0x8f8
   __DATA.__data: 0xae8
-  __DATA.__bss: 0x870
-  __DATA.__common: 0x438
+  __DATA.__bss: 0x880
+  __DATA.__common: 0x440
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
+  - /System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts
   - /System/Library/PrivateFrameworks/ScreenContinuityServices.framework/ScreenContinuityServices
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CD01F27E-6857-30CB-8A26-E063546C96EB
-  Functions: 1109
-  Symbols:   463
-  CStrings:  2041
+  UUID: 7B13777D-D2C4-33CB-84F8-31AEBC07056E
+  Functions: 1138
+  Symbols:   475
+  CStrings:  2191
 
Symbols:
+ _NCLogSafetyAlerts
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_SafetyAlerts
+ _OBJC_CLASS_$_SafetyAlertsSwitchExtension
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_CLASS_$_UITextView
+ _OBJC_METACLASS_$_SafetyAlertsSwitchExtension
+ _UIRoundToViewScale
+ ___NSDictionary0__struct
+ _kSAEnabledByDefault
+ _kSASwitchDescription
+ _kSASwitchHeading
+ _kSASwitchLink
+ _kSASwitchName
+ _kSASwitchSupported
+ _kSAUserConfigurable
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_UIScreen
- _OBJC_CLASS_$_UITraitCollection
- _UIRoundToScreenScale
CStrings:
+ "%@%@"
+ "%s, Added footer with hyperlink: %@ -> %@"
+ "%s, Added footer without link: %@"
+ "%s, Added privacy footer text without link: %@"
+ "%s, Added privacy hyperlink footer with name: %@ and URL: %@"
+ "%s, Alert type %@ not supported, skipping"
+ "%s, Could not find Learn More range, using plain text: %@"
+ "%s, Creating grouped specifier for %@ (supported: %@, enabled: %@, configurable: %@)"
+ "%s, Creating individual specifier for %@ (supported: %@, enabled: %@, configurable: %@)"
+ "%s, Creating spinner specifiers"
+ "%s, Found setting for %@: %@"
+ "%s, Invalid Privacy URL format: %@"
+ "%s, Invalid URL format: %@"
+ "%s, Main switch i.e. %s not supported, do not show Critical Safety Alerts switch"
+ "%s, No Privacy URL found, falling back to custom page"
+ "%s, No Safety Alerts dict, returning default: %@"
+ "%s, No Safety Alerts dictionary found"
+ "%s, No URL found for Learn More link"
+ "%s, No critical safety alerts available, showing None placeholder with name: %@"
+ "%s, No enabled key for %@, returning default: %@"
+ "%s, No safety alerts settings available"
+ "%s, No settings data, returning default: %@"
+ "%s, No settings for %@, returning default: %@"
+ "%s, No settings found for alert type: %@"
+ "%s, Opening Learn More URL: %@"
+ "%s, Opening Privacy URL: %@"
+ "%s, Opening Privacy page"
+ "%s, Received settings from SafetyAlerts: %@"
+ "%s, Safety Alerts main entry not found, skipping specifier"
+ "%s, Safety Alerts settings not available, skipping specifier"
+ "%s, Sending to SafetyAlerts: %@"
+ "%s, Starting async fetch"
+ "%s, Starting sync fetch"
+ "%s, User toggled %@ to %@"
+ "%s, creating switch specifiers"
+ "%s, init called"
+ "%s, nil specifiers"
+ "%s, readUserSettingsFromUserDefaults"
+ "%s, readUserSettingsFromUserDefaults no settings found"
+ "%s, readUserSettingsFromUserDefaults: %@"
+ "%s, safetyAlertValue for %@"
+ "%s, setSafetyAlertState called"
+ "%s, showing spinner while loading"
+ "%s, specifiers called"
+ "%s, sync fetch completed"
+ "%s, viewDidAppear called"
+ "-[BulletinBoardController(SafetyAlerts) _addSafetyAlertsSettingsToSpecifiers:]"
+ "-[BulletinBoardController(SafetyAlerts) readUserSettingsFromUserDefaults]"
+ "-[SafetyAlertsSwitchExtension _createSpinnerSpecifiers]"
+ "-[SafetyAlertsSwitchExtension _createSwitchSpecifiers]"
+ "-[SafetyAlertsSwitchExtension _fetchSafetyAlertsSettingsAsync]"
+ "-[SafetyAlertsSwitchExtension _fetchSafetyAlertsSettingsAsync]_block_invoke"
+ "-[SafetyAlertsSwitchExtension _fetchSafetyAlertsSettingsSync]"
+ "-[SafetyAlertsSwitchExtension init]"
+ "-[SafetyAlertsSwitchExtension openPrivacyPage:]"
+ "-[SafetyAlertsSwitchExtension openPrivacyURL:]"
+ "-[SafetyAlertsSwitchExtension openSafetyAlertsLearnMoreURL:]"
+ "-[SafetyAlertsSwitchExtension safetyAlertValue:]"
+ "-[SafetyAlertsSwitchExtension setSafetyAlertState:forSpecifier:]"
+ "-[SafetyAlertsSwitchExtension specifiers]"
+ "-[SafetyAlertsSwitchExtension viewDidAppear:]"
+ "@24@0:8q16"
+ "@52@0:8@16@24B32#36@44"
+ "AboutPrivacy"
+ "AlertType"
+ "AlwaysPlaySound"
+ "CriticalSafetyAlertsMain"
+ "Earthquake"
+ "EmptyScreenSwitch"
+ "ImprovedAlertDelivery"
+ "NO"
+ "OtherAlerts"
+ "SAFETY_ALERTS_ABOUT_PRIVACY"
+ "SAFETY_ALERTS_EMPTY_SCREEN_SWITCH_NONE"
+ "SAFETY_ALERTS_LEARN_MORE"
+ "SAFETY_ALERTS_PRIVACY_PAGE_TEXT"
+ "Safety Alerts"
+ "SafetyAlerts"
+ "SafetyAlertsSettings"
+ "SafetyAlertsSettingsDictionary"
+ "SafetyAlertsSwitchExtension"
+ "T@\"NSMutableDictionary\",&,N,V_safetyAlertsSettings"
+ "T@\"NSString\",&,N,V_learnMoreURL"
+ "T@\"NSString\",&,N,V_privacyURL"
+ "TB,N,V_loadingSafetyAlerts"
+ "YES"
+ "_addSafetyAlertsSettingsToSpecifiers:"
+ "_createDeepMutableCopy:"
+ "_createSpinnerSpecifiers"
+ "_createSwitchSpecifiers"
+ "_fetchSafetyAlertsSettingsAsync"
+ "_fetchSafetyAlertsSettingsSync"
+ "_getBoolValueForAlertType:"
+ "_learnMoreURL"
+ "_loadingSafetyAlerts"
+ "_privacyURL"
+ "_safetyAlertsSettings"
+ "_scaledImageForImage:traitCollection:"
+ "com.apple.cmas.SafetyAlertsSettings"
+ "com.apple.cmas.SafetyAlertsSettings.Cleared"
+ "com.apple.safetyalerts"
+ "d32@0:8d16@24"
+ "dismissPrivacyPage:"
+ "fetchSafetyAlertsSettingsSpecifiers:withReply:"
+ "fetchSafetyAlertsSettingsSpecifiersSync"
+ "getDictionaryDefaultsForKey:"
+ "getMicaFileURLForIdiom:"
+ "getNoneValue:"
+ "initWithSuiteName:"
+ "learnMoreURL"
+ "loadingSafetyAlerts"
+ "nc_settingsIconImageForTraitCollection:"
+ "notificationListDisplayStyleSelectionImageForType:traitCollection:"
+ "openPrivacyPage:"
+ "openPrivacyURL:"
+ "openSafetyAlertsLearnMoreURL:"
+ "openURL:options:completionHandler:"
+ "preferredHeightInWidth:forView:"
+ "privacyURL"
+ "readUserSettingsFromUserDefaults"
+ "safetyAlertValue:"
+ "safetyAlertsSettings"
+ "setAutoresizingMask:"
+ "setEditable:"
+ "setLearnMoreURL:"
+ "setLoadingSafetyAlerts:"
+ "setObject:forKeyedSubscript:"
+ "setPrivacyURL:"
+ "setSafetyAlertState:forSpecifier:"
+ "setSafetyAlertsSettings:"
+ "setSafetyAlertsSettingsState:"
+ "setTextContainerInset:"
+ "sharedApplication"
+ "sharedInterface"
+ "spokenNotificationsSpecifierNamed:sectionInfo:showIcon:class:traitCollection:"
+ "stringValue"
+ "systemGroupedBackgroundColor"
+ "v16@?0@\"NSDictionary\"8"
- "@44@0:8@16@24B32#36"
- "_scaledImageForImage:"
- "currentTraitCollection"
- "emulatedArtworkSubtype"
- "getMicaFileURL"
- "isEmulatedDevice"
- "mainScreen"
- "nc_settingsIconImage"
- "notificationListDisplayStyleSelectionImageForType:"
- "spokenNotificationsSpecifierNamed:sectionInfo:showIcon:class:"

```
