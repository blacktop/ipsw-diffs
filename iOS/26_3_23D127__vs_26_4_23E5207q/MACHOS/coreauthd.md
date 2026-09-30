## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x3b188
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x34a0
-  __TEXT.__objc_methlist: 0x1984
-  __TEXT.__const: 0x1370
-  __TEXT.__objc_methname: 0x4633
-  __TEXT.__cstring: 0x4951
-  __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methtype: 0x1f0a
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__oslogstring: 0x162b
-  __TEXT.__unwind_info: 0xc78
-  __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x4c8
+2005.100.174.0.0
+  __TEXT.__text: 0x39050
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x193c
+  __TEXT.__const: 0x13d8
+  __TEXT.__objc_methname: 0x45a8
+  __TEXT.__cstring: 0x4e2b
+  __TEXT.__objc_classname: 0x6d0
+  __TEXT.__objc_methtype: 0x1e93
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__oslogstring: 0x1655
+  __TEXT.__unwind_info: 0xcb8
+  __DATA_CONST.__auth_got: 0x710
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2130
-  __DATA_CONST.__cfstring: 0xdc0
+  __DATA_CONST.__const: 0x20c8
+  __DATA_CONST.__cfstring: 0xd00
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA.__objc_const: 0x7958
-  __DATA.__objc_selrefs: 0x10e8
-  __DATA.__objc_ivar: 0x178
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x7818
+  __DATA.__objc_selrefs: 0x1128
+  __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x1ac8
+  __DATA.__data: 0x1ad0
   __DATA.__bss: 0x150
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CA7BD46-DEE1-3B2C-9D24-51DA8A8C5FCE
-  Functions: 1441
-  Symbols:   396
-  CStrings:  1897
+  UUID: BD9A7613-785D-3B3C-8A09-DA07A1EF393E
+  Functions: 1526
+  Symbols:   415
+  CStrings:  1913
 
Symbols:
+ _LACCredentialCapture
+ _LACEntitlementDTO
+ _LACEntitlementExtractCredential
+ _LACEntitlementNonDisposableContextPool
+ _LACEntitlementSPI
+ _LACEntitlementSecureUIRecording
+ _LACEntitlementSoftwareUpdate
+ _LACEntitlementStorage
+ _LACEventPasscode
+ _LACEventPearl
+ _LACPolicyOptionAuthenticationTitle
+ _LACPolicyOptionCallerIconPath
+ _LACPolicyOptionCheckApplePayEnabled
+ _LACPolicyOptionExtractablePassword
+ _LACPolicyOptionPasscodeTitle
+ _LACPolicyOptionPhysicalButtonTitle
+ _LACPolicySoftwareUpdate
+ _LACStorageDomainSecure
+ _LACStorageKeyBiometricSuccessAge
+ _OBJC_CLASS_$_LACAutoLockServiceFactory
+ _OBJC_CLASS_$_LACBootArgParser
+ _OBJC_CLASS_$_LACConcurrentEvaluationHelper
+ _OBJC_CLASS_$_LACDTOAnalyticsService
+ _OBJC_CLASS_$_LACDTOFeatureRequirementsDataSourceProvider
+ _OBJC_CLASS_$_LACInstanceIDGenerator
+ _OBJC_CLASS_$_LACMaxBiometryFailureProcessor
+ _OBJC_CLASS_$_LACMutableXPCClient
+ _OBJC_CLASS_$_LACServiceAdapter
+ _OBJC_CLASS_$_LACServiceManagerBase
+ _OBJC_CLASS_$_LACXPCClient
+ _OBJC_METACLASS_$_LACServiceManagerBase
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_LABaseServiceManager
- _OBJC_CLASS_$_LACAuditToken
- _OBJC_CLASS_$_LACClientInfoProvider
- _OBJC_CLASS_$_LACDTOFeatureRequirementsDataSource
- _OBJC_CLASS_$_LAServiceAdapter
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_METACLASS_$_LABaseServiceManager
- _getuid
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "@\"<LACAutoLockService>\""
+ "@\"<LACContextUIDelegate>\""
+ "@\"<LACServiceManager>\""
+ "@\"LACDTOAnalyticsService\""
+ "@\"LACXPCClient\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSDate\"20@0:8I16"
+ "@20@0:8I16"
+ "@48@0:8q16@24@32@40"
+ "@56@0:8@16@24@?32@40Q48"
+ "ACMContextCredentialGetPropertyEx"
+ "Can't toggle event because non matching evaluation is running"
+ "Injecting LACPolicyOptionTimeout = %d"
+ "LACContextExternalizingXPC"
+ "LACRemoteUIEndpointProvider"
+ "LACServiceManager"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "RemoteUIListener failed to vend listener for identifier: %{public}@"
+ "T@\"<LACAutoLockService>\",R,N,V_autoLock"
+ "TQ,R,N,V_instanceId"
+ "_analyticsService"
+ "_autoLock"
+ "_client"
+ "_connectToExistingContext:callback:clientId:client:flags:invalidationBlock:reply:"
+ "_evaluateRequest:preflightKey:uiDelegate:reply:"
+ "_makeStorageRequestWithKey:options:contextUUID:connection:"
+ "_startAutoLock"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "autoLock"
+ "checkIsAutoEnablementAllowedWithCompletion:"
+ "clientInfo"
+ "compare:"
+ "connectToExistingContext:%x, client:%@, flags:%x"
+ "connectToExistingContext:callback:clientId:client:flags:reply:"
+ "connectionToRemoteUIInvalidatedForIdentifier:reply:"
+ "contextID"
+ "enableFeatureWithOptions:completion:"
+ "evaluateRequest:uiDelegate:reply:"
+ "evaluationRequest"
+ "externalizedContextProvider"
+ "featureFlagDimpleKeySentinelEnabled"
+ "featureFlagPresentationContextEnabled"
+ "hasStashedRequestsForContextID:"
+ "identities"
+ "initWithAnalyticsReporting:"
+ "initWithAuthenticator:environmentProvider:sessionMonitor:replyQueue:"
+ "initWithAuthenticator:environmentProvider:sessionMonitor:uiPresenter:replyQueue:"
+ "initWithConnection:"
+ "initWithContext:client:invalidationBlock:callback:clientId:"
+ "initWithDevice:kvStore:globalDomain:replyQueue:"
+ "initWithFeatureController:ratchetStateProvider:ratchetHandler:trustStateProvider:pendingEvaluationController:"
+ "initWithHelper:manager:replyQueue:"
+ "initWithKVStore:dataSourceProvider:featureFlags:bootArgParser:analytics:workQueue:"
+ "initWithOptions:client:contextID:originatorId:"
+ "initWithStorageDomain:key:options:contextID:originatorId:connection:"
+ "initWithTelemetryReporter:kvStore:ratchetStateMonitor:workQueue:"
+ "isEventPaused:"
+ "kLACServiceTypeAnalytics"
+ "kLACServiceTypeEnvironment"
+ "kLACServiceTypeRatchet"
+ "kLACServiceTypeSecureStorage"
+ "lastBiometricEnrollmentDateForCurrentUser"
+ "lastBiometricEnrollmentDateForUser:"
+ "makeAutoLockService"
+ "managedContextWithExternalizedContext:client:flags:reply:"
+ "nextInstanceIDInDomain:"
+ "passcodeSetDidChangeForUser:"
+ "pause:event:"
+ "placeholderIdentity"
+ "resetRatchetWithReason:completion:"
+ "restartRequestsForContextID:unpauseEvents:"
+ "returning %{public}@ on client: %@"
+ "runningAuthentication"
+ "setBypassEntitlement:"
+ "setCallback:"
+ "setObject:forKey:options:contextUUID:connection:completionHandler:"
+ "setOriginatorId:"
+ "v20@0:8I16"
+ "v28@0:8@\"NSUUID\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"LACDTOFeatureEnablementOptions\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"EvaluationRequest\"16@\"<LACContextUIDelegate>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v48@0:8@16@24q32@?40"
+ "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v64@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56"
+ "v64@0:8@16@24Q32@40q48@?56"
+ "v72@0:8@16@24Q32@40q48@?56@?64"
- "\t"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "@\"<LACContextCallbackXPC>\"16@0:8"
- "@\"<LAServiceManager>\""
- "@\"<LAUIDelegate>\""
- "@\"LACAuditToken\""
- "@\"NSData\"24@0:8^@16"
- "@104@0:8@16i24I28i32{?=[8I]}36B68@?72@?80@88Q96"
- "@24@0:8^@16"
- "@56@0:8q16@24@32@40@48"
- "ACMContextCredentialGetProperty"
- "B16@?0@\"NSString\"8"
- "Injecting LAOptionTimeout = %d"
- "LACContextExternalizing"
- "LAServiceManager"
- "Missing originator"
- "RemoteUIEndpointProvider"
- "T@\"<LACContextCallbackXPC>\",R,N"
- "T@\"<LACContextCallbackXPC>\",R,N,V_callback"
- "TB,R,N,V_cApiOrigin"
- "_auditToken"
- "_cApiOrigin"
- "_checkEntitlementBlock"
- "_connectToExistingContext:callback:clientId:flags:processId:userId:auditSessionId:auditToken:cApiOrigin:checkEntitlementBlock:invalidationBlock:connectionHash:reply:"
- "_evaluateRequest:originator:preflightKey:uiDelegate:reply:"
- "_makeStorageRequestWithKey:acl:options:contextUUID:connection:"
- "aclForKey:contextUUID:connection:completionHandler:"
- "aclForRequest:completionHandler:"
- "asid"
- "auditSessionIdentifier"
- "belongsToPlatformBinary:"
- "cApiOrigin"
- "cachedExternalizedContext"
- "callback"
- "com.apple.LocalAuthentication.RemoteUIHost"
- "com.apple.private.LocalAuthentication.DTO"
- "com.apple.private.LocalAuthentication.ExtractCredential"
- "com.apple.private.LocalAuthentication.NonDisposableContextPool"
- "com.apple.private.LocalAuthentication.SecureUIRecording"
- "com.apple.private.LocalAuthentication.SoftwareUpdate"
- "com.apple.private.LocalAuthentication.Storage"
- "connectToExistingContext:%x, pid:%d, uid:%u, flags:%x, cAPI:%d, connection:%x"
- "connectToExistingContext:userId:connection:checkEntitlementBlock:callback:clientId:flags:reply:"
- "connectionToViewServiceInvalidatedForIdentifier:reply:"
- "enableFeatureActivatingGracePeriodWithCompletion:"
- "enableFeatureWithCompletion:"
- "euid"
- "evaluateACL:operation:options:uiDelegate:originator:reply:"
- "evaluatePolicy:options:uiDelegate:originator:reply:"
- "evaluateRequest:uiDelegate:originator:reply:"
- "featureFlagLaunchAngelEnabled"
- "getDomainStateWithOptions:originator:reply:"
- "hasEntitlement:"
- "initWithAuthenticator:clientInfoProvider:environmentProvider:sessionMonitor:replyQueue:"
- "initWithAuthenticator:clientInfoProvider:environmentProvider:sessionMonitor:uiPresenter:replyQueue:"
- "initWithContext:processId:userId:auditSessionId:auditToken:cApiOrigin:checkEntitlementBlock:invalidationBlock:callback:clientId:"
- "initWithDevice:replyQueue:"
- "initWithFeatureController:ratchetStateProvider:trustStateProvider:pendingEvaluationController:"
- "initWithKVStore:requirementsDataSource:featureFlags:workQueue:"
- "initWithOptions:client:contextID:"
- "initWithRawValue:"
- "initWithStorageDomain:key:acl:options:contextID:connection:"
- "initWithTelemetryReporter:ratchetStateMonitor:"
- "kLAServiceTypeAnalytics"
- "kLAServiceTypeEnvironment"
- "kLAServiceTypeRatchet"
- "kLAServiceTypeSecureStorage"
- "managedContextWithExternalizedContext:processId:userId:auditSessionId:flags:checkEntitlementBlock:reply:"
- "passcodeSetDidChangeForHelper:"
- "processIdentifier"
- "q"
- "restartRequestsForContextID:"
- "returning %{public}@ on connection: %x"
- "setObject:acl:forKey:options:contextUUID:connection:completionHandler:"
- "signingID:"
- "synchronousExternalizedContextWithError:"
- "v128@0:8@16@24Q32q40i48I52i56{?=[8I]}60B92@?96@?104Q112@?120"
- "v24@0:8@\"LACPasscodeHelper\"16"
- "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LACOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8q16@\"NSDictionary\"24@\"<LAUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LAUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v60@0:8@16i24I28i32q36@?44@?52"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSData\"16@\"NSData\"24q32@\"NSDictionary\"40@\"NSUUID\"48@\"NSXPCConnection\"56@?<v@?@@\"NSError\">64"
- "v72@0:8@16@24q32@40@48@56@?64"
- "v76@0:8@16I24@28@?36@44Q52q60@?68"

```
