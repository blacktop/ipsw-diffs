## FindMyDeviceUI

> `/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI`

```diff

-142.35.2.23.2
-  __TEXT.__text: 0x43e8
-  __TEXT.__auth_stubs: 0x300
+145.30.2.1.1
+  __TEXT.__text: 0x3f28
   __TEXT.__objc_methlist: 0x3c8
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x76e
+  __TEXT.__cstring: 0x770
   __TEXT.__oslogstring: 0x13a
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x119f
-  __TEXT.__objc_methtype: 0xcf
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__objc_const: 0x400
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0BB4184A-746A-321D-96CF-0C75C71D6754
+  UUID: 66BAAFDB-3B9A-33FF-927D-912FCD254344
   Functions: 109
-  Symbols:   528
-  CStrings:  332
+  Symbols:   530
+  CStrings:  122
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[FMDUIFMIPiCloudSettingsViewController init] : 136 -> 132
~ -[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration] : 140 -> 136
~ ___70-[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration]_block_invoke : 192 -> 200
~ ___70-[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration]_block_invoke_2 : 276 -> 224
~ -[FMDUIFMIPiCloudSettingsViewController setSearchPartyConfigurationActive:] : 284 -> 288
~ ___75-[FMDUIFMIPiCloudSettingsViewController setSearchPartyConfigurationActive:]_block_invoke : 224 -> 176
~ -[FMDUIFMIPiCloudSettingsViewController viewDidLoad] : 216 -> 204
~ -[FMDUIFMIPiCloudSettingsViewController viewWillAppear:] : 152 -> 148
~ -[FMDUIFMIPiCloudSettingsViewController viewDidAppear:] : 200 -> 192
~ -[FMDUIFMIPiCloudSettingsViewController viewWillDisappear:] : 136 -> 132
~ -[FMDUIFMIPiCloudSettingsViewController isDTOEnabledAndFindMyOn] : 292 -> 240
~ -[FMDUIFMIPiCloudSettingsViewController isFMIPSwitchEnabled] : 324 -> 272
~ -[FMDUIFMIPiCloudSettingsViewController specifiers] : 452 -> 416
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForFMIP] : 336 -> 316
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForFMIP] : 1028 -> 952
~ -[FMDUIFMIPiCloudSettingsViewController addHyperLinkStyleToText:inString:action:forGroup:] : 308 -> 296
~ -[FMDUIFMIPiCloudSettingsViewController showLearnMoreLinkInDTODisclosure:] : 292 -> 236
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForOfflineFinding] : 232 -> 220
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForOfflineFinding] : 464 -> 432
~ -[FMDUIFMIPiCloudSettingsViewController _doesDeviceSupportOfflineFindingLowPowerMode] : 336 -> 280
~ -[FMDUIFMIPiCloudSettingsViewController showHSA2UpgradeAlert] : 704 -> 660
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForSendLastLocation] : 232 -> 220
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForSendLastLocation] : 236 -> 220
~ -[FMDUIFMIPiCloudSettingsViewController _showFMIPPrivacyPage] : 112 -> 108
~ -[FMDUIFMIPiCloudSettingsViewController _setFMIPSwitchOn:forSpecifier:] : 484 -> 464
~ -[FMDUIFMIPiCloudSettingsViewController _fmipSwitchOnForSpecifier:] : 184 -> 172
~ -[FMDUIFMIPiCloudSettingsViewController _offlineFindingSwitchOnForSpecifier:] : 120 -> 116
~ -[FMDUIFMIPiCloudSettingsViewController _showOfflineFindingAlertWhenTurningOff] : 764 -> 720
~ -[FMDUIFMIPiCloudSettingsViewController _setSendLastLocationSwitchOn:forSpecifier:] : 236 -> 232
~ ___83-[FMDUIFMIPiCloudSettingsViewController _setSendLastLocationSwitchOn:forSpecifier:]_block_invoke : 212 -> 208
~ -[FMDUIFMIPiCloudSettingsViewController _sendLastLocationSwitchOnForSpecifier:] : 132 -> 124
~ ___52-[FMDUIFMIPiCloudSettingsViewController _enableFMIP]_block_invoke_2 : 740 -> 684
~ ___52-[FMDUIFMIPiCloudSettingsViewController _enableFMIP]_block_invoke_3 : 120 -> 112
~ -[FMDUIFMIPiCloudSettingsViewController _disableFMIP] : 248 -> 244
~ ___53-[FMDUIFMIPiCloudSettingsViewController _disableFMIP]_block_invoke : 192 -> 196
~ ___53-[FMDUIFMIPiCloudSettingsViewController _disableFMIP]_block_invoke_2 : 164 -> 156
~ ___69-[FMDUIFMIPiCloudSettingsViewController _fmipSettingsCacheDidUpdate:]_block_invoke : 512 -> 484
~ -[FMDUIFMIPiCloudSettingsViewController _userAgentHeader] : 200 -> 184
~ -[FMDUIFMIPiCloudSettingsViewController _clientInfoHeader] : 596 -> 532
~ -[FMDUIFMIPiCloudSettingsViewController showActivityInProgress] : 192 -> 180
~ -[FMDUIFMIPiCloudSettingsViewController hideActivityInProgressUI] : 88 -> 96
~ -[FMDUIFMIPiCloudSettingsViewController hideActivityInProgressUIWithDelay:] : 140 -> 144
~ -[FMDUIFMIPiCloudSettingsViewController isShowingActivityInProgressUI] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController firstTimeSetup] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setFirstTimeSetup:] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController account] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setAccount:] : 80 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController fmipSpecifier] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setFmipSpecifier:] : 80 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController togglingFMIPSwitch] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setTogglingFMIPSwitch:] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController sendLastLocationSpecifier] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setSendLastLocationSpecifier:] : 80 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController hud] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setHud:] : 80 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController activityInProgress] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setActivityInProgress:] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController spSession] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setSpSession:] : 80 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController offlineFindingEnabled] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setOfflineFindingEnabled:] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController offlineFindingDisabledDueToNotHSA2] : 16 -> 20
~ -[FMDUIFMIPiCloudSettingsViewController setOfflineFindingDisabledDueToNotHSA2:] : 16 -> 20
~ +[FMDUIFMIPSettingsCache sharedInstance] : 84 -> 68
~ __fmipStateChangeNotificationReceived : 76 -> 72
~ __lowBatteryLocateStateChangeNotificationReceived : 76 -> 72
~ -[FMDUIFMIPSettingsCache _loadLowBatteryState] : 220 -> 216
~ ___46-[FMDUIFMIPSettingsCache _loadLowBatteryState]_block_invoke : 144 -> 140
~ -[FMDUIFMIPSettingsCache _loadFMIPState] : 220 -> 216
~ ___40-[FMDUIFMIPSettingsCache _loadFMIPState]_block_invoke : 144 -> 140
~ _LogCategory_Unspecified : 84 -> 68
~ -[FMDUIFMIPiCloudSettingsViewController addHyperLinkStyleToText:inString:action:forGroup:].cold.1 : 120 -> 76
CStrings:
- ".cxx_destruct"
- "@\"ACAccount\""
- "@\"NSObject<SPSettingsConfigurating>\""
- "@\"PSSpecifier\""
- "@\"UIProgressHUD\""
- "@16@0:8"
- "@24@0:8@16"
- "B"
- "B16@0:8"
- "FMDUIFMIPSettingsCache"
- "FMDUIFMIPiCloudSettingsViewController"
- "FMWLANEnabled"
- "Q"
- "Q16@0:8"
- "T@\"ACAccount\",&,N,V_account"
- "T@\"NSObject<SPSettingsConfigurating>\",&,N,V_spSession"
- "T@\"PSSpecifier\",&,N,V_fmipSpecifier"
- "T@\"PSSpecifier\",&,N,V_sendLastLocationSpecifier"
- "T@\"UIProgressHUD\",&,N,V_hud"
- "TB,N,V_activityInProgress"
- "TB,N,V_firstTimeSetup"
- "TB,N,V_fmipStateAvailable"
- "TB,N,V_lowBatteryLocateEnabled"
- "TB,N,V_lowBatteryLocateStateAvailable"
- "TB,N,V_offlineFindingDisabledDueToNotHSA2"
- "TB,N,V_offlineFindingEnabled"
- "TB,N,V_togglingFMIPSwitch"
- "TB,R,N"
- "TQ,N,V_fmipState"
- "URLWithString:"
- "_account"
- "_activityInProgress"
- "_clientInfoHeader"
- "_disableFMIP"
- "_doesDeviceSupportOfflineFindingLowPowerMode"
- "_enableFMIP"
- "_firstTimeSetup"
- "_fmipSettingsCacheDidUpdate:"
- "_fmipSpecifier"
- "_fmipState"
- "_fmipStateAvailable"
- "_fmipSwitchOnForSpecifier:"
- "_groupSpecifierForFMIP"
- "_groupSpecifierForOfflineFinding"
- "_groupSpecifierForSendLastLocation"
- "_hud"
- "_loadFMIPState"
- "_loadLowBatteryState"
- "_loadSearchPartyConfiguration"
- "_lowBatteryLocateEnabled"
- "_lowBatteryLocateStateAvailable"
- "_offlineFindingDisabledDueToNotHSA2"
- "_offlineFindingEnabled"
- "_offlineFindingSwitchOnForSpecifier:"
- "_reloadSpecifiersOnMainQueue"
- "_sendLastLocationSpecifier"
- "_sendLastLocationSwitchOnForSpecifier:"
- "_setFMIPSwitchOn:forSpecifier:"
- "_setOfflineFindingSwitchOn:forSpecifier:"
- "_setSendLastLocationSwitchOn:forSpecifier:"
- "_showOfflineFindingAlertWhenTurningOff"
- "_spSession"
- "_specifierForFMIP"
- "_specifierForOfflineFinding"
- "_specifierForSendLastLocation"
- "_togglingFMIPSwitch"
- "_userAgentHeader"
- "account"
- "actionWithTitle:style:handler:"
- "activityInProgress"
- "addAction:"
- "addFooterHyperlinkWithRange:target:action:"
- "addHyperLinkStyleToText:inString:action:forGroup:"
- "addObject:"
- "addObserver:selector:name:object:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allObjects"
- "beginIgnoringInteractionEvents"
- "beginRefreshingServiceStateWithBlock:"
- "boolValue"
- "buildVersion"
- "bundleForClass:"
- "bundleIdentifier"
- "containsObject:"
- "defaultCenter"
- "defaultWorkspace"
- "deviceClass"
- "disableInContext:withWipeToken:"
- "dismissViewControllerAnimated:completion:"
- "done"
- "enableInContext:"
- "endIgnoringInteractionEvents"
- "firstTimeSetup"
- "flow"
- "fmipEnabled"
- "fmipSpecifier"
- "fmipState"
- "fmipStateAvailable"
- "fmipStateChangeInProgress"
- "fmipStateWithCompletion:"
- "groupSpecifierWithID:"
- "hideActivityInProgress"
- "hideActivityInProgressUI"
- "hideActivityInProgressUIWithDelay:"
- "hud"
- "identifier"
- "infoDictionary"
- "init"
- "initWithNibName:bundle:"
- "initWithPresentingViewController:"
- "initWithRootViewController:"
- "isDTOEnabledAndFindMyOn"
- "isEqualToString:"
- "isFMIPSwitchEnabled"
- "isFeatureEnabled"
- "isShowingActivityInProgressUI"
- "linkWithBundleIdentifier:"
- "localizedButtonTitle"
- "localizedStringForKey:value:table:"
- "locationServicesEnabled"
- "lowBatteryLocateEnabled"
- "lowBatteryLocateEnabledWithCompletion:"
- "lowBatteryLocateStateAvailable"
- "mainBundle"
- "modelSpecificLocalizedStringKeyForKey:"
- "numberWithBool:"
- "objectForKey:"
- "offlineFindingDisabledDueToNotHSA2"
- "offlineFindingEnabled"
- "openSensitiveURL:withOptions:"
- "openSensitiveURL:withOptions:error:"
- "osName"
- "osVersion"
- "parentController"
- "performDeviceToDeviceEncryptionStateRepairForContext:withCompletion:"
- "performSelector:withObject:afterDelay:"
- "postNotificationName:object:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferencesURL"
- "present"
- "presentHSA2UpgradeForOfflineFinding"
- "presentViewController:animated:completion:"
- "presenterForPrivacySplashWithIdentifer:"
- "primaryAccountAltDSID"
- "productType"
- "productVersion"
- "propertyForKey:"
- "rangeOfString:"
- "reloadSpecifier:"
- "reloadSpecifierID:animated:"
- "reloadSpecifiers"
- "removeFromSuperview"
- "removeObserver:name:object:"
- "sendLastLocationSpecifier"
- "setAccount:"
- "setActivityInProgress:"
- "setAltDSID:"
- "setFirstTimeSetup:"
- "setFmipSpecifier:"
- "setFmipState:"
- "setFmipStateAvailable:"
- "setFontSize:"
- "setHud:"
- "setLowBatteryLocateEnabled:"
- "setLowBatteryLocateEnabled:withCompletion:"
- "setLowBatteryLocateStateAvailable:"
- "setOfflineFindingDisabledDueToNotHSA2:"
- "setOfflineFindingEnabled:"
- "setPreferredAction:"
- "setPresentingViewController:"
- "setProperty:forKey:"
- "setSearchPartyConfigurationActive:"
- "setSendLastLocationSpecifier:"
- "setServiceState:completion:"
- "setShouldEnable:"
- "setSpSession:"
- "setSpecifiers:"
- "setText:"
- "setTitle:"
- "setTogglingFMIPSwitch:"
- "settingsConfiguration"
- "sharedInstance"
- "shouldEnable"
- "showActivityInProgress"
- "showActivityInProgressUIWithMessage:"
- "showDisableAlertForAccount:presentingViewController:withCompletion:"
- "showEnableAlertWithCompletion:"
- "showHSA2UpgradeAlert"
- "showInView:"
- "showLearnMoreLinkInDTODisclosure:"
- "spSession"
- "specifier"
- "specifiers"
- "stringWithFormat:"
- "superview"
- "togglingFMIPSwitch"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@16@24"
- "v48@0:8@16@24:32@40"
- "valueWithNonretainedObject:"
- "viewDidAppear:"
- "viewDidLoad"
- "viewWillAppear:"
- "viewWillDisappear:"

```
