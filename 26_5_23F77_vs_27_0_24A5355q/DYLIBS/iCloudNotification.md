## iCloudNotification

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification`

```diff

-301.23.4.7.0
-  __TEXT.__text: 0x5b1c
-  __TEXT.__auth_stubs: 0x2f0
+301.24.0.19.0
+  __TEXT.__text: 0x5640
   __TEXT.__objc_methlist: 0x5c4
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__cstring: 0x5cb
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__cstring: 0x5bf
   __TEXT.__oslogstring: 0x62d
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x2b0
-  __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x119e
-  __TEXT.__objc_methtype: 0x920
-  __TEXT.__objc_stubs: 0x980
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x650
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x180
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECFA4659-3F11-3F44-9644-7E7D566354C3
-  Functions: 154
-  Symbols:   584
-  CStrings:  367
+  UUID: 509ECE69-5852-3ECF-BFED-2551C9D018E0
+  Functions: 152
+  Symbols:   586
+  CStrings:  120
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __os_feature_enabled_impl
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B40@0:8@16Q24^@32"
- "INDaemonConnection"
- "INDaemonInterface"
- "INDaemonProtocol"
- "INDiagnosticReport"
- "INManagedDefaults"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Quota"
- "Solarium"
- "SwiftUI"
- "T#,R"
- "T@\"NSArray\",C,N,V_pushTopics"
- "T@\"NSDate\",C,N,V_nextHeartbeatDate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_pushEnvironment"
- "T@\"NSString\",C,N,V_pushToken"
- "T@\"NSString\",R,C"
- "TB,N,V_disabled"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "XPCInterface"
- "^{_NSZone=}16@0:8"
- "_buildXPCInterface"
- "_connection"
- "_disabled"
- "_nextHeartbeatDate"
- "_numberingSystem"
- "_pushEnvironment"
- "_pushToken"
- "_pushTopics"
- "_readManagedDefaults"
- "_writeManagedDefaults:"
- "aa_addBasicAuthorizationHeaderWithAccount:preferUsingPassword:"
- "addValue:forHTTPHeaderField:"
- "allHTTPHeaderFields"
- "appLaunchLinkDidPresentForBundleIdentifier:"
- "appLaunchLinkDidPresentForBundleIdentifier:completion:"
- "autorelease"
- "boolValue"
- "calculateExtraQuotaNeededToSyncForAccountWithID:isAccountFull:completion:"
- "class"
- "clearAllRegistrationDigestsWithCompletion:"
- "clearAllRegistrationDigestsWithError:"
- "code"
- "commonHeadersForRequest:withCompletion:"
- "conformsToProtocol:"
- "copy"
- "currentInfo"
- "currentLocale"
- "daemonWithErrorHandler:"
- "dealloc"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "diagnosticReport"
- "diagnosticReportWithCompletion:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "displayDelayedOfferWithContext:completion:"
- "domain"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "fetchAppsSyncingToiCloudDriveForAltDSID:completion:"
- "fetchBackupInfoForAltDSID:completion:"
- "fetchCompletedAndDismissedRecommendationsForAltDSID:configuration:completion:"
- "fetchRecommendationsForAltDSID:completion:"
- "fetchRecommendationsRulesetForAltDSID:completion:"
- "fetchStorageAppsForAltDSID:completion:"
- "fetchStorageByApp:forAltDSID:completion:"
- "fetchStorageSummaryForAltDSID:completion:"
- "getCacheDataForLink:completion:"
- "handleChatterboxURL:completion:"
- "hash"
- "iCloudServerOfferForAccount:options:completion:"
- "iCloudServerOfferForAccountWithID:options:completion:"
- "identifier"
- "ind_addQuotaHeadersForAccount:"
- "ind_addUserAgentString"
- "infoDictionary"
- "init"
- "initWithCoder:"
- "initWithInt:"
- "initWithMachServiceName:options:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNSNumber__"
- "isNSString__"
- "isProxy"
- "localizedDescription"
- "mainBundle"
- "mutableCopy"
- "notifyAMSEngagementAppDidBecomeActiveWithCompletion:"
- "notifyDeviceStorageLevel:completion:"
- "numberWithBool:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeFPItem:notifyURL:completion:"
- "osName"
- "osVersion"
- "performAMSEngagementWithParameters:completion:"
- "performPostPurchaseTeardownWithCompletion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "presentHiddenFreshmintWithContext:completion:"
- "registerAccount:foriCloudNotificationsWithReason:completion:"
- "registerAccount:foriCloudNotificationsWithReason:error:"
- "registerAccountWithID:foriCloudNotificationsWithReason:completion:"
- "registerDeviceForLoggedOutiCloudNotificationsWithReason:completion:"
- "release"
- "remoteFreshmintFlowCompletedWithSuccess:completion:"
- "remoteFreshmintFlowCompletedWithSuccess:error:"
- "remoteObjectProxyWithErrorHandler:"
- "renewCredentialsWithCompletion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "sendStatusForRecommendationsWithAltDSID:configuration:params:completion:"
- "sendStatusForRecommendationsWithAltDSID:configuration:status:recommendationIdentifiers:storageRecovered:completion:"
- "sendTipDismissedNetworkRequestForAltDSID:tip:completion:"
- "sendTipDisplayedNetworkRequestForAltDSID:tip:completion:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDisabled:"
- "setHTTPMethod:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNextHeartbeatDate:"
- "setObject:forKeyedSubscript:"
- "setPushEnvironment:"
- "setPushToken:"
- "setPushTopics:"
- "setRemoteObjectInterface:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKey:"
- "setValue:forManagedDefault:"
- "setWithObjects:"
- "sharedInstance"
- "standardDateFormat:"
- "startDelayedOfferFailsafeActivityWithDelaySecs:completion:"
- "stopDelayedOfferFailsafeActivityWithCompletion:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "syncFPItem:observeItemIDs:notifyURL:completion:"
- "synchronousDaemonWithErrorHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "teardownOffersForAccount:withCompletion:"
- "udid"
- "unregisterAccount:fromiCloudNotificationsWithCompletion:"
- "unregisterAccount:fromiCloudNotificationsWithError:"
- "unregisterAccountWithID:fromiCloudNotificationsWithCompletion:"
- "unregisterDeviceFromLoggedOutiCloudNotificationsWithCompletion:"
- "unregisterDeviceFromLoggedOutiCloudNotificationsWithReason:completion:"
- "updateOfferForAccount:offerId:buttonId:info:completion:"
- "updateOfferForAccountWithID:offerId:buttonId:info:completion:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"INDiagnosticReport\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v28@0:8B16@\"NSError\"20"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v32@0:8@\"ACAccount\"16@?<v@?>24"
- "v32@0:8@\"ICQLink\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"ICQRemoteContext\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"CERuleConfiguration\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"CEServerRecommendations\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ICQAppsSyncingToDrive\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ICQBackupInfo\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ICQCloudStorageApps\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ICQCloudStorageSummary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSURLRequest\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?B@\"NSError\">24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v32@0:8q16@?<v@?B@\"NSError\">24"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"NSNumber\"@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"FPItemID\"16@\"NSURL\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"CERuleConfiguration\"24@?<v@?@\"CEServerRecommendations\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"ICQInlineTip\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"ICQAppCloudStorage\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v48@0:8@\"FPItemID\"16@\"NSArray\"24@\"NSURL\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"CERuleConfiguration\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?B@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSString\"16@\"CERuleConfiguration\"24@\"NSString\"32@\"NSArray\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "valueForManagedDefault:"
- "zone"

```
