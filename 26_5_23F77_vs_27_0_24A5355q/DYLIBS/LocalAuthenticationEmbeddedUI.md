## LocalAuthenticationEmbeddedUI

> `/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`

```diff

-2005.120.18.0.0
-  __TEXT.__text: 0x23fa4
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x38c8
+2305.0.0.0.1
+  __TEXT.__text: 0x212a8
+  __TEXT.__objc_methlist: 0x3788
   __TEXT.__const: 0x4f2
-  __TEXT.__cstring: 0x253f
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__oslogstring: 0x846
+  __TEXT.__cstring: 0x234f
+  __TEXT.__gcc_except_tab: 0x3b8
+  __TEXT.__oslogstring: 0x816
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__swift5_typeref: 0x236
+  __TEXT.__swift5_typeref: 0x22c
   __TEXT.__swift5_capture: 0x40
   __TEXT.__constg_swiftt: 0xb0
   __TEXT.__swift5_reflstr: 0x5e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xe60
-  __TEXT.__objc_classname: 0xbfb
-  __TEXT.__objc_methname: 0x737e
-  __TEXT.__objc_methtype: 0x1d66
-  __TEXT.__objc_stubs: 0x5e20
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0xfe0
-  __DATA_CONST.__objc_classlist: 0x248
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c80
+  __DATA_CONST.__objc_selrefs: 0x1c48
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH_CONST.__const: 0x330
-  __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0xa5d0
+  __DATA_CONST.__objc_superrefs: 0x128
+  __DATA_CONST.__got: 0x440
+  __AUTH_CONST.__const: 0x310
+  __AUTH_CONST.__cfstring: 0x1060
+  __AUTH_CONST.__objc_const: 0xa2d0
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH.__objc_data: 0x1738
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH.__objc_data: 0x1648
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0xa70
+  __DATA.__objc_ivar: 0x378
+  __DATA.__data: 0xa00
   __DATA.__bss: 0x540
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7934BBDB-EE6B-3612-9AD0-3AF5186F3688
-  Functions: 1237
-  Symbols:   4489
-  CStrings:  1909
+  UUID: E0EAA4F5-A9B4-3E6E-ABF9-FF41FEF330A9
+  Functions: 1194
+  Symbols:   4380
+  CStrings:  434
 
Symbols:
+ +[LAPSErrorBuilder errorWithError:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration .cxx_destruct]
+ -[LACUIPasscodeServiceOptionsViewConfiguration allowedPasscodeTypes]
+ -[LACUIPasscodeServiceOptionsViewConfiguration cancelTitle]
+ -[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryEnabled]
+ -[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryOptionVisible]
+ -[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoveryRestricted]
+ -[LACUIPasscodeServiceOptionsViewConfiguration isPasscodeRecoverySupported]
+ -[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryDisabledTitle]
+ -[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryEnabledTitle]
+ -[LACUIPasscodeServiceOptionsViewConfiguration passcodeRecoveryTitle]
+ -[LACUIPasscodeServiceOptionsViewConfiguration selectedPasscodeType]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setAllowedPasscodeTypes:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setCancelTitle:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryEnabled:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryOptionVisible:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoveryRestricted:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setIsPasscodeRecoverySupported:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryDisabledTitle:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryEnabledTitle:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setPasscodeRecoveryTitle:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setSelectedPasscodeType:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration setTitle:]
+ -[LACUIPasscodeServiceOptionsViewConfiguration title]
+ -[LAPSCurrentPasscodeService verifyPasscode:contextRef:completion:]
+ -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:]
+ -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:].cold.1
+ -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:].cold.2
+ -[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:]
+ -[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:].cold.1
+ -[LAPSPasscode extractablePassword]
+ -[LAPSPasscodeChangeController verifyPasscode:completion:]
+ -[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodeChangeSystemRecoveryAdapter verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodeChangeSystemRemovalAdapter verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodeChangeSystemStandardAdapter verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodeChangeSystemStubbedAdapter verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodeChangeSystemVerificationAdapter verifyPasscode:contextRef:completion:]
+ -[LAPSPasscodePersistenceAdapter verifyPasscode:contextRef:]
+ -[LAPSPasscodePersistenceMKBAdapter _verifyPasscode:contextRef:options:]
+ -[LAPSPasscodePersistenceMKBAdapter verifyPasscode:contextRef:]
+ -[LAPasscodeVerificationServiceOptions passcode]
+ -[LAPasscodeVerificationServiceOptions setPasscode:]
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table5
+ _LACErrorCodeUserCancel
+ _LACPasscodeVariableLength
+ _MKBVerifyACMPasswordWithContext
+ _NSLocalizedStringFromLACPasscodeType
+ _OBJC_CLASS_$_LACPasscode
+ _OBJC_CLASS_$_LACPasscodeCollection
+ _OBJC_CLASS_$_LACSExtractablePassword
+ _OBJC_CLASS_$_LACUIPasscodeServiceOptionsViewConfiguration
+ _OBJC_CLASS_$_LACUIPasscodeServiceViewConfiguration
+ _OBJC_CLASS_$_LACUIPasscodeServiceViewController
+ _OBJC_CLASS_$_NSData
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._allowedPasscodeTypes
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._cancelTitle
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._isPasscodeRecoveryEnabled
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._isPasscodeRecoveryOptionVisible
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._isPasscodeRecoveryRestricted
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._isPasscodeRecoverySupported
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._passcodeRecoveryDisabledTitle
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._passcodeRecoveryEnabledTitle
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._passcodeRecoveryTitle
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._selectedPasscodeType
+ _OBJC_IVAR_$_LACUIPasscodeServiceOptionsViewConfiguration._title
+ _OBJC_IVAR_$_LAPSPasscode._extractablePassword
+ _OBJC_IVAR_$_LAPasscodeVerificationServiceOptions._passcode
+ _OBJC_METACLASS_$_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_$_INSTANCE_METHODS_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_$_PROP_LIST_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_$_PROP_LIST_LACUIPasscodeServiceViewControlling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUIPasscodeServiceViewControlling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUIPasscodeServiceViewControlling
+ __OBJC_$_PROTOCOL_REFS_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_LACUIPasscodeServiceViewControlling
+ __OBJC_CLASS_RO_$_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_LABEL_PROTOCOL_$_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_LACUIPasscodeServiceViewControlling
+ __OBJC_METACLASS_RO_$_LACUIPasscodeServiceOptionsViewConfiguration
+ __OBJC_PROTOCOL_$_LACUIPasscodeServiceViewControllerDelegate
+ __OBJC_PROTOCOL_$_LACUIPasscodeServiceViewControlling
+ ___54-[LAPasscodeChangeService _startOperation:completion:]_block_invoke_2
+ ___58-[LAPSPasscodeChangeController verifyPasscode:completion:]_block_invoke
+ ___60-[LAPasscodeVerificationService _startOperation:completion:]_block_invoke_2
+ ___78-[LAPSPasscodeChangeUICoordinator fetchOldPasscodeCoordinator:verifyPasscode:]_block_invoke.62
+ ___79-[LAPSPasscodeChangeSystemStubbedAdapter verifyPasscode:contextRef:completion:]_block_invoke
+ ___82-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:contextRef:completion:]_block_invoke
+ ___82-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:contextRef:completion:]_block_invoke_2
+ ___82-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:contextRef:completion:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e51_"LACUIPasscodeServiceOptionsViewConfiguration"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e60_"UIViewController<LACUIPasscodeServiceViewControlling>"8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e31_v24?0"LAContext"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e60_"UIViewController<LACUIPasscodeServiceViewControlling>"8?0ls32l8s40l8
+ ___block_literal_global.50
+ ___block_literal_global.51
+ ___block_literal_global.52
+ ___block_literal_global.56
+ ___block_literal_global.76
+ ___block_literal_global.82
+ ___block_literal_global.85
+ ___swift__destructor
+ ___swift_closure_destructor
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_LocalAuthenticationEmbeddedUI
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_verifyPasscode:contextRef:options:
+ _objc_msgSend$changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:outError:
+ _objc_msgSend$changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:outError:
+ _objc_msgSend$data:
+ _objc_msgSend$errorWithError:
+ _objc_msgSend$extractablePassword
+ _objc_msgSend$featureFlagSwiftUIPasscodeServicesEnabled
+ _objc_msgSend$initWithData:error:
+ _objc_msgSend$passcodeContext:meetsCurrentConstraintsOutError:
+ _objc_msgSend$passcodeViewController:verifyPasscode:passcodeType:
+ _objc_msgSend$unsafeContextRef
+ _objc_msgSend$verifyPasscode:contextRef:
+ _objc_msgSend$verifyPasscode:contextRef:completion:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x22
- +[LAPSPasscodeType alphanumericType]
- +[LAPSPasscodeType noneType]
- +[LAPSPasscodeType numericCustomDigitsType]
- +[LAPSPasscodeType numericFourDigitsType]
- +[LAPSPasscodeType numericSixDigitsType]
- +[LAPSPasscodeType typeAllowingString:]
- +[LAPSPasscodeType typeAllowingString:].cold.1
- +[LAPSPasscodeTypeCollection _allWhere:]
- +[LAPSPasscodeTypeCollection allPasscodeTypesWhereComplexityIsGreaterThanOrEqualTo:]
- +[LAPSPasscodeTypeCollection allPasscodeTypes]
- -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:]
- -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:].cold.1
- -[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:].cold.2
- -[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:]
- -[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:].cold.1
- -[LAPSPasscode externalizePasscode]
- -[LAPSPasscode externalizePasscode].cold.1
- -[LAPSPasscodeOptionsViewControllerConfiguration .cxx_destruct]
- -[LAPSPasscodeOptionsViewControllerConfiguration allowedPasscodeTypes]
- -[LAPSPasscodeOptionsViewControllerConfiguration cancelTitle]
- -[LAPSPasscodeOptionsViewControllerConfiguration isPasscodeRecoveryEnabled]
- -[LAPSPasscodeOptionsViewControllerConfiguration isPasscodeRecoveryOptionVisible]
- -[LAPSPasscodeOptionsViewControllerConfiguration isPasscodeRecoveryRestricted]
- -[LAPSPasscodeOptionsViewControllerConfiguration isPasscodeRecoverySupported]
- -[LAPSPasscodeOptionsViewControllerConfiguration passcodeRecoveryDisabledTitle]
- -[LAPSPasscodeOptionsViewControllerConfiguration passcodeRecoveryEnabledTitle]
- -[LAPSPasscodeOptionsViewControllerConfiguration passcodeRecoveryTitle]
- -[LAPSPasscodeOptionsViewControllerConfiguration selectedPasscodeType]
- -[LAPSPasscodeOptionsViewControllerConfiguration setAllowedPasscodeTypes:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setCancelTitle:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setIsPasscodeRecoveryEnabled:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setIsPasscodeRecoveryOptionVisible:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setIsPasscodeRecoveryRestricted:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setIsPasscodeRecoverySupported:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setPasscodeRecoveryDisabledTitle:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setPasscodeRecoveryEnabledTitle:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setPasscodeRecoveryTitle:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setSelectedPasscodeType:]
- -[LAPSPasscodeOptionsViewControllerConfiguration setTitle:]
- -[LAPSPasscodeOptionsViewControllerConfiguration title]
- -[LAPSPasscodePersistenceMKBAdapter _verifyPasscode:options:]
- -[LAPSPasscodeType allowsLength:]
- -[LAPSPasscodeType allowsString:]
- -[LAPSPasscodeType complexityRating]
- -[LAPSPasscodeType copyWithZone:]
- -[LAPSPasscodeType description]
- -[LAPSPasscodeType hasFixedLength]
- -[LAPSPasscodeType hash]
- -[LAPSPasscodeType identifier]
- -[LAPSPasscodeType initWithIdentifier:length:]
- -[LAPSPasscodeType isEqual:]
- -[LAPSPasscodeType length]
- -[LAPSPasscodeType localizedName]
- -[LAPSPasscodeType setIdentifier:]
- -[LAPSPasscodeViewControllerConfiguration .cxx_destruct]
- -[LAPSPasscodeViewControllerConfiguration errorMessage]
- -[LAPSPasscodeViewControllerConfiguration footer]
- -[LAPSPasscodeViewControllerConfiguration nextButton]
- -[LAPSPasscodeViewControllerConfiguration optionsConfiguration]
- -[LAPSPasscodeViewControllerConfiguration passcodeType]
- -[LAPSPasscodeViewControllerConfiguration prompt]
- -[LAPSPasscodeViewControllerConfiguration setErrorMessage:]
- -[LAPSPasscodeViewControllerConfiguration setFooter:]
- -[LAPSPasscodeViewControllerConfiguration setNextButton:]
- -[LAPSPasscodeViewControllerConfiguration setOptionsConfiguration:]
- -[LAPSPasscodeViewControllerConfiguration setPasscodeType:]
- -[LAPSPasscodeViewControllerConfiguration setPrompt:]
- -[LAPSPasscodeViewControllerConfiguration setShouldAvoidBecomingFirstResponderOnStart:]
- -[LAPSPasscodeViewControllerConfiguration setSubPrompt:]
- -[LAPSPasscodeViewControllerConfiguration setTitle:]
- -[LAPSPasscodeViewControllerConfiguration shouldAvoidBecomingFirstResponderOnStart]
- -[LAPSPasscodeViewControllerConfiguration subPrompt]
- -[LAPSPasscodeViewControllerConfiguration title]
- GCC_except_table14
- GCC_except_table21
- GCC_except_table28
- _LACErrorCodeDenied
- _LAPSPasscodeTypeVariableLength
- _MKBVerifyPasswordWithContext
- _NSStringFromLAPSPasscodeTypeIdentifier
- _OBJC_CLASS_$_LAPSPasscodeOptionsViewControllerConfiguration
- _OBJC_CLASS_$_LAPSPasscodeType
- _OBJC_CLASS_$_LAPSPasscodeTypeCollection
- _OBJC_CLASS_$_LAPSPasscodeViewControllerConfiguration
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_IVAR_$_LAPSPasscode._passcode
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._allowedPasscodeTypes
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._cancelTitle
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._isPasscodeRecoveryEnabled
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._isPasscodeRecoveryOptionVisible
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._isPasscodeRecoveryRestricted
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._isPasscodeRecoverySupported
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._passcodeRecoveryDisabledTitle
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._passcodeRecoveryEnabledTitle
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._passcodeRecoveryTitle
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._selectedPasscodeType
- _OBJC_IVAR_$_LAPSPasscodeOptionsViewControllerConfiguration._title
- _OBJC_IVAR_$_LAPSPasscodeType._identifier
- _OBJC_IVAR_$_LAPSPasscodeType._length
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._errorMessage
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._footer
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._nextButton
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._optionsConfiguration
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._passcodeType
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._prompt
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._shouldAvoidBecomingFirstResponderOnStart
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._subPrompt
- _OBJC_IVAR_$_LAPSPasscodeViewControllerConfiguration._title
- _OBJC_METACLASS_$_LAPSPasscodeOptionsViewControllerConfiguration
- _OBJC_METACLASS_$_LAPSPasscodeType
- _OBJC_METACLASS_$_LAPSPasscodeTypeCollection
- _OBJC_METACLASS_$_LAPSPasscodeViewControllerConfiguration
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __OBJC_$_CLASS_METHODS_LAPSPasscodeType
- __OBJC_$_CLASS_METHODS_LAPSPasscodeTypeCollection
- __OBJC_$_INSTANCE_METHODS_LAPSPasscodeOptionsViewControllerConfiguration
- __OBJC_$_INSTANCE_METHODS_LAPSPasscodeType
- __OBJC_$_INSTANCE_METHODS_LAPSPasscodeViewControllerConfiguration
- __OBJC_$_INSTANCE_VARIABLES_LAPSPasscodeOptionsViewControllerConfiguration
- __OBJC_$_INSTANCE_VARIABLES_LAPSPasscodeType
- __OBJC_$_INSTANCE_VARIABLES_LAPSPasscodeViewControllerConfiguration
- __OBJC_$_PROP_LIST_LAPSPasscodeOptionsViewControllerConfiguration
- __OBJC_$_PROP_LIST_LAPSPasscodeType
- __OBJC_$_PROP_LIST_LAPSPasscodeViewControllerConfiguration
- __OBJC_$_PROP_LIST_LAPSPasscodeViewControlling
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAPSPasscodeViewControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAPSPasscodeViewControlling
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAPSPasscodeViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAPSPasscodeViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAPSPasscodeViewControlling
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_$_PROTOCOL_REFS_LAPSPasscodeViewControllerDelegate
- __OBJC_$_PROTOCOL_REFS_LAPSPasscodeViewControlling
- __OBJC_CLASS_PROTOCOLS_$_LAPSPasscodeType
- __OBJC_CLASS_RO_$_LAPSPasscodeOptionsViewControllerConfiguration
- __OBJC_CLASS_RO_$_LAPSPasscodeType
- __OBJC_CLASS_RO_$_LAPSPasscodeTypeCollection
- __OBJC_CLASS_RO_$_LAPSPasscodeViewControllerConfiguration
- __OBJC_LABEL_PROTOCOL_$_LAPSPasscodeViewControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_LAPSPasscodeViewControlling
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_METACLASS_RO_$_LAPSPasscodeOptionsViewControllerConfiguration
- __OBJC_METACLASS_RO_$_LAPSPasscodeType
- __OBJC_METACLASS_RO_$_LAPSPasscodeTypeCollection
- __OBJC_METACLASS_RO_$_LAPSPasscodeViewControllerConfiguration
- __OBJC_PROTOCOL_$_LAPSPasscodeViewControllerDelegate
- __OBJC_PROTOCOL_$_LAPSPasscodeViewControlling
- __OBJC_PROTOCOL_$_NSCopying
- ___33-[LAPSPasscodeType allowsString:]_block_invoke
- ___33-[LAPSPasscodeType allowsString:]_block_invoke.cold.1
- ___33-[LAPSPasscodeType allowsString:]_block_invoke_2
- ___40+[LAPSPasscodeTypeCollection _allWhere:]_block_invoke
- ___46+[LAPSPasscodeTypeCollection allPasscodeTypes]_block_invoke
- ___53-[LAPSFetchOldPasscodeCoordinator _presentPasscodeVC]_block_invoke_2
- ___68-[LAPSPasscodeChangeSystemStubbedAdapter verifyPasscode:completion:]_block_invoke
- ___71-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:completion:]_block_invoke
- ___71-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:completion:]_block_invoke_2
- ___71-[LAPSPasscodeChangeSystemDispatchDecorator verifyPasscode:completion:]_block_invoke_3
- ___78-[LAPSPasscodeChangeUICoordinator fetchOldPasscodeCoordinator:verifyPasscode:]_block_invoke.20
- ___79-[LAPSFetchNewPasscodeCoordinator _presentVerifyPasscodeVCWithTransitionStyle:]_block_invoke_2
- ___84+[LAPSPasscodeTypeCollection allPasscodeTypesWhereComplexityIsGreaterThanOrEqualTo:]_block_invoke
- ___89-[LAPSFetchNewPasscodeCoordinator _presentNewPasscodeVCWithTransitionStyle:errorMessage:]_block_invoke_3
- ___block_descriptor_32_e47_q24?0"LAPSPasscodeType"8"LAPSPasscodeType"16l
- ___block_descriptor_40_e26_B16?0"LAPSPasscodeType"8l
- ___block_descriptor_40_e8_32bs_e33_B32?0"LAPSPasscodeType"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e26_"NSRegularExpression"8?0ls32l8
- ___block_descriptor_40_e8_32s_e46_"LAPSPasscodeViewControllerConfiguration"8?0ls32l8
- ___block_descriptor_40_e8_32s_e52_"UIViewController<LAPSPasscodeViewControlling>"8?0ls32l8
- ___block_descriptor_40_e8_32s_e53_"LAPSPasscodeOptionsViewControllerConfiguration"8?0ls32l8
- ___block_descriptor_48_e8_32s40s_e46_"LAPSPasscodeViewControllerConfiguration"8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e52_"UIViewController<LAPSPasscodeViewControlling>"8?0ls32l8s40l8
- ___block_literal_global.10
- ___block_literal_global.12
- ___block_literal_global.16
- ___block_literal_global.34
- ___block_literal_global.40
- ___block_literal_global.43
- ___block_literal_global.9
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_LocalAuthenticationEmbeddedUI
- _objc_msgSend$_allWhere:
- _objc_msgSend$_verifyPasscode:options:
- _objc_msgSend$allPasscodeTypes
- _objc_msgSend$changePasscodeFrom:to:skipRecovery:outError:
- _objc_msgSend$changePasscodeWithRecoveryPasscode:to:skipRecovery:outError:
- _objc_msgSend$compare:
- _objc_msgSend$externalizePasscode
- _objc_msgSend$identifier
- _objc_msgSend$indexesOfObjectsPassingTest:
- _objc_msgSend$initWithIdentifier:length:
- _objc_msgSend$localizedName
- _objc_msgSend$objectsAtIndexes:
- _objc_msgSend$passcode:meetsCurrentConstraintsOutError:
- _objc_msgSend$passcodeTypeAlphanumeric
- _objc_msgSend$passcodeTypeNone
- _objc_msgSend$passcodeTypeNumericCustomDigits
- _objc_msgSend$passcodeTypeNumericFourDigits
- _objc_msgSend$passcodeTypeNumericSixDigits
- _objc_msgSend$passcodeViewController:verifyPasscode:
- _objc_msgSend$rangeOfFirstMatchInString:options:range:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$setCredential:type:
- _objc_msgSend$setCredential:type:error:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$verifyPasscode:
- _swift_retain
- _symbolic ______ypt So38UIApplicationOpenExternalURLOptionsKeya
CStrings:
+ "-[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:]"
+ "-[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:]"
+ "@\"LACUIPasscodeServiceOptionsViewConfiguration\"8@?0"
+ "@\"UIViewController<LACUIPasscodeServiceViewControlling>\"8@?0"
+ "Failed to create extractable password: %@"
+ "Failed to extract passcode data: %@"
+ "[[_input passcodeType] isEqual:passcodeType]"
+ "[simplestAllowedPasscodeType type] != LACPasscodeTypeNone"
+ "_passcodeType == passcodeType"
- "#16@0:8"
- "+[LAPSPasscodeType typeAllowingString:]"
- "-[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:]"
- "-[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:]"
- "-[LAPSPasscodeType allowsString:]_block_invoke"
- ".cxx_destruct"
- "@\"<LAAuthorizationViewControllerDelegate>\""
- "@\"<LACContext>\"16@0:8"
- "@\"<LACPSAuthorizer>\""
- "@\"<LACUIRatchetViewModelType>\""
- "@\"<LAPSFetchNewPasscodeCoordinatorDelegate>\""
- "@\"<LAPSFetchOldPasscodeCoordinatorDelegate>\""
- "@\"<LAPSPasscodeChangeController>\""
- "@\"<LAPSPasscodeChangeController>\"24@0:8@\"LAPSPasscodeChangeControllerProviderOptions\"16"
- "@\"<LAPSPasscodeChangeControllerProviding>\""
- "@\"<LAPSPasscodeChangePreflightController>\"16@0:8"
- "@\"<LAPSPasscodeChangeSystem>\""
- "@\"<LAPSPasscodeChangeUI>\""
- "@\"<LAPSPasscodeChangeUIDelegate>\""
- "@\"<LAPSPasscodeChangeUIDelegate>\"16@0:8"
- "@\"<LAPSPasscodeOptionsViewControllerDelegate>\""
- "@\"<LAPSPasscodeOptionsViewControllerDelegate>\"16@0:8"
- "@\"<LAPSPasscodePersistence>\""
- "@\"<LAPSPasscodeViewControllerDelegate>\""
- "@\"<LAPSPasscodeViewControllerDelegate>\"16@0:8"
- "@\"<LARatchetViewControllerDelegate>\""
- "@\"LAAuthorizationViewController\""
- "@\"LACSExtractablePassword\""
- "@\"LACUIAuthenticatorServiceConfiguration\""
- "@\"LACUIContainerViewController\""
- "@\"LACUIKeyboardLayoutGuide\""
- "@\"LACUIPasscodeField\""
- "@\"LAExtractablePassword\""
- "@\"LAPSCurrentPasscodeService\""
- "@\"LAPSCurrentPasscodeServiceOptions\""
- "@\"LAPSFetchNewPasscodeCoordinatorInput\""
- "@\"LAPSFetchNewPasscodeRequest\"16@0:8"
- "@\"LAPSFetchOldPasscodeCoordinatorInput\""
- "@\"LAPSFetchOldPasscodeRequest\"16@0:8"
- "@\"LAPSNewPasscodeService\""
- "@\"LAPSPasscode\""
- "@\"LAPSPasscodeBackoffTimerController\""
- "@\"LAPSPasscodeChangeAuthorizationOptions\""
- "@\"LAPSPasscodeChangeControllerOptions\""
- "@\"LAPSPasscodeChangeSystemOptions\""
- "@\"LAPSPasscodeChangeUICoordinatorOptions\""
- "@\"LAPSPasscodeChangeUIPresentationController\""
- "@\"LAPSPasscodeOptionsViewControllerConfiguration\""
- "@\"LAPSPasscodeOptionsViewControllerConfiguration\"8@?0"
- "@\"LAPSPasscodePersistenceCDPAdapter\""
- "@\"LAPSPasscodePersistenceLAAdapter\""
- "@\"LAPSPasscodePersistenceMCAdapter\""
- "@\"LAPSPasscodePersistenceMKBAdapter\""
- "@\"LAPSPasscodePersistenceSecAdapter\""
- "@\"LAPSPasscodeType\""
- "@\"LAPSPasscodeType\"16@0:8"
- "@\"LAPSPasscodeViewControllerConfiguration\""
- "@\"LAPSPasscodeViewControllerConfiguration\"8@?0"
- "@\"LAPSPasscodeViewControllerManagedViews\""
- "@\"LAPSRecoveryPasscodeService\""
- "@\"LARatchetViewControllerConfiguration\""
- "@\"NSArray\""
- "@\"NSArray\"24@0:8@\"UITableView\"16"
- "@\"NSArray\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSError\"16@0:8"
- "@\"NSError\"20@0:8B16"
- "@\"NSError\"24@0:8@\"LAPSPasscode\"16"
- "@\"NSError\"24@0:8@\"NSError\"16"
- "@\"NSIndexPath\"24@0:8@\"UITableView\"16"
- "@\"NSIndexPath\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSIndexPath\"40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSOrderedSet\""
- "@\"NSRegularExpression\"8@?0"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"32@0:8@\"LAPSFetchOldPasscodeCoordinator\"16q24"
- "@\"NSString\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"NSString\"32@0:8@\"UITableView\"16q24"
- "@\"NSURL\""
- "@\"UIBarButtonItem\""
- "@\"UIButton\""
- "@\"UIContextMenuConfiguration\"48@0:8@\"UITableView\"16@\"NSIndexPath\"24{CGPoint=dd}32"
- "@\"UILabel\""
- "@\"UIPageViewController\""
- "@\"UIScrollView\""
- "@\"UISwipeActionsConfiguration\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITableView\""
- "@\"UITableViewCell\"32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "@\"UITargetedPreview\"32@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24"
- "@\"UIView\""
- "@\"UIView\"24@0:8@\"UIScrollView\"16"
- "@\"UIView\"32@0:8@\"UITableView\"16q24"
- "@\"UIViewController\""
- "@\"UIViewController<LACUIAuthenticatorUI>\""
- "@\"UIViewController<LAPSPasscodeViewControlling>\""
- "@\"UIViewController<LAPSPasscodeViewControlling>\"8@?0"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"LAPSPasscodeOptionsViewControllerConfiguration\"16"
- "@24@0:8@\"LAPSPasscodeViewControllerConfiguration\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16q24"
- "@32@0:8q16@24"
- "@32@0:8q16Q24"
- "@32@0:8q16q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8q16@?24@?32"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24{CGPoint=dd}32"
- "@?"
- "B16@0:8"
- "B16@?0@\"LAPSPasscodeType\"8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"LAPSPasscode\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UIScrollView\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8q16"
- "B32@0:8@\"LAPSPasscode\"16^@24"
- "B32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "B32@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16q24"
- "B32@?0@\"LAPSPasscodeType\"8Q16^B24"
- "B40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"<UISpringLoadedInteractionContext>\"32"
- "B40@0:8@16@24@32"
- "B44@0:8@\"LAPSPasscode\"16@\"LAPSPasscode\"24B32^@36"
- "B44@0:8@16@24B32^@36"
- "B48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "B48@0:8@16:24@32@40"
- "Base"
- "Could not authenticate using credential %{public}@"
- "Could not externalize passcode"
- "InternalBase"
- "LAAuthorizationViewController"
- "LACContextObserver"
- "LACContextProviding"
- "LACPSAuthorizer"
- "LACUIAuthenticatorUIDelegate"
- "LACUIContainerViewControllerDelegate"
- "LACUIRatchetViewModelType"
- "LAContextHelper"
- "LAContextUIHelper"
- "LAContextUITrampoline"
- "LAHostingController"
- "LALocalizedString"
- "LAPSCurrentPasscodeService"
- "LAPSCurrentPasscodeServiceOptions"
- "LAPSErrorBuilder"
- "LAPSFetchNewPasscodeCoordinator"
- "LAPSFetchNewPasscodeCoordinatorDelegate"
- "LAPSFetchNewPasscodeCoordinatorInput"
- "LAPSFetchNewPasscodeCoordinatorOutput"
- "LAPSFetchNewPasscodeRequest"
- "LAPSFetchNewPasscodeResult"
- "LAPSFetchOldPasscodeCoordinator"
- "LAPSFetchOldPasscodeCoordinatorDelegate"
- "LAPSFetchOldPasscodeCoordinatorInput"
- "LAPSFetchOldPasscodeCoordinatorOutput"
- "LAPSFetchOldPasscodeRequest"
- "LAPSFetchOldPasscodeResult"
- "LAPSNewPasscodeService"
- "LAPSPasscode"
- "LAPSPasscodeBackoffTimerController"
- "LAPSPasscodeChangeAuthorizationOptions"
- "LAPSPasscodeChangeAuthorizerBuilder"
- "LAPSPasscodeChangeAuthorizerDTOAdapter"
- "LAPSPasscodeChangeController"
- "LAPSPasscodeChangeControllerOptions"
- "LAPSPasscodeChangeControllerProvider"
- "LAPSPasscodeChangeControllerProviderOptions"
- "LAPSPasscodeChangeControllerProviding"
- "LAPSPasscodeChangePreflightController"
- "LAPSPasscodeChangeSystem"
- "LAPSPasscodeChangeSystemBuilder"
- "LAPSPasscodeChangeSystemDispatchDecorator"
- "LAPSPasscodeChangeSystemOptions"
- "LAPSPasscodeChangeSystemRecoveryAdapter"
- "LAPSPasscodeChangeSystemRemovalAdapter"
- "LAPSPasscodeChangeSystemStandardAdapter"
- "LAPSPasscodeChangeSystemStubbedAdapter"
- "LAPSPasscodeChangeSystemVerificationAdapter"
- "LAPSPasscodeChangeUI"
- "LAPSPasscodeChangeUICoordinator"
- "LAPSPasscodeChangeUICoordinatorOptions"
- "LAPSPasscodeChangeUIDelegate"
- "LAPSPasscodeChangeUIPresentationController"
- "LAPSPasscodeOptionsAlertViewController"
- "LAPSPasscodeOptionsPresentationController"
- "LAPSPasscodeOptionsPresentationRequest"
- "LAPSPasscodeOptionsSheetViewController"
- "LAPSPasscodeOptionsViewController"
- "LAPSPasscodeOptionsViewControllerConfiguration"
- "LAPSPasscodeOptionsViewControllerDelegate"
- "LAPSPasscodePersistence"
- "LAPSPasscodePersistenceAdapter"
- "LAPSPasscodePersistenceCDPAdapter"
- "LAPSPasscodePersistenceLAAdapter"
- "LAPSPasscodePersistenceMCAdapter"
- "LAPSPasscodePersistenceMKBAdapter"
- "LAPSPasscodePersistenceSecAdapter"
- "LAPSPasscodeType"
- "LAPSPasscodeType.m"
- "LAPSPasscodeTypeCollection"
- "LAPSPasscodeTypeIdentifierAlphanumeric"
- "LAPSPasscodeTypeIdentifierNone"
- "LAPSPasscodeTypeIdentifierNumericCustomDigits"
- "LAPSPasscodeTypeIdentifierNumericFourDigits"
- "LAPSPasscodeTypeIdentifierNumericSixDigits"
- "LAPSPasscodeTypeIdentifierUnknown"
- "LAPSPasscodeViewController"
- "LAPSPasscodeViewControllerBase"
- "LAPSPasscodeViewControllerConfiguration"
- "LAPSPasscodeViewControllerDelegate"
- "LAPSPasscodeViewControllerManagedViews"
- "LAPSPasscodeViewControlling"
- "LAPSRecoveryPasscodeService"
- "LAPasscodeChangeErrorBuilder"
- "LAPasscodeChangeService"
- "LAPasscodeChangeServiceOptions"
- "LAPasscodeRecoveryErrorBuilder"
- "LAPasscodeRecoveryService"
- "LAPasscodeRemovalService"
- "LAPasscodeRemovalServiceOptions"
- "LAPasscodeServiceErrorBuilder"
- "LAPasscodeVerificationService"
- "LAPasscodeVerificationServiceOptions"
- "LARatchetViewController"
- "LARatchetViewControllerConfiguration"
- "LARatchetViewControllerDelegate"
- "LAView"
- "NSCopying"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<LAAuthorizationViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<LAPSFetchNewPasscodeCoordinatorDelegate>\",W,N,V_delegate"
- "T@\"<LAPSFetchOldPasscodeCoordinatorDelegate>\",W,N,V_delegate"
- "T@\"<LAPSPasscodeChangeUIDelegate>\",W,N"
- "T@\"<LAPSPasscodeChangeUIDelegate>\",W,N,Vdelegate"
- "T@\"<LAPSPasscodeOptionsViewControllerDelegate>\",W,N"
- "T@\"<LAPSPasscodeOptionsViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<LAPSPasscodePersistence>\",R,N,V_persistence"
- "T@\"<LAPSPasscodeViewControllerDelegate>\",W,N"
- "T@\"<LARatchetViewControllerDelegate>\",W,N,V_delegate"
- "T@\"LACSExtractablePassword\",&,N,V_passcode"
- "T@\"LACUIPasscodeField\",W,N,V_passcodeFieldVC"
- "T@\"LAContextUIHelper\",&,D,N"
- "T@\"LAExtractablePassword\",&,N,V_currentPasscode"
- "T@\"LAExtractablePassword\",&,N,V_newPasscode"
- "T@\"LAExtractablePassword\",&,N,V_oldPasscode"
- "T@\"LAPSPasscode\",&,N,V_passcode"
- "T@\"LAPSPasscode\",R,N,V_passcode"
- "T@\"LAPSPasscodeOptionsViewControllerConfiguration\",&,N,V_config"
- "T@\"LAPSPasscodeOptionsViewControllerConfiguration\",&,N,V_optionsConfiguration"
- "T@\"LAPSPasscodeType\",&,N,V_passcodeType"
- "T@\"LAPSPasscodeType\",&,N,V_selectedPasscodeType"
- "T@\"LAPSPasscodeType\",R,N,V_type"
- "T@\"LARatchetViewControllerConfiguration\",R,N,V_configuration"
- "T@\"NSData\",R,N"
- "T@\"NSDictionary\",R,N,V_options"
- "T@\"NSError\",R,N"
- "T@\"NSOrderedSet\",&,N,V_allowedPasscodeTypes"
- "T@\"NSString\",&,N,V_calloutReason"
- "T@\"NSString\",&,N,V_cancelTitle"
- "T@\"NSString\",&,N,V_countdownPrimaryActionTitle"
- "T@\"NSString\",&,N,V_currentPasscodePrompt"
- "T@\"NSString\",&,N,V_currentPasscodeSubPrompt"
- "T@\"NSString\",&,N,V_errorMessage"
- "T@\"NSString\",&,N,V_footer"
- "T@\"NSString\",&,N,V_footerRecoveryDisabled"
- "T@\"NSString\",&,N,V_footerRecoveryEnabled"
- "T@\"NSString\",&,N,V_nextButton"
- "T@\"NSString\",&,N,V_oldPasscodePrompt"
- "T@\"NSString\",&,N,V_oldPasscodeSubPrompt"
- "T@\"NSString\",&,N,V_passcodeOptionsCancelTitle"
- "T@\"NSString\",&,N,V_passcodeOptionsTitle"
- "T@\"NSString\",&,N,V_passcodePrompt"
- "T@\"NSString\",&,N,V_passcodeRecoveryDisabledTitle"
- "T@\"NSString\",&,N,V_passcodeRecoveryEnabledTitle"
- "T@\"NSString\",&,N,V_passcodeRecoveryTitle"
- "T@\"NSString\",&,N,V_passcodeSubPrompt"
- "T@\"NSString\",&,N,V_prompt"
- "T@\"NSString\",&,N,V_subPrompt"
- "T@\"NSString\",&,N,V_title"
- "T@\"NSString\",&,N,V_verifyNextButton"
- "T@\"NSString\",&,N,V_verifyPrompt"
- "T@\"NSString\",&,N,V_verifySubPrompt"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_passcode"
- "T@\"NSURL\",&,N,V_calloutURL"
- "T@\"UIBarButtonItem\",&,N,V_sourceItem"
- "T@\"UILabel\",W,N,V_errorCapsule"
- "T@\"UILabel\",W,N,V_footerLabel"
- "T@\"UILabel\",W,N,V_headerLabel"
- "T@\"UILabel\",W,N,V_subHeaderLabel"
- "T@\"UIScrollView\",W,N,V_scrollView"
- "T@\"UIView\",&,N,V_sourceView"
- "T@\"UIView\",W,N,V_errorCapsuleContainer"
- "T@\"UIViewController\",R,N,V_parentVC"
- "T@\"UIViewController\",R,N,V_sourceViewController"
- "TB,N,V_animated"
- "TB,N,V_dismissUIAfterCompletion"
- "TB,N,V_hidePasscodeRecoveryMessage"
- "TB,N,V_isPasscodeRecoveryEnabled"
- "TB,N,V_isPasscodeRecoveryMessageHidden"
- "TB,N,V_isPasscodeRecoveryOptionVisible"
- "TB,N,V_isPasscodeRecoveryRestricted"
- "TB,N,V_isPasscodeRecoverySupported"
- "TB,N,V_isPasscodeSet"
- "TB,N,V_shouldAvoidBecomingFirstResponderOnStart"
- "TB,N,V_skipNewPasscode"
- "TB,N,V_skipOldPasscode"
- "TB,N,V_skipSuccessNotification"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isPasscodeRecoveryEnabled"
- "TQ,R"
- "TQ,R,N,V_length"
- "Tq,N,V_backoffTimeout"
- "Tq,N,V_failedAttempts"
- "Tq,N,V_identifier"
- "Tq,N,V_presentationStyle"
- "Tq,R,N,V_useCase"
- "UI"
- "UIScrollViewDelegate"
- "UITableViewDataSource"
- "UITableViewDelegate"
- "URLWithString:"
- "Vv16@0:8"
- "[[LAPSPasscodeType noneType] allowsString:string]"
- "[[_input passcodeType] isEqual:[passcode type]]"
- "[simplestAllowedPasscodeType identifier] != LAPSPasscodeTypeIdentifierNone"
- "^$"
- "^.+$"
- "^\\d+$"
- "^\\d{4}$"
- "^\\d{6}$"
- "^{_NSZone=}16@0:8"
- "_TtC29LocalAuthenticationEmbeddedUI17LAContextProvider"
- "_addActionForPasscodeType:"
- "_addActionForRecoveryEnabled:restricted:"
- "_addActionWithTitle:style:completion:"
- "_addActionWithTitle:style:handler:shouldDismissHandler:"
- "_addSectionDelimiter"
- "_alertControllerWithTitle:message:"
- "_allWhere:"
- "_allowedPasscodeTypes"
- "_animated"
- "_applicationDidEnterBackground:"
- "_applicationKeyWindow"
- "_authenticateWithOptions:acl:availableMechanisms:hostVC:context:operation:updatedOptions:reply:"
- "_authorizeOperationWithIdentifier:options:completion:"
- "_authorizePasscodeChangeWithCompletion:"
- "_authorizePasscodeRecoveryWithCompletion:"
- "_authorizePasscodeRemovalWithCompletion:"
- "_authorizePasscodeVerificationWithCompletion:"
- "_authorizer"
- "_authorizerWithUseCase:options:"
- "_backoffTimeout"
- "_bodyStackHorizontalPadding"
- "_bodyStackSpacing"
- "_builder"
- "_calloutReason"
- "_calloutURL"
- "_canShowWhileLocked"
- "_cancelTitle"
- "_cdpAdapter"
- "_cellIdentifierForIndexPath:"
- "_changePasscodeRecoveryStatus:"
- "_changeSelectedPasscodeTypeIndex:"
- "_changeSystem"
- "_checkCanChangePasscodeWithCompletion:"
- "_clearRecoveryPasscode"
- "_close:"
- "_completion"
- "_completionHandler"
- "_config"
- "_configuration"
- "_configurePasscodeSubPromptForConfig:request:"
- "_configureVerifySubPromptForConfig:request:"
- "_containerVC"
- "_countdownPrimaryActionTitle"
- "_currentPasscode"
- "_currentPasscodePrompt"
- "_currentPasscodeService"
- "_currentPasscodeSubPrompt"
- "_customKeyboardGuide"
- "_deactivate"
- "_decoratedSystem:"
- "_defaultSystemOptions"
- "_delegate"
- "_deviceLockStateValueForKey:"
- "_deviceSecretType:"
- "_dismiss"
- "_dismissUIAfterCompletion"
- "_dismissWithCompletion:"
- "_errorCapsule"
- "_errorCapsuleContainer"
- "_errorMessage"
- "_errorWithCode:debugDescription:"
- "_errorWithCode:userInfo:"
- "_extractCSPasscode:completion:"
- "_extractPasscode:completion:"
- "_failedAttempts"
- "_failedPasscodeAttempts"
- "_failedPasscodeRecoveryAttempts"
- "_fetchNewPasscode:completion:"
- "_fetchOldPasscode:completion:"
- "_finishWithError:"
- "_flashScrollIndicatorsPersistingPreviousFlashes"
- "_footer"
- "_footerLabel"
- "_footerRecoveryDisabled"
- "_footerRecoveryEnabled"
- "_footerText"
- "_genericErrorWithDebugDescription:"
- "_genericErrorWithUserInfo:"
- "_handleCancel:"
- "_handleNext:"
- "_handler"
- "_hasAttemptedPasscodeEnoughTimes"
- "_hasPasscodeRecoveryAttemptsLeft"
- "_headerLabel"
- "_heightForFooterInSection:"
- "_heightForHeaderInSection:"
- "_hidePasscodeRecoveryMessage"
- "_identifier"
- "_injectNewPasscodeWithCompletion:"
- "_injectOldPasscodeWithCompletion:"
- "_input"
- "_internalOptions"
- "_invokeHandlerWithError:"
- "_invokeHandlerWithOutput:"
- "_invokeHandlerWithOutput:error:"
- "_isInViewHierarchy"
- "_isNextButtonEnabled"
- "_isPasscodeRecoveryEnabled"
- "_isPasscodeRecoveryMessageHidden"
- "_isPasscodeRecoveryOptionVisible"
- "_isPasscodeRecoveryRestricted"
- "_isPasscodeRecoverySupported"
- "_isPasscodeSet"
- "_isRemoteVCPrepared"
- "_laAdapter"
- "_length"
- "_localizedDescriptionFromError:"
- "_localizedErrorMessageForBiometryType:"
- "_localizedErrorTitleForBiometryType:"
- "_mainStackHorizontalPadding"
- "_mainStackInsets"
- "_mainStackSpacing"
- "_managedViews"
- "_maxPasscodeRecoveryAttempts"
- "_mcAdapter"
- "_mcProfileConnection"
- "_mementoStateValueForKey:"
- "_minRequiredPasscodeFailures"
- "_mkbAdapter"
- "_newPasscode"
- "_newPasscodeService"
- "_nextButton"
- "_notifyCompletionWithPasscode:error:"
- "_oldPasscode"
- "_oldPasscodePrompt"
- "_oldPasscodeSubPrompt"
- "_operation"
- "_options"
- "_optionsButton"
- "_optionsConfiguration"
- "_pageViewController"
- "_parentModalInPresentationOriginalFlag"
- "_parentVC"
- "_passcode"
- "_passcodeFieldVC"
- "_passcodeOptionsCancelTitle"
- "_passcodeOptionsTitle"
- "_passcodePrompt"
- "_passcodeRecoveryDisabledTitle"
- "_passcodeRecoveryEnabledTitle"
- "_passcodeRecoveryService"
- "_passcodeRecoveryTitle"
- "_passcodeStubbedSystem"
- "_passcodeSubPrompt"
- "_passcodeType"
- "_passcodeType == [passcode type]"
- "_passcodeTypeForQuery:"
- "_passcodeVC"
- "_performOnBackgroundQueue:"
- "_performOnMainQueue:"
- "_persistence"
- "_persistenceErrorWithPasscodeVerificationStatus:"
- "_preferredFontForTextStyle:weight:"
- "_presentErrorIfNeed:completion:"
- "_presentNewPasscodeVCWithTransitionStyle:"
- "_presentNewPasscodeVCWithTransitionStyle:errorMessage:"
- "_presentPasscodeDoesNotMeetRequirementsError:completion:"
- "_presentPasscodeIsTooSimpleErrorWithCompletion:"
- "_presentPasscodeOptionsAlert:completion:"
- "_presentPasscodeOptionsPopOverWithContentVC:request:completion:"
- "_presentPasscodeOptionsPopover:completion:"
- "_presentPasscodeOptionsSheet:completion:"
- "_presentPasscodeVC"
- "_presentPasscodesDidNotMatchErrorWithCompletion:"
- "_presentVerifyPasscodeVCWithTransitionStyle:"
- "_presentViewController:transitionStyle:"
- "_presentationContext"
- "_presentationController"
- "_presentationStyle"
- "_prompt"
- "_recoveryController"
- "_recoveryPasscodeService"
- "_remoteVC"
- "_reportPasscodeChangedTo:"
- "_restoreParentModalInPresentationFlag"
- "_rootVC"
- "_runWithCompletion:"
- "_scrollTo:"
- "_scrollToPasscodeField"
- "_scrollView"
- "_secAdapter"
- "_selectedPasscodeType"
- "_selectedPasscodeTypeIndex"
- "_setActionWithTitle:enabled:"
- "_setPasscodeRecoveryEnabled:"
- "_setPasscodeType:"
- "_setup"
- "_setupParentVCIfNeededAnimated:"
- "_shouldAvoidBecomingFirstResponderOnStart"
- "_shouldInjectNewPasscode"
- "_shouldInjectOldPasscode"
- "_shouldShowNextButton"
- "_shouldUseFooterMessages"
- "_shouldUseStandardKeyboardGuide"
- "_showPasscodeOptions:"
- "_showPasscodeOptionsSourceWithView:sourceItem:presentationStyle:shouldResignFirstResponder:"
- "_skipNewPasscode"
- "_skipOldPasscode"
- "_skipSuccessNotification"
- "_sourceItem"
- "_sourceView"
- "_sourceViewController"
- "_startOperation:completion:"
- "_startTimerWithTimeout:"
- "_storeParentModalInPresentationFlag"
- "_style"
- "_subHeaderLabel"
- "_subPrompt"
- "_subPromptForRequest:"
- "_submitPasscode:"
- "_subscriptions"
- "_system"
- "_tableCellTextColor"
- "_tableRowShouldDismissOnSelection"
- "_tableView"
- "_tableViewNeedsHeaderView"
- "_tableViewStyle"
- "_timeout"
- "_timer"
- "_title"
- "_type"
- "_ui"
- "_uiWithOptions:"
- "_updateHandler"
- "_useCase"
- "_useStubbedAdapter"
- "_validateAvailableMechanims:completion:"
- "_verifyNextButton"
- "_verifyPasscode:options:"
- "_verifyPrompt"
- "_verifySubPrompt"
- "_viewModel"
- "_widthMultiplier"
- "_workQueue"
- "actionWithHandler:"
- "actionWithTitle:style:handler:"
- "actions"
- "activateConstraints:"
- "active"
- "addAction:"
- "addAction:forControlEvents:"
- "addArrangedSubview:"
- "addChildViewController:"
- "addContextObserver:"
- "addObserver:selector:name:object:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "alertControllerWithTitle:message:preferredStyle:"
- "allPasscodeTypes"
- "allPasscodeTypesWhereComplexityIsGreaterThanOrEqualTo:"
- "allowedPasscodeTypes"
- "allowsLength:"
- "allowsString:"
- "alphanumericType"
- "animated"
- "appendString:"
- "armWithOptions:completion:"
- "arrayWithObjects:count:"
- "authenticateWithOptions:availableMechanisms:hostVC:context:reply:"
- "authorizationController:didProvideAuthorizationRequirementWithReply:"
- "authorizeWithCompletion:"
- "authorizeWithLocalizedReason:completion:"
- "authorizeWithLocalizedReason:inPresentationContext:completion:"
- "authorizeWithOptions:completion:"
- "authorizerWithOptions:"
- "autorelease"
- "backgroundColor"
- "backoffTimeout"
- "becomeFirstResponder"
- "biometryType"
- "boolValue"
- "bottomAnchor"
- "bounds"
- "buildWithAvailableMechanisms:"
- "bundleForClass:"
- "buttonWithConfiguration:primaryAction:"
- "buttonWithType:"
- "canBecomeFirstResponder"
- "canChangePasscode"
- "canChangePasscodeWithError:"
- "canEvaluatePolicy:error:"
- "canOpenURL:"
- "canRemovePasscode:"
- "canRemovePasscodeWithError:"
- "cancel"
- "cancelRecovery"
- "cancelTitle"
- "cellForRowAtIndexPath:"
- "centerXAnchor"
- "centerYAnchor"
- "changePasscode:to:completion:"
- "changePasscode:to:enableRecovery:completion:"
- "changePasscode:to:enableRecovery:error:"
- "changePasscodeFrom:to:skipRecovery:outError:"
- "changePasscodeWithRecoveryPasscode:to:skipRecovery:outError:"
- "checkError:hasCode:"
- "checkErrorIsInteractive:"
- "class"
- "clean"
- "clear"
- "clearRecoveryPasscode"
- "clearWithErrorMessage:"
- "clientCanceledError"
- "code"
- "compare:"
- "complexityRating"
- "config"
- "configuration"
- "configurationWithFont:scale:"
- "conformsToProtocol:"
- "constraintEqualToAnchor:"
- "constraintEqualToAnchor:constant:"
- "constraintEqualToAnchor:multiplier:"
- "constraintEqualToConstant:"
- "constraintGreaterThanOrEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintLessThanOrEqualToAnchor:"
- "constraintLessThanOrEqualToAnchor:constant:"
- "containerViewControllerViewDidDisappear:"
- "containsObject:"
- "contentSize"
- "contextDidBecomeInvalid:"
- "continueWithPasscode:"
- "convertRect:toView:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countdownPrimaryActionTitle"
- "createContext"
- "createUserInitiatedSerialQueueWithIdentifier:"
- "currentDevice"
- "currentPasscode"
- "currentPasscodePrompt"
- "currentPasscodeSubPrompt"
- "currentViewController"
- "customDetentWithIdentifier:resolver:"
- "d16@0:8"
- "d24@0:8q16"
- "d32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "d32@0:8@\"UITableView\"16q24"
- "d32@0:8@16@24"
- "d32@0:8@16q24"
- "data"
- "dataUsingEncoding:"
- "dateByAddingTimeInterval:"
- "deactivateConstraints:"
- "deactivateWithCompletion:"
- "dealloc"
- "debugDescription"
- "decimalDigitCharacterSet"
- "defaultCenter"
- "defaultContentConfiguration"
- "defaultNewPasscodeEntryScreenTypeWithOutSimplePasscodeType:"
- "defaultNewPasscodeType"
- "delegate"
- "deniedByLAError"
- "deniedByMDMError"
- "dequeueReusableCellWithIdentifier:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "didProvideAuthorizationRequirementWithReply:"
- "dismiss"
- "dismissViewControllerAnimated:completion:"
- "dismissWithCompletion:"
- "domain"
- "dtoLearnMoreLinkURL"
- "dtoUnexpectedSecurityDelayRadarURL"
- "emptyPasscode"
- "enterPasscode"
- "error == nil"
- "error:hasCode:"
- "errorCapsule"
- "errorCapsuleContainer"
- "errorMessage"
- "errorWithCode:"
- "errorWithCode:debugDescription:"
- "errorWithCode:userInfo:"
- "errorWithDomain:code:userInfo:"
- "evaluateAccessControl:context:operation:options:presentationContext:reply:"
- "evaluateAccessControl:operation:options:presentationContext:reply:"
- "evaluateAccessControl:operation:options:reply:"
- "evaluateAndPresentViewController"
- "evaluateAndShowViewController"
- "exceptionWithName:reason:userInfo:"
- "externalizePasscode"
- "externalizedContext"
- "extractPasswordWithCompletion:"
- "faceIDServiceName"
- "failedAttempts"
- "failedPasscodeAttempts"
- "failedPasscodeRecoveryAttempts"
- "featureFlagPasscodeServicesProtectionEnabled"
- "featureFlagPasscodeServicesUseKeyboardGuideEnabled"
- "featureFlagPasscodeServicesUseKeyboardGuidePadsEnabled"
- "fetchNewPasscode:completion:"
- "fetchNewPasscodeCoordinator:verifyPasscode:"
- "fetchNewPasscodeCoordinator:verifyPasscode:matchesPasscode:"
- "fetchOldPasscode:completion:"
- "fetchOldPasscodeCoordinator:backoffMessageForTimeout:"
- "fetchOldPasscodeCoordinator:verifyPasscode:"
- "finishWithError:"
- "finishWithPasscode:"
- "finishWithResult:error:"
- "firstObject"
- "focus"
- "footer"
- "footerLabel"
- "footerRecoveryDisabled"
- "footerRecoveryEnabled"
- "frame"
- "genericError"
- "genericErrorWithDebugDescription:"
- "genericErrorWithUnderlyingError:"
- "genericErrorWithUnderlyingError:debugDescription:"
- "grayButtonConfiguration"
- "hasFixedLength"
- "hasPasscode"
- "hash"
- "headerLabel"
- "heightAnchor"
- "hideSpinner"
- "identifier"
- "indexOfObject:"
- "indexPathForPreferredFocusedViewInTableView:"
- "indexPathForSelectedRow"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithArray:"
- "initWithAuthorizer:"
- "initWithAuthorizers:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithConfiguration:"
- "initWithConfiguration:completion:"
- "initWithConfiguration:style:"
- "initWithContext:requirement:options:"
- "initWithControllerBuilder:"
- "initWithCustomView:"
- "initWithData:encoding:"
- "initWithExternalizedContext:"
- "initWithFrame:"
- "initWithFrame:style:"
- "initWithIdentifier:"
- "initWithIdentifier:length:"
- "initWithImage:"
- "initWithImage:menu:"
- "initWithLocalizedPasscode:type:"
- "initWithNibName:bundle:"
- "initWithOptions:"
- "initWithOptions:configuration:"
- "initWithParentVC:"
- "initWithParentVC:containerVC:"
- "initWithParentVC:options:"
- "initWithPasscode:"
- "initWithPasscode:isPasscodeRecoveryEnabled:"
- "initWithPasscode:type:"
- "initWithPersistence:"
- "initWithPersistence:options:"
- "initWithRawPasscode:"
- "initWithRawPasscode:isPasscodeRecoveryEnabled:"
- "initWithRequiredEntitlements:"
- "initWithRootViewController:"
- "initWithSourceViewController:"
- "initWithString:attributes:"
- "initWithStyle:"
- "initWithStyle:reuseIdentifier:"
- "initWithSystem:"
- "initWithSystem:authorizer:ui:"
- "initWithSystem:authorizer:ui:options:"
- "initWithSystem:workQueue:"
- "initWithTimeout:updateHandler:completionHandler:"
- "initWithTransitionStyle:navigationOrientation:options:"
- "initWithUseCase:"
- "initWithView:"
- "integerValue"
- "internalOptions"
- "invalidPasscodeError"
- "invalidPasscodeErrorWithFailedAttemptsCount:"
- "invalidPasscodeErrorWithFailedAttemptsCount:backoffTimeout:"
- "invalidate"
- "isAccessibilityTextEnabled"
- "isDescendantOfView:"
- "isEqual:"
- "isEqualToString:"
- "isHidden"
- "isIdiomPad"
- "isInViewHierarchy"
- "isInvalidated"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isModalInPresentation"
- "isOn"
- "isPasscodeLockedOut"
- "isPasscodeModificationAllowed"
- "isPasscodeRecoveryAllowed"
- "isPasscodeRecoveryAvailable"
- "isPasscodeRecoveryAvailableWithError:"
- "isPasscodeRecoveryEnabled"
- "isPasscodeRecoveryMessageHidden"
- "isPasscodeRecoveryOptionVisible"
- "isPasscodeRecoveryRestricted"
- "isPasscodeRecoverySupported"
- "isPasscodeRequired"
- "isPasscodeSet"
- "isProxy"
- "isRecoveryAvailableWithError:"
- "keyboardLayoutGuide"
- "labelColor"
- "lastPasscodeChange"
- "layoutIfNeeded"
- "leadingAnchor"
- "length"
- "loadView"
- "localSecretChangedTo:secretType:completion:"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "localizedDescriptionOfDefaultNewPasscodeConstraints"
- "localizedName"
- "localizedPasscodeRequirements"
- "localizedStringForKey:value:table:"
- "makeHostingControllerWithConfiguration:"
- "makeViewControllerWithOptions:"
- "makeViewControllerWithOptions:configuration:"
- "mapError:"
- "maxPasscodeRecoveryAttempts"
- "minimumNewPasscodeEntryScreenTypeWithOutSimplePasscodeType:"
- "modalPresentationStyle"
- "modalTransitionStyle"
- "mutableCopy"
- "navigationItem"
- "newPasscode"
- "newPasscodeDoesNotMeetRequirementsErrorWithLocalizedDescription:"
- "newPasscodeIsTooEasyError"
- "newPasscodeRequest"
- "nextButton"
- "noneType"
- "now"
- "null"
- "numberFromString:"
- "numberOfSectionsInTableView:"
- "numberWithInteger:"
- "numericCustomDigitsType"
- "numericFourDigitsType"
- "numericSixDigitsType"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "ok"
- "oldPasscode"
- "oldPasscodePrompt"
- "oldPasscodeRequest"
- "oldPasscodeSubPrompt"
- "openURL:options:completionHandler:"
- "options"
- "optionsConfiguration"
- "optionsForRatchetArmOptions:"
- "orderedSetWithArray:"
- "pageViewController"
- "parentVC"
- "parentViewController"
- "passcode"
- "passcode:meetsCurrentConstraintsOutError:"
- "passcodeChangeBackoffMessage:"
- "passcodeChangeControllerWithOptions:"
- "passcodeChangeDone"
- "passcodeChangeErrorInvalidPasscodeWithFailedAttemptsCount:"
- "passcodeChangeErrorNewPasscodeMismatchInlineText"
- "passcodeChangeErrorNewPasscodeMismatchText"
- "passcodeChangeErrorNewPasscodeMismatchTitle"
- "passcodeChangeErrorPasscodeDoesNotMeetRequirementsInlineText"
- "passcodeChangeErrorPasscodeDoesNotMeetRequirementsText"
- "passcodeChangeErrorPasscodeDoesNotMeetRequirementsTitle"
- "passcodeChangeErrorPasscodeIsTooEasyText"
- "passcodeChangeErrorPasscodeIsTooEasyTitle"
- "passcodeChangeFailedTitle"
- "passcodeChangeLocalizedReason"
- "passcodeChangeNewPasscode"
- "passcodeChangeNewPasscodeVerify"
- "passcodeChangeNext"
- "passcodeChangeNotAvailable"
- "passcodeChangeOldPasscode"
- "passcodeChangeOptions"
- "passcodeChangeRatchetBeginText"
- "passcodeChangeRatchetBeginTitle"
- "passcodeChangeRatchetCalloutReason"
- "passcodeChangeRatchetCountdownText"
- "passcodeChangeSubPrompt"
- "passcodeChangeSystem"
- "passcodeChangeSystemWithOptions:"
- "passcodeChangeSystemWithPersistence:"
- "passcodeChangeSystemWithPersistence:options:"
- "passcodeChangeTitle"
- "passcodeChangeUI:verifyNewPasscode:completion:"
- "passcodeChangeUI:verifyPasscode:completion:"
- "passcodeChangeUIDidDisappear:"
- "passcodeChangeUseAnyway"
- "passcodeChangeUseDifferentPasscode"
- "passcodeCreationDate"
- "passcodeField:didChangePasscodeLength:"
- "passcodeField:didSubmitPasscode:"
- "passcodeFieldVC"
- "passcodeOptionsCancelTitle"
- "passcodeOptionsTitle"
- "passcodeOptionsViewController:didSelectPasscodeType:"
- "passcodeOptionsViewController:didSetPasscodeRecoveryEnabled:"
- "passcodeOptionsViewControllerDidDisappear:"
- "passcodeOptionsViewControllerWillDisappear:"
- "passcodeRecoveryControllerWithOptions:"
- "passcodeRecoveryDisabledTitle"
- "passcodeRecoveryEnabledTitle"
- "passcodeRecoveryFailedTitle"
- "passcodeRecoveryOldPasscodePrompt"
- "passcodeRecoveryOldPasscodeSubPrompt"
- "passcodeRecoveryPreflightController"
- "passcodeRecoveryRecoveryDisabled"
- "passcodeRecoveryRecoveryEnabled"
- "passcodeRecoverySystem"
- "passcodeRecoverySystemWithPersistence:"
- "passcodeRecoveryTitle"
- "passcodeRemovalControllerWithOptions:"
- "passcodeRemovalFailedTitle"
- "passcodeRemovalLocalizedReason"
- "passcodeRemovalNotAllowedTextFaceID"
- "passcodeRemovalNotAllowedTextOpticID"
- "passcodeRemovalNotAllowedTextTouchID"
- "passcodeRemovalNotAllowedTitleFaceID"
- "passcodeRemovalNotAllowedTitleOpticID"
- "passcodeRemovalNotAllowedTitleTouchID"
- "passcodeRemovalOldPasscode"
- "passcodeRemovalRatchetBeginText"
- "passcodeRemovalRatchetBeginTitle"
- "passcodeRemovalRatchetCalloutReason"
- "passcodeRemovalRatchetCountdownText"
- "passcodeRemovalSystem"
- "passcodeRemovalSystemWithPersistence:"
- "passcodeRemovalTitle"
- "passcodeSubPrompt"
- "passcodeType"
- "passcodeTypeAlphanumeric"
- "passcodeTypeNone"
- "passcodeTypeNumericCustomDigits"
- "passcodeTypeNumericFourDigits"
- "passcodeTypeNumericSixDigits"
- "passcodeVerificationControllerWithOptions:"
- "passcodeVerificationPrompt"
- "passcodeVerificationSubPrompt"
- "passcodeVerificationSystem"
- "passcodeVerificationSystemWithPersistence:"
- "passcodeVerificationTitle"
- "passcodeViewController:didCancelWithError:"
- "passcodeViewController:didSelectPasscodeType:"
- "passcodeViewController:didSetPasscodeRecoveryEnabled:"
- "passcodeViewController:verifyPasscode:"
- "performRecovery:newPasscode:enableRecovery:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "persistence"
- "popoverPresentationController"
- "preferredContentSize"
- "preferredContentSizeCategory"
- "preferredFontForTextStyle:"
- "preferredStatusBarStyle"
- "prepareRemoteSceneWithCompletion:"
- "presentAlertVC:"
- "presentAlertWithTitle:message:button:completion:"
- "presentInContainerViewController:"
- "presentPasscodeOptions:completion:"
- "presentVC:animated:"
- "presentVC:transitionStyle:"
- "presentViewController:animated:completion:"
- "presentViewController:transitionStyle:"
- "presentationContext"
- "presentationStyle"
- "presentedViewController"
- "presentingViewController"
- "prompt"
- "pushViewController:animated:"
- "q16@0:8"
- "q24@0:8@\"UITableView\"16"
- "q24@0:8@16"
- "q24@?0@\"LAPSPasscodeType\"8@\"LAPSPasscodeType\"16"
- "q32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "q32@0:8@\"UITableView\"16q24"
- "q32@0:8@16@24"
- "q32@0:8@16q24"
- "q40@0:8@\"UITableView\"16@\"NSString\"24q32"
- "q40@0:8@16@24q32"
- "rangeOfFirstMatchInString:options:range:"
- "ratchetErrorForError:"
- "ratchetResultForResult:"
- "ratchetViewController:didFinishWithResult:error:"
- "ratchetViewControllerDidAppear:"
- "recoveryPasscodeAvailable"
- "recoveryPasscodeType"
- "recoveryPasscodeUnlockScreenTypeWithOutSimplePasscodeType:"
- "redactError:"
- "regularExpressionWithPattern:options:error:"
- "release"
- "removeObject:"
- "removeObjectForKey:"
- "reportPasscodeDidChangeTo:completion:"
- "reportPasscodeDidChangeTo:passcodeType:completion:"
- "requestAuthorizationForService:completion:"
- "resignFirstResponder"
- "respondsToSelector:"
- "restart"
- "restartWithErrorMessage:"
- "retain"
- "retainCount"
- "rightBarButtonItem"
- "rootViewController"
- "row"
- "scrollView"
- "scrollViewDidChangeAdjustedContentInset:"
- "scrollViewDidEndDecelerating:"
- "scrollViewDidEndDragging:willDecelerate:"
- "scrollViewDidEndScrollingAnimation:"
- "scrollViewDidEndZooming:withView:atScale:"
- "scrollViewDidScroll:"
- "scrollViewDidScrollToTop:"
- "scrollViewDidZoom:"
- "scrollViewShouldScrollToTop:"
- "scrollViewWillBeginDecelerating:"
- "scrollViewWillBeginDragging:"
- "scrollViewWillBeginZooming:withView:"
- "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
- "secondaryLabelColor"
- "section"
- "sectionIndexTitlesForTableView:"
- "selectRowAtIndexPath:animated:scrollPosition:"
- "selectedPasscodeType"
- "self"
- "sender"
- "setAcceptInputs:"
- "setAccessoryType:"
- "setAccessoryView:"
- "setAction:"
- "setActive:"
- "setAlignment:"
- "setAllowedPasscodeTypes:"
- "setAllowsMultipleSelection:"
- "setAnimated:"
- "setAttributedTitle:forState:"
- "setAxis:"
- "setBackBarButtonItem:"
- "setBackgroundColor:"
- "setBackoffTimeout:"
- "setCalloutReason:"
- "setCalloutURL:"
- "setCanShowInLockScreen:"
- "setCancelTitle:"
- "setColor:"
- "setConfig:"
- "setContentConfiguration:"
- "setContentHuggingPriority:forAxis:"
- "setContentInsets:"
- "setContentMode:"
- "setContentOffset:animated:"
- "setCornerStyle:"
- "setCountdownPrimaryActionTitle:"
- "setCredential:type:"
- "setCredential:type:error:"
- "setCurrentPasscode:"
- "setCurrentPasscodePrompt:"
- "setCurrentPasscodeSubPrompt:"
- "setCustomSpacing:afterView:"
- "setDataSource:"
- "setDelegate:"
- "setDetents:"
- "setDirectionalLayoutMargins:"
- "setDismissUIAfterCompletion:"
- "setDistribution:"
- "setEnabled:"
- "setErrorCapsule:"
- "setErrorCapsuleContainer:"
- "setErrorMessage:"
- "setFailedAttempts:"
- "setFont:"
- "setFooter:"
- "setFooterLabel:"
- "setFooterRecoveryDisabled:"
- "setFooterRecoveryEnabled:"
- "setFrame:"
- "setHeader:"
- "setHeaderLabel:"
- "setHidden:"
- "setHidePasscodeRecoveryMessage:"
- "setHidesBackButton:animated:"
- "setIdentifier:"
- "setImage:"
- "setImageColorTransformer:"
- "setIsInViewHierarchy:"
- "setIsPasscodeRecoveryEnabled:"
- "setIsPasscodeRecoveryMessageHidden:"
- "setIsPasscodeRecoveryOptionVisible:"
- "setIsPasscodeRecoveryRestricted:"
- "setIsPasscodeRecoverySupported:"
- "setIsPasscodeSet:"
- "setLayoutMarginsRelativeArrangement:"
- "setLeftBarButtonItem:"
- "setLocale:"
- "setModalInPresentation:"
- "setModalPresentationStyle:"
- "setNewPasscode:"
- "setNextButton:"
- "setNumberOfLines:"
- "setObject:forKeyedSubscript:"
- "setOldPasscode:"
- "setOldPasscodePrompt:"
- "setOldPasscodeSubPrompt:"
- "setOn:"
- "setOptionsConfiguration:"
- "setPasscode:"
- "setPasscodeFieldVC:"
- "setPasscodeOptionsCancelTitle:"
- "setPasscodeOptionsTitle:"
- "setPasscodePrompt:"
- "setPasscodeRecoveryDisabledTitle:"
- "setPasscodeRecoveryEnabled:"
- "setPasscodeRecoveryEnabledTitle:"
- "setPasscodeRecoveryTitle:"
- "setPasscodeSubPrompt:"
- "setPasscodeType:"
- "setPermittedArrowDirections:"
- "setPreferredCornerRadius:"
- "setPreferredStyle:"
- "setPreferredSymbolConfigurationForImage:"
- "setPresentationStyle:"
- "setPrompt:"
- "setRightBarButtonItem:"
- "setScrollView:"
- "setSectionHeaderTopPadding:"
- "setSelected:"
- "setSelectedPasscodeType:"
- "setSelectionStyle:"
- "setShouldAvoidBecomingFirstResponderOnStart:"
- "setShouldTrackPreferredContentSize:"
- "setShowsHorizontalScrollIndicator:"
- "setSkipNewPasscode:"
- "setSkipOldPasscode:"
- "setSkipSuccessNotification:"
- "setSourceItem:"
- "setSourceRect:"
- "setSourceView:"
- "setSpacing:"
- "setStyle:"
- "setSubHeader:"
- "setSubHeaderLabel:"
- "setSubPrompt:"
- "setSubscriptions:"
- "setTableHeaderView:"
- "setTarget:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTintColor:"
- "setTitle:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUiHelper:"
- "setUserInteractionEnabled:"
- "setVerifyNextButton:"
- "setVerifyPrompt:"
- "setVerifySubPrompt:"
- "setView:"
- "setViewControllers:direction:animated:completion:"
- "setViewModel:"
- "setup"
- "setupNavigationItem"
- "shakeWithCompletion:"
- "sharedApplication"
- "sharedConnection"
- "sharedInstance"
- "sheetDidFinishWithError:"
- "sheetPresentationController"
- "shouldAvoidBecomingFirstResponderOnStart"
- "shouldShowPasscodeOptionsButton"
- "showPasscodeOptionsSourceItem:presentationStyle:shouldResignFirstResponder:"
- "showPasscodeOptionsSourceWithView:presentationStyle:shouldResignFirstResponder:"
- "showPasscodeValidationError:completion:"
- "showSpinner"
- "showViewController:sender:"
- "simplestAllowedNewPasscodeType"
- "skipNewPasscode"
- "skipOldPasscode"
- "sortedArrayUsingComparator:"
- "sourceItem"
- "sourceView"
- "sourceViewController"
- "start"
- "startAnimating"
- "startBackoffWithTimeout:"
- "startInParentVC:completion:"
- "startInParentVC:options:completion:"
- "startRecoveryInParentVC:completion:"
- "startWithCompletion:"
- "startWithConfiguration:reply:"
- "startWithInput:presentationController:completion:"
- "stopWithReason:invalidate:"
- "stopWithReply:"
- "stringByTrimmingCharactersInSet:"
- "stringFromNumber:"
- "stringWithFormat:"
- "style"
- "styleWithPasscodeType:"
- "subHeaderLabel"
- "subPrompt"
- "submit"
- "subscriptions"
- "substringWithRange:"
- "subviews"
- "superclass"
- "supportedInterfaceOrientations"
- "systemBackgroundColor"
- "systemBlueColor"
- "systemCanceledErrorWithDebugDescription:"
- "systemImageNamed:"
- "tableCellBlueTextColor"
- "tableView:accessoryButtonTappedForRowWithIndexPath:"
- "tableView:accessoryTypeForRowWithIndexPath:"
- "tableView:canEditRowAtIndexPath:"
- "tableView:canFocusRowAtIndexPath:"
- "tableView:canMoveRowAtIndexPath:"
- "tableView:canPerformAction:forRowAtIndexPath:withSender:"
- "tableView:canPerformPrimaryActionForRowAtIndexPath:"
- "tableView:cellForRowAtIndexPath:"
- "tableView:commitEditingStyle:forRowAtIndexPath:"
- "tableView:contextMenuConfigurationForRowAtIndexPath:point:"
- "tableView:didBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:didDeselectRowAtIndexPath:"
- "tableView:didEndDisplayingCell:forRowAtIndexPath:"
- "tableView:didEndDisplayingFooterView:forSection:"
- "tableView:didEndDisplayingHeaderView:forSection:"
- "tableView:didEndEditingRowAtIndexPath:"
- "tableView:didHighlightRowAtIndexPath:"
- "tableView:didSelectRowAtIndexPath:"
- "tableView:didUnhighlightRowAtIndexPath:"
- "tableView:didUpdateFocusInContext:withAnimationCoordinator:"
- "tableView:editActionsForRowAtIndexPath:"
- "tableView:editingStyleForRowAtIndexPath:"
- "tableView:estimatedHeightForFooterInSection:"
- "tableView:estimatedHeightForHeaderInSection:"
- "tableView:estimatedHeightForRowAtIndexPath:"
- "tableView:heightForFooterInSection:"
- "tableView:heightForHeaderInSection:"
- "tableView:heightForRowAtIndexPath:"
- "tableView:indentationLevelForRowAtIndexPath:"
- "tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:moveRowAtIndexPath:toIndexPath:"
- "tableView:numberOfRowsInSection:"
- "tableView:performAction:forRowAtIndexPath:withSender:"
- "tableView:performPrimaryActionForRowAtIndexPath:"
- "tableView:previewForDismissingContextMenuWithConfiguration:"
- "tableView:previewForHighlightingContextMenuWithConfiguration:"
- "tableView:sectionForSectionIndexTitle:atIndex:"
- "tableView:selectionFollowsFocusForRowAtIndexPath:"
- "tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:"
- "tableView:shouldHighlightRowAtIndexPath:"
- "tableView:shouldIndentWhileEditingRowAtIndexPath:"
- "tableView:shouldShowMenuForRowAtIndexPath:"
- "tableView:shouldSpringLoadRowAtIndexPath:withContext:"
- "tableView:shouldUpdateFocusInContext:"
- "tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:"
- "tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:"
- "tableView:titleForFooterInSection:"
- "tableView:titleForHeaderInSection:"
- "tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:"
- "tableView:viewForFooterInSection:"
- "tableView:viewForHeaderInSection:"
- "tableView:willBeginEditingRowAtIndexPath:"
- "tableView:willDeselectRowAtIndexPath:"
- "tableView:willDisplayCell:forRowAtIndexPath:"
- "tableView:willDisplayContextMenuWithConfiguration:animator:"
- "tableView:willDisplayFooterView:forSection:"
- "tableView:willDisplayHeaderView:forSection:"
- "tableView:willEndContextMenuInteractionWithConfiguration:animator:"
- "tableView:willPerformPreviewActionForMenuWithConfiguration:animator:"
- "tableView:willSelectRowAtIndexPath:"
- "tableViewDidEndMultipleSelectionInteraction:"
- "textProperties"
- "titleLabel"
- "tooManyAttemptsError"
- "topAnchor"
- "trailingAnchor"
- "traitCollection"
- "tryAgain"
- "type"
- "typeAllowingString:"
- "uiHelper"
- "unfocus"
- "unlockScreenTypeWithOutSimplePasscodeType:"
- "unsignedIntValue"
- "updateLayoutAfterPasscodeLengthChangeIfNeeded:"
- "updateLayoutAfterPasscodeTypeChangeIfNeeded"
- "updateLayoutIfNeeded"
- "useCase"
- "userCanceledError"
- "userInfo"
- "userInterfaceIdiom"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<LACContext>\"16"
- "v24@0:8@\"<LAPSPasscodeChangeUI>\"16"
- "v24@0:8@\"<LAPSPasscodeChangeUIDelegate>\"16"
- "v24@0:8@\"<LAPSPasscodeOptionsViewController>\"16"
- "v24@0:8@\"<LAPSPasscodeOptionsViewControllerDelegate>\"16"
- "v24@0:8@\"<LAPSPasscodeViewControllerDelegate>\"16"
- "v24@0:8@\"LACUIContainerViewController\"16"
- "v24@0:8@\"LARatchetViewController\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIScrollView\"16"
- "v24@0:8@\"UITableView\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"LAPSPasscode\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8B16B20"
- "v24@0:8q16"
- "v28@0:8@\"<LAPSPasscodeOptionsViewController>\"16B24"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@\"UIScrollView\"16B24"
- "v28@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"<LAPSPasscodeOptionsViewController>\"16@\"LAPSPasscodeType\"24"
- "v32@0:8@\"LAPSFetchNewPasscodeCoordinator\"16@\"LAPSPasscode\"24"
- "v32@0:8@\"LAPSFetchNewPasscodeRequest\"16@?<v@?@\"LAPSFetchNewPasscodeResult\"@\"NSError\">24"
- "v32@0:8@\"LAPSFetchOldPasscodeCoordinator\"16@\"LAPSPasscode\"24"
- "v32@0:8@\"LAPSFetchOldPasscodeRequest\"16@?<v@?@\"LAPSFetchOldPasscodeResult\"@\"NSError\">24"
- "v32@0:8@\"LAPSPasscode\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
- "v32@0:8@\"UITableView\"16@\"NSIndexPath\"24"
- "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"LAPSPasscode\"24"
- "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"LAPSPasscodeType\"24"
- "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8q16@24"
- "v36@0:8@16q24B32"
- "v40@0:8@\"<LAPSPasscodeChangeUI>\"16@\"LAPSPasscode\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"LAPSFetchNewPasscodeCoordinator\"16@\"LAPSPasscode\"24@\"LAPSPasscode\"32"
- "v40@0:8@\"LAPSFetchOldPasscodeResult\"16@\"LAPSFetchNewPasscodeResult\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"LARatchetViewController\"16@\"NSDictionary\"24@\"NSError\"32"
- "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
- "v40@0:8@\"UITableView\"16@\"NSIndexPath\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewCell\"24@\"NSIndexPath\"32"
- "v40@0:8@\"UITableView\"16@\"UITableViewFocusUpdateContext\"24@\"UIFocusAnimationCoordinator\"32"
- "v40@0:8@\"UITableView\"16@\"UIView\"24q32"
- "v40@0:8@\"UITableView\"16q24@\"NSIndexPath\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24d32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24@?32"
- "v40@0:8{CGSize=dd}16@32"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16@24q32B40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
- "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v48@0:8@\"UITableView\"16:24@\"NSIndexPath\"32@40"
- "v48@0:8@16:24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8^{__SecAccessControl=}16q24@32@40@?48"
- "v64@0:8^{__SecAccessControl=}16@24q32@40@48@?56"
- "v80@0:8@16^{__SecAccessControl=}24@32@40@48q56@64@?72"
- "verifyFixedLengthNumericPasscodeIsStrong:"
- "verifyNewPasscode:completion:"
- "verifyNewPasscodeMeetsPlatformRequirements:error:"
- "verifyNextButton"
- "verifyPasscode:"
- "verifyPasscode:completion:"
- "verifyPrompt"
- "verifyRecoveryPasscode:"
- "verifySubPrompt"
- "verifyVariableLengthAlphanumericPasscodeIsStrong:"
- "view"
- "viewControllers"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewForZoomingInScrollView:"
- "viewModel"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "widthAnchor"
- "willMoveToParentViewController:"
- "zone"
- "{CGSize=dd}16@0:8"
- "{NSDirectionalEdgeInsets=dddd}16@0:8"

```
