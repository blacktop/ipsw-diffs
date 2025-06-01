## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-858.80.1.0.0
-  __TEXT.__text: 0x3cce0
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x4e58
+874.102.1.0.0
+  __TEXT.__text: 0x3f50c
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x51d8
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x3fd0
-  __TEXT.__oslogstring: 0x23d2
-  __TEXT.__gcc_except_tab: 0x504
-  __TEXT.__unwind_info: 0x1370
-  __TEXT.__objc_classname: 0xe44
-  __TEXT.__objc_methname: 0x72e7
-  __TEXT.__objc_methtype: 0x145c
-  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__cstring: 0x44af
+  __TEXT.__oslogstring: 0x25d0
+  __TEXT.__gcc_except_tab: 0x70c
+  __TEXT.__unwind_info: 0x13f0
+  __TEXT.__objc_classname: 0xe9b
+  __TEXT.__objc_methname: 0x791b
+  __TEXT.__objc_methtype: 0x14fb
+  __TEXT.__objc_stubs: 0x4860
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xbe0
-  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6d38
-  __DATA_CONST.__objc_selrefs: 0x1a40
-  __AUTH_CONST.__objc_const: 0x3b28
-  __AUTH_CONST.__cfstring: 0x56a0
+  __DATA_CONST.__objc_const: 0x7358
+  __DATA_CONST.__objc_selrefs: 0x1b50
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x2c0
+  __AUTH_CONST.__objc_const: 0x3d20
+  __AUTH_CONST.__cfstring: 0x5a60
   __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH.__objc_data: 0x1630
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x450
-  __DATA.__objc_superrefs: 0x2a0
-  __DATA.__objc_ivar: 0x510
-  __DATA.__data: 0x758
-  __DATA.__bss: 0x138
-  __DATA_DIRTY.__objc_data: 0x11d0
+  __AUTH_CONST.__auth_got: 0x700
+  __AUTH.__objc_data: 0x1720
+  __DATA.__objc_ivar: 0x580
+  __DATA.__data: 0x768
+  __DATA.__bss: 0x128
+  __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6075CF31-AC5B-39CA-ABF6-26CCBBDEE5CD
-  Functions: 1978
-  Symbols:   6300
-  CStrings:  3400
+  UUID: AAAE5D0C-5BAA-3AC5-9E84-E043232865CF
+  Functions: 2057
+  Symbols:   6554
+  CStrings:  3546
 
Symbols:
+ +[RBSMachEndpoint supportsRBSXPCSecureCoding]
+ +[RBSOpaqueProcessIdentity supportsRBSXPCSecureCoding]
+ +[RBSProcessEndowmentInfo supportsRBSXPCSecureCoding]
+ +[RBSProcessIdentity decodeFromJob:]
+ +[RBSProcessIdentity identityForLSApplicationIdentity:LSApplicationRecord:uuid:]
+ +[RBSProcessIdentity identityForUnbundledMacApplicationJobLabel:]
+ +[RBSProcessIdentity identityForWrappedInfoProvider:]
+ +[RBSProcessIdentity identityForWrappedInfoProvider:uuid:]
+ +[RBSWrappedLSInfo infoWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:]
+ -[RBSConnection executeLaunchRequest:]
+ -[RBSConnection executeLaunchRequest:].cold.1
+ -[RBSConnection managedEndpointByLaunchIdentifier]
+ -[RBSEmbeddedAppProcessIdentity _initEmbeddedAppWithAppInfo:]
+ -[RBSEmbeddedAppProcessIdentity _initEmbeddedAppWithAppInfo:].cold.1
+ -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:]
+ -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:].cold.1
+ -[RBSHandshakeResponse managedEndpointByLaunchIdentifier]
+ -[RBSHandshakeResponse setManagedEndpointByLaunchIdentifier:]
+ -[RBSLaunchContext managedEndpointLaunchIdentifiers]
+ -[RBSLaunchContext requiredExistingProcess]
+ -[RBSLaunchContext setManagedEndpointLaunchIdentifiers:]
+ -[RBSLaunchContext setRequiredExistingProcess:]
+ -[RBSLaunchRequest executeRequest]
+ -[RBSLaunchResponse .cxx_destruct]
+ -[RBSLaunchResponse _init]
+ -[RBSLaunchResponse assertion]
+ -[RBSLaunchResponse error]
+ -[RBSLaunchResponse managedEndpointByLaunchIdentifier]
+ -[RBSLaunchResponse process]
+ -[RBSLaunchResponse setAssertion:]
+ -[RBSLaunchResponse setError:]
+ -[RBSLaunchResponse setManagedEndpointByLaunchIdentifier:]
+ -[RBSLaunchResponse setProcess:]
+ -[RBSMacAppProcessIdentity _initMacAppWithInfo:auid:uuid:]
+ -[RBSMachEndpoint .cxx_destruct]
+ -[RBSMachEndpoint _copy]
+ -[RBSMachEndpoint _initWithName:nonLaunching:port:]
+ -[RBSMachEndpoint _isCachedPortValid]
+ -[RBSMachEndpoint _isEquivalentToEndpoint:]
+ -[RBSMachEndpoint description]
+ -[RBSMachEndpoint encodeWithRBSXPCCoder:]
+ -[RBSMachEndpoint endpoint]
+ -[RBSMachEndpoint initWithRBSXPCCoder:]
+ -[RBSMachEndpoint init]
+ -[RBSMachEndpoint isNonLaunching]
+ -[RBSMachEndpoint name]
+ -[RBSOSServiceProcessIdentity encodeForJob]
+ -[RBSOSServiceProcessIdentity encodeForJob].cold.1
+ -[RBSOSServiceProcessIdentity initWithDecodeFromJob:]
+ -[RBSOpaqueProcessIdentity _initOpaqueWithPid:auid:description:]
+ -[RBSOpaqueProcessIdentity _initOpaqueWithPid:name:auid:]
+ -[RBSOpaqueProcessIdentity copyWithAuid:]
+ -[RBSOpaqueProcessIdentity encodeForJob]
+ -[RBSOpaqueProcessIdentity encodeWithRBSXPCCoder:]
+ -[RBSOpaqueProcessIdentity initWithDecodeFromJob:]
+ -[RBSOpaqueProcessIdentity initWithRBSXPCCoder:]
+ -[RBSProcessEndowmentInfo .cxx_destruct]
+ -[RBSProcessEndowmentInfo _initWithNamespace:environment:encodedEndowment:]
+ -[RBSProcessEndowmentInfo _initWithNamespace:environment:encodedEndowment:].cold.1
+ -[RBSProcessEndowmentInfo copyWithZone:]
+ -[RBSProcessEndowmentInfo description]
+ -[RBSProcessEndowmentInfo encodeWithRBSXPCCoder:]
+ -[RBSProcessEndowmentInfo encodedEndowment]
+ -[RBSProcessEndowmentInfo endowmentNamespace]
+ -[RBSProcessEndowmentInfo endowment]
+ -[RBSProcessEndowmentInfo environment]
+ -[RBSProcessEndowmentInfo hash]
+ -[RBSProcessEndowmentInfo initWithRBSXPCCoder:]
+ -[RBSProcessEndowmentInfo isEqual:]
+ -[RBSProcessHandle endowmentInfoForHandle]
+ -[RBSProcessIdentity isMultiInstanceExtension]
+ -[RBSProcessState endowmentInfos]
+ -[RBSProcessState setEndowmentInfos:]
+ -[RBSService managedEndpointByLaunchIdentifier]
+ -[RBSWrappedLSInfo _initWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:]
+ -[RBSWrappedLSInfo bundleInode]
+ -[RBSWrappedLSInfo execInode]
+ -[RBSWrappedLSInfo persistentJobLabel]
+ -[RBSWrappedLSInfo platform]
+ -[RBSXPCCoder decodeDictionaryOfClass:forKey:]
+ -[RBSXPCCoder encodeDictionary:forKey:]
+ -[RBSXPCServiceProcessIdentity isMultiInstanceExtension]
+ GCC_except_table41
+ GCC_except_table5
+ _CFDictionaryGetCount
+ _OBJC_CLASS_$_RBSLaunchResponse
+ _OBJC_CLASS_$_RBSMachEndpoint
+ _OBJC_CLASS_$_RBSOpaqueProcessIdentity
+ _OBJC_CLASS_$_RBSProcessEndowmentInfo
+ _OBJC_IVAR_$_RBSConnection._managedEndpointByLaunchIdentifier
+ _OBJC_IVAR_$_RBSHandshakeResponse._managedEndpointByLaunchIdentifier
+ _OBJC_IVAR_$_RBSIdentityAndRecordInfoProvider._bundleInode
+ _OBJC_IVAR_$_RBSIdentityAndRecordInfoProvider._execInode
+ _OBJC_IVAR_$_RBSIdentityAndRecordInfoProvider._persistentJobLabel
+ _OBJC_IVAR_$_RBSIdentityAndRecordInfoProvider._platform
+ _OBJC_IVAR_$_RBSLaunchContext._managedEndpointLaunchIdentifiers
+ _OBJC_IVAR_$_RBSLaunchContext._requiredExistingProcess
+ _OBJC_IVAR_$_RBSLaunchResponse._assertion
+ _OBJC_IVAR_$_RBSLaunchResponse._error
+ _OBJC_IVAR_$_RBSLaunchResponse._managedEndpointByLaunchIdentifier
+ _OBJC_IVAR_$_RBSLaunchResponse._process
+ _OBJC_IVAR_$_RBSMachEndpoint._getterCache_endpoint
+ _OBJC_IVAR_$_RBSMachEndpoint._lock
+ _OBJC_IVAR_$_RBSMachEndpoint._lock_hasCheckedEndpoint
+ _OBJC_IVAR_$_RBSMachEndpoint._name
+ _OBJC_IVAR_$_RBSMachEndpoint._nonLaunching
+ _OBJC_IVAR_$_RBSMachEndpoint._port
+ _OBJC_IVAR_$_RBSProcessEndowmentInfo._encodedEndowment
+ _OBJC_IVAR_$_RBSProcessEndowmentInfo._encodedEndowmentHash
+ _OBJC_IVAR_$_RBSProcessEndowmentInfo._endowmentNamespace
+ _OBJC_IVAR_$_RBSProcessEndowmentInfo._environment
+ _OBJC_IVAR_$_RBSProcessEndowmentInfo._hash
+ _OBJC_IVAR_$_RBSProcessState._endowmentInfos
+ _OBJC_IVAR_$_RBSWrappedLSInfo._bundleInode
+ _OBJC_IVAR_$_RBSWrappedLSInfo._execInode
+ _OBJC_IVAR_$_RBSWrappedLSInfo._persistentJobLabel
+ _OBJC_IVAR_$_RBSWrappedLSInfo._platform
+ _OBJC_METACLASS_$_RBSLaunchResponse
+ _OBJC_METACLASS_$_RBSMachEndpoint
+ _OBJC_METACLASS_$_RBSOpaqueProcessIdentity
+ _OBJC_METACLASS_$_RBSProcessEndowmentInfo
+ _RBSServiceMessageManagedEndpointByLaunchIdentifierKey
+ __BSXPCDecodeObjectFromContext
+ __BSXPCDecodeObjectFromContext.cold.1
+ __BSXPCDecodeObjectFromContext.cold.10
+ __BSXPCDecodeObjectFromContext.cold.11
+ __BSXPCDecodeObjectFromContext.cold.12
+ __BSXPCDecodeObjectFromContext.cold.13
+ __BSXPCDecodeObjectFromContext.cold.2
+ __BSXPCDecodeObjectFromContext.cold.3
+ __BSXPCDecodeObjectFromContext.cold.4
+ __BSXPCDecodeObjectFromContext.cold.5
+ __BSXPCDecodeObjectFromContext.cold.6
+ __BSXPCDecodeObjectFromContext.cold.7
+ __BSXPCDecodeObjectFromContext.cold.8
+ __BSXPCDecodeObjectFromContext.cold.9
+ __NSIsNSDictionary
+ __OBJC_$_CLASS_METHODS_RBSMachEndpoint
+ __OBJC_$_CLASS_METHODS_RBSOpaqueProcessIdentity
+ __OBJC_$_CLASS_METHODS_RBSProcessEndowmentInfo
+ __OBJC_$_INSTANCE_METHODS_RBSLaunchResponse
+ __OBJC_$_INSTANCE_METHODS_RBSMachEndpoint
+ __OBJC_$_INSTANCE_METHODS_RBSOpaqueProcessIdentity
+ __OBJC_$_INSTANCE_METHODS_RBSProcessEndowmentInfo
+ __OBJC_$_INSTANCE_VARIABLES_RBSLaunchResponse
+ __OBJC_$_INSTANCE_VARIABLES_RBSMachEndpoint
+ __OBJC_$_INSTANCE_VARIABLES_RBSProcessEndowmentInfo
+ __OBJC_$_PROP_LIST_RBSLaunchResponse
+ __OBJC_$_PROP_LIST_RBSMachEndpoint
+ __OBJC_$_PROP_LIST_RBSProcessEndowmentInfo
+ __OBJC_CLASS_PROTOCOLS_$_RBSMachEndpoint
+ __OBJC_CLASS_PROTOCOLS_$_RBSProcessEndowmentInfo
+ __OBJC_CLASS_RO_$_RBSLaunchResponse
+ __OBJC_CLASS_RO_$_RBSMachEndpoint
+ __OBJC_CLASS_RO_$_RBSOpaqueProcessIdentity
+ __OBJC_CLASS_RO_$_RBSProcessEndowmentInfo
+ __OBJC_METACLASS_RO_$_RBSLaunchResponse
+ __OBJC_METACLASS_RO_$_RBSMachEndpoint
+ __OBJC_METACLASS_RO_$_RBSOpaqueProcessIdentity
+ __OBJC_METACLASS_RO_$_RBSProcessEndowmentInfo
+ __RBSXPCEncodeObjectForKey.cold.1
+ ___27-[RBSConnection _handshake]_block_invoke.cold.5
+ ___41-[RBSProcessStateDescriptor filterState:]_block_invoke
+ ___50-[RBSConnection managedEndpointByLaunchIdentifier]_block_invoke
+ ____BSXPCDecodeObject_block_invoke.202
+ ____BSXPCDecodeObject_block_invoke.cold.1
+ ____RBSXPCEncodeObjectForKey_block_invoke_3
+ ___block_descriptor_48_e8_32s40r_e37_v24?0"RBSProcessEndowmentInfo"8^B16ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48r_e37_B24?0r*8"NSObject<OS_xpc_object>"16ls32l8u56l8s40l8r48l8
+ ___block_literal_global.128
+ ___block_literal_global.59
+ ___block_literal_global.62
+ _dispatch_async_and_wait
+ _executeLaunchRequest:.permanentError
+ _objc_msgSend$_initEmbeddedApp:personaString:
+ _objc_msgSend$_initEmbeddedAppWithAppInfo:
+ _objc_msgSend$_initEmbeddedAppWithBundleID:
+ _objc_msgSend$_initOpaqueWithPid:auid:description:
+ _objc_msgSend$_initOpaqueWithPid:name:auid:
+ _objc_msgSend$_initWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:
+ _objc_msgSend$_initWithName:nonLaunching:port:
+ _objc_msgSend$_initWithNamespace:environment:encodedEndowment:
+ _objc_msgSend$_initWithXPCServiceID:pid:auid:
+ _objc_msgSend$_isCachedPortValid
+ _objc_msgSend$_isEquivalentToEndpoint:
+ _objc_msgSend$assertion
+ _objc_msgSend$decodeDictionaryOfClass:forKey:
+ _objc_msgSend$decodeFromJob:
+ _objc_msgSend$decodeTopLevelObjectOfClasses:forKey:error:
+ _objc_msgSend$encodeCollection:forKey:
+ _objc_msgSend$encodeDictionary:forKey:
+ _objc_msgSend$encodeForJob
+ _objc_msgSend$endowmentInfos
+ _objc_msgSend$error
+ _objc_msgSend$execute:assertion:error:
+ _objc_msgSend$executeLaunchRequest:
+ _objc_msgSend$identityForWrappedInfoProvider:
+ _objc_msgSend$identityForWrappedInfoProvider:uuid:
+ _objc_msgSend$infoWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$managedEndpointByLaunchIdentifier
+ _objc_msgSend$managedEndpointLaunchIdentifiers
+ _objc_msgSend$persistentJobLabel
+ _objc_msgSend$requiredExistingProcess
+ _objc_msgSend$setAssertion:
+ _objc_msgSend$setEndowmentInfos:
+ _objc_msgSend$setError:
+ _objc_msgSend$setManagedEndpointByLaunchIdentifier:
+ _objc_msgSend$setManagedEndpointLaunchIdentifiers:
+ _objc_msgSend$setRequiredExistingProcess:
+ _xpc_dictionary_create_empty
+ _xpc_endpoint_create_bs_from_port
+ _xpc_get_class4NSXPC
+ _xpc_mach_send_create_with_disposition
+ _xpc_mach_send_get_right
- +[RBSProcessIdentity identityForMacApplicationJobLabel:wrappedInfoProvider:platform:]
- +[RBSProcessIdentity identityForWrappedInfoProviderIdentity:]
- +[RBSWrappedLSInfo infoWithBundleID:personaString:]
- -[RBSConnection executeLaunchRequest:process:assertion:error:]
- -[RBSConnection executeLaunchRequest:process:assertion:error:].cold.1
- -[RBSConnection executeLaunchRequest:withCallback:]
- -[RBSConnection executeLaunchRequest:withCallback:].cold.1
- -[RBSEmbeddedAppProcessIdentity _initEmbeddedAppWithAppInfoProvider:]
- -[RBSEmbeddedAppProcessIdentity _initEmbeddedAppWithAppInfoProvider:].cold.1
- -[RBSLaunchRequest executeWithCallback:]
- -[RBSMacAppProcessIdentity _initMacAppWithLabel:infoProvider:auid:platform:]
- -[RBSProcessIdentity _initOpaqueWithPid:name:auid:]
- -[RBSProcessIdentity initWithDecodeFromJob:].cold.1
- -[RBSProcessIdentity initWithDecodeFromJob:].cold.2
- -[RBSProcessIdentity initWithDecodeFromJob:].cold.3
- -[RBSProcessIdentity matchesRecoveredIdentity:]
- -[RBSProcessIdentity matchesRecoveredIdentity:].cold.1
- -[RBSWrappedLSInfo _initWithBundleID:personaString:]
- -[RBSXPCServiceProcessIdentity hash]
- -[RBSXPCServiceProcessIdentity initWithDecodeFromJob:].cold.1
- -[RBSXPCServiceProcessIdentity matchesRecoveredIdentity:]
- GCC_except_table38
- GCC_except_table44
- __BSXPCDecodeObject
- __BSXPCDecodeObject.cold.1
- __BSXPCDecodeObject.cold.2
- __BSXPCDecodeObject.cold.3
- __BSXPCDecodeObject.cold.4
- __BSXPCDecodeObject.cold.5
- __BSXPCPopDecodingContext
- __BSXPCPushDecodingContext
- ___51-[RBSConnection executeLaunchRequest:withCallback:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8u48l8
- ___block_literal_global.127
- _dispatch_get_global_queue
- _executeLaunchRequest:process:assertion:error:.permanentError
- _objc_msgSend$_initWithBundleID:personaString:
- _objc_msgSend$doubleValue
- _objc_msgSend$executeLaunchRequest:process:assertion:error:
- _objc_msgSend$identityForMacApplicationJobLabel:wrappedInfoProvider:platform:
- _objc_msgSend$identityForWrappedInfoProviderIdentity:
- _objc_msgSend$infoWithBundleID:personaString:
- _objc_msgSend$matchesRecoveredIdentity:
- _xpc_dictionary_get_double
CStrings:
+ "\x01\x11\x16"
+ "\x01?\x05\x19"
+ "\x04+"
+ " endowmentInfo:[\n\t"
+ " endowmentNamespace:[\n\t"
+ "-[RBSMacAppProcessIdentity _initMacAppWithInfo:auid:uuid:]"
+ "-[RBSProcessIdentity copyWithAuid:]"
+ "-[RBSProcessIdentity encodeWithRBSXPCCoder:]"
+ "-[RBSProcessIdentity initWithDecodeFromJob:]"
+ "-[RBSProcessIdentity initWithRBSXPCCoder:]"
+ "1@`"
+ ":{%lu}"
+ "<%@| name:%@ nonLaunching:%@ port:%@>"
+ "<%@| namespace:%@ env:%@ %@ %lu>"
+ "<%@| task:%@ debug:%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
+ "@\"NSDictionary\"32@0:8#16@\"NSString\"24"
+ "@\"NSError\""
+ "@\"RBSLaunchResponse\"24@0:8@\"RBSLaunchRequest\"16"
+ "@32@0:8i16@20I28"
+ "@32@0:8i16I20@24"
+ "@36@0:8@16B24@28"
+ "@36@0:8@16I24@28"
+ "@60@0:8@16@24@32i40Q44Q52"
+ "Array element %zu failed to decode: %@"
+ "Attempted to decode a collection (%@) without specifying the class it contains"
+ "Attempted to decode a collection (%{public}@) without specifying the class it contains"
+ "Dictionary keys must be of type NSString"
+ "Error during decoding of %@: %@"
+ "Exception thrown while decoding class %{public}@ for key \"%{public}@\": %{public}@"
+ "Exception thrown while encoding object of class %{public}@ (key: \"%{public}@\"): %{public}@"
+ "Exception thrown while encoding object of class %{public}@: %{public}@"
+ "H"
+ "Invalid"
+ "Invalid decoding context for dictionary"
+ "NO"
+ "NSObject *_BSXPCDecodeObjectFromContext(RBSXPCCoder *__strong, __strong xpc_object_t, NSString *__strong, __unsafe_unretained Class, __unsafe_unretained Class)"
+ "No data was decoded from which to create an NSKeyedUnarchiver"
+ "No valid encoding type could be determined for expected class: %@"
+ "No valid encoding type could be determined for expected class: %{public}@"
+ "Object is not an NSDictionary"
+ "RBSLaunchRequest.m"
+ "RBSLaunchResponse"
+ "RBSMachEndpoint"
+ "RBSMachEndpoint.m"
+ "RBSOpaqueProcessIdentity"
+ "RBSProcessEndowmentInfo"
+ "RBSXPCEncodingNSSecure expects a dictionary decodingContext"
+ "T@\"NSDictionary\",&,N,V_managedEndpointByLaunchIdentifier"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSObject<OS_xpc_object>\",R,N"
+ "T@\"NSSet\",C,N,V_endowmentInfos"
+ "T@\"NSSet\",C,N,V_managedEndpointLaunchIdentifiers"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_name"
+ "T@\"NSString\",R,C,N,V_persistentJobLabel"
+ "T@\"RBSAssertion\",&,N,V_assertion"
+ "T@\"RBSProcessIdentifier\",C,N,V_requiredExistingProcess"
+ "TB,R,N,GisNonLaunching,V_nonLaunching"
+ "TQ,R,N,V_bundleInode"
+ "TQ,R,N,V_execInode"
+ "Unable to decode array: an object within the array failed to decode"
+ "Unable to decode dictionary key %@"
+ "Unable to decode dictionary key %{public}@"
+ "YES"
+ "_bundleInode"
+ "_copy"
+ "_endowmentInfos"
+ "_error"
+ "_execInode"
+ "_getterCache_endpoint"
+ "_initEmbeddedApp:personaString:"
+ "_initEmbeddedAppWithAppInfo:"
+ "_initEmbeddedAppWithBundleID:"
+ "_initMacAppWithInfo:auid:uuid:"
+ "_initOpaqueWithPid:auid:description:"
+ "_initOpaqueWithPid:name:auid:"
+ "_initWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:"
+ "_initWithName:nonLaunching:port:"
+ "_initWithNamespace:environment:encodedEndowment:"
+ "_initWithXPCServiceID:pid:auid:"
+ "_isCachedPortValid"
+ "_isEquivalentToEndpoint:"
+ "_lock_hasCheckedEndpoint"
+ "_managedEndpointByLaunchIdentifier"
+ "_managedEndpointLaunchIdentifiers"
+ "_nonLaunching"
+ "_persistentJobLabel"
+ "_requiredExistingProcess"
+ "assertion failure: can only encode well defined types : type=%i"
+ "bundleInode"
+ "cannot call -init on RBSMachEndpoint"
+ "decodeDictionaryOfClass:forKey:"
+ "decodeFromJob:"
+ "decodeTopLevelObjectOfClasses:forKey:error:"
+ "encodeDictionary:forKey:"
+ "endowmentInfoForHandle"
+ "endowmentInfos"
+ "endowmentNamespace can not be nil"
+ "error encoding host identity for job: %@ of %@"
+ "execInode"
+ "executeLaunchRequest:"
+ "executeLaunchRequest:error:"
+ "executeRequest"
+ "identityForLSApplicationIdentity:LSApplicationRecord:uuid:"
+ "identityForUnbundledMacApplicationJobLabel:"
+ "identityForWrappedInfoProvider:"
+ "identityForWrappedInfoProvider:uuid:"
+ "infoWithBundleID:personaString:persistentJobLabel:platform:bundleInode:execInode:"
+ "initWithDictionary:"
+ "intersectsSet:"
+ "isMultiInstanceExtension"
+ "isNonLaunching"
+ "l"
+ "managed-endpoint-by-launch-identifier"
+ "managedEndpointByLaunchIdentifier"
+ "managedEndpointByLaunchIdentifier mismatch : previous=%{public}@ new=%{public}@"
+ "managedEndpointLaunchIdentifiers"
+ "name != nil"
+ "nonLaunching"
+ "payload:"
+ "persistentJobLabel"
+ "port != nil"
+ "requiredExistingProcess"
+ "setAssertion:"
+ "setEndowmentInfos:"
+ "setError:"
+ "setManagedEndpointByLaunchIdentifier:"
+ "setManagedEndpointLaunchIdentifiers:"
+ "setRequiredExistingProcess:"
+ "unexpected port type %@"
+ "v24@?0@\"RBSProcessEndowmentInfo\"8^B16"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "void _BSXPCEncodeCollectionWithKey(RBSXPCCoder *__strong, NSString *__strong, __strong id<NSFastEnumeration>)"
+ "we should not have been able to vet the class without defining the encoding"
- "\x01\x11\x15"
- "\x01?\x03\x19"
- "\x04*"
- " endowments:[\n\t"
- "-[RBSMacAppProcessIdentity _initMacAppWithLabel:infoProvider:auid:platform:]"
- "<%@| task:%@ debug:%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
- "B48@0:8@\"RBSLaunchRequest\"16o^@24o^@32o^@40"
- "B48@0:8@16o^@24o^@32o^@40"
- "Backing off for %llu seconds %lf - %lf"
- "Backoff triggered without backoff time %{public}@ : %{public}@"
- "_initMacAppWithLabel:infoProvider:auid:platform:"
- "_initWithBundleID:personaString:"
- "anon<%@>(%d)"
- "assertion failure: can only encode extensions"
- "doubleValue"
- "executeLaunchRequest:identifier:error:"
- "executeLaunchRequest:process:assertion:error:"
- "executeWithCallback:"
- "identityForMacApplicationJobLabel:wrappedInfoProvider:platform:"
- "identityForWrappedInfoProviderIdentity:"
- "infoWithBundleID:personaString:"
- "initWithDecodeFromJob failed with unrecognized type %d"
- "initWithDecodeFromJob tried to decode mac app without label"
- "matchesRecoveredIdentity should be overridden."
- "matchesRecoveredIdentity:"
- "re-attempting backed off launch request"
- "recovered XPC service identity %@ has determined to be equivalent to client's saved XPC service identity %@"
- "void _BSXPCEncodeArrayWithKey(RBSXPCCoder *__strong, NSString *__strong, __strong id<NSFastEnumeration>)"

```
