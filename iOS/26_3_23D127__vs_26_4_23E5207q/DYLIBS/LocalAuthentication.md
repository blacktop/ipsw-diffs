## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2005.80.10.0.0
-  __TEXT.__text: 0x355c4
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x3638
-  __TEXT.__const: 0x2f4
-  __TEXT.__gcc_except_tab: 0x1008
-  __TEXT.__cstring: 0x1829
+2005.100.174.0.0
+  __TEXT.__text: 0x36cc4
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x36b0
+  __TEXT.__const: 0x324
+  __TEXT.__gcc_except_tab: 0xec8
+  __TEXT.__cstring: 0x1900
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x268f
-  __TEXT.__swift5_typeref: 0x6e
+  __TEXT.__oslogstring: 0x28e3
+  __TEXT.__swift5_typeref: 0x86
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x2a
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12a0
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0x6dcc
-  __TEXT.__objc_methtype: 0x1c3a
-  __TEXT.__objc_stubs: 0x4960
-  __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x1b40
+  __TEXT.__objc_classname: 0x9e2
+  __TEXT.__objc_methname: 0x6f1b
+  __TEXT.__objc_methtype: 0x1b41
+  __TEXT.__objc_stubs: 0x4ae0
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x1af8
   __DATA_CONST.__objc_classlist: 0x298
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b90
+  __DATA_CONST.__objc_selrefs: 0x1bd8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1e0
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x1880
-  __AUTH_CONST.__objc_const: 0x8080
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0xb88
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x80c0
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH.__objc_data: 0x660
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x294
+  __DATA.__data: 0xc30
   __DATA.__bss: 0x3f0
-  __DATA_DIRTY.__objc_data: 0x1400
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: DD7DF52A-6BA7-3498-9138-F373C1AD05EF
-  Functions: 1455
-  Symbols:   5190
-  CStrings:  2212
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: FBB499AC-3493-3F4C-B107-C5FAFEFDB2E9
+  Functions: 1501
+  Symbols:   5202
+  CStrings:  2233
 
Symbols:
+ +[LARatchetErrorBuilder autoEnablementNotAllowedWithUserInfo:]
+ +[LARightStore makeStore]
+ -[LAClient _connectToServerWithRecovery:userSession:legacyService:].cold.1
+ -[LAClient externalizedContextProvider]
+ -[LAClient externalizedContextWithError:]
+ -[LAClient setExternalizedContextProvider:]
+ -[LAContext optionIgnoreExistingDoublePress]
+ -[LAContext setOptionIgnoreExistingDoublePress:]
+ -[LARatchetManager enableFeatureWithOptions:reply:]
+ -[LARatchetManager isAutoEnablementAllowed:]
+ -[LARatchetManager performArmRequestWithContext:options:completion:]
+ -[LARatchetManager resetRatchetWithReason:completion:]
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table43
+ GCC_except_table55
+ _LACDTOErrorDomain
+ _LACErrorCodeInternal
+ _LACErrorCodeNotFound
+ _LACErrorDomain
+ _LACLogAuthorization
+ _LACLogStorage
+ _LACPolicyOptionAuthenticationIdentifier
+ _OBJC_CLASS_$_LACDTOFeatureEnablementOptions
+ _OBJC_CLASS_$_LACExternalizedContextProvider
+ _OBJC_CLASS_$_LACInstanceIDGenerator
+ _OBJC_CLASS_$_LARatchetFeatureEnablementOptions
+ _OBJC_IVAR_$_LAClient._externalizedContextProvider
+ _OBJC_METACLASS_$_LARatchetFeatureEnablementOptions
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __DATA_LARatchetFeatureEnablementOptions
+ __INSTANCE_METHODS_LARatchetFeatureEnablementOptions
+ __IVARS_LARatchetFeatureEnablementOptions
+ __METACLASS_DATA_LARatchetFeatureEnablementOptions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextObserver
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizingXPC
+ __OBJC_$_PROTOCOL_REFS_LACContextObserver
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizingXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextObserver
+ __OBJC_PROTOCOL_$_LACContextExternalizingXPC
+ __OBJC_PROTOCOL_$_LACContextObserver
+ __PROPERTIES_LARatchetFeatureEnablementOptions
+ ___41-[LAClient externalizedContextWithError:]_block_invoke
+ ___41-[LAClient externalizedContextWithError:]_block_invoke_2
+ ___44-[LAStorage processError:completionHandler:]_block_invoke.27
+ ___51-[LARatchetManager enableFeatureWithOptions:reply:]_block_invoke
+ ___51-[LARatchetManager enableFeatureWithOptions:reply:]_block_invoke_2
+ ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.25
+ ___54-[LARatchetManager resetRatchetWithReason:completion:]_block_invoke
+ ___56-[LARightStore _saveRight:identifier:secret:completion:]_block_invoke_2.53
+ ___56-[LARightStore _saveRight:identifier:secret:completion:]_block_invoke_4
+ ___68-[LARatchetManager performArmRequestWithContext:options:completion:]_block_invoke
+ ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.98
+ ___block_descriptor_40_e8_32s_e37_"LACDTOFeatureEnablementOptions"8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e21_"NSMutableArray"8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e29_v24?0"NSArray"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e37_v24?0"<LAKeyStoreKey>"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e49_v24?0"<LAKeyStoreGenericPassword>"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0ls32l8s40l8w72l8s64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_LocalAuthentication
+ __swift_stdlib_reportUnimplementedInitializer
+ _keypath_get_selector_isAutoEnablement
+ _keypath_get_selector_isExtendedPolicyModeEnabled
+ _keypath_get_selector_isGracePeriodEnabled
+ _keypath_get_selector_isStrictModeEnabled
+ _keypath_get_selector_source
+ _objc_allocWithZone
+ _objc_msgSend$autoEnablementNotAllowedWithUserInfo:
+ _objc_msgSend$enableFeatureWithOptions:reply:
+ _objc_msgSend$externalizedContextProvider
+ _objc_msgSend$initWithExternalizer:
+ _objc_msgSend$initWithSource:
+ _objc_msgSend$isAutoEnablement
+ _objc_msgSend$isAutoEnablementAllowed:
+ _objc_msgSend$isExtendedPolicyModeEnabled
+ _objc_msgSend$isGracePeriodEnabled
+ _objc_msgSend$isStrictModeEnabled
+ _objc_msgSend$performArmRequestWithContext:options:completion:
+ _objc_msgSend$resetRatchetWithReason:completion:
+ _objc_msgSend$setIsAutoEnablement:
+ _objc_msgSend$setIsExtendedPolicyModeEnabled:
+ _objc_msgSend$setIsGracePeriodEnabled:
+ _objc_msgSend$setIsStrictModeEnabled:
+ _objc_msgSend$setObject:forKey:options:contextUUID:connection:completionHandler:
+ _objc_msgSend$setSource:
+ _objc_msgSend$source
+ _swift_beginAccess
+ _swift_getObjCClassFromMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_unknownObjectRelease
+ _symbolic SaySSG
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic ypSg
- +[LACustomPasswordRequirement requestCreationWithLocalizedReason:completion:]
- +[LACustomPasswordVerificationAction submitCustomPasswordAction:]
- +[LACustomPasswordVerificationAction terminateAction]
- +[LACustomPasswordVerificationAction userCancelAction]
- +[LAKeyStoreBackendBuilder buildBackend].cold.1
- -[LAClient cachedExternalizedContext]
- -[LAClient setCachedExternalizedContext:]
- -[LAClient synchronousExternalizedContextWithError:]
- -[LACustomPasswordVerificationAction .cxx_destruct]
- -[LACustomPasswordVerificationAction initWithType:]
- -[LACustomPasswordVerificationAction initWithType:customPassword:]
- -[LACustomPasswordVerificationAction isEqual:]
- -[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]
- -[LAStorage accessControlForKey:error:]
- -[LAStorage accessControl]
- -[LAStorage setAccessControl:]
- GCC_except_table161
- GCC_except_table25
- GCC_except_table26
- GCC_except_table30
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table57
- _LACStorageOperationDataExchange
- _LA_LOG
- _LA_LOG.cold.1
- _LA_LOG.log
- _LA_LOG.once
- _LA_LOG_INTERACTIVE.log
- _LA_LOG_INTERACTIVE.once
- _OBJC_CLASS_$_LACCachedExternalizedContext
- _OBJC_CLASS_$_LACustomPasswordVerificationAction
- _OBJC_CLASS_$_LAInstanceIDGenerator
- _OBJC_IVAR_$_LAClient._cachedExternalizedContext
- _OBJC_IVAR_$_LACustomPasswordVerificationAction._customPassword
- _OBJC_IVAR_$_LACustomPasswordVerificationAction._type
- _OBJC_IVAR_$_LAStorage._accessControl
- _OBJC_METACLASS_$_LACustomPasswordVerificationAction
- __OBJC_$_CLASS_METHODS_LACustomPasswordRequirement
- __OBJC_$_CLASS_METHODS_LACustomPasswordVerificationAction
- __OBJC_$_CLASS_PROP_LIST_LACustomPasswordVerificationAction
- __OBJC_$_INSTANCE_METHODS_LACustomPasswordVerificationAction
- __OBJC_$_INSTANCE_VARIABLES_LACustomPasswordVerificationAction
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAContextObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextObserver
- __OBJC_$_PROTOCOL_REFS_LAContextObserver
- __OBJC_CLASS_RO_$_LACustomPasswordVerificationAction
- __OBJC_LABEL_PROTOCOL_$_LAContextObserver
- __OBJC_METACLASS_RO_$_LACustomPasswordVerificationAction
- __OBJC_PROTOCOL_$_LAContextObserver
- ___39-[LAStorage accessControlForKey:error:]_block_invoke
- ___39-[LAStorage accessControlForKey:error:]_block_invoke_2
- ___43-[LARatchetManager enableFeatureWithReply:]_block_invoke
- ___44-[LAStorage processError:completionHandler:]_block_invoke.30
- ___51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.28
- ___52-[LAClient synchronousExternalizedContextWithError:]_block_invoke
- ___52-[LAClient synchronousExternalizedContextWithError:]_block_invoke_2
- ___56-[LARightStore _saveRight:identifier:secret:completion:]_block_invoke_2.55
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.103
- ___68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.cold.1
- ___79-[LARatchetManager performArmRequestWithIdentifier:context:options:completion:]_block_invoke
- ___LA_LOG_INTERACTIVE_block_invoke
- ___LA_LOG_block_invoke
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls32l8w48l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e38_v24?0"LAPersistedRight"8"NSError"16ls32l8w48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e37_v24?0"<LAKeyStoreKey>"8"NSError"16ls32l8w64l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0ls32l8w64l8s56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72w_e29_v24?0"NSArray"8"NSError"16ls32l8w72l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72w_e37_v24?0"<LAKeyStoreKey>"8"NSError"16ls32l8w72l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72w_e49_v24?0"<LAKeyStoreGenericPassword>"8"NSError"16ls32l8w72l8s64l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80w_e5_v8?0lw80l8s72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e5_v8?0ls32l8s40l8w88l8s80l8s48l8s56l8s64l8s72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e5_v8?0ls32l8w88l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.150
- ___block_literal_global.203
- ___block_literal_global.84
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$accessControl
- _objc_msgSend$aclForKey:contextUUID:connection:completionHandler:
- _objc_msgSend$enableFeatureActivatingGracePeriodWithReply:
- _objc_msgSend$initWithExternalizationDelegate:
- _objc_msgSend$isKeyAvailable:operation:
- _objc_msgSend$performArmRequestWithIdentifier:context:options:completion:
- _objc_msgSend$setObject:acl:forKey:options:contextUUID:connection:completionHandler:
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "#"
+ "%{public}@ invalidated stale XPC connection before creating a new one"
+ "@\"LACDTOFeatureEnablementOptions\"8@?0"
+ "@\"LACExternalizedContextProvider\""
+ "LACContextExternalizingXPC"
+ "LACContextObserver"
+ "LARatchetFeatureEnablementOptions"
+ "LocalAuthentication.Authorization._saveRight.rightForIdentifier"
+ "LocalAuthentication.Authorization._saveRight.storeGenericPassword"
+ "LocalAuthentication.Authorization._saveRight.storeKey"
+ "LocalAuthentication.Authorization.authorizeWithLocalizedReason.completion"
+ "LocalAuthentication.Authorization.authorizeWithOptions.completion"
+ "LocalAuthentication.Authorization.rightForIdentifier.fetchGenericPasswords"
+ "LocalAuthentication.Authorization.rightForIdentifier.fetchKey"
+ "LocalAuthentication.Authorization.rightForIdentifier.fetchKeys"
+ "LocalAuthentication_Private.LARatchetFeatureEnablementOptions"
+ "Retrying on externalizedContextProvider"
+ "T@\"LACExternalizedContextProvider\",&,V_externalizedContextProvider"
+ "T@\"NSString\",N,R"
+ "TB,N,VisAutoEnablement"
+ "TB,N,VisExtendedPolicyModeEnabled"
+ "TB,N,VisGracePeriodEnabled"
+ "TB,N,VisStrictModeEnabled"
+ "Tq,N,Vsource"
+ "_externalizedContextProvider"
+ "autoEnablementNotAllowedWithUserInfo:"
+ "enableFeatureWithOptions:reply:"
+ "externalizedContextProvider"
+ "externalizedContextWithError:"
+ "init()"
+ "initWithExternalizer:"
+ "initWithSource:"
+ "isAutoEnablement"
+ "isAutoEnablement: "
+ "isAutoEnablementAllowed:"
+ "isExtendedPolicyModeEnabled"
+ "isExtendedPolicyModeEnabled: "
+ "isGracePeriodEnabled"
+ "isGracePeriodEnabled: "
+ "isStrictModeEnabled"
+ "isStrictModeEnabled: "
+ "kLACServiceTypeEnvironment"
+ "kLACServiceTypeSecureStorage"
+ "optionIgnoreExistingDoublePress"
+ "performArmRequestWithContext:options:completion:"
+ "resetRatchetWithReason:completion:"
+ "setExternalizedContextProvider:"
+ "setIsAutoEnablement:"
+ "setIsExtendedPolicyModeEnabled:"
+ "setIsGracePeriodEnabled:"
+ "setIsStrictModeEnabled:"
+ "setObject:forKey:options:contextUUID:connection:completionHandler:"
+ "setOptionIgnoreExistingDoublePress:"
+ "setSource:"
+ "source"
+ "v24@0:8@\"<LACContext>\"16"
+ "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v64@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56"
+ "v64@0:8@16q24@32@40@48@?56"
- "3"
- "@\"LACCachedExternalizedContext\""
- "LAContextObserver"
- "LACustomPasswordVerificationAction"
- "Retrying on cachedExternalizedContext"
- "T@\"LACCachedExternalizedContext\",&,V_cachedExternalizedContext"
- "T@\"LACustomPasswordVerificationAction\",R"
- "T^{__SecAccessControl=},N,V_accessControl"
- "^{__SecAccessControl=}16@0:8"
- "^{__SecAccessControl=}32@0:8q16^@24"
- "_accessControl"
- "_cachedExternalizedContext"
- "_customPassword"
- "accessControl"
- "accessControlForKey:error:"
- "aclForKey:contextUUID:connection:completionHandler:"
- "initWithExternalizationDelegate:"
- "isKeyAvailable:operation:"
- "kLAServiceTypeEnvironment"
- "kLAServiceTypeSecureStorage"
- "key does not support data exchange"
- "performArmRequestWithIdentifier:context:options:completion:"
- "requestCreationWithLocalizedReason:completion:"
- "setAccessControl:"
- "setCachedExternalizedContext:"
- "setObject:acl:forKey:options:contextUUID:connection:completionHandler:"
- "submitCustomPasswordAction:"
- "synchronousExternalizedContextWithError:"
- "terminateAction"
- "userCancelAction"
- "v24@0:8@\"LAContext\"16"
- "v24@0:8^{__SecAccessControl=}16"
- "v48@0:8q16@\"NSDictionary\"24@\"<LAUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LAUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v72@0:8@\"NSData\"16@\"NSData\"24q32@\"NSDictionary\"40@\"NSUUID\"48@\"NSXPCConnection\"56@?<v@?@@\"NSError\">64"
- "v72@0:8@16@24q32@40@48@56@?64"

```
