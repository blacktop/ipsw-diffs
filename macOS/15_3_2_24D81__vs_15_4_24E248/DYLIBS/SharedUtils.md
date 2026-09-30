## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/Versions/A/SharedUtils`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x24a4c
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0xc88
-  __TEXT.__const: 0x249
-  __TEXT.__cstring: 0x2d37
-  __TEXT.__oslogstring: 0xf96
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__unwind_info: 0x8a8
-  __TEXT.__objc_classname: 0x4d2
-  __TEXT.__objc_methname: 0x2d8d
-  __TEXT.__objc_methtype: 0x1469
-  __TEXT.__objc_stubs: 0x1c20
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x2d0
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x118
+1656.100.223.0.0
+  __TEXT.__text: 0x1f618
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x1154
+  __TEXT.__const: 0x221
+  __TEXT.__cstring: 0x287e
+  __TEXT.__oslogstring: 0xac8
+  __TEXT.__gcc_except_tab: 0x300
+  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__objc_classname: 0x443
+  __TEXT.__objc_methname: 0x27d4
+  __TEXT.__objc_methtype: 0x13c5
+  __TEXT.__objc_stubs: 0x16a0
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
-  __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x1460
-  __AUTH_CONST.__objc_const: 0x2b80
-  __AUTH_CONST.__objc_intobj: 0x8b8
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0xd2a
-  __DATA.__bss: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__const: 0x920
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0x1d58
+  __AUTH_CONST.__objc_intobj: 0x840
+  __AUTH.__objc_data: 0x780
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0xbaa
+  __DATA.__bss: 0x178
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: 745707D2-8DBD-3408-B294-3B3F017A267A
-  Functions: 695
-  Symbols:   1675
-  CStrings:  1406
+  UUID: BC046204-7125-3689-B9EB-7210DF6C4B1F
+  Functions: 732
+  Symbols:   1561
+  CStrings:  1184
 
Symbols:
+ +[LAInstanceIDGenerator sharedInstance].cold.1
+ +[LAInternalProtocols interfaceWithInternalProtocol:].cold.1
+ +[LAParamChecker _checkEventProcessingEventDictionary:].cold.1
+ +[LAParamChecker checkCredentialType:].cold.1
+ +[LAParamChecker checkEvent:].cold.1
+ +[LAParamChecker checkInternalOperation:options:].cold.1
+ +[LAParamChecker checkOptions:].cold.1
+ +[LAParamChecker checkPolicy:].cold.1
+ +[LAPasscodeHelper sharedInstance].cold.1
+ +[LAPasscodeHelperPasscodeStateRepository currentState].cold.1
+ +[LAUtils _eosDeviceType].cold.1
+ +[LAUtils runningInOsxRecovery].cold.1
+ +[LAUtils runningInOsxSystemContext].cold.1
+ ACMContextGetExternalForm.cold.1
+ GCC_except_table11
+ GCC_except_table22
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table77
+ LALogForCategory.cold.1
+ LA_LOG.cold.1
+ LA_LOG_LADFR.cold.1
+ LA_LOG_LAErrorHelper.cold.1
+ _LACLogService
+ _OBJC_CLASS_$_LACPolicyUtilities
+ _OBJC_CLASS_$_LACXPCInterface
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __30-[LAPasscodeHelper dumpStatus]_block_invoke.17
+ __31+[LAParamChecker checkOptions:]_block_invoke.150
+ __NSDictionaryFromACMRequirement_block_invoke.203
+ __NSDictionaryFromACMRequirement_block_invoke_2.204
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAgentProxyXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextCallbackXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACRemoteUI
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACRemoteUIHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUIMechanism
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACRemoteUI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAgentProxyXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextCallbackXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACRemoteUI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACRemoteUIHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUIMechanism
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_REFS_LACRemoteUI
+ __OBJC_$_PROTOCOL_REFS_LACUIMechanism
+ __OBJC_LABEL_PROTOCOL_$_LACAgentProxyXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextCallbackXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteUI
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteUIHost
+ __OBJC_LABEL_PROTOCOL_$_LACUIMechanism
+ __OBJC_PROTOCOL_$_LACAgentProxyXPC
+ __OBJC_PROTOCOL_$_LACContextCallbackXPC
+ __OBJC_PROTOCOL_$_LACContextExternalizing
+ __OBJC_PROTOCOL_$_LACRemoteUI
+ __OBJC_PROTOCOL_$_LACRemoteUIHost
+ __OBJC_PROTOCOL_$_LACUIMechanism
+ __OBJC_PROTOCOL_REFERENCE_$_LACAgentProxyXPC
+ __OBJC_PROTOCOL_REFERENCE_$_LACContextCallbackXPC
+ __OBJC_PROTOCOL_REFERENCE_$_LACRemoteUI
+ __OBJC_PROTOCOL_REFERENCE_$_LACRemoteUIHost
+ __OBJC_PROTOCOL_REFERENCE_$_LACUIMechanism
+ __block_literal_global.153
+ __block_literal_global.161
+ __block_literal_global.168
+ __block_literal_global.186
+ __block_literal_global.204
+ __block_literal_global.227
+ __block_literal_global.28
+ __block_literal_global.65
+ _objc_msgSend$hasBridge
+ _objc_msgSend$hasSEP
+ _objc_msgSend$interfaceForXPCProtocol:
+ _objc_msgSend$nonHiddenDeviceOwners
+ _objc_msgSend$verifyFvPassword:acmContext:kek:vek:options:error:
+ _objc_msgSend$verifyPasscodeUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:
+ _objc_msgSend$verifyPasscodeUsingPAM:userID:pamService:pamUser:pamToken:
+ updateLogLevelFromKext.cold.1
- +[LAACMHelper _errorFromACMStatus:]
- +[LAACMHelper ratchetStatusWithConfig:]
- +[LAUtils isApplePayPolicy:]
- +[LAUtils isApplePayPolicy:inApp:]
- +[LAUtils isBiometricOnlyPolicy:]
- +[LAUtils isPolicyAcceptingEmptyPassword:]
- +[LAUtils truncateString:maxLength:]
- +[LAUtils truncateString:maxLength:].cold.1
- -[LACachedExternalizedContext .cxx_destruct]
- -[LACachedExternalizedContext cachedExternalizedContext]
- -[LACachedExternalizedContext externalizationObserver]
- -[LACachedExternalizedContext externalizedContextWithError:]
- -[LACachedExternalizedContext externalizedContextWithReply:]
- -[LACachedExternalizedContext externalizedContext]
- -[LACachedExternalizedContext externalizedContext].cold.1
- -[LACachedExternalizedContext initWithExternalizationDelegate:]
- -[LACachedExternalizedContext initWithExternalizedContext:]
- -[LACachedExternalizedContext invalidateBecauseOfInvalidConnection:]
- -[LACachedExternalizedContext setCachedExternalizedContext:]
- -[LACachedExternalizedContext setExternalizationObserver:]
- -[LAErrorOysterRedactor _linkedAgainstRequiredSDKVersion].cold.1
- -[LALocalBackoffCounter actionBackoffWithReply:]
- -[LALocalBackoffCounter actionFailureWithReply:]
- -[LALocalBackoffCounter actionSuccess]
- -[LALocalBackoffCounter currentBackoffErrorWithReply:]
- -[LAPasscodeHelper .cxx_destruct]
- -[LAPasscodeHelper _currentUserID]
- -[LAPasscodeHelper _increaseFailedAttemptCountForUserID:]
- -[LAPasscodeHelper _keybagHandleForUserId:]
- -[LAPasscodeHelper _passwordPolicyStatusForUserID:]
- -[LAPasscodeHelper _resetFailedAttemptCountForUserID:]
- -[LAPasscodeHelper _shouldUseODVerifierForUserId:policy:options:]
- -[LAPasscodeHelper _shouldUsePAMVerifierForUserId:policy:options:]
- -[LAPasscodeHelper _verifyPasswordUsingMKB:acmContext:userId:options:log:]
- -[LAPasscodeHelper _verifyPasswordUsingOD:acmContext:userId:options:log:]
- -[LAPasscodeHelper _verifyPasswordUsingOD:acmContext:userId:options:log:].cold.1
- -[LAPasscodeHelper _verifyPasswordUsingOD:acmContext:userId:options:log:].cold.2
- -[LAPasscodeHelper backoffTimeIntervalForUserID:].cold.1
- -[LAPasscodeHelper init]
- -[LAPasscodeHelper verifyFvPassword:acmContext:kek:vek:options:]
- -[LAPasscodeHelper verifyPasswordUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:].cold.1
- -[LAPasscodeHelper verifyPasswordUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:].cold.2
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.1
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.2
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.3
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.4
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.5
- -[LAPasscodeHelper verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:].cold.6
- GCC_except_table12
- GCC_except_table24
- GCC_except_table56
- GCC_except_table64
- GCC_except_table66
- GCC_except_table68
- GCC_except_table70
- GCC_except_table72
- GCC_except_table74
- GCC_except_table83
- LA_LOG_INTERACTIVE.log
- LA_LOG_INTERACTIVE.once
- LA_LOG_LAServiceKit.log
- LA_LOG_LAServiceKit.once
- OBJC_IVAR_$_LACachedExternalizedContext._cachedExternalizedContext
- OBJC_IVAR_$_LACachedExternalizedContext._externalizationDelegate
- OBJC_IVAR_$_LACachedExternalizedContext._externalizationObserver
- OBJC_IVAR_$_LAPasscodeHelper._backoffEndTimeDictionary
- OBJC_IVAR_$_LAPasscodeHelper._failedAttemptsDictionary
- OBJC_IVAR_$_LAPasscodeHelper._keyBagProvider
- _IOConnectCallMethod
- _IOServiceClose
- _LACErrorCodeInternal
- _LACLogContext
- _LA_LOG_INTERACTIVE
- _LA_LOG_LAServiceKit
- _MKBGetDeviceLockStateInfo
- _MKBGetPolicyStatus
- _MKBKeyBagKeyStashCreateWithManifest
- _MKBKeyBagKeyStashCreateWithMode
- _MKBUnlockDevice
- _MKBVerifyPasswordWithContext
- _NSStringFromMechanismEvent
- _NSStringFromMechanismEventAndValue
- _NSStringFromRemoteUIEvent
- _NSStringFromRemoteUIEventAndOptions
- _OBJC_CLASS_$_LACError
- _OBJC_CLASS_$_LACKeyBagProvider
- _OBJC_CLASS_$_LACachedExternalizedContext
- _OBJC_CLASS_$_LALocalBackoffCounter
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_ODNode
- _OBJC_CLASS_$_ODSession
- _OBJC_METACLASS_$_LACachedExternalizedContext
- _OBJC_METACLASS_$_LALocalBackoffCounter
- __30-[LAPasscodeHelper dumpStatus]_block_invoke.75
- __31+[LAParamChecker checkOptions:]_block_invoke.146
- __CFMZEnabled
- __NSDictionaryFromACMRequirement_block_invoke.210
- __NSDictionaryFromACMRequirement_block_invoke_2.211
- __OBJC_$_INSTANCE_METHODS_LACachedExternalizedContext
- __OBJC_$_INSTANCE_METHODS_LALocalBackoffCounter
- __OBJC_$_INSTANCE_VARIABLES_LACachedExternalizedContext
- __OBJC_$_INSTANCE_VARIABLES_LAPasscodeHelper
- __OBJC_$_PROP_LIST_LACachedExternalizedContext
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAAgentProxyXPC
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LABackoffCounter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextCallbackXPC
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LARemoteUI
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LARemoteUIHost
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAUIMechanism
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSXPCProxyCreating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LARemoteUI
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCProxyCreating
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAAgentProxyXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_LABackoffCounter
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextCallbackXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_METHOD_TYPES_LARemoteUI
- __OBJC_$_PROTOCOL_METHOD_TYPES_LARemoteUIHost
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAUIMechanism
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCProxyCreating
- __OBJC_$_PROTOCOL_REFS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_REFS_LARemoteUI
- __OBJC_$_PROTOCOL_REFS_LAUIMechanism
- __OBJC_CLASS_PROTOCOLS_$_LALocalBackoffCounter
- __OBJC_CLASS_RO_$_LACachedExternalizedContext
- __OBJC_CLASS_RO_$_LALocalBackoffCounter
- __OBJC_LABEL_PROTOCOL_$_LAAgentProxyXPC
- __OBJC_LABEL_PROTOCOL_$_LABackoffCounter
- __OBJC_LABEL_PROTOCOL_$_LAContextCallbackXPC
- __OBJC_LABEL_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_LABEL_PROTOCOL_$_LARemoteAuthenticationOwnership
- __OBJC_LABEL_PROTOCOL_$_LARemoteContextOwnership
- __OBJC_LABEL_PROTOCOL_$_LARemoteUI
- __OBJC_LABEL_PROTOCOL_$_LARemoteUIHost
- __OBJC_LABEL_PROTOCOL_$_LAUIMechanism
- __OBJC_LABEL_PROTOCOL_$_NSXPCProxyCreating
- __OBJC_METACLASS_RO_$_LACachedExternalizedContext
- __OBJC_METACLASS_RO_$_LALocalBackoffCounter
- __OBJC_PROTOCOL_$_LAAgentProxyXPC
- __OBJC_PROTOCOL_$_LABackoffCounter
- __OBJC_PROTOCOL_$_LAContextCallbackXPC
- __OBJC_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_PROTOCOL_$_LARemoteAuthenticationOwnership
- __OBJC_PROTOCOL_$_LARemoteContextOwnership
- __OBJC_PROTOCOL_$_LARemoteUI
- __OBJC_PROTOCOL_$_LARemoteUIHost
- __OBJC_PROTOCOL_$_LAUIMechanism
- __OBJC_PROTOCOL_$_NSXPCProxyCreating
- __OBJC_PROTOCOL_REFERENCE_$_LAAgentProxyXPC
- __OBJC_PROTOCOL_REFERENCE_$_LABackoffCounter
- __OBJC_PROTOCOL_REFERENCE_$_LAContextCallbackXPC
- __OBJC_PROTOCOL_REFERENCE_$_LARemoteAuthenticationOwnership
- __OBJC_PROTOCOL_REFERENCE_$_LARemoteContextOwnership
- __OBJC_PROTOCOL_REFERENCE_$_LARemoteUI
- __OBJC_PROTOCOL_REFERENCE_$_LARemoteUIHost
- __OBJC_PROTOCOL_REFERENCE_$_LAUIMechanism
- __OBJC_PROTOCOL_REFERENCE_$_NSXPCProxyCreating
- ___20+[LAUtils hasBridge]_block_invoke
- ___30+[LAUtils isSecureBootCapable]_block_invoke
- ___32-[LAPasscodeHelper deviceOwners]_block_invoke
- ___39+[LAACMHelper ratchetStatusWithConfig:]_block_invoke
- ___41-[LAPasscodeHelper nonHiddenDeviceOwners]_block_invoke
- ___60-[LACachedExternalizedContext externalizedContextWithError:]_block_invoke
- ___60-[LACachedExternalizedContext externalizedContextWithReply:]_block_invoke
- ___95-[LAPasscodeHelper verifyPasswordUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:]_block_invoke
- ___LA_LOG_INTERACTIVE_block_invoke
- ___LA_LOG_LAServiceKit_block_invoke
- ___block_descriptor_40_e8_32s_e27_v32?0"LACADMUser"8Q16^B24l
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_89_e8_32s40s48s56s64s72s_e5_i8?0l
- ___copy_helper_block_e8_32s40b
- ___copy_helper_block_e8_32s40s48s56s64s72s
- ___destroy_helper_block_e8_32s40s48s56s64s72s
- ___get_aks_client_connection_block_invoke
- ___get_aks_client_dispatch_queue_block_invoke
- ___stdoutp
- __block_descriptor_tmp.141
- __block_descriptor_tmp.160
- __block_literal_global.132
- __block_literal_global.134
- __block_literal_global.149
- __block_literal_global.157
- __block_literal_global.162
- __block_literal_global.164
- __block_literal_global.182
- __block_literal_global.200
- __block_literal_global.223
- __block_literal_global.29
- __block_literal_global.35
- __block_literal_global.39
- __block_literal_global.81
- __copy_aks_client_connection
- __isNullOrEqualMem2
- _aks_fv_unwrap_vek_with_acm
- _aks_fv_verify_user_opts
- _ccder_blob_decode_range
- _ccder_blob_encode_body_tl
- _ccder_blob_encode_tl
- _der_utils_decode_fv_key
- _der_utils_decode_implicit_raw_octet_string_copy_len
- _der_utils_encode_fv_data
- _der_utils_encode_fv_params
- _dispatch_queue_create
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _fprintf
- _get_aks_client_connection
- _getuid
- _kMKBConfigMaxUnlockAttempts
- _kMKBInfoBackOff
- _kMKBPolicyBackOffDelay
- _kMKBPolicyFailedUnlockAttempts
- _kMKBPolicyUID
- _kODAttributeTypeFullName
- _kODAttributeTypeUniqueID
- _kODRecordTypeUsers
- _objc_msgSend$_currentUserID
- _objc_msgSend$_eosDeviceType
- _objc_msgSend$_errorFromACMStatus:
- _objc_msgSend$_increaseFailedAttemptCountForUserID:
- _objc_msgSend$_keybagHandleForUserId:
- _objc_msgSend$_passwordPolicyStatusForUserID:
- _objc_msgSend$_resetFailedAttemptCountForUserID:
- _objc_msgSend$_shouldUseODVerifierForUserId:policy:options:
- _objc_msgSend$_shouldUsePAMVerifierForUserId:policy:options:
- _objc_msgSend$_verifyPasswordUsingMKB:acmContext:userId:options:log:
- _objc_msgSend$_verifyPasswordUsingOD:acmContext:userId:options:log:
- _objc_msgSend$addExtractablePassphrase:scope:error:
- _objc_msgSend$allLocalUsers
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$cachedExternalizedContext
- _objc_msgSend$conformsToProtocol:
- _objc_msgSend$contextWasExternalized:
- _objc_msgSend$currentBackoffErrorWithReply:
- _objc_msgSend$date
- _objc_msgSend$dateByAddingTimeInterval:
- _objc_msgSend$dateWithTimeIntervalSinceNow:
- _objc_msgSend$defaultSession
- _objc_msgSend$doubleValue
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$errorWithCode:debugDescription:
- _objc_msgSend$externalizedContextWithError:
- _objc_msgSend$externalizedContextWithReply:
- _objc_msgSend$findUserByID:searchParent:
- _objc_msgSend$initWithExternalizedContext:
- _objc_msgSend$isAdministrator
- _objc_msgSend$isDeviceOwner
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$keybagForUserId:
- _objc_msgSend$nodeWithSession:type:error:
- _objc_msgSend$nullTerminatedCopy
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$rangeOfComposedCharacterSequencesForRange:
- _objc_msgSend$recordWithRecordType:name:attributes:error:
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$reset
- _objc_msgSend$setCachedExternalizedContext:
- _objc_msgSend$setData:type:error:
- _objc_msgSend$state
- _objc_msgSend$substringWithRange:
- _objc_msgSend$synchronousExternalizedContextWithError:
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$updatePasscodeSuccessAgeWithCurrentSystemUptime
- _objc_msgSend$userNameFromUID:
- _objc_msgSend$verifyFvPassword:acmContext:kek:vek:options:
- _objc_msgSend$verifyPassword:withOptions:error:
- _objc_msgSend$verifyPasswordUsingPAM:userID:pamService:pamUser:pamToken:
- _objc_opt_respondsToSelector
- _openpam_nullconv
- _pam_acct_mgmt
- _pam_authenticate
- _pam_end
- _pam_set_data
- _pam_set_item
- _pam_start
- _syslog$DARWIN_EXTSN
- get_aks_client_connection.connection
- get_aks_client_dispatch_queue.connection_queue
- get_aks_client_dispatch_queue.onceToken
- hasBridge._hasBridge
- hasBridge.onceToken
- isSecureBootCapable._hasSecureBoot
- isSecureBootCapable.onceToken
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "LACAgentProxyXPC"
+ "LACContextCallbackXPC"
+ "LACContextExternalizing"
+ "LACRemoteUI"
+ "LACRemoteUIHost"
+ "LACUIMechanism"
+ "analyticsAction:dismissing:reply:"
+ "analyticsMechanism:result:reply:"
+ "analyticsMechanism:starting:reply:"
+ "analyticsSessionStarting:dialogID:bundleID:reply:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "connectRemoteUI:requestID:reply:"
+ "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
+ "interfaceForXPCProtocol:"
+ "v24@0:8@?<v@?@\"<LACAgentProxyXPC>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v32@0:8q16@?<v@?@\"<LACRemoteAuthenticationOwnership>\"@\"NSError\">24"
+ "v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "v64@0:8@\"NSUUID\"16@\"<LACRemoteContextOwnership>\"24@\"NSString\"32@\"NSUUID\"40Q48@?<v@?@\"<LACRemoteContextOwnership>\"@\"NSError\">56"
+ "verifyPasscodeUsingAKS:acmContext:userId:policy:options:bioLockoutRecovery:"
+ "verifyPasscodeUsingPAM:userID:pamService:pamUser:pamToken:"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s: Admin [%@, %@, %@]"
- "%s: missing user ID"
- "%{public}@ has %d failed passcode attempts out of %d"
- "%{public}@ has backoff interval of %.0f seconds"
- ", options: %@"
- ", value: %@"
- "-[LAPasscodeHelper _shouldUseODVerifierForUserId:policy:options:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- ":"
- "@\"<LAContextExternalizationObserverProt>\""
- "@\"<LAContextExternalizationProt>\""
- "@\"LACKeyBagProvider\""
- "@\"NSData\""
- "@24@0:8@?<v@?@\"NSError\">16"
- "@32@0:8@16q24"
- "AKS FV verification returned %x"
- "AppleKeyStore"
- "B24@0:8q16"
- "B28@0:8q16B24"
- "B40@0:8@16q24@32"
- "B56@0:8@16@24@32@40@48"
- "BiometryLockout"
- "BiometryMatch"
- "BiometryNoMatch"
- "BiometryPresenceDetectionIn"
- "BiometryPresenceDetectionOut"
- "BiometrySensorActive"
- "BiometrySensorInactive"
- "Bootstrap"
- "CancelButtonPressed"
- "CoachingFeedback"
- "ContinueButtonPressed"
- "DeviceHandle"
- "DidAppear"
- "DidDisappear"
- "DismissButtonPressed"
- "FaceIdHighTemperature"
- "FaceIdLowPower"
- "FaceIdLowTemperature"
- "FaceIdSilentFallback"
- "Failed to fetch ratchet state and config (stat: %d)"
- "Failed to get OD node for user %{public}@: %{public}@"
- "Failed to get OD node: %{public}@"
- "Failed to get externalized context: %{public}@"
- "Failure"
- "FallbackButtonPressed"
- "GotFocus"
- "I24@0:8@16"
- "IOService:/IOResources/AppleKeyStore"
- "Invalid LAMechanismEvent: %d"
- "Invalid LARemoteUIEvent: %d"
- "Invalid string (%@)"
- "LAAgentProxyXPC"
- "LABackoffCounter"
- "LACachedExternalizedContext"
- "LAContextCallbackXPC"
- "LAContextExternalizationProt"
- "LALocalBackoffCounter"
- "LARemoteAuthenticationOwnership"
- "LARemoteContextOwnership"
- "LARemoteUI"
- "LARemoteUIHost"
- "LAServiceKit"
- "LAUIMechanism"
- "LostFocus"
- "MKB device unlock for keybag %d returned %d"
- "MKB password verification for keybag %d returned %d"
- "MKBGetPolicyStatus(): err=%d, policy=%@"
- "Missing ACM context"
- "Missing externalizationDelegate"
- "NSXPCProxyCreating"
- "None"
- "OD password verification returned %{public}@"
- "PAM verification: %u"
- "Passcode backoff"
- "PasscodeRejected"
- "PasscodeVerified"
- "Password rejected: %x"
- "Provided user is not admin"
- "PushButtonDoubleClicked"
- "PushButtonExpired"
- "RetryButtonPressed"
- "RetryTime"
- "StartedTypingPasscode"
- "T@\"<LAContextExternalizationObserverProt>\",W,N,V_externalizationObserver"
- "T@\"NSData\",&,V_cachedExternalizedContext"
- "T@\"NSData\",R,N"
- "This system %{public}s Secure Boot capable."
- "This system %{public}s bridge."
- "Unable to verify data with PAM %{public}@, token data missing"
- "Verifying user %s(%u) using PAM service: %{public}@"
- "WatchApproved"
- "_backoffEndTimeDictionary"
- "_cachedExternalizedContext"
- "_currentUserID"
- "_errorFromACMStatus:"
- "_externalizationDelegate"
- "_externalizationObserver"
- "_failedAttemptsDictionary"
- "_increaseFailedAttemptCountForUserID:"
- "_keyBagProvider"
- "_keybagHandleForUserId:"
- "_passwordPolicyStatusForUserID:"
- "_resetFailedAttemptCountForUserID:"
- "_shouldUseODVerifierForUserId:policy:options:"
- "_shouldUsePAMVerifierForUserId: %{public}@ [%@, %@, %@, %@]"
- "_shouldUsePAMVerifierForUserId: missing user ID"
- "_shouldUsePAMVerifierForUserId:policy:options:"
- "_verifyPasswordUsingMKB:acmContext:userId:options:log:"
- "_verifyPasswordUsingOD:acmContext:userId:options:log:"
- "actionBackoffWithReply:"
- "actionFailureWithReply:"
- "actionSuccess"
- "aks"
- "aks-client-queue"
- "aks_fv_unwrap_vek_with_acm"
- "allLocalUsers"
- "arrayWithObjects:count:"
- "authorization"
- "authorization_%@"
- "backoff: %{public}@"
- "cachedExternalizedContext"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "contextWasExternalized:"
- "create stash with manifest: %d"
- "create stash with mode: %d"
- "current user"
- "currentBackoffErrorWithReply:"
- "date"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "defaultSession"
- "deviceOwners method finishes with %lu owner(s)"
- "deviceOwners method starts"
- "dismissRemoteUIWasInvalidated:completionHandler:"
- "doesn't have"
- "doubleValue"
- "enumerateObjectsUsingBlock:"
- "errorWithCode:debugDescription:"
- "externalizationObserver"
- "externalizedContext"
- "externalizedContextWithError:"
- "failed to open connection to %s\n"
- "failedAttempts: %u"
- "findUserByID:searchParent:"
- "getpwuid failed: %d"
- "has"
- "i56@0:8@16@24@32@40@48"
- "i56@0:8@16@24@32@40Q48"
- "initWithExternalizationDelegate:"
- "invalidateBecauseOfInvalidConnection:"
- "is"
- "is not"
- "isAdministrator"
- "isApplePayPolicy:inApp:"
- "isBiometricOnlyPolicy:"
- "isDeviceOwner"
- "isEqualToNumber:"
- "isPolicyAcceptingEmptyPassword:"
- "kODVerifyPasswordOptionAdditionalACMData"
- "keybagForUserId:"
- "nodeWithSession:type:error:"
- "nonHiddenDeviceOwners method finishes with %lu owner(s)"
- "nonHiddenDeviceOwners method starts"
- "nullTerminatedCopy"
- "objectAtIndex:"
- "pam_acct_mgmt: %d"
- "pam_authenticate: %d"
- "pam_set_item: %d"
- "pam_start: %d"
- "q20@0:8i16"
- "rangeOfComposedCharacterSequencesForRange:"
- "ratchetStatusWithConfig:"
- "recordWithRecordType:name:attributes:error:"
- "remoteObjectProxy"
- "removeObjectForKey:"
- "reset"
- "setCachedExternalizedContext:"
- "setExternalizationObserver:"
- "substringWithRange:"
- "success"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceDate:"
- "token_%@"
- "truncateString:maxLength:"
- "updatePasscodeSuccessAgeWithCurrentSystemUptime"
- "user %d"
- "v20@0:8B16"
- "v24@0:8@?<v@?@\"<LAAgentProxyXPC>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v32@0:8q16@?<v@?@\"<LARemoteAuthenticationOwnership>\"@\"NSError\">24"
- "v32@?0@\"LACADMUser\"8Q16^B24"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "v64@0:8@\"NSUUID\"16@\"<LARemoteContextOwnership>\"24@\"NSString\"32@\"NSUUID\"40Q48@?<v@?@\"<LARemoteContextOwnership>\"@\"NSError\">56"
- "verifyFvPassword:acmContext:kek:vek:options:"
- "verifyPassword:withOptions:error:"

```
