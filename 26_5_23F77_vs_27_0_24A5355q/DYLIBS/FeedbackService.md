## FeedbackService

> `/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService`

```diff

-208.3.0.0.0
-  __TEXT.__text: 0x8fadc
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x1364
-  __TEXT.__const: 0xc080
-  __TEXT.__cstring: 0x28f8
+227.0.0.0.0
+  __TEXT.__text: 0x96ee0
+  __TEXT.__objc_methlist: 0x1420
+  __TEXT.__const: 0xcb24
+  __TEXT.__oslogstring: 0x1376
+  __TEXT.__cstring: 0x2bd2
   __TEXT.__ustring: 0xd8
-  __TEXT.__oslogstring: 0x10bf
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__constg_swiftt: 0x23d4
-  __TEXT.__swift5_typeref: 0x28da
-  __TEXT.__swift5_fieldmd: 0x2594
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_types: 0x350
-  __TEXT.__swift5_reflstr: 0x1291
-  __TEXT.__swift5_proto: 0xacc
-  __TEXT.__swift5_capture: 0x58c
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x84
+  __TEXT.__gcc_except_tab: 0xb8
+  __TEXT.__swift5_typeref: 0x2b17
+  __TEXT.__constg_swiftt: 0x25a4
+  __TEXT.__swift5_reflstr: 0x1382
+  __TEXT.__swift5_fieldmd: 0x2790
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_mpenum: 0x44
+  __TEXT.__swift5_proto: 0xb5c
+  __TEXT.__swift5_types: 0x380
+  __TEXT.__swift5_capture: 0x5dc
+  __TEXT.__swift_as_entry: 0x98
+  __TEXT.__swift_as_ret: 0x94
+  __TEXT.__swift_as_cont: 0x148
+  __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_mpenum: 0x3c
-  __TEXT.__unwind_info: 0x2670
-  __TEXT.__eh_frame: 0x26b8
-  __TEXT.__objc_classname: 0x6f7
-  __TEXT.__objc_methname: 0x346a
-  __TEXT.__objc_methtype: 0xf45
-  __TEXT.__objc_stubs: 0x1ee0
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__objc_classlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__unwind_info: 0x2738
+  __TEXT.__eh_frame: 0x2958
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb70
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0xbe8
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xab0
-  __AUTH_CONST.__const: 0x5a90
-  __AUTH_CONST.__cfstring: 0xe00
-  __AUTH_CONST.__objc_const: 0x2dc8
-  __AUTH.__objc_data: 0x1218
-  __AUTH.__data: 0x538
-  __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0x1478
+  __DATA_CONST.__got: 0x438
+  __AUTH_CONST.__const: 0x61c9
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0x2fe0
+  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH.__objc_data: 0x13a0
+  __AUTH.__data: 0x588
+  __DATA.__objc_ivar: 0x120
+  __DATA.__data: 0x15f8
+  __DATA.__bss: 0xb610
   __DATA.__common: 0x88
-  __DATA.__bss: 0xa5b0
-  __DATA_DIRTY.__objc_data: 0x8d0
-  __DATA_DIRTY.__data: 0x12c8
+  __DATA_DIRTY.__objc_data: 0x920
+  __DATA_DIRTY.__data: 0x1300
+  __DATA_DIRTY.__bss: 0xb620
   __DATA_DIRTY.__common: 0x88
-  __DATA_DIRTY.__bss: 0xb480
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
-  - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7E023967-23B9-3831-9308-681CEADF8DC9
-  Functions: 3724
-  Symbols:   2847
-  CStrings:  1257
+  UUID: 615A7472-E6DF-3B19-B7CF-F432064EE18D
+  Functions: 3906
+  Symbols:   3187
+  CStrings:  581
 
Symbols:
+ +[FBKSDeviceRegion currentDeviceRegionHeaderValue]
+ -[FBKSAnnotatedContentObjc _issueSandboxExtensionForURL:]
+ -[FBKSAnnotatedContentObjc _issueSandboxExtensionForURL:].cold.1
+ -[FBKSAnnotatedContentObjc _issueSandboxExtensionForURL:].cold.2
+ -[FBKSAnnotatedContentObjc initWithPayloadURL:displayName:description:fileName:iconType:additionalInfo:]
+ -[FBKSAnnotatedContentObjc payloadURL]
+ -[FBKSAnnotatedContentObjc sandboxToken]
+ -[FBKSAnnotatedContentObjc setPayloadURL:]
+ -[FBKSAnnotatedContentObjc setSandboxToken:]
+ _APP_SANDBOX_READ
+ _OBJC_CLASS_$_FBKSDeviceRegion
+ _OBJC_CLASS_$_RDEstimate
+ _OBJC_CLASS_$__TtC15FeedbackService29FeedbackFilingDaemonInterface
+ _OBJC_CLASS_$__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ _OBJC_IVAR_$_FBKSAnnotatedContentObjc._payloadURL
+ _OBJC_IVAR_$_FBKSAnnotatedContentObjc._sandboxToken
+ _OBJC_METACLASS_$_FBKSDeviceRegion
+ _OBJC_METACLASS_$__TtC15FeedbackService29FeedbackFilingDaemonInterface
+ _OBJC_METACLASS_$__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ _SANDBOX_EXTENSION_DEFAULT
+ __DATA__TtC15FeedbackService29FeedbackFilingDaemonInterface
+ __DATA__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ __INSTANCE_METHODS__TtC15FeedbackService29FeedbackFilingDaemonInterface
+ __INSTANCE_METHODS__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ __IVARS__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ __METACLASS_DATA__TtC15FeedbackService29FeedbackFilingDaemonInterface
+ __METACLASS_DATA__TtC15FeedbackService30FeedbackFilingDaemonConnection
+ __OBJC_$_CLASS_METHODS_FBKSDeviceRegion
+ __OBJC_CLASS_RO_$_FBKSDeviceRegion
+ __OBJC_METACLASS_RO_$_FBKSDeviceRegion
+ __PROTOCOL_INSTANCE_METHODS__TtP15FeedbackService28FeedbackFilingDaemonProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP15FeedbackService28FeedbackFilingDaemonProtocol_
+ __PROTOCOL__TtP15FeedbackService28FeedbackFilingDaemonProtocol_
+ ___50-[FBKSHTTPClient jsonForURLRequest:success:error:]_block_invoke.56
+ ___62-[FBKSHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.73
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.105
+ ___swift_closure_destructor.108
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.114
+ ___swift_closure_destructor.118
+ ___swift_closure_destructor.11Tm
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.121
+ ___swift_closure_destructor.12Tm
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.15
+ ___swift_closure_destructor.15Tm
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.18Tm
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.33
+ ___swift_closure_destructor.333
+ ___swift_closure_destructor.336
+ ___swift_closure_destructor.340
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.4
+ ___swift_closure_destructor.40
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.53
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.67
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.70
+ ___swift_closure_destructor.73
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.79
+ ___swift_closure_destructor.7Tm
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.82
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.88
+ ___swift_closure_destructor.8Tm
+ ___swift_closure_destructor.9
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.92
+ ___swift_closure_destructor.93
+ ___swift_closure_destructor.95
+ ___swift_closure_destructor.97
+ ___swift_closure_destructorTm
+ __swift_implicitisolationactor_to_executor_cast
+ _associated conformance 15FeedbackService15FBKSInteractionC13FeatureDomainO31SafariTabOrganizationCodingKeys33_417385B848639E587EC54297A34836BDLLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService15FBKSInteractionC13FeatureDomainO31SafariTabOrganizationCodingKeys33_417385B848639E587EC54297A34836BDLLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOSHAASQ
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOSHAASQ
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19CancelledCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19CancelledCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOSHAASQ
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOSHAASQ
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOSHAASQ
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.100
+ _block_copy_helper.110
+ _block_copy_helper.123
+ _block_copy_helper.20
+ _block_copy_helper.26
+ _block_copy_helper.32
+ _block_copy_helper.343
+ _block_copy_helper.35
+ _block_copy_helper.38
+ _block_copy_helper.57
+ _block_copy_helper.66
+ _block_copy_helper.72
+ _block_copy_helper.75
+ _block_copy_helper.84
+ _block_copy_helper.97
+ _block_descriptor.102
+ _block_descriptor.112
+ _block_descriptor.125
+ _block_descriptor.22
+ _block_descriptor.28
+ _block_descriptor.34
+ _block_descriptor.345
+ _block_descriptor.37
+ _block_descriptor.40
+ _block_descriptor.59
+ _block_descriptor.68
+ _block_descriptor.74
+ _block_descriptor.77
+ _block_descriptor.86
+ _block_descriptor.99
+ _block_destroy_helper.101
+ _block_destroy_helper.111
+ _block_destroy_helper.124
+ _block_destroy_helper.21
+ _block_destroy_helper.27
+ _block_destroy_helper.33
+ _block_destroy_helper.344
+ _block_destroy_helper.36
+ _block_destroy_helper.39
+ _block_destroy_helper.58
+ _block_destroy_helper.67
+ _block_destroy_helper.73
+ _block_destroy_helper.76
+ _block_destroy_helper.85
+ _block_destroy_helper.98
+ _flat unique 15FeedbackService0A20FilingDaemonProtocol_p
+ _free
+ _get_enum_tag_for_layout_string 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO
+ _keypath_get.24Tm
+ _keypath_get.26Tm
+ _keypath_get.36Tm
+ _keypath_get.42Tm
+ _keypath_set.43Tm
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_issueSandboxExtensionForURL:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$countryCode
+ _objc_msgSend$currentDeviceRegionHeaderValue
+ _objc_msgSend$currentEstimates
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$lastKnownEstimates
+ _objc_msgSend$launchFormInRemoteViewWithFormData:completion:
+ _objc_msgSend$payloadURL
+ _objc_msgSend$sandboxToken
+ _objc_msgSend$stringWithUTF8String:
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _sandbox_extension_issue_file
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_coroFrameAlloc
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_willThrowTypedImpl
+ _symbolic $s15FeedbackService0A20FilingDaemonProtocolP
+ _symbolic SS10responseID_t
+ _symbolic SS16errorDescription_t
+ _symbolic SS_SSt
+ _symbolic ScCy_____Sg______pG 15FeedbackService24FBKSFeedbackFilingResultV s5ErrorP
+ _symbolic SiSg
+ _symbolic _____ 15FeedbackService0A21FilingDaemonInterfaceC
+ _symbolic _____ 15FeedbackService0A22FilingDaemonConnectionC
+ _symbolic _____ 15FeedbackService15FBKSInteractionC13FeatureDomainO31SafariTabOrganizationCodingKeys33_417385B848639E587EC54297A34836BDLLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19CancelledCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____ 15FeedbackService7StringsV3XPCV0A6FilingV
+ _symbolic _____Sg 15FeedbackService24FBKSFeedbackFilingResultV
+ _symbolic ______p 15FeedbackService0A20FilingDaemonProtocolP
+ _symbolic _____ySSSay_____GG s18_DictionaryStorageC 15FeedbackService15FBKSInteractionC16AnnotatedContentV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService15FBKSInteractionC13FeatureDomainO31SafariTabOrganizationCodingKeys33_417385B848639E587EC54297A34836BDLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19CancelledCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService15FBKSInteractionC13FeatureDomainO31SafariTabOrganizationCodingKeys33_417385B848639E587EC54297A34836BDLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO10CodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19CancelledCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO19SubmittedCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO23FailedToStartCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO24FailedToSubmitCodingKeys33_5FA4E9C34884DA8872F80DBA566899E2LLO
+ _symbolic _____y_____SgG s23_ContiguousArrayStorageC 15FeedbackService15FBKSInteractionC16AnnotatedContentV
+ _symbolic yp3key_yp5valuet
+ _symbolic yp3key_yp5valuetSg
+ _type_layout_string 15FeedbackService24FBKSFeedbackFilingResultV
+ _type_layout_string 15FeedbackService24FBKSFeedbackFilingResultV7OutcomeO
- GCC_except_table27
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___50-[FBKSHTTPClient jsonForURLRequest:success:error:]_block_invoke.52
- ___62-[FBKSHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.69
- _associated conformance So18FBKSPendingConsentC7Combine16ObservableObject15FeedbackService0E19WillChangePublisherAcDP_AC0J0
- _associated conformance So18FBKSPendingConsentCs12Identifiable15FeedbackService2IDsACP_SH
- _block_copy_helper.102
- _block_copy_helper.103
- _block_copy_helper.115
- _block_copy_helper.127
- _block_copy_helper.18
- _block_copy_helper.25
- _block_copy_helper.30
- _block_copy_helper.338
- _block_copy_helper.34
- _block_copy_helper.36
- _block_copy_helper.42
- _block_copy_helper.53
- _block_copy_helper.62
- _block_copy_helper.73
- _block_copy_helper.74
- _block_copy_helper.88
- _block_descriptor.104
- _block_descriptor.105
- _block_descriptor.117
- _block_descriptor.129
- _block_descriptor.20
- _block_descriptor.27
- _block_descriptor.32
- _block_descriptor.340
- _block_descriptor.36
- _block_descriptor.38
- _block_descriptor.44
- _block_descriptor.55
- _block_descriptor.64
- _block_descriptor.75
- _block_descriptor.76
- _block_descriptor.90
- _block_destroy_helper.103
- _block_destroy_helper.104
- _block_destroy_helper.116
- _block_destroy_helper.128
- _block_destroy_helper.19
- _block_destroy_helper.26
- _block_destroy_helper.31
- _block_destroy_helper.339
- _block_destroy_helper.35
- _block_destroy_helper.37
- _block_destroy_helper.43
- _block_destroy_helper.54
- _block_destroy_helper.63
- _block_destroy_helper.74
- _block_destroy_helper.75
- _block_destroy_helper.89
- _keypath_get.20Tm
- _keypath_get.22Tm
- _keypath_get.32Tm
- _keypath_get.38Tm
- _keypath_set.39Tm
- _objc_msgSend$ID
- _objectdestroy.10Tm
- _objectdestroy.22Tm
- _objectdestroy.342Tm
- _objectdestroy.3Tm
- _objectdestroy.42Tm
- _objectdestroy.77Tm
- _objectdestroy.8Tm
- _objectdestroyTm
- _swift_release_n
- _symbolic $s7Combine16ObservableObjectP
- _symbolic $ss12IdentifiableP
- _symbolic So18FBKSPendingConsentC
- _symbolic _____ 7Combine25ObservableObjectPublisherC
- _symbolic ypSg
CStrings:
+ "%s: Setting up connection to feedback filing daemon"
+ ","
+ "-[FBKSAnnotatedContentObjc initWithPayload:displayName:description:fileName:iconType:additionalInfo:]"
+ "-[FBKSAnnotatedContentObjc initWithPayloadURL:displayName:description:fileName:iconType:additionalInfo:]"
+ "Cannot get file system representation for URL: %{public}@"
+ "Connection to feedback filing daemon interrupted"
+ "Connection to feedback filing daemon invalidated"
+ "FBKSFeedbackFilingResult("
+ "FBKSInteraction: contentRole [%{public}s] is shared by %ld AnnotatedContent values [%{public}s]. contentRole must be unique within a report; relatedFile lookups will be ambiguous."
+ "Failed to connect to feedback filing daemon"
+ "Failed to connect to feedback filing daemon: %s"
+ "Failed to decode FBKSFeedbackFilingResult: %s"
+ "Failed to issue sandbox extension for URL: %{private}@"
+ "Failed to obtain remote object proxy for daemon"
+ "Failed to obtain remote object proxy for feedback filing daemon"
+ "Failed to start: "
+ "Failed to submit: "
+ "Submitted (responseID: "
+ "Tab Organization"
+ "Using device region: [%{public}@]"
+ "X-B3-TraceId"
+ "X-Device-Region"
+ "[%{public}s"
+ "annotateURL(inURL:displayName:description:contentRole:group:iconType:additionalInfo:displayOrder:)"
+ "com.apple.feedbackd.remote-feedback"
+ "contentRole"
+ "displayOrder"
+ "launchInRemoteView()"
+ "safariTabOrganization"
+ "sandboxToken"
- "#16@0:8"
- "$__lazy_storage_$_connectionForAdmin"
- "$__lazy_storage_$_dataSizeFormatter"
- "$__lazy_storage_$_xpcConnection"
- "$defaultActor"
- ".cxx_destruct"
- "?"
- "@\"<FBKSHTTPClientProtocol>\""
- "@\"FBKSAnnotatedContentObjc\""
- "@\"FBKSCampaign\""
- "@\"FBKSCampaignError_FrameworkPrivateName\""
- "@\"FBKSCampaign_FrameworkPrivateName\""
- "@\"FBKSCustomBehavior\""
- "@\"FBKSDraftLauncher\""
- "@\"FBKSDraftLauncher_FrameworkPrivateName\""
- "@\"FBKSFeedbackCount_FrameworkPrivateName\""
- "@\"FBKSFeedback_FrameworkPrivateName\""
- "@\"FBKSForm_FrameworkPrivateName\""
- "@\"FBKSLaunchConfiguration_FrameworkPrivateName\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSHTTPCookie\""
- "@\"NSHTTPCookie\"16@0:8"
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURLSession\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@28@0:8@16s24"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32q40"
- "@64@0:8@16@24@32@40@48@56"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Donation is not supported on FCS"
- "FBKSAnalytics"
- "FBKSAnnotatedContentObjc"
- "FBKSCampaign"
- "FBKSCampaignError"
- "FBKSCampaignError_FrameworkPrivateName"
- "FBKSCampaign_FrameworkPrivateName"
- "FBKSCustomBehavior"
- "FBKSDeviceToken"
- "FBKSDraftLauncher"
- "FBKSDraftLauncher_FrameworkPrivateName"
- "FBKSFeedback"
- "FBKSFeedbackCount"
- "FBKSFeedbackCount_FrameworkPrivateName"
- "FBKSFeedback_FrameworkPrivateName"
- "FBKSForm"
- "FBKSForm_FrameworkPrivateName"
- "FBKSHTTPClient"
- "FBKSHTTPClientProtocol"
- "FBKSInteractionObjc"
- "FBKSLaunchConfiguration"
- "FBKSLaunchConfiguration_FrameworkPrivateName"
- "FBKSPendingConsent"
- "FBKSSeedPortalAPI"
- "FBKSSharedConstants"
- "FBKSUserLoginInfo"
- "Failed to access data in URL "
- "FeedbackService"
- "FeedbackServiceBundleIdentifier"
- "HTTPAdditionalHeaders"
- "HTTPMethod"
- "ID"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "NSURLSessionDataDelegate"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<FBKSHTTPClientProtocol>\",&,N,V_coreHTTPClient"
- "T@\"FBKSAnnotatedContentObjc\",&,N,V_generatedAnnotatedContent"
- "T@\"FBKSAnnotatedContentObjc\",&,N,V_originalAnnotatedContent"
- "T@\"FBKSCampaign\",R,N,V_currentCampaign"
- "T@\"FBKSCampaignError_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSCampaign_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSCampaign_FrameworkPrivateName\",N,R,VcurrentCampaign"
- "T@\"FBKSCustomBehavior\",&,N,V_behavior"
- "T@\"FBKSDraftLauncher\",R,N,V_form"
- "T@\"FBKSDraftLauncher_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSFeedbackCount_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSFeedback_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSForm_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"FBKSForm_FrameworkPrivateName\",N,&,Vform"
- "T@\"FBKSLaunchConfiguration_FrameworkPrivateName\",&,N,V_swiftObject"
- "T@\"NSArray\",&,N,V_extraContent"
- "T@\"NSArray\",&,N,V_pendingConsents"
- "T@\"NSArray\",&,N,V_signedConsents"
- "T@\"NSArray\",N,R"
- "T@\"NSArray\",R,N,V_errors"
- "T@\"NSArray\",R,N,V_feedbackFiled"
- "T@\"NSData\",&,N,V_payload"
- "T@\"NSData\",N,R"
- "T@\"NSDate\",N,R"
- "T@\"NSDate\",R,N"
- "T@\"NSDictionary\",&,N,V_additionalInfo"
- "T@\"NSDictionary\",&,N,V_answers"
- "T@\"NSDictionary\",&,N,V_prefillQuestions"
- "T@\"NSHTTPCookie\",&,V_seedPortalSession"
- "T@\"NSHTTPCookie\",?,R"
- "T@\"NSHTTPCookie\",R"
- "T@\"NSNumber\",&,N,V_formId"
- "T@\"NSNumber\",&,N,V_participantID"
- "T@\"NSNumber\",R,N,V_ID"
- "T@\"NSString\",&,N,V__description"
- "T@\"NSString\",&,N,V_deviceToken"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSString\",&,N,V_familyName"
- "T@\"NSString\",&,N,V_fileName"
- "T@\"NSString\",&,N,V_givenName"
- "T@\"NSString\",&,N,V_iconType"
- "T@\"NSString\",&,N,V_username"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_attributionBundleId"
- "T@\"NSString\",C,N,V_featureDomain"
- "T@\"NSString\",C,N,V_feedbackTitle"
- "T@\"NSString\",C,N,V_localizedAlertViewDeclineButtonTitle"
- "T@\"NSString\",C,N,V_localizedAlertViewProceedButtonTitle"
- "T@\"NSString\",C,N,V_localizedPromptMessage"
- "T@\"NSString\",C,N,V_localizedPromptTitle"
- "T@\"NSString\",C,N,V_modelVersion"
- "T@\"NSString\",C,N,V_presentingBundleId"
- "T@\"NSString\",C,N,V_sceneId"
- "T@\"NSString\",N,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_agreeButtonText"
- "T@\"NSString\",R,N,V_bodyText"
- "T@\"NSString\",R,N,V_declineButtonText"
- "T@\"NSString\",R,N,V_symbolImageName"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSURL\",&,N,V_feedbackURL"
- "T@\"NSURL\",&,N,V_seedPortalURL"
- "T@\"NSURL\",R,N,V_learnMoreURL"
- "T@\"NSURLSession\",&,V_session"
- "T@\"NSUserDefaults\",R,N"
- "T@,R,N"
- "TB,N,V_alwaysUseRemoteAlertController"
- "TB,N,V_isAppleConnectLogin"
- "TB,N,V_isCaptive"
- "TB,N,V_isPIPLConsent"
- "TB,N,V_isSystemAccount"
- "TB,N,V_launchNewDraft"
- "TB,N,V_makeVisible"
- "TB,N,V_notifyImmediately"
- "TB,N,V_notifyOnUpload"
- "TB,N,V_skipsPrompt"
- "TB,R,N,V_isRequired"
- "TQ,R"
- "TQ,R,N,V_type"
- "Tq,N,R,Vcode"
- "Tq,N,R,VdeclineCount"
- "Tq,N,R,Vid"
- "Tq,N,R,Vstate"
- "Tq,N,V_ID"
- "Tq,N,V_authenticationMethod"
- "Tq,N,V_promptStyle"
- "Tq,N,VauthenticationMethod"
- "Tq,N,VpromptStyle"
- "Tq,R,N"
- "Tq,R,N,V_declineCount"
- "Ts,N,V_environment"
- "URL"
- "URLByAppendingPathComponent:"
- "URLQueryAllowedCharacterSet"
- "URLSession:dataTask:didBecomeDownloadTask:"
- "URLSession:dataTask:didBecomeStreamTask:"
- "URLSession:dataTask:didReceiveData:"
- "URLSession:dataTask:didReceiveResponse:completionHandler:"
- "URLSession:dataTask:willCacheResponse:completionHandler:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "X-Request-Id"
- "^{_NSZone=}16@0:8"
- "_ID"
- "_TtC15FeedbackService10SeedPortal"
- "_TtC15FeedbackService11FBKSStrings"
- "_TtC15FeedbackService12FBKSDonation"
- "_TtC15FeedbackService13FBKSSInboxTat"
- "_TtC15FeedbackService14FBKSEvaluation"
- "_TtC15FeedbackService15FBKSInteraction"
- "_TtC15FeedbackService16DaemonConnection"
- "_TtC15FeedbackService19CFBDaemonConnection"
- "_TtC15FeedbackService21DaemonAdminConnection"
- "_TtC15FeedbackService21FBKSSharedPersistence"
- "_TtC15FeedbackService23FeedbackDaemonInterface"
- "_TtC15FeedbackService24ReportAConcernObjCBridge"
- "_TtC15FeedbackService28FeedbackDaemonAdminInterface"
- "_TtC15FeedbackService34CentralizedFeedbackDaemonInterface"
- "_TtC15FeedbackServiceP33_DB1E4EC7AE64AA60E6746FC6257A195C12AClassInFBKS"
- "_TtP15FeedbackService22FeedbackDaemonProtocol_"
- "_TtP15FeedbackService27FeedbackDaemonAdminProtocol_"
- "_TtP15FeedbackService33CentralizedFeedbackDaemonProtocol_"
- "_TtP15FeedbackService33RemoteViewControllerReplyProtocol_"
- "__description"
- "_additionalInfo"
- "_agreeButtonText"
- "_alwaysUseRemoteAlertController"
- "_answers"
- "_attributionBundleId"
- "_authenticationMethod"
- "_basicParameterWithoutLabel"
- "_basicParametersForWriting"
- "_behavior"
- "_bodyText"
- "_bundleID"
- "_coreHTTPClient"
- "_currentCampaign"
- "_declineButtonText"
- "_declineCount"
- "_deriveSystemVersion"
- "_description"
- "_deviceToken"
- "_displayName"
- "_environment"
- "_errors"
- "_evaluationID"
- "_extraContent"
- "_familyName"
- "_featureDomain"
- "_feedbackFiled"
- "_feedbackTitle"
- "_feedbackURL"
- "_fileName"
- "_filterForValue"
- "_form"
- "_formId"
- "_generatedAnnotatedContent"
- "_givenName"
- "_iconType"
- "_isAppleConnectLogin"
- "_isCaptive"
- "_isPIPLConsent"
- "_isRequired"
- "_isSystemAccount"
- "_launchNewDraft"
- "_learnMoreURL"
- "_localizedAlertViewDeclineButtonTitle"
- "_localizedAlertViewProceedButtonTitle"
- "_localizedPromptMessage"
- "_localizedPromptTitle"
- "_makeVisible"
- "_modelVersion"
- "_notifyImmediately"
- "_notifyOnUpload"
- "_originalAnnotatedContent"
- "_participantID"
- "_payload"
- "_pendingConsents"
- "_prefillQuestions"
- "_presentingBundleId"
- "_promptStyle"
- "_queryForParticipantID:isForWriting:"
- "_sceneId"
- "_seedPortalSession"
- "_seedPortalURL"
- "_session"
- "_signedConsents"
- "_skipsPrompt"
- "_swiftObject"
- "_symbolImageName"
- "_title"
- "_type"
- "_username"
- "action"
- "addEntriesFromDictionary:"
- "addObject:"
- "addSuiteNamed:"
- "agreeButtonText"
- "allHTTPHeaderFields"
- "allHeaderFields"
- "alwaysUseRemoteAlertController"
- "annotateURL(inURL:displayName:description:group:iconType:additionalInfo:)"
- "appendFormat:"
- "appleSeedURL"
- "appleSeedURLFromDefaults:withEnvironment:"
- "arrayForKey:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "asFBAURLSchemeWithIsSurvey:"
- "asJSON"
- "attributionBundleId"
- "autorelease"
- "bodyText"
- "boolForKey:"
- "boolValue"
- "build"
- "bundleForClass:"
- "bundleIdentifier"
- "cStringUsingEncoding:"
- "characterAtIndex:"
- "class"
- "clearAllDeviceTokens"
- "clearCachedUserSessionWithCompletion:"
- "clearDeviceTokenForParticipantID:"
- "client"
- "collectFeedbackWithFormData:launchConfigurationData:completion:"
- "collectFeedbackWithLaunchConfiguration:completion:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "configuration"
- "conformsToProtocol:"
- "consentTypeString"
- "containsObject:"
- "containsString:"
- "cookiesWithResponseHeaderFields:forURL:"
- "copy"
- "coreHTTPClient"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "credentialForTrust:"
- "currentCampaign"
- "dataForURL:success:error:"
- "dataForURLRequest:success:error:"
- "dataForURLRequest:successWithResponse:error:"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateAdded"
- "dealloc"
- "debugDescription"
- "declineButtonText"
- "declineCount"
- "defaultSessionConfiguration"
- "deleteDonationWithDonationID:completion:"
- "deviceToken"
- "diagnostics"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didFinishSubmissionWithFormIdentifier:feedbackId:isSurvey:error:completion:"
- "domain"
- "donateWithDonationJSON:donationID:completion:"
- "errorWithDomain:code:userInfo:"
- "evaluateWithAction:showFeedbackForm:associateWithAppleAccount:completion:"
- "evaluateWithAction:showFeedbackForm:associateWithAppleAccount:completionWithResult:"
- "evaluateWithInteraction:action:showFeedbackForm:associateWithAppleAccount:sceneID:presentingBundleId:completion:"
- "evaluateWithInteraction:action:showFeedbackForm:associateWithAppleAccount:sceneID:presentingBundleId:completionWithResult:"
- "exceptionWithName:reason:userInfo:"
- "expiresDate"
- "extraContent"
- "familyName"
- "featureDomain"
- "feedbackFiled"
- "feedbackTitle"
- "feedbackURL"
- "fetchCountsForFormWithIdentifier:completion:"
- "fetchDeviceTokenForParticipantID:"
- "fetchDonationIDsWithCount:fromLatest:excludingEvaluationIDs:completion:"
- "fetchDonationWithDonationID:completion:"
- "fetchDonationsWithCount:fromLatest:completion:"
- "fetchDonationsWithCount:fromLatest:excludingEvaluationIDs:completion:"
- "fetchEvaluationWithEvaluationID:completion:"
- "firstEvaluation"
- "firstObject"
- "form"
- "formId"
- "formIdentifier"
- "formItemsURLFormTat:"
- "formResponse"
- "formattedRequestHeader:session:cookies:"
- "fromJSONWithData:"
- "givenName"
- "hasPrefix:"
- "hash"
- "host"
- "infoDictionary"
- "init"
- "initClient:"
- "initWithCampaign:campaignErrors:feedbackSubmitted:declineCount:"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFeatureDomain:feedbackTitle:prefillQuestions:attributionBundleId:modelVersion:originalAnnotatedContent:generatedAnnotatedContent:extraContent:"
- "initWithFeedbackForm:"
- "initWithIdentifier:"
- "initWithInteger:"
- "initWithMachServiceName:options:"
- "initWithPayload:displayName:description:fileName:iconType:additionalInfo:"
- "initWithSuiteName:"
- "initWithSwiftObject:"
- "initialize"
- "integerValue"
- "invalidateDonationWithDonationJSON:completion:"
- "isAppleConnectLogin"
- "isCaptive"
- "isEqual:"
- "isEqualToString:"
- "isHighPriority"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPIPLConsent"
- "isProxy"
- "isRequired"
- "isSystemAccount"
- "jsonForURLRequest:success:error:"
- "launchNewDraft"
- "learnMoreURL"
- "length"
- "loadFormItemWithFormTat:withCompletion:"
- "localizedStringForKey:value:table:"
- "logFeedbackdLaunchedFeedbackWithForm:usedAlertPrompt:usedNotificationPrompt:usedHiddenApp:"
- "logFeedbackdReceivedNotificationResponse:formIdentifier:"
- "logHTTPErrorWithResponse:withData:fromRequest:"
- "logOutServerSideWithCompletion:"
- "loginWithTokenURL"
- "lowercaseString"
- "mainBundle"
- "makeVisible"
- "modelVersion"
- "mutableCopy"
- "notifyOnUpload"
- "null"
- "numberWithInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "originalContent"
- "overrideEnvironment:host:"
- "overrideGeoCountryCode"
- "participantID"
- "path"
- "pendingConsents"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prefill:answer:"
- "prefillWithQuestion:answer:"
- "presentedDonationWithEvaluationID:completion:"
- "presentedInteractionWithAnalyticsPayload:featureDomainEventName:completion:"
- "presentedWithCompletion:"
- "presentedWithInteraction:completion:"
- "presentingBundleId"
- "processInfo"
- "processName"
- "productVersion"
- "protectionSpace"
- "q"
- "q16@0:8"
- "queryItemWithName:value:"
- "recordEvaluationWithEvaluationJSON:completion:"
- "registerDefaults:"
- "release"
- "remoteEvaluateWithRequest:sceneID:bundleID:completion:"
- "remoteObjectProxyWithErrorHandler:"
- "remoteViewControllerDidLaunchWhileLockedWithCompletion:"
- "removeObjectForKey:"
- "reportFailureToLaunchFormWithFormIdentifier:completion:"
- "requestWithURL:"
- "resetDaemonWithCompletion:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "s"
- "s16@0:8"
- "saveDeviceTokenLookupInformation"
- "scanCharactersFromSet:intoString:"
- "scanInteger:"
- "scannerWithString:"
- "sceneId"
- "seedPortal"
- "seedPortalLoginAsUnauthenticatedUserWithSuccessHandler:error:"
- "seedPortalLoginWithDeviceToken:success:error:"
- "seedPortalSession"
- "seedPortalURL"
- "self"
- "sentPresented"
- "serverTrust"
- "session"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAdditionalInfo:"
- "setAllowedUnits:"
- "setAlwaysLaunchInRemoteAlert:"
- "setAlwaysUseRemoteAlertController:"
- "setAnswers:"
- "setAttributionBundleId:"
- "setAuthenticationMethod:"
- "setBehavior:"
- "setCharactersToBeSkipped:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCoreHTTPClient:"
- "setCountStyle:"
- "setDateStyle:"
- "setDeviceToken:"
- "setDeviceToken:forParticipantID:"
- "setDisplayName:"
- "setEnvironment:"
- "setExportedObject:"
- "setExtraContent:"
- "setFamilyName:"
- "setFeatureDomain:"
- "setFeedbackTitle:"
- "setFeedbackURL:"
- "setFileName:"
- "setForm:"
- "setFormId:"
- "setGeneratedAnnotatedContent:"
- "setGivenName:"
- "setHTTPAdditionalHeaders:"
- "setHTTPBody:"
- "setHTTPContentType:"
- "setHTTPMethod:"
- "setID:"
- "setIconType:"
- "setIdentifier:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsAppleConnectLogin:"
- "setIsCaptive:"
- "setIsPIPLConsent:"
- "setIsSystemAccount:"
- "setLaunchNewDraft:"
- "setLocalizedAlertViewDeclineButtonTitle:"
- "setLocalizedAlertViewProceedButtonTitle:"
- "setLocalizedPromptMessage:"
- "setLocalizedPromptTitle:"
- "setMakeVisible:"
- "setModelVersion:"
- "setNotifyImmediately:"
- "setNotifyOnUpload:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOriginalAnnotatedContent:"
- "setParticipantID:"
- "setPayload:"
- "setPendingConsents:"
- "setPrefillQuestions:"
- "setPresentingBundleId:"
- "setPromptStyle:"
- "setProtocol:"
- "setQueryItems:"
- "setQuestionsWithNsMutableDict:"
- "setRemoteObjectInterface:"
- "setSceneId:"
- "setSeedPortalSession:"
- "setSeedPortalURL:"
- "setSession:"
- "setSignedConsents:"
- "setSkipsPrompt:"
- "setSwiftObject:"
- "setTimeStyle:"
- "setToSkipPrompt:"
- "setURLCache:"
- "setUsername:"
- "setValue:forKey:"
- "set_description:"
- "sharedUserDefaults"
- "signOutURL"
- "signedConsents"
- "standardUserDefaults"
- "state"
- "statusCode"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringForKey:"
- "stringFromByteCount:"
- "stringFromDate:"
- "stringValue"
- "stringWithFormat:"
- "subject"
- "submissionDate"
- "superclass"
- "swTrain"
- "swVers"
- "swiftObject"
- "symbolImageName"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unauthenticatedLoginURL"
- "unsignedLongValue"
- "updatedAt"
- "uppercaseLetterCharacterSet"
- "uppercaseString"
- "userInfo"
- "username"
- "v16@0:8"
- "v16@?0@\"FBKSUserLoginInfo\"8"
- "v20@0:8B16"
- "v20@0:8s16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8q16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "v28@0:8s16@20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@?16@?24"
- "v32@0:8I16B20@?24"
- "v32@0:8I16B20@?<v@?@\"NSData\"@\"NSError\">24"
- "v36@0:8@16B24B28B32"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSUUID\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURL\"16@?<v@?@\"NSData\">24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURLRequest\"16@?<v@?@\"NSData\">24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURLRequest\"16@?<v@?@\"NSData\"@\"NSURLResponse\">24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURLRequest\"16@?<v@?@>24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8I16B20@\"NSArray\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8I16B20@24@?32"
- "v40@0:8q16B24B28@?32"
- "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v52@0:8@\"NSString\"16@\"NSNumber\"24B32@\"NSError\"36@?<v@?@\"NSError\">44"
- "v52@0:8@16@24B32@36@?44"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "v64@0:8@16q24B32B36@40@48@?56"
- "value"
- "valueForHTTPHeaderField:"
- "valueForKey:"
- "whitespaceAndNewlineCharacterSet"
- "zone"

```
