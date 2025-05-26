## FinanceKit

> `/System/Library/Frameworks/FinanceKit.framework/FinanceKit`

```diff

-143.7.1.1.0
-  __TEXT.__text: 0x499734
-  __TEXT.__auth_stubs: 0x4130
-  __TEXT.__objc_methlist: 0x3724
-  __TEXT.__const: 0x2ab64
-  __TEXT.__cstring: 0x153b8
+143.7.13.0.0
+  __TEXT.__text: 0x4b90f4
+  __TEXT.__auth_stubs: 0x41a0
+  __TEXT.__objc_methlist: 0x376c
+  __TEXT.__const: 0x2bf64
+  __TEXT.__cstring: 0x15ed8
   __TEXT.__oslogstring: 0x2df
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__swift5_typeref: 0xa6e8
-  __TEXT.__swift5_reflstr: 0x780f
-  __TEXT.__swift5_assocty: 0x1a58
-  __TEXT.__constg_swiftt: 0xb31c
-  __TEXT.__swift5_fieldmd: 0xbaac
-  __TEXT.__swift5_builtin: 0x35c
-  __TEXT.__swift5_proto: 0x28b8
-  __TEXT.__swift5_types: 0xee8
-  __TEXT.__swift5_capture: 0x1ae4
-  __TEXT.__swift5_protos: 0x160
-  __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x14e20
-  __TEXT.__eh_frame: 0x1f47c
+  __TEXT.__swift5_typeref: 0xaaec
+  __TEXT.__swift5_reflstr: 0x7c5f
+  __TEXT.__swift5_assocty: 0x1b80
+  __TEXT.__constg_swiftt: 0xb650
+  __TEXT.__swift5_fieldmd: 0xbf68
+  __TEXT.__swift5_builtin: 0x384
+  __TEXT.__swift5_proto: 0x29e0
+  __TEXT.__swift5_types: 0xf40
+  __TEXT.__swift5_capture: 0x1c44
+  __TEXT.__swift5_protos: 0x164
+  __TEXT.__swift5_mpenum: 0xc8
+  __TEXT.__unwind_info: 0x155ec
+  __TEXT.__eh_frame: 0x203b4
   __TEXT.__objc_classname: 0x728
-  __TEXT.__objc_methname: 0xb4d3
-  __TEXT.__objc_methtype: 0xfba
-  __TEXT.__objc_stubs: 0xd80
-  __DATA_CONST.__got: 0x9f8
-  __DATA_CONST.__const: 0x2850
-  __DATA_CONST.__objc_classlist: 0x7d0
-  __DATA_CONST.__objc_catlist: 0x88
+  __TEXT.__objc_methname: 0xb7e4
+  __TEXT.__objc_methtype: 0xfc5
+  __TEXT.__objc_stubs: 0xd60
+  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__const: 0x28e8
+  __DATA_CONST.__objc_classlist: 0x7e0
+  __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xde68
-  __DATA_CONST.__objc_selrefs: 0x2bb0
-  __AUTH_CONST.__objc_const: 0x23c8
+  __DATA_CONST.__objc_const: 0xe0b8
+  __DATA_CONST.__objc_selrefs: 0x2c50
+  __AUTH_CONST.__objc_const: 0x2408
   __AUTH_CONST.__cfstring: 0x4e0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__const: 0x20a20
-  __AUTH_CONST.__auth_ptr: 0x958
-  __AUTH_CONST.__auth_got: 0x20a8
-  __AUTH.__objc_data: 0x6230
-  __AUTH.__data: 0x92d0
+  __AUTH_CONST.__const: 0x21978
+  __AUTH_CONST.__auth_ptr: 0x970
+  __AUTH_CONST.__auth_got: 0x20e0
+  __AUTH.__objc_data: 0x62e8
+  __AUTH.__data: 0x9600
   __DATA.__objc_protorefs: 0x138
   __DATA.__objc_classrefs: 0x4b0
   __DATA.__objc_superrefs: 0x168
-  __DATA.__objc_ivar: 0x318
+  __DATA.__objc_ivar: 0x324
   __DATA.__objc_data: 0x598
-  __DATA.__data: 0xcc30
-  __DATA.__bss: 0x4c8b0
-  __DATA.__common: 0x240
+  __DATA.__data: 0xd150
+  __DATA.__bss: 0x4ecc0
+  __DATA.__common: 0x248
   __DATA_DIRTY.__objc_data: 0x10a8
   __DATA_DIRTY.__data: 0x1748
   __DATA_DIRTY.__bss: 0x500

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 30483
-  Symbols:   8425
-  CStrings:  4203
+  Functions: 31322
+  Symbols:   8556
+  CStrings:  4290
 
Symbols:
+ -[FKAccount accountRefreshFailure]
+ -[FKAccount initWithFullyQualifiedAccountIdentifier:accountType:balance:accountBalance:creditLimit:minimumPaymentAmount:nextPaymentDate:overduePaymentAmount:actions:isAccountEnabled:isAccountMismatched:accountRefreshFailure:transactionsRefreshFailure:]
+ -[FKAccount transactionsRefreshFailure]
+ -[FKInstitution initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:backgroundRefreshEnabled:termsAndConditionsURL:]
+ -[FKInstitution supportedAuthTypes]
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ _OBJC_IVAR_$_FKAccount._accountRefreshFailure
+ _OBJC_IVAR_$_FKAccount._transactionsRefreshFailure
+ _OBJC_IVAR_$_FKInstitution._supportedAuthTypes
+ _OBJC_METACLASS_$__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ __CATEGORY__TtC10FinanceKit34ManagedInstitutionMatchingResponse_$_FinanceKit
+ __DATA__TtC10FinanceKit32InternalTransactionAsyncSequence
+ __DATA__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ __IVARS__TtC10FinanceKit32InternalTransactionAsyncSequence
+ __METACLASS_DATA__TtC10FinanceKit32InternalTransactionAsyncSequence
+ __METACLASS_DATA__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ __OBJC_$_INSTANCE_METHODS__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ __OBJC_$_INSTANCE_METHODS__TtC10FinanceKit34ManagedInstitutionMatchingResponse(FinanceKit)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FKBankConnectInstitutionsProviderDelegate
+ __PROPERTIES__TtC10FinanceKit34ManagedInstitutionMatchingResponse
+ __PROTOCOLS_XPCBankConnectAccountConnectionResult.15
+ __PROTOCOLS_XPCBankConnectAuthorizationPayload.14
+ __PROTOCOLS_XPCFullyQualifiedAccountIdentifier.12
+ __PROTOCOLS_XPCInternalAccount.19
+ _associated conformance 10FinanceKit0A12NetworkErrorO10Foundation09LocalizedD0AAs0D0
+ _associated conformance 10FinanceKit0A12NetworkErrorO10Foundation13CustomNSErrorAAs0D0
+ _associated conformance 10FinanceKit0A12NetworkErrorO4CodeOSHAASQ
+ _associated conformance 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLOSHAASQ
+ _associated conformance 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10FinanceKit18RawBankConnectDataO11InstitutionV18SupportedAuthTypesOSHAASQ
+ _associated conformance 10FinanceKit18RawBankConnectDataO11InstitutionV18SupportedAuthTypesOs12CaseIterableAA8AllCasessAHP_Sl
+ _associated conformance 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLOSHAASQ
+ _associated conformance 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyVSHAASQ
+ _associated conformance 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLOSHAASQ
+ _associated conformance 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLOs0K3KeyAAs23CustomStringConvertible
+ _associated conformance 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLOs0K3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10FinanceKit18SupportedAuthTypesVSHAASQ
+ _associated conformance 10FinanceKit18SupportedAuthTypesVs10SetAlgebraAASQ
+ _associated conformance 10FinanceKit18SupportedAuthTypesVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 10FinanceKit18SupportedAuthTypesVs9OptionSetAASY
+ _associated conformance 10FinanceKit18SupportedAuthTypesVs9OptionSetAAs0G7Algebra
+ _associated conformance 10FinanceKit19TaskQueueDescriptorOSHAASQ
+ _associated conformance 10FinanceKit25BankConnectRefreshFailureOSHAASQ
+ _associated conformance 10FinanceKit32InternalTransactionAsyncSequenceCSciAA0E8IteratorSci_ScI
+ _associated conformance 10FinanceKit39ManagedInstitutionMatchingResponseErrorOSHAASQ
+ _associated conformance 10FinanceKit40BankConnectServiceAccountConnectingErrorO10Foundation09LocalizedH0AAs0H0
+ _associated conformance 10FinanceKit40BankConnectServiceAccountConnectingErrorO10Foundation13CustomNSErrorAAs0H0
+ _associated conformance 10FinanceKit40BankConnectServiceAccountConnectingErrorO4CodeOSHAASQ
+ _associated conformance 10FinanceKit41BankConnectWebServiceRevokeConsentRequestVAA15JSONHTTPRequestAA8JSONBodyAaDP_SE
+ _associated conformance 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLOSHAASQ
+ _associated conformance 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.77
+ _block_descriptor.79
+ _block_destroy_helper.78
+ _keypath_get.14Tm
+ _keypath_get.50Tm
+ _keypath_get.60Tm
+ _keypath_get.62Tm
+ _keypath_get_selector_authTypeObjects
+ _keypath_get_selector_orderProviderDisplayName
+ _keypath_get_selector_orderProviderTrackingLogoNameDarkColorScheme
+ _keypath_get_selector_orderProviderTrackingLogoNameLightColorScheme
+ _keypath_get_selector_orderProviderURL
+ _keypath_get_selector_passSerial
+ _keypath_set.17Tm
+ _keypath_set.63Tm
+ _objectdestroy.48Tm
+ _objectdestroy.56Tm
+ _swift_getMetatypeMetadata
+ _symbolic $s10FinanceKit37PersistentHistoryTransactionProvidingP
+ _symbolic SDy__________G 10FinanceKit19TaskQueueDescriptorO AA011BankConnectcD0C
+ _symbolic SaySccy_____yxGSg______pGG 10FinanceKit7UpdatesV s5ErrorP
+ _symbolic Say_____G 10FinanceKit18RawBankConnectDataO11InstitutionV18SupportedAuthTypesO
+ _symbolic Say_____G s5Int16V
+ _symbolic Ss
+ _symbolic Ss_Sst
+ _symbolic _____ 10FinanceKit0A12NetworkErrorO4CodeO
+ _symbolic _____ 10FinanceKit16RawOrderProviderV
+ _symbolic _____ 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLO
+ _symbolic _____ 10FinanceKit18RawBankConnectDataO11InstitutionV18SupportedAuthTypesO
+ _symbolic _____ 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV
+ _symbolic _____ 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLO
+ _symbolic _____ 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV
+ _symbolic _____ 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLO
+ _symbolic _____ 10FinanceKit18SupportedAuthTypesV
+ _symbolic _____ 10FinanceKit19TaskQueueDescriptorO
+ _symbolic _____ 10FinanceKit20ManagedOrderContentsC0D8ProviderV
+ _symbolic _____ 10FinanceKit25BankConnectRefreshFailureO
+ _symbolic _____ 10FinanceKit25InternalTransactionResultV
+ _symbolic _____ 10FinanceKit32InternalTransactionAsyncSequenceC
+ _symbolic _____ 10FinanceKit32InternalTransactionAsyncSequenceC8IteratorV
+ _symbolic _____ 10FinanceKit32InternalTransactionDataExtractorV
+ _symbolic _____ 10FinanceKit34ManagedInstitutionMatchingResponseC
+ _symbolic _____ 10FinanceKit36PersistentHistoryTransactionProvider33_DFAAF0A220CBE86CB324400498351B20LLV
+ _symbolic _____ 10FinanceKit39ManagedInstitutionMatchingResponseErrorO
+ _symbolic _____ 10FinanceKit40BankConnectServiceAccountConnectingErrorO
+ _symbolic _____ 10FinanceKit40BankConnectServiceAccountConnectingErrorO4CodeO
+ _symbolic _____ 10FinanceKit5OrderV8ProviderV
+ _symbolic _____ 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLO
+ _symbolic _____ 10Foundation12DateIntervalV
+ _symbolic _____Sg 10FinanceKit16RawOrderProviderV
+ _symbolic _____Sg 10FinanceKit18RawBankConnectDataO11InstitutionV
+ _symbolic _____Sg 10FinanceKit20ManagedOrderContentsC0D8ProviderV
+ _symbolic _____Sg 10FinanceKit25BankConnectRefreshFailureO
+ _symbolic _____Sg 10FinanceKit5OrderV8ProviderV
+ _symbolic _____Sg_ABt 10FinanceKit16RawOrderProviderV
+ _symbolic _____Sg_ABt 10FinanceKit5OrderV8ProviderV
+ _symbolic ______p 10FinanceKit37PersistentHistoryTransactionProvidingP
+ _symbolic _____ySSSo6NSNullCG s18_DictionaryStorageC
+ _symbolic _____ySccy_____y_____GSg______pGG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC15InternalAccountV s5ErrorP
+ _symbolic _____ySccy_____y_____GSg______pGG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC18BankConnectConsentV s5ErrorP
+ _symbolic _____ySccy_____y_____GSg______pGG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC19InternalTransactionV s5ErrorP
+ _symbolic _____ySccy_____y_____GSg______pGG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC22InternalAccountBalanceV s5ErrorP
+ _symbolic _____ySs_SstG 17_StringProcessing5RegexV
+ _symbolic _____ySs_Sst_G 17_StringProcessing5RegexV5MatchV
+ _symbolic _____ySs_Sst_GSg 17_StringProcessing5RegexV5MatchV
+ _symbolic _____y_____G 10FinanceKit6ChangeO AA20CreditDebitIndicatorO
+ _symbolic _____y_____G 10FinanceKit7UpdatesV AA19InternalTransactionV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10FinanceKit16RawOrderProviderV10CodingKeys33_C02989D97F6BB61FD65D2355E05E253ALLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10FinanceKit18RawBankConnectDataO24RevokeConsentRequestBodyV10CodingKeys33_0AFEB7D44DF6EE09D38C1885D17E7A0ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10FinanceKit18RawBankConnectDataO34InstitutionsResponseWithExpirationV10CodingKeys33_D8221EEEC044A807CCA353F1B9385F4DLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10FinanceKit5OrderV8ProviderV10CodingKeys33_B789C2A9FB4251A1C12F4298A76ADF07LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10FinanceKit18RawBankConnectDataO11InstitutionV18SupportedAuthTypesO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int16V
+ _symbolic _____y_____GSg 10FinanceKit7UpdatesV AA19InternalTransactionV
+ _symbolic _____y__________G s18_DictionaryStorageC 10FinanceKit19TaskQueueDescriptorO AC011BankConnecteF0C
+ _symbolic _____y_______________G 10FinanceKit24EntityLongRunningFetcherC AA19InternalTransactionV AA07ManagedgH0C AA0iH0C
+ _symbolic _____y_______________G 10FinanceKit26FinancialDataAsyncSequenceC AA26ManagedInternalTransactionC AA0hI0V AA0gI0C
+ _symbolic _____y_______________GSg 10FinanceKit24EntityLongRunningFetcherC AA19InternalTransactionV AA07ManagedgH0C AA0iH0C
+ _symbolic _____y_______________GSgXw 10FinanceKit24EntityLongRunningFetcherC AA19InternalTransactionV AA07ManagedgH0C AA0iH0C
+ _symbolic _____y_______________GSgXw 10FinanceKit26FinancialDataAsyncSequenceC AA26ManagedInternalTransactionC AA0hI0V AA0gI0C
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC19InternalTransactionV
+ _symbolic _____y_____y_______________G_____G s13ManagedBufferC 10FinanceKit31FinancialDataAsyncSequenceStateV AC19InternalTransactionV AC0ajK0C AC0aK0C So16os_unfair_lock_sV
+ _symbolic y______pSgc s5ErrorP
+ _symbolic ytSg
- -[FKAccount initWithFullyQualifiedAccountIdentifier:accountType:balance:accountBalance:creditLimit:minimumPaymentAmount:nextPaymentDate:overduePaymentAmount:actions:isAccountEnabled:isAccountMismatched:]
- -[FKBankConnectInstitutionsProvider institutionsWithCompletion:]
- -[FKInstitution initWithInstitutionIdentifier:name:reconsentType:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:backgroundRefreshEnabled:termsAndConditionsURL:]
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FKBankConnectInstitutionsProviderDelegate
- __PROTOCOLS_XPCBankConnectAccountConnectionResult.10
- __PROTOCOLS_XPCBankConnectAuthorizationPayload.12
- __PROTOCOLS_XPCFullyQualifiedAccountIdentifier.11
- __PROTOCOLS_XPCInternalAccount.18
- _block_copy_helper.57
- _block_copy_helper.74
- _block_descriptor.35
- _block_descriptor.59
- _block_descriptor.76
- _block_destroy_helper.58
- _block_destroy_helper.75
- _keypath_get.49Tm
- _keypath_get.59Tm
- _keypath_set.12Tm
- _keypath_set.50Tm
- _objc_msgSend$fetchInstitutionsWithCompletion:
- _symbolic SDySS_____G 10FinanceKit20BankConnectTaskQueueC
- _symbolic SaySccy_____yxGSg_____GG 10FinanceKit7UpdatesV s5NeverO
- _symbolic SaySo13FKInstitutionCGIegg_
- _symbolic _____ySS_____G s18_DictionaryStorageC 10FinanceKit20BankConnectTaskQueueC
- _symbolic _____ySccy_____y_____GSg_____GG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC15InternalAccountV s5NeverO
- _symbolic _____ySccy_____y_____GSg_____GG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC18BankConnectConsentV s5NeverO
- _symbolic _____ySccy_____y_____GSg_____GG s23_ContiguousArrayStorageC 10FinanceKit7UpdatesV AC22InternalAccountBalanceV s5NeverO
CStrings:
+ "@112@0:8@16Q24@32@40@48@56@64@72@80B88B92Q96Q104"
+ "@88@0:8@16@24Q32s40@44d52d60@68B76@80"
+ "APP_EXTENSION"
+ "Authentication Invalid"
+ "BankConnectRefreshFailure.tooManyRequests"
+ "BankConnectRefreshFailure.unspecifiedError"
+ "Cleaned up transactions in non-terminal state for account: %s dateInterval: %s"
+ "Clearing lastAccountRefreshFailure"
+ "Clearing lastAccountTransactionsFailure"
+ "Complete auth failed with underlying error: "
+ "Connect account failed with underlying error: "
+ "Data invalid with underlying error: "
+ "Deleting all balances because of an exception"
+ "Failed to cleanup transactions in non-terminal state for account: %s error: %@"
+ "Failed to fetch the oldest non-terminal transaction for account: %s dateQuery: %s error: %@"
+ "Failed to load transaction page %@. Merged similar BC and CNS transations."
+ "Failed to match an account. Multiple accounts matched."
+ "Failed to match an account. No accounts matched."
+ "FinancialDataAsyncSequence is nil while terminating"
+ "Finished post-processing transactions. Missing transactions are cleaned up, similar BankConnect and PassKit transactions are linked."
+ "Institution:\tNo matched institution\n"
+ "Invalid raw value: "
+ "No BankConnect endpoint set, using default: %s"
+ "OAUTH_APP"
+ "OAUTH_WEB"
+ "Request creation failed with underlying error: "
+ "Request failed with underlying error: "
+ "Response invalid was expecting: "
+ "Setting lastAccountRefreshFailure to: %s for error: %@"
+ "Setting lastTransactionsRefreshFailure to: %s for error: %@"
+ "Skip transactions cleanup. Non-terminal transactions aren't fully loaded. oldestTransactionDate: %s, dateInterval: %s"
+ "Skip transactions cleanup. dateInterval is nil."
+ "Skip transactions cleanup. oldestTransaction is nil."
+ "Skip transactions cleanup. seenTransactionIDs is empty."
+ "TQ,R,N,V_accountRefreshFailure"
+ "TQ,R,N,V_transactionsRefreshFailure"
+ "Too many requests, retry after: "
+ "Ts,R,N,V_supportedAuthTypes"
+ "Unable to obtain institutions from ManagedInstitutionMatchingResponse: %@"
+ "Unable to set account refresh failure for account: %s to: %s error: %@"
+ "Unable to set transactions refresh failure for account: %s to: %s error: %@"
+ "Unexpected response status code: "
+ "Using BankConnect endpoint: %s"
+ "_TtC10FinanceKit32InternalTransactionAsyncSequence"
+ "_TtC10FinanceKit34ManagedInstitutionMatchingResponse"
+ "_accountRefreshFailure"
+ "_supportedAuthTypes"
+ "_transactionsRefreshFailure"
+ "accountRefreshFailure"
+ "authTypeObjects"
+ "com.finance.BankConnectServiceAccountConnectingError"
+ "com.finance.FinanceNetworkError"
+ "expiration"
+ "expiration <= %@"
+ "initWithFullyQualifiedAccountIdentifier:accountType:balance:accountBalance:creditLimit:minimumPaymentAmount:nextPaymentDate:overduePaymentAmount:actions:isAccountEnabled:isAccountMismatched:accountRefreshFailure:transactionsRefreshFailure:"
+ "initWithInstitutionIdentifier:name:reconsentType:supportedAuthTypes:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:backgroundRefreshEnabled:termsAndConditionsURL:"
+ "institutionsResponse"
+ "institutionsResponseData"
+ "lastAccountRefreshFailureValue"
+ "lastTransactionsRefreshFailureValue"
+ "orderProvider"
+ "orderProviderDisplayName"
+ "orderProviderTrackingLogoNameDarkColorScheme"
+ "orderProviderTrackingLogoNameLightColorScheme"
+ "orderProviderURL"
+ "passSerial"
+ "passSerial == %@"
+ "passSerial == %@ AND expiration > %@"
+ "persistentHistoryTransactionProvider"
+ "publicTransactionObject IN %@"
+ "publicTransactionObject.statusValue IN %@"
+ "setAuthTypeObjects:"
+ "setExpiration:"
+ "setInstitutionsResponseData:"
+ "setLastAccountRefreshFailureValue:"
+ "setLastTransactionsRefreshFailureValue:"
+ "setOrderProviderDisplayName:"
+ "setOrderProviderTrackingLogoNameDarkColorScheme:"
+ "setOrderProviderTrackingLogoNameLightColorScheme:"
+ "setOrderProviderURL:"
+ "setPassSerial:"
+ "supportedAuthTypes"
+ "terminate"
+ "trackingLogoNameDarkColorScheme"
+ "trackingLogoNameLightColorScheme"
+ "transactionsRefreshFailure"
+ "v32@0:8@\"XPCInstitution\"16@?<v@?@\"NSArray\">24"
- "$__lazy_storage_$_fetchedAccountId"
- "@84@0:8@16@24Q32@40d48d56@64B72@76"
- "@96@0:8@16Q24@32@40@48@56@64@72@80B88B92"
- "Cannot perform initial fetch: %@"
- "FinanceKit/FinancialDataAsyncSequence.swift"
- "Finished post-processing transactions. Missing transactions are cleaned up,\nsimilar BankConnect and PassKit transactions are linked."
- "No Boskoop endpoint set, using default: %s"
- "Using Boskoop endpoint: %s"
- "fetchInstitutionsWithCompletion:"
- "initWithFullyQualifiedAccountIdentifier:accountType:balance:accountBalance:creditLimit:minimumPaymentAmount:nextPaymentDate:overduePaymentAmount:actions:isAccountEnabled:isAccountMismatched:"
- "initWithInstitutionIdentifier:name:reconsentType:firstTransactionsRequestWindow:maxAgeTransactionsFirstRequest:maxAgeTransactionsRefreshRequest:extensionsBundleIdentifiers:backgroundRefreshEnabled:termsAndConditionsURL:"
- "institutionsDidChange:"
- "institutionsWithCompletion:"
- "v32@0:8@\"XPCInstitution\"16@?<v@?@\"NSArray\"@\"NSError\">24"

```
