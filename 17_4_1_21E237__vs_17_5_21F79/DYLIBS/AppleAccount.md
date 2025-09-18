## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-981.12.0.0.0
-  __TEXT.__text: 0xb7bd4
+981.20.0.0.0
+  __TEXT.__text: 0xb86cc
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x8ce4
+  __TEXT.__objc_methlist: 0x8e0c
   __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0xb564
-  __TEXT.__oslogstring: 0xd2ca
-  __TEXT.__gcc_except_tab: 0x1718
+  __TEXT.__cstring: 0xb5d4
+  __TEXT.__oslogstring: 0xd32e
+  __TEXT.__gcc_except_tab: 0x1710
   __TEXT.__dlopen_cstrs: 0x241
-  __TEXT.__unwind_info: 0x2458
-  __TEXT.__objc_classname: 0x1bc8
-  __TEXT.__objc_methname: 0x1322d
+  __TEXT.__unwind_info: 0x2454
+  __TEXT.__objc_classname: 0x1c08
+  __TEXT.__objc_methname: 0x1339d
   __TEXT.__objc_methtype: 0x29df
-  __TEXT.__objc_stubs: 0xac60
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x3028
-  __DATA_CONST.__objc_classlist: 0x720
+  __TEXT.__objc_stubs: 0xace0
+  __DATA_CONST.__got: 0x510
+  __DATA_CONST.__const: 0x3038
+  __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1add8
-  __DATA_CONST.__objc_selrefs: 0x43c8
+  __DATA_CONST.__objc_const: 0x1b008
+  __DATA_CONST.__objc_selrefs: 0x4408
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0x710
-  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_classrefs: 0x718
+  __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xace0
+  __AUTH_CONST.__cfstring: 0xad60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_const: 0x1a8
+  __AUTH_CONST.__objc_const: 0x238
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__const: 0x48d0
+  __AUTH_CONST.__const: 0x48f0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__auth_got: 0x570
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xac4
-  __DATA.__data: 0x12e8
-  __DATA.__bss: 0x300
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xae4
+  __DATA.__data: 0x1328
+  __DATA.__bss: 0x2c0
   __DATA.__common: 0x6c
-  __DATA_DIRTY.__const: 0x680
+  __DATA_DIRTY.__const: 0x660
   __DATA_DIRTY.__objc_const: 0x5b68
   __DATA_DIRTY.__objc_data: 0x4600
   __DATA_DIRTY.__data: 0x60

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C3CF8AE-0099-3B5E-88D0-CF4229146FD8
-  Functions: 3868
-  Symbols:   13687
-  CStrings:  7759
+  UUID: ACAD5113-FE24-35E4-A76E-4A0D8CF92053
+  Functions: 3898
+  Symbols:   13774
+  CStrings:  7785
 
Symbols:
+ +[AAiCloudTermsDisagreeRequest responseClass]
+ -[AAAcceptedTermsController _shouldRecordTermsForBuddyWithTermsInfo:]
+ -[AAContactsProvider fetchWalrusEligibleCustodiansForExpansionCohortsWithCompletion:]
+ -[AACustodianDataRecoveryKeys initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:]
+ -[AACustodianDataRecoveryKeys recordBuildVersion]
+ -[AACustodianDataRecoveryKeys setRecordBuildVersion:]
+ -[AACustodianRecoveryRequestContext recordBuildVersion]
+ -[AACustodianRecoveryRequestContext setRecordBuildVersion:]
+ -[AAURLConfiguration homepodSetupiCloudTerms]
+ -[AAiCloudTermsAgreeRequest serverInfo]
+ -[AAiCloudTermsAgreeRequest setServerInfo:]
+ -[AAiCloudTermsAgreeRequest urlRequest].cold.1
+ -[AAiCloudTermsDisagreeRequest .cxx_destruct]
+ -[AAiCloudTermsDisagreeRequest account]
+ -[AAiCloudTermsDisagreeRequest additionalHeaders]
+ -[AAiCloudTermsDisagreeRequest initWithURLString:account:]
+ -[AAiCloudTermsDisagreeRequest preferPassword]
+ -[AAiCloudTermsDisagreeRequest serverInfo]
+ -[AAiCloudTermsDisagreeRequest setAccount:]
+ -[AAiCloudTermsDisagreeRequest setAdditionalHeaders:]
+ -[AAiCloudTermsDisagreeRequest setPreferPassword:]
+ -[AAiCloudTermsDisagreeRequest setServerInfo:]
+ -[AAiCloudTermsDisagreeRequest setSlaVersion:]
+ -[AAiCloudTermsDisagreeRequest slaVersion]
+ -[AAiCloudTermsDisagreeRequest urlRequest]
+ -[AAiCloudTermsDisagreeRequest urlRequest].cold.1
+ _AATermsEntryHomePodSLA
+ _ACAccountDataclassPhoneFaceTime
+ _OBJC_CLASS_$_AAiCloudTermsDisagreeRequest
+ _OBJC_CLASS_$_AAiCloudTermsDisagreeResponse
+ _OBJC_IVAR_$_AACustodianDataRecoveryKeys._recordBuildVersion
+ _OBJC_IVAR_$_AACustodianRecoveryRequestContext._recordBuildVersion
+ _OBJC_IVAR_$_AAiCloudTermsAgreeRequest._serverInfo
+ _OBJC_IVAR_$_AAiCloudTermsDisagreeRequest._account
+ _OBJC_IVAR_$_AAiCloudTermsDisagreeRequest._additionalHeaders
+ _OBJC_IVAR_$_AAiCloudTermsDisagreeRequest._preferPassword
+ _OBJC_IVAR_$_AAiCloudTermsDisagreeRequest._serverInfo
+ _OBJC_IVAR_$_AAiCloudTermsDisagreeRequest._slaVersion
+ _OBJC_METACLASS_$_AAiCloudTermsDisagreeRequest
+ _OBJC_METACLASS_$_AAiCloudTermsDisagreeResponse
+ __OBJC_$_CLASS_METHODS_AAiCloudTermsDisagreeRequest
+ __OBJC_$_INSTANCE_METHODS_AAiCloudTermsDisagreeRequest
+ __OBJC_$_INSTANCE_VARIABLES_AAiCloudTermsDisagreeRequest
+ __OBJC_$_PROP_LIST_AAiCloudTermsDisagreeRequest
+ __OBJC_CLASS_RO_$_AAiCloudTermsDisagreeRequest
+ __OBJC_CLASS_RO_$_AAiCloudTermsDisagreeResponse
+ __OBJC_METACLASS_RO_$_AAiCloudTermsDisagreeRequest
+ __OBJC_METACLASS_RO_$_AAiCloudTermsDisagreeResponse
+ ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.117
+ ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.107
+ ___42-[AAiCloudTermsDisagreeRequest urlRequest]_block_invoke
+ ___85-[AAContactsProvider fetchWalrusEligibleCustodiansForExpansionCohortsWithCompletion:]_block_invoke
+ ___86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.103
+ _getCDPCustodianRecoveryInfoClass
+ _kAAAnalyticsADPCohortType
+ _kAAFDeviceSessionIdString
+ _kAAFFlowIdString
+ _kAATermsInfoKeyProxiedContext
+ _objc_msgSend$_shouldRecordTermsForBuddyWithTermsInfo:
+ _objc_msgSend$initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$recordBuildVersion
- +[AAPreferences repairWithoutTransparencyCFU]
- ___103-[AASignInFlowController _delegate_presentGenericTermsUIforAccount:authResults:serverError:completion:]_block_invoke.115
- ___131-[AASignInFlowController _onqueue_saveAccount:withAuthResults:withCDPEnablement:withAllDataclassesEnabledIfPossibleWithCompletion:]_block_invoke.105
- ___86-[AASignInFlowController _onqueue_enrollCDPStateForAccount:withCDPContext:completion:]_block_invoke.101
- _kAAFDeviceSessionId
- _kAAFFlowId
- _kAAProtocolPrefRepairWithoutTransparencyCFUKey
CStrings:
+ "\x01\x13"
+ "\x16"
+ "%@: Account property is `nil`. Not adding authorization header."
+ "<%@: %p> for UUID: %@ recordBuildVersion: %@"
+ "AAiCloudTermsDisagreeRequest"
+ "AAiCloudTermsDisagreeResponse"
+ "CustodianRecoveryRequestContext with ownerAppleID: %@ \nsessionID: %@ \nrecoveryCode: %@ \ncustodianUUID: %@ \nrecoveryToken: %@ \ncliMode: %i \ndataOnly: %@, recordBuildVersion: %@"
+ "HomePodSLA"
+ "Returning canRepairCustodianV2 from urlbag: %@"
+ "Returning maxRepairCountV2 from urlbag: %@"
+ "T@\"NSString\",C,N,V_recordBuildVersion"
+ "T@\"NSString\",C,N,V_serverInfo"
+ "Terms Disagree Request is: %@"
+ "_recordBuildVersion"
+ "_serverInfo"
+ "_shouldRecordTermsForBuddyWithTermsInfo:"
+ "canRepairCustodianV2"
+ "custodianCfgsV2"
+ "custodianCfgsV2 from urlbag: %@"
+ "fetchWalrusEligibleCustodiansForExpansionCohortsWithCompletion:"
+ "homepod-setup-icloud-terms"
+ "homepodSetupiCloudTerms"
+ "initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:"
+ "instancesRespondToSelector:"
+ "maxRepairCountV2"
+ "proxiedcontext"
+ "recordBuildVersion"
+ "setRecordBuildVersion:"
+ "setServerInfo:"
+ "telemetryVersion"
- "<%@: %p> for UUID: %@"
- "AARepairWithoutTransparencyCFU"
- "CustodianRecoveryRequestContext with ownerAppleID: %@ \nsessionID: %@ \nrecoveryCode: %@ \ncustodianUUID: %@ \nrecoveryToken: %@ \ncliMode: %i \ndataOnly: %@"
- "Returning canRepairCustodian from urlbag: %@"
- "Returning maxRepairCount from urlbag: %@"
- "custodianCfgs"
- "custodianCfgs from urlbag: %@"
- "repairWithoutTransparencyCFU"

```
