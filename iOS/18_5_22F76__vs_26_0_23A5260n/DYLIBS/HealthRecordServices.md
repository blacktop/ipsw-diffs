## HealthRecordServices

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x47c64
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x52cc
-  __TEXT.__const: 0xa88
-  __TEXT.__cstring: 0x3785
+6074.1.2.4.0
+  __TEXT.__text: 0x49988
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x548c
+  __TEXT.__const: 0xcf8
+  __TEXT.__cstring: 0x3b75
   __TEXT.__ustring: 0x78
   __TEXT.__oslogstring: 0xb60
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__swift5_typeref: 0x180
-  __TEXT.__swift5_fieldmd: 0x20c
-  __TEXT.__constg_swiftt: 0x27c
-  __TEXT.__swift5_reflstr: 0x15b
+  __TEXT.__gcc_except_tab: 0x104
+  __TEXT.__constg_swiftt: 0x328
+  __TEXT.__swift5_typeref: 0x20c
+  __TEXT.__swift5_fieldmd: 0x254
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_reflstr: 0x169
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_proto: 0xa8
+  __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0x1658
-  __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0xfc1
-  __TEXT.__objc_methname: 0xb562
-  __TEXT.__objc_methtype: 0x22cb
-  __TEXT.__objc_stubs: 0x5bc0
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__const: 0x1590
-  __DATA_CONST.__objc_classlist: 0x310
+  __TEXT.__unwind_info: 0x1718
+  __TEXT.__eh_frame: 0x340
+  __TEXT.__objc_classname: 0xff4
+  __TEXT.__objc_methname: 0xb8c0
+  __TEXT.__objc_methtype: 0x2418
+  __TEXT.__objc_stubs: 0x5de0
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x1630
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f78
+  __DATA_CONST.__objc_selrefs: 0x2038
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x2c0
-  __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH_CONST.__const: 0x760
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0xa068
+  __DATA_CONST.__objc_superrefs: 0x2d0
+  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__const: 0x900
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0xa2d0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1220
-  __DATA.__objc_ivar: 0x59c
-  __DATA.__data: 0xbc0
-  __DATA.__bss: 0xd80
-  __DATA_DIRTY.__objc_data: 0xc30
+  __AUTH.__objc_data: 0x1338
+  __AUTH.__data: 0xd0
+  __DATA.__objc_ivar: 0x598
+  __DATA.__data: 0xc60
+  __DATA.__bss: 0x1200
+  __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__data: 0x258
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8C759988-0C3F-3D5F-AA1C-144268D692C6
-  Functions: 2106
-  Symbols:   6377
-  CStrings:  3170
+  UUID: 0CF78AA6-6D99-3C5B-9F35-6C72FC47EC2A
+  Functions: 2183
+  Symbols:   6537
+  CStrings:  3255
 
Symbols:
+ +[HKClinicalStore taskIdentifier]
+ +[HKFHIRCredential nilCredential]
+ +[HKSignedClinicalDataParsingResultMux supportsSecureCoding]
+ +[HKSignedClinicalDataSource sourceWithQRCodeValue:passcode:error:]
+ -[HDHealthRecordsLegacyIngestionServiceClient _doubleObjectCompletionOnClientQueue:]
+ -[HDHealthRecordsLegacyIngestionServiceClient fetchAccessTokenForTokenSession:connectionInformation:completion:]
+ -[HDHealthRecordsLegacyIngestionServiceClient fetchOrRefreshCredentialForAccount:completion:]
+ -[HKClinicalAccountConnectionInformation initWithAccountIdentifier:gateway:authorization:authentication:]
+ -[HKClinicalAccountStore refreshAccountConnectionInformationForAccountWithIdentifier:completion:]
+ -[HKClinicalGatewayEndpointSchema _queryItemsWithBindings:queryMode:authentication:error:]
+ -[HKClinicalGatewayEndpointSchema _queryParametersWithAuthentication:]
+ -[HKClinicalGatewayEndpointSchema createURLWithBindings:queryMode:authentication:error:]
+ -[HKClinicalGatewayEndpointSchema currentScopeStringWithError:]
+ -[HKClinicalGatewayEndpointSchema definition]
+ -[HKClinicalGatewayEndpointSchema initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:definition:]
+ -[HKClinicalGatewayEndpointSchemaParameter useWithQueryMode:]
+ -[HKClinicalProviderServiceStore setHealthRecordsEnvironment:completion:]
+ -[HKClinicalStore .cxx_destruct]
+ -[HKClinicalStore automaticProxyReconnectionHandler]
+ -[HKClinicalStore clientQueueActionHandlerWithCompletion:]
+ -[HKClinicalStore clientQueueBoolHandlerWithCompletion:]
+ -[HKClinicalStore clientQueueDoubleBoolHandlerWithCompletion:]
+ -[HKClinicalStore clientQueueErrorHandlerWithCompletion:]
+ -[HKClinicalStore clientQueueFailableActionHandlerWithCompletion:]
+ -[HKClinicalStore clientQueueObjectHandlerWithCompletion:]
+ -[HKClinicalStore dispatchAsyncProxyClientQueue:]
+ -[HKClinicalStore fetchServerProxyWithHandler:errorHandler:]
+ -[HKClinicalStore getSynchronousProxyWithHandler:errorHandler:]
+ -[HKClinicalStore healthStore]
+ -[HKClinicalStore initWithHealthStore:exportedObject:]
+ -[HKClinicalStore initWithHealthStore:exportedObject:].cold.1
+ -[HKClinicalStore proxyProviderShouldRetryOnInterruption]
+ -[HKClinicalStore setAutomaticProxyReconnectionHandler:]
+ -[HKClinicalStore setProxyProviderShouldRetryOnInterruption:]
+ -[HKFHIRCredential asRefreshResultWithError:]
+ -[HKFHIRCredentialRefreshResult debugDescription]
+ -[HKSignedClinicalDataParsingResult muxed]
+ -[HKSignedClinicalDataParsingResultMux .cxx_destruct]
+ -[HKSignedClinicalDataParsingResultMux copyWithZone:]
+ -[HKSignedClinicalDataParsingResultMux encodeWithCoder:]
+ -[HKSignedClinicalDataParsingResultMux hash]
+ -[HKSignedClinicalDataParsingResultMux initWithCoder:]
+ -[HKSignedClinicalDataParsingResultMux initWithSignedClinicalData:]
+ -[HKSignedClinicalDataParsingResultMux initWithSignedClinicalData:].cold.1
+ -[HKSignedClinicalDataParsingResultMux init]
+ -[HKSignedClinicalDataParsingResultMux isEqual:]
+ -[HKSignedClinicalDataParsingResultMux signedClinicalData]
+ -[HKSignedClinicalDataQRSegment hash]
+ -[HKSignedClinicalDataQRSegment initWithDataValue:sourceType:position:numberOfExpectedSiblings:]
+ -[HKSignedClinicalDataQRSegment sourceType]
+ -[HKSignedClinicalDataSource hash]
+ -[HKSignedClinicalDataSource initWithQRRepresentation:passcode:]
+ -[HKSignedClinicalDataSource passcode]
+ GCC_except_table1
+ GCC_except_table11
+ GCC_except_table38
+ GCC_except_table48
+ _HKFHIRAuthorizationSchemaParameterNamePKCEChallenge
+ _HKFHIRAuthorizationSchemaParameterNamePKCEMethod
+ _HKFHIRAuthorizationSchemaParameterNamePKCEVerifier
+ _HKFHIREndpointSchemaVariableClientID
+ _HKFHIREndpointSchemaVariableClientSecret
+ _HKFHIREndpointSchemaVariableCode
+ _HKFHIREndpointSchemaVariableGreaterEqualLastFetchDate
+ _HKFHIREndpointSchemaVariableGreaterEqualLastFetchDateTime
+ _HKFHIREndpointSchemaVariablePKCEChallenge
+ _HKFHIREndpointSchemaVariablePKCEVerifier
+ _HKFHIREndpointSchemaVariablePatient
+ _HKFHIREndpointSchemaVariableRefreshToken
+ _HKFHIREndpointSchemaVariableState
+ _HKFHIRResourceQueryModeFromNSString
+ _HKHealthRecordsEnvironmentDefaultsKey
+ _HKHealthRecordsEnvironmentsLogicallySorted
+ _HKHealthRecordsEnvironmentsLogicallySorted.arr
+ _OBJC_CLASS_$_HKClinicalStore
+ _OBJC_CLASS_$_HKSignedClinicalDataParsingResultMux
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$__HKDaemonPreferences
+ _OBJC_CLASS_$__TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider
+ _OBJC_IVAR_$_HKClinicalGatewayEndpointSchema._definition
+ _OBJC_IVAR_$_HKClinicalStore._healthStore
+ _OBJC_IVAR_$_HKClinicalStore._proxyProvider
+ _OBJC_IVAR_$_HKSignedClinicalDataParsingResultMux._signedClinicalData
+ _OBJC_IVAR_$_HKSignedClinicalDataQRSegment._sourceType
+ _OBJC_IVAR_$_HKSignedClinicalDataSource._passcode
+ _OBJC_METACLASS_$_HKClinicalStore
+ _OBJC_METACLASS_$_HKSignedClinicalDataParsingResultMux
+ _OBJC_METACLASS_$__TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider
+ __Block_copy
+ __Block_release
+ __DATA__TtC20HealthRecordServices23CodableFHIRResourceData
+ __DATA__TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider
+ __INSTANCE_METHODS__TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider
+ __IVARS__TtC20HealthRecordServices23CodableFHIRResourceData
+ __METACLASS_DATA__TtC20HealthRecordServices23CodableFHIRResourceData
+ __METACLASS_DATA__TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider
+ __OBJC_$_CLASS_METHODS_HKClinicalStore
+ __OBJC_$_CLASS_METHODS_HKSignedClinicalDataParsingResultMux
+ __OBJC_$_CLASS_PROP_LIST_HKClinicalStore
+ __OBJC_$_CLASS_PROP_LIST_HKSignedClinicalDataParsingResultMux
+ __OBJC_$_INSTANCE_METHODS_HKClinicalStore
+ __OBJC_$_INSTANCE_METHODS_HKSignedClinicalDataParsingResultMux
+ __OBJC_$_INSTANCE_VARIABLES_HKClinicalStore
+ __OBJC_$_INSTANCE_VARIABLES_HKSignedClinicalDataParsingResultMux
+ __OBJC_$_PROP_LIST_HKClinicalStore
+ __OBJC_$_PROP_LIST_HKSignedClinicalDataParsingResultMux
+ __OBJC_CLASS_PROTOCOLS_$_HKSignedClinicalDataParsingResultMux
+ __OBJC_CLASS_RO_$_HKClinicalStore
+ __OBJC_CLASS_RO_$_HKSignedClinicalDataParsingResultMux
+ __OBJC_METACLASS_RO_$_HKClinicalStore
+ __OBJC_METACLASS_RO_$_HKSignedClinicalDataParsingResultMux
+ ___112-[HDHealthRecordsLegacyIngestionServiceClient fetchAccessTokenForTokenSession:connectionInformation:completion:]_block_invoke
+ ___112-[HDHealthRecordsLegacyIngestionServiceClient fetchAccessTokenForTokenSession:connectionInformation:completion:]_block_invoke_2
+ ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.292
+ ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.292.cold.1
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.302
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.302.cold.1
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.304
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.308
+ ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.308.cold.1
+ ___56-[HKClinicalStore clientQueueBoolHandlerWithCompletion:]_block_invoke
+ ___56-[HKClinicalStore clientQueueBoolHandlerWithCompletion:]_block_invoke_2
+ ___62-[HKClinicalStore clientQueueDoubleBoolHandlerWithCompletion:]_block_invoke
+ ___62-[HKClinicalStore clientQueueDoubleBoolHandlerWithCompletion:]_block_invoke_2
+ ___66-[HKClinicalStore clientQueueFailableActionHandlerWithCompletion:]_block_invoke
+ ___66-[HKClinicalStore clientQueueFailableActionHandlerWithCompletion:]_block_invoke_2
+ ___73-[HKClinicalProviderServiceStore setHealthRecordsEnvironment:completion:]_block_invoke
+ ___73-[HKClinicalProviderServiceStore setHealthRecordsEnvironment:completion:]_block_invoke_2
+ ___84-[HDHealthRecordsLegacyIngestionServiceClient _doubleObjectCompletionOnClientQueue:]_block_invoke
+ ___84-[HDHealthRecordsLegacyIngestionServiceClient _doubleObjectCompletionOnClientQueue:]_block_invoke_2
+ ___93-[HDHealthRecordsLegacyIngestionServiceClient fetchOrRefreshCredentialForAccount:completion:]_block_invoke
+ ___93-[HDHealthRecordsLegacyIngestionServiceClient fetchOrRefreshCredentialForAccount:completion:]_block_invoke_2
+ ___97-[HKClinicalAccountStore refreshAccountConnectionInformationForAccountWithIdentifier:completion:]_block_invoke
+ ___97-[HKClinicalAccountStore refreshAccountConnectionInformationForAccountWithIdentifier:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs_e57_v16?0"<HKClinicalProviderServiceStoreServerInterface>"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v32?0816"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e58_v16?0"<HDHealthRecordsLegacyIngestionServiceInterface>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_literal_global.301
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HealthRecordServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HealthRecordServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HealthRecordServices
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 20HealthRecordServices23CodableFHIRResourceDataC10CodingKeysOSHAASQ
+ _associated conformance 20HealthRecordServices23CodableFHIRResourceDataC10CodingKeysOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 20HealthRecordServices23CodableFHIRResourceDataC10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper
+ _block_copy_helper.9
+ _block_descriptor
+ _block_descriptor.11
+ _block_destroy_helper
+ _block_destroy_helper.10
+ _objc_autorelease
+ _objc_msgSend$_doubleObjectCompletionOnClientQueue:
+ _objc_msgSend$_queryItemsWithBindings:queryMode:authentication:error:
+ _objc_msgSend$_queryParametersWithAuthentication:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$asRefreshResultWithError:
+ _objc_msgSend$automaticProxyReconnectionHandler
+ _objc_msgSend$clientQueueBoolHandlerWithCompletion:
+ _objc_msgSend$clientQueueDoubleBoolHandlerWithCompletion:
+ _objc_msgSend$clientQueueFailableActionHandlerWithCompletion:
+ _objc_msgSend$dispatchAsyncProxyClientQueue:
+ _objc_msgSend$fetchServerProxyWithHandler:errorHandler:
+ _objc_msgSend$initWithAccountIdentifier:gateway:authorization:authentication:
+ _objc_msgSend$initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:definition:
+ _objc_msgSend$initWithDataValue:sourceType:position:numberOfExpectedSiblings:
+ _objc_msgSend$initWithName:value:
+ _objc_msgSend$initWithQRRepresentation:passcode:
+ _objc_msgSend$initWithSignedClinicalData:
+ _objc_msgSend$nilCredential
+ _objc_msgSend$passcode
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$remote_fetchAccessTokenForTokenSession:connectionInformation:completion:
+ _objc_msgSend$remote_fetchOrRefreshCredentialForAccount:completion:
+ _objc_msgSend$remote_refreshAccountConnectionInformationForAccountWithIdentifier:completion:
+ _objc_msgSend$remote_setHealthRecordsEnvironment:completion:
+ _objc_msgSend$setProxyProviderShouldRetryOnInterruption:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$shouldRetryOnInterruption
+ _objc_msgSend$signedClinicalData
+ _objc_msgSend$sourceWithQRCodeValue:passcode:error:
+ _objc_msgSend$useWithQueryMode:
+ _objc_release_x1
+ _prefixStringForSignedClinicalDataSourceType
+ _swift_arrayDestroy
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCastObjCClassUnconditional
+ _swift_errorRelease
+ _swift_setDeallocating
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic So15HKProxyProviderC
+ _symbolic So18HDFHIRResourceDataC
+ _symbolic So21NSXPCListenerEndpointCIeyBy_
+ _symbolic So7NSErrorCIeyBy_
+ _symbolic _____ 20HealthRecordServices0A26RecordsDaemonProxyProviderC
+ _symbolic _____ 20HealthRecordServices23CodableFHIRResourceDataC
+ _symbolic _____ 20HealthRecordServices23CodableFHIRResourceDataC10CodingKeysO
- +[HKClinicalAccountStore taskIdentifier]
- +[HKClinicalDocumentStore taskIdentifier]
- +[HKClinicalIngestionStore taskIdentifier]
- -[HDHealthRecordsLegacyIngestionServiceClient foo]
- -[HKClinicalAccountConnectionInformation authSchemaDefinitions]
- -[HKClinicalAccountConnectionInformation initWithAccountIdentifier:gateway:authorization:authentication:authSchemaDefinitions:resourceSchemaDefinitions:]
- -[HKClinicalAccountConnectionInformation resourceSchemaDefinitions]
- -[HKClinicalAccountStore _clientQueueBoolHandlerWithCompletion:]
- -[HKClinicalAccountStore _clientQueueDoubleBoolHandlerWithCompletion:]
- -[HKClinicalAccountStore _clientQueueFailableActionHandlerWithCompletion:]
- -[HKClinicalAccountStore _fetchServerProxyWithHandler:errorHandler:]
- -[HKClinicalAccountStore allAccountsWithError:]
- -[HKClinicalAccountStore healthStore]
- -[HKClinicalAccountStore refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:]
- -[HKClinicalDocumentStore _fetchServerProxyWithHandler:errorHandler:]
- -[HKClinicalDocumentStore _getSynchronousServerProxyWithHandler:errorHandler:]
- -[HKClinicalGatewayEndpointSchema initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:]
- -[HKClinicalIngestionStore healthStore]
- -[HKClinicalProviderServiceStore fetchLogoDataForFeaturedBrandsAtScaleKey:completion:]
- -[HKSignedClinicalDataQRSegment initWithDataValue:position:numberOfExpectedSiblings:]
- GCC_except_table2
- GCC_except_table42
- GCC_except_table52
- _HKHealthRecordsSetEnvironment
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_IVAR_$_HKClinicalAccountConnectionInformation._authSchemaDefinitions
- _OBJC_IVAR_$_HKClinicalAccountConnectionInformation._resourceSchemaDefinitions
- _OBJC_IVAR_$_HKClinicalAccountStore._healthStore
- _OBJC_IVAR_$_HKClinicalAccountStore._proxyProvider
- _OBJC_IVAR_$_HKClinicalDocumentStore._proxyProvider
- _OBJC_IVAR_$_HKClinicalIngestionStore._healthStore
- _OBJC_IVAR_$_HKClinicalIngestionStore._proxyProvider
- __OBJC_$_CLASS_METHODS_HKClinicalAccountStore
- __OBJC_$_CLASS_METHODS_HKClinicalDocumentStore
- __OBJC_$_CLASS_METHODS_HKClinicalIngestionStore
- __OBJC_$_CLASS_PROP_LIST_HKClinicalAccountStore
- __OBJC_$_CLASS_PROP_LIST_HKClinicalDocumentStore
- __OBJC_$_CLASS_PROP_LIST_HKClinicalIngestionStore
- ___47-[HKClinicalAccountStore allAccountsWithError:]_block_invoke
- ___47-[HKClinicalAccountStore allAccountsWithError:]_block_invoke_2
- ___47-[HKClinicalAccountStore allAccountsWithError:]_block_invoke_3
- ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.291
- ___52-[HKClinicalDocumentStore _establishProxyConnection]_block_invoke.291.cold.1
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.299
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.299.cold.1
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke.301
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.305
- ___54-[HKClinicalSharingSyncObserver resumeWithCompletion:]_block_invoke_2.305.cold.1
- ___64-[HKClinicalAccountStore _clientQueueBoolHandlerWithCompletion:]_block_invoke
- ___64-[HKClinicalAccountStore _clientQueueBoolHandlerWithCompletion:]_block_invoke_2
- ___70-[HKClinicalAccountStore _clientQueueDoubleBoolHandlerWithCompletion:]_block_invoke
- ___70-[HKClinicalAccountStore _clientQueueDoubleBoolHandlerWithCompletion:]_block_invoke_2
- ___74-[HKClinicalAccountStore _clientQueueFailableActionHandlerWithCompletion:]_block_invoke
- ___74-[HKClinicalAccountStore _clientQueueFailableActionHandlerWithCompletion:]_block_invoke_2
- ___86-[HKClinicalProviderServiceStore fetchLogoDataForFeaturedBrandsAtScaleKey:completion:]_block_invoke
- ___86-[HKClinicalProviderServiceStore fetchLogoDataForFeaturedBrandsAtScaleKey:completion:]_block_invoke_2
- ___99-[HKClinicalAccountStore refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:]_block_invoke
- ___99-[HKClinicalAccountStore refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e49_v16?0"<HKClinicalAccountStoreServerInterface>"8lr32l8r40l8
- ___block_literal_global.289
- ___block_literal_global.304
- ___block_literal_global.305
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HealthRecordServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HealthRecordServices
- _objc_msgSend$_clientQueueBoolHandlerWithCompletion:
- _objc_msgSend$_clientQueueDoubleBoolHandlerWithCompletion:
- _objc_msgSend$_clientQueueFailableActionHandlerWithCompletion:
- _objc_msgSend$authSchemaDefinitions
- _objc_msgSend$initWithAccountIdentifier:gateway:authorization:authentication:authSchemaDefinitions:resourceSchemaDefinitions:
- _objc_msgSend$initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:
- _objc_msgSend$initWithDataValue:position:numberOfExpectedSiblings:
- _objc_msgSend$initWithQRRepresentation:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$remote_fetchLogoDataForFeaturedBrandsAtScaleKey:completion:
- _objc_msgSend$remote_refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:
- _objc_msgSend$resourceSchemaDefinitions
- _objc_msgSend$setInteger:forKey:
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "!"
+ "<%@ %p; credential %@; auth response %@; end states %@; error %@>"
+ "@"
+ "@\"HKSignedClinicalDataParsingResult\""
+ "@100@0:8@16@24B32@36@44@52q60@68@76@84@92"
+ "@48@0:8@16q24@32^@40"
+ "B24@0:8q16"
+ "HKClinicalStore"
+ "HKClinicalStore.m"
+ "HKSignedClinicalDataParsingResultMux"
+ "HKSignedClinicalDataParsingResultMux.m"
+ "HealthRecordServices.HealthRecordsDaemonProxyProvider"
+ "PKCEChallenge"
+ "PKCEVerifier"
+ "Scope parameter item did not have a literal key-value pair %@"
+ "SignedClinicalData"
+ "T@\"HKSignedClinicalDataParsingResult\",R,C,N,V_signedClinicalData"
+ "T@\"NSString\",R,C,N,V_passcode"
+ "T@,R,C,N,V_definition"
+ "T@?,C"
+ "TB"
+ "Unable to create URL from components: %@"
+ "Unable to determine base URL for endpoint %@"
+ "Unable to find scope query parameter"
+ "Unbound variable: %@"
+ "_TtC20HealthRecordServices23CodableFHIRResourceData"
+ "_TtC20HealthRecordServices32HealthRecordsDaemonProxyProvider"
+ "_definition"
+ "_doubleObjectCompletionOnClientQueue:"
+ "_passcode"
+ "_queryItemsWithBindings:queryMode:authentication:error:"
+ "_queryParametersWithAuthentication:"
+ "_signedClinicalData"
+ "arrayByAddingObjectsFromArray:"
+ "asRefreshResultWithError:"
+ "attempting to add a segment with a different source type"
+ "authorize"
+ "automaticProxyReconnectionHandler"
+ "clientQueueBoolHandlerWithCompletion:"
+ "clientQueueDoubleBoolHandlerWithCompletion:"
+ "clientQueueFailableActionHandlerWithCompletion:"
+ "code_challenge"
+ "code_challenge_method"
+ "code_verifier"
+ "createURLWithBindings:queryMode:authentication:error:"
+ "currentScopeStringWithError:"
+ "definition"
+ "dispatchAsyncProxyClientQueue:"
+ "fetchAccessTokenForTokenSession:connectionInformation:completion:"
+ "fetchOrRefreshCredentialForAccount:completion:"
+ "fetchServerProxyWithHandler:errorHandler:"
+ "fhir"
+ "geLastFetchedDate"
+ "geLastFetchedDateTime"
+ "healthStore != nil"
+ "init(source:serviceIdentifier:exportedObject:exportedInterface:remoteInterface:)"
+ "initWithAccountIdentifier:gateway:authorization:authentication:"
+ "initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:definition:"
+ "initWithDataValue:sourceType:position:numberOfExpectedSiblings:"
+ "initWithHealthStore:exportedObject:"
+ "initWithName:value:"
+ "initWithQRRepresentation:passcode:"
+ "initWithSignedClinicalData:"
+ "muxed"
+ "nilCredential"
+ "passcode"
+ "proxyProviderShouldRetryOnInterruption"
+ "rangeOfString:options:range:"
+ "refreshAccountConnectionInformationForAccountWithIdentifier:completion:"
+ "remote_fetchAccessTokenForTokenSession:connectionInformation:completion:"
+ "remote_fetchOrRefreshCredentialForAccount:completion:"
+ "remote_refreshAccountConnectionInformationForAccountWithIdentifier:completion:"
+ "remote_setHealthRecordsEnvironment:completion:"
+ "result != nil"
+ "setHealthRecordsEnvironment:completion:"
+ "setProxyProviderShouldRetryOnInterruption:"
+ "setQueryItems:"
+ "shouldRetryOnInterruption"
+ "signedClinicalData"
+ "sourceWithQRCodeValue:passcode:error:"
+ "unable to fetch legacy ingestion service interface proxy"
+ "unsupported code value starting with \"%@\""
+ "useWithQueryMode:"
+ "v16@?0@\"NSXPCListenerEndpoint\"8"
+ "v20@0:8B16"
+ "v32@0:8@\"HKClinicalAccountConnectionInformation\"16@?<v@?@\"HKFHIRCredentialRefreshResult\">24"
+ "v32@0:8@\"HKSignedClinicalDataSource\"16@?<v@?@\"HKSignedClinicalDataParsingResultMux\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"HKClinicalAccountConnectionInformation\"@\"NSError\">24"
+ "v32@?0@8@16@\"NSError\"24"
+ "v40@0:8@\"HKOAuth2TokenSession\"16@\"HKClinicalAccountConnectionInformation\"24@?<v@?@\"HKFHIRCredential\"@\"HKFHIRRequestTaskEndState\"@\"NSError\">32"
+ "v40@0:8@\"HKSignedClinicalDataSource\"16Q24@?<v@?@\"HKSignedClinicalDataParsingResultMux\"@\"NSError\">32"
- "#"
- "@40@0:8@16q24q32"
- "@92@0:8@16@24B32@36@44@52q60@68@76@84"
- "T@\"NSArray\",R,C,N,V_authSchemaDefinitions"
- "T@\"NSArray\",R,C,N,V_resourceSchemaDefinitions"
- "_authSchemaDefinitions"
- "_clientQueueBoolHandlerWithCompletion:"
- "_clientQueueDoubleBoolHandlerWithCompletion:"
- "_clientQueueFailableActionHandlerWithCompletion:"
- "_resourceSchemaDefinitions"
- "allAccountsWithError:"
- "authSchemaDefinitions"
- "com.apple.healthd"
- "fetchLogoDataForFeaturedBrandsAtScaleKey:completion:"
- "foo"
- "initWithAccountIdentifier:gateway:authorization:authentication:authSchemaDefinitions:resourceSchemaDefinitions:"
- "initWithAuth:body:enabled:form:headers:method:minCompatibleAPIVersion:name:query:URL:"
- "initWithDataValue:position:numberOfExpectedSiblings:"
- "initWithSuiteName:"
- "refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:"
- "remote_fetchLogoDataForFeaturedBrandsAtScaleKey:completion:"
- "remote_refreshAccountConnectionInformationForAccountsWithIdentifiers:completion:"
- "resourceSchemaDefinitions"
- "setInteger:forKey:"
- "unsupported code value \"%@\""
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v32@0:8@\"HKSignedClinicalDataSource\"16@?<v@?@\"HKSignedClinicalDataParsingResult\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v40@0:8@\"HKSignedClinicalDataSource\"16Q24@?<v@?@\"HKSignedClinicalDataParsingResult\"@\"NSError\">32"

```
