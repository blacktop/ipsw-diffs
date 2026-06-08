## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-514.120.2.0.0
-  __TEXT.__text: 0x30fdc
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x45c
-  __TEXT.__const: 0x210
-  __TEXT.__oslogstring: 0x594d
-  __TEXT.__gcc_except_tab: 0x210
-  __TEXT.__cstring: 0x2099
+538.0.0.0.1
+  __TEXT.__text: 0x2ffa8
+  __TEXT.__objc_methlist: 0x46c
+  __TEXT.__const: 0x220
+  __TEXT.__oslogstring: 0x5c28
+  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__cstring: 0x228e
   __TEXT.__unwind_info: 0x938
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0xca9
-  __TEXT.__objc_methtype: 0x5a9
-  __TEXT.__objc_stubs: 0xae0
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xaa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xb10
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb08
-  __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x21e0
-  __AUTH_CONST.__objc_const: 0x5d0
+  __DATA_CONST.__got: 0x3c8
+  __AUTH_CONST.__const: 0x7c8
+  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__objc_const: 0x5d8
+  __AUTH_CONST.__auth_got: 0xb20
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x2e1
-  __DATA.__bss: 0xb0
+  __DATA.__data: 0x2d1
+  __DATA.__bss: 0xd0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__bss: 0x2a8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B54BAC9D-FD9A-3091-B49F-2584CD66A154
-  Functions: 764
-  Symbols:   2365
-  CStrings:  1599
+  UUID: 7CA7EE8B-2B93-3617-B6B9-FC62DBE7091D
+  Functions: 772
+  Symbols:   2409
+  CStrings:  1436
 
Symbols:
+ _BBMonitorNotificationCancel
+ _BBMonitorNotificationPost
+ _BBMonitorNotificationResponse
+ _BBMonitorPromptUser
+ _CNManageCaptiveThreadPriority
+ _CNManageCaptiveThreadPriority.s_original_qos_class
+ _CNManageCaptiveThreadPriority.s_qos_boosted
+ _CNManageCaptiveThreadPriority.s_qos_restored
+ _CNSServerShowBBMonitorPrompt
+ _MGCopyAnswer
+ _OBJC_CLASS_$_CUUserNotificationSession
+ _OBJC_CLASS_$_NSBundle
+ _S_prompting_banner
+ _S_prompting_bb
+ _S_response_context
+ _S_response_func
+ _S_session
+ __XShowBBMonitorPrompt
+ ___BBMonitorNotificationResponse_block_invoke
+ ___block_descriptor_32_e20_v20?0i8"NSError"12l
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.60
+ ___block_literal_global.58
+ ___block_literal_global.62
+ ___setButtons_block_invoke
+ ___setButtons_block_invoke.56
+ ___setButtons_block_invoke.59
+ __handleIPv6OnlyEvaluationFailure
+ _info_get_value
+ _kSymptomManagedEventKeyBBHAONRNF
+ _kSymptomManagedEventKeyBBHProbeTimeout
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$activate
+ _objc_msgSend$addActionWithIdentifier:title:flags:handler:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$setActionHandler:
+ _objc_msgSend$setBodyKey:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setCategoryID:
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setHeader:
+ _objc_msgSend$setIconSystemName:
+ _objc_msgSend$setInterruptionLevel:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _pthread_set_qos_class_self_np
+ _qos_class_self
- _BBMonitorCancel
- _BBMonitorUserResponse
- _CFBundleCopyBundleURL
- _CFUserNotificationCancel
- _CFUserNotificationCreate
- _CFUserNotificationCreateRunLoopSource
- _CaptiveSymptomFramework
- ___block_descriptor_tmp.17
- __handleBuiltinEvaluationFailureForCarPlayNetwork
- _add_localized_string
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
- _kCFUserNotificationLocalizationURLKey
- _objc_retain_x26
CStrings:
+ " and IC enabled"
+ "%s: cancelled"
+ "%s: couldn't determine device name"
+ "%s: error: %@"
+ "%s: internal error, banner provides no callback"
+ "%s: posted %s"
+ "%s: timeout"
+ "%s: unrecognized action %d"
+ "%s: user chose Stay on Wi-Fi"
+ "%s: user chose Use Cellular"
+ "%s: user dismissed"
+ "%s: user tapped notification"
+ "/System/Library/Frameworks/UIKit.framework"
+ "BBMonitor(%s): IC enabled, using cellular data"
+ "BBMonitor(%s): IC is %s"
+ "BBMonitor(%s): ignoring IC change"
+ "BBMonitor(%s): remediation is %srequired"
+ "BBMonitor(%s): waiting until the next probe interval"
+ "BBMonitor: '%s' %g is too long, using max %g"
+ "BBMonitor: '%s' %g is too short, using min %g"
+ "BBMonitor: IC is %s"
+ "BBMonitor: asking user to choose Cellular or Remain On WiFi"
+ "BBMonitor: detected broken%s%s"
+ "BBMonitor: failed to post notification"
+ "BBMonitor: informing user that WiFi is broken"
+ "BBMonitor: using specified '%s' = %g"
+ "BBMonitorNotification"
+ "BBMonitorNotificationResponse: stale response"
+ "BROKEN_BACKHAUL"
+ "BROKEN_BACKHAUL_BANNER"
+ "BROKEN_BACKHAUL_BANNER_BODY_FORMAT"
+ "BROKEN_BACKHAUL_BANNER_BODY_FORMAT_CH"
+ "BROKEN_BACKHAUL_BANNER_TITLE"
+ "BROKEN_BACKHAUL_BANNER_TITLE_CH"
+ "BROKEN_BACKHAUL_BODY_FORMAT"
+ "BROKEN_BACKHAUL_BODY_FORMAT_CH"
+ "BROKEN_BACKHAUL_DEFAULT_BUTTON_CH"
+ "BROKEN_BACKHAUL_TITLE"
+ "CaptiveNetworkSupport-538.0.0.0.1"
+ "CarPlay callback received an unactionable mode"
+ "CarPlay mode change was already handled"
+ "CarPlayAndUserConfigured"
+ "CarPlayOnly"
+ "DeviceClass"
+ "Hotspot20"
+ "STAY_ON_WIFI"
+ "USE_CELLULAR"
+ "UserConfigured"
+ "WAC"
+ "banner"
+ "broken backhaul detection now idle"
+ "com.apple.BrokenBackhaulNotification"
+ "dialog"
+ "failed to boost the priority of the captive thread"
+ "failed to restore the priority of the captive thread"
+ "iPhone"
+ "network type changed to %@"
+ "now "
+ "remediation is not required"
+ "successfully boosted the priority of the captive thread"
+ "successfully restored the priority of the captive thread"
+ "v20@?0i8@\"NSError\"12"
+ "wifi.exclamationmark"
- "#16@0:8"
- ".cxx_destruct"
- "@\"CoreTelephonyClient\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16i24"
- "BBMonitor(%s): waiting until next probe interval"
- "BBMonitor: detected broken%s"
- "BBMonitor: failed to create CFUserNotification"
- "BBMonitor: prompting user, waiting for response"
- "BBMonitorUserResponse: mismatch cfun"
- "BBMonitorUserResponse: why S_bb NULL?"
- "BROKEN_BACKHAUL_HEADER_FORMAT"
- "BROKEN_BACKHAUL_HEADER_FORMAT_CH"
- "BROKEN_BACKHAUL_MESSAGE"
- "BROKEN_BACKHAUL_MESSAGE_CH"
- "CNHotspotSessionManager"
- "Callback received an invalid CarPlay mode %d"
- "CaptiveNetworkSupport-514.120.2"
- "CarPlay mode change to %d was already handled"
- "CarPlay mode change was notified with %u"
- "CarrierSettingsStatusIndicator"
- "CoreTelephonyClientCarrierBundleDelegate"
- "CoreTelephonyClientDataDelegate"
- "EUIMID"
- "MEID"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CoreTelephonyClient\",&,N,V_coreTelephonyClient"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "T^?,V_callback"
- "T^?,V_handler"
- "T^v,N,V_hotspotSession"
- "T^v,V_context"
- "T^{__CFRunLoop=},V_runloop"
- "T^{__CFString=},V_runloopMode"
- "Ti,V_currentSessionStatus"
- "UUIDString"
- "Vv16@0:8"
- "^?"
- "^?16@0:8"
- "^v"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoop=}"
- "^{__CFRunLoop=}16@0:8"
- "^{__CFString=}"
- "^{__CFString=}16@0:8"
- "_callback"
- "_context"
- "_coreTelephonyClient"
- "_currentSessionStatus"
- "_handler"
- "_hotspotSession"
- "_queue"
- "_runloop"
- "_runloopMode"
- "acquireWithError:"
- "anbrActivationState:enabled:"
- "anbrBitrateRecommendation:bitrate:direction:"
- "application"
- "applicationProxyForIdentifier:"
- "applicationType"
- "array"
- "arrayWithObjects:count:"
- "attributeWithDomain:name:"
- "authenticationProviderBundleIdentifier"
- "autorelease"
- "boolValue"
- "bundle"
- "bundleIdentifier"
- "bundleInfoValueForKey:"
- "bundleRecordForAuditToken:error:"
- "callback"
- "carrierBundleChange:"
- "class"
- "code"
- "conformsToProtocol:"
- "connectionActivationError:connection:error:"
- "connectionAvailability:availableConnections:"
- "connectionStateChanged:connection:dataConnectionStatusInfo:"
- "context"
- "continuing to evaluate CarPlay Wi-Fi"
- "copyCarrierBundleValue:key:bundleType:completion:"
- "copyMobileEquipmentInfo:"
- "coreTelephonyClient"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createConnection"
- "currentDataServiceDescriptorChanged:"
- "currentDataSimChanged:"
- "currentSessionStatus"
- "dataRoamingSettingsChanged:status:"
- "dataSettingsChanged:"
- "dataStatus:dataStatusInfo:"
- "dealloc"
- "debugDescription"
- "defaultBundleChange"
- "defaultWorkspace"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateBundlesOfType:block:"
- "enumerateObjectsUsingBlock:"
- "evaluatedSSIDs"
- "evaluationProviderBundleIdentifier"
- "eventTypeString:"
- "extensionPointRecord"
- "getRatSelection:completion:"
- "getSIMStatus:error:"
- "getSubscriptionInfoWithError:"
- "getUUIDBytes:"
- "handleForIdentifier:error:"
- "handler"
- "hash"
- "hotspot"
- "hotspotSession"
- "hotspotSessionQueue"
- "i"
- "i16@0:8"
- "identifier"
- "identifierWithPid:"
- "init"
- "initWithBundleType:"
- "initWithDictionary:"
- "initWithExplanation:target:attributes:"
- "initWithQueue:"
- "initWithUUIDString:"
- "intValue"
- "internetConnectionActivationError:"
- "internetConnectionAvailability:"
- "internetConnectionStateChanged:"
- "internetDataStatus:"
- "internetDataStatusBasic:"
- "intersectOrderedSet:"
- "invalidate"
- "isEnabled"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "loadConfigurationsWithCompletionQueue:handler:"
- "localizedNameForContext:"
- "meInfoList"
- "nrSliceAppStateChanged:status:trafficDescriptors:"
- "nrSlicedRunningAppStateChanged:"
- "objectForKey:"
- "openApplication:withOptions:completion:"
- "operatorBundleChange:"
- "optionsWithDictionary:"
- "orderedSetWithArray:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneNumber"
- "preferredDataServiceDescriptorChanged:"
- "preferredDataSimChanged:"
- "probe server is reachable again"
- "queue"
- "regDataModeChanged:dataMode:"
- "release"
- "respondsToSelector:"
- "response flags 0x%lx"
- "retain"
- "retainCount"
- "runloop"
- "runloopMode"
- "scheduleRequestCompletionHandler:"
- "self"
- "serviceDisconnection:status:"
- "servingNetworkChanged:"
- "sessionStatusString:"
- "sessionTypeString:"
- "setCallback:"
- "setContext:"
- "setCoreTelephonyClient:"
- "setCurrentSessionStatus:"
- "setDelegate:"
- "setHandler:"
- "setHotspotSession:"
- "setObject:forKeyedSubscript:"
- "setQueue:"
- "setRunloop:"
- "setRunloopMode:"
- "sharedManagerForAllUsers"
- "slotID"
- "slotId"
- "startWithConfigurationID:sessionType:"
- "stop"
- "subscriptions"
- "superclass"
- "targetWithPid:"
- "tetheringStatus:"
- "tetheringStatus:connectionType:"
- "userDataPreferred"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CTDataConnectionStatus\"16"
- "v24@0:8@\"CTDataSettings\"16"
- "v24@0:8@\"CTDataStatus\"16"
- "v24@0:8@\"CTDataStatusBasic\"16"
- "v24@0:8@\"CTServiceDescriptor\"16"
- "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
- "v24@0:8@\"CTTetheringStatus\"16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@0:8@16"
- "v24@0:8^?16"
- "v24@0:8^v16"
- "v24@0:8^{__CFRunLoop=}16"
- "v24@0:8^{__CFString=}16"
- "v28@0:8@\"CTServiceDescriptor\"16B24"
- "v28@0:8@\"CTTetheringStatus\"16i24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
- "v32@0:8@16@24"
- "v32@0:8@16i24i28"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
- "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@28"
- "v36@0:8@16i24@28"
- "zone"

```
