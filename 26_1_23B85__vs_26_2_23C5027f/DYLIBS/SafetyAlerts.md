## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-64.0.26.0.0
-  __TEXT.__text: 0x6950
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x34c
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0xae8
-  __TEXT.__cstring: 0x984
-  __TEXT.__oslogstring: 0x1a8c
-  __TEXT.__unwind_info: 0x368
+64.0.36.0.0
+  __TEXT.__text: 0x7fac
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x3d4
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0xd04
+  __TEXT.__cstring: 0xd15
+  __TEXT.__oslogstring: 0x24e3
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methname: 0xbf8
+  __TEXT.__objc_methname: 0xdea
   __TEXT.__objc_methtype: 0x108
-  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__objc_stubs: 0xb20
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x2d8
-  __DATA.__objc_ivar: 0x24
+  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__objc_const: 0x368
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x88
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F02F5155-2BE7-3ABD-8351-0420BF6BF8D4
-  Functions: 95
-  Symbols:   476
-  CStrings:  381
+  UUID: 7D1AF8DB-4E0C-3B86-9D40-EAE2AC291A83
+  Functions: 109
+  Symbols:   549
+  CStrings:  465
 
Symbols:
+ -[SAEDFollowUpManager SAIsImprovedDeliveryStateEnabled]
+ -[SAEDFollowUpManager SAIsImprovedDeliveryVisible]
+ -[SAEDFollowUpManager newCFUShown]
+ -[SAEDFollowUpManager setNewCFUShown:]
+ -[SAEDFollowUpManager setSAIsImprovedDeliveryStateEnabled:]
+ -[SAEDFollowUpManager setSAIsImprovedDeliveryVisible:]
+ -[SAEDFollowUpManager settingsUpdate:isImprovedAlertStateEnabled:]
+ -[SafetyAlerts fetchSafetyAlertsSettingsSpecifiers:withReply:]
+ -[SafetyAlerts fetchSafetyAlertsSettingsSpecifiersSync]
+ -[SafetyAlerts onSettingsPageVisited]
+ -[SafetyAlerts setSafetyAlertsSettingsState:]
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ _OBJC_IVAR_$_SAEDFollowUpManager._SAIsImprovedDeliveryStateEnabled
+ _OBJC_IVAR_$_SAEDFollowUpManager._SAIsImprovedDeliveryVisible
+ _OBJC_IVAR_$_SAEDFollowUpManager._cfuPostInProgress
+ __CFXPCCreateCFObjectFromXPCObject
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.95
+ ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.50
+ ___58-[SafetyAlerts fetchAvailableAlertTypesOnQueue:withReply:]_block_invoke.68
+ ___62-[SafetyAlerts fetchSafetyAlertsSettingsSpecifiers:withReply:]_block_invoke
+ ___66-[SAEDFollowUpManager settingsUpdate:isImprovedAlertStateEnabled:]_block_invoke
+ ___66-[SAEDFollowUpManager settingsUpdate:isImprovedAlertStateEnabled:]_block_invoke_2
+ ___block_descriptor_42_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e19_"NSDictionary"8?0l
+ _kSAAboutPrivacy
+ _kSAAboutPrivacyDescription
+ _kSAAlwaysPlaySound
+ _kSAAlwaysPlaySoundDescription
+ _kSAEarthquakeAlert
+ _kSAEarthquakeAlertsDescription
+ _kSAEarthquakeAlertsDescriptionForWatch
+ _kSAEmptyScreen
+ _kSAEmptyScreenDescription
+ _kSAEnabledByDefault
+ _kSAImprovedAlertDelivery
+ _kSAImprovedAlertDeliveryDescription
+ _kSAOtherAlerts
+ _kSAOtherAlertsDescription
+ _kSAOtherAlertsDescriptionForWatch
+ _kSASafetyAlertsMainSwitchDescription
+ _kSASafetyAlertsMainSwitchName
+ _kSASwitchDescription
+ _kSASwitchHeading
+ _kSASwitchHeadingLabel
+ _kSASwitchLink
+ _kSASwitchName
+ _kSASwitchSupported
+ _kSAUserConfigurable
+ _objc_msgSend$SAIsImprovedDeliveryStateEnabled
+ _objc_msgSend$SAIsImprovedDeliveryVisible
+ _objc_msgSend$boolForDefaultsKey:defaultValue:
+ _objc_msgSend$newCFUShown
+ _objc_msgSend$onSettingsPageVisited
+ _objc_msgSend$setNewCFUShown:
+ _objc_msgSend$setSAIsImprovedDeliveryStateEnabled:
+ _objc_msgSend$setSAIsImprovedDeliveryVisible:
+ _xpc_dictionary_get_value
- GCC_except_table19
- GCC_except_table36
- GCC_except_table55
- GCC_except_table58
- ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.92
- ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.47
- ___58-[SafetyAlerts fetchAvailableAlertTypesOnQueue:withReply:]_block_invoke.32
- ___block_descriptor_56_e19_"NSDictionary"8?0l
- _objc_msgSend$_ctSuppressEDFollowUpReason
- _objc_msgSend$_shouldPostFollowUpForCTReason:
- _objc_msgSend$setCtSuppressEDFollowUpReason:
CStrings:
+ "AlwaysPlaySound"
+ "CriticalSafetyAlertsMain"
+ "Earthquake"
+ "EnabledByDefault"
+ "ImprovedAlertDelivery"
+ "OtherAlerts"
+ "SAFETY_ALERTS_ABOUT_PRIVACY"
+ "SAFETY_ALERTS_ALWAYS_PLAY_SOUND"
+ "SAFETY_ALERTS_ALWAYS_PLAY_SOUND_DESCRIPTION"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERT"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERTS_DESCRIPTION"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERTS_DESCRIPTION_FOR_WATCH"
+ "SAFETY_ALERTS_EMPTY_SCREEN"
+ "SAFETY_ALERTS_IMPROVED_ALERT_DELIVERY"
+ "SAFETY_ALERTS_IMPROVED_ALERT_DELIVERY_DESCRIPTION"
+ "SAFETY_ALERTS_MAIN_SWITCH_DESCRIPTION"
+ "SAFETY_ALERTS_MAIN_SWITCH_NAME"
+ "SAFETY_ALERTS_OTHER_ALERTS"
+ "SAFETY_ALERTS_OTHER_ALERTS_DESCRIPTION"
+ "SAFETY_ALERTS_OTHER_ALERTS_DESCRIPTION_FOR_WATCH"
+ "SAFETY_ALERTS_SWITCH_HEADING_LABEL"
+ "SAIsImprovedDeliveryStateEnabled"
+ "SAIsImprovedDeliveryVisible"
+ "SafetyAlertsSettingsDictionary"
+ "SwitchDescription"
+ "SwitchHeadingLabel"
+ "SwitchLink"
+ "SwitchName"
+ "SwitchSupported"
+ "TB,N,V_SAIsImprovedDeliveryStateEnabled"
+ "TB,N,V_SAIsImprovedDeliveryVisible"
+ "UserConfigurable"
+ "_SAIsImprovedDeliveryStateEnabled"
+ "_SAIsImprovedDeliveryVisible"
+ "_cfuPostInProgress"
+ "enhancedDelivery.followUp.newCFUShown"
+ "fetchSafetyAlertsSettingsSpecifiers:withReply:"
+ "fetchSafetyAlertsSettingsSpecifiersSync"
+ "newCFUShown"
+ "onSettingsPageVisited"
+ "prefs:root=NOTIFICATIONS_ID&path=com.apple.cmas.SafetyAlertsSettings"
+ "saGetSafetyAlertsSettingsSpecifiers"
+ "saSetSafetyAlertsSettingsSpecifiers"
+ "setNewCFUShown:"
+ "setSAIsImprovedDeliveryStateEnabled:"
+ "setSAIsImprovedDeliveryVisible:"
+ "setSafetyAlertsSettingsState:"
+ "settingsData"
+ "settingsPageVisited"
+ "settingsUpdate:isImprovedAlertStateEnabled:"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpStateAsync,!isIgneousEnabled,skipping\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpStateAsync,entry\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED\", \"shouldShowImprovedDelivery\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,posted,switchTurnedOn,retracting FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,switchAlreadyOn,markingCFUAsShown\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_isIgneousEnabled\", \"isIgneousEnabled\":%{public}hhd, \"SAIsImprovedDeliveryVisible\":%{public}hhd, \"SAIsImprovedDeliveryStateEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_postFollowUp,completion,switchTurnedOnDuringPost,ignoringResult\", \"success\":%{public}hhd, \"isEnabled\":%{public}hhd, \"newCFUShown\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_postFollowUp,switchNowOnOrAlreadyShown,skipping\", \"isEnabled\":%{public}hhd, \"newCFUShown\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,init\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,settingsUpdate,entry\", \"isImprovedAlertVisible\":%{public}hhd, \"isImprovedAlertStateEnabled\":%{public}hhd, \"oldVisible\":%{public}hhd, \"oldEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,settingsUpdate,noChangeSkippingEvaluation\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,settingsUpdate,stored\", \"visibilityChanged\":%{public}hhd, \"stateChanged\":%{public}hhd, \"newVisible\":%{public}hhd, \"newEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,settingsUpdate,switchNotVisible,skipping\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,settingsUpdate,triggeringEvaluation\"}"
+ "{\"msg%{public}.0s\":\"#saClient,SettingsPageVisited\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiers return\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiers sending response\", \"saSettingsSpecifiers\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiers sending response\", \"saSettingsSpecifiersDictionary\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiers sending response\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiersSync response received\", \"saSettingsSpecifiers\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiersSync sending response\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onEnhancedDeliveryPageVisited deprecated\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,#warning,setSafetyAlertsSettingsState,cantCreateMessage\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,#warning,settingsData,emptyInfo\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,settingsData\", \"eqState\":%{public, location:escape_only}@, \"alwaysPlaySoundState\":%{public, location:escape_only}@, \"otherAlertsState\":%{public, location:escape_only}@, \"improvedAlertDeliveryState\":%{public, location:escape_only}@, \"mainSafetyAlerts\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,settingsData\", \"settingsData\":%{private, location:escape_only}@}"
- "enhancedDeliveryPageVisited"
- "prefs:root=NOTIFICATIONS_ID&path=com.apple.cmas.EmergencyAlerts"
- "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState with !isIgneousEnabled\"}"
- "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED\", \"followUpState\":%{public}lu, \"ctSuppressEDFollowUpReason\":%{public}lu, \"saSuppressEDFollowUpReason\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#SAEDFollowUp,init,!isIgneousEnabled\"}"
- "{\"msg%{public}.0s\":\"#saClient,onEnhancedDeliveryPageVisited\"}"

```
