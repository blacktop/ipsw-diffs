## ConfigurationProfilesUI

> `/System/Library/PrivateFrameworks/ConfigurationProfilesUI.framework/Versions/A/ConfigurationProfilesUI`

```diff

-1851.2.2.0.0
-  __TEXT.__text: 0x48674
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x1d20
-  __TEXT.__gcc_except_tab: 0x9050
+1851.4.12.0.0
+  __TEXT.__text: 0x4b0b4
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x2608
+  __TEXT.__gcc_except_tab: 0x9524
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xaccf
+  __TEXT.__cstring: 0xb3c9
   __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__ustring: 0x5c
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x1fd0
-  __TEXT.__objc_classname: 0x47a
-  __TEXT.__objc_methname: 0x864b
-  __TEXT.__objc_methtype: 0x1b13
-  __TEXT.__objc_stubs: 0x6280
-  __DATA_CONST.__got: 0x688
+  __TEXT.__unwind_info: 0x2100
+  __TEXT.__objc_classname: 0x479
+  __TEXT.__objc_methname: 0x88a5
+  __TEXT.__objc_methtype: 0x1b5b
+  __TEXT.__objc_stubs: 0x6360
+  __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d68
+  __DATA_CONST.__objc_selrefs: 0x2140
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_arraydata: 0x288
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0x15f0
-  __AUTH_CONST.__cfstring: 0x8e00
-  __AUTH_CONST.__objc_const: 0x4d00
+  __DATA_CONST.__objc_arraydata: 0x290
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__const: 0x1720
+  __AUTH_CONST.__cfstring: 0x94c0
+  __AUTH_CONST.__objc_const: 0x3d30
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x2e4
+  __DATA.__objc_ivar: 0x2ec
   __DATA.__data: 0x678
-  __DATA.__bss: 0x368
+  __DATA.__bss: 0x3c0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/Frameworks/SecurityInterface.framework/Versions/A/SecurityInterface
   - /System/Library/Frameworks/WebKit.framework/Versions/A/WebKit
   - /System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/AOSUI
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/Versions/A/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit

   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/Versions/A/MDMClientLibrary
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C5146E4-9996-35B1-9BF9-7337664405ED
-  Functions: 1321
-  Symbols:   3821
-  CStrings:  4080
+  UUID: 2D73AB8F-07CE-3405-8590-3FDA9BD9717A
+  Functions: 1394
+  Symbols:   4018
+  CStrings:  4204
 
Symbols:
+ +[CPUI_SA_CloudConfigurationHelper shouldShowDEPNagUI].cold.1
+ +[DMCEnrollmentMCXConnection shared].cold.1
+ -[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:]
+ -[CPUI_EnrollmentController isDoingOrgoPhase2]
+ -[CPUI_EnrollmentController setIsDoingOrgoPhase2:]
+ -[CPUI_SA_CloudConfigurationHelper depNagOptions].cold.1
+ -[CPUI_SA_CloudConfigurationHelper userSnoozedDEPNag].cold.1
+ -[CP_GetEnrollmentProfileController download:decideDestinationUsingResponse:suggestedFilename:completionHandler:]
+ -[CP_GetEnrollmentProfileController download:didFailWithError:resumeData:]
+ -[CP_GetEnrollmentProfileController download:didReceiveAuthenticationChallenge:completionHandler:]
+ -[CP_GetEnrollmentProfileController download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]
+ -[CP_GetEnrollmentProfileController downloadDidFinish:]
+ -[CP_GetEnrollmentProfileController webView:navigationAction:didBecomeDownload:]
+ -[CP_GetEnrollmentProfileController webView:navigationResponse:didBecomeDownload:]
+ -[CloudConfigClassicEnrollmentManager isSilentEnroll]
+ -[CloudConfigClassicEnrollmentManager setIsSilentEnroll:]
+ -[URLConnectionLoader URLSession:dataTask:didReceiveData:].cold.1
+ -[URLConnectionLoader URLSession:dataTask:didReceiveResponse:completionHandler:].cold.1
+ -[URLConnectionLoader URLSession:task:didCompleteWithError:].cold.1
+ -[URLConnectionLoader URLSession:task:didCompleteWithError:].cold.2
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.1
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.10
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.11
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.12
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.13
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.14
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.15
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.2
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.3
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.4
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.5
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.6
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.7
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.8
+ -[URLConnectionLoader URLSession:task:didReceiveChallenge:completionHandler:].cold.9
+ -[URLConnectionLoader URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:].cold.1
+ -[URLConnectionLoader URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:].cold.2
+ -[URLConnectionLoader URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:].cold.3
+ -[URLConnectionLoader httpResponse].cold.1
+ -[URLConnectionLoader prepRequest:taskType:forOpDesc:].cold.1
+ -[URLConnectionLoader sendSynchronousRequest:forOpDesc:returningError:].cold.1
+ -[URLConnectionLoader start].cold.1
+ -[URLConnectionLoader start].cold.2
+ -[URLConnectionLoader start].cold.3
+ CallMDMClient_IsRunningAppleInternalOrFactory.cold.1
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table149
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table90
+ GetCurrentUserODRecord.cold.1
+ LogRequest.cold.1
+ LogRequest.cold.2
+ LogRequest.cold.3
+ LogRequest.cold.4
+ LogResponse.cold.1
+ LogResponse.cold.2
+ LogResponse.cold.3
+ LogResponse.cold.4
+ OBJC_IVAR_$_CPUI_EnrollmentController._isDoingOrgoPhase2
+ OBJC_IVAR_$_CloudConfigClassicEnrollmentManager._isSilentEnroll
+ _AAAccountClassPrimary
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CPUI_AMPCoDProxyInstallSystemProfileData
+ _CPUI_AMPCoDProxyRemoveSystemProfileWithIdentifier
+ _CP_InstallSystemProfileData
+ _CP_RemoteManagementSetSystemMDMProperty
+ _CP_RemoveSystemProfileWithIdentifier
+ _CallMDMClient_IsRunningAppleInternalOrFactory
+ _MGCopyAnswer
+ _OBJC_CLASS_$_NSDateFormatter
+ _Z16IsLAContextValidP9LAContext.cold.1
+ _Z16IsModernKeychainPKv.cold.1
+ _Z17IsRunningAsDaemonv.cold.1
+ _Z19GetProfilesUIHelperv.cold.1
+ _Z22CPUI_GetLocalizedRsrcsv.cold.1
+ _Z22CPUI_StartDisplayErrorP8NSWindowP7NSImageP8NSStringP7NSErrorU13block_pointerFvvE.cold.1
+ _Z22GetCurrentBootstrapUIDv.cold.1
+ _Z22IsRunningAppleInternalv.cold.1
+ _Z23IsRunningOnAppleSiliconv.cold.1
+ _Z23IsRunningOnFactoryQuickv.cold.1
+ _Z25AdjLocStrKeyForAAMktgNameP8NSString.cold.1
+ _Z28RemoveProvisionalDEPFlagFilev.cold.1
+ _Z3logv.cold.1
+ _ZL10DebugAlertP8NSString.cold.1
+ _ZL12GetAdminPrefP8NSString.cold.1
+ _ZL16GetFirstODRecordP7NSArrayIP8ODRecordEPP7NSError.cold.1
+ _ZL18GetLocalizedStringP8NSString.cold.1
+ _ZL18GetOurEntitlementsv.cold.1
+ _ZL19DoLogPinningFailureP8NSStringP7NSError18SecTrustResultTypebP7NSArraym.cold.1
+ _ZL19DoLogPinningFailureP8NSStringP7NSError18SecTrustResultTypebP7NSArraym.cold.2
+ _ZL19DoLogPinningFailureP8NSStringP7NSError18SecTrustResultTypebP7NSArraym.cold.3
+ _ZL19GetDefaultLogHandlev.cold.1
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.1
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.2
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.3
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.4
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.5
+ _ZL22HandleCertificateErrorP7NSErrorb.cold.6
+ _ZL22LogRequestResponseCoreP8NSStringP12NSDictionaryS0_.cold.1
+ _ZL22LogRequestResponseCoreP8NSStringP12NSDictionaryS0_.cold.2
+ _ZL22LogRequestResponseCoreP8NSStringP12NSDictionaryS0_.cold.3
+ _ZL22LogRequestResponseCoreP8NSStringP12NSDictionaryS0_.cold.4
+ _ZL31ValidateWithPinningCertificatesP7NSArraymP28NSURLAuthenticationChallengePU15__autoreleasingP7NSError.cold.1
+ _ZL41EvaluateServerTrustWithAnchorCertificatesP10__SecTrustP7NSArrayPU15__autoreleasingP7NSError.cold.1
+ _ZL41EvaluateServerTrustWithAnchorCertificatesP10__SecTrustP7NSArrayPU15__autoreleasingP7NSError.cold.2
+ _ZL41EvaluateServerTrustWithAnchorCertificatesP10__SecTrustP7NSArrayPU15__autoreleasingP7NSError.cold.3
+ _ZL41EvaluateServerTrustWithAnchorCertificatesP10__SecTrustP7NSArrayPU15__autoreleasingP7NSError.cold.4
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.3
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.4
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.5
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.6
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.7
+ _ZL5DoLog18LoggerMessageLevelmP13LoggingHandleP8NSStringPc.cold.8
+ _ZN11USecureBoot23LocalPolicySupportsSMB5Ev.cold.1
+ _ZN11USecureBoot23SupportsLocalBootPolicyEv.cold.1
+ _ZN15UMDM403Response22BuildSetupInfoForBuddyEP7NSErrorbPU15__autoreleasingS1_.cold.1
+ _ZN20UEnrollmentPreflight5StartEP8NSStringbU13block_pointerFvbP7NSErrorE.cold.1
+ _ZN4ULog23SetSubsystemAndCategoryEP8NSStringS1_.cold.1
+ _ZN4ULog23SetSubsystemAndCategoryEP8NSStringS1_.cold.2
+ _ZN4ULog4BeepEb.cold.1
+ _ZN6ODUtil8LogErrorERP7NSErrorPS1_P8NSStringz.cold.1
+ _ZN9UAccounts15GetAccountStoreEv.cold.1
+ __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.338
+ __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.358
+ __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.381
+ __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke_2.343
+ __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke_2.368
+ __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.272
+ __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.288
+ __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.277
+ __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke.300
+ __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke.306
+ __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke_2.301
+ __28-[URLConnectionLoader start]_block_invoke.144.cold.1
+ __54-[CPUI_iCloudSilentSignIn _startSignInWithCompletion:]_block_invoke.306
+ __63-[CPUI_EnrollmentController removeProfileWithIdentifier:async:]_block_invoke.250
+ __81-[CPUI_SA_CloudConfigurationHelper startFetchCloudConfigurationInWindow:options:]_block_invoke.231
+ __81-[CPUI_SA_CloudConfigurationHelper startFetchCloudConfigurationInWindow:options:]_block_invoke.243
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke.128
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke.157
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke.65
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.150
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.161
+ __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.66
+ __CPUI_PreflightManagedAccountDeletion_block_invoke.37
+ __CPUI_PreflightManagedAccountDeletion_block_invoke.40
+ __CPUI_StartMDMReAuth_block_invoke.24
+ __CPUI_StartMDMReAuth_block_invoke.35
+ __CallMDMClient_IsRunningAppleInternalOrFactory_block_invoke.cold.1
+ __CallMDMClient_IsRunningAppleInternalOrFactory_block_invoke.cold.2
+ __MergedGlobals
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_REFS_WKDownloadDelegate
+ __OBJC_LABEL_PROTOCOL_$_WKDownloadDelegate
+ __OBJC_PROTOCOL_$_WKDownloadDelegate
+ __Z10GetDateStrP6NSDate20NSDateFormatterStyleS1_
+ __Z14NSIsDictionaryP11objc_object
+ __Z16GenerateSHA1HashP6NSData
+ __Z18GetDateStrWithSecsP6NSDate
+ __Z18SetSuccessForPlistP19NSMutableDictionarybP7NSError
+ __Z20CleanNSErrorForPlistP7NSError
+ __Z23IsRunningOnAppleSiliconv
+ __Z23IsRunningOnFactoryQuickv
+ __Z25NSDictionaryGetBooleanObjP12NSDictionaryP8NSString
+ __Z25XPC_MDM_SendPublicRequest13CPDestinationP12NSDictionaryPU15__autoreleasingS1_P9CPPLoggerPU15__autoreleasingP7NSError
+ __Z27BuildExtAuthForSilentEnrollP8NSStringS0_
+ __Z30SendProfilesPrefPaneQueryItemsP7NSArrayIP14NSURLQueryItemE
+ __ZL18CleanValueForPlistP11objc_object
+ __ZL20BuildAppProvidedDatabb
+ __ZL33GetAppleAccountMDMServerTokenDescP9ACAccount
+ __ZL34BuildProfilesPrefPaneURLComponentsv
+ __ZN14UAppleAccounts24GetAccountForCurrentUserEP9CPProfile
+ __ZNKSt3__16vectorI17AuthorizationItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI17AuthorizationItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZ23IsRunningOnAppleSiliconvE15gIsAppleSilicon
+ __ZZ23IsRunningOnAppleSiliconvE5gOnce
+ __ZZ23IsRunningOnFactoryQuickvE10gIsFactory
+ __ZZ23IsRunningOnFactoryQuickvE5gOnce
+ __ZZ27BuildExtAuthForSilentEnrollP8NSStringS0_E6gLACtx
+ __ZZ45CallMDMClient_IsRunningAppleInternalOrFactoryE30gRunningAppleInternalOrFactory
+ __ZZ45CallMDMClient_IsRunningAppleInternalOrFactoryE5gOnce
+ __ZZL24IsRunningOnFactorySecurevE17gRunningOnFactory
+ __ZZL24IsRunningOnFactorySecurevE5gOnce
+ __ZZL26HaveFactoryInstallSentinelvE10gIsFactory
+ __ZZL26HaveFactoryInstallSentinelvE5gOnce
+ ___113-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:]_block_invoke
+ ___113-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:]_block_invoke_2
+ ___63-[CPUI_EnrollmentController removeProfileWithIdentifier:async:]_block_invoke_2
+ ___CPUI_PreflightManagedAccountDeletion_block_invoke
+ ___CPUI_PreflightManagedAccountDeletion_block_invoke_2
+ ___CallMDMClient_IsRunningAppleInternalOrFactory_block_invoke
+ ___Z23IsRunningOnFactoryQuickv_block_invoke.cold.1
+ ___ZL10DebugAlertP8NSString_block_invoke_2.cold.1
+ ___ZL13StartUnenrollP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvvE_block_invoke.106
+ ___ZL13StartUnenrollP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvvE_block_invoke_2.116
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.69
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.75
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.89
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.70
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.82
+ ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.90
+ ___ZL16_SendMessageSyncbjP12NSDictionaryPU15__autoreleasingS0_P9CPPLoggerPU15__autoreleasingP7NSError_block_invoke.152
+ ___ZL16_SendMessageSyncbjP12NSDictionaryPU15__autoreleasingS0_P9CPPLoggerPU15__autoreleasingP7NSError_block_invoke.159
+ ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke.116
+ ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke.128
+ ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke_2.121
+ ___ZL22ShowCFUserNotificationP8NSString_block_invoke.cold.1
+ ___ZL33StartBYODEnrollmentFlowControllerP27DMCEnrollmentFlowControllerP8NSStringU13block_pointerFvbbP7NSErrorE_block_invoke.187
+ ____Z23IsRunningOnAppleSiliconv_block_invoke
+ ____Z23IsRunningOnFactoryQuickv_block_invoke
+ ____ZL13StartUnenrollP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvvE_block_invoke
+ ____ZL13StartUnenrollP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvvE_block_invoke_2
+ ____ZL13StartUnenrollP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvvE_block_invoke_3
+ ____ZL24IsRunningOnFactorySecurev_block_invoke
+ ____ZL24ShowAlertWhyCantUnenrollP8NSWindowP7NSImageP8NSStringU13block_pointerFvvE_block_invoke
+ ____ZL26HaveFactoryInstallSentinelv_block_invoke
+ ____ZL40PromptForManagedAppleAccountUnenrollmentbP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke
+ ___block_descriptor_48_ea8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_ea8_32s40s48bs_e37_v28?0"NSDictionary"8B16"NSError"20l
+ ___block_descriptor_56_ea8_32s40s48s_e25_v16?0?<v?B"NSError">8l
+ ___block_descriptor_75_ea8_32s40s48s56bs64r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_75_ea8_32s40s48s56s64r_e25_v16?0?<v?B"NSError">8l
+ ___block_descriptor_81_ea8_32s40s48s56s64s72bs_e8_v12?0B8l
+ ___block_descriptor_81_ea8_32s40s48s56s64s72s_e25_v16?0?<v?B"NSError">8l
+ ___block_descriptor_88_ea8_32s40s48s56s64s72s80s_e25_v16?0?<v?B"NSError">8l
+ ___copy_helper_block_ea8_32s40s48s56s64r
+ ___copy_helper_block_ea8_32s40s48s56s64s72s80s
+ __block_literal_global.189
+ __block_literal_global.194
+ __block_literal_global.400
+ __block_literal_global.6
+ __block_literal_global.714
+ __block_literal_global.742
+ __block_literal_global.8
+ _kDMCErrorDetailsSUInfoKey
+ _memcpy
+ _objc_msgSend$aa_mdmServerToken
+ _objc_msgSend$isDoingOrgoPhase2
+ _objc_msgSend$isSilentEnroll
+ _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
+ _objc_msgSend$originalRequest
+ _objc_msgSend$setCredential:type:
+ _objc_msgSend$setIsDoingOrgoPhase2:
+ _objc_msgSend$setIsSilentEnroll:
+ _objc_msgSend$setPreventsApplicationTerminationWhenModal:
+ _sysctlbyname
- -[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:completionHandler:]
- -[CP_GetEnrollmentProfileController _download:decideDestinationWithSuggestedFilename:completionHandler:]
- -[CP_GetEnrollmentProfileController _download:didCreateDestination:]
- -[CP_GetEnrollmentProfileController _download:didFailWithError:]
- -[CP_GetEnrollmentProfileController _download:didReceiveAuthenticationChallenge:completionHandler:]
- -[CP_GetEnrollmentProfileController _downloadDidCancel:]
- -[CP_GetEnrollmentProfileController _downloadDidFinish:]
- -[CP_GetEnrollmentProfileController _downloadDidStart:]
- -[CP_GetEnrollmentProfileController _downloadProcessDidCrash:]
- GCC_except_table116
- GCC_except_table136
- GCC_except_table138
- GCC_except_table148
- GCC_except_table152
- GCC_except_table153
- GCC_except_table155
- __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.325
- __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.345
- __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke.365
- __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke_2.330
- __124-[CPUI_EnrollmentController requestMAIDSignInWithAuthenticationResults:personaID:makeiTunesAccountActive:completionHandler:]_block_invoke_2.352
- __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.259
- __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.275
- __128-[CPUI_EnrollmentController requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.264
- __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke.287
- __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke.293
- __131-[CPUI_EnrollmentController requestSilentMAIDAuthenticationWithAuthenticationResults:personaID:requireAppleMAID:completionHandler:]_block_invoke_2.288
- __63-[CPUI_EnrollmentController removeProfileWithIdentifier:async:]_block_invoke.244
- __81-[CPUI_SA_CloudConfigurationHelper startFetchCloudConfigurationInWindow:options:]_block_invoke.221
- __81-[CPUI_SA_CloudConfigurationHelper startFetchCloudConfigurationInWindow:options:]_block_invoke.233
- __CPUI_EnrollInRemoteManagementPriv_block_invoke.119
- __CPUI_EnrollInRemoteManagementPriv_block_invoke.149
- __CPUI_EnrollInRemoteManagementPriv_block_invoke.56
- __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.141
- __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.153
- __CPUI_EnrollInRemoteManagementPriv_block_invoke_2.57
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKDownloadDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKDownloadDelegate
- __OBJC_$_PROTOCOL_REFS__WKDownloadDelegate
- __OBJC_LABEL_PROTOCOL_$__WKDownloadDelegate
- __OBJC_PROTOCOL_$__WKDownloadDelegate
- __ZGVZL9LogToFileP8NSStringE7logPath
- __ZNKSt3__16vectorI17AuthorizationItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI17AuthorizationItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZL9LogToFileP8NSStringE7logPath
- ___98-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:completionHandler:]_block_invoke
- ___98-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:completionHandler:]_block_invoke_2
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.52
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.57
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke.68
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.53
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.61
- ___ZL14StartMDMReAuthP8NSWindowP9CPProfileP8NSStringPU31objcproto20CPUI_ProgressHandler11objc_objectU13block_pointerFvbE_block_invoke_2.69
- ___ZL16_SendMessageSyncbjP12NSDictionaryPU15__autoreleasingS0_P9CPPLoggerPU15__autoreleasingP7NSError_block_invoke.148
- ___ZL16_SendMessageSyncbjP12NSDictionaryPU15__autoreleasingS0_P9CPPLoggerPU15__autoreleasingP7NSError_block_invoke.155
- ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke.102
- ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke.81
- ___ZL19StartAccountsSignInP8NSWindowPU31objcproto20CPUI_ProgressHandler11objc_objectP8NSStringP12NSDictionaryIS4_PU8__kindofU25objcproto14NSSecureCoding8NSObjectES4_bU13block_pointerFvbPS5_P7NSErrorE_block_invoke_2.86
- ___ZL33StartBYODEnrollmentFlowControllerP27DMCEnrollmentFlowControllerP8NSStringU13block_pointerFvbbP7NSErrorE_block_invoke.186
- ___ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke.86
- ___ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke_2.96
- ___ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke_3.103
- ____ZL24ShowAlertWhyCantUnenrollP8NSWindowP7NSImageU13block_pointerFvbE_block_invoke
- ____ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke
- ____ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke_2
- ____ZL40PromptForManagedAppleAccountUnenrollmentP8NSWindowP7NSImageP9ACAccountP12NSDictionaryU13block_pointerFvbE_block_invoke_3
- ___block_descriptor_40_ea8_32bs_e37_v28?0B8"NSDictionary"12"NSError"20l
- ___block_descriptor_58_ea8_32s40s48r_e25_v16?0?<v?B"NSError">8l
- ___block_descriptor_74_ea8_32s40s48s56bs64r_e20_v20?0B8"NSError"12l
- ___block_descriptor_80_ea8_32s40s48s56s64s72s_e25_v16?0?<v?B"NSError">8l
- ___block_descriptor_88_ea8_32s40s48s56s64s72bs_e8_v16?0q8l
- ___copy_helper_block_ea8_32s40s48r
- __block_literal_global.193
- __block_literal_global.5
- __block_literal_global.736
- _objc_msgSend$_setDownloadDelegate:
- _objc_msgSend$processPool
CStrings:
+ "-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/AsyncUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/CFUtil.cp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/FileUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/LocUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/Logger.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/MiscUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/NSUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/ODUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/SecurityUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/SerialRunner.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/StdErrors.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/XPCUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/AccountsUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/AppleAccountUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPAdminRights.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPDestination.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPInstallerUIPriv.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPProfileAdminRights.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CloudConfigUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ConfigProfileUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/DMCUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/HTTPUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/MDMXPCUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ManagedAppleIDUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ProfilesPrefPaneUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/SecureBoot.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/UserManagementUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_AuthUtilPriv.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_Common/CPUI_UtilsPriv.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_Common/DMCEnrollmentMCXConnection.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_MiscPriv.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/CPUI_CloudConfiguration.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/CPUI_SACloudConfigurationHelper.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfile.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfileASWebAuth.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfileClassic.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ManagedAccounts/CPUI_ManagedAccounts.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/AccountDrivenEnrollment.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/AccountDrivenEnrollmentUI.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/CPUI_ORGOBYODPriv.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/EnrollmentControllerBase.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/ORGOBYODEnrollment.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/ORGOBYODUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/Phase2Enrollment.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ProgressWindow/CPUI_ProgressWindowController.mm"
+ "/System/Library/CoreServices/GroundhogTestStationBaseImage.plist"
+ "/tmp/MDM_DEP_%@"
+ "403 'details' is not a dictionary: %@"
+ "<CLEANED_FOR_PLIST>%@"
+ "<No AppleAccount>"
+ "@\"NSArray\"24@0:8@\"NSArray\"16"
+ "AASignInErrors"
+ "AIDAMgr (iCloud) signInService completed.  Success: %@ (already signed in: %@)"
+ "AuthKit auth error: %@"
+ "AuthKit auth returned: %@"
+ "CLEANED_FOR_PLIST_%@"
+ "CPUI_AMPCoDProxyRemoveSystemProfileWithIdentifier disallowed on this platform"
+ "Checking if servers need to be polled after clearing pending MAID state (MDM: %@)"
+ "ErrorDetails"
+ "ExplicitlyRequireFactory"
+ "Factory"
+ "Found existing acct: %@"
+ "GetEnrollmentProfile: Will use WebView to load: %@"
+ "GetEnrollmentProfileClassic"
+ "GroundhogEnabled"
+ "Have factory sentinel: %@"
+ "IsFactory (AS): %@"
+ "IsRunningAsDaemon:bootstrap_parent failed: %d"
+ "IsRunningOnFactorySecure"
+ "Obtaining CloudConfiguration profile using 'classic' URL in window: %@"
+ "Programmatic"
+ "Providing APC: %@"
+ "Providing APD: %@"
+ "ReAuth(AppleMAID) completed: %@"
+ "ReAuth(BYOD) completed: %@"
+ "Running on factory"
+ "RunningOnFactory"
+ "Silent reAuth error ==> %@"
+ "SilentEnroll"
+ "SilentEnroll: %@"
+ "Simulated iCloudSignIn failure"
+ "SimulateiCloudSignInFailure"
+ "Starting ReAuth method: %@"
+ "TB,V_isDoingOrgoPhase2"
+ "TB,V_isSilentEnroll"
+ "Test_iCloudSignInFailure"
+ "Unable to prompt for authentication since doing silent enrollment"
+ "Unable to securely verify running on factory ==> %@"
+ "UserPassword"
+ "WKDownloadDelegate"
+ "WebView: Aborting unexpected download"
+ "WebView: Download failed: %@"
+ "WebView: Requesting download of: %@"
+ "WebView: Switching to download for introspection of 403 response"
+ "WebView: Switching to download of profile"
+ "WebView: decidePolicyForNavigationResponse (%@): %@"
+ "WebView: didFailNavigation: %@"
+ "WebView: didFailProvisionalNavigation error: %@"
+ "WebView: didReceiveAuthenticationChallenge"
+ "WebView: didReceiveAuthenticationChallenge (%@)  Prot: %@ FailureCount: %@ PageCount: %@"
+ "WebView: didStartProvisionalNavigation: URL: %@"
+ "WebView: download: %@ of %@ bytes received"
+ "WebView: download: suggestedFileName: %@ from: %@"
+ "WebView: downloadDidFinish"
+ "WebView: navigationAction: %@ became download: %@"
+ "WebView: navigationDidFinishDocumentLoad"
+ "WebView: navigationResponse: %@ became download: %@"
+ "[DMCEFP] %s called.  MAID: %@  EnrollmentType: %@"
+ "[DMCEFP] %s called.  ProfileID: %@ (async: %@)"
+ "[TEST] Forcing update profile metadata for: %@"
+ "[TEST] Simulating iCloud sign-in failure"
+ "[TEST] Update profile metadata completed"
+ "[TEST] Will simulate iCloud sign-in failure after delay"
+ "__Error__"
+ "__Success__"
+ "_isDoingOrgoPhase2"
+ "_isSilentEnroll"
+ "aa_mdmServerToken"
+ "download:decideDestinationUsingResponse:suggestedFilename:completionHandler:"
+ "download:decidePlaceholderPolicy:"
+ "download:didFailWithError:resumeData:"
+ "download:didReceiveAuthenticationChallenge:completionHandler:"
+ "download:didReceiveFinalURL:"
+ "download:didReceivePlaceholderURL:completionHandler:"
+ "download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
+ "download:willPerformHTTPRedirection:newRequest:decisionHandler:"
+ "downloadDidFinish:"
+ "ensureActivationWithCompletionHandler:"
+ "extensionIDsFromESSOProfileIdentifiers:"
+ "hw.optional.x86_64"
+ "initiateDEPPushTokenSyncWithCompletionHandler:"
+ "isDoingOrgoPhase2"
+ "isSilentEnroll"
+ "localizedStringFromDate:dateStyle:timeStyle:"
+ "mdmProfileID"
+ "mdmToken.afterAuth: %@"
+ "mdmToken.afterSignIn: %@"
+ "mdmToken.startReAuth: %@"
+ "mdmToken.updateBearerToken.before: %@"
+ "opHandlePostEnrollmentSignIn skip: %@"
+ "originalRequest"
+ "requestDeviceErasureWithCompletionHandler:"
+ "requestSoftwareUpdateWithInfoDictionary:completionHandler:"
+ "requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:"
+ "setCredential:type:"
+ "setIsDoingOrgoPhase2:"
+ "setIsSilentEnroll:"
+ "setPreventsApplicationTerminationWhenModal:"
+ "startMDMUnenroll"
+ "str_MA_AccountRequiredNonRemovable_Msg"
+ "unassignFromDEPWithCompletionHandler:"
+ "updateCloudConfigurationWithRMAccountIdentifier:"
+ "updateLanguage:locale:completionHandler:"
+ "v24@0:8@\"WKDownload\"16"
+ "v32@0:8@\"WKDownload\"16@\"NSURL\"24"
+ "v32@0:8@\"WKDownload\"16@?<v@?q@\"NSURL\">24"
+ "v40@0:8@\"WKDownload\"16@\"NSError\"24@\"NSData\"32"
+ "v40@0:8@\"WKDownload\"16@\"NSURL\"24@?<v@?>32"
+ "v40@0:8@\"WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v48@0:8@\"NSData\"16@\"NSString\"24Q32@?<v@?B>40"
+ "v48@0:8@\"WKDownload\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32@?<v@?q>40"
+ "v48@0:8@\"WKDownload\"16@\"NSURLResponse\"24@\"NSString\"32@?<v@?@\"NSURL\">40"
+ "v48@0:8@16@24Q32@?40"
+ "v48@0:8@16q24q32q40"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "-[AccountEnrollmentController requestUserConsentWithProfileData:managedAppleID:completionHandler:]"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/AsyncUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/CFUtil.cp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/FileUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/LocUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/Logger.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/MiscUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/NSUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/ODUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/SecurityUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/SerialRunner.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/StdErrors.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/Common/XPCUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/AccountsUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/AppleAccountUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPAdminRights.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPDestination.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPInstallerUIPriv.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CPProfileAdminRights.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/CloudConfigUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ConfigProfileUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/DMCUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/HTTPUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/MDMXPCUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ManagedAppleIDUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/ProfilesPrefPaneUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/SecureBoot.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPCommon/UserManagementUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_AuthUtilPriv.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_Common/CPUI_UtilsPriv.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_Common/DMCEnrollmentMCXConnection.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CPUI_MiscPriv.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/CPUI_CloudConfiguration.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/CPUI_SACloudConfigurationHelper.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfile.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfileASWebAuth.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/CloudConfiguration/GetEnrollmentProfileClassic.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ManagedAccounts/CPUI_ManagedAccounts.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/AccountDrivenEnrollment.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/AccountDrivenEnrollmentUI.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/CPUI_ORGOBYODPriv.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/EnrollmentControllerBase.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/ORGOBYODEnrollment.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/ORGOBYODUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ORGOBYOD/Phase2Enrollment.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools_uiframeworks/ConfigProfiles/CPUI_Framework/ProgressWindow/CPUI_ProgressWindowController.mm"
- "/tmp/%@"
- "@\"NSString\"40@0:8@\"_WKDownload\"16@\"NSString\"24^B32"
- "@40@0:8@16@24^B32"
- "AIDAMgr (iCloud) signInService completed.  Success: %@"
- "B32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "Checking if servers need to be polled after MAID sign-in"
- "Download cancelled"
- "Download didCreateDestination: %@"
- "Download failed: %@"
- "Download process crashed"
- "GetEnrollmentProfile: windowDidLoad.  Will load: %@"
- "Managed AppleID auth error: %@"
- "Obtaining CloudConfiguration profile using 'classic' URL."
- "ReAuth method: %@"
- "WKDownload.downloadDidStart"
- "WKWebView: decidePolicyForNavigationResponse (%@): %@"
- "WKWebView: didFailNavigation: %@"
- "WKWebView: didFailProvisionalNavigation error: %@"
- "WKWebView: didReceiveAuthenticationChallenge (%@)  Prot: %@ FailureCount: %@ PageCount: %@"
- "WKWebView: didStartProvisionalNavigation: URL: %@"
- "WKWebView: navigationDidFinishDocumentLoad"
- "[DMCEFP] %s called.  MAID: %@"
- "_WKDownloadDelegate"
- "_download:decideDestinationWithSuggestedFilename: %@ from: %@"
- "_download:decideDestinationWithSuggestedFilename:allowOverwrite:"
- "_download:decideDestinationWithSuggestedFilename:completionHandler:"
- "_download:didCreateDestination:"
- "_download:didFailWithError:"
- "_download:didReceiveAuthenticationChallenge:completionHandler:"
- "_download:didReceiveData:"
- "_download:didReceiveResponse:"
- "_download:didReceiveServerRedirectToURL:"
- "_download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
- "_download:shouldDecodeSourceDataOfMIMEType:"
- "_downloadDidCancel:"
- "_downloadDidFinish:"
- "_downloadDidStart:"
- "_downloadProcessDidCrash:"
- "_setDownloadDelegate:"
- "processPool"
- "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
- "str_Err_DownloadProcessCrashed"
- "v24@0:8@\"_WKDownload\"16"
- "v32@0:8@\"_WKDownload\"16@\"NSError\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURL\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURLResponse\"24"
- "v32@0:8@\"_WKDownload\"16Q24"
- "v32@0:8@16Q24"
- "v40@0:8@\"_WKDownload\"16@\"NSString\"24@?<v@?B@\"NSString\">32"
- "v40@0:8@\"_WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v48@0:8@\"_WKDownload\"16Q24Q32Q40"
- "v48@0:8@16Q24Q32Q40"

```
