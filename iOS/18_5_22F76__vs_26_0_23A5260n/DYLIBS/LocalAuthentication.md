## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x36430
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x37b8
+2005.0.13.0.0
+  __TEXT.__text: 0x37e24
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x3938
   __TEXT.__const: 0x2d4
-  __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0x19a0
+  __TEXT.__gcc_except_tab: 0x10bc
+  __TEXT.__cstring: 0x19f7
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2748
+  __TEXT.__oslogstring: 0x2aef
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__unwind_info: 0x1370
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa2f
-  __TEXT.__objc_methname: 0x6f47
-  __TEXT.__objc_methtype: 0x1d33
-  __TEXT.__objc_stubs: 0x49c0
-  __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__objc_classlist: 0x2b0
-  __DATA_CONST.__objc_protolist: 0xf8
+  __TEXT.__objc_classname: 0xa7e
+  __TEXT.__objc_methname: 0x734a
+  __TEXT.__objc_methtype: 0x1db7
+  __TEXT.__objc_stubs: 0x4d20
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__const: 0x1d18
+  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd8
+  __DATA_CONST.__objc_selrefs: 0x1ce8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x88f8
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x8b58
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x2b8
-  __DATA.__data: 0xbe8
-  __DATA.__bss: 0x420
-  __DATA_DIRTY.__objc_data: 0x1590
-  __DATA_DIRTY.__bss: 0xd0
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x2c8
+  __DATA.__data: 0xc48
+  __DATA.__bss: 0x410
+  __DATA_DIRTY.__objc_data: 0x1540
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6C6FB48F-FD21-3FED-9D3F-5BF57844260B
-  Functions: 1468
-  Symbols:   5270
-  CStrings:  2264
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  UUID: 38745A15-ED4D-32B0-86C8-6894FC01A63F
+  Functions: 1519
+  Symbols:   5441
+  CStrings:  2329
 
Symbols:
+ -[LAClient _resolveUIDelegateFromDelegate:]
+ -[LAClient credentialEncodingSeedWithReply:]
+ -[LAClient credentialsUUIDWithReply:]
+ -[LAClient initWithExternalizedContext:userSession:flags:context:]
+ -[LAClient setCredential:type:options:reply:]
+ -[LAClient setCredentialsUUID:reply:]
+ -[LAContext _checkCredentialRequiresExtractionEntitlements:]
+ -[LAContext _decodeCredential:type:reply:]
+ -[LAContext _encodeCredential:type:reply:]
+ -[LAContext _setCredential:type:options:log:cid:error:]
+ -[LAContext _setCredential:type:options:log:cid:reply:]
+ -[LAContext _setCredential:type:options:log:cid:reply:].cold.1
+ -[LAContext credentialCoder]
+ -[LAContext credentialOfType:reply:].cold.1
+ -[LAContext credentialsUUIDWithReply:]
+ -[LAContext entitlementsChecker]
+ -[LAContext evaluateCorePolicy:options:error:]
+ -[LAContext initNonDisposableWithError:]
+ -[LAContext initWithExternalizedContext:userSession:flags:]
+ -[LAContext initWithExternalizedContext:userSession:flags:].cold.1
+ -[LAContext optionDisableVisionCompanion]
+ -[LAContext setCoreCredential:type:options:error:]
+ -[LAContext setCoreCredential:type:options:reply:]
+ -[LAContext setCredential:type:options:error:]
+ -[LAContext setCredential:type:options:reply:]
+ -[LAContext setCredentialCoder:]
+ -[LAContext setCredentialsUUID:reply:]
+ -[LAContext setEntitlementsChecker:]
+ -[LAContext setOptionDisableVisionCompanion:]
+ -[LAContextProvider .cxx_destruct]
+ -[LAContextProvider initWithTargetUID:]
+ -[LAContextProvider initWithTargetUIDRef:]
+ -[LAContextProvider init]
+ -[LAEnvironmentServiceXPCClient _bootstrapServiceType:completion:]
+ -[LAEnvironmentServiceXPCClient _createConnectionToDaemon]
+ -[LAEnvironmentServiceXPCClient _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]
+ -[LAEnvironmentServiceXPCClient synchronousProxyToEnvironmentServiceWithCompletion:]
+ -[LAStorage processError:completionHandler:]
+ -[LAStorage setObject:forKey:withOptions:completionHandler:]
+ -[LAStorage setObject:forKey:withOptions:error:]
+ -[LAUIDelegateWeakBox event:params:reply:]
+ GCC_except_table101
+ GCC_except_table104
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table169
+ GCC_except_table36
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table71
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table93
+ GCC_except_table97
+ _LACCredentialExtractablePasswordMaxSize
+ _LACCredentialExtractablePasswordMinSize
+ _LACEntitlementExtractCredential
+ _LACEntitlementSaveExtractableCredential
+ _LACErrorCodeParameter
+ _LACLogDefault
+ _OBJC_CLASS_$_LACAuditToken
+ _OBJC_CLASS_$_LACContextCredentialCoder
+ _OBJC_CLASS_$_LACEntitlementsChecker
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACGlobalDomain
+ _OBJC_CLASS_$_LACParamChecker
+ _OBJC_CLASS_$_LACSExtractablePassword
+ _OBJC_CLASS_$_LACTCCManager
+ _OBJC_CLASS_$_LACWeakBox
+ _OBJC_CLASS_$_LACXPCInterface
+ _OBJC_CLASS_$_LAEnvironmentServiceXPCClient
+ _OBJC_CLASS_$_LAUIDelegateWeakBox
+ _OBJC_IVAR_$_LAContext._credentialCoder
+ _OBJC_IVAR_$_LAContext._entitlementsChecker
+ _OBJC_IVAR_$_LAContext._flags
+ _OBJC_IVAR_$_LAContextProvider._uidRef
+ _OBJC_IVAR_$_LAEnvironment._xpcClient
+ _OBJC_IVAR_$_LAExtractablePassword._password
+ _OBJC_METACLASS_$_LACWeakBox
+ _OBJC_METACLASS_$_LAEnvironmentServiceXPCClient
+ _OBJC_METACLASS_$_LAUIDelegateWeakBox
+ _OUTLINED_FUNCTION_3
+ __OBJC_$_INSTANCE_METHODS_LAEnvironmentServiceXPCClient
+ __OBJC_$_INSTANCE_METHODS_LAUIDelegateWeakBox
+ __OBJC_$_INSTANCE_VARIABLES_LAContextProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACLegacyNotificationPosting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACSecureStorageService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACLegacyNotificationPosting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACSecureStorageService
+ __OBJC_$_PROTOCOL_REFS_LACLegacyNotificationPosting
+ __OBJC_$_PROTOCOL_REFS_LACSecureStorageService
+ __OBJC_CLASS_PROTOCOLS_$_LAUIDelegateWeakBox
+ __OBJC_CLASS_RO_$_LAEnvironmentServiceXPCClient
+ __OBJC_CLASS_RO_$_LAUIDelegateWeakBox
+ __OBJC_LABEL_PROTOCOL_$_LACLegacyNotificationPosting
+ __OBJC_LABEL_PROTOCOL_$_LACSecureStorageService
+ __OBJC_METACLASS_RO_$_LAEnvironmentServiceXPCClient
+ __OBJC_METACLASS_RO_$_LAUIDelegateWeakBox
+ __OBJC_PROTOCOL_$_LACLegacyNotificationPosting
+ __OBJC_PROTOCOL_$_LACSecureStorageService
+ __OBJC_PROTOCOL_REFERENCE_$_LACSecureStorageService
+ ___29-[LAContext encodeWithCoder:]_block_invoke.55
+ ___29-[LAContext encodeWithCoder:]_block_invoke.55.cold.1
+ ___29-[LAContext encodeWithCoder:]_block_invoke.55.cold.2
+ ___29-[LAContext isCredentialSet:]_block_invoke_2
+ ___29-[LAEnvironment _updateState]_block_invoke.cold.1
+ ___36-[LAContext credentialOfType:error:]_block_invoke_2
+ ___36-[LAContext credentialOfType:reply:]_block_invoke.91
+ ___36-[LAContext credentialOfType:reply:]_block_invoke.91.cold.1
+ ___37-[LAClient credentialsUUIDWithReply:]_block_invoke
+ ___37-[LAClient setCredentialsUUID:reply:]_block_invoke
+ ___42-[LAContext _decodeCredential:type:reply:]_block_invoke
+ ___42-[LAContext _encodeCredential:type:reply:]_block_invoke
+ ___44-[LAClient credentialEncodingSeedWithReply:]_block_invoke
+ ___44-[LAStorage objectForKey:completionHandler:]_block_invoke.29
+ ___44-[LAStorage processError:completionHandler:]_block_invoke
+ ___44-[LAStorage processError:completionHandler:]_block_invoke.36
+ ___44-[LAStorage processError:completionHandler:]_block_invoke.cold.1
+ ___44-[LAStorage processError:completionHandler:]_block_invoke_2
+ ___44-[LAStorage processError:completionHandler:]_block_invoke_3
+ ___45-[LAClient setCredential:type:options:reply:]_block_invoke
+ ___48-[LAStorage setObject:forKey:withOptions:error:]_block_invoke
+ ___50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.30
+ ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.34
+ ___54-[LAClient _synchronousRemoteObjectProxy:performCall:]_block_invoke.96
+ ___55-[LAContext _setCredential:type:options:log:cid:error:]_block_invoke
+ ___55-[LAContext _setCredential:type:options:log:cid:error:]_block_invoke_2
+ ___55-[LAContext _setCredential:type:options:log:cid:reply:]_block_invoke
+ ___55-[LAContext _setCredential:type:options:log:cid:reply:]_block_invoke.90
+ ___59-[LAContext initWithExternalizedContext:userSession:flags:]_block_invoke
+ ___60-[LAStorage setObject:forKey:withOptions:completionHandler:]_block_invoke
+ ___60-[LAStorage setObject:forKey:withOptions:completionHandler:]_block_invoke.27
+ ___60-[LAStorage setObject:forKey:withOptions:completionHandler:]_block_invoke.cold.1
+ ___66-[LAClient initWithExternalizedContext:userSession:flags:context:]_block_invoke
+ ___66-[LAClient initWithExternalizedContext:userSession:flags:context:]_block_invoke_2
+ ___66-[LAContext setCredential:forProcessedEvent:credentialType:reply:]_block_invoke.82
+ ___66-[LAContext setCredential:forProcessedEvent:credentialType:reply:]_block_invoke.cold.1
+ ___66-[LAEnvironmentServiceXPCClient _bootstrapServiceType:completion:]_block_invoke
+ ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.94
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.109
+ ___84-[LAEnvironmentServiceXPCClient synchronousProxyToEnvironmentServiceWithCompletion:]_block_invoke
+ ___94-[LAEnvironmentServiceXPCClient _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]_block_invoke
+ ___block_descriptor_40_e8_32s_e55_v24?0"<LACSecureStorageService>"8?<v?"NSError">16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_48_e8_32r40r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e25_v16?0?<v?B"NSError">8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e55_v24?0"<LACSecureStorageService>"8?<v?"NSError">16ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e28_v24?0"NSData"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e8_v16?08ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e55_v24?0"<LACSecureStorageService>"8?<v?"NSError">16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s_e55_v24?0"<LACSecureStorageService>"8?<v?"NSError">16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e8_v16?0q8ls32l8s40l8s56l8s64l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e20_v24?08"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48bs56r_e20_v20?0B8"NSError"12lr56l8s32l8s40l8s48l8
+ ___block_descriptor_76_e8_32s40s48bs56w_e28_v24?0"NSData"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_84_e8_32s40s48bs56w_e28_v24?0"NSData"8"NSError"16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_84_e8_32s40s48s56bs64w_e28_v24?0"NSData"8"NSError"16lw64l8s32l8s40l8s56l8s48l8
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.87
+ ___block_literal_global.93
+ ___block_literal_global.95
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_LocalAuthentication
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_LocalAuthentication
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_LocalAuthentication
+ _dispatch_block_create
+ _dispatch_block_wait
+ _initWithExternalizedContext:userSession:flags:.onceToken
+ _objc_msgSend$_checkCredentialRequiresExtractionEntitlements:
+ _objc_msgSend$_decodeCredential:type:reply:
+ _objc_msgSend$_encodeCredential:type:reply:
+ _objc_msgSend$_resolveUIDelegateFromDelegate:
+ _objc_msgSend$_setCredential:type:options:log:cid:error:
+ _objc_msgSend$_setCredential:type:options:log:cid:reply:
+ _objc_msgSend$aclForKey:contextUUID:connection:completionHandler:
+ _objc_msgSend$checkCredentialRequiresEncoding:
+ _objc_msgSend$checkHasEntitlements:error:
+ _objc_msgSend$checkStorageOptions:
+ _objc_msgSend$connectToExistingContext:callback:clientId:flags:reply:
+ _objc_msgSend$credentialCoder
+ _objc_msgSend$credentialEncodingSeedWithReply:
+ _objc_msgSend$credentialsUUIDWithReply:
+ _objc_msgSend$data:
+ _objc_msgSend$decode:seed:error:
+ _objc_msgSend$encode:seed:error:
+ _objc_msgSend$entitlementsChecker
+ _objc_msgSend$errorWithCode:debugDescription:
+ _objc_msgSend$event:params:reply:
+ _objc_msgSend$featureFlagExtractableCredentialProtectionEnabled
+ _objc_msgSend$initWithData:error:
+ _objc_msgSend$initWithExternalizedContext:userSession:flags:
+ _objc_msgSend$initWithExternalizedContext:userSession:flags:context:
+ _objc_msgSend$initWithExternalizedContextRef:
+ _objc_msgSend$initWithRawValue:
+ _objc_msgSend$initWithReceiver:
+ _objc_msgSend$initWithTargetUIDRef:
+ _objc_msgSend$intValue
+ _objc_msgSend$interfaceForXPCProtocol:
+ _objc_msgSend$objectForKey:contextUUID:connection:completionHandler:
+ _objc_msgSend$processError:completionHandler:
+ _objc_msgSend$receiver
+ _objc_msgSend$releaseUIDelegate
+ _objc_msgSend$removeObjectForKey:contextUUID:connection:completionHandler:
+ _objc_msgSend$requestAuthorizationForService:completion:
+ _objc_msgSend$setCoreCredential:type:options:error:
+ _objc_msgSend$setCoreCredential:type:options:reply:
+ _objc_msgSend$setCredential:type:options:error:
+ _objc_msgSend$setCredential:type:options:reply:
+ _objc_msgSend$setCredentialsUUID:reply:
+ _objc_msgSend$setObject:acl:forKey:options:contextUUID:connection:completionHandler:
+ _objc_msgSend$setObject:forKey:withOptions:completionHandler:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$synchronousProxyToEnvironmentServiceWithCompletion:
+ _objc_retain_x6
- -[LAClient initWithExternalizedContext:userSession:context:]
- -[LAClient setCredential:type:reply:]
- -[LAContext _setCredential:type:log:cid:error:]
- -[LAContext _setCredential:type:log:cid:reply:]
- -[LAContext initWithExternalizedContext:userSession:].cold.1
- -[LAEnvironment _bootstrapServiceType:completion:]
- -[LAEnvironment _createConnectionToDaemon]
- -[LAEnvironment _environmentServiceEndpointWithCompletion:]
- -[LAEnvironment _synchronousProxyToEnvironmentServiceWithCompletion:]
- -[LAEnvironment _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]
- -[LAExtractablePassword init]
- GCC_except_table107
- GCC_except_table111
- GCC_except_table115
- GCC_except_table163
- GCC_except_table27
- GCC_except_table33
- GCC_except_table40
- GCC_except_table47
- GCC_except_table50
- GCC_except_table52
- GCC_except_table56
- GCC_except_table67
- GCC_except_table69
- GCC_except_table75
- GCC_except_table80
- GCC_except_table90
- GCC_except_table92
- _OBJC_CLASS_$_LACEnvironmentMechanismBiometry
- _OBJC_CLASS_$_LACEnvironmentMechanismCompanion
- _OBJC_CLASS_$_LACEnvironmentMechanismUserPassword
- _OBJC_CLASS_$_LACEnvironmentState
- _OBJC_CLASS_$_LACExtractablePasswordPersistenceBuilder
- _OBJC_CLASS_$_LACExtractablePasswordPersistenceOptions
- _OBJC_CLASS_$_LAParamChecker
- _OBJC_CLASS_$_LAUtils
- _OBJC_IVAR_$_LAEnvironment._environmentServiceEndpoint
- _OBJC_IVAR_$_LAExtractablePassword._persistence
- _TCCAccessRequest
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LASecureStorageService
- __OBJC_$_PROTOCOL_METHOD_TYPES_LASecureStorageService
- __OBJC_$_PROTOCOL_REFS_LASecureStorageService
- __OBJC_LABEL_PROTOCOL_$_LASecureStorageService
- __OBJC_PROTOCOL_$_LASecureStorageService
- __OBJC_PROTOCOL_REFERENCE_$_LASecureStorageService
- ___29-[LAContext encodeWithCoder:]_block_invoke.49
- ___29-[LAContext encodeWithCoder:]_block_invoke.49.cold.1
- ___29-[LAContext encodeWithCoder:]_block_invoke.49.cold.2
- ___29-[LAExtractablePassword init]_block_invoke
- ___37-[LAClient setCredential:type:reply:]_block_invoke
- ___44-[LAStorage objectForKey:completionHandler:]_block_invoke.28
- ___47-[LAContext _setCredential:type:log:cid:error:]_block_invoke
- ___47-[LAContext _setCredential:type:log:cid:reply:]_block_invoke
- ___48-[LAStorage setObject:forKey:completionHandler:]_block_invoke
- ___48-[LAStorage setObject:forKey:completionHandler:]_block_invoke.26
- ___48-[LAStorage setObject:forKey:completionHandler:]_block_invoke.cold.1
- ___50-[LAEnvironment _bootstrapServiceType:completion:]_block_invoke
- ___50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.29
- ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.33
- ___53-[LAContext initWithExternalizedContext:userSession:]_block_invoke
- ___54-[LAClient _synchronousRemoteObjectProxy:performCall:]_block_invoke.95
- ___60-[LAClient initWithExternalizedContext:userSession:context:]_block_invoke
- ___60-[LAClient initWithExternalizedContext:userSession:context:]_block_invoke_2
- ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.93
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.113
- ___69-[LAEnvironment _synchronousProxyToEnvironmentServiceWithCompletion:]_block_invoke
- ___70-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:]_block_invoke.109
- ___78-[LAEnvironment _synchronousProxyToEnvironmentServiceWithEndpoint:completion:]_block_invoke
- ___block_descriptor_48_e8_32bs40w_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16ls32l8w40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s_e54_v24?0"<LASecureStorageService>"8?<v?"NSError">16ls32l8
- ___block_descriptor_56_e8_32s40r48r_e28_v24?0"NSData"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s_e54_v24?0"<LASecureStorageService>"8?<v?"NSError">16ls32l8s40l8
- ___block_descriptor_56_e8_32s40w_e54_v24?0"<LASecureStorageService>"8?<v?"NSError">16lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56r_e8_v12?0C8ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e8_v12?0C8ls32l8s40l8s56l8s64l8s48l8
- ___block_descriptor_76_e8_32s40s48s56r_e20_v20?0B8"NSError"12lr56l8s32l8s40l8s48l8
- ___block_descriptor_84_e8_32s40s48s56s64r_e20_v20?0B8"NSError"12ls32l8s40l8s48l8r64l8s56l8
- ___block_literal_global.212
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_LocalAuthentication
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_LocalAuthentication
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _initWithExternalizedContext:userSession:.onceToken
- _objc_msgSend$_environmentServiceEndpointWithCompletion:
- _objc_msgSend$_setCredential:type:log:cid:error:
- _objc_msgSend$_setCredential:type:log:cid:reply:
- _objc_msgSend$_synchronousProxyToEnvironmentServiceWithCompletion:
- _objc_msgSend$aclForKey:contextUUID:completionHandler:
- _objc_msgSend$auditTokenToData:
- _objc_msgSend$connectToExistingContext:callback:clientId:reply:
- _objc_msgSend$extractPassword:
- _objc_msgSend$extractPasswordWithCompletion:
- _objc_msgSend$initWithExternalizedContext:userSession:context:
- _objc_msgSend$objectForKey:contextUUID:completionHandler:
- _objc_msgSend$passwordPersistenceWithOptions:
- _objc_msgSend$remoteObjectInterface
- _objc_msgSend$removeObjectForKey:contextUUID:completionHandler:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setCredential:type:reply:
- _objc_msgSend$setObject:acl:forKey:contextUUID:completionHandler:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$stashPassword:completion:
- _swift_unknownObjectRelease
CStrings:
+ " uiDelegate:%@"
+ "%@ not forwarding %s, receiver is nil"
+ "-[LAUIDelegateWeakBox event:params:reply:]"
+ "-nd"
+ "@\"<LACSecureStorageService>\""
+ "@\"LACContextCredentialCoder\""
+ "@\"LACEntitlementsChecker\""
+ "@\"LACSExtractablePassword\""
+ "@\"LAEnvironmentServiceXPCClient\""
+ "@20@0:8I16"
+ "@40@0:8@16r^I24q32"
+ "@48@0:8@16r^I24q32@40"
+ "B48@0:8@16q24@32^@40"
+ "B60@0:8@16q24@32q40I48^@52"
+ "Did reboot for %{public}@ on %{public}@"
+ "Extracting a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675). Error: %{public}@"
+ "Failed to obtain environment endpoint %{public}@"
+ "Failed to reboot for %{public}@ on %{public}@ with error: %{public}@"
+ "Failed to set key %d with value %{public}@ and options %{public}@ on %{public}@: %{public}@"
+ "Key %d set successfully with value %{public}@ and options %{public}@ on %{public}@"
+ "LACLegacyNotificationPosting"
+ "LACSecureStorageService"
+ "LAContext[%u:%@"
+ "LAEnvironmentServiceXPCClient"
+ "LAUIDelegateWeakBox"
+ "Rebooting for %{public}@ on %{public}@"
+ "Setting key %d with value %{public}@ and options %{public}@ on %{public}@"
+ "Stashing a LACredentialTypeExtractablePassword will require the '%@' entitlement in Luckier (rdar://140411675). Error: %{public}@"
+ "T@\"<LACSecureStorageService>\",R,N,V_remoteObjectProxy"
+ "T@\"LACContextCredentialCoder\",&,N,V_credentialCoder"
+ "T@\"LACEntitlementsChecker\",&,N,V_entitlementsChecker"
+ "The provided data should have between %d and %d bytes"
+ "]"
+ "_checkCredentialRequiresExtractionEntitlements:"
+ "_credentialCoder"
+ "_decodeCredential:type:reply:"
+ "_encodeCredential:type:reply:"
+ "_entitlementsChecker"
+ "_flags"
+ "_resolveUIDelegateFromDelegate:"
+ "_setCredential:type:options:log:cid:error:"
+ "_setCredential:type:options:log:cid:reply:"
+ "_uidRef"
+ "_xpcClient"
+ "checkCredentialRequiresEncoding:"
+ "checkHasEntitlements:error:"
+ "checkStorageOptions:"
+ "connectToExistingContext:callback:clientId:flags:reply:"
+ "credentialCoder"
+ "credentialEncodingSeedWithReply:"
+ "credentialOfType:%d on %{public}@ cid:%u returned %{public}@ when attempting to decode credential"
+ "credentialsUUIDWithReply:"
+ "data:"
+ "decode:seed:error:"
+ "encode:seed:error:"
+ "entitlementsChecker"
+ "errorWithCode:debugDescription:"
+ "evaluateCorePolicy:options:error:"
+ "featureFlagExtractableCredentialProtectionEnabled"
+ "initNonDisposableWithError:"
+ "initWithData:error:"
+ "initWithExternalizedContext:userSession:flags:"
+ "initWithExternalizedContext:userSession:flags:context:"
+ "initWithExternalizedContextRef:"
+ "initWithRawValue:"
+ "initWithReceiver:"
+ "initWithTargetUID:"
+ "initWithTargetUIDRef:"
+ "intValue"
+ "interfaceForXPCProtocol:"
+ "optionDisableVisionCompanion"
+ "processError:completionHandler:"
+ "receiver"
+ "releaseUIDelegate"
+ "requestAuthorizationForService:completion:"
+ "setCoreCredential:type:options:error:"
+ "setCoreCredential:type:options:reply:"
+ "setCredential:%d type:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential"
+ "setCredential:forProcessedEvent:%d credentialType:%d on %{public}@ cid:%u returned %{public}@ when attempting to encode credential"
+ "setCredential:type:%d options:%{public}@ on %{public}@ cid:%u"
+ "setCredential:type:options:error:"
+ "setCredential:type:options:reply:"
+ "setCredentialCoder:"
+ "setCredentialsUUID:reply:"
+ "setEntitlementsChecker:"
+ "setObject:acl:forKey:options:contextUUID:connection:completionHandler:"
+ "setObject:forKey:withOptions:completionHandler:"
+ "setObject:forKey:withOptions:error:"
+ "setOptionDisableVisionCompanion:"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "synchronousProxyToEnvironmentServiceWithCompletion:"
+ "v16@?0q8"
+ "v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16"
+ "v24@?0@\"<LACSecureStorageService>\"8@?<v@?@@\"NSError\">16"
+ "v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
+ "v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16q24@32@?40"
+ "v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48"
+ "v56@0:8@16@24Q32q40@?48"
+ "v60@0:8@16q24@32q40I48@?52"
+ "v72@0:8@\"NSData\"16@\"NSData\"24q32@\"NSDictionary\"40@\"NSUUID\"48@\"NSXPCConnection\"56@?<v@?@@\"NSError\">64"
+ "v72@0:8@16@24q32@40@48@56@?64"
- "@\"<LACExtractablePasswordPersistence>\""
- "@\"<LASecureStorageService>\""
- "@\"NSXPCListenerEndpoint\""
- "@40@0:8@16^I24@32"
- "B52@0:8@16q24q32I40^@44"
- "Failed to set key %d with %{public}@ on %{public}@: %{public}@"
- "Key %d set successfully with %{public}@ on %{public}@"
- "LAContext[%u:%@ uiDelegate:%@]"
- "LAContext[%u:%@]"
- "LASecureStorageService"
- "Setting key %d with %{public}@ on %{public}@"
- "T@\"<LASecureStorageService>\",R,N,V_remoteObjectProxy"
- "_environmentServiceEndpoint"
- "_environmentServiceEndpointWithCompletion:"
- "_persistence"
- "_setCredential:type:log:cid:error:"
- "_setCredential:type:log:cid:reply:"
- "_synchronousProxyToEnvironmentServiceWithCompletion:"
- "aclForKey:contextUUID:completionHandler:"
- "auditTokenToData:"
- "connectToExistingContext:callback:clientId:reply:"
- "initWithExternalizedContext:userSession:context:"
- "objectForKey:contextUUID:completionHandler:"
- "passwordPersistenceWithOptions:"
- "remoteObjectInterface"
- "removeObjectForKey:contextUUID:completionHandler:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCredential:type:%d on %{public}@ cid:%u"
- "setObject:acl:forKey:contextUUID:completionHandler:"
- "setObject:acl:forKey:contextUUID:connection:completionHandler:"
- "setWithObjects:"
- "v12@?0C8"
- "v24@?0@\"<LASecureStorageService>\"8@?<v@?@@\"NSError\">16"
- "v40@0:8@\"NSData\"16q24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@\"NSUUID\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8q16@\"NSUUID\"24@?<v@?@@\"NSError\">32"
- "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v52@0:8@16q24q32I40@?44"
- "v56@0:8@\"NSData\"16@\"NSData\"24q32@\"NSUUID\"40@?<v@?@@\"NSError\">48"
- "v56@0:8@16@24q32@40@?48"
- "v64@0:8@\"NSData\"16@\"NSData\"24q32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56"
- "v64@0:8@16@24q32@40@48@?56"

```
