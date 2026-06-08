## HAENotifications

> `/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications`

```diff

-819.603.0.0.0
-  __TEXT.__text: 0xdbf8
-  __TEXT.__auth_stubs: 0x600
+879.1.0.0.0
+  __TEXT.__text: 0xc2cc
   __TEXT.__objc_methlist: 0xc34
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0xeca
-  __TEXT.__oslogstring: 0x159d
+  __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__objc_classname: 0x1d7
-  __TEXT.__objc_methname: 0x223c
-  __TEXT.__objc_methtype: 0x70f
-  __TEXT.__objc_stubs: 0x2000
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x258
+  __TEXT.__cstring: 0xecb
+  __TEXT.__oslogstring: 0x15e6
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x328
   __AUTH_CONST.__const: 0x298
-  __AUTH_CONST.__cfstring: 0x10c0
-  __AUTH_CONST.__objc_const: 0x1c30
+  __AUTH_CONST.__cfstring: 0x1060
+  __AUTH_CONST.__objc_const: 0x1640
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x20
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 890A6EE8-7600-3F6B-ABA1-AE98C57D0CBE
-  Functions: 315
-  Symbols:   1442
-  CStrings:  935
+  UUID: 39685290-159F-3E41-BC26-E82607B2A948
+  Functions: 249
+  Symbols:   1265
+  CStrings:  428
 
Symbols:
+ GCC_except_table139
+ ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.373
+ ___block_literal_global.110
+ ___block_literal_global.129
+ ___block_literal_global.188
+ ___block_literal_global.225
+ ___block_literal_global.257
+ ___block_literal_global.347
+ ___block_literal_global.383
+ ___block_literal_global.550
+ ___block_literal_global.68
+ ___block_literal_global.743
+ ___block_literal_global.788
+ ___block_literal_global.86
+ ___block_literal_global.91
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x9
+ _sharedInstance.instance.189
+ _sharedInstance.instance.226
+ _sharedInstance.instance.258
+ _sharedInstance.instance.348
+ _sharedInstance.instance.551
+ _sharedInstance.instance.69
+ _sharedInstance.instance.744
+ _sharedInstance.instance.92
+ _sharedInstance.once.187
+ _sharedInstance.once.224
+ _sharedInstance.once.256
+ _sharedInstance.once.346
+ _sharedInstance.once.549
+ _sharedInstance.once.67
+ _sharedInstance.once.742
+ _sharedInstance.once.90
- +[HAENAccessoryInfo getAccessoryInfo:].cold.1
- +[HAENAccessoryInfo getAccessoryInfo:].cold.2
- +[HAENAccessoryInfo getAccessoryInfoFromIOAccesoryManager:].cold.1
- +[HAENAccessoryInfo getAccessoryInfoFromIOAccesoryManager:].cold.2
- +[HAENAccessoryInfo getAccessoryInfoFromIOAccesoryManager:].cold.3
- +[HAENAccessoryInfo getAccessoryInfoFromIOAccesoryManager:].cold.4
- +[HAENAccessoryInfo getAccessoryInfoFromIOKitDirectly:].cold.1
- +[HAENDefaults HAENSupportedForCurrentDeviceClass].cold.1
- +[HAENDefaults isCurrentProcessMediaserverd].cold.1
- +[HAENDefaults isRunningCITests].cold.1
- +[HAENDefaults sharedInstance].cold.1
- +[HAENHealthKitStore createHKCategorySampleForEvent:].cold.1
- +[HAENHealthKitStore sharedInstance].cold.1
- +[HAENLocationGatingHelper sharedInstance].cold.1
- +[HAENStatistics sharedInstance].cold.1
- +[HAENSystemSoundPlayer sharedInstance].cold.1
- +[HAENUnknownDeviceManager sharedInstance].cold.1
- +[HAENVolumeControl sharedInstance].cold.1
- +[HAENotificationCenterManager sharedInstance].cold.1
- +[HAENotificationCenterServer sharedInstance].cold.1
- -[HAENDefaults _updateSetting:value:notify:].cold.1
- -[HAENDefaults getAudioAccessoryConnectionInfoWithKey:].cold.1
- -[HAENDefaults getAudioAccessoryConnectionInfo].cold.1
- -[HAENDefaults isCurrentAudioAccessoryHeadphoneWithKey:].cold.1
- -[HAENDefaults isCurrentAudioAccessoryHeadphone].cold.1
- -[HAENDefaults setAudioAccessoryIsConnectedToHeadphones:withName:].cold.1
- -[HAENDefaults setUserVolumeWithValue:mininum:].cold.1
- -[HAENDefaults setUserVolumeWithValue:mininum:].cold.2
- -[HAENDefaults updateAudioAccessoryIsConnectedToHeadphones:].cold.1
- -[HAENDefaults updateAudioAccessoryIsConnectedToHeadphones:].cold.2
- -[HAENLocationGatingHelper _isMandatoryDeviceClass].cold.1
- -[HAENLocationGatingHelper _loadRegionPlistFile].cold.1
- -[HAENUnknownDeviceManager deviceSessionCreated:SessionID:].cold.1
- -[HAENUnknownDeviceManager deviceSessionDestroyed:isWired:].cold.1
- -[HAENUnknownDeviceManager registerDevice:].cold.1
- -[HAENUnknownDeviceManager registerDevice:].cold.2
- -[HAENUnknownDeviceManager updateWiredDeviceStatus].cold.1
- -[HAENVolumeControl getCurrentVolumeForCategory:route:].cold.1
- -[HAENVolumeControl limitVolumeTo:category:route:actionResult:].cold.1
- -[HAENotificationCenterManager donateSignalToTipsKit:].cold.1
- -[HAENotificationCenterManager sendBannerNotificationWithEvent:volumeLoweringAction:].cold.1
- -[NotificationCenter handleNotificationAction:].cold.1
- -[NotificationCenter handleNotificationAction:].cold.2
- -[NotificationCenter sendNotificationWithExposureLevel:duration:eventType:volumeLoweringAction:].cold.1
- -[NotificationCenter userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:].cold.1
- GCC_except_table3
- _GeoLocationDidChange.cold.1
- _HAENAccessoryInfoErrorDomain
- _HAENLocalizationUtilityGetBundle.cold.1
- _HAENotificationsFrameworkVersionNumber
- _HAENotificationsFrameworkVersionString
- _HAENotificationsLog.cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _ReleaseHAENRouteInfo
- _RemoveDeviceSpecificDefaultsFor
- _SyncDeviceSpecificDomain
- ___46-[HAENotificationCenterClient setupConnection]_block_invoke.50.cold.1
- ___46-[HAENotificationCenterClient setupConnection]_block_invoke.50.cold.2
- ___46-[HAENotificationCenterClient setupConnection]_block_invoke.cold.1
- ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.352
- ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.352.cold.1
- ___55-[HAENotificationCenterClient addHAENotificationEvent:]_block_invoke.cold.1
- ___96-[NotificationCenter sendNotificationWithExposureLevel:duration:eventType:volumeLoweringAction:]_block_invoke.cold.1
- ___block_literal_global.90
- _kDefaultsKeyHAENFeatureMandatory
- _kDefaultsKeyHAENGeoLocationFinalized
- _kDefaultsKeyHAENGeoLocationSource
- _kHAENKeyEventAudioExposureLevel
- _kHAENKeyEventDateInterval
- _kHAENKeyEventMetadata
- _kHAENKeyEventType
- _kHAENKeyEventUUID
- _kHAENMandatoryPlistFilePath
- _kHAENVolumeReductionUnitDelta
- _kISOCountryCode_SOUTH_KOREA
- _kInvalidADAMSessionID
- _kRegionalPlistKey
- _kWiredHeadsetName
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "DeviceSupportsClosedLoopHaptics"
+ "DeviceSupportsHaptics"
+ "failed to update the HAEN Unknown-Headset DB because the name is missing"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HAENotificationCenterDelegate>\""
- "@\"<HAENotificationCenterUserDelegate>\""
- "@\"HAENGeoLocation\""
- "@\"HKHealthStore\""
- "@\"NSDate\""
- "@\"NSDateInterval\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"NotificationCenter\""
- "@\"UNUserNotificationCenter\""
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16I24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@44@0:8I16d20@28@36"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "Discoverability"
- "HAENAccessoryInfo"
- "HAENDefaults"
- "HAENGeoLocation"
- "HAENGeoLocationFinalized"
- "HAENHealthKitStore"
- "HAENLocationGatingHelper"
- "HAENStatistics"
- "HAENSupportedForCurrentDeviceClass"
- "HAENSystemSoundPlayer"
- "HAENUnknownDeviceManager"
- "HAENVolumeControl"
- "HAENotificationCenter"
- "HAENotificationCenterClient"
- "HAENotificationCenterDelegate"
- "HAENotificationCenterManager"
- "HAENotificationCenterServer"
- "HAENotificationEvent"
- "I"
- "I16@0:8"
- "I24@0:8@16"
- "KR"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "NotificationCenter"
- "PME_enabled"
- "Q"
- "Q16@0:8"
- "Signals"
- "T#,R"
- "T@\"<HAENotificationCenterUserDelegate>\",R,W,N,V_delegate"
- "T@\"NSDate\",R,N,Vtimestamp"
- "T@\"NSDateInterval\",R,N,VdateInterval"
- "T@\"NSDictionary\",R,N,Vmetadata"
- "T@\"NSNumber\",R,V_interfaceDeviceSerialNumber"
- "T@\"NSString\",&,N,VbundleID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,VbundleID"
- "T@\"NSString\",R,N,VcountryCode"
- "T@\"NSString\",R,N,VimmutableDescription"
- "T@\"NSString\",R,V_interfaceModuleSerialNumber"
- "T@\"NSString\",R,V_manufacturer"
- "T@\"NSString\",R,V_modelNumber"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_serialNumber"
- "T@\"NSUUID\",R,N,Vuuid"
- "TB,R"
- "TI,R,N,VeventType"
- "TI,R,N,Vsource"
- "TI,R,N,VsourceDevice"
- "TQ,R"
- "Td,R,N,Vlevel"
- "Td,R,N,VliveMonitorWindowInSec"
- "Td,R,N,VliveThresholdInDBA"
- "UNUserNotificationCenterDelegate"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFUserNotification=}"
- "_EUVolumeLimitFlag"
- "_EUVolumeLimitFlagOn"
- "_RLSAllowsMXVolumeLimit"
- "_SKVolumeLimitFlag"
- "_SKVolumeLimitFlagOn"
- "_adamSessionID"
- "_alertPending"
- "_alertSupported"
- "_body"
- "_connectionCnt"
- "_contryConfigurationDidChange:"
- "_delegate"
- "_deviceName"
- "_deviceUID"
- "_domainSettings"
- "_donateSignalToTipsKit:"
- "_donateSignalToTipsKitOnInitialization"
- "_eventQueue"
- "_fetchCategory:routeInfo:"
- "_generateAccessoryKeyWithManufacture:andSerialNumber:"
- "_geoLocation"
- "_getMGProductType"
- "_haenFeatureEnabled"
- "_hasHaptics"
- "_hasHealthApp"
- "_healthAppHidden"
- "_healthStore"
- "_interfaceDeviceSerialNumber"
- "_interfaceModuleSerialNumber"
- "_isAlertSupported"
- "_isHAENFeatureMandatory:dataDisposition:"
- "_isIPad"
- "_isIPod"
- "_isMandatoryDeviceClass"
- "_isUnknownWiredHeadset:"
- "_isWiredUnknown"
- "_liveThresholdInDBA"
- "_loadRegionPlistFile"
- "_lock"
- "_logLocationGatingFlags"
- "_lowerHeadphoneVolumeAtNextSession"
- "_manufacturer"
- "_modelNumber"
- "_mxVolumeLimitOn"
- "_name"
- "_notification"
- "_notificationCenter"
- "_options"
- "_pid"
- "_processPrompt:"
- "_processWiredDevice:"
- "_productTypeOverride"
- "_queue"
- "_readDeviceDisposition"
- "_regionAndDeviceMandatesFeature:"
- "_regionBehavior"
- "_registerNotification:"
- "_resetWiredStatus"
- "_sem"
- "_sendMessage:"
- "_serialNumber"
- "_setFeatureMandatoryFlag:"
- "_setHEANEnabled:"
- "_setMXVolumeLimit:"
- "_shouldRepromptSinceDate:"
- "_shouldSurfaceAlert:"
- "_shouldUpdateLocation:"
- "_stats"
- "_subtitle"
- "_targetVolume74dB"
- "_targetVolume80dB"
- "_title"
- "_turnOFFSound"
- "_updateFlags"
- "_updateImpl"
- "_updateLocationGatingFlags"
- "_updateMXVolumeLimit"
- "_updateMXVolumeLimitStatus:"
- "_updateQueue"
- "_updateSampleTransient:"
- "_updateSetting:value:notify:"
- "_updateStatsWithGeoLocation:disposition:andMandatoryFlag:"
- "_userDefaults"
- "_userNotificationCenter"
- "_validCountryCodeSource:"
- "_validDataDisposition:"
- "_wiredDeviceSessionCreated:SessionID:"
- "_wiredDeviceSessionDestroyed:"
- "_wiredDeviceSessionInit:"
- "_wiredHeadphoneConnected"
- "_xpcListener"
- "actionIdentifier"
- "actionWithIdentifier:title:options:"
- "addHAENotificationEvent:"
- "addHAENotificationEvent:completion:"
- "addHAENotificationEvent:error:"
- "addNotificationRequest:withCompletionHandler:"
- "addObject:"
- "addObserver:selector:name:object:"
- "allocWithZone:"
- "appState"
- "applicationProxyForIdentifier:placeholder:"
- "applyVolumeLoweringAtNextSession"
- "applyVolumeReductionToHeadphoneRoutes:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolValue"
- "bundleID"
- "bundleWithPath:"
- "cBy4BcYs5YWtFHbBpt4C6A"
- "categoryIdentifier"
- "categorySampleWithType:value:startDate:endDate:device:metadata:"
- "categoryTypeForIdentifier:"
- "categoryWithIdentifier:actions:intentIdentifiers:options:"
- "centerDelegate"
- "class"
- "code"
- "computeLimitedVolume:event:action:"
- "conformsToProtocol:"
- "connectedWiredDeviceIsHeadphone"
- "connectedWiredDeviceIsHeadphoneWithUUID:"
- "connection"
- "connectionDidInvalidate"
- "containsObject:"
- "content"
- "copy"
- "copyWithZone:"
- "countryCodeWithSource:updatedAtTime:"
- "createHKCategorySampleForEvent:"
- "d"
- "d16@0:8"
- "dateInterval"
- "dealloc"
- "debugDescription"
- "decibelAWeightedSoundPressureLevelUnit"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultManager"
- "defaultWorkspace"
- "delegate"
- "describeSource"
- "description"
- "deviceDataDispositionDidChange"
- "deviceSessionCreated:SessionID:"
- "deviceSessionDestroyed:isWired:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "domain"
- "donateSignalToTipsKit:"
- "doubleValue"
- "duration"
- "effectiveBoolValueForSetting:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endDate"
- "errorWithDomain:code:userInfo:"
- "eventType"
- "f"
- "f32@0:8^{__CFString=}16^{?=^{__CFString}^{__CFString}^{__CFString}}24"
- "f36@0:8f16@20^I28"
- "fetchGeoLocation"
- "fileSystemRepresentationWithPath:"
- "floatValue"
- "forceReadDefaults"
- "getAccessoryInfo:"
- "getAccessoryInfoFromIOAccesoryManager:"
- "getAccessoryInfoFromIOKitDirectly:"
- "getAudioAccessoryConnectionInfo"
- "getAudioAccessoryConnectionInfoWithKey:"
- "getCurrentVolumeForCategory:route:"
- "getDeviceName"
- "getDeviceUID"
- "getEventTypeString"
- "getLiveMonitorTimeWindowInSeconds"
- "getLiveMonitoringThreshold"
- "getPreferenceFor:"
- "getPreferencesFor:"
- "getReduceLoudSoundThreshold"
- "getStats"
- "gqDnklGQnpv5ilgh5uHckw"
- "handleNotificationAction:"
- "hasPrefix:"
- "hash"
- "i16@0:8"
- "immutableDescription"
- "init"
- "initWithBundleID:"
- "initWithBundleIdentifier:"
- "initWithCoder:"
- "initWithContentIdentifier:context:osBuild:userInfo:"
- "initWithDomain:code:userInfo:"
- "initWithEventType:exposureLevel:dateInterval:metadata:"
- "initWithFormat:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceDeviceSerialNumber"
- "interfaceModuleSerialNumber"
- "interfaceWithProtocol:"
- "isAppleWatch"
- "isConnectedUnknownWiredDeviceHeadphone"
- "isCurrentAudioAccessoryHeadphone"
- "isCurrentAudioAccessoryHeadphoneWithKey:"
- "isCurrentProcessMediaserverd"
- "isDeviceHeadphoneJack:"
- "isEUVolumeLimitOn"
- "isEqual:"
- "isEqualToString:"
- "isHAENFeatureEnabled"
- "isHAENFeatureMandatory"
- "isHAENFeatureOptedIn"
- "isHAEOtherDevicesEnabled"
- "isHKWriteEnabled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isReduceLoudSoundEnabled"
- "isRestricted"
- "isRunningCITests"
- "isSKVolumeLimitOn"
- "isUSBCPort"
- "limitVolume:"
- "limitVolumeTo:category:route:actionResult:"
- "listener:shouldAcceptNewConnection:"
- "liveMonitorWindowInSec"
- "liveThresholdInDBA"
- "localizedStringForKey:value:table:"
- "manufacturer"
- "mcc"
- "metadata"
- "migrateKeyEnableHAEHKMeasurement:"
- "modelNumber"
- "mutableCopy"
- "notification"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "openSensitiveURL:withOptions:error:"
- "parentalControlsBlacklistedAppBundleIDs"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personalAudioAccommodationTypes"
- "personalMediaEnabled"
- "playSystemSoundWithEvent:completion:"
- "processIdentifier"
- "processInfo"
- "processMessage:"
- "processName"
- "processStatsForEvent:"
- "processStatsForLocationGating:"
- "q16@0:8"
- "q24@0:8@16"
- "quantityWithUnit:doubleValue:"
- "registerDevice:"
- "release"
- "reloadProductTypeOverride"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllAdapters"
- "removeObjectForKey:"
- "removeObserver:name:object:"
- "removePreferenceFor:"
- "removePreferenceFor:notify:"
- "request"
- "requestWithIdentifier:content:trigger:destinations:"
- "respondsToSelector:"
- "restrictedAppBundleIDs"
- "resume"
- "retain"
- "retainCount"
- "saveHAENotificationEventAsHKCategorySample:"
- "saveNotificationEventToHealthKit:"
- "saveNotificationEventToHealthKit:withDelegate:"
- "saveObject:withCompletion:"
- "secondUnit"
- "self"
- "sendBannerNotificationWithEvent:volumeLoweringAction:"
- "sendEvent:"
- "sendLiveExposureEvent:volumeLoweringAction:"
- "sendNotificationWithExposureLevel:duration:eventType:volumeLoweringAction:"
- "sendSingleMessage:category:type:"
- "sendWeeklyExposureEvent:volumeLoweringAction:"
- "serialNumber"
- "setAlertTopic:"
- "setAudioAccessoryIsConnectedToHeadphones:withKey:name:"
- "setAudioAccessoryIsConnectedToHeadphones:withName:"
- "setBody:"
- "setBundleID:"
- "setCategoryIdentifier:"
- "setDelegate:"
- "setDeviceConnectionState:isConnected:"
- "setDeviceInfo:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNotificationCategories:"
- "setObject:forKey:"
- "setPreferenceFor:value:"
- "setPreferenceFor:value:notify:"
- "setRemoteObjectInterface:"
- "setShouldBackgroundDefaultAction:"
- "setSound:"
- "setSubtitle:"
- "setThreadIdentifier:"
- "setTitle:"
- "setToneIdentifier:"
- "setUserVolumeWithValue:mininum:"
- "setValue:forKey:"
- "setWantsNotificationResponsesDelivered"
- "setWithObject:"
- "setWithObjects:"
- "setupConnection"
- "sharedBehavior"
- "sharedConfiguration"
- "sharedConnection"
- "sharedInstance"
- "softwareVersionEnabled"
- "soundWithAlertType:"
- "sourceDevice"
- "startDate"
- "startNotificationCenterServer"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "surfaceAlertBox"
- "timeIntervalSinceDate:"
- "timestamp"
- "unknownWiredConnectionDidChange:"
- "unknownWiredHeadsetConnectedThroughB204"
- "unsignedIntValue"
- "unsignedLongValue"
- "update"
- "updateAudioAccessoryIsConnectedToHeadphones:"
- "updateAudioAccessoryIsConnectedToHeadphones:WithKey:"
- "updateMXVolumeLimitStatus"
- "updateRLSSettings"
- "updateUserVolumeForVolumeLimit"
- "updateWiredDeviceStatus"
- "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
- "userNotificationCenter:openSettingsForNotification:"
- "userNotificationCenter:willPresentNotification:withCompletionHandler:"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"HAENotificationEvent\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8f16f20"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8^{__CFString=}16^{?=^{__CFString}^{__CFString}^{__CFString}}24"
- "v32@0:8q16@24"
- "v36@0:8@16@24B32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
- "v40@0:8@16@24@?32"
- "v40@0:8d16d24I32I36"
- "v40@0:8q16@24@32"
- "v44@0:8f16^{__CFString=}20^{?=^{__CFString}^{__CFString}^{__CFString}}28^I36"
- "v48@0:8{?=@@@BB}16"
- "valueForKey:"
- "verifyInvariants"
- "volumeActionString:"
- "volumeReductionDelta"
- "wiredDeviceStatusDidChange"
- "wiredHeadphoneConnected:"
- "zone"
- "{?=\"countryCode\"@\"NSString\"\"source\"@\"NSString\"\"disposition\"@\"NSString\"\"featureMandatory\"B\"EUVolumeLimitBehavior\"B}"
- "{?=\"currVolume\"f\"targetVolume\"f\"volumeAction\"I}"
- "{?=@@@BB}16@0:8"
- "{?=ffI}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
