## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-961.100.17.0.0
-  __TEXT.__text: 0x7a950
-  __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_methlist: 0x5efc
+1002.0.0.502.1
+  __TEXT.__text: 0x7d74c
+  __TEXT.__auth_stubs: 0x1470
+  __TEXT.__objc_methlist: 0x61b4
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7a2d
-  __TEXT.__oslogstring: 0xb44b
-  __TEXT.__gcc_except_tab: 0xca4
-  __TEXT.__unwind_info: 0x19e8
-  __TEXT.__objc_classname: 0xf1d
-  __TEXT.__objc_methname: 0xceb2
-  __TEXT.__objc_methtype: 0x2bfc
-  __TEXT.__objc_stubs: 0x9cc0
-  __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x1708
-  __DATA_CONST.__objc_classlist: 0x360
+  __TEXT.__cstring: 0x7bae
+  __TEXT.__oslogstring: 0xb4dd
+  __TEXT.__gcc_except_tab: 0xcbc
+  __TEXT.__unwind_info: 0x1a98
+  __TEXT.__objc_classname: 0xf79
+  __TEXT.__objc_methname: 0xd4b5
+  __TEXT.__objc_methtype: 0x2cc4
+  __TEXT.__objc_stubs: 0xa220
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__const: 0x1770
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cb8
-  __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x6b8
-  __AUTH_CONST.__auth_got: 0xa38
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x6760
-  __AUTH_CONST.__objc_const: 0xd160
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH_CONST.__objc_dictobj: 0x3c0
+  __DATA_CONST.__objc_selrefs: 0x2e00
+  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_arraydata: 0x768
+  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__cfstring: 0x6ac0
+  __AUTH_CONST.__objc_const: 0xd548
+  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x9ec
+  __DATA.__objc_ivar: 0xa18
   __DATA.__data: 0x1320
-  __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x20d0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x23c
+  __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 200C6E8C-49E1-3948-9898-37FD9583D831
-  Functions: 2659
-  Symbols:   9295
-  CStrings:  5307
+  UUID: 51C610D9-516F-3F74-97B0-E8907784AB7B
+  Functions: 2713
+  Symbols:   9462
+  CStrings:  5416
 
Symbols:
+ +[RBPropertyDomainRestriction domainRestrictionForDictionary:withError:]
+ +[RBTargetClientRestriction domainRestrictionForDictionary:withError:]
+ +[RBTargetClientRestriction domainRestrictionForDictionary:withError:].cold.1
+ +[RBXNUWrapper setGPURoleWithKernel:forPid:]
+ -[RBAssertionAcquisitionContext setTargetClientRestriction:]
+ -[RBAssertionAcquisitionContext targetClientRestriction]
+ -[RBAssertionBatchContext setTargetClientRestriction:]
+ -[RBAssertionBatchContext targetClientRestriction]
+ -[RBAssertionDescriptorValidatorContext setOriginatorProperties:]
+ -[RBAssertionDescriptorValidatorContext setTargetClientRestriction:]
+ -[RBAssertionDescriptorValidatorContext targetClientRestriction]
+ -[RBAttributeContext targetClientRestriction]
+ -[RBBundleProperties groupIdentifiers]
+ -[RBCompoundAllDomainRestriction dictionaryRepresentation]
+ -[RBCompoundAnyDomainRestriction dictionaryRepresentation]
+ -[RBCompoundNoneDomainRestriction dictionaryRepresentation]
+ -[RBDomainRestriction dictionaryRepresentation]
+ -[RBJetsamProperties overrideMemoryLimitCategoriesWithProperties:]
+ -[RBLSBundleProperties groupIdentifiers]
+ -[RBLaunchdInterface instancePropertiesFromJobProperties:]
+ -[RBLaunchdInterface submitExtensionWithExecutableURL:properties:domain:error:]
+ -[RBLaunchdInterface submitExtensionWithExecutableURL:properties:domain:error:].cold.1
+ -[RBLaunchdJobManager _adjustLaunchdJobProperties:context:]
+ -[RBLaunchdJobManager _adjustLaunchdJobProperties:context:].cold.1
+ -[RBLaunchdProperties _parseClientRestriction:]
+ -[RBLaunchdProperties clientRestriction]
+ -[RBLessThanConditionDomainRestriction dictionaryRepresentation]
+ -[RBOriginatorEntitlementDomainRestriction dictionaryRepresentation]
+ -[RBOriginatorExtensionPointRestriction dictionaryRepresentation]
+ -[RBOriginatorPropertyDomainRestriction allowsContext:withError:]
+ -[RBOriginatorPropertyDomainRestriction variantName]
+ -[RBProcess clientRestriction]
+ -[RBPropertyDomainRestriction .cxx_destruct]
+ -[RBPropertyDomainRestriction _initWithProperty:value:]
+ -[RBPropertyDomainRestriction allEntitlements]
+ -[RBPropertyDomainRestriction allowsWithProperties:error:]
+ -[RBPropertyDomainRestriction copyWithZone:]
+ -[RBPropertyDomainRestriction description]
+ -[RBPropertyDomainRestriction dictionaryRepresentation]
+ -[RBPropertyDomainRestriction hash]
+ -[RBPropertyDomainRestriction isEqual:]
+ -[RBPropertyDomainRestriction variantName]
+ -[RBTargetClientRestriction .cxx_destruct]
+ -[RBTargetClientRestriction _init]
+ -[RBTargetClientRestriction allEntitlements]
+ -[RBTargetClientRestriction allowsContext:withError:]
+ -[RBTargetClientRestriction copyWithZone:]
+ -[RBTargetClientRestriction description]
+ -[RBTargetClientRestriction dictionaryRepresentation]
+ -[RBTargetClientRestriction hash]
+ -[RBTargetClientRestriction isEqual:]
+ -[RBTargetEntitlementDomainRestriction dictionaryRepresentation]
+ -[RBTargetExtensionPointRestriction dictionaryRepresentation]
+ -[RBTargetPropertyDomainRestriction variantName]
+ -[RBTargetsHostedDomainRestriction dictionaryRepresentation]
+ -[RBTargetsSelfDomainRestriction dictionaryRepresentation]
+ -[RBXNUWrapper setGPURoleWithGPUDevice:forPid:]
+ -[RBXNUWrapper setGPURoleWithGPUDevice:forPid:].cold.1
+ -[RBXNUWrapper setGPURoleWithGPUDevice:forPid:].cold.2
+ -[RBXPCBundleProperties groupIdentifiers]
+ _NSStringFromDarwinGPURole
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_RBOriginatorPropertyDomainRestriction
+ _OBJC_CLASS_$_RBPropertyDomainRestriction
+ _OBJC_CLASS_$_RBSExtensionProcessIdentity
+ _OBJC_CLASS_$_RBTargetClientRestriction
+ _OBJC_IVAR_$_RBAssertionAcquisitionContext._targetClientRestriction
+ _OBJC_IVAR_$_RBAssertionBatchContext._targetClientRestriction
+ _OBJC_IVAR_$_RBAssertionDescriptorValidatorContext._targetClientRestriction
+ _OBJC_IVAR_$_RBAttributeContext._targetClientRestriction
+ _OBJC_IVAR_$_RBJetsamPropertyManager._extensionInstances
+ _OBJC_IVAR_$_RBJetsamPropertyManager._extensionInstancesGlobal
+ _OBJC_IVAR_$_RBLSBundleProperties._groupIdentifiers
+ _OBJC_IVAR_$_RBLaunchdProperties._clientRestriction
+ _OBJC_IVAR_$_RBProcess._clientRestriction
+ _OBJC_IVAR_$_RBPropertyDomainRestriction._numberValue
+ _OBJC_IVAR_$_RBPropertyDomainRestriction._property
+ _OBJC_IVAR_$_RBPropertyDomainRestriction._stringValue
+ _OBJC_IVAR_$_RBTargetClientRestriction._restrictions
+ _OBJC_IVAR_$_RBXPCBundleProperties._groupIdentifiers
+ _OBJC_METACLASS_$_RBOriginatorPropertyDomainRestriction
+ _OBJC_METACLASS_$_RBPropertyDomainRestriction
+ _OBJC_METACLASS_$_RBTargetClientRestriction
+ __OBJC_$_CLASS_METHODS_RBPropertyDomainRestriction
+ __OBJC_$_CLASS_METHODS_RBTargetClientRestriction
+ __OBJC_$_INSTANCE_METHODS_RBOriginatorPropertyDomainRestriction
+ __OBJC_$_INSTANCE_METHODS_RBPropertyDomainRestriction
+ __OBJC_$_INSTANCE_METHODS_RBTargetClientRestriction
+ __OBJC_$_INSTANCE_VARIABLES_RBPropertyDomainRestriction
+ __OBJC_$_INSTANCE_VARIABLES_RBTargetClientRestriction
+ __OBJC_$_PROP_LIST_RBBundleProperties.111
+ __OBJC_CLASS_RO_$_RBOriginatorPropertyDomainRestriction
+ __OBJC_CLASS_RO_$_RBPropertyDomainRestriction
+ __OBJC_CLASS_RO_$_RBTargetClientRestriction
+ __OBJC_METACLASS_RO_$_RBOriginatorPropertyDomainRestriction
+ __OBJC_METACLASS_RO_$_RBPropertyDomainRestriction
+ __OBJC_METACLASS_RO_$_RBTargetClientRestriction
+ ___56-[RBConnectionClient executeTerminateRequest:withReply:]_block_invoke.181
+ ___56-[RBConnectionClient executeTerminateRequest:withReply:]_block_invoke.183
+ ___59-[RBLaunchdJobManager _adjustLaunchdJobProperties:context:]_block_invoke
+ ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.198
+ ___63-[RBLaunchdJobManager _createAndSubmitExtensionJob:UUID:error:]_block_invoke.150
+ ___70+[RBTargetClientRestriction domainRestrictionForDictionary:withError:]_block_invoke
+ ___80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke.26
+ ___84-[RBProcess collectDiagnostic:description:domain:code:additionalPayload:completion:]_block_invoke.55
+ ___block_descriptor_74_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.295
+ ___block_literal_global.318
+ ___block_literal_global.344
+ ___block_literal_global.355
+ __xpc_type_data
+ _domainRestrictionForDictionary:withError:.onceToken.293
+ _domainRestrictionForDictionary:withError:.onceToken.315
+ _domainRestrictionForDictionary:withError:.onceToken.353
+ _domainRestrictionForDictionary:withError:.singleton.292
+ _domainRestrictionForDictionary:withError:.singleton.316
+ _domainRestrictionForDictionary:withError:.singleton.352
+ _objc_msgSend$_adjustLaunchdJobProperties:context:
+ _objc_msgSend$_parseClientRestriction:
+ _objc_msgSend$allowsWithProperties:error:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$clientRestriction
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$encodeRootObject:
+ _objc_msgSend$encodedData
+ _objc_msgSend$executableURL
+ _objc_msgSend$extensionIdentity
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$groupIdentifiers
+ _objc_msgSend$initRequiringSecureCoding:
+ _objc_msgSend$instancePropertiesFromJobProperties:
+ _objc_msgSend$jobProperties
+ _objc_msgSend$launchRequestEndpointIdentifiers
+ _objc_msgSend$launchdJobDescriptorFor:error:
+ _objc_msgSend$launchdJobProperties
+ _objc_msgSend$originatorProperties
+ _objc_msgSend$overrideMemoryLimitCategoriesWithProperties:
+ _objc_msgSend$sandboxContainer
+ _objc_msgSend$sandboxProfile
+ _objc_msgSend$setAdditionalProperties:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setClientRestriction:
+ _objc_msgSend$setEnterprisePersona:
+ _objc_msgSend$setGPURoleWithGPUDevice:forPid:
+ _objc_msgSend$setGPURoleWithKernel:forPid:
+ _objc_msgSend$setLaunchdJobProperties:
+ _objc_msgSend$setOriginatorProperties:
+ _objc_msgSend$setOverlay:
+ _objc_msgSend$setPersonaString:
+ _objc_msgSend$setSandboxContainer:
+ _objc_msgSend$setSpawnConstraint:
+ _objc_msgSend$setTargetClientRestriction:
+ _objc_msgSend$setTargetProperties:
+ _objc_msgSend$submitExtensionAtURL:properties:domain:error:
+ _objc_msgSend$submitExtensionWithExecutableURL:properties:domain:error:
+ _objc_msgSend$targetClientRestriction
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$variantName
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
- +[RBTargetPropertyDomainRestriction domainRestrictionForDictionary:withError:]
- -[RBTargetPropertyDomainRestriction .cxx_destruct]
- -[RBTargetPropertyDomainRestriction _initWithProperty:value:]
- -[RBTargetPropertyDomainRestriction allEntitlements]
- -[RBTargetPropertyDomainRestriction copyWithZone:]
- -[RBTargetPropertyDomainRestriction description]
- -[RBTargetPropertyDomainRestriction hash]
- -[RBTargetPropertyDomainRestriction isEqual:]
- -[RBXNUWrapper setGPURole:forPid:].cold.1
- -[RBXNUWrapper setGPURole:forPid:].cold.2
- GCC_except_table26
- _OBJC_IVAR_$_RBTargetPropertyDomainRestriction._numberValue
- _OBJC_IVAR_$_RBTargetPropertyDomainRestriction._property
- _OBJC_IVAR_$_RBTargetPropertyDomainRestriction._stringValue
- __OBJC_$_CLASS_METHODS_RBTargetPropertyDomainRestriction
- __OBJC_$_INSTANCE_VARIABLES_RBTargetPropertyDomainRestriction
- __OBJC_$_PROP_LIST_RBBundleProperties.107
- ___56-[RBConnectionClient executeTerminateRequest:withReply:]_block_invoke.180
- ___56-[RBConnectionClient executeTerminateRequest:withReply:]_block_invoke.182
- ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.148
- ___80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke.21
- ___84-[RBProcess collectDiagnostic:description:domain:code:additionalPayload:completion:]_block_invoke.54
- ___block_literal_global.246
- ___block_literal_global.262
- ___block_literal_global.339
- _domainRestrictionForDictionary:withError:.onceToken.244
- _domainRestrictionForDictionary:withError:.onceToken.259
- _domainRestrictionForDictionary:withError:.singleton.243
- _domainRestrictionForDictionary:withError:.singleton.260
CStrings:
+ "%@ doesn't have %@='%@'"
+ "%d Error setting Darwin GPU to \"%{public}@s\" (%d): %s"
+ "%d Set Darwin GPU to \"%{public}@s\" (%d)"
+ "'%@' Constructed job description:\n%@"
+ "'%{public}@' Submitting extension job properties (host PID %d, path %{public}@):\n%{public}@"
+ "(undefined)"
+ "(unknown)"
+ "@\"<OSLaunchdJobInstancePropertiesProtocol>\"24@0:8@\"OSLaunchdJobProperties\"16"
+ "@\"<OSLaunchdJobProtocol>\"48@0:8@\"NSURL\"16@\"OSLaunchdJobProperties\"24@\"OSLaunchdDomain\"32o^@40"
+ "@\"RBDomainRestriction\"16@0:8"
+ "Allow"
+ "Background"
+ "BundlePath"
+ "Client is not allowed to make termination request."
+ "ClientRestriction"
+ "Deny"
+ "ExtensionInstance"
+ "GroupIdentifiers"
+ "Jetsam Properties Loaded x:%lu xs:%lu e:%lu ei:%lu ee:%lu a:%lu as:%lu ai:%lu g:%lu d:%lu T:%lu"
+ "OSLaunchdErrorDomain"
+ "OriginatorProperty"
+ "Process"
+ "RBLaunchdInterface.m"
+ "RBOriginatorPropertyDomainRestriction"
+ "RBPropertyDomainRestriction"
+ "RBPropertyDomainRestriction doesn't specify property: %@"
+ "RBPropertyDomainRestriction doesn't specify value: %@"
+ "RBSRoleUserInitiated"
+ "RBTargetClientRestriction"
+ "T@\"<RBBundleProperties>\",&,N,V_originatorProperties"
+ "T@\"NSDictionary\",R,C,N,V_clientRestriction"
+ "T@\"NSSet\",R,N,V_groupIdentifiers"
+ "T@\"RBDomainRestriction\",&,N,V_targetClientRestriction"
+ "T@\"RBDomainRestriction\",N,V_targetClientRestriction"
+ "T@\"RBDomainRestriction\",R,N"
+ "T@\"RBDomainRestriction\",R,N,V_clientRestriction"
+ "T@\"RBDomainRestriction\",R,N,V_targetClientRestriction"
+ "TargetClientRestriction"
+ "UserInteractive"
+ "UserInteractiveFocal"
+ "UserInteractiveNonFocal"
+ "Utility"
+ "_adjustLaunchdJobProperties:context:"
+ "_clientRestriction"
+ "_extensionInstances"
+ "_extensionInstancesGlobal"
+ "_groupIdentifiers"
+ "_parseClientRestriction:"
+ "_targetClientRestriction"
+ "`hostless_extensions` feature is disabled."
+ "allowsWithProperties:error:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "clientRestriction"
+ "com.apple.security.application-groups"
+ "dataWithBytes:length:"
+ "dictionaryRepresentation"
+ "encodeRootObject:"
+ "encodedData"
+ "executableURL"
+ "extensionIdentity"
+ "finishEncoding"
+ "groupIdentifiers"
+ "hostless_extensions"
+ "hw.jetsam_properties_product_type"
+ "initRequiringSecureCoding:"
+ "instancePropertiesFromJobProperties:"
+ "jobProperties"
+ "launchRequestEndpointIdentifiers"
+ "launchdJobDescriptorFor:error:"
+ "launchdJobProperties"
+ "overrideMemoryLimitCategoriesWithProperties:"
+ "sandboxContainer"
+ "sandboxProfile"
+ "setAdditionalProperties:"
+ "setBundleIdentifier:"
+ "setClientRestriction:"
+ "setEnterprisePersona:"
+ "setGPURoleWithGPUDevice:forPid:"
+ "setGPURoleWithKernel:forPid:"
+ "setLaunchdJobProperties:"
+ "setOriginatorProperties:"
+ "setOverlay:"
+ "setPersonaString:"
+ "setSandboxContainer:"
+ "setSpawnConstraint:"
+ "setTargetClientRestriction:"
+ "submitExtensionAtURL:properties:domain:error:"
+ "submitExtensionWithExecutableURL:properties:domain:error:"
+ "targetClientRestriction"
+ "unarchivedObjectOfClass:fromData:error:"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "variantName"
- "%d Error setting Darwin GPU to \"%{public}s\": %s"
- "%d Set Darwin GPU to \"%{public}s\""
- "'"
- "'%{public}@' Constructed job description:\n%{public}@"
- "Jetsam Properties Loaded x:%lu xs:%lu e:%lu ee:%lu a:%lu as:%lu ai:%lu g:%lu d:%lu T:%lu"
- "RBTargetPropertyDomainRestriction doesn't specify property: %@"
- "RBTargetPropertyDomainRestriction doesn't specify value: %@"
- "Target doesn't have %@='%@'"
- "deny"
- "hw.targettype"

```
