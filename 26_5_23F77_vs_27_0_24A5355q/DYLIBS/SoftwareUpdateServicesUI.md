## SoftwareUpdateServicesUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI`

```diff

-251.120.2.0.0
-  __TEXT.__text: 0x992c
-  __TEXT.__auth_stubs: 0x2d0
+300.0.0.0.0
+  __TEXT.__text: 0x94f4
   __TEXT.__objc_methlist: 0xb18
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1166
-  __TEXT.__oslogstring: 0x39c
-  __TEXT.__gcc_except_tab: 0xd8
+  __TEXT.__cstring: 0x12e2
+  __TEXT.__oslogstring: 0x3b7
+  __TEXT.__gcc_except_tab: 0x50
   __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x2a9
-  __TEXT.__objc_methname: 0x1df6
-  __TEXT.__objc_methtype: 0x4b8
-  __TEXT.__objc_stubs: 0x15a0
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x2248
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x24a8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x888
+  __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x15c0
+  __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x1aa0
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x2b0
+  __DATA.__data: 0x2b8
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC832DB7-E801-3382-8949-023BE9F9A348
+  UUID: FF1E328D-0267-3816-A504-0230752922A4
   Functions: 222
-  Symbols:   1992
-  CStrings:  819
+  Symbols:   2068
+  CStrings:  433
 
Symbols:
+ -[SUSUIDefaults .cxx_destruct]
+ -[SUSUIDefaults _bindAndRegisterDefaults]
+ -[SUSUIDefaults _clearLegacySpringBoardPreferences]
+ -[SUSUIDefaults _initWithLegacyDefaults:]
+ -[SUSUIDefaults _migrateLegacySpringBoardPreferences]
+ -[SUSUIDefaults clearDeveloperInstallBrickAlerts]
+ -[SUSUIDefaults init]
+ -[SUSUIDefaults migrateAndClearLegacyPreferences]
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_INTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_CARRIER
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_INTERNAL
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_KEY
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_PATH_KEY
+ _MKBUnlockDeviceWithACM
+ _OBJC_CLASS_$_SUSUIDefaults
+ _OBJC_IVAR_$_SUSUIDefaults._sbLegacyDefaults
+ _OBJC_METACLASS_$_SUSUIDefaults
+ __OBJC_$_INSTANCE_METHODS_SUSUIDefaults
+ __OBJC_$_INSTANCE_VARIABLES_SUSUIDefaults
+ __OBJC_$_PROP_LIST_SUSUIDefaults
+ __OBJC_CLASS_RO_$_SUSUIDefaults
+ __OBJC_METACLASS_RO_$_SUSUIDefaults
+ ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.358
+ _kCBPowerMitigationAmbrosia
+ _kCBPowerMitigationEcoMode
+ _kCBPowerMitigationLevel
+ _kCBPowerMitigationNone
+ _kCoreBrightnessDisplayAliasIDs
+ _kCoreBrightnessDisplayDeviceIDs
+ _kCoreBrightnessDisplayInfo
+ _kCoreBrightnessDisplayInfoDeviceID
+ _kCoreBrightnessDisplayInfoDisplayBuiltIn
+ _kCoreBrightnessDisplayInfoDisplayFramebuffer
+ _kCoreBrightnessDisplayInfoDisplayID
+ _kCoreBrightnessDisplayInfoDisplayName
+ _kCoreBrightnessDisplayInfoDisplayUUID
+ _kCoreBrightnessDisplayList
+ _objc_msgSend$externalizedContext
- -[SUSUISoftwareUpdateDefaults .cxx_destruct]
- -[SUSUISoftwareUpdateDefaults _bindAndRegisterDefaults]
- -[SUSUISoftwareUpdateDefaults _clearLegacySpringBoardPreferences]
- -[SUSUISoftwareUpdateDefaults _initWithLegacyDefaults:]
- -[SUSUISoftwareUpdateDefaults _migrateLegacySpringBoardPreferences]
- -[SUSUISoftwareUpdateDefaults clearDeveloperInstallBrickAlerts]
- -[SUSUISoftwareUpdateDefaults init]
- -[SUSUISoftwareUpdateDefaults migrateAndClearLegacyPreferences]
- _MKBUnlockDevice
- _OBJC_CLASS_$_SUSUISoftwareUpdateDefaults
- _OBJC_IVAR_$_SUSUISoftwareUpdateDefaults._sbLegacyDefaults
- _OBJC_METACLASS_$_SUSUISoftwareUpdateDefaults
- __OBJC_$_INSTANCE_METHODS_SUSUISoftwareUpdateDefaults
- __OBJC_$_INSTANCE_VARIABLES_SUSUISoftwareUpdateDefaults
- __OBJC_$_PROP_LIST_SUSUISoftwareUpdateDefaults
- __OBJC_CLASS_RO_$_SUSUISoftwareUpdateDefaults
- __OBJC_METACLASS_RO_$_SUSUISoftwareUpdateDefaults
- ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke.337
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ -[SUKeybagInterface(SUSUIAuthenticationKeybagInterface) authenticate:] : 132 -> 288
~ -[SUKeybagInterface(SUSUIAuthenticationKeybagInterface) backOffTime] -> ___os_log_helper_16_0_1_4_0 : 200 -> 56
~ +[SUSUIAuthenticationInterface sharedInstance] -> -[SUKeybagInterface(SUSUIAuthenticationKeybagInterface) backOffTime] : 144 -> 200
~ ___46+[SUSUIAuthenticationInterface sharedInstance]_block_invoke -> +[SUSUIAuthenticationInterface sharedInstance] : 80 -> 144
~ -[SUSUIAuthenticationInterface init] -> ___46+[SUSUIAuthenticationInterface sharedInstance]_block_invoke : 168 -> 80
~ -[SUSUIAuthenticationInterface initWithKeybag:] -> -[SUSUIAuthenticationInterface init] : 496 -> 168
~ ___os_log_helper_16_0_1_4_0 -> -[SUSUIAuthenticationInterface initWithKeybag:] : 56 -> 448
~ -[SUSUIAuthenticationInterface isBlocked] : 488 -> 432
~ -[SUSUIAuthenticationInterface _setPasscodeLocked:] : 284 -> 236
~ ___144-[SUSUIAuthenticationAlertAction initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:]_block_invoke : 392 -> 344
~ ___114-[SUSUIAuthenticationAlertAction initWithRollbackDescriptor:canDeferInstallation:completionQueue:completionBlock:]_block_invoke : 392 -> 344
~ -[SUSUICommandLineToolClient URLForType:] : 460 -> 404
~ -[SUSUICommandLineToolClient _connectToServerIfNecessary] : 1472 -> 1172
~ ___57-[SUSUICommandLineToolClient _connectToServerIfNecessary]_block_invoke_2 : 268 -> 220
~ -[SUSUICommandLineToolClient _noteConnectionDropped] : 216 -> 168
~ -[SUSUIControllerClient getPasscodePolicy:] : 656 -> 608
~ ___43-[SUSUIControllerClient getPasscodePolicy:]_block_invoke : 272 -> 224
~ -[SUSUIControllerClient _connectToServerIfNecessary] : 1472 -> 1176
~ ___52-[SUSUIControllerClient _connectToServerIfNecessary]_block_invoke_2 : 268 -> 220
~ -[SUSUIControllerClient _noteConnectionDropped] : 216 -> 168
~ ___65-[SUSUILaggardsUIAlertAction initWithDescriptor:completionBlock:]_block_invoke : 444 -> 396
CStrings:
+ "220d35fc-bc97-422e-8c96-7ea2785548a1"
+ "55b4b4f0-0ecd-4a85-a72f-3e5e6feeac4d"
+ "5f33eae7-f1e0-4811-9713-07dd879f16d5"
+ "63efd5fa-738b-4560-913f-49a55bc873f4"
+ "71b10ce9-15df-40be-bfca-49113fff8fcc"
+ "Ambrosia"
+ "CBDisplayAliasIDs"
+ "CBDisplayDeviceIDs"
+ "CBDisplayInfo"
+ "CBDisplayInfoDeviceID"
+ "CBDisplayInfoDisplayID"
+ "CBDisplayList"
+ "EcoMode"
+ "MKBUnlockDeviceWithACM: %d"
+ "None"
+ "PowerMitigationLevel"
+ "SUSUIOSVersion"
+ "SUSUIState"
+ "b9e3c9f6-a252-481e-a9ab-0bd3beeae429"
+ "builtIn"
+ "c1b5ebc2-72ff-44a5-a761-50502d26fc66"
+ "demo-external"
+ "demo-internal"
+ "fc098402-04dd-45c5-86f8-50e36d846af1"
+ "framebuffer"
+ "name"
+ "sandboxExtensionShortTermLocksKey"
+ "sandboxExtensionShortTermLocksPathKey"
- "#16@0:8"
- ".cxx_destruct"
- "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
- "85ff7a90-361b-42d1-a420-97dee860f018"
- "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
- "@\"<SUSUICommandLineToolClientDelegate>\""
- "@\"BSAction\""
- "@\"NSNumber\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@\"SUAutoInstallForecast\""
- "@\"SUDescriptor\""
- "@\"SUKeybagInterface\""
- "@\"SURollbackDescriptor\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "@44@0:8@16B24@28@?36"
- "@56@0:8@16@24B32B36@40@?48"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@16^B24"
- "NSObject"
- "Q"
- "Q16@0:8"
- "SUKeybagInterfaceObserver"
- "SUSUI"
- "SUSUIAuthenticationInterface"
- "SUSUIAuthenticationKeybagInterface"
- "SUSUICommandLineToolClient"
- "SUSUICommandLineToolClientInterface"
- "SUSUICommandLineToolServerInterface"
- "SUSUIControllerClient"
- "SUSUIControllerServerInterface"
- "SUSUIExternalSettingsAppDefaults"
- "SUSUIFakeDocumentation"
- "SUSUIFakeSUAutoInstallForecast"
- "SUSUIFakeSUAutoInstallOperation"
- "SUSUIFakeSUDescriptor"
- "SUSUIFakeSUDownload"
- "SUSUIFakeSUDownloadMetadata"
- "SUSUIFakeSUOperationProgress"
- "SUSUIFakeSURollbackDescriptor"
- "SUSUIFakeSUScanResults"
- "SUSUILaggardsUIAlertAction"
- "SUSUIPreferences"
- "SUSUIRemoteEmergencyCallAlertAction"
- "SUSUISoftwareUpdateDefaults"
- "SUSUISoftwareUpdateOSVersion"
- "SUSUISoftwareUpdateState"
- "T#,R"
- "T@\"<SUSUICommandLineToolClientDelegate>\",W,N,V_delegate"
- "T@\"BSAction\",&,N,V_baseAction"
- "T@\"NSDictionary\",&,D,N"
- "T@\"NSNumber\",R,&,N,V_installAlertIntervalMinutes"
- "T@\"NSNumber\",R,&,N,V_passcodeRequiredDays"
- "T@\"NSNumber\",R,&,N,V_restartCountdownOverrideIntervalSeconds"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"SUAutoInstallForecast\",R,&,N"
- "T@\"SUDescriptor\",R,&,N"
- "T@\"SURollbackDescriptor\",R,&,N"
- "TB,D,N"
- "TB,N,GisBadgedForSoftwareUpdate"
- "TB,N,SsetLastAppliedUpdateWasSplatOnly:,V_lastAppliedUpdateWasSplatOnly"
- "TB,N,SsetLastUpdateWasSuccessful:,V_lastUpdateWasSuccessful"
- "TB,N,SsetNeedsAlertPresentationAfterOTAUpdate:,V_needsAlertPresentationAfterOTAUpdate"
- "TB,N,V_isController"
- "TB,R,N"
- "TB,R,N,V_IWillRebootLater"
- "TB,R,N,V_alertAfterDownload"
- "TB,R,N,V_isSharedIPad"
- "TB,R,N,V_preventCountdownAlert"
- "TB,R,N,V_preventPostUpdateAlert"
- "TB,R,N,V_preventRebootAlert"
- "TB,R,N,V_useMobileInboxUpdaterRebootDelay"
- "TQ,N,G_numberOfFailedAuthenticationAttempts,S_setNumberOfFailedAuthenticationAttempts:"
- "TQ,R"
- "TQ,R,N"
- "URLForType:"
- "URLWithString:"
- "Vv16@0:8"
- "^v32@0:8^{__CFString=}16Q24"
- "^{_NSZone=}16@0:8"
- "_IWillRebootLater"
- "__useDynamicMethodResolution"
- "_alertAfterDownload"
- "_alertType"
- "_autoInstallForecast"
- "_baseAction"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_calendar"
- "_canDeferInstallation"
- "_cancelled"
- "_clearLegacySpringBoardPreferences"
- "_componentsFromDate:"
- "_connectToServerIfNecessary"
- "_connected"
- "_copyNumberPreferenceForKey:"
- "_copyPreferenceForKey:ofType:"
- "_copyStringPreferenceForKey:"
- "_currentFailedAttemptsCount"
- "_defaults"
- "_delegate"
- "_descriptor"
- "_forInstallTonight"
- "_getBooleanPreferenceForKey:withDefaultValue:"
- "_incrementFailedAttemptsCount"
- "_initWithDomain:"
- "_initWithLegacyDefaults:"
- "_installAlertIntervalMinutes"
- "_invalidateConnection"
- "_isController"
- "_isPasscodeLocked"
- "_isSharedIPad"
- "_isSharedIpad"
- "_keybag"
- "_lastAppliedUpdateWasSplatOnly"
- "_lastUpdateWasSuccessful"
- "_loadIfNecessary"
- "_loadPreferences"
- "_loaded"
- "_migrateLegacySpringBoardPreferences"
- "_needsAlertPresentationAfterOTAUpdate"
- "_noteConnectionDropped"
- "_noteServerExiting"
- "_now"
- "_numberOfFailedAuthenticationAttempts"
- "_passcodeRequiredDays"
- "_preventCountdownAlert"
- "_preventPostUpdateAlert"
- "_preventRebootAlert"
- "_remoteInterface"
- "_remoteInterfaceWithErrorHandler:"
- "_restartCountdownOverrideIntervalSeconds"
- "_rollbackDescriptor"
- "_roundedEndTime"
- "_roundedStartTime"
- "_sbLegacyDefaults"
- "_serverConnection"
- "_serverIsExiting"
- "_setBooleanPreferenceForKey:value:"
- "_setDisableInstallTonight:"
- "_setMsuPrepareSize:"
- "_setNumberOfFailedAuthenticationAttempts:"
- "_setPasscodeLocked:"
- "_setQueue:"
- "_setUnarchiveSize:"
- "_store"
- "_susui_cardinalityForRoundedEndTime"
- "_susui_cardinalityForRoundedStartTime"
- "_susui_formattedRoundedEndTimeString"
- "_susui_formattedRoundedStartTimeString"
- "_timeFormatter"
- "_useMobileInboxUpdaterRebootDelay"
- "_uses24HourTimeForLocale"
- "_uuid"
- "addObserver:"
- "alertType"
- "attemptAuthentication:outBlocked:"
- "authenticate:"
- "autoInstallForecast"
- "autorelease"
- "backOffTime"
- "badgedForSoftwareUpdate"
- "baseAction"
- "boolForKey:"
- "boolValue"
- "buildVersion"
- "bundleIdentifier"
- "canDeferInstallation"
- "canSendResponse"
- "cancel"
- "class"
- "clearDeveloperInstallBrickAlerts"
- "components:fromDate:"
- "conformsToProtocol:"
- "createInstallationKeybag:forUnattendedInstall:"
- "createKeybagWithSecret:"
- "currentDevice"
- "currentLocale"
- "d"
- "d16@0:8"
- "dataUsingEncoding:"
- "dateFormat"
- "dateWithTimeIntervalSinceReferenceDate:"
- "ddmInstallNow"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeFromCoder:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "delegate"
- "description"
- "descriptor"
- "destroyInstallationKeybag"
- "dictionaryForKey:"
- "dismissAllAlerts"
- "doubleValue"
- "downloadDidFinish"
- "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "f16@0:8"
- "fakeAlternateDescriptor"
- "fakeDocumentation"
- "fakePreferredDescriptor"
- "fallbackXPCEncodableClass"
- "fb333b76-b463-401f-8899-96d82fc4c598"
- "finishDecoding"
- "fireCompletionIfNecessaryForResult:"
- "firstUnlock"
- "flagForSetting:"
- "forInstallTonight"
- "forecast"
- "formatCardinalityForDate:"
- "getAlertStatus:"
- "getDDMAlertStatus:"
- "getPasscodePolicy:"
- "hash"
- "hour"
- "i16@0:8"
- "id"
- "info"
- "init"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithCompletionBlock:"
- "initWithDelegate:"
- "initWithDelegate:queue:clientType:"
- "initWithDescriptor:autoInstallForecast:forInstallTonight:canDeferInstallation:completionQueue:completionBlock:"
- "initWithDescriptor:completionBlock:"
- "initWithInfo:forBaseAction:"
- "initWithInfo:responder:"
- "initWithInfo:timeout:forResponseOnQueue:withHandler:"
- "initWithKeybag:"
- "initWithMachServiceName:options:"
- "initWithPreferredDescriptor:alternateDescriptor:"
- "initWithRollbackDescriptor:canDeferInstallation:completionQueue:completionBlock:"
- "initWithSuiteName:"
- "installAlertIntervalMinutes"
- "interfaceWithProtocol:"
- "invalidate"
- "isAutoDownload"
- "isBadgedForSoftwareUpdate"
- "isBlocked"
- "isCanceled"
- "isController"
- "isDone"
- "isEqual:"
- "isEqualToString:"
- "isExpired"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPasscodeLocked"
- "isProxy"
- "keybagInterface:hasPasscodeSetDidChange:"
- "keybagInterface:passcodeLockedStateDidChange:"
- "keybagInterfacePasscodeDidChange:"
- "licenseAgreement"
- "loadIfNecessary"
- "localeIdentifier"
- "lockDevice"
- "mainBundle"
- "metadata"
- "migrateAndClearLegacyPreferences"
- "normalizedPercentComplete"
- "numberOfFailedAuthenticationAttempts"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectForSetting:"
- "percentComplete"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phase"
- "productBuildVersion"
- "productVersion"
- "progress"
- "q16@0:8"
- "rangeOfString:"
- "reboot:"
- "release"
- "releaseType"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeObjectForKey:"
- "resetAttempts"
- "responderWithHandler:"
- "respondsToSelector:"
- "responseWithInfo:"
- "restoreVersion"
- "resume"
- "retain"
- "retainCount"
- "rollbackDescriptor"
- "scheduleType"
- "self"
- "sendResponse:"
- "setAssetID:"
- "setAudienceType:"
- "setAutoDownloadAllowableForCellular:"
- "setAutoUpdateEnabled:"
- "setBadgedForSoftwareUpdate:"
- "setBaseAction:"
- "setBool:forKey:"
- "setCriticalOutOfBoxOnly:"
- "setDateStyle:"
- "setDelegate:"
- "setDownloadSize:"
- "setDownloadable:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFlag:forSetting:"
- "setForcePasscodeRequired:"
- "setHideInstallAlert:"
- "setHumanReadableUpdateName:"
- "setInstallOperation:"
- "setInstallationSize:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsController:"
- "setIsSplatOnly:"
- "setLastAppliedUpdateWasSplatOnly:"
- "setLastUpdateWasSuccessful:"
- "setLocalizedDateFormatFromTemplate:"
- "setMandatoryUpdateEligible:"
- "setMandatoryUpdateOptional:"
- "setMandatoryUpdateRestrictedToOutOfTheBox:"
- "setMandatoryUpdateVersionMax:"
- "setMandatoryUpdateVersionMin:"
- "setNeedsAlertPresentationAfterOTAUpdate:"
- "setObject:forKey:"
- "setObject:forSetting:"
- "setPasscodePolicy:"
- "setPreferenceType:"
- "setPrerequisiteBuild:"
- "setPrerequisiteOS:"
- "setProductBuildVersion:"
- "setProductSystemName:"
- "setProductVersion:"
- "setPromoteAlternateUpdate:"
- "setPublisher:"
- "setRampEnabled:"
- "setRemoteObjectInterface:"
- "setRestartCountdownOverrideIntervalSeconds:"
- "setSetupCritical:"
- "setTimeStyle:"
- "setUpdateToInstall:"
- "setUpdateType:"
- "setUpgradeType:"
- "sharedInstance"
- "showAuthenticationUIWithOptions:result:"
- "showDDMAlert:install:"
- "showEmergencyCallUIWithOptions:result:"
- "showFollowUp:"
- "showLaggardsUi:usingFakeData:result:"
- "showMiniAlertWithDescriptors:errorCode:downloadDescriptor:scanResultsDescriptor:autoInstallForecast:andRollbackDescriptor:result:"
- "showMiniAlertWithScan:errorCode:result:"
- "simulateComingFromOTAUpdate"
- "standardUserDefaults"
- "stringFromDate:"
- "stringWithUTF8String:"
- "suEndDate"
- "suStartDate"
- "superclass"
- "synchronize"
- "systemVersion"
- "termsAndConditionsAgreementStatus"
- "timeIntervalSinceReferenceDate"
- "timeRemaining"
- "toggleSettingsBadge:"
- "unlockEndDate"
- "unlockStartDate"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"SUAutoInstallOperation\"16"
- "v24@0:8@\"SUDownload\"16"
- "v24@0:8@\"SUKeybagInterface\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?Q>16"
- "v24@0:8Q16"
- "v28@0:8@\"SUKeybagInterface\"16B24"
- "v28@0:8@16B24"
- "v28@0:8q16B24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v36@0:8Q16B24@?28"
- "v36@0:8Q16B24@?<v@?B@\"NSError\">28"
- "v40@0:8Q16@\"NSNumber\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v72@0:8Q16@\"NSNumber\"24@\"SUDownload\"32@\"SUScanResults\"40@\"SUAutoInstallForecast\"48@\"SURollbackDescriptor\"56@?<v@?@\"NSString\"@\"NSError\">64"
- "v72@0:8Q16@24@32@40@48@56@?64"
- "valueForKey:"
- "zone"

```
