## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount`

```diff

-1067.0.0.0.0
-  __TEXT.__text: 0x277650
-  __TEXT.__objc_methlist: 0xb354
-  __TEXT.__cstring: 0x104d1
+1069.125.4.0.0
+  __TEXT.__text: 0x277e8c
+  __TEXT.__objc_methlist: 0xb314
+  __TEXT.__cstring: 0x10581
   __TEXT.__const: 0x484f0
+  __TEXT.__oslogstring: 0x127dd
   __TEXT.__gcc_except_tab: 0x1aa8
-  __TEXT.__oslogstring: 0x126ad
   __TEXT.__dlopen_cstrs: 0x2d3
   __TEXT.__swift5_typeref: 0x336a
   __TEXT.__constg_swiftt: 0x26c4

   __TEXT.__swift_as_ret: 0x244
   __TEXT.__swift_as_cont: 0x450
   __TEXT.__swift5_capture: 0x7b8
-  __TEXT.__unwind_info: 0x7b20
+  __TEXT.__unwind_info: 0x7b18
   __TEXT.__eh_frame: 0x6938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2670
-  __DATA_CONST.__objc_classlist: 0x888
+  __DATA_CONST.__const: 0x2690
+  __DATA_CONST.__objc_classlist: 0x898
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50f8
+  __DATA_CONST.__objc_selrefs: 0x50b8
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x580
+  __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x1020
+  __DATA_CONST.__got: 0x1038
   __AUTH_CONST.__const: 0x10990
-  __AUTH_CONST.__cfstring: 0xcec0
-  __AUTH_CONST.__objc_const: 0x26218
+  __AUTH_CONST.__cfstring: 0xcfe0
+  __AUTH_CONST.__objc_const: 0x26360
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x12c8
-  __AUTH.__objc_data: 0xfd0
+  __AUTH.__objc_data: 0x1070
   __AUTH.__data: 0xb60
-  __DATA.__objc_ivar: 0xba4
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0x3fb8
   __DATA.__common: 0xa60
   __DATA_DIRTY.__objc_data: 0x4bd0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8772
-  Symbols:   11427
-  CStrings:  3506
+  Functions: 8770
+  Symbols:   11447
+  CStrings:  3521
 
Symbols:
+ +[AACloudKitDevicesListRequest urlBagKey]
+ +[AACloudKitMigrationStateRequest urlBagKey]
+ +[AACloudKitStartMigrationRequest urlBagKey]
+ +[AAFMIPAuthenticateRequest urlBagKey]
+ +[AAFamilyDetailsRequest urlBagKey]
+ +[AAFamilyEligibilityRequest urlBagKey]
+ +[AAFeatureFlags isAAAFoundationBackoffEnabled]
+ +[AAGenericTermsUIRequest urlBagKey]
+ +[AALoginDelegatesRequest urlBagKey]
+ +[AAMyPhotoRequest urlBagKey]
+ +[AAPasswordSecurityUIRequest urlBagKey]
+ +[AAPaymentSummaryRequest urlBagKey]
+ +[AAPaymentUIRequest urlBagKey]
+ +[AAPersonalInfoUIRequest urlBagKey]
+ +[AAPreferences isForceServerBackoffEnabled]
+ +[AAPreferences setForceServerBackoffEnabled:]
+ +[AARequest urlBagKey]
+ +[AASecondaryAuthenticationRequest urlBagKey]
+ +[AAServerBackoffHelper sharedHelper]
+ +[AAUpdateAccountUIRequest urlBagKey]
+ +[AAUpdateMyPhotoRequest urlBagKey]
+ +[AAUpdateNameRequest urlBagKey]
+ +[ATVHighSecurityAccountDeviceList urlBagKey]
+ +[ATVHighSecurityAccountSendCode urlBagKey]
+ +[ATVHighSecurityAccountVerifyCode urlBagKey]
+ +[_AAURLSessionOperation operationWithURLBagKey:completion:]
+ -[AACustodianUpdateRequestContext isSyncAction]
+ -[AACustodianUpdateRequestContext setIsSyncAction:]
+ -[AADataclassManager _appStateForDataclass:bundleID:]
+ -[AALocalContactInfo initWithHandle:contact:source:]
+ -[AALocalContactInfo intelligenceScore]
+ -[AALocalContactInfo setIntelligenceScore:]
+ -[AALocalContactInfo setSource:]
+ -[AALocalContactInfo source]
+ -[AALoginDelegatesRequest initWithAccount:proxiedAppBundleID:parameters:]
+ -[AARequest clientBundleID]
+ -[AARequest proxiedAppBundleID]
+ -[AARequest setClientBundleID:]
+ -[AARequest setProxiedAppBundleID:]
+ -[AAServerBackoffHelper .cxx_destruct]
+ -[AAServerBackoffHelper appendBackoffHeadersToRequest:]
+ -[AAServerBackoffHelper initWithBackoffController:]
+ -[AAServerBackoffHelper init]
+ -[AAServerBackoffHelper processBackoffInfoFromHeaderFields:]
+ -[AAServerBackoffHelper shouldBackoffRequest:urlBagKey:]
+ -[AAURLConfiguration urlStringForKey:]
+ -[AAURLSession _enqueueRequest:withFlowID:urlBagKey:completion:]
+ -[AAURLSession _sessionQueue_enqueueTask:urlBagKey:completion:]
+ -[AAURLSession dataTaskWithRequest:withFlowID:urlBagKey:completion:]
+ -[AAURLSession serverBackoffHelper]
+ -[AAURLSession setServerBackoffHelper:]
+ -[_AAServerBackoffThrottledTask cancel]
+ -[_AAServerBackoffThrottledTask copyWithZone:]
+ -[_AAServerBackoffThrottledTask resume]
+ -[_AAServerBackoffThrottledTask suspend]
+ -[_AAURLSessionOperation initWithURLBagKey:completion:]
+ -[_AAURLSessionOperation urlBagKey]
+ GCC_except_table125
+ GCC_except_table36
+ OBJC_IVAR_$_AACustodianUpdateRequestContext._isSyncAction
+ OBJC_IVAR_$_AALocalContactInfo._intelligenceScore
+ OBJC_IVAR_$_AALocalContactInfo._source
+ OBJC_IVAR_$_AARequest._clientBundleID
+ OBJC_IVAR_$_AARequest._proxiedAppBundleID
+ OBJC_IVAR_$_AAServerBackoffHelper._backoffController
+ OBJC_IVAR_$_AAURLSession._serverBackoffHelper
+ OBJC_IVAR_$__AAURLSessionOperation._urlBagKey
+ _AAServerBackoffClientBundleIDHeaderKey
+ _AAServerBackoffForceHeaderKey
+ _AAServerBackoffProxiedAppBundleIDHeaderKey
+ _OBJC_CLASS_$_AAFServerBackoffController
+ _OBJC_CLASS_$_AAServerBackoffHelper
+ _OBJC_CLASS_$__AAServerBackoffThrottledTask
+ _OBJC_METACLASS_$_AAServerBackoffHelper
+ _OBJC_METACLASS_$__AAServerBackoffThrottledTask
+ __64-[AAURLSession _enqueueRequest:withFlowID:urlBagKey:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_AAPasswordSecurityUIRequest
+ __OBJC_$_CLASS_METHODS_AAPaymentUIRequest
+ __OBJC_$_CLASS_METHODS_AAPersonalInfoUIRequest
+ __OBJC_$_CLASS_METHODS_AAServerBackoffHelper
+ __OBJC_$_CLASS_METHODS_AAUpdateAccountUIRequest
+ __OBJC_$_CLASS_METHODS_AAUpdateMyPhotoRequest
+ __OBJC_$_INSTANCE_METHODS_AAServerBackoffHelper
+ __OBJC_$_INSTANCE_METHODS__AAServerBackoffThrottledTask
+ __OBJC_$_INSTANCE_VARIABLES_AAServerBackoffHelper
+ __OBJC_$_PROP_LIST__AAServerBackoffThrottledTask
+ __OBJC_CLASS_PROTOCOLS_$__AAServerBackoffThrottledTask
+ __OBJC_CLASS_RO_$_AAServerBackoffHelper
+ __OBJC_CLASS_RO_$__AAServerBackoffThrottledTask
+ __OBJC_METACLASS_RO_$_AAServerBackoffHelper
+ __OBJC_METACLASS_RO_$__AAServerBackoffThrottledTask
+ ___37+[AAServerBackoffHelper sharedHelper]_block_invoke
+ ___64-[AAURLSession _enqueueRequest:withFlowID:urlBagKey:completion:]_block_invoke
+ _kAAProtocolPrefForceServerBackoffKey
+ _objc_msgSend$_appStateForDataclass:bundleID:
+ _objc_msgSend$_enqueueRequest:withFlowID:urlBagKey:completion:
+ _objc_msgSend$_sessionQueue_enqueueTask:urlBagKey:completion:
+ _objc_msgSend$appendBackoffHeadersToRequest:
+ _objc_msgSend$appendBackoffHeadersToRequest:clientBundleID:proxiedAppBundleID:
+ _objc_msgSend$dataTaskWithRequest:withFlowID:urlBagKey:completion:
+ _objc_msgSend$initWithAccount:proxiedAppBundleID:parameters:
+ _objc_msgSend$initWithAppServerName:userDefaults:
+ _objc_msgSend$initWithBackoffController:
+ _objc_msgSend$initWithURLBagKey:completion:
+ _objc_msgSend$isAAAFoundationBackoffEnabled
+ _objc_msgSend$isForceServerBackoffEnabled
+ _objc_msgSend$operationWithURLBagKey:completion:
+ _objc_msgSend$processBackoffInfoFrom:
+ _objc_msgSend$processBackoffInfoFromHeaderFields:
+ _objc_msgSend$serverBackoffHelper
+ _objc_msgSend$setProxiedAppBundleID:
+ _objc_msgSend$sharedHelper
+ _objc_msgSend$shouldBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:
+ _objc_msgSend$shouldBackoffRequest:urlBagKey:
+ _objc_msgSend$urlBagKey
+ _objc_msgSend$urlStringForKey:
+ sharedHelper.onceToken
+ sharedHelper.sharedHelper
- +[_AAURLSessionOperation operationWithCompletion:]
- -[AACloudKitDevicesListRequest urlString]
- -[AACloudKitMigrationStateRequest urlString]
- -[AACloudKitStartMigrationRequest urlString]
- -[AAFMIPAuthenticateRequest urlString]
- -[AAFamilyDetailsRequest urlString]
- -[AAFamilyEligibilityRequest urlString]
- -[AAGenericTermsUIRequest urlString]
- -[AALoginDelegatesRequest urlString]
- -[AAMyPhotoRequest urlString]
- -[AAPasswordSecurityUIRequest urlString]
- -[AAPaymentSummaryRequest urlString]
- -[AAPaymentUIRequest urlString]
- -[AAPersonalInfoUIRequest urlString]
- -[AASecondaryAuthenticationRequest urlString]
- -[AAURLConfiguration(Deprecated) _urlStringForKey:]
- -[AAURLConfiguration(Deprecated) acceptFamilyInviteV2URL]
- -[AAURLConfiguration(Deprecated) accountCreationUIURL]
- -[AAURLConfiguration(Deprecated) accountCreationURL]
- -[AAURLConfiguration(Deprecated) accountManagementUIURL]
- -[AAURLConfiguration(Deprecated) addFamilyMemberUIURL]
- -[AAURLConfiguration(Deprecated) checkiCloudMembershipURL]
- -[AAURLConfiguration(Deprecated) childAccountCreationUIURL]
- -[AAURLConfiguration(Deprecated) cloudKitDevicesListURL]
- -[AAURLConfiguration(Deprecated) cloudKitMigrationStateURL]
- -[AAURLConfiguration(Deprecated) cloudKitStartMigrationURL]
- -[AAURLConfiguration(Deprecated) deviceListURL]
- -[AAURLConfiguration(Deprecated) devicesUIURL]
- -[AAURLConfiguration(Deprecated) emailLookupURL]
- -[AAURLConfiguration(Deprecated) familyEligibilityURL]
- -[AAURLConfiguration(Deprecated) familyInviteSentV2URL]
- -[AAURLConfiguration(Deprecated) familyUIURL]
- -[AAURLConfiguration(Deprecated) fetchFamilyInviteV2URL]
- -[AAURLConfiguration(Deprecated) fmipAuthenticate]
- -[AAURLConfiguration(Deprecated) getFamilyDetailsURL]
- -[AAURLConfiguration(Deprecated) getMyPhotoURL]
- -[AAURLConfiguration(Deprecated) grandslamURL]
- -[AAURLConfiguration(Deprecated) initiateFamilyV2URL]
- -[AAURLConfiguration(Deprecated) loginDelegatesURL]
- -[AAURLConfiguration(Deprecated) mobileMeOfferAlertURL]
- -[AAURLConfiguration(Deprecated) passwordSecurityUIURL]
- -[AAURLConfiguration(Deprecated) paymentInfoUIURL]
- -[AAURLConfiguration(Deprecated) paymentSummaryURL]
- -[AAURLConfiguration(Deprecated) pendingFamilyInvitesUIURL]
- -[AAURLConfiguration(Deprecated) personalInfoUIURL]
- -[AAURLConfiguration(Deprecated) registerURL]
- -[AAURLConfiguration(Deprecated) secondaryAuthenticationURL]
- -[AAURLConfiguration(Deprecated) sendCodeURL]
- -[AAURLConfiguration(Deprecated) startFamilyInviteV2URL]
- -[AAURLConfiguration(Deprecated) updateAccountUIURL]
- -[AAURLConfiguration(Deprecated) updateAccountURL]
- -[AAURLConfiguration(Deprecated) updateNameURL]
- -[AAURLConfiguration(Deprecated) validateURL]
- -[AAURLConfiguration(Deprecated) verifyCodeURL]
- -[AAURLSession _enqueueRequest:withFlowID:completion:]
- -[AAURLSession _sessionQueue_enqueueTask:completion:]
- -[AAUpdateAccountUIRequest urlString]
- -[AAUpdateMyPhotoRequest urlString]
- -[AAUpdateNameRequest urlString]
- -[ATVHighSecurityAccountDeviceList urlString]
- -[ATVHighSecurityAccountSendCode urlString]
- -[ATVHighSecurityAccountVerifyCode urlString]
- -[_AAURLSessionOperation initWithCompletion:]
- GCC_except_table119
- GCC_except_table19
- GCC_except_table34
- __OBJC_$_INSTANCE_METHODS_AACloudKitDevicesListRequest
- __OBJC_$_INSTANCE_METHODS_AACloudKitMigrationStateRequest
- __OBJC_$_INSTANCE_METHODS_AACloudKitStartMigrationRequest
- __OBJC_$_INSTANCE_METHODS_AAPaymentUIRequest
- __OBJC_$_INSTANCE_METHODS_AAPersonalInfoUIRequest
- ___54-[AAURLSession _enqueueRequest:withFlowID:completion:]_block_invoke
- _objc_msgSend$_enqueueRequest:withFlowID:completion:
- _objc_msgSend$_sessionQueue_enqueueTask:completion:
- _objc_msgSend$_urlStringForKey:
- _objc_msgSend$cloudKitDevicesListURL
- _objc_msgSend$cloudKitMigrationStateURL
- _objc_msgSend$cloudKitStartMigrationURL
- _objc_msgSend$dataTaskWithRequest:withFlowID:completion:
- _objc_msgSend$deviceListURL
- _objc_msgSend$familyEligibilityURL
- _objc_msgSend$fmipAuthenticate
- _objc_msgSend$genericTermsURL
- _objc_msgSend$getFamilyDetailsURL
- _objc_msgSend$getMyPhotoURL
- _objc_msgSend$initWithCompletion:
- _objc_msgSend$loginDelegatesURL
- _objc_msgSend$operationWithCompletion:
- _objc_msgSend$passwordSecurityUIURL
- _objc_msgSend$paymentInfoUIURL
- _objc_msgSend$paymentSummaryURL
- _objc_msgSend$personalInfoUIURL
- _objc_msgSend$secondaryAuthenticationURL
- _objc_msgSend$sendCodeURL
- _objc_msgSend$updateAccountUIURL
- _objc_msgSend$updateMyPhotoURL
- _objc_msgSend$updateNameURL
- _objc_msgSend$verifyCodeURL
CStrings:
+ "AAAFoundationBackoff"
+ "AAForceServerBackoff"
+ "AAServerBackoffHelper: asking the server for a backoff directive via %{public}@"
+ "AAServerBackoffHelper: processed backoff info from response headers"
+ "AAServerBackoffHelper: suppressing request for urlBagKey=%{public}@"
+ "Setting client bundle ID header: %@"
+ "Setting proxied app bundle ID header: %@"
+ "X-Apple-I-Client-Bundle-Id"
+ "X-Apple-I-Force-Backoff"
+ "X-Apple-I-Proxied-Bundle-Id"
+ "_intelligenceScore"
+ "_isSyncAction"
+ "_source"
+ "com.apple.campo"
+ "icss"
```
