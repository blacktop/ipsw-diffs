## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.0.61.0.0
-  __TEXT.__text: 0xf9544
-  __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_methlist: 0x9ad8
-  __TEXT.__const: 0x4b24
-  __TEXT.__gcc_except_tab: 0x1aa0
-  __TEXT.__oslogstring: 0x6881
-  __TEXT.__cstring: 0xe2b7
+2005.40.31.0.0
+  __TEXT.__text: 0xfc89c
+  __TEXT.__auth_stubs: 0x2480
+  __TEXT.__objc_methlist: 0x9cd8
+  __TEXT.__const: 0x4b14
+  __TEXT.__gcc_except_tab: 0x1afc
+  __TEXT.__oslogstring: 0x6ce1
+  __TEXT.__cstring: 0xe627
   __TEXT.__dlopen_cstrs: 0x4bb
-  __TEXT.__swift5_typeref: 0x1938
+  __TEXT.__swift5_typeref: 0x1962
   __TEXT.__constg_swiftt: 0xf7c
-  __TEXT.__swift5_reflstr: 0x84e
-  __TEXT.__swift5_fieldmd: 0xa40
+  __TEXT.__swift5_reflstr: 0x85e
+  __TEXT.__swift5_fieldmd: 0xa4c
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__swift5_capture: 0xc8c

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift_as_ret: 0xd8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x43d8
-  __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0x2272
-  __TEXT.__objc_methname: 0xfb73
-  __TEXT.__objc_methtype: 0x4879
-  __TEXT.__objc_stubs: 0xa760
-  __DATA_CONST.__got: 0xb10
-  __DATA_CONST.__const: 0x49e0
-  __DATA_CONST.__objc_classlist: 0x838
-  __DATA_CONST.__objc_protolist: 0x630
+  __TEXT.__unwind_info: 0x44a8
+  __TEXT.__eh_frame: 0x2450
+  __TEXT.__objc_classname: 0x22f1
+  __TEXT.__objc_methname: 0xfe97
+  __TEXT.__objc_methtype: 0x499b
+  __TEXT.__objc_stubs: 0xa8a0
+  __DATA_CONST.__got: 0xb28
+  __DATA_CONST.__const: 0x4b10
+  __DATA_CONST.__objc_classlist: 0x848
+  __DATA_CONST.__objc_protolist: 0x660
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b88
-  __DATA_CONST.__objc_protorefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x3c30
+  __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__const: 0x3aa8
-  __AUTH_CONST.__cfstring: 0x6580
-  __AUTH_CONST.__objc_const: 0x39cc8
+  __AUTH_CONST.__auth_got: 0x1250
+  __AUTH_CONST.__const: 0x3bc8
+  __AUTH_CONST.__cfstring: 0x6640
+  __AUTH_CONST.__objc_const: 0x3aca0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x3c30
-  __AUTH.__data: 0xe78
-  __DATA.__objc_ivar: 0x838
-  __DATA.__data: 0x4ff8
-  __DATA.__bss: 0x2c79
+  __AUTH.__objc_data: 0x3cf8
+  __AUTH.__data: 0xe90
+  __DATA.__objc_ivar: 0x844
+  __DATA.__data: 0x5210
+  __DATA.__bss: 0x2ca9
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x1e60
   __DATA_DIRTY.__data: 0x280
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5C32EAEB-3425-3211-8F84-5AAAF4A7978E
-  Functions: 6382
-  Symbols:   22181
-  CStrings:  6882
+  UUID: 3BAFFD11-F247-3FE3-9316-482B500447F2
+  Functions: 6454
+  Symbols:   22446
+  CStrings:  6969
 
Symbols:
+ +[LACCredentialSignpostEvent sharedInstance]
+ +[LACCredentialSignpostEvent sharedInstance].cold.1
+ +[LACSysUtility sharedInstance]
+ +[LACSysUtility sharedInstance].cold.1
+ -[LACACMHelper ageForDataWithType:error:]
+ -[LACACMHelper performNumberContextBlock:error:]
+ -[LACAuditToken .cxx_destruct]
+ -[LACAuditToken belongsToPlatformBinary:]
+ -[LACAuditToken belongsToPlatformBinary:].cold.1
+ -[LACAuditToken signingID:]
+ -[LACAuditToken signingID:].cold.1
+ -[LACCredentialSignpostEvent extractableCredentialFailedReadAttemptWithAge:signingID:]
+ -[LACCredentialSignpostEvent extractableCredentialFailedWriteAttemptWithSigningID:]
+ -[LACCredentialSignpostEvent extractableCredentialReadAttemptWithAge:accessAllowed:]
+ -[LACCredentialSignpostEvent extractableCredentialWriteAttemptWithAccessAllowed:]
+ -[LACDeviceLifecycleManager rebootDeviceWithReason:forced:completion:]
+ -[LACPreboardLauncher _terminateApp:]
+ -[LACPreboardLauncher _terminateApp:].cold.1
+ -[LACPreboardLauncher initWithLifecycleManager:]
+ -[LACSysUtility _getCodeSigningConfig]
+ -[LACSysUtility _getCodeSigningConfig].cold.1
+ -[LACSysUtility _getCodeSigningMonitorType]
+ -[LACSysUtility _getCodeSigningMonitorType].cold.1
+ -[LACSysUtility _hasCodeSigningMonitorOfType:]
+ -[LACSysUtility hasCodeSigningMonitor]
+ -[LACSysUtility hasPPL]
+ -[LACSysUtility hasTXM]
+ -[LACSysUtility txmSecurityBootMode]
+ -[LACXPCClient isFirstPartyClient]
+ -[LACXPCClient signingID]
+ GCC_except_table53
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table91
+ _$s10Foundation4UUIDVSgWOcTm
+ _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE010sysUtilityACSo09LACSecureE4Type_p_So06LACSyshJ0_ptcfC
+ _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE010sysUtilityACSo09LACSecureE4Type_p_So06LACSyshJ0_ptcfCTj
+ _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE010sysUtilityACSo09LACSecureE4Type_p_So06LACSyshJ0_ptcfCTq
+ _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE010sysUtilityACSo09LACSecureE4Type_p_So06LACSyshJ0_ptcfc
+ _$s23LocalAuthenticationCore18LACPreboardStorageC10sysUtility33_F71D1BD8614598B9F6981260B7FA3828LLSo06LACSysG4Type_pvpWvd
+ _$s23LocalAuthenticationCore6LACLogO11credentials2os6LoggerVvgZ
+ _$s23LocalAuthenticationCore6LACLogO11credentials2os6LoggerVvpZMV
+ _$sSS9hasPrefixySbSSF
+ _$sSh21_nonEmptyArrayLiteralShyxGSayxG_tcfCSS_Tt0g5Tf4g_n
+ _$sSh8containsySbxFSS_Tg5
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE022checkOriginatorCanReadB10CredentialyySo17LACOriginatorProt_pKF
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE022checkOriginatorCanReadB10CredentialyySo17LACOriginatorProt_pKFTo
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE022checkOriginatorCanReadB10CredentialyySo17LACOriginatorProt_pKFToTm
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE022checkOriginatorCanReadbC10Credential33_3083616BDF280358C5BA62532A77738FLL_13credentialAgeySo17LACOriginatorProt_p_So8NSNumberCtKFTf4nnd_n
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE023checkOriginatorCanWriteB10CredentialyySo17LACOriginatorProt_pKF
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE023checkOriginatorCanWriteB10CredentialyySo17LACOriginatorProt_pKFTo
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE023checkOriginatorCanWritebC10Credential33_3083616BDF280358C5BA62532A77738FLLyySo17LACOriginatorProt_pKFTf4nd_n
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE05fetchbC13CredentialAge33_3083616BDF280358C5BA62532A77738FLLSo8NSNumberCyKF
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE10signPoster33_3083616BDF280358C5BA62532A77738FLLSo0A21SignpostEventProvider_pvpWvd
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE12featureFlags33_3083616BDF280358C5BA62532A77738FLLSo19LACFlagsCredentials_pvpWvd
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE47checkOriginatorIsExemptedFromAccessRequirements33_3083616BDF280358C5BA62532A77738FLLySbSo17LACOriginatorProt_pFTv_r
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelper12featureFlags10signPosterABSo12LACACMHelper_p_So19LACFlagsCredentials_pSo0A21SignpostEventProvider_ptcfC
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelper12featureFlags10signPosterABSo12LACACMHelper_p_So19LACFlagsCredentials_pSo0A21SignpostEventProvider_ptcfc
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelper12featureFlags10signPosterABSo12LACACMHelper_p_So19LACFlagsCredentials_pSo0A21SignpostEventProvider_ptcfcTo
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelper33_3083616BDF280358C5BA62532A77738FLLSo12LACACMHelper_pvpWvd
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelperABSo12LACACMHelper_p_tcfC
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelperABSo12LACACMHelper_p_tcfc
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreE9acmHelperABSo12LACACMHelper_p_tcfcTo
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreEABycfC
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreEABycfc
+ _$sSo42LACCredentialExtractablePasswordAuthorizerC23LocalAuthenticationCoreEABycfcTo
+ _$sSo42LACCredentialExtractablePasswordAuthorizerCML
+ _$sSo42LACCredentialExtractablePasswordAuthorizerCMa
+ _$sSo42LACCredentialExtractablePasswordAuthorizerCfETo
+ _$sSo8NSNumberC10FoundationE14integerLiteralABSi_tcfC
+ _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
+ _$ss11_SetStorageCMn
+ _$ss11_SetStorageCySSGMD
+ _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
+ _LACEntitlementContextDataExtendedMaxAge
+ _LACLogCredentials
+ _LACLogCredentials.__logObj
+ _LACLogCredentials.cold.1
+ _LACLogCredentials.onceToken
+ _OBJC_CLASS_$_LACCredentialExtractablePasswordAuthorizer
+ _OBJC_CLASS_$_LACCredentialSignpostEvent
+ _OBJC_IVAR_$_LACAuditToken._belongsToPlatformBinary
+ _OBJC_IVAR_$_LACAuditToken._signingID
+ _OBJC_IVAR_$_LACPreboardLauncher._lifecycleManager
+ _OBJC_METACLASS_$_LACCredentialExtractablePasswordAuthorizer
+ _OBJC_METACLASS_$_LACCredentialSignpostEvent
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _SecTaskGetCodeSignStatus
+ __DATA_LACCredentialExtractablePasswordAuthorizer
+ __INSTANCE_METHODS_LACCredentialExtractablePasswordAuthorizer
+ __IVARS_LACCredentialExtractablePasswordAuthorizer
+ __METACLASS_DATA_LACCredentialExtractablePasswordAuthorizer
+ __OBJC_$_CLASS_METHODS_LACCredentialSignpostEvent
+ __OBJC_$_CLASS_PROP_LIST_LACCredentialSignpostEvent
+ __OBJC_$_CLASS_PROP_LIST_LACSysUtility
+ __OBJC_$_INSTANCE_METHODS_LACCredentialSignpostEvent
+ __OBJC_$_INSTANCE_METHODS_LACSysUtility
+ __OBJC_$_PROP_LIST_LACCredentialSignpostEvent
+ __OBJC_$_PROP_LIST_LACFeatureFlagsCredentials
+ __OBJC_$_PROP_LIST_LACSysUtility
+ __OBJC_$_PROP_LIST_LACSysUtilityType
+ __OBJC_$_PROP_LIST_LACXPCClient.90
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACACMHelper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACCredentialSignpostEventProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACFeatureFlagsCredentials
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACSysUtilityType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACACMHelper
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACCredentialSignpostEventProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACFeatureFlagsCredentials
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACSysUtilityType
+ __OBJC_$_PROTOCOL_REFS_LACACMHelper
+ __OBJC_$_PROTOCOL_REFS_LACCredentialSignpostEventProvider
+ __OBJC_$_PROTOCOL_REFS_LACFeatureFlagsCredentials
+ __OBJC_$_PROTOCOL_REFS_LACFlagsCredentials
+ __OBJC_$_PROTOCOL_REFS_LACSysUtilityType
+ __OBJC_CLASS_PROTOCOLS_$_LACACMHelper
+ __OBJC_CLASS_PROTOCOLS_$_LACCredentialSignpostEvent
+ __OBJC_CLASS_PROTOCOLS_$_LACSysUtility
+ __OBJC_CLASS_RO_$_LACCredentialSignpostEvent
+ __OBJC_LABEL_PROTOCOL_$_LACACMHelper
+ __OBJC_LABEL_PROTOCOL_$_LACCredentialSignpostEventProvider
+ __OBJC_LABEL_PROTOCOL_$_LACFeatureFlagsCredentials
+ __OBJC_LABEL_PROTOCOL_$_LACFlagsCredentials
+ __OBJC_LABEL_PROTOCOL_$_LACSysUtilityType
+ __OBJC_METACLASS_RO_$_LACCredentialSignpostEvent
+ __OBJC_PROTOCOL_$_LACACMHelper
+ __OBJC_PROTOCOL_$_LACCredentialSignpostEventProvider
+ __OBJC_PROTOCOL_$_LACFeatureFlagsCredentials
+ __OBJC_PROTOCOL_$_LACFlagsCredentials
+ __OBJC_PROTOCOL_$_LACSysUtilityType
+ ___31+[LACSysUtility sharedInstance]_block_invoke
+ ___37-[LACPreboardLauncher _terminateApp:]_block_invoke
+ ___37-[LACPreboardLauncher _terminateApp:]_block_invoke_2
+ ___38-[LACSysUtility _getCodeSigningConfig]_block_invoke
+ ___38-[LACSysUtility _getCodeSigningConfig]_block_invoke.cold.1
+ ___41-[LACACMHelper ageForDataWithType:error:]_block_invoke
+ ___41-[LACACMHelper ageForDataWithType:error:]_block_invoke.40
+ ___41-[LACACMHelper ageForDataWithType:error:]_block_invoke.40.cold.1
+ ___41-[LACACMHelper ageForDataWithType:error:]_block_invoke_2
+ ___41-[LACACMHelper ageForDataWithType:error:]_block_invoke_2.cold.1
+ ___43-[LACSysUtility _getCodeSigningMonitorType]_block_invoke
+ ___43-[LACSysUtility _getCodeSigningMonitorType]_block_invoke.cold.1
+ ___44+[LACCredentialSignpostEvent sharedInstance]_block_invoke
+ ___46-[LACPasscodeFormatter localizePasscode:type:]_block_invoke
+ ___55-[LACSecureStorage objectForRequest:completionHandler:]_block_invoke.3
+ ___66-[LACACMHelper _verifyRequirement:satisfiedForType:present:flags:]_block_invoke.89
+ ___81-[LACCredentialSignpostEvent extractableCredentialWriteAttemptWithAccessAllowed:]_block_invoke
+ ___81-[LACCredentialSignpostEvent extractableCredentialWriteAttemptWithAccessAllowed:]_block_invoke_2
+ ___83-[LACCredentialSignpostEvent extractableCredentialFailedWriteAttemptWithSigningID:]_block_invoke
+ ___83-[LACCredentialSignpostEvent extractableCredentialFailedWriteAttemptWithSigningID:]_block_invoke_2
+ ___84-[LACCredentialSignpostEvent extractableCredentialReadAttemptWithAge:accessAllowed:]_block_invoke
+ ___84-[LACCredentialSignpostEvent extractableCredentialReadAttemptWithAge:accessAllowed:]_block_invoke_2
+ ___86-[LACCredentialSignpostEvent extractableCredentialFailedReadAttemptWithAge:signingID:]_block_invoke
+ ___86-[LACCredentialSignpostEvent extractableCredentialFailedReadAttemptWithAge:signingID:]_block_invoke_2
+ ___LACLogCredentials_block_invoke
+ ___block_descriptor_33_e23_"LACSignpostEvent"8?0l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_36_e36_"NSNumber"24?0^{__ACMHandle=}8^16l
+ ___block_descriptor_40_e8_32s_e23_"LACSignpostEvent"8?0ls32l8
+ ___block_descriptor_41_e8_32s_e23_"LACSignpostEvent"8?0ls32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e23_"LACSignpostEvent"8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8r48l8s40l8
+ ___block_literal_global.154
+ ___der_key_ephdm
+ __getCodeSigningConfig.codeSigningConfig
+ __getCodeSigningConfig.onceToken
+ __getCodeSigningMonitorType.codeSigningMonitor
+ __getCodeSigningMonitorType.onceToken
+ __swiftEmptySetSingleton
+ _der_key_ephdm
+ _flat unique So17LACSysUtilityType_p
+ _objc_msgSend$_getCodeSigningConfig
+ _objc_msgSend$_getCodeSigningMonitorType
+ _objc_msgSend$_hasCodeSigningMonitorOfType:
+ _objc_msgSend$_terminateApp:
+ _objc_msgSend$belongsToPlatformBinary:
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$hasCodeSigningMonitor
+ _objc_msgSend$hasPPL
+ _objc_msgSend$hasTXM
+ _objc_msgSend$performNumberContextBlock:error:
+ _objc_msgSend$rebootDeviceWithReason:forced:completion:
+ _objc_msgSend$signingID:
+ _objc_msgSend$txmSecurityBootMode
+ _reboot3
+ _symbolic ______p So17LACSysUtilityTypeP
+ _symbolic _____ySSG s11_SetStorageC
- +[LACSysUtility isTXMDevice]
- +[LACSysUtility isTXMDevice].cold.1
- +[LACSysUtility isTXMDevice].cold.2
- +[LACSysUtility txmSecurityBootMode]
- -[LACPreboardLauncher init]
- -[LACXPCClient setAuditToken:]
- GCC_except_table66
- GCC_except_table70
- GCC_except_table72
- GCC_except_table74
- GCC_except_table76
- GCC_except_table83
- GCC_except_table86
- _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE0ACSo09LACSecureE4Type_p_tcfC
- _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE0ACSo09LACSecureE4Type_p_tcfCTj
- _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE0ACSo09LACSecureE4Type_p_tcfCTq
- _$s23LocalAuthenticationCore18LACPreboardStorageC06secureE0ACSo09LACSecureE4Type_p_tcfc
- __OBJC_$_PROP_LIST_LACXPCClient.86
- ___55-[LACSecureStorage objectForRequest:completionHandler:]_block_invoke.2
- ___60-[LACPreboardLauncher alternateSystemApp:didExitWithStatus:]_block_invoke
- ___66-[LACACMHelper _verifyRequirement:satisfiedForType:present:flags:]_block_invoke.80
- _objc_msgSend$characterAtIndex:
- _objc_msgSend$isTXMDevice
- _objc_msgSend$stringWithCharacters:length:
CStrings:
+ " enableTelemetry=YES  age=%{public,signpost.telemetry:number1,name=age}d  ok=%{public,signpost.telemetry:number2,name=ok}d "
+ " enableTelemetry=YES  age=%{public,signpost.telemetry:number1,name=age}d  sid=%{public,signpost.telemetry:string1,name=sid}@ "
+ " enableTelemetry=YES  ok=%{public,signpost.telemetry:number1,name=ok}d "
+ " enableTelemetry=YES  sid=%{public,signpost.telemetry:string1,name=sid}@ "
+ "%s (%s)"
+ "@\"<LACDeviceLifecycleManaging>\""
+ "@\"LACSignpostEvent\"20@0:8B16"
+ "@\"LACSignpostEvent\"24@0:8@\"NSString\"16"
+ "@\"LACSignpostEvent\"28@0:8@\"NSNumber\"16B24"
+ "@\"LACSignpostEvent\"32@0:8@\"NSNumber\"16@\"NSString\"24"
+ "@\"LACSignpostEvent\"8@?0"
+ "@\"NSNumber\"24@?0^{__ACMHandle=}8^@16"
+ "@\"NSNumber\"28@0:8I16^@20"
+ "B20@0:8I16"
+ "Boot mode not completed"
+ "Could not determine if audit token belongs to platform binary"
+ "Could not determine the age of the kACMContextDataTypePassphrase credential"
+ "Could not obtain signingID from audit token"
+ "CredentialExtractAge"
+ "CredentialExtractFailed"
+ "CredentialWriteAttempt"
+ "CredentialWriteFailed"
+ "Credentials"
+ "Data exchange for key: %ld failed: %@"
+ "Data exchange returned error: %@ for key: %ld but we return nil for compatibility reasons"
+ "Did exchange data: %s for key: %ld"
+ "Extracting a LACredentialTypeExtractablePassword after %ld secs requires the '%s' entitlement"
+ "Extracting a LACredentialTypeExtractablePassword requires the '%s' entitlement"
+ "Failed to get ACM context data ModificationTimestamp: %d"
+ "Failed to get SEPTimeSinceBootInMs: %d"
+ "Failed to reboot the device"
+ "LACCredentialExtractablePasswordAuthorizer"
+ "LACCredentialSignpostEvent"
+ "LACCredentialSignpostEventProvider"
+ "LACFeatureFlagsCredentials"
+ "LACFlagsCredentials"
+ "LACSysUtilityType"
+ "LocalAuthenticationCore.LACCredentialExtractablePasswordAuthorizer"
+ "Preprocessing value completed (%{private}@)"
+ "Rebooting because PreBoard failed to complete current boot mode"
+ "Received unexpected modification timestamp data %@ length: %d"
+ "Received unexpected time since boot data %@ length: %d"
+ "Requested hard reboot with result: %d"
+ "Requested soft reboot"
+ "Stashing a LACredentialTypeExtractablePassword requires the '%s' entitlement"
+ "T@\"LACCredentialSignpostEvent\",R,N"
+ "T@\"LACSysUtility\",R,N"
+ "Temporarily waiving access requirements"
+ "_belongsToPlatformBinary"
+ "_getCodeSigningConfig"
+ "_getCodeSigningMonitorType"
+ "_hasCodeSigningMonitorOfType:"
+ "_lifecycleManager"
+ "_signingID"
+ "_terminateApp:"
+ "aclForKey rid:%u returned %{private}@"
+ "aclForKey:%d rid:%u"
+ "ageForDataWithType:error:"
+ "belongsToPlatformBinary:"
+ "checkOriginatorCanReadExtractableCredential:error:"
+ "checkOriginatorCanWriteExtractableCredential:error:"
+ "com.apple.InstallAssistant."
+ "com.apple.installer.osinstallersetupd"
+ "com.apple.installer.osishelperd"
+ "com.apple.installer.osishelperd-intel"
+ "com.apple.installer.osisstashhelper"
+ "com.apple.private.LocalAuthentication.ContextData.ExtendedMaxAge"
+ "enumerateSubstringsInRange:options:usingBlock:"
+ "exchangeData forKey:%d rid:%u"
+ "exchangeData rid:%u returned %{private}@"
+ "extractableCredentialFailedReadAttemptWithAge:signingID:"
+ "extractableCredentialFailedWriteAttemptWithSigningID:"
+ "extractableCredentialReadAttemptWithAge:accessAllowed:"
+ "extractableCredentialWriteAttemptWithAccessAllowed:"
+ "featureFlags"
+ "hasCodeSigningMonitor"
+ "hasPPL"
+ "hasTXM"
+ "initWithACMHelper:"
+ "initWithACMHelper:featureFlags:signPoster:"
+ "initWithLifecycleManager:"
+ "isFirstPartyClient"
+ "objectForKey rid:%u returned %{private}@"
+ "objectForKey:%d rid:%u"
+ "performNumberContextBlock:error:"
+ "processError key:%d rid:%u"
+ "processError rid:%u returned %{private}@"
+ "rebootDeviceWithReason:forced:completion:"
+ "removeObjectForKey rid:%u returned %{private}@"
+ "removeObjectForKey:%d rid:%u"
+ "setObject forKey:%d rid:%u"
+ "setObject rid:%u returned %{private}@"
+ "signPoster"
+ "signingID"
+ "signingID:"
+ "sysUtility"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
- "Data exchange is not supported for key: %ld"
- "Preprocessing value: %@ result: %@"
- "Reboot is not available on the current platform"
- "Requested reboot"
- "Unable to exchange data for key: "
- "aclForKey:%d on %{public}@ rid:%u"
- "characterAtIndex:"
- "exchangeObject rid:%u returned %@, error: %{public}@"
- "exchangeObject:%@ forKey:%d on %{public}@ rid:%u"
- "isTXMDevice"
- "objectForKey rid:%u returned %{public}@"
- "objectForKey:%d on %{public}@ rid:%u"
- "processError rid:%u returned %{public}@"
- "processError:%@ key:%@ on %{public}@ rid:%u"
- "removeObjectForKey rid:%u returned %{public}@"
- "removeObjectForKey:%d on %{public}@ rid:%u"
- "setObject rid:%u returned %{public}@"
- "setObject:%@ forKey:%d on %{public}@ rid:%u"
- "stringWithCharacters:length:"

```
