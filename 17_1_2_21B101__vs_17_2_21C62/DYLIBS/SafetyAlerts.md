## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-43.0.9.0.1
-  __TEXT.__text: 0xfe8
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x103
-  __TEXT.__oslogstring: 0x652
-  __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x129
-  __TEXT.__objc_methtype: 0x6f
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x8
+43.0.27.0.0
+  __TEXT.__text: 0x4a40
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x320
+  __TEXT.__const: 0x4c
+  __TEXT.__cstring: 0x81d
+  __TEXT.__oslogstring: 0x1754
+  __TEXT.__gcc_except_tab: 0xc
+  __TEXT.__unwind_info: 0x160
+  __TEXT.__objc_classname: 0x22
+  __TEXT.__objc_methname: 0xafb
+  __TEXT.__objc_methtype: 0x106
+  __TEXT.__objc_stubs: 0x960
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x48
-  __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__auth_got: 0xc0
-  __DATA.__objc_classrefs: 0x10
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x8
+  __DATA_CONST.__objc_const: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x320
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH_CONST.__auth_got: 0x170
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_ivar: 0x24
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libPCITransport.dylib

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14
-  Symbols:   86
-  CStrings:  59
+  Functions: 85
+  Symbols:   358
+  CStrings:  281
 
Symbols:
+ +[SAEDFollowUpManager sharedInstance]
+ -[SAEDFollowUpManager _addNotificationObservers]
+ -[SAEDFollowUpManager _ctSuppressEDFollowUpReason]
+ -[SAEDFollowUpManager _currentDeviceHasEnhancedDeliverySwitch]
+ -[SAEDFollowUpManager _evaluateFollowUpStateAsync]
+ -[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]
+ -[SAEDFollowUpManager _isIgneousEnabled]
+ -[SAEDFollowUpManager _onCellConfigChanged:]
+ -[SAEDFollowUpManager _postFollowUp]
+ -[SAEDFollowUpManager _removeNotificationObservers]
+ -[SAEDFollowUpManager _retractFollowUp]
+ -[SAEDFollowUpManager _saSuppressEDFollowUpReason]
+ -[SAEDFollowUpManager _shouldDeferFollowUpForSAReason:]
+ -[SAEDFollowUpManager _shouldPostFollowUpForCTReason:]
+ -[SAEDFollowUpManager _shouldPostFollowUpForSAReason:]
+ -[SAEDFollowUpManager _shouldRetractFollowUpForSAReason:]
+ -[SAEDFollowUpManager boolForDefaultsKey:defaultValue:]
+ -[SAEDFollowUpManager boolOverrideForDefaultsKey:defaultValue:]
+ -[SAEDFollowUpManager ctSuppressEDFollowUpReason]
+ -[SAEDFollowUpManager currentLocationInCoveredRegion]
+ -[SAEDFollowUpManager dealloc]
+ -[SAEDFollowUpManager followUpState]
+ -[SAEDFollowUpManager hasNumberOverrideForDefaultsKey:]
+ -[SAEDFollowUpManager hasValidCurrentLocationInCoveredRegion]
+ -[SAEDFollowUpManager hasValidLocationServicesEnabled]
+ -[SAEDFollowUpManager hasValidUptakeCoefficient]
+ -[SAEDFollowUpManager init]
+ -[SAEDFollowUpManager locationServicesEnabled]
+ -[SAEDFollowUpManager noteUserViewedEDSettings]
+ -[SAEDFollowUpManager numberOverrideForDefaultsKey:defaultValue:]
+ -[SAEDFollowUpManager saSuppressEDFollowUpReason]
+ -[SAEDFollowUpManager setCtSuppressEDFollowUpReason:]
+ -[SAEDFollowUpManager setCurrentLocationInCoveredRegion:]
+ -[SAEDFollowUpManager setFollowUpState:]
+ -[SAEDFollowUpManager setLocationServicesEnabled:]
+ -[SAEDFollowUpManager setSAEWEnabledState:]
+ -[SAEDFollowUpManager setSaSuppressEDFollowUpReason:]
+ -[SAEDFollowUpManager setUptakeCoefficient:]
+ -[SAEDFollowUpManager setUserViewedEDSettings:]
+ -[SAEDFollowUpManager shouldShowCFUPerUptakeCoefficient]
+ -[SAEDFollowUpManager start]
+ -[SAEDFollowUpManager stringForDefaultsKey:defaultValue:]
+ -[SAEDFollowUpManager uintForDefaultsKey:defaultValue:]
+ -[SAEDFollowUpManager uptakeCoefficient]
+ -[SAEDFollowUpManager userDefaults]
+ -[SAEDFollowUpManager userViewedEDSettings]
+ -[SafetyAlerts fetchIsSaewEnabledOnQueue:withReply:]
+ -[SafetyAlerts getIgneousEnablementStateReply:stateInfo:]
+ -[SafetyAlerts getIgneousStatusInfoFromReply:]
+ -[SafetyAlerts getIgneousTestStatusSync]
+ -[SafetyAlerts isSaewEnabledSync:]
+ -[SafetyAlerts onEnhancedDeliveryEnabled:]
+ -[SafetyAlerts onEnhancedDeliveryPageVisited]
+ GCC_except_table0
+ _AnalyticsSendEventLazy
+ _CFRelease
+ _FLGroupIdentifierDevice
+ _MGCopyAnswer
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_FLFollowUpAction
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_FLFollowUpItem
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_SAEDFollowUpManager
+ _OBJC_IVAR_$_SAEDFollowUpManager._currentLocationInCoveredRegion
+ _OBJC_IVAR_$_SAEDFollowUpManager._currentLocationInCoveredRegion_Valid
+ _OBJC_IVAR_$_SAEDFollowUpManager._evaluationQueue
+ _OBJC_IVAR_$_SAEDFollowUpManager._locationServicesEnabled
+ _OBJC_IVAR_$_SAEDFollowUpManager._locationServicesEnabled_Valid
+ _OBJC_IVAR_$_SAEDFollowUpManager._uptakeCoefficient
+ _OBJC_IVAR_$_SAEDFollowUpManager._uptakeCoefficient_Valid
+ _OBJC_METACLASS_$_SAEDFollowUpManager
+ __CTServerConnectionCreateOnTargetQueue
+ __CTServerConnectionGetCellBroadcastConfig
+ __OBJC_$_CLASS_METHODS_SAEDFollowUpManager
+ __OBJC_$_INSTANCE_METHODS_SAEDFollowUpManager
+ __OBJC_$_INSTANCE_VARIABLES_SAEDFollowUpManager
+ __OBJC_$_PROP_LIST_SAEDFollowUpManager
+ __OBJC_CLASS_RO_$_SAEDFollowUpManager
+ __OBJC_METACLASS_RO_$_SAEDFollowUpManager
+ __Unwind_Resume
+ __ZGVZN14SAPlatformInfo8instanceEvE14saPlatformInfo
+ __ZN14SAPlatformInfo18fetchIsTinkerWatchEv
+ __ZN14SAPlatformInfo8instanceEv
+ __ZN14SAPlatformInfoC1Ev
+ __ZN14SAPlatformInfoC2Ev
+ __ZZN14SAPlatformInfo8instanceEvE14saPlatformInfo
+ ___35-[SAEDFollowUpManager userDefaults]_block_invoke
+ ___36-[SAEDFollowUpManager _postFollowUp]_block_invoke
+ ___36-[SAEDFollowUpManager _postFollowUp]_block_invoke_2
+ ___37+[SAEDFollowUpManager sharedInstance]_block_invoke
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.91
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke_2
+ ___40-[SAEDFollowUpManager setFollowUpState:]_block_invoke
+ ___43-[SAEDFollowUpManager setSAEWEnabledState:]_block_invoke
+ ___47-[SAEDFollowUpManager setUserViewedEDSettings:]_block_invoke
+ ___50-[SAEDFollowUpManager _evaluateFollowUpStateAsync]_block_invoke
+ ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke
+ ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.29
+ ___52-[SafetyAlerts fetchIsSaewEnabledOnQueue:withReply:]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32o_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32o_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_41_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32o40b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_49_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e19_"NSDictionary"8?0l
+ ___block_descriptor_56_e8_32o40o48o_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ ___gxx_personality_v0
+ _arc4random_uniform
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _kCTSMSCellBroadcastConfigChangedNotification
+ _objc_alloc
+ _objc_autorelease
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_addNotificationObservers
+ _objc_msgSend$_ctSuppressEDFollowUpReason
+ _objc_msgSend$_currentDeviceHasEnhancedDeliverySwitch
+ _objc_msgSend$_evaluateFollowUpStateAsync
+ _objc_msgSend$_evaluateFollowUpState_LOCKED
+ _objc_msgSend$_isIgneousEnabled
+ _objc_msgSend$_postFollowUp
+ _objc_msgSend$_removeNotificationObservers
+ _objc_msgSend$_retractFollowUp
+ _objc_msgSend$_saSuppressEDFollowUpReason
+ _objc_msgSend$_shouldDeferFollowUpForSAReason:
+ _objc_msgSend$_shouldPostFollowUpForCTReason:
+ _objc_msgSend$_shouldPostFollowUpForSAReason:
+ _objc_msgSend$_shouldRetractFollowUpForSAReason:
+ _objc_msgSend$actionWithLabel:url:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$boolOverrideForDefaultsKey:defaultValue:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$clearPendingFollowUpItemsWithUniqueIdentifiers:completion:
+ _objc_msgSend$countOfPendingFollowUpItemsWithCompletion:
+ _objc_msgSend$ctSuppressEDFollowUpReason
+ _objc_msgSend$currentLocationInCoveredRegion
+ _objc_msgSend$date
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$floatValue
+ _objc_msgSend$followUpState
+ _objc_msgSend$getIgneousEnablementStateReply:stateInfo:
+ _objc_msgSend$getIgneousStatusInfoFromReply:
+ _objc_msgSend$hasNumberOverrideForDefaultsKey:
+ _objc_msgSend$hasValidCurrentLocationInCoveredRegion
+ _objc_msgSend$hasValidLocationServicesEnabled
+ _objc_msgSend$hasValidUptakeCoefficient
+ _objc_msgSend$initWithClientIdentifier:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$locationServicesEnabled
+ _objc_msgSend$numberOverrideForDefaultsKey:defaultValue:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$postFollowUpItem:completion:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$saSuppressEDFollowUpReason
+ _objc_msgSend$setActions:
+ _objc_msgSend$setCtSuppressEDFollowUpReason:
+ _objc_msgSend$setDisplayStyle:
+ _objc_msgSend$setFollowUpState:
+ _objc_msgSend$setGroupIdentifier:
+ _objc_msgSend$setInformativeText:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setSaSuppressEDFollowUpReason:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setUniqueIdentifier:
+ _objc_msgSend$setUserViewedEDSettings:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shouldShowCFUPerUptakeCoefficient
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$uintForDefaultsKey:defaultValue:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$uptakeCoefficient
+ _objc_msgSend$userDefaults
+ _objc_msgSend$userViewedEDSettings
+ _os_variant_has_internal_content
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_double
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_bool
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "@24@0:8@16"
+ "@32@0:8@16@24"
+ "B"
+ "B24@0:8Q16"
+ "B24@0:8^@16"
+ "B28@0:8@16B24"
+ "B32@0:8@16@24"
+ "DeviceClass"
+ "EmergencyAlertsPref"
+ "Enabled"
+ "EnhancedDeliveryAvailability"
+ "EnhancedDeliveryPref"
+ "Evaluate"
+ "NOP"
+ "Q16@0:8"
+ "Q32@0:8@16Q24"
+ "SAEDFollowUpManager"
+ "SAFETYALERTS_ENHANCED_DELIVERY_FOLLOW_UP_BODY_PHONE"
+ "SAFETYALERTS_ENHANCED_DELIVERY_FOLLOW_UP_REDIRECT_ACTION_TITLE"
+ "SAFETYALERTS_ENHANCED_DELIVERY_FOLLOW_UP_TITLE"
+ "SetFollowupState"
+ "ShowedEDSettings"
+ "T@\"NSUserDefaults\",R,N"
+ "TB,N"
+ "TB,N,V_currentLocationInCoveredRegion"
+ "TB,N,V_locationServicesEnabled"
+ "TQ,N"
+ "Tf,N,V_uptakeCoefficient"
+ "URLWithString:"
+ "_addNotificationObservers"
+ "_ctSuppressEDFollowUpReason"
+ "_currentDeviceHasEnhancedDeliverySwitch"
+ "_currentLocationInCoveredRegion"
+ "_currentLocationInCoveredRegion_Valid"
+ "_evaluateFollowUpStateAsync"
+ "_evaluateFollowUpState_LOCKED"
+ "_evaluationQueue"
+ "_isIgneousEnabled"
+ "_locationServicesEnabled"
+ "_locationServicesEnabled_Valid"
+ "_onCellConfigChanged:"
+ "_postFollowUp"
+ "_removeNotificationObservers"
+ "_retractFollowUp"
+ "_saSuppressEDFollowUpReason"
+ "_shouldDeferFollowUpForSAReason:"
+ "_shouldPostFollowUpForCTReason:"
+ "_shouldPostFollowUpForSAReason:"
+ "_shouldRetractFollowUpForSAReason:"
+ "_uptakeCoefficient"
+ "_uptakeCoefficient_Valid"
+ "action"
+ "actionWithLabel:url:"
+ "addObserver:selector:name:object:"
+ "arrayWithObjects:count:"
+ "boolForDefaultsKey:defaultValue:"
+ "boolOverrideForDefaultsKey:defaultValue:"
+ "boolValue"
+ "bundleForClass:"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:completion:"
+ "com.apple.SAEDFollowUpManager"
+ "com.apple.safetyalerts.enhancedDelivery.CFU.update"
+ "com.apple.safetyalerts.enhancedDelivery.onboardPrompt"
+ "contains-cellular-radio"
+ "countOfPendingFollowUpItemsWithCompletion:"
+ "ctSuppressEDFollowUpReason"
+ "currentLocationInCoveredRegion"
+ "date"
+ "dealloc"
+ "defaultCenter"
+ "dictionaryWithObjects:forKeys:count:"
+ "dictionaryWithObjectsAndKeys:"
+ "enhancedDelivery.followUp.ctSuppressionReason"
+ "enhancedDelivery.followUp.lastTestedUptakeCoefficient"
+ "enhancedDelivery.followUp.override.currentLocationInCoveredRegion"
+ "enhancedDelivery.followUp.override.emergencyAlertsEnabled"
+ "enhancedDelivery.followUp.override.enhancedDeliveryAvailable"
+ "enhancedDelivery.followUp.override.enhancedDeliveryPrefEnabled"
+ "enhancedDelivery.followUp.override.isIgneousEnabled"
+ "enhancedDelivery.followUp.override.locationServicesEnabled"
+ "enhancedDelivery.followUp.override.uptakeCoefficient"
+ "enhancedDelivery.followUp.saSuppressionReason"
+ "enhancedDelivery.followUp.settingsViewedDate"
+ "enhancedDelivery.followUp.state"
+ "enhancedDeliveryPageVisited"
+ "f"
+ "f16@0:8"
+ "fetchIsSaewEnabledOnQueue:withReply:"
+ "floatValue"
+ "followUpState"
+ "getIgneousEnablementStateReply:stateInfo:"
+ "getIgneousStatusInfoFromReply:"
+ "getIgneousTestStatusSync"
+ "hasNumberOverrideForDefaultsKey:"
+ "hasValidCurrentLocationInCoveredRegion"
+ "hasValidLocationServicesEnabled"
+ "hasValidUptakeCoefficient"
+ "iPhone"
+ "igneousAlertReceivedTs"
+ "igneousStateInfoChannel"
+ "igneousStateInfoError"
+ "igneousStateInfoIngressLatency"
+ "igneousStateInfoOriginiatedLatency"
+ "igneousStateInfoUID"
+ "initWithClientIdentifier:"
+ "initWithSuiteName:"
+ "isEqualToString:"
+ "isSaewEnabledSync:"
+ "jkr5aFPOh/d6zTzNKYthBw"
+ "localizedStringForKey:value:table:"
+ "locationServicesEnabled"
+ "newFollowUpState"
+ "noteUserViewedEDSettings"
+ "numberOverrideForDefaultsKey:defaultValue:"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithFloat:"
+ "numberWithInt:"
+ "numberWithUnsignedInteger:"
+ "objectForKeyedSubscript:"
+ "onEnhancedDeliveryEnabled:"
+ "onEnhancedDeliveryPageVisited"
+ "postFollowUpItem:completion:"
+ "prefs:root=NOTIFICATIONS_ID&path=com.apple.cmas.EmergencyAlerts"
+ "removeObserver:name:object:"
+ "saDelivery"
+ "saEnabledStateDefaultsWrite"
+ "saEnablementStateEnabled"
+ "saEnablementStateInCountry"
+ "saEnablementStateInCoverageArea"
+ "saEnablementStateInMagnetMode"
+ "saEnablementStateOptedIn"
+ "saIgneousEnableState"
+ "saIgneousTestState"
+ "saSuppressEDFollowUpReason"
+ "setActions:"
+ "setCtSuppressEDFollowUpReason:"
+ "setCurrentLocationInCoveredRegion:"
+ "setDisplayStyle:"
+ "setFollowUpState:"
+ "setGroupIdentifier:"
+ "setInformativeText:"
+ "setLocationServicesEnabled:"
+ "setObject:forKey:"
+ "setSAEWEnabledState:"
+ "setSaSuppressEDFollowUpReason:"
+ "setTitle:"
+ "setUniqueIdentifier:"
+ "setUptakeCoefficient:"
+ "setUserViewedEDSettings:"
+ "setValue:forKey:"
+ "sharedInstance"
+ "shouldShowCFUPerUptakeCoefficient"
+ "start"
+ "startingFollowUpState"
+ "stringForDefaultsKey:defaultValue:"
+ "stringWithUTF8String:"
+ "uintForDefaultsKey:defaultValue:"
+ "unsignedIntegerValue"
+ "uptakeCoefficient"
+ "userDefaults"
+ "userViewedEDSettings"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v20@0:8f16"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8Q16"
+ "v24@?0Q8@\"NSError\"16"
+ "weaAlertReceivedTs"
+ "weaText"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_addNotificationObservers\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_ctSuppressEDFollowUpReason,_CTServerConnectionGetCellBroadcastConfig error\", \"error.domain\":%{public}ld, \"error.error\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_ctSuppressEDFollowUpReason,_CTServerConnectionGetCellBroadcastConfig\", \"configDict\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState with !isIgneousEnabled\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED\", \"followUpState\":%{public}lu, \"ctSuppressEDFollowUpReason\":%{public}lu, \"saSuppressEDFollowUpReason\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,deferring FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,followUpState >= SAFollowUpStateRetracted\", \"followUpState\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,posted,leaving posted\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,posted,retracting FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,posting FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,retractingFailed,retracting FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,skipping FollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_evaluateFollowUpState_LOCKED,unexpected followUpState\", \"followUpState\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_onCellConfigChanged\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_postFollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_postFollowUp,failed to post FollowUp\", \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_postFollowUp,posted FollowUp successfully\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_removeNotificationObservers\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_retractFollowUp\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_retractFollowUp,cleared FollowUp successfully\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_retractFollowUp,error from countOfPendingFollowUpItemsWithCompletion\", \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_retractFollowUp,failed to clear FollowUp\", \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_retractFollowUp,no pendingFollowUpItems\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,_shouldRetractFollowUpForSAReason,very unexpected reason\", \"saSuppressEDFollowUpReason\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,init,!isIgneousEnabled\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,noteUserViewedEDSettings\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,numberOverrideForDefaultsKey,#overriding\", \"key\":%{public, location:escape_only}@, \"overrideNumber\":%{public, location:escape_only}@, \"defaultValue\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,setSAEWEnabledState\", \"state\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,shouldShowCFUPerUptakeCoefficient\", \"showCFU\":%{public}hhd, \"uptakeCoefficient\":\"%{public}f\", \"threshold\":\"%{public}f\", \"randomValue\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"#SAEDFollowUp,start\"}"
+ "{\"msg%{public}.0s\":\"#saClient,Igneous reply nil\"}"
+ "{\"msg%{public}.0s\":\"#saClient,IgneousInfo,replyIsNotADictionary\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply nil\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply\", \"inCountry\":%{public}hhd, \"inCoverage\":%{public}hhd, \"inMagnetMode\":%{public}hhd, \"optedIn\":%{public}hhd, \"enabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousEnablementStateReply,replyIsNotADictionary\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousStatusInfoFromReply\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousTestStatusSyncDone\"}"
+ "{\"msg%{public}.0s\":\"#saClient,isSaewEnabledSyncDone\", \"enabled\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saClient,onEnhancedDeliveryEnabled\", \"isEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saClient,onEnhancedDeliveryPageVisited\"}"
+ "{\"msg%{public}.0s\":\"currentLocationInCoveredRegion + !hasValidCurrentLocationInCoveredRegion\"}"
+ "{\"msg%{public}.0s\":\"daemonInterfaceProd,getIgneousTestStatusSync\"}"
+ "{\"msg%{public}.0s\":\"locationServicesEnabled + !hasValidLocationServicesEnabled\"}"
+ "{\"msg%{public}.0s\":\"saClient,isSaewEnabledSync invalid context\"}"
+ "{\"msg%{public}.0s\":\"saClient,isSaewEnabledSync\"}"
+ "{\"msg%{public}.0s\":\"uptakeCoefficient + !hasValidUptakeCoefficient\"}"

```
