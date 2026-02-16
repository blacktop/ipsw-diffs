## FindMyDeviceUI

> `/System/Library/PrivateFrameworks/FindMyDeviceUI.framework/FindMyDeviceUI`

```diff

-142.32.10.4.1
-  __TEXT.__text: 0x4010
-  __TEXT.__auth_stubs: 0x340
+142.34.7.18.3
+  __TEXT.__text: 0x43e8
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x3c8
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x774
+  __TEXT.__cstring: 0x76e
   __TEXT.__oslogstring: 0x13a
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__unwind_info: 0x1e0
   __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x116b
+  __TEXT.__objc_methname: 0x119f
   __TEXT.__objc_methtype: 0xcf
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__objc_stubs: 0x1140
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x2f0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__objc_const: 0x400

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89A0DB7F-0C23-3DD7-94D3-F7C077FD8D90
+  UUID: 7BA60654-15F8-390B-B1ED-E0A3A10BB910
   Functions: 109
   Symbols:   528
-  CStrings:  329
+  CStrings:  332
 
Symbols:
+ _OBJC_CLASS_$_OBPrivacyLinkController
+ _objc_msgSend$flow
+ _objc_msgSend$linkWithBundleIdentifier:
+ _objc_msgSend$localizedButtonTitle
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[FMDUIFMIPiCloudSettingsViewController init] : 132 -> 136
~ -[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration] : 136 -> 140
~ ___70-[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration]_block_invoke : 200 -> 192
~ ___70-[FMDUIFMIPiCloudSettingsViewController _loadSearchPartyConfiguration]_block_invoke_2 : 268 -> 276
~ -[FMDUIFMIPiCloudSettingsViewController setSearchPartyConfigurationActive:] : 288 -> 284
~ ___75-[FMDUIFMIPiCloudSettingsViewController setSearchPartyConfigurationActive:]_block_invoke : 220 -> 224
~ -[FMDUIFMIPiCloudSettingsViewController viewDidLoad] : 204 -> 216
~ -[FMDUIFMIPiCloudSettingsViewController viewWillAppear:] : 148 -> 152
~ -[FMDUIFMIPiCloudSettingsViewController viewDidAppear:] : 192 -> 200
~ -[FMDUIFMIPiCloudSettingsViewController viewWillDisappear:] : 132 -> 136
~ -[FMDUIFMIPiCloudSettingsViewController isDTOEnabledAndFindMyOn] : 284 -> 292
~ -[FMDUIFMIPiCloudSettingsViewController isFMIPSwitchEnabled] : 316 -> 324
~ -[FMDUIFMIPiCloudSettingsViewController specifiers] : 416 -> 452
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForFMIP] : 316 -> 336
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForFMIP] : 960 -> 1028
~ -[FMDUIFMIPiCloudSettingsViewController addHyperLinkStyleToText:inString:action:forGroup:] : 296 -> 308
~ -[FMDUIFMIPiCloudSettingsViewController showLearnMoreLinkInDTODisclosure:] : 280 -> 292
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForOfflineFinding] : 220 -> 232
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForOfflineFinding] : 432 -> 464
~ -[FMDUIFMIPiCloudSettingsViewController _doesDeviceSupportOfflineFindingLowPowerMode] : 324 -> 336
~ -[FMDUIFMIPiCloudSettingsViewController showHSA2UpgradeAlert] : 660 -> 704
~ -[FMDUIFMIPiCloudSettingsViewController _specifierForSendLastLocation] : 220 -> 232
~ -[FMDUIFMIPiCloudSettingsViewController _groupSpecifierForSendLastLocation] : 220 -> 236
~ -[FMDUIFMIPiCloudSettingsViewController _showFMIPPrivacyPage] : 108 -> 112
~ -[FMDUIFMIPiCloudSettingsViewController _setFMIPSwitchOn:forSpecifier:] : 464 -> 484
~ -[FMDUIFMIPiCloudSettingsViewController _fmipSwitchOnForSpecifier:] : 172 -> 184
~ -[FMDUIFMIPiCloudSettingsViewController _offlineFindingSwitchOnForSpecifier:] : 116 -> 120
~ -[FMDUIFMIPiCloudSettingsViewController _showOfflineFindingAlertWhenTurningOff] : 720 -> 764
~ -[FMDUIFMIPiCloudSettingsViewController _setSendLastLocationSwitchOn:forSpecifier:] : 232 -> 236
~ ___83-[FMDUIFMIPiCloudSettingsViewController _setSendLastLocationSwitchOn:forSpecifier:]_block_invoke : 208 -> 212
~ -[FMDUIFMIPiCloudSettingsViewController _sendLastLocationSwitchOnForSpecifier:] : 124 -> 132
~ ___52-[FMDUIFMIPiCloudSettingsViewController _enableFMIP]_block_invoke_2 : 684 -> 740
~ ___52-[FMDUIFMIPiCloudSettingsViewController _enableFMIP]_block_invoke_3 : 112 -> 120
~ -[FMDUIFMIPiCloudSettingsViewController _disableFMIP] : 244 -> 248
~ ___53-[FMDUIFMIPiCloudSettingsViewController _disableFMIP]_block_invoke : 196 -> 192
~ ___53-[FMDUIFMIPiCloudSettingsViewController _disableFMIP]_block_invoke_2 : 156 -> 164
~ ___69-[FMDUIFMIPiCloudSettingsViewController _fmipSettingsCacheDidUpdate:]_block_invoke : 484 -> 512
~ -[FMDUIFMIPiCloudSettingsViewController _userAgentHeader] : 184 -> 200
~ -[FMDUIFMIPiCloudSettingsViewController _clientInfoHeader] : 536 -> 596
~ -[FMDUIFMIPiCloudSettingsViewController showActivityInProgress] : 180 -> 192
~ -[FMDUIFMIPiCloudSettingsViewController showActivityInProgressUIWithMessage:] : 304 -> 316
~ -[FMDUIFMIPiCloudSettingsViewController setAccount:] : 20 -> 80
~ -[FMDUIFMIPiCloudSettingsViewController setFmipSpecifier:] : 20 -> 80
~ -[FMDUIFMIPiCloudSettingsViewController setSendLastLocationSpecifier:] : 20 -> 80
~ -[FMDUIFMIPiCloudSettingsViewController setHud:] : 20 -> 80
~ -[FMDUIFMIPiCloudSettingsViewController setSpSession:] : 20 -> 80
~ +[FMDUIFMIPSettingsCache sharedInstance] : 68 -> 84
~ __fmipStateChangeNotificationReceived : 72 -> 76
~ __lowBatteryLocateStateChangeNotificationReceived : 72 -> 76
~ -[FMDUIFMIPSettingsCache _loadLowBatteryState] : 216 -> 220
~ ___46-[FMDUIFMIPSettingsCache _loadLowBatteryState]_block_invoke : 140 -> 144
~ -[FMDUIFMIPSettingsCache _loadFMIPState] : 216 -> 220
~ ___40-[FMDUIFMIPSettingsCache _loadFMIPState]_block_invoke : 140 -> 144
~ _LogCategory_Unspecified : 68 -> 84
CStrings:
+ "com.apple.onboarding.findmy"
+ "flow"
+ "linkWithBundleIdentifier:"
+ "localizedButtonTitle"
- "FMD_ABOUT_FMIP_PRIVACY_LINK_TITLE"

```
