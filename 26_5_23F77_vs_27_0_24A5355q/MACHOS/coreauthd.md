## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.120.18.0.0
-  __TEXT.__text: 0x39198
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x3720
-  __TEXT.__objc_methlist: 0x195c
-  __TEXT.__const: 0x13d8
-  __TEXT.__objc_methname: 0x467a
-  __TEXT.__cstring: 0x4e2b
-  __TEXT.__objc_classname: 0x6ef
-  __TEXT.__objc_methtype: 0x1e93
-  __TEXT.__gcc_except_tab: 0x1c8
+2305.0.0.0.1
+  __TEXT.__text: 0x38044
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_stubs: 0x3620
+  __TEXT.__objc_methlist: 0x19ac
+  __TEXT.__const: 0x13f0
+  __TEXT.__objc_methname: 0x472f
+  __TEXT.__cstring: 0x4ff1
+  __TEXT.__objc_classname: 0x6d4
+  __TEXT.__objc_methtype: 0x1eef
+  __TEXT.__gcc_except_tab: 0x19c
   __TEXT.__oslogstring: 0x1655
-  __TEXT.__unwind_info: 0xcb8
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x20c8
-  __DATA_CONST.__cfstring: 0xd00
+  __TEXT.__unwind_info: 0xd08
+  __DATA_CONST.__const: 0x20a0
+  __DATA_CONST.__cfstring: 0xcc0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x7840
-  __DATA.__objc_selrefs: 0x1158
-  __DATA.__objc_ivar: 0x170
+  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA.__objc_const: 0x7990
+  __DATA.__objc_selrefs: 0x1150
+  __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x1b30
+  __DATA.__data: 0x1b38
   __DATA.__bss: 0x150
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0826AD67-D0C9-36B0-8C99-7FA4C6568541
-  Functions: 1527
-  Symbols:   417
-  CStrings:  1920
+  UUID: CDE63D1E-3DCF-3D88-BF6F-1BCFEADD8DDA
+  Functions: 1557
+  Symbols:   423
+  CStrings:  1933
 
Symbols:
+ _LACEntitlementRGBCapture
+ _LACStorageKeyDSLExtendedPolicyProtectionEnabled
+ _OBJC_CLASS_$_LACDTOAppleAccountInfoProvider
+ _OBJC_CLASS_$_LACDTOCoreProcessor
+ _OBJC_CLASS_$_LACDTOExtendedPolicyProtectionProcessor
+ _OBJC_CLASS_$_LACDTOFeatureRequirementsDataSource
+ _OBJC_CLASS_$_LACDTOLocationServicesInfoProvider
+ _OBJC_CLASS_$_LACLocalizationUtils
+ _OBJC_CLASS_$_LACSDKHelper
+ _OBJC_CLASS_$_LACSUnmanagedExtractablePassword
+ _OBJC_CLASS_$_LACStashedCredentialsProcessor
+ ___stderrp
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- _LACEntitlementSecureUIRecording
- _LACLogSubsystem
- _LACPolicyOptionSecureUIRecording
- _NSGlobalDomain
- _OBJC_CLASS_$_LACDTOAnalyticsProcessorLocation
- _OBJC_CLASS_$_LACDTOFeatureRequirementsDataSourceProvider
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_PreflightCache
- ___kCFBooleanFalse
- _objc_retainAutoreleasedReturnValue
- _os_variant_allows_internal_security_policies
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "@\"<LACDTOEventBus>\"16@0:8"
+ "@\"<LACDTOTelemetryReporting>\""
+ "@\"<LACDTOTelemetryReporting>\"16@0:8"
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "Failed to get data protection class for given path %s with errno %s (%d)\n"
+ "T@\"<LACDTOEventBus>\",R,N"
+ "T@\"<LACDTOEventBus>\",R,N,V_eventBus"
+ "T@\"<LACDTOTelemetryReporting>\",R,N"
+ "T@\"<LACDTOTelemetryReporting>\",R,N,V_telemetry"
+ "_aks_remote_peer_drop"
+ "_aks_remote_peer_get_state"
+ "_evaluateRequest:uiDelegate:reply:"
+ "_telemetry"
+ "aks_pki_token_get_info"
+ "aks_pki_token_list"
+ "aks_pki_token_op_register"
+ "aks_pki_token_op_set_password"
+ "aks_pki_token_op_unlock"
+ "aks_pki_token_op_verify"
+ "aks_pki_token_register_internal"
+ "aks_pki_token_request_challenge"
+ "aks_pki_token_unregister"
+ "checkIsExtendedPolicyProtectionAvailableWithCompletion:"
+ "checkIsExtendedPolicyProtectionEnabledWithCompletion:"
+ "controllerWithStore:featureController:eventBus:featureFlags:telemetry:workQueue:"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
+ "disableExtendedPolicyProtectionWithContext:completion:"
+ "enableExtendedPolicyProtectionWithCompletion:"
+ "eventBus"
+ "initWithData:error:"
+ "initWithDevice:kvStore:accountProvider:locationServicesProvider:globalDomain:replyQueue:"
+ "initWithFeatureController:featureFlags:"
+ "initWithKVStore:dataSource:featureFlags:bootArgParser:analytics:workQueue:"
+ "initWithLostModeProvider:store:telemetry:workQueue:"
+ "initWithRatchetStateProvider:ratchetHandler:device:evaluationIdentifierFactory:persistentStore:telemetry:workQueue:"
+ "initWithReplyQueue:uiController:store:featureStateProvider:telemetry:"
+ "isLocalizationKey:"
+ "isRunningOnInternalBuild"
+ "telemetryReporter"
- "AKSGetKeyBagStats"
- "AKSGetStashStats"
- "LA.preflightCache.enabled"
- "_evaluateRequest:preflightKey:uiDelegate:reply:"
- "_isPreflightOnCleanContext:"
- "addPreflightResult:forKey:"
- "aks_fv_new_sibling_vek"
- "aks_remote_peer_drop"
- "aks_remote_peer_get_state"
- "aks_smartcard_register"
- "aks_smartcard_request_unlock"
- "aks_smartcard_unlock"
- "aks_smartcard_unregister"
- "aks_stash_escrow"
- "cachedPreflightResultForKey:"
- "com.apple.private.LocalAuthentication.RGBCapture"
- "controllerWithStore:featureController:eventBus:featureFlags:workQueue:"
- "featureFlagDimpleKeyiPadTelemetryEnabled"
- "initWithAnalyticsReporting:locationProvider:"
- "initWithDevice:kvStore:globalDomain:replyQueue:"
- "initWithKVStore:dataSourceProvider:featureFlags:bootArgParser:analytics:workQueue:"
- "initWithLostModeProvider:store:workQueue:"
- "initWithRatchetStateProvider:ratchetHandler:device:evaluationIdentifierFactory:persistentStore:workQueue:"
- "initWithReplyQueue:uiController:store:featureStateProvider:"
- "keyForPreflightOfACL:operation:options:auditToken:uid:"
- "keyForPreflightOfPolicy:options:auditToken:uid:"
- "persistentDomainForName:"
- "readOnlyLocationProviderWithStore:workQueue:"
- "resultInfo"
- "standardUserDefaults"

```
