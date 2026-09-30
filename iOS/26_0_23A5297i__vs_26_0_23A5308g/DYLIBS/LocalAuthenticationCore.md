## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.0.49.0.0
-  __TEXT.__text: 0xf8c10
+2005.0.60.0.0
+  __TEXT.__text: 0xf9054
   __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_methlist: 0x9a90
+  __TEXT.__objc_methlist: 0x9ad8
   __TEXT.__const: 0x4b14
-  __TEXT.__gcc_except_tab: 0x1a8c
-  __TEXT.__oslogstring: 0x6841
-  __TEXT.__cstring: 0xe017
+  __TEXT.__gcc_except_tab: 0x1aa0
+  __TEXT.__oslogstring: 0x6881
+  __TEXT.__cstring: 0xe2b7
   __TEXT.__dlopen_cstrs: 0x4bb
   __TEXT.__swift5_typeref: 0x1938
   __TEXT.__constg_swiftt: 0xf7c

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__unwind_info: 0x43d8
   __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0x2260
-  __TEXT.__objc_methname: 0xfba6
-  __TEXT.__objc_methtype: 0x48d2
-  __TEXT.__objc_stubs: 0xa740
-  __DATA_CONST.__got: 0xb08
+  __TEXT.__objc_classname: 0x2272
+  __TEXT.__objc_methname: 0xfb73
+  __TEXT.__objc_methtype: 0x4879
+  __TEXT.__objc_stubs: 0xa760
+  __DATA_CONST.__got: 0xb10
   __DATA_CONST.__const: 0x49e0
-  __DATA_CONST.__objc_classlist: 0x830
+  __DATA_CONST.__objc_classlist: 0x838
   __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b80
+  __DATA_CONST.__objc_selrefs: 0x3b88
   __DATA_CONST.__objc_protorefs: 0x270
-  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__const: 0x3a38
-  __AUTH_CONST.__cfstring: 0x65a0
-  __AUTH_CONST.__objc_const: 0x39c08
+  __AUTH_CONST.__const: 0x3aa8
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0x39cc8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x3218
-  __AUTH.__data: 0xbf0
-  __DATA.__objc_ivar: 0x834
-  __DATA.__data: 0x4fc0
-  __DATA.__bss: 0x2cb1
+  __AUTH.__objc_data: 0x3c30
+  __AUTH.__data: 0xe78
+  __DATA.__objc_ivar: 0x838
+  __DATA.__data: 0x4ff0
+  __DATA.__bss: 0x2c79
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_data: 0x2828
-  __DATA_DIRTY.__data: 0x4e0
-  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__objc_data: 0x1e60
+  __DATA_DIRTY.__data: 0x280
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 376737F8-8F08-338E-81E4-1FB7AD61B6A6
-  Functions: 6374
-  Symbols:   22142
-  CStrings:  6859
+  UUID: 89D731A8-F1CB-3378-A5EB-3DD4BCF23A80
+  Functions: 6381
+  Symbols:   22177
+  CStrings:  6882
 
Symbols:
+ +[LACACMParameter acmParameterDoNotStartDTOTimers]
+ +[LACACMParameter acmParameterSecureIntentSupport]
+ +[LACACMParameter acmParameterWithMaxContinuityAge:]
+ +[LACACMParameter acmParameterWithTimeOffset:]
+ +[LACACMParameter acmParameterWithUserId:]
+ -[LACACMHelper performContextVerificationWithParameters:block:completion:]
+ -[LACACMHelper preflightPolicy:parameters:maxGlobalCredentialAge:processRequirement:]
+ -[LACACMHelper verifyAclConstraint:operation:preflight:parameters:maxGlobalCredentialAge:processRequirement:]
+ -[LACACMHelper verifyPolicy:preflight:parameters:maxGlobalCredentialAge:processRequirement:]
+ -[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:]
+ -[LACACMParameter .cxx_destruct]
+ -[LACACMParameter copyWithZone:]
+ -[LACACMParameter data]
+ -[LACACMParameter description]
+ -[LACACMParameter initWithACMParamType:bytes:length:description:]
+ -[LACACMParameter type]
+ -[LACACMParameterCollection .cxx_destruct]
+ -[LACACMParameterCollection addParameter:]
+ -[LACACMParameterCollection copyWithZone:]
+ -[LACACMParameterCollection description]
+ -[LACACMParameterCollection initWithParameter:]
+ -[LACACMParameterCollection init]
+ -[LACACMParameterCollection makeACMParameters]
+ -[LACACMParameterCollection makeACMParameters].cold.1
+ -[LACACMParameterCollection makeACMParameters].cold.2
+ -[LACACMParameterCollection parameterCount]
+ -[LACACMParameterCollection parameterWithType:]
+ _$s23LocalAuthenticationCore6LACLogOWV
+ _$s23LocalAuthenticationCore6LACLogOwet
+ _$s23LocalAuthenticationCore6LACLogOwst
+ _$s23LocalAuthenticationCore6LACLogOwug
+ _$s23LocalAuthenticationCore6LACLogOwui
+ _$s23LocalAuthenticationCore6LACLogOwup
+ _OBJC_CLASS_$_LACACMParameter
+ _OBJC_CLASS_$_LACACMParameterCollection
+ _OBJC_IVAR_$_LACACMParameter._data
+ _OBJC_IVAR_$_LACACMParameter._description
+ _OBJC_IVAR_$_LACACMParameter._type
+ _OBJC_IVAR_$_LACACMParameterCollection._parameters
+ _OBJC_METACLASS_$_LACACMParameter
+ _OBJC_METACLASS_$_LACACMParameterCollection
+ __OBJC_$_CLASS_METHODS_LACACMParameter
+ __OBJC_$_INSTANCE_METHODS_LACACMParameter
+ __OBJC_$_INSTANCE_METHODS_LACACMParameterCollection
+ __OBJC_$_INSTANCE_VARIABLES_LACACMParameter
+ __OBJC_$_INSTANCE_VARIABLES_LACACMParameterCollection
+ __OBJC_$_PROP_LIST_LACACMParameter
+ __OBJC_$_PROP_LIST_LACACMParameterCollection
+ __OBJC_CLASS_PROTOCOLS_$_LACACMParameterCollection
+ __OBJC_CLASS_RO_$_LACACMParameter
+ __OBJC_CLASS_RO_$_LACACMParameterCollection
+ __OBJC_METACLASS_RO_$_LACACMParameter
+ __OBJC_METACLASS_RO_$_LACACMParameterCollection
+ ___109-[LACACMHelper verifyAclConstraint:operation:preflight:parameters:maxGlobalCredentialAge:processRequirement:]_block_invoke
+ ___109-[LACACMHelper verifyAclConstraint:operation:preflight:parameters:maxGlobalCredentialAge:processRequirement:]_block_invoke_2
+ ___74-[LACACMHelper performContextVerificationWithParameters:block:completion:]_block_invoke
+ ___84-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:]_block_invoke
+ ___84-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:]_block_invoke_2
+ ___84-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:]_block_invoke_2.cold.1
+ ___92-[LACACMHelper verifyPolicy:preflight:parameters:maxGlobalCredentialAge:processRequirement:]_block_invoke
+ ___block_descriptor_45_e67_v36?0^{__ACMHandle=}8^{?=I^vI}16I24?<v?iB^{__ACMRequirement=}>28l
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0i8B12r^{__ACMRequirement=}16ls40l8s32l8
+ ___block_descriptor_69_e67_v36?0^{__ACMHandle=}8^{?=I^vI}16I24?<v?iB^{__ACMRequirement=}>28l
+ ___block_descriptor_76_e8_32s40s48r56r_e34_v24?0i8B12r^{__ACMRequirement=}16lr48l8s32l8r56l8s40l8
+ _audit_stringCryptoTokenKit
+ _objc_msgSend$addParameter:
+ _objc_msgSend$makeACMParameters
+ _objc_msgSend$parameterCount
+ _objc_msgSend$performContextVerificationWithParameters:block:completion:
+ _objc_msgSend$verifyPolicy:preflight:parameters:maxGlobalCredentialAge:processRequirement:
+ _objc_msgSend$verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:
- +[LACManagedACMParameters acmParameterDoNotStartDTOTimers]
- +[LACManagedACMParameters acmParameterSecureIntentSupport]
- +[LACManagedACMParameters acmParameterWithMaxContinuityAge:]
- +[LACManagedACMParameters acmParameterWithTimeOffset:]
- +[LACManagedACMParameters acmParameterWithUserId:]
- -[LACACMHelper performContextVerificationBlock:completion:]
- -[LACACMHelper preflightPolicy:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]
- -[LACACMHelper verifyAclConstraint:operation:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]
- -[LACACMHelper verifyPolicy:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]
- -[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:]
- -[LACManagedACMParameters .cxx_destruct]
- -[LACManagedACMParameters _appendACMParameter:]
- -[LACManagedACMParameters acmParameterByAppendingACMParameters:]
- -[LACManagedACMParameters acmParameters]
- -[LACManagedACMParameters copyWithZone:]
- -[LACManagedACMParameters count]
- -[LACManagedACMParameters data]
- -[LACManagedACMParameters description]
- -[LACManagedACMParameters findACMParameterWithType:]
- -[LACManagedACMParameters initWithACMParamType:bytes:length:description:]
- _OBJC_CLASS_$_LACManagedACMParameters
- _OBJC_IVAR_$_LACManagedACMParameters._count
- _OBJC_IVAR_$_LACManagedACMParameters._data
- _OBJC_IVAR_$_LACManagedACMParameters._description
- _OBJC_METACLASS_$_LACManagedACMParameters
- __OBJC_$_CLASS_METHODS_LACManagedACMParameters
- __OBJC_$_INSTANCE_METHODS_LACManagedACMParameters
- __OBJC_$_INSTANCE_VARIABLES_LACManagedACMParameters
- __OBJC_$_PROP_LIST_LACManagedACMParameters
- __OBJC_CLASS_PROTOCOLS_$_LACManagedACMParameters
- __OBJC_CLASS_RO_$_LACManagedACMParameters
- __OBJC_METACLASS_RO_$_LACManagedACMParameters
- ___108-[LACACMHelper verifyPolicy:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]_block_invoke
- ___125-[LACACMHelper verifyAclConstraint:operation:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]_block_invoke
- ___125-[LACACMHelper verifyAclConstraint:operation:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:]_block_invoke_2
- ___59-[LACACMHelper performContextVerificationBlock:completion:]_block_invoke
- ___83-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:]_block_invoke
- ___83-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:]_block_invoke_2
- ___83-[LACACMHelper verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:]_block_invoke_2.cold.1
- ___block_descriptor_40_e8_32bs_e34_v24?0i8B12r^{__ACMRequirement=}16ls32l8
- ___block_descriptor_57_e53_v24?0^{__ACMHandle=}8?<v?iB^{__ACMRequirement=}>16l
- ___block_descriptor_68_e8_32s40r48r_e34_v24?0i8B12r^{__ACMRequirement=}16lr40l8s32l8r48l8
- ___block_descriptor_81_e53_v24?0^{__ACMHandle=}8?<v?iB^{__ACMRequirement=}>16l
- _objc_msgSend$_appendACMParameter:
- _objc_msgSend$acmParameters
- _objc_msgSend$performContextVerificationBlock:completion:
- _objc_msgSend$verifyPolicy:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:
- _objc_msgSend$verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:
CStrings:
+ "?"
+ "@\"<LACADMUserProviding>\""
+ "@\"<LACClientInfoProviding>\""
+ "@\"<LACCompanionAuthenticationCoordinating>\""
+ "@\"<LACCompanionAuthenticationEnvironmentProviding>\""
+ "@\"<LACCompanionAuthenticationProviding>\""
+ "@\"<LACEligibilityHelping>\""
+ "@\"LACAuditToken\""
+ "@\"LACSecureData\""
+ "@\"OS_dispatch_queue\""
+ "ACMParameter length overflow"
+ "ACMParameter: %@ data length exceeds UINT32_MAX"
+ "LACACMParameter"
+ "LACACMParameterCollection"
+ "T@\"NSData\",R,N,V_data"
+ "TI,R,N,V_type"
+ "TQ,R,N"
+ "_parameters"
+ "_type"
+ "addParameter:"
+ "initWithParameter:"
+ "makeACMParameters"
+ "parameterCount"
+ "parameterWithType:"
+ "performContextVerificationWithParameters:block:completion:"
+ "preflightPolicy:parameters:maxGlobalCredentialAge:processRequirement:"
+ "v36@?0^{__ACMHandle=}8^{?=I^vI}16I24@?<v@?iB^{__ACMRequirement=}>28"
+ "v44@0:8*16@24I32@?36"
+ "v48@0:8*16B24@28I36@?40"
+ "v56@0:8@16@24B32@36I44@?48"
+ "verifyAclConstraint:operation:preflight:parameters:maxGlobalCredentialAge:processRequirement:"
+ "verifyPolicy:preflight:parameters:maxGlobalCredentialAge:processRequirement:"
+ "verifyRequirementOfType:policy:mustBePresent:parameters:flags:error:"
- ", %@"
- "@\"NSMutableData\""
- "LACManagedACMParameters"
- "T@\"NSMutableData\",R,N,V_data"
- "TI,R,N,V_count"
- "T^{?=I^vI},R,N"
- "^{?=I^vI}16@0:8"
- "_appendACMParameter:"
- "_count"
- "acmParameterByAppendingACMParameters:"
- "acmParameters"
- "findACMParameterWithType:"
- "performContextVerificationBlock:completion:"
- "preflightPolicy:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:"
- "r^{?=I^vI}20@0:8I16"
- "v24@?0^{__ACMHandle=}8@?<v@?iB^{__ACMRequirement=}>16"
- "v48@0:8*16r^{?=I^vI}24I32I36@?40"
- "v52@0:8*16B24r^{?=I^vI}28I36I40@?44"
- "v60@0:8@16@24B32r^{?=I^vI}36I44I48@?52"
- "verifyAclConstraint:operation:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:"
- "verifyPolicy:preflight:parameters:parametersCount:maxGlobalCredentialAge:processRequirement:"
- "verifyRequirementOfType:policy:mustBePresent:parameter:flags:error:"

```
