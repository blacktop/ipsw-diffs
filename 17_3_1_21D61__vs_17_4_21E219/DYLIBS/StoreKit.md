## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-813.3.3.0.0
-  __TEXT.__text: 0x170280
+813.4.32.0.0
+  __TEXT.__text: 0x16b074
   __TEXT.__auth_stubs: 0x3110
-  __TEXT.__objc_methlist: 0x470c
-  __TEXT.__gcc_except_tab: 0xef4
-  __TEXT.__const: 0x942a
-  __TEXT.__cstring: 0x72ba
+  __TEXT.__objc_methlist: 0x4754
+  __TEXT.__gcc_except_tab: 0xf0c
+  __TEXT.__const: 0x8e5a
+  __TEXT.__cstring: 0x76aa
   __TEXT.__oslogstring: 0x20a9
-  __TEXT.__dlopen_cstrs: 0x3dd
-  __TEXT.__swift5_typeref: 0x3263
-  __TEXT.__constg_swiftt: 0x2a84
+  __TEXT.__dlopen_cstrs: 0x43f
+  __TEXT.__swift5_typeref: 0x2f85
+  __TEXT.__constg_swiftt: 0x21d4
   __TEXT.__swift5_reflstr: 0x1d35
-  __TEXT.__swift5_fieldmd: 0x2c24
-  __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_assocty: 0xa88
-  __TEXT.__swift5_proto: 0x920
-  __TEXT.__swift5_types: 0x3bc
-  __TEXT.__swift5_capture: 0xd3c
+  __TEXT.__swift5_fieldmd: 0x29a8
+  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_assocty: 0x620
+  __TEXT.__swift5_proto: 0x878
+  __TEXT.__swift5_types: 0x334
+  __TEXT.__swift5_capture: 0xd70
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x6f40
-  __TEXT.__eh_frame: 0x8698
-  __TEXT.__objc_classname: 0x1202
-  __TEXT.__objc_methname: 0xc956
-  __TEXT.__objc_methtype: 0x2af5
-  __TEXT.__objc_stubs: 0x82a0
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0x1988
+  __TEXT.__swift5_protos: 0x20
+  __TEXT.__unwind_info: 0x6cd0
+  __TEXT.__eh_frame: 0x8908
+  __TEXT.__objc_classname: 0x1217
+  __TEXT.__objc_methname: 0xcaa6
+  __TEXT.__objc_methtype: 0x2b8d
+  __TEXT.__objc_stubs: 0x82e0
+  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__const: 0x1968
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12ed0
-  __DATA_CONST.__objc_selrefs: 0x2cf0
+  __DATA_CONST.__objc_const: 0x12eb0
+  __DATA_CONST.__objc_selrefs: 0x2d08
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_classrefs: 0x580
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x94c8
+  __AUTH_CONST.__const: 0x8ee0
   __AUTH_CONST.__objc_const: 0x2798
-  __AUTH_CONST.__cfstring: 0x3720
+  __AUTH_CONST.__cfstring: 0x3780
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1898
   __AUTH.__objc_data: 0x2488
-  __AUTH.__data: 0x27c8
-  __DATA.__objc_protorefs: 0x110
-  __DATA.__objc_classrefs: 0x580
-  __DATA.__objc_superrefs: 0x228
-  __DATA.__objc_ivar: 0x5d4
-  __DATA.__data: 0x8258
-  __DATA.__bss: 0xdc30
-  __DATA.__common: 0x68
+  __AUTH.__data: 0x1c90
+  __DATA.__objc_ivar: 0x5dc
+  __DATA.__data: 0x9a98
+  __DATA.__bss: 0xd1c0
+  __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/AppStoreFoundation.framework/AppStoreFoundation
   - /System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FFF11BF0-9DAA-3187-8A3F-EF7C1D0676D9
-  Functions: 11117
-  Symbols:   14062
-  CStrings:  4160
+  UUID: 4FBD81D2-630B-3F24-8189-E4BFA7338369
+  Functions: 10253
+  Symbols:   13153
+  CStrings:  4199
 
Symbols:
+ -[SKCloudServiceSetupViewController viewWillAppear:]
+ -[SKEngagementRemoteViewTask presentationWindow]
+ -[SKEngagementRemoteViewTask setPresentationWindow:]
+ -[SKServiceBroker externalGatewayServiceWithErrorHandler:]
+ -[SKStoreReviewViewController presentationWindow]
+ -[SKStoreReviewViewController setPresentationWindow:]
+ _AppleMediaServicesLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_SKEngagementRemoteViewTask._presentationWindow
+ _OBJC_IVAR_$_SKStoreReviewViewController._presentationWindow
+ _OUTLINED_FUNCTION_469
+ _OUTLINED_FUNCTION_470
+ _OUTLINED_FUNCTION_471
+ _OUTLINED_FUNCTION_472
+ _OUTLINED_FUNCTION_473
+ _OUTLINED_FUNCTION_474
+ _OUTLINED_FUNCTION_475
+ _OUTLINED_FUNCTION_476
+ _OUTLINED_FUNCTION_477
+ _OUTLINED_FUNCTION_478
+ _OUTLINED_FUNCTION_479
+ _OUTLINED_FUNCTION_480
+ _OUTLINED_FUNCTION_481
+ _OUTLINED_FUNCTION_482
+ _OUTLINED_FUNCTION_483
+ _OUTLINED_FUNCTION_484
+ _OUTLINED_FUNCTION_485
+ _OUTLINED_FUNCTION_486
+ _OUTLINED_FUNCTION_487
+ _OUTLINED_FUNCTION_488
+ _OUTLINED_FUNCTION_489
+ _OUTLINED_FUNCTION_490
+ _OUTLINED_FUNCTION_491
+ _OUTLINED_FUNCTION_492
+ _OUTLINED_FUNCTION_493
+ _OUTLINED_FUNCTION_494
+ _OUTLINED_FUNCTION_495
+ _OUTLINED_FUNCTION_496
+ _OUTLINED_FUNCTION_497
+ _SKEntitlementExternalPurchase
+ _SKEntitlementExternalPurchaseLink
+ _SKStoreProductParameterEnableOpenAppCallback
+ _SKStoreProductParameterWebBrowser
+ __BuildDateString
+ __BuildTimeString
+ __DYLDProgramSDKAtLeast2019A
+ __DYLDProgramSDKAtLeast2023E
+ __DeviceIsRunningInternalBuild
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ExternalGatewayService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ExternalGatewayService
+ __OBJC_LABEL_PROTOCOL_$_ExternalGatewayService
+ __OBJC_PROTOCOL_$_ExternalGatewayService
+ ___58-[SKServiceBroker externalGatewayServiceWithErrorHandler:]_block_invoke
+ ___65-[SKCloudServiceSetupViewController _requestRemoteViewController]_block_invoke.116
+ ___AppleMediaServicesLibraryCore_block_invoke
+ ___getAMSBiometricsClass_block_invoke
+ ___getAMSBiometricsClass_block_invoke.cold.1
+ ___swift_memcpy96_8
+ _associated conformance 15StoreKit_Shared0aB13InternalErrorO27PurchasesDisabledCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared0aB13InternalErrorO27PurchasesDisabledCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared0aB13InternalErrorO34NotAvailableInStorefrontCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared0aB13InternalErrorO34NotAvailableInStorefrontCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLOs0J3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO0E10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO0E10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOSHAASQ
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO17AccountCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO17AccountCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO21AlternativeCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeO21AlternativeCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared19ExternalGatewayModeOSHAASQ
+ _associated conformance 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysOSHAASQ
+ _associated conformance 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 8StoreKit16ExternalPurchaseO6OptionVSHAASQ
+ _associated conformance 8StoreKit20ExternalPurchaseLinkO6OptionVSHAASQ
+ _associated conformance 8StoreKit7ProductV17SubscriptionOfferV9SignatureVSHAASQ
+ _audit_stringAppleMediaServices
+ _block_copy_helper.100
+ _block_copy_helper.106
+ _block_copy_helper.117
+ _block_copy_helper.123
+ _block_copy_helper.129
+ _block_copy_helper.135
+ _block_copy_helper.14
+ _block_copy_helper.36
+ _block_copy_helper.42
+ _block_copy_helper.48
+ _block_copy_helper.50
+ _block_copy_helper.52
+ _block_copy_helper.56
+ _block_copy_helper.62
+ _block_copy_helper.68
+ _block_copy_helper.74
+ _block_copy_helper.76
+ _block_copy_helper.80
+ _block_copy_helper.82
+ _block_copy_helper.86
+ _block_copy_helper.92
+ _block_copy_helper.94
+ _block_descriptor.102
+ _block_descriptor.108
+ _block_descriptor.119
+ _block_descriptor.125
+ _block_descriptor.131
+ _block_descriptor.137
+ _block_descriptor.16
+ _block_descriptor.38
+ _block_descriptor.44
+ _block_descriptor.50
+ _block_descriptor.52
+ _block_descriptor.54
+ _block_descriptor.58
+ _block_descriptor.64
+ _block_descriptor.70
+ _block_descriptor.76
+ _block_descriptor.78
+ _block_descriptor.82
+ _block_descriptor.84
+ _block_descriptor.88
+ _block_descriptor.94
+ _block_descriptor.96
+ _block_destroy_helper.101
+ _block_destroy_helper.107
+ _block_destroy_helper.118
+ _block_destroy_helper.124
+ _block_destroy_helper.130
+ _block_destroy_helper.136
+ _block_destroy_helper.15
+ _block_destroy_helper.37
+ _block_destroy_helper.43
+ _block_destroy_helper.49
+ _block_destroy_helper.51
+ _block_destroy_helper.53
+ _block_destroy_helper.57
+ _block_destroy_helper.63
+ _block_destroy_helper.69
+ _block_destroy_helper.75
+ _block_destroy_helper.77
+ _block_destroy_helper.81
+ _block_destroy_helper.83
+ _block_destroy_helper.87
+ _block_destroy_helper.93
+ _block_destroy_helper.95
+ _getAMSBiometricsClass.softClass
+ _objc_msgSend$isAvailableForAccount:
+ _objc_msgSend$setPresentationWindow:
+ _objectdestroy.127Tm
+ _objectdestroy.36Tm
+ _objectdestroy.83Tm
+ _objectdestroy.8Tm
+ _os_variant_has_internal_content
+ _symbolic SDySSypGSg
+ _symbolic SS5token_t
+ _symbolic ScCySSSg______pG s5ErrorP
+ _symbolic _____ 15StoreKit_Shared0aB13InternalErrorO27PurchasesDisabledCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____ 15StoreKit_Shared0aB13InternalErrorO34NotAvailableInStorefrontCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____ 15StoreKit_Shared19ExternalGatewayModeO
+ _symbolic _____ 15StoreKit_Shared19ExternalGatewayModeO0E10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____ 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____ 15StoreKit_Shared19ExternalGatewayModeO17AccountCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____ 15StoreKit_Shared19ExternalGatewayModeO21AlternativeCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____ 15StoreKit_Shared27ExternalGatewaySheetRequestV
+ _symbolic _____ 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysO
+ _symbolic _____ 15StoreKit_Shared7LazyJWSV
+ _symbolic _____ 8StoreKit16ExternalPurchaseO6OptionV
+ _symbolic _____ 8StoreKit20ExternalPurchaseLinkO6OptionV
+ _symbolic _____ 8StoreKit7ProductV15LazyDataStorage33_3C0143BCD22F0BF641CAA00711A4F505LLV
+ _symbolic _____ 8StoreKit7ProductV17SubscriptionOfferV9SignatureV
+ _symbolic _____Sg 15StoreKit_Shared7LazyJWSV
+ _symbolic _____ySo6NSDataCG 15AtomicsInternal26ManagedAtomicLazyReferenceC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared0dE13InternalErrorO27PurchasesDisabledCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared0dE13InternalErrorO34NotAvailableInStorefrontCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared19ExternalGatewayModeO0H10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared19ExternalGatewayModeO17AccountCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared19ExternalGatewayModeO21AlternativeCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared0dE13InternalErrorO27PurchasesDisabledCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared0dE13InternalErrorO34NotAvailableInStorefrontCodingKeys33_12C5235E2CAE281542EE4A381ACA6DA2LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared19ExternalGatewayModeO0H10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared19ExternalGatewayModeO10CodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared19ExternalGatewayModeO17AccountCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared19ExternalGatewayModeO21AlternativeCodingKeys33_3CD8D5DD6047930674276B58B49B20D7LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared27ExternalGatewaySheetRequestV10CodingKeysO
- _SKSimulatorToHostServiceName
- __IVARS__TtC7Atomics13ManagedAtomic
- __IVARS__TtC7Atomics26ManagedAtomicLazyReference
- ___65-[SKCloudServiceSetupViewController _requestRemoteViewController]_block_invoke.114
- ___unnamed_10
- ___unnamed_4
- ___unnamed_5
- ___unnamed_7
- ___unnamed_8
- ___unnamed_9
- __sa_cmpxchg_strong_acq_rel_acquire_Bool
- __sa_cmpxchg_strong_acq_rel_acquire_DoubleWord
- __sa_cmpxchg_strong_acq_rel_acquire_Int
- __sa_cmpxchg_strong_acq_rel_acquire_Int16
- __sa_cmpxchg_strong_acq_rel_acquire_Int32
- __sa_cmpxchg_strong_acq_rel_acquire_Int8
- __sa_cmpxchg_strong_acq_rel_acquire_UInt16
- __sa_cmpxchg_strong_acq_rel_acquire_UInt8
- __sa_cmpxchg_strong_acq_rel_relaxed_Bool
- __sa_cmpxchg_strong_acq_rel_relaxed_DoubleWord
- __sa_cmpxchg_strong_acq_rel_relaxed_Int
- __sa_cmpxchg_strong_acq_rel_relaxed_Int16
- __sa_cmpxchg_strong_acq_rel_relaxed_Int32
- __sa_cmpxchg_strong_acq_rel_relaxed_Int8
- __sa_cmpxchg_strong_acq_rel_relaxed_UInt16
- __sa_cmpxchg_strong_acq_rel_relaxed_UInt8
- __sa_cmpxchg_strong_acquire_acquire_Bool
- __sa_cmpxchg_strong_acquire_acquire_DoubleWord
- __sa_cmpxchg_strong_acquire_acquire_Int
- __sa_cmpxchg_strong_acquire_acquire_Int16
- __sa_cmpxchg_strong_acquire_acquire_Int32
- __sa_cmpxchg_strong_acquire_acquire_Int8
- __sa_cmpxchg_strong_acquire_acquire_UInt16
- __sa_cmpxchg_strong_acquire_acquire_UInt8
- __sa_cmpxchg_strong_acquire_relaxed_Bool
- __sa_cmpxchg_strong_acquire_relaxed_DoubleWord
- __sa_cmpxchg_strong_acquire_relaxed_Int
- __sa_cmpxchg_strong_acquire_relaxed_Int16
- __sa_cmpxchg_strong_acquire_relaxed_Int32
- __sa_cmpxchg_strong_acquire_relaxed_Int8
- __sa_cmpxchg_strong_acquire_relaxed_UInt16
- __sa_cmpxchg_strong_acquire_relaxed_UInt8
- __sa_cmpxchg_strong_relaxed_relaxed_Bool
- __sa_cmpxchg_strong_relaxed_relaxed_DoubleWord
- __sa_cmpxchg_strong_relaxed_relaxed_Int
- __sa_cmpxchg_strong_relaxed_relaxed_Int16
- __sa_cmpxchg_strong_relaxed_relaxed_Int32
- __sa_cmpxchg_strong_relaxed_relaxed_Int8
- __sa_cmpxchg_strong_relaxed_relaxed_UInt16
- __sa_cmpxchg_strong_relaxed_relaxed_UInt8
- __sa_cmpxchg_strong_release_relaxed_Bool
- __sa_cmpxchg_strong_release_relaxed_DoubleWord
- __sa_cmpxchg_strong_release_relaxed_Int
- __sa_cmpxchg_strong_release_relaxed_Int16
- __sa_cmpxchg_strong_release_relaxed_Int32
- __sa_cmpxchg_strong_release_relaxed_Int8
- __sa_cmpxchg_strong_release_relaxed_UInt16
- __sa_cmpxchg_strong_release_relaxed_UInt8
- __sa_cmpxchg_strong_seq_cst_acquire_Bool
- __sa_cmpxchg_strong_seq_cst_acquire_DoubleWord
- __sa_cmpxchg_strong_seq_cst_acquire_Int
- __sa_cmpxchg_strong_seq_cst_acquire_Int16
- __sa_cmpxchg_strong_seq_cst_acquire_Int32
- __sa_cmpxchg_strong_seq_cst_acquire_Int8
- __sa_cmpxchg_strong_seq_cst_acquire_UInt16
- __sa_cmpxchg_strong_seq_cst_acquire_UInt8
- __sa_cmpxchg_strong_seq_cst_relaxed_Bool
- __sa_cmpxchg_strong_seq_cst_relaxed_DoubleWord
- __sa_cmpxchg_strong_seq_cst_relaxed_Int
- __sa_cmpxchg_strong_seq_cst_relaxed_Int16
- __sa_cmpxchg_strong_seq_cst_relaxed_Int32
- __sa_cmpxchg_strong_seq_cst_relaxed_Int8
- __sa_cmpxchg_strong_seq_cst_relaxed_UInt16
- __sa_cmpxchg_strong_seq_cst_relaxed_UInt8
- __sa_cmpxchg_strong_seq_cst_seq_cst_Bool
- __sa_cmpxchg_strong_seq_cst_seq_cst_DoubleWord
- __sa_cmpxchg_strong_seq_cst_seq_cst_Int
- __sa_cmpxchg_strong_seq_cst_seq_cst_Int16
- __sa_cmpxchg_strong_seq_cst_seq_cst_Int32
- __sa_cmpxchg_strong_seq_cst_seq_cst_Int8
- __sa_cmpxchg_strong_seq_cst_seq_cst_UInt16
- __sa_cmpxchg_strong_seq_cst_seq_cst_UInt8
- __sa_cmpxchg_weak_acq_rel_acquire_Bool
- __sa_cmpxchg_weak_acq_rel_acquire_DoubleWord
- __sa_cmpxchg_weak_acq_rel_acquire_Int
- __sa_cmpxchg_weak_acq_rel_acquire_Int16
- __sa_cmpxchg_weak_acq_rel_acquire_Int32
- __sa_cmpxchg_weak_acq_rel_acquire_Int8
- __sa_cmpxchg_weak_acq_rel_acquire_UInt16
- __sa_cmpxchg_weak_acq_rel_acquire_UInt8
- __sa_cmpxchg_weak_acq_rel_relaxed_Bool
- __sa_cmpxchg_weak_acq_rel_relaxed_DoubleWord
- __sa_cmpxchg_weak_acq_rel_relaxed_Int
- __sa_cmpxchg_weak_acq_rel_relaxed_Int16
- __sa_cmpxchg_weak_acq_rel_relaxed_Int32
- __sa_cmpxchg_weak_acq_rel_relaxed_Int8
- __sa_cmpxchg_weak_acq_rel_relaxed_UInt16
- __sa_cmpxchg_weak_acq_rel_relaxed_UInt8
- __sa_cmpxchg_weak_acquire_acquire_Bool
- __sa_cmpxchg_weak_acquire_acquire_DoubleWord
- __sa_cmpxchg_weak_acquire_acquire_Int
- __sa_cmpxchg_weak_acquire_acquire_Int16
- __sa_cmpxchg_weak_acquire_acquire_Int32
- __sa_cmpxchg_weak_acquire_acquire_Int8
- __sa_cmpxchg_weak_acquire_acquire_UInt16
- __sa_cmpxchg_weak_acquire_acquire_UInt8
- __sa_cmpxchg_weak_acquire_relaxed_Bool
- __sa_cmpxchg_weak_acquire_relaxed_DoubleWord
- __sa_cmpxchg_weak_acquire_relaxed_Int
- __sa_cmpxchg_weak_acquire_relaxed_Int16
- __sa_cmpxchg_weak_acquire_relaxed_Int32
- __sa_cmpxchg_weak_acquire_relaxed_Int8
- __sa_cmpxchg_weak_acquire_relaxed_UInt16
- __sa_cmpxchg_weak_acquire_relaxed_UInt8
- __sa_cmpxchg_weak_relaxed_relaxed_Bool
- __sa_cmpxchg_weak_relaxed_relaxed_DoubleWord
- __sa_cmpxchg_weak_relaxed_relaxed_Int
- __sa_cmpxchg_weak_relaxed_relaxed_Int16
- __sa_cmpxchg_weak_relaxed_relaxed_Int32
- __sa_cmpxchg_weak_relaxed_relaxed_Int8
- __sa_cmpxchg_weak_relaxed_relaxed_UInt16
- __sa_cmpxchg_weak_relaxed_relaxed_UInt8
- __sa_cmpxchg_weak_release_relaxed_Bool
- __sa_cmpxchg_weak_release_relaxed_DoubleWord
- __sa_cmpxchg_weak_release_relaxed_Int
- __sa_cmpxchg_weak_release_relaxed_Int16
- __sa_cmpxchg_weak_release_relaxed_Int32
- __sa_cmpxchg_weak_release_relaxed_Int8
- __sa_cmpxchg_weak_release_relaxed_UInt16
- __sa_cmpxchg_weak_release_relaxed_UInt8
- __sa_cmpxchg_weak_seq_cst_acquire_Bool
- __sa_cmpxchg_weak_seq_cst_acquire_DoubleWord
- __sa_cmpxchg_weak_seq_cst_acquire_Int
- __sa_cmpxchg_weak_seq_cst_acquire_Int16
- __sa_cmpxchg_weak_seq_cst_acquire_Int32
- __sa_cmpxchg_weak_seq_cst_acquire_Int8
- __sa_cmpxchg_weak_seq_cst_acquire_UInt16
- __sa_cmpxchg_weak_seq_cst_acquire_UInt8
- __sa_cmpxchg_weak_seq_cst_relaxed_Bool
- __sa_cmpxchg_weak_seq_cst_relaxed_DoubleWord
- __sa_cmpxchg_weak_seq_cst_relaxed_Int
- __sa_cmpxchg_weak_seq_cst_relaxed_Int16
- __sa_cmpxchg_weak_seq_cst_relaxed_Int32
- __sa_cmpxchg_weak_seq_cst_relaxed_Int8
- __sa_cmpxchg_weak_seq_cst_relaxed_UInt16
- __sa_cmpxchg_weak_seq_cst_relaxed_UInt8
- __sa_cmpxchg_weak_seq_cst_seq_cst_Bool
- __sa_cmpxchg_weak_seq_cst_seq_cst_DoubleWord
- __sa_cmpxchg_weak_seq_cst_seq_cst_Int
- __sa_cmpxchg_weak_seq_cst_seq_cst_Int16
- __sa_cmpxchg_weak_seq_cst_seq_cst_Int32
- __sa_cmpxchg_weak_seq_cst_seq_cst_Int8
- __sa_cmpxchg_weak_seq_cst_seq_cst_UInt16
- __sa_cmpxchg_weak_seq_cst_seq_cst_UInt8
- __sa_dispose_Bool
- __sa_dispose_Int16
- __sa_dispose_Int32
- __sa_dispose_Int8
- __sa_dispose_UInt16
- __sa_dispose_UInt8
- __sa_dword_extract_high
- __sa_dword_extract_low
- __sa_exchange_acq_rel_Bool
- __sa_exchange_acq_rel_DoubleWord
- __sa_exchange_acq_rel_Int
- __sa_exchange_acq_rel_Int16
- __sa_exchange_acq_rel_Int32
- __sa_exchange_acq_rel_Int8
- __sa_exchange_acq_rel_UInt16
- __sa_exchange_acq_rel_UInt8
- __sa_exchange_acquire_Bool
- __sa_exchange_acquire_DoubleWord
- __sa_exchange_acquire_Int
- __sa_exchange_acquire_Int16
- __sa_exchange_acquire_Int32
- __sa_exchange_acquire_Int8
- __sa_exchange_acquire_UInt16
- __sa_exchange_acquire_UInt8
- __sa_exchange_relaxed_Bool
- __sa_exchange_relaxed_DoubleWord
- __sa_exchange_relaxed_Int
- __sa_exchange_relaxed_Int16
- __sa_exchange_relaxed_Int32
- __sa_exchange_relaxed_Int8
- __sa_exchange_relaxed_UInt16
- __sa_exchange_relaxed_UInt8
- __sa_exchange_release_Bool
- __sa_exchange_release_DoubleWord
- __sa_exchange_release_Int
- __sa_exchange_release_Int16
- __sa_exchange_release_Int32
- __sa_exchange_release_Int8
- __sa_exchange_release_UInt16
- __sa_exchange_release_UInt8
- __sa_exchange_seq_cst_Bool
- __sa_exchange_seq_cst_DoubleWord
- __sa_exchange_seq_cst_Int
- __sa_exchange_seq_cst_Int16
- __sa_exchange_seq_cst_Int32
- __sa_exchange_seq_cst_Int8
- __sa_exchange_seq_cst_UInt16
- __sa_exchange_seq_cst_UInt8
- __sa_fetch_add_acq_rel_Int
- __sa_fetch_add_acq_rel_Int16
- __sa_fetch_add_acq_rel_Int32
- __sa_fetch_add_acq_rel_Int8
- __sa_fetch_add_acq_rel_UInt16
- __sa_fetch_add_acq_rel_UInt8
- __sa_fetch_add_acquire_Int
- __sa_fetch_add_acquire_Int16
- __sa_fetch_add_acquire_Int32
- __sa_fetch_add_acquire_Int8
- __sa_fetch_add_acquire_UInt16
- __sa_fetch_add_acquire_UInt8
- __sa_fetch_add_relaxed_Int
- __sa_fetch_add_relaxed_Int16
- __sa_fetch_add_relaxed_Int32
- __sa_fetch_add_relaxed_Int8
- __sa_fetch_add_relaxed_UInt16
- __sa_fetch_add_relaxed_UInt8
- __sa_fetch_add_release_Int
- __sa_fetch_add_release_Int16
- __sa_fetch_add_release_Int32
- __sa_fetch_add_release_Int8
- __sa_fetch_add_release_UInt16
- __sa_fetch_add_release_UInt8
- __sa_fetch_add_seq_cst_Int
- __sa_fetch_add_seq_cst_Int16
- __sa_fetch_add_seq_cst_Int32
- __sa_fetch_add_seq_cst_Int8
- __sa_fetch_add_seq_cst_UInt16
- __sa_fetch_add_seq_cst_UInt8
- __sa_fetch_and_acq_rel_Int
- __sa_fetch_and_acq_rel_Int16
- __sa_fetch_and_acq_rel_Int32
- __sa_fetch_and_acq_rel_Int8
- __sa_fetch_and_acq_rel_UInt16
- __sa_fetch_and_acq_rel_UInt8
- __sa_fetch_and_acquire_Int
- __sa_fetch_and_acquire_Int16
- __sa_fetch_and_acquire_Int32
- __sa_fetch_and_acquire_Int8
- __sa_fetch_and_acquire_UInt16
- __sa_fetch_and_acquire_UInt8
- __sa_fetch_and_relaxed_Int
- __sa_fetch_and_relaxed_Int16
- __sa_fetch_and_relaxed_Int32
- __sa_fetch_and_relaxed_Int8
- __sa_fetch_and_relaxed_UInt16
- __sa_fetch_and_relaxed_UInt8
- __sa_fetch_and_release_Int
- __sa_fetch_and_release_Int16
- __sa_fetch_and_release_Int32
- __sa_fetch_and_release_Int8
- __sa_fetch_and_release_UInt16
- __sa_fetch_and_release_UInt8
- __sa_fetch_and_seq_cst_Int
- __sa_fetch_and_seq_cst_Int16
- __sa_fetch_and_seq_cst_Int32
- __sa_fetch_and_seq_cst_Int8
- __sa_fetch_and_seq_cst_UInt16
- __sa_fetch_and_seq_cst_UInt8
- __sa_fetch_or_acq_rel_Int
- __sa_fetch_or_acq_rel_Int16
- __sa_fetch_or_acq_rel_Int32
- __sa_fetch_or_acq_rel_Int8
- __sa_fetch_or_acq_rel_UInt16
- __sa_fetch_or_acq_rel_UInt8
- __sa_fetch_or_acquire_Int
- __sa_fetch_or_acquire_Int16
- __sa_fetch_or_acquire_Int32
- __sa_fetch_or_acquire_Int8
- __sa_fetch_or_acquire_UInt16
- __sa_fetch_or_acquire_UInt8
- __sa_fetch_or_relaxed_Int
- __sa_fetch_or_relaxed_Int16
- __sa_fetch_or_relaxed_Int32
- __sa_fetch_or_relaxed_Int8
- __sa_fetch_or_relaxed_UInt16
- __sa_fetch_or_relaxed_UInt8
- __sa_fetch_or_release_Int
- __sa_fetch_or_release_Int16
- __sa_fetch_or_release_Int32
- __sa_fetch_or_release_Int8
- __sa_fetch_or_release_UInt16
- __sa_fetch_or_release_UInt8
- __sa_fetch_or_seq_cst_Int
- __sa_fetch_or_seq_cst_Int16
- __sa_fetch_or_seq_cst_Int32
- __sa_fetch_or_seq_cst_Int8
- __sa_fetch_or_seq_cst_UInt16
- __sa_fetch_or_seq_cst_UInt8
- __sa_fetch_sub_acq_rel_Int
- __sa_fetch_sub_acq_rel_Int16
- __sa_fetch_sub_acq_rel_Int32
- __sa_fetch_sub_acq_rel_Int8
- __sa_fetch_sub_acq_rel_UInt16
- __sa_fetch_sub_acq_rel_UInt8
- __sa_fetch_sub_acquire_Int
- __sa_fetch_sub_acquire_Int16
- __sa_fetch_sub_acquire_Int32
- __sa_fetch_sub_acquire_Int8
- __sa_fetch_sub_acquire_UInt16
- __sa_fetch_sub_acquire_UInt8
- __sa_fetch_sub_relaxed_Int
- __sa_fetch_sub_relaxed_Int16
- __sa_fetch_sub_relaxed_Int32
- __sa_fetch_sub_relaxed_Int8
- __sa_fetch_sub_relaxed_UInt16
- __sa_fetch_sub_relaxed_UInt8
- __sa_fetch_sub_release_Int
- __sa_fetch_sub_release_Int16
- __sa_fetch_sub_release_Int32
- __sa_fetch_sub_release_Int8
- __sa_fetch_sub_release_UInt16
- __sa_fetch_sub_release_UInt8
- __sa_fetch_sub_seq_cst_Int
- __sa_fetch_sub_seq_cst_Int16
- __sa_fetch_sub_seq_cst_Int32
- __sa_fetch_sub_seq_cst_Int8
- __sa_fetch_sub_seq_cst_UInt16
- __sa_fetch_sub_seq_cst_UInt8
- __sa_fetch_xor_acq_rel_Int
- __sa_fetch_xor_acq_rel_Int16
- __sa_fetch_xor_acq_rel_Int32
- __sa_fetch_xor_acq_rel_Int8
- __sa_fetch_xor_acq_rel_UInt16
- __sa_fetch_xor_acq_rel_UInt8
- __sa_fetch_xor_acquire_Int
- __sa_fetch_xor_acquire_Int16
- __sa_fetch_xor_acquire_Int32
- __sa_fetch_xor_acquire_Int8
- __sa_fetch_xor_acquire_UInt16
- __sa_fetch_xor_acquire_UInt8
- __sa_fetch_xor_relaxed_Int
- __sa_fetch_xor_relaxed_Int16
- __sa_fetch_xor_relaxed_Int32
- __sa_fetch_xor_relaxed_Int8
- __sa_fetch_xor_relaxed_UInt16
- __sa_fetch_xor_relaxed_UInt8
- __sa_fetch_xor_release_Int
- __sa_fetch_xor_release_Int16
- __sa_fetch_xor_release_Int32
- __sa_fetch_xor_release_Int8
- __sa_fetch_xor_release_UInt16
- __sa_fetch_xor_release_UInt8
- __sa_fetch_xor_seq_cst_Int
- __sa_fetch_xor_seq_cst_Int16
- __sa_fetch_xor_seq_cst_Int32
- __sa_fetch_xor_seq_cst_Int8
- __sa_fetch_xor_seq_cst_UInt16
- __sa_fetch_xor_seq_cst_UInt8
- __sa_load_acquire_Bool
- __sa_load_acquire_DoubleWord
- __sa_load_acquire_Int
- __sa_load_acquire_Int16
- __sa_load_acquire_Int32
- __sa_load_acquire_Int8
- __sa_load_acquire_UInt16
- __sa_load_acquire_UInt8
- __sa_load_relaxed_Bool
- __sa_load_relaxed_DoubleWord
- __sa_load_relaxed_Int
- __sa_load_relaxed_Int16
- __sa_load_relaxed_Int32
- __sa_load_relaxed_Int8
- __sa_load_relaxed_UInt16
- __sa_load_relaxed_UInt8
- __sa_load_seq_cst_Bool
- __sa_load_seq_cst_DoubleWord
- __sa_load_seq_cst_Int
- __sa_load_seq_cst_Int16
- __sa_load_seq_cst_Int32
- __sa_load_seq_cst_Int8
- __sa_load_seq_cst_UInt16
- __sa_load_seq_cst_UInt8
- __sa_prepare_Bool
- __sa_release_n
- __sa_retain_n
- __sa_store_relaxed_Bool
- __sa_store_relaxed_DoubleWord
- __sa_store_relaxed_Int
- __sa_store_relaxed_Int16
- __sa_store_relaxed_Int32
- __sa_store_relaxed_Int8
- __sa_store_relaxed_UInt16
- __sa_store_relaxed_UInt8
- __sa_store_release_Bool
- __sa_store_release_DoubleWord
- __sa_store_release_Int
- __sa_store_release_Int16
- __sa_store_release_Int32
- __sa_store_release_Int8
- __sa_store_release_UInt16
- __sa_store_release_UInt8
- __sa_store_seq_cst_Bool
- __sa_store_seq_cst_DoubleWord
- __sa_store_seq_cst_Int
- __sa_store_seq_cst_Int16
- __sa_store_seq_cst_Int32
- __sa_store_seq_cst_Int8
- __sa_store_seq_cst_UInt16
- __sa_store_seq_cst_UInt8
- _associated conformance 7Atomics18AtomicLoadOrderingVSHAASQ
- _associated conformance 7Atomics19AtomicStoreOrderingVSHAASQ
- _associated conformance 7Atomics20AtomicUpdateOrderingVSHAASQ
- _associated conformance SPyxG7Atomics11AtomicValueAB0B14RepresentationAbCP_AB0B7Storage
- _associated conformance SPyxG7Atomics23AtomicOptionalWrappableAB0bC14RepresentationAbCP_AB0B7Storage
- _associated conformance SV7Atomics11AtomicValueAA0B14RepresentationAaBP_AA0B7Storage
- _associated conformance SV7Atomics23AtomicOptionalWrappableAA0bC14RepresentationAaBP_AA0B7Storage
- _associated conformance Sb7Atomics11AtomicValueAA0B14RepresentationAaBP_AA0B7Storage
- _associated conformance Si7Atomics11AtomicValueAA0B14RepresentationAaBP_AA0B7Storage
- _associated conformance Si7Atomics13AtomicIntegerAA0B14RepresentationAA0B5ValueP_AA0bC7Storage
- _associated conformance So9_sa_dworda7Atomics11AtomicValueAC0D14RepresentationAcDP_AC0D7Storage
- _associated conformance So9_sa_dwordaSH7AtomicsSQ
- _associated conformance SpyxG7Atomics11AtomicValueAB0B14RepresentationAbCP_AB0B7Storage
- _associated conformance SpyxG7Atomics23AtomicOptionalWrappableAB0bC14RepresentationAbCP_AB0B7Storage
- _associated conformance Su7Atomics11AtomicValueAA0B14RepresentationAaBP_AA0B7Storage
- _associated conformance Su7Atomics13AtomicIntegerAA0B14RepresentationAA0B5ValueP_AA0bC7Storage
- _associated conformance Sv7Atomics11AtomicValueAA0B14RepresentationAaBP_AA0B7Storage
- _associated conformance Sv7Atomics23AtomicOptionalWrappableAA0bC14RepresentationAaBP_AA0B7Storage
- _associated conformance s4Int8V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s4Int8V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s5Int16V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s5Int16V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s5Int32V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s5Int32V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s5Int64V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s5Int64V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s5UInt8V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s5UInt8V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s6UInt16V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s6UInt16V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s6UInt32V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s6UInt32V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s6UInt64V7Atomics11AtomicValueAC0C14RepresentationAcDP_AC0C7Storage
- _associated conformance s6UInt64V7Atomics13AtomicIntegerAC0C14RepresentationAC0C5ValueP_AC0cD7Storage
- _associated conformance s9UnmanagedVyxG7Atomics11AtomicValueAD0C14RepresentationAdEP_AD0C7Storage
- _associated conformance s9UnmanagedVyxG7Atomics23AtomicOptionalWrappableAD0cD14RepresentationAdEP_AD0C7Storage
- _associated conformance xSg7Atomics11AtomicValueA2B0B17OptionalWrappableRzl0B14RepresentationAbCP_AB0B7Storage
- _block_copy_helper.105
- _block_copy_helper.116
- _block_copy_helper.122
- _block_copy_helper.128
- _block_copy_helper.13
- _block_copy_helper.134
- _block_copy_helper.19
- _block_copy_helper.21
- _block_copy_helper.27
- _block_copy_helper.33
- _block_copy_helper.39
- _block_copy_helper.45
- _block_copy_helper.57
- _block_copy_helper.63
- _block_copy_helper.69
- _block_copy_helper.75
- _block_copy_helper.81
- _block_copy_helper.87
- _block_copy_helper.93
- _block_copy_helper.99
- _block_descriptor.101
- _block_descriptor.107
- _block_descriptor.118
- _block_descriptor.124
- _block_descriptor.130
- _block_descriptor.136
- _block_descriptor.15
- _block_descriptor.21
- _block_descriptor.23
- _block_descriptor.29
- _block_descriptor.35
- _block_descriptor.41
- _block_descriptor.47
- _block_descriptor.59
- _block_descriptor.65
- _block_descriptor.71
- _block_descriptor.77
- _block_descriptor.83
- _block_descriptor.89
- _block_descriptor.95
- _block_destroy_helper.100
- _block_destroy_helper.106
- _block_destroy_helper.117
- _block_destroy_helper.123
- _block_destroy_helper.129
- _block_destroy_helper.135
- _block_destroy_helper.14
- _block_destroy_helper.20
- _block_destroy_helper.22
- _block_destroy_helper.28
- _block_destroy_helper.34
- _block_destroy_helper.40
- _block_destroy_helper.46
- _block_destroy_helper.58
- _block_destroy_helper.64
- _block_destroy_helper.70
- _block_destroy_helper.76
- _block_destroy_helper.82
- _block_destroy_helper.88
- _block_destroy_helper.94
- _objectdestroy.124Tm
- _objectdestroy.126Tm
- _objectdestroy.15Tm
- _objectdestroy.221Tm
- _objectdestroy.37Tm
- _objectdestroy.90Tm
- _swift_unknownObjectRetain_n
- _symbolic $s7Atomics11AtomicValueP
- _symbolic $s7Atomics13AtomicIntegerP
- _symbolic $s7Atomics13AtomicStorageP
- _symbolic $s7Atomics15AtomicReferenceP
- _symbolic $s7Atomics20AtomicIntegerStorageP
- _symbolic $s7Atomics23AtomicOptionalWrappableP
- _symbolic 20AtomicRepresentation_____Qz 7Atomics11AtomicValueP
- _symbolic 20AtomicRepresentation______5Value_____QZ 7Atomics11AtomicValueP AA0B7StorageP
- _symbolic 28AtomicOptionalRepresentation_____Qz 7Atomics23AtomicOptionalWrappableP
- _symbolic 28AtomicOptionalRepresentation______5Value_____QZ 7Atomics23AtomicOptionalWrappableP AA0B7StorageP
- _symbolic 8RawValueSY_20AtomicRepresentation_____QZ 7Atomics11AtomicValueP
- _symbolic SP
- _symbolic SPyxG
- _symbolic SPyxGSg
- _symbolic SV
- _symbolic SVSg
- _symbolic Sccy___________pG 8StoreKit16ExternalPurchaseO12NoticeResultO s5ErrorP
- _symbolic Sp
- _symbolic Spy20AtomicRepresentation_____QzG 7Atomics11AtomicValueP
- _symbolic Spy_____yx_GG s9UnmanagedV7AtomicsE28AtomicOptionalRepresentationV
- _symbolic SpyxG
- _symbolic SpyxGSg
- _symbolic Sq
- _symbolic Su
- _symbolic Sv
- _symbolic SvSg
- _symbolic _____ 7Atomics12UnsafeAtomicV
- _symbolic _____ 7Atomics13ManagedAtomicC
- _symbolic _____ 7Atomics18AtomicLoadOrderingV
- _symbolic _____ 7Atomics19AtomicStoreOrderingV
- _symbolic _____ 7Atomics20AtomicUpdateOrderingV
- _symbolic _____ 7Atomics22AtomicReferenceStorageV
- _symbolic _____ 7Atomics23_AtomicReferenceStorageV
- _symbolic _____ 7Atomics25UnsafeAtomicLazyReferenceV
- _symbolic _____ 7Atomics25UnsafeAtomicLazyReferenceV7StorageV
- _symbolic _____ 7Atomics26ManagedAtomicLazyReferenceC
- _symbolic _____ 7Atomics29AtomicRawRepresentableStorageV
- _symbolic _____ 7Atomics30AtomicOptionalReferenceStorageV
- _symbolic _____ SP7AtomicsE20AtomicRepresentationV
- _symbolic _____ SP7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____ SV7AtomicsE20AtomicRepresentationV
- _symbolic _____ SV7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____ Sb7AtomicsE20AtomicRepresentationV
- _symbolic _____ Si7AtomicsE20AtomicRepresentationV
- _symbolic _____ So10_sa_UInt16a
- _symbolic _____ So10_sa_UInt32a
- _symbolic _____ So10_sa_UInt64a
- _symbolic _____ So13SKGaletteModeV
- _symbolic _____ So14_sa_DoubleWorda
- _symbolic _____ So7_sa_Inta
- _symbolic _____ So8_sa_Boola
- _symbolic _____ So8_sa_Int8a
- _symbolic _____ So8_sa_UInta
- _symbolic _____ So9_sa_Int16a
- _symbolic _____ So9_sa_Int32a
- _symbolic _____ So9_sa_Int64a
- _symbolic _____ So9_sa_UInt8a
- _symbolic _____ So9_sa_dworda
- _symbolic _____ So9_sa_dworda7AtomicsE20AtomicRepresentationV
- _symbolic _____ Sp7AtomicsE20AtomicRepresentationV
- _symbolic _____ Sp7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____ Su7AtomicsE20AtomicRepresentationV
- _symbolic _____ Sv7AtomicsE20AtomicRepresentationV
- _symbolic _____ Sv7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____ s4Int8V
- _symbolic _____ s4Int8V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s5Int16V
- _symbolic _____ s5Int16V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s5Int32V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s5Int64V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s5UInt8V
- _symbolic _____ s5UInt8V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s6UInt16V
- _symbolic _____ s6UInt16V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s6UInt32V
- _symbolic _____ s6UInt32V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s6UInt64V7AtomicsE20AtomicRepresentationV
- _symbolic _____ s9UnmanagedV
- _symbolic _____ s9UnmanagedV7AtomicsE20AtomicRepresentationV
- _symbolic _____ s9UnmanagedV7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____ySo6NSDataCG 7Atomics26ManagedAtomicLazyReferenceC
- _symbolic _____yxG 7Atomics22AtomicReferenceStorageV
- _symbolic _____yxG 7Atomics30AtomicOptionalReferenceStorageV
- _symbolic _____yxG s9UnmanagedV
- _symbolic _____yxGSg s9UnmanagedV
- _symbolic _____yx_G SP7AtomicsE20AtomicRepresentationV
- _symbolic _____yx_G SP7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____yx_G Sp7AtomicsE20AtomicRepresentationV
- _symbolic _____yx_G Sp7AtomicsE28AtomicOptionalRepresentationV
- _symbolic _____yx_G s9UnmanagedV7AtomicsE20AtomicRepresentationV
- _symbolic _____yx_G s9UnmanagedV7AtomicsE28AtomicOptionalRepresentationV
- _symbolic xSg
CStrings:
+ "00:29:11"
+ "@\"SKRemoteEngagementPresentationWindow\""
+ "@\"SKStoreReviewPresentationWindow\""
+ "AMSBiometrics"
+ "Could not cast options to Dictionary<String, Any>"
+ "Division by zero"
+ "Division results in an overflow"
+ "Error checking intro offer eligibility: "
+ "Error encoding External Gateway request "
+ "External gateway not available: "
+ "ExternalGatewayService"
+ "Failed in XPC to open "
+ "Failed to get XPC remote object to open "
+ "Feb 17 2024"
+ "Insufficient space allocated to copy string contents"
+ "Must take zero or more splits"
+ "Negative value is not representable"
+ "Range requires lowerBound <= upperBound"
+ "Received error that does not have a corresponding StoreKit Error: "
+ "Starting External Gateway request "
+ "StoreKit_Shared.StoreKitInternalError"
+ "Swift/Collection.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"SKRemoteEngagementPresentationWindow\",&,N,V_presentationWindow"
+ "T@\"SKStoreReviewPresentationWindow\",&,N,V_presentationWindow"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_presentationWindow"
+ "check introductory offer eligibility"
+ "com.apple.developer.storekit.external-purchase"
+ "com.apple.developer.storekit.external-purchase-link"
+ "enableOpenAppCallback"
+ "externalGatewayServiceWithErrorHandler:"
+ "externalGatewaySheetWithRequest:reply:"
+ "externalPurchaseLinkURLForBundleID:reply:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isAvailableForAccount:"
+ "isEligibleForIntroductoryOfferForGroupID:reply:"
+ "notAvailableInStorefront"
+ "presentationWindow"
+ "purchasesDisabled"
+ "setPresentationWindow:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices"
+ "startRequest(_:)"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "webBrowser"
- "\v"
- "AtomicLoadOrdering("
- "AtomicStoreOrdering("
- "AtomicUpdateOrdering("
- "Atomics/AtomicBool.swift"
- "Atomics/AtomicMemoryOrderings.swift"
- "Atomics/IntegerConformances.swift"
- "DoubleWord(high: "
- "Failed in XPC to check can open %s: %{public}@"
- "Failed in XPC to open %s: %{public}@"
- "Failed in XPC to present external purchase learn more: %{public}@"
- "Failed to get XPC remote object to check can open %s"
- "Failed to get XPC remote object to open %s"
- "Failed to get XPC remote object to present external purchase learn more"
- "Received error that does not have a corresponding StoreKit Error:\n"
- "Unsupported ordering"
- "acquiringAndReleasing"
- "canOpenGalette:reply:"
- "com.apple.storekitservice.sim2host"
- "exchanged original "
- "openAlternativeWithReply:"
- "openGalette:reply:"
- "sequentiallyConsistent"
- "v32@0:8q16@?<v@?@\"NSError\">24"
- "v32@0:8q16@?<v@?B>24"

```
