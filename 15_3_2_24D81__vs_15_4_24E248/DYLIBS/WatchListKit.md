## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit`

```diff

-850.30.4.0.0
-  __TEXT.__text: 0x66c64
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x63f4
+850.40.40.0.0
+  __TEXT.__text: 0x66a68
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x6a64
   __TEXT.__const: 0x19c
-  __TEXT.__cstring: 0x700c
-  __TEXT.__oslogstring: 0x56c0
-  __TEXT.__gcc_except_tab: 0xef4
-  __TEXT.__unwind_info: 0x1b00
-  __TEXT.__objc_classname: 0x126b
-  __TEXT.__objc_methname: 0xecc1
-  __TEXT.__objc_methtype: 0x19c4
-  __TEXT.__objc_stubs: 0x8c60
+  __TEXT.__cstring: 0x7100
+  __TEXT.__oslogstring: 0x563f
+  __TEXT.__gcc_except_tab: 0xf5c
+  __TEXT.__unwind_info: 0x1bc0
+  __TEXT.__objc_classname: 0x125a
+  __TEXT.__objc_methname: 0xed2b
+  __TEXT.__objc_methtype: 0x19a6
+  __TEXT.__objc_stubs: 0x8ce0
   __DATA_CONST.__got: 0x808
-  __DATA_CONST.__const: 0xbb8
-  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__const: 0xc18
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3280
+  __DATA_CONST.__objc_selrefs: 0x3468
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x4a0
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x618
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x26f0
-  __AUTH_CONST.__cfstring: 0x9a40
-  __AUTH_CONST.__objc_const: 0x11b28
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x27e0
+  __AUTH_CONST.__cfstring: 0x9b40
+  __AUTH_CONST.__objc_const: 0x10e90
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x3520
-  __DATA.__objc_ivar: 0x9ec
+  __AUTH.__objc_data: 0x34d0
+  __DATA.__objc_ivar: 0x9e4
   __DATA.__data: 0x620
-  __DATA.__bss: 0x4e0
+  __DATA.__bss: 0x4d0
   __DATA.__common: 0x5
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4D94752-ABEC-3D32-9889-F9848022CEE4
-  Functions: 2588
-  Symbols:   6887
-  CStrings:  6030
+  UUID: CD630B66-7CFC-3F37-B41E-D4B2A0C75E54
+  Functions: 2665
+  Symbols:   6971
+  CStrings:  6047
 
Symbols:
+ +[NSOperationQueue(WLKAdditions) wlkDefaultConcurrentQueue].cold.1
+ +[NSOperationQueue(WLKAdditions) wlkDefaultQueue].cold.1
+ +[NSUserDefaults(WLKAdditions) wlk_userDefaults].cold.1
+ +[WLKAccountMonitor sharedInstance].cold.1
+ +[WLKAppInstaller defaultAppInstaller].cold.1
+ +[WLKAppLibrary defaultAppLibrary].cold.1
+ +[WLKAsyncOperation keyPathsForValuesAffectingIsCancelled]
+ +[WLKBackgroundUpdateController sharedInstance].cold.1
+ +[WLKBadgingUtilities sharedUtilities].cold.1
+ +[WLKChannelManager defaultChannelManager].cold.1
+ +[WLKChannelUtilities _validiTunesBundles].cold.1
+ +[WLKChannelUtilities sharedInstanceFiltered].cold.1
+ +[WLKChannelUtilities sharedInstance].cold.1
+ +[WLKConfigurationManager sharedInstance].cold.1
+ +[WLKContinuationMetadataBase _contextForString:].cold.1
+ +[WLKExternalMediaContentManager sharedManager].cold.1
+ +[WLKFederatedAnalyticsReporter defaultFederatedAnalyticsReporter].cold.1
+ +[WLKLaunchConfiguration sharedInstance].cold.1
+ +[WLKLocationManager defaultLocationManager].cold.1
+ +[WLKMescal signNetworkRequest:completionHandler:]
+ +[WLKNetworkRequestReauthCoordinator coordinator].cold.1
+ +[WLKNetworkRequestUtilities _createAMSEncoder:account:]
+ +[WLKNetworkRequestUtilities _defaultAppSessionConfiguration].cold.1
+ +[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:completionHandler:]
+ +[WLKNetworkRequestUtilities _sharedCacheSessionConfiguration].cold.1
+ +[WLKNotificationCenter defaultCenter].cold.1
+ +[WLKOfferManager defaultOfferManager].cold.1
+ +[WLKPostPlayAutoPlayManager defaultManager].cold.1
+ +[WLKPrewarming sharedInstance].cold.1
+ +[WLKProcessInfo currentProcessInfo].cold.1
+ +[WLKReachabilityMonitor sharedInstance].cold.1
+ +[WLKRestrictionsObserver sharedObserver].cold.1
+ +[WLKSettingsAMSBagTracker sharedTracker].cold.1
+ +[WLKSettingsCloudUtilities _queue].cold.1
+ +[WLKSettingsLanguageUtilities staticLanguageCodes]
+ +[WLKSettingsStore sharedSettings].cold.1
+ +[WLKSportsFavoriteManager defaultManager].cold.1
+ +[WLKStoredConfigurationManager sharedInstance].cold.1
+ +[WLKSubscriptionStore sharedInstance].cold.1
+ +[WLKSystemPreferencesStore sharedPreferences].cold.1
+ +[WLKURLResponseDecoder logNetworkHeaders:identifier:].cold.1
+ +[WLKURLSessionManager sharedInstance].cold.1
+ +[WLKUpNextDeltaStore sharedInstance].cold.1
+ -[NSString(WLKAdditions) wlk_stringByAppendingPathComponents:].cold.1
+ -[WLKAppSettings _statusStrings].cold.1
+ -[WLKAsyncOperation _finish]
+ -[WLKBadgingUtilities _notificationCenter].cold.1
+ -[WLKNetworkRequestOperation _executeRequest]
+ -[WLKNetworkRequestOperation amsUrlResponse]
+ -[WLKNetworkRequestOperation configureSession].cold.1
+ -[WLKNetworkRequestOperation configureSession].cold.2
+ -[WLKNetworkRequestOperation networkActivity]
+ -[WLKNetworkRequestOperation networkLabel]
+ -[WLKNetworkRequestOperation setAmsUrlResponse:]
+ -[WLKNetworkRequestOperation setNetworkActivity:]
+ -[WLKNetworkRequestOperation setNetworkLabel:]
+ -[WLKNetworkRequestOperation(ResponseHeaders) httpHeaderResponseDate].cold.1
+ -[WLKPlaybackSummary initWithCoder:].cold.1
+ -[WLKStoreOfferPeriod _offerPeriodForString:].cold.1
+ -[WLKUserEnvironment _entitlementsQuery].cold.1
+ -[WLKUserEnvironment isRunningInTVAppExtension]
+ -[WLKUserEnvironment isRunningInTVExtension]
+ -[WLKUserEnvironment tvExtensionBundleIDs]
+ GCC_except_table13
+ OBJC_IVAR_$_WLKNetworkRequestOperation._amsUrlResponse
+ OBJC_IVAR_$_WLKNetworkRequestOperation._networkActivity
+ OBJC_IVAR_$_WLKNetworkRequestOperation._networkLabel
+ WLKAppVisibilityLogObject.cold.1
+ WLKCurrentAPIVersion.cold.1
+ WLKCurrentProtocolVersion.cold.1
+ WLKDefaultSupportPath.cold.1
+ WLKIgnoreHTTPCacheOverride.cold.1
+ WLKIsDaemon.cold.1
+ WLKIsNewsApp.cold.1
+ WLKIsRunningTest.cold.1
+ WLKIsSandboxed.cold.1
+ WLKIsTVApp.cold.1
+ WLKIsTool.cold.1
+ WLKIsWatchlisttool.cold.1
+ WLKNetworkSignpostLogObject.cold.1
+ WLKNetworkingLogObject.cold.1
+ WLKPlaybackTrackingLogObject.cold.1
+ WLKPlistClasses.cold.1
+ WLKPushNotificationsLogObject.cold.1
+ WLKRetryOnBackgroundTimeOutJSOverride.cold.1
+ WLKShouldRunInProcess.cold.1
+ WLKSiriActionsLogObject.cold.1
+ WLKStartupSignpostLogObject.cold.1
+ WLKSubscriptionSyncLogObject.cold.1
+ WLKSystemLogObject.cold.1
+ _TVAppExtensionBundleID
+ _TVProductPageExtensionBundleID
+ __101+[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:completionHandler:]_block_invoke.cold.1
+ __159+[WLKConfigurationRequest fetchWithOptions:cachePolicy:wlkCachePolicy:extendedCacheExpireDuration:sessionConfiguration:queryParameters:fileStorage:completion:]_block_invoke.7
+ __159+[WLKConfigurationRequest fetchWithOptions:cachePolicy:wlkCachePolicy:extendedCacheExpireDuration:sessionConfiguration:queryParameters:fileStorage:completion:]_block_invoke.8
+ __45-[WLKNetworkRequestOperation _executeRequest]_block_invoke.33
+ __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.109
+ __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.109.cold.1
+ __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.113
+ __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.114
+ __84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke_2.cold.1
+ __98+[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:completion:]_block_invoke.14
+ __98+[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:completion:]_block_invoke_2.16
+ __WLKShouldRunInProcess_block_invoke.cold.1
+ __WLKUserEnvironmentPlatformCompanion
+ __WLKUserEnvironmentPlatformPadExtension
+ __WLKUserEnvironmentPlatformPhoneExtension
+ ___101+[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:completionHandler:]_block_invoke
+ ___45-[WLKNetworkRequestOperation _executeRequest]_block_invoke
+ ___45-[WLKNetworkRequestOperation _executeRequest]_block_invoke_2
+ ___50+[WLKMescal signNetworkRequest:completionHandler:]_block_invoke
+ ___98+[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:completion:]_block_invoke_2
+ ___block_descriptor_32_e30_v16?0"NSURLSessionDataTask"8l
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_48_e8_32s40w_e35_v24?0"AMSURLRequest"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"AMSURLRequest"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48s56bs_e59_v32?0"AMSURLRequestEncoder"8"NSURLRequest"16"NSError"24l
+ ___block_descriptor_72_e8_32s40s48bs56r_e20_v20?0B8"NSError"12l
+ __block_literal_global.29
+ __block_literal_global.33
+ _objc_msgSend$_createAMSEncoder:account:
+ _objc_msgSend$_executeRequest
+ _objc_msgSend$_prepareEncoder:account:sessionConfiguration:options:completionHandler:
+ _objc_msgSend$isRunningInTVAppExtension
+ _objc_msgSend$isRunningInTVExtension
+ _objc_msgSend$networkActivity
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$setAmsUrlResponse:
+ _objc_msgSend$signNetworkRequest:completionHandler:
+ _objc_msgSend$signaturePromiseFromData:type:bag:
+ _objc_msgSend$staticLanguageCodes
+ _objc_msgSend$taskInterval
+ _objc_msgSend$tvExtensionBundleIDs
- +[WLKMescal signNetworkRequest:error:]
- +[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:error:]
- +[WLKNetworkRequestUtilities _prepareEncoder:account:sessionConfiguration:options:error:].cold.1
- +[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:activity:completion:]
- -[WLKMetricsActivity .cxx_destruct]
- -[WLKMetricsActivity activity]
- -[WLKMetricsActivity finish:]
- -[WLKMetricsActivity finish:].cold.1
- -[WLKMetricsActivity finish:].cold.2
- -[WLKMetricsActivity initWithLabel:]
- -[WLKMetricsActivity label]
- -[WLKNetworkRequestOperation initWithURLRequest:options:activity:]
- -[WLKNetworkRequestOperation nwactivity]
- -[WLKNetworkRequestOperation setNwactivity:]
- OBJC_IVAR_$_WLKAsyncOperation._cancelled
- OBJC_IVAR_$_WLKAsyncOperation._lock
- OBJC_IVAR_$_WLKMetricsActivity._activity
- OBJC_IVAR_$_WLKMetricsActivity._label
- OBJC_IVAR_$_WLKNetworkRequestOperation._nwactivity
- _OBJC_CLASS_$_WLKMetricsActivity
- _OBJC_METACLASS_$_WLKMetricsActivity
- __159+[WLKConfigurationRequest fetchWithOptions:cachePolicy:wlkCachePolicy:extendedCacheExpireDuration:sessionConfiguration:queryParameters:fileStorage:completion:]_block_invoke.10
- __159+[WLKConfigurationRequest fetchWithOptions:cachePolicy:wlkCachePolicy:extendedCacheExpireDuration:sessionConfiguration:queryParameters:fileStorage:completion:]_block_invoke.9
- __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.106
- __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.106.cold.1
- __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.110
- __50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.111
- __50-[WLKNetworkRequestOperation _startNetworkRequest]_block_invoke.32
- __OBJC_$_INSTANCE_METHODS_WLKMetricsActivity
- __OBJC_$_INSTANCE_VARIABLES_WLKMetricsActivity
- __OBJC_$_PROP_LIST_WLKMetricsActivity
- __OBJC_CLASS_RO_$_WLKMetricsActivity
- __OBJC_METACLASS_RO_$_WLKMetricsActivity
- ___107+[WLKNetworkRequestUtilities startNetworkRequest:account:sessionConfiguration:options:activity:completion:]_block_invoke
- ___157+[WLKURLRequestProperties requestPropertiesWithEndpoint:queryParameters:httpMethod:httpBody:headers:caller:timeout:apiVersion:options:clientProtocolVersion:]_block_invoke
- ___block_descriptor_64_e8_32s40s48bs56r_e34_v24?0"AMSURLResult"8"NSError"16l
- __block_literal_global.433
- _nw_activity_activate
- _nw_activity_complete_with_reason
- _nw_activity_complete_with_reason_and_underlying_error
- _nw_activity_create
- _nw_activity_is_activated
- _nw_activity_is_complete
- _objc_msgSend$_prepareEncoder:account:sessionConfiguration:options:error:
- _objc_msgSend$activity
- _objc_msgSend$dataTaskPromiseWithRequest:activity:
- _objc_msgSend$dataTaskWithRequest:completionHandler:
- _objc_msgSend$finish:
- _objc_msgSend$nwactivity
- _objc_msgSend$resultWithError:
- _objc_msgSend$signNetworkRequest:error:
- _objc_msgSend$signatureFromData:type:bag:error:
- requestPropertiesWithEndpoint:queryParameters:httpMethod:httpBody:headers:caller:timeout:apiVersion:options:clientProtocolVersion:.migratedEndpoints
- requestPropertiesWithEndpoint:queryParameters:httpMethod:httpBody:headers:caller:timeout:apiVersion:options:clientProtocolVersion:.once
CStrings:
+ "@\"AMSURLResult\""
+ "@32@0:8q16@24"
+ "A"
+ "T@\"AMSURLResult\",&,N,V_amsUrlResponse"
+ "T@\"NSNumber\",&,N,V_networkLabel"
+ "T@\"NSObject<OS_nw_activity>\",&,N,V_networkActivity"
+ "T@\"NSSet\",R,N"
+ "WLKConfigurationRequest - Configuration request is completed"
+ "WLKNetworkRequestOperation - Request status: %lu elapsed time: %.5f id: %@ ck:%@ url: %@ %@ %@ %f"
+ "_amsUrlResponse"
+ "_createAMSEncoder:account:"
+ "_executeRequest"
+ "_networkActivity"
+ "_networkLabel"
+ "_prepareEncoder:account:sessionConfiguration:options:completionHandler:"
+ "amsUrlResponse"
+ "com.apple.VideosUI.TVAppExtension"
+ "com.apple.VideosUI.TVProductPageExtension"
+ "iPad-extension"
+ "iPhone-extension"
+ "isRunningInTVAppExtension"
+ "isRunningInTVExtension"
+ "keyPathsForValuesAffectingIsCancelled"
+ "li"
+ "networkActivity"
+ "networkLabel"
+ "resultWithCompletion:"
+ "setAmsUrlResponse:"
+ "setNetworkActivity:"
+ "setNetworkLabel:"
+ "signNetworkRequest:completionHandler:"
+ "signaturePromiseFromData:type:bag:"
+ "staticLanguageCodes"
+ "taskInterval"
+ "tvExtensionBundleIDs"
+ "tvjs"
+ "v24@?0@\"AMSURLRequest\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@?0@\"AMSURLRequestEncoder\"8@\"NSURLRequest\"16@\"NSError\"24"
+ "vision-companion"
+ "{?=\"isReady\"B\"isCancelled\"B\"isExecuting\"B\"isFinished\"B}"
- "@\"WLKMetricsActivity\""
- "@20@0:8I16"
- "@40@0:8@16q24@32"
- "@56@0:8@16@24@32q40^@48"
- "B32@0:8@16^@24"
- "T@\"NSObject<OS_nw_activity>\",R,V_activity"
- "T@\"WLKMetricsActivity\",&,N,V_nwactivity"
- "TI,R,V_label"
- "The -start method may only be called once."
- "WLKAsyncOperation - operation already executing."
- "WLKAsyncOperation - operation was cancelled, skip"
- "WLKMetricsActivity"
- "WLKMetricsActivity - activity already completed."
- "WLKMetricsActivity - activity not activated."
- "WLKNetworkRequestOperation - Request status: %lu elapsed time: %.5f id: %@ ck:%@ url: %@ %@ %@"
- "_activity"
- "_cancelled"
- "_label"
- "_nwactivity"
- "_prepareEncoder:account:sessionConfiguration:options:error:"
- "activity"
- "dataTaskPromiseWithRequest:activity:"
- "dataTaskWithRequest:completionHandler:"
- "finish:"
- "initWithLabel:"
- "initWithURLRequest:options:activity:"
- "label"
- "li-CG"
- "nwactivity"
- "resultWithError:"
- "setNwactivity:"
- "signNetworkRequest:error:"
- "signatureFromData:type:bag:error:"
- "startNetworkRequest:account:sessionConfiguration:options:activity:completion:"
- "v64@0:8@16@24@32q40@48@?56"

```
