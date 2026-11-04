## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-625.2.8.10.6
-  __TEXT.__text: 0x39c34
-  __TEXT.__objc_methlist: 0x2230
-  __TEXT.__cstring: 0x2b27
-  __TEXT.__const: 0x874
-  __TEXT.__gcc_except_tab: 0x12cc
-  __TEXT.__oslogstring: 0x1708
+626.1.12.10.3
+  __TEXT.__text: 0x3bacc
+  __TEXT.__objc_methlist: 0x2478
+  __TEXT.__cstring: 0x2bca
+  __TEXT.__const: 0x894
+  __TEXT.__gcc_except_tab: 0x12e8
+  __TEXT.__oslogstring: 0x17c8
   __TEXT.__dlopen_cstrs: 0x203
   __TEXT.__ustring: 0x224
-  __TEXT.__swift5_typeref: 0x3fe
-  __TEXT.__constg_swiftt: 0x57c
+  __TEXT.__swift5_typeref: 0x42e
+  __TEXT.__constg_swiftt: 0x5d4
   __TEXT.__swift5_reflstr: 0x1ed
-  __TEXT.__swift5_fieldmd: 0x254
-  __TEXT.__swift5_capture: 0x338
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_fieldmd: 0x270
+  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__swift5_types: 0x30
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x100
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x19f0
+  __TEXT.__unwind_info: 0x1a98
   __TEXT.__eh_frame: 0x14b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15c0
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x15b8
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a10
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x588
-  __AUTH_CONST.__const: 0xf88
+  __AUTH_CONST.__const: 0xfd0
   __AUTH_CONST.__cfstring: 0x1f40
-  __AUTH_CONST.__objc_const: 0x3c08
+  __AUTH_CONST.__objc_const: 0x3ef8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x990
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1c8
-  __DATA.__objc_ivar: 0x1e0
-  __DATA.__data: 0x1a8
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH.__objc_data: 0x168
+  __AUTH.__data: 0x1f8
+  __DATA.__objc_ivar: 0x1f0
+  __DATA.__data: 0x1f8
   __DATA_DIRTY.__objc_data: 0xcb8
-  __DATA_DIRTY.__data: 0xa88
+  __DATA_DIRTY.__data: 0xaa0
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1511
-  Symbols:   2126
-  CStrings:  443
+  Functions: 1572
+  Symbols:   2195
+  CStrings:  448
 
Symbols:
+ +[SFAutoFillOneTimeCode _embeddedDomainArrayFromIMCoreEmbeddedDomains:]
+ +[_SFAutoFillDeliveredOneTimeCodeRecord _deliveredCodeRecordWithKind:]
+ +[_SFAutoFillDeliveredOneTimeCodeRecord supportsSecureCoding]
+ -[SFAppAutoFillOneTimeCodeProvider _localizedApplicationNameForApplicationIdentifier:]
+ -[SFAppAutoFillOneTimeCodeProvider didFocusOneTimeCodeFieldWithProvenance:maskedEmailAddress:canReportUnfocus:]
+ -[SFAppAutoFillOneTimeCodeProvider didUnfocusOneTimeCodeField]
+ -[SFAutoFillOneTimeCode _initByCopyingOneTimeCode:]
+ -[SFAutoFillOneTimeCode _localizedSubtitleDescribingSources]
+ -[SFAutoFillOneTimeCode _oneTimeCodeByMergingSourcesFromOneTimeCode:]
+ -[SFAutoFillOneTimeCode _sourceForDomainBoundValues]
+ -[SFAutoFillOneTimeCode deliveredCodeRecords]
+ -[SFAutoFillOneTimeCode initWithBulkInferenceData:appDisplayName:]
+ -[SFAutoFillOneTimeCode initWithIMCoreDictionary:appDisplayName:]
+ -[SFAutoFillOneTimeCode initWithMailOneTimeCode:timestamp:messageID:appDisplayName:]
+ -[SFAutoFillOneTimeCode initWithMessagesOneTimeCode:displayCode:displayMoneyAmount:GUID:handle:machineReadableCode:domain:domainStrictMatch:embeddedDomain:embeddedDomains:timestamp:appDisplayName:]
+ -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:displayCode:timestamp:appDisplayName:sourceAppApplicationIdentifer:notificationIdentifier:]
+ -[SFCredentialIdentity _computeDomainWithoutWWWDotLocked]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord .cxx_destruct]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord GUID]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord _fillableCode]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord applicationIdentifier]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord description]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord detectedCode]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord displayCode]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord displayMoneyAmount]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord displayName]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord domainStrictMatch]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord domain]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord embeddedDomain]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord embeddedDomains]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord encodeWithCoder:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord handle]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord hash]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord initWithCoder:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord isEqual:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord kind]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord machineReadableCode]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord messageID]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord notificationIdentifier]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setApplicationIdentifier:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDetectedCode:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDisplayCode:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDisplayMoneyAmount:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDisplayName:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDomain:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setDomainStrictMatch:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setEmbeddedDomain:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setEmbeddedDomains:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setGUID:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setHandle:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setMachineReadableCode:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setMessageID:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord setNotificationIdentifier:]
+ -[_SFAutoFillDeliveredOneTimeCodeRecord supportsDomainBoundCodes]
+ GCC_except_table19
+ GCC_except_table49
+ _EmailLibraryCore
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_CLASS_$__SFAutoFillDeliveredOneTimeCodeRecord
+ _OBJC_IVAR_$_SFAutoFillHelperProxy._connectionLock
+ _OBJC_IVAR_$_SFAutoFillOneTimeCode._deliveredCodeRecords
+ _OBJC_IVAR_$_SFAutoFillOneTimeCode._generatedCodeDomain
+ _OBJC_IVAR_$_SFCredentialIdentity._domainWithoutWWWDotLock
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._GUID
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._applicationIdentifier
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._detectedCode
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._displayCode
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._displayMoneyAmount
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._displayName
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._domain
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._domainStrictMatch
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._embeddedDomain
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._embeddedDomains
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._handle
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._kind
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._machineReadableCode
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._messageID
+ _OBJC_IVAR_$__SFAutoFillDeliveredOneTimeCodeRecord._notificationIdentifier
+ _OBJC_METACLASS_$__SFAutoFillDeliveredOneTimeCodeRecord
+ _OBJC_METACLASS_$__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ _OUTLINED_FUNCTION_5
+ __DATA__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ __INSTANCE_METHODS__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ __IVARS__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ __METACLASS_DATA__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ __OBJC_$_CLASS_METHODS__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_$_CLASS_PROP_LIST__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_$_INSTANCE_METHODS__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_$_INSTANCE_VARIABLES__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_$_PROP_LIST__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_CLASS_PROTOCOLS_$__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_CLASS_RO_$__SFAutoFillDeliveredOneTimeCodeRecord
+ __OBJC_METACLASS_RO_$__SFAutoFillDeliveredOneTimeCodeRecord
+ __PROTOCOLS__TtCFE16SafariFoundationCSo32SFAppAutoFillOneTimeCodeProviderg23deliveredCodesDidChangeGVs11AsyncStreamT__L_8Observer
+ ___111-[SFAppAutoFillOneTimeCodeProvider didFocusOneTimeCodeFieldWithProvenance:maskedEmailAddress:canReportUnfocus:]_block_invoke
+ ___60-[SFAppAutoFillOneTimeCodeProvider associatedDomainsManager]_block_invoke
+ ___64-[SFAppAutoFillOneTimeCodeProvider setAssociatedDomainsManager:]_block_invoke
+ ___block_descriptor_32_e41_v16?0"EMEnterOneTimeCodeFieldResponse"8l
+ ___getEMOneTimeCodeFieldContextClass_block_invoke
+ _getEMOneTimeCodeFieldContextClass.softClass
+ _objc_getProperty
+ _objc_setProperty_atomic
+ _symbolic So22SFFileVaultRecoveryKeyCSgSo7NSErrorCSgIeyByy_Sg
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_Sg
+ _symbolic So7NSErrorCSgIeyBy_Sg
+ _symbolic _____ So32SFAppAutoFillOneTimeCodeProviderC16SafariFoundationE23deliveredCodesDidChangeScSyytGvg8ObserverL_C
+ _symbolic _____yyt_G ScS12ContinuationV
+ _symbolic _____yyt__G ScS12ContinuationV11YieldResultO
+ _symbolic _____yyt__G ScS12ContinuationV15BufferingPolicyO
- -[SFAppAutoFillOneTimeCodeProvider test_deliverOneTimeCode:fromSource:]
- -[SFAppAutoFillOneTimeCodeProvider test_setOverrideForAppIdentifier:associatedDomainEntriess:]
- -[SFAppAutoFillOneTimeCodeProvider test_setOverrideForAppIdentifier:isWebBrowser:]
- -[SFAutoFillFeatureManager _preferredCredentialProviderForSaving]
- -[SFAutoFillFeatureManager preferredCredentialProviderForSaving]
- -[SFAutoFillFeatureManager setPreferredCredentialProviderForSaving:]
- -[SFAutoFillOneTimeCode _embeddedDomainArrayFromIMCoreEmbeddedDomains:]
- -[SFAutoFillOneTimeCode initWithBulkInferenceData:]
- -[SFAutoFillOneTimeCode initWithIMCoreDictionary:]
- -[SFAutoFillOneTimeCode initWithMailOneTimeCode:timestamp:messageID:]
- -[SFAutoFillOneTimeCode initWithNotificationOneTimeCode:displayCode:timestamp:sourceAppName:sourceAppApplicationIdentifer:notificationIdentifier:]
- GCC_except_table9
- _CFGetTypeID
- _CFPreferencesCopyAppValue
- _CFStringGetTypeID
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._GUID
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._detectedCode
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._displayCode
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._displayMoneyAmount
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._domain
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._domainStrictMatch
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._embeddedDomain
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._embeddedDomains
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._handle
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._machineReadableCode
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._messageID
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._notificationIdentifier
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._source
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._sourceAppName
- _OBJC_IVAR_$_SFAutoFillOneTimeCode._sourceApplicationIdentifier
- _WBSMailAppBundleIdentifier
- _WBSMessagesAppBundleIdentifier
- ___64-[SFAutoFillFeatureManager preferredCredentialProviderForSaving]_block_invoke
- ___71-[SFAppAutoFillOneTimeCodeProvider test_deliverOneTimeCode:fromSource:]_block_invoke
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- _fillCodeString
- _fromAppNameString
- _symbolic So22SFFileVaultRecoveryKeyCSgSo7NSErrorCSgIeyByy_
- _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
- _symbolic So7NSErrorCSgIeyBy_
CStrings:
+ "<%@: %p; kind=%ld; applicationIdentifier=\"%@\"; displayName=\"%@\"; code=\"%@\"; displayCode=\"%@\"; domain=\"%@\">"
+ "Could not fetch application record to resolve a display name for application identifier %{private}@, with error: %@"
+ "EMOneTimeCodeFieldContext"
+ "Fatal error"
+ "Mail one-time code field-enter response: accountMatchResult=%ld accountIsActive=%d"
+ "SafariFoundation/SFFileVaultRecoveryKey.swift"
+ "SafariFoundation/SFFileVaultRecoveryKeySaveRequest.swift"
+ "applicationIdentifier"
+ "deliveredCodeRecords"
+ "generatedCodeDomain"
+ "kind"
+ "messageID"
+ "notificationIdentifier"
+ "v16@?0@\"EMEnterOneTimeCodeFieldResponse\"8"
- "From Mail"
- "From Messages"
- "PreferredCredentialProviderForSaving"
- "SafariFoundation_Private.SFFileVaultRecoveryKey"
- "SafariFoundation_Private.SFFileVaultRecoveryKeySaveRequest"
- "notificationIdentifierKey"
- "source"
- "sourceAppName"
- "sourceApplicationIdentifier"
```
