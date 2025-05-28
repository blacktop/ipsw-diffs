## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-485.80.4.0.0
-  __TEXT.__text: 0x2e6f4
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0x1014
-  __TEXT.__const: 0x20c8
-  __TEXT.__objc_methname: 0x331d
-  __TEXT.__cstring: 0x1e30
-  __TEXT.__objc_classname: 0x2c7
-  __TEXT.__objc_methtype: 0x70c
-  __TEXT.__oslogstring: 0xf1e
-  __TEXT.__gcc_except_tab: 0x184
+558.0.0.0.0
+  __TEXT.__text: 0x51b08
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_stubs: 0x30a0
+  __TEXT.__objc_methlist: 0x1384
+  __TEXT.__const: 0x2628
+  __TEXT.__objc_methname: 0x3eba
+  __TEXT.__oslogstring: 0x12d4
+  __TEXT.__cstring: 0x2c00
+  __TEXT.__objc_classname: 0x38f
+  __TEXT.__objc_methtype: 0xade
+  __TEXT.__gcc_except_tab: 0x228
   __TEXT.__dlopen_cstrs: 0x74
-  __TEXT.__swift5_typeref: 0x4b8
+  __TEXT.__swift5_typeref: 0x910
+  __TEXT.__swift5_fieldmd: 0x1174
+  __TEXT.__constg_swiftt: 0xcc4
+  __TEXT.__swift5_reflstr: 0x1093
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__swift5_fieldmd: 0x578
-  __TEXT.__constg_swiftt: 0x5d8
-  __TEXT.__swift5_reflstr: 0x383
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x1e4
-  __TEXT.__swift5_types: 0x70
-  __TEXT.__unwind_info: 0x1ab0
-  __TEXT.__eh_frame: 0xb60
-  __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x7d0
-  __DATA_CONST.__cfstring: 0x1840
-  __DATA_CONST.__objc_classlist: 0x118
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x2e0
+  __TEXT.__swift5_types: 0x154
+  __TEXT.__swift5_assocty: 0x558
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x24c8
+  __TEXT.__eh_frame: 0x42f0
+  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x2da0
+  __DATA_CONST.__cfstring: 0x1ca0
+  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2688
-  __DATA.__objc_selrefs: 0xba8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1c0
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__objc_data: 0xe58
-  __DATA.__data: 0x1738
-  __DATA.__bss: 0x3ce0
-  __DATA.__common: 0x218
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x2d40
+  __DATA.__objc_selrefs: 0xec8
+  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_data: 0x1008
+  __DATA.__data: 0x2778
+  __DATA.__bss: 0x5680
+  __DATA.__common: 0x140
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
-  - /System/Library/Frameworks/ExposureNotification.framework/ExposureNotification
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1826
-  Symbols:   295
-  CStrings:  1009
+  Functions: 3042
+  Symbols:   332
+  CStrings:  1275
 
Symbols:
+ _DiagnosticLogSubmissionEnabled
+ _NSInternalInconsistencyException
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSPPrivateAccessTokenFetcher
+ _OBJC_CLASS_$__DPDAP02PayloadEncoder
+ _OBJC_CLASS_$__DPDAP09PayloadEncoder
+ _OBJC_CLASS_$__DPDAPPayloadEncoder
+ _OBJC_CLASS_$__DPDediscoBackgroundDownloaderService
+ _OBJC_CLASS_$__DPDediscoPayloadUploader
+ _OBJC_CLASS_$__DPPPM_0_2_0_PayloadEncoderShim
+ _OBJC_CLASS_$__DPPrivateAccessTokenChallenge
+ _OBJC_CLASS_$__DPPrivateAccessTokenManager
+ _OBJC_CLASS_$__DPReportAuth
+ _OBJC_CLASS_$__DPSemanticVersion
+ _OBJC_CLASS_$__DPTaskProv
+ _OBJC_CLASS_$__DPTaskProv00
+ _OBJC_CLASS_$__DPTaskProv06
+ _OBJC_CLASS_$__DPTokenFetcherHelper
+ _OBJC_CLASS_$__DPTokenFetcherService
+ _OBJC_METACLASS_$__DPDAP02PayloadEncoder
+ _OBJC_METACLASS_$__DPDAP09PayloadEncoder
+ _OBJC_METACLASS_$__DPDAPPayloadEncoder
+ _OBJC_METACLASS_$__DPDediscoBackgroundDownloaderService
+ _OBJC_METACLASS_$__DPDediscoPayloadUploader
+ _OBJC_METACLASS_$__DPPPM_0_2_0_PayloadEncoderShim
+ _OBJC_METACLASS_$__DPPrivateAccessTokenChallenge
+ _OBJC_METACLASS_$__DPPrivateAccessTokenManager
+ _OBJC_METACLASS_$__DPReportAuth
+ _OBJC_METACLASS_$__DPSemanticVersion
+ _OBJC_METACLASS_$__DPTaskProv
+ _OBJC_METACLASS_$__DPTaskProv00
+ _OBJC_METACLASS_$__DPTaskProv06
+ _OBJC_METACLASS_$__DPTokenFetcherHelper
+ _OBJC_METACLASS_$__DPTokenFetcherService
+ __DPSemanticVersionError
+ __os_log_debug_impl
+ __set_user_dir_suffix
+ _kDPMetadataDediscoTaskConfigDPConfig
+ _kDPMetadataDediscoTaskConfigDPConfigLocalEpsilon
+ _kDPMetadataDediscoTaskConfigFeatures
+ _kDPMetadataDediscoTaskConfigFeaturesOHTTP
+ _kDPMetadataDediscoTaskConfigFeaturesPAT
+ _kDPMetadataVDAF
+ _kDPMetadataVDAFNonce
+ _kDPMetadataVDAFPrio3SumVectorChunkLength
+ _kDPMetadataVDAFPrio3SumVectorDimension
+ _kDPMetadataVDAFPublicShare
+ _kDPTaskProvMaxBatchQueryCount
+ _kDPTaskProvTimePrecision
+ _kDPVDAFPrio3NumOfProofs
+ _kDPVDAFPrio3SumVectorBitWidth
+ _kDPVDAFType
+ _kRemoteDediscoKeyConfig
+ _objc_exception_throw
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _swift_allocError
+ _swift_checkMetadataState
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getTupleTypeMetadata2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStackObject
+ _swift_initStaticObject
+ _swift_willThrow
- _OBJC_CLASS_$_ENManager
- _OBJC_CLASS_$__DPDediscoPayloadHandler
- _OBJC_CLASS_$__DPENCertificateValidator
- _OBJC_CLASS_$__DPENCertificateValidatorResult
- _OBJC_CLASS_$__DPENConfig
- _OBJC_CLASS_$__DPENServerConfig
- _OBJC_CLASS_$__DPENService
- _OBJC_CLASS_$__DPPrioError
- _OBJC_CLASS_$__DPPrioNetworkingService
- _OBJC_CLASS_$__DPPrioSubmissionManager
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__DPDediscoPayloadHandler
- _OBJC_METACLASS_$__DPENCertificateValidator
- _OBJC_METACLASS_$__DPENCertificateValidatorResult
- _OBJC_METACLASS_$__DPENConfig
- _OBJC_METACLASS_$__DPENServerConfig
- _OBJC_METACLASS_$__DPENService
- _OBJC_METACLASS_$__DPPrioError
- _OBJC_METACLASS_$__DPPrioNetworkingService
- _OBJC_METACLASS_$__DPPrioSubmissionManager
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- _SecCertificateCopyKey
- _SecCertificateCopySubjectPublicKeyInfoSHA256Digest
- _SecCertificateCopySubjectString
- _SecPolicyCreateAggregateMetricEncryption
- ___kCFBooleanTrue
- __swiftEmptyArrayStorage
- _kDPMetadataCountryCode
- _kDPMetadataState
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _swift_deallocClassInstance
- _swift_isUniquelyReferenced_nonNull_native
CStrings:
+ "\x03\x11"
+ "\x03\x16"
+ "\x05"
+ "\x11"
+ "\x11\x13"
+ "$\x13"
+ "%@ encrypted key length exceeds 64KB."
+ "%@ encrypted payload length exceeds 4GB."
+ "%@%ld"
+ "%@/tasks/%@/reports"
+ "%@; "
+ "%@Tokens_%@.pat"
+ ") larger than the encoded length of the "
+ "+"
+ "-"
+ "/"
+ "/var/mobile/Library/PPM/PAT/"
+ "0"
+ "02"
+ "09"
+ "1"
+ "="
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSURLSession\""
+ "@\"_DPDediscoKeyConfigurationV2\""
+ "@\"_DPTaskProv\""
+ "@104@0:8@16@24@32Q40S48I52I56Q60d68I76I80C84I88C92^@96"
+ "@20@0:8S16"
+ "@28@0:8@16B24"
+ "@28@0:8C16^@20"
+ "@36@0:8@16@24B32"
+ "@36@0:8@16I24^@28"
+ "@36@0:8C16@20^@28"
+ "@40@0:8Q16Q24Q32"
+ "@44@0:8@16@24@32B40"
+ "@56@0:8@16@24Q32@40^@48"
+ "@60@0:8@16Q24@32@40@48B56"
+ "@88@0:8@16@24@32Q40S48I52I56Q60d68I76^@80"
+ "@88@0:8@16Q24@32C40@44@52C60@64@72^@80"
+ "Aggregator URL is empty."
+ "All token files are empty at path %@. No token was retrieved."
+ "Attempted to encode more number of bytes "
+ "Attempted to initialize a number with encoded length "
+ "Attempted to read "
+ "Buffer is too short to read "
+ "Bypassing SGX for V2 collectionID %@ - Sending DAP report only"
+ "C16@0:8"
+ "Cannot create _DPReportAuth - empty challenge or token"
+ "Cannot encode DAP extension - total length exceeds UINT16_MAX"
+ "Client failed to download config file with status code %ld and error: %@. %ld retries left."
+ "DPConfig"
+ "DPSubmissionService"
+ "DPSubmissionService1"
+ "DPSubmissionServiceStrictOHTTPDisabled"
+ "DediscoTokensDirectoryPath"
+ "Download finished successfully."
+ "Downloading config file from url %@ ..."
+ "Error in reading config file: %@"
+ "Error: config file length is 0."
+ "Expect TLS vector's `CodingParameter` to be non-nil, and contain the encoded length bounds and the vector element's coding parameter."
+ "Expect the encoded vector length to be "
+ "Expected encoded vector length should be in range "
+ "Expected the encoded vector length to be exactly "
+ "Expected v2 key configurations."
+ "Failed to allocate Private Access Token for %@"
+ "Failed to consume correct number of bytes when decoding vector element. The consumed number of bytes for this element should be between 0 and "
+ "Failed to create DAP payload encoder"
+ "Failed to create HTTP client"
+ "Failed to create NSData from Base-64 encoded string %@"
+ "Failed to create directory at path %@ with error %@."
+ "Failed to create payload encoder for Dedisco V2"
+ "Failed to deserialize the configuration, using default aggregator list."
+ "Failed to deserialize token data with error %@."
+ "Failed to directly upload payload: v1 payload is unsupported"
+ "Failed to download config: timeout on client (%lld sec)"
+ "Failed to extract token fields from config file."
+ "Failed to fetch %ld tokens out of %ld with errors: %@"
+ "Failed to fetch a token after %lld sec timeout."
+ "Failed to fetch a token after %lld sec timeout; "
+ "Failed to fetch a token with error: %@."
+ "Failed to fetch token-challenge pair for aggregator %@: token or challenge missing"
+ "Failed to find matching DAP version from PPM version %lu."
+ "Failed to find matching TaskProv version from PPM version %lu."
+ "Failed to initialize _DPDediscoPayloadUploader: nil upload URL"
+ "Failed to initialize token fetcher."
+ "Failed to match raw value "
+ "Failed to obtain issuer URL."
+ "Failed to parse semantic version from '%@'."
+ "Failed to read the JSON token fields with error %@."
+ "Failed to remove token bucket file %@ in submission service with error %@."
+ "Failed to retrieve challenge data from challenge string."
+ "Failed to retrieve token data from token string."
+ "Failed to send V1 payloads collectionID %@ - http upload is forbidden"
+ "Failed to serialize token array with error: %@"
+ "Failed to update token file at path %@."
+ "Failed to upload DAP Payload: %@"
+ "Failed to upload DAP payload: leader URL is empty"
+ "Failed to upload to DAP report to %@, error: %@"
+ "Failed to write tokens to file at path %@ with error:%@."
+ "Features"
+ "Fetched %lld tokens for aggregator %@."
+ "GET"
+ "Headers in reply: %@"
+ "Helper"
+ "I"
+ "I16@0:8"
+ "Incorrect data type for %@.%@.%@ - expect boolean"
+ "Invalid VDAF parameter(%@) in algorithm parameters, it should be a number."
+ "Invalid VDAF parameter(%@) in metadata, it should be a number."
+ "Invalid VDAF parameter(%@) in metadata."
+ "Issuer URL length must be positive and not exceed 64KB."
+ "LocalEpsilon"
+ "Malformed PPM version in donation metadata, error: %@"
+ "Malformed TLSEnumType: No range is specified for enum "
+ "Malformed parameter (%@.%@) in metadata, it should be a number."
+ "Malformed parameter (%@.%@) in metadata, it should be at least min batch size (%zu)"
+ "Malformed parameter (%@.%@.%@) in metadata, it should be a number"
+ "Missing VDAFType."
+ "NSURLSessionDownloadDelegate"
+ "NSURLSessionTaskDelegate"
+ "No arm specified for case `"
+ "No data found in file path %@ to retrieve token."
+ "No enum case matches the specified raw value: "
+ "No file found in path %@ to retrieve token for aggregator %@."
+ "Nonce"
+ "Nothing to upload: serialized report is empty: %@"
+ "OFF"
+ "OHTTP"
+ "ON"
+ "Origin info length exceeds 64KB."
+ "PPM version is not specified in donation metadata. Using default PPM version 0.2.0 to upload the donation."
+ "PUT"
+ "Prio3NumberOfProofs"
+ "Prio3SumVectorBitWidth"
+ "Prio3SumVectorChunkLength"
+ "Prio3SumVectorDimension"
+ "PrivateAccessToken"
+ "Property for case `eps_delta` is nil."
+ "Property for case `eps` is nil."
+ "Property for case `fixed_size` is nil."
+ "Property for case `float16` is nil."
+ "Property for case `float32` is nil."
+ "Property for case `float64` is nil."
+ "Property for case `none` is nil."
+ "Property for case `poplar1` is nil."
+ "Property for case `prio2` is nil."
+ "Property for case `prio3_count` is nil."
+ "Property for case `prio3_histogram` is nil."
+ "Property for case `prio3_sum_vec_field64_multiproof_cmac_aes128` is nil."
+ "Property for case `prio3_sum_vec_field64_multiproof_hmac_sha256_aes128` is nil."
+ "Property for case `prio3_sum_vec` is nil."
+ "Property for case `prio3_sum` is nil."
+ "Property for case `prio_pirappor` is nil."
+ "Property for case `prio_plusplus` is nil."
+ "Property for case `renyi` is nil."
+ "Property for case `time_interval` is nil."
+ "PublicShare"
+ "Reached maximum retries. Failed to download the config file."
+ "Redemption context length, %@, must be equal to 32."
+ "Report requires Private Access Token"
+ "Report requires no Private Access Token"
+ "Skipping field (%@) expected NSDictionary value, got %@."
+ "Skipping field =(%@) as it cannot be serialized into JSON, type=%@."
+ "Successfully saved tokens to file."
+ "Successfully uploaded DAP report to %@"
+ "T@\"NSData\",&,N,V_challenge"
+ "T@\"NSData\",&,N,V_data"
+ "T@\"NSData\",&,N,V_encodedTaskConfig"
+ "T@\"NSData\",&,N,V_extensions"
+ "T@\"NSData\",&,N,V_reportID"
+ "T@\"NSData\",&,N,V_taskID"
+ "T@\"NSData\",&,N,V_token"
+ "T@\"NSData\",R,C,N,V_redemptionContext"
+ "T@\"NSData\",R,N,V_helperURL"
+ "T@\"NSData\",R,N,V_leaderURL"
+ "T@\"NSData\",R,N,V_taskInfo"
+ "T@\"NSDictionary\",&,N,V_deserializedConfig"
+ "T@\"NSDictionary\",&,N,V_tokenFields"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_wait"
+ "T@\"NSString\",&,N,V_baseURL"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_issuerURL"
+ "T@\"NSString\",C,N,V_tokensDirectoryPath"
+ "T@\"NSString\",R,C,N,V_issuer"
+ "T@\"NSString\",R,C,N,V_origin"
+ "T@\"NSString\",R,N,V_collectionID"
+ "T@\"NSURL\",R,N,V_url"
+ "T@\"NSURLSession\",R,N,V_backgroundSession"
+ "T@\"_DPDediscoKeyConfigurationV2\",R,N,V_keys"
+ "T@\"_DPTaskProv\",R,N,V_taskProv"
+ "TB,N,V_uploadWithOHTTP"
+ "TB,N,V_useOHTTP"
+ "TI,R,N,V_maxBatchSize"
+ "TI,R,N,V_minBatchSize"
+ "TI,R,N,V_vdafType"
+ "TLS variant must receive a non-nil coding parameter."
+ "TQ,N,V_maxRetries"
+ "TQ,R,N,V_majorVersion"
+ "TQ,R,N,V_minorVersion"
+ "TQ,R,N,V_patchVersion"
+ "TQ,R,N,V_taskExpiration"
+ "TQ,R,N,V_time"
+ "TaskProv extension data length exceeds 64KB."
+ "TaskProv00 cannot handle any VDAF other than Prio2."
+ "Timeout uploading: %@"
+ "Token type not supported."
+ "UInt24 cannot be initialized from a UInt32 value of "
+ "URLSession:didCreateTask:"
+ "URLSession:downloadTask:didFinishDownloadingToURL:"
+ "URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:"
+ "URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "Unable to encrypt %@ share with HPKE."
+ "Unable to find a matching PPM version from donation metadata's version string: '%@'"
+ "Unknown VDAFType = %lu in TaskProv06."
+ "Unknown VDAFType = %lu."
+ "Upload rejected: unable to determine OHTTP flag: %@"
+ "Upload via HTTP body size: %lu - uploading to %@"
+ "Uploading DAP payload to %@, OHTTP:%s"
+ "Using PPM version 0.1.0 to upload the donation."
+ "Using PPM version 0.2.0 to upload the donation."
+ "VDAF"
+ "VDAFType"
+ "Version string is not a valid semantic version string. It should specify at least \"<major>.<minor>.<patch>\"."
+ "^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
+ "_"
+ "_DPDAP02PayloadEncoder"
+ "_DPDAP09PayloadEncoder"
+ "_DPDAPPayloadEncoder"
+ "_DPDediscoBackgroundDownloaderService"
+ "_DPDediscoPayloadUploader"
+ "_DPPPM_0_2_0_PayloadEncoderShim"
+ "_DPPrivateAccessTokenChallenge"
+ "_DPPrivateAccessTokenManager"
+ "_DPReportAuth"
+ "_DPSemanticVersion"
+ "_DPTaskProv"
+ "_DPTaskProv00"
+ "_DPTaskProv06"
+ "_DPTokenFetcherHelper"
+ "_DPTokenFetcherService"
+ "_backgroundSession"
+ "_baseURL"
+ "_challenge"
+ "_data"
+ "_deserializedConfig"
+ "_encodedTaskConfig"
+ "_extensions"
+ "_helperURL"
+ "_issuer"
+ "_issuerURL"
+ "_leaderURL"
+ "_majorVersion"
+ "_maxBatchSize"
+ "_maxRetries"
+ "_minBatchSize"
+ "_minorVersion"
+ "_origin"
+ "_patchVersion"
+ "_queue"
+ "_redemptionContext"
+ "_reportID"
+ "_setPrivacyProxyFailClosed:"
+ "_taskExpiration"
+ "_taskID"
+ "_taskProv"
+ "_token"
+ "_tokenFields"
+ "_tokensDirectoryPath"
+ "_uploadWithOHTTP"
+ "_url"
+ "_useOHTTP"
+ "_vdafType"
+ "_wait"
+ "`Nid` must be specified in the coding parameter to indicate the TLS vector length."
+ "addObjectsFromArray:"
+ "addTimeInterval:"
+ "aggregatorList"
+ "allHeaderFields"
+ "allKeys"
+ "application/dap-report;version=%@;build-type=%@"
+ "attributesOfItemAtPath:error:"
+ "backgroundSession"
+ "backgroundSessionConfigurationWithIdentifier:"
+ "baseURL"
+ "buildHTTPHeadersWithPayload:withEncoder:withError:"
+ "challenge"
+ "com.apple.DPSubmissionService.BackgroundDownload"
+ "com.apple.DifferentialPrivacy.SemanticVersionError"
+ "com.apple.DifferentialPrivacy.tokens"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createUploadClientWithURL:withHeaders:uploadWithOHTTP:"
+ "currentQueue"
+ "dap-%@ input share"
+ "dap-collection-id"
+ "dap-reportauth"
+ "dap-reportauth: %@"
+ "dap-taskprov"
+ "dap-taskprov: %@"
+ "data"
+ "dataWithContentsOfFile:"
+ "dataWithContentsOfFile:options:error:"
+ "dd_MM_yyyy_HH_mm_ss"
+ "decoding `Data`, but there are only "
+ "defaultManager"
+ "derivedMaxBatchSizeFromDonationMetadata:minBatchSize:error:"
+ "derivedMinBatchSize"
+ "derivedTaskExpiration"
+ "deserializedConfig"
+ "dictionary"
+ "dictionaryWithDictionary:"
+ "dictionaryWithObjects:forKeys:"
+ "downloadConfigSynchronously"
+ "downloadTaskWithURL:"
+ "encodeExtensionsWithError:"
+ "encodeReportID"
+ "encodeWithError:"
+ "encodedInfoForServerRole:"
+ "encodedInputShareAADWithTaskID:reportID:time:publicShare:error:"
+ "encodedPlaintextInputShareForServerRole:error:"
+ "encodedPlaintextInputShareWithTaskProvExtensionData:payload:error:"
+ "encodedQueryConfig"
+ "encodedReportAuthExtensionDataWithError:"
+ "encodedReportWithError:"
+ "encodedReportWithReportID:time:publicShare:leaderHPKEConfigID:leaderEnc:leaderPayload:helperHPKEConfigID:helperEnc:helperPayload:error:"
+ "encodedTaskConfig"
+ "encodedTaskConfigForPrio2WithTaskInfo:leaderAggregatorEndpoint:helperAggregatorEndpoint:timePrecision:maxBatchQueryCount:minBatchSize:maxBatchSize:taskExpiration:epsilon:length:error:"
+ "encodedTaskConfigForPrio3SumVectorWithTaskInfo:leaderAggregatorEndpoint:helperAggregatorEndpoint:timePrecision:maxBatchQueryCount:minBatchSize:maxBatchSize:taskExpiration:epsilon:vdafTypeRawValue:length:bits:chunkLength:numProofs:error:"
+ "encodedTaskConfigWithError:"
+ "encodedTaskProvExtensionDataWithError:"
+ "encodedVDAFConfig"
+ "encoderForDonation:keys:error:"
+ "encryptedShareForServerRole:publicKey:error:"
+ "enumeratorAtPath:"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "exceptionWithName:reason:userInfo:"
+ "extensions"
+ "extractIssuerURL"
+ "extractTokenFieldsFromConfig:"
+ "fedstats:com.apple.Bitacora.TokenFetcher:000:000:000"
+ "fetchMultipleChallengeTokenPairForAggregator:"
+ "fetchTokenWithQueue:completionHandler:"
+ "fetchTokenWithReply:"
+ "fetchTokens"
+ "fileCreationDate"
+ "fileExistsAtPath:isDirectory:"
+ "fileSize"
+ "fileURLWithPath:"
+ "filesInDirectory:"
+ "getCollectionId"
+ "getDAPVersion"
+ "getHelperServerName"
+ "getLeaderServerName"
+ "getReport"
+ "hasSuffix:"
+ "helperHPKEConfigID"
+ "helperURL"
+ "host"
+ "initWithBase64Encoding:"
+ "initWithBaseURL:useOHTTP:"
+ "initWithChallenge:tokenKey:originNameKey:"
+ "initWithDomain:configurationURL:tlsTrustPinningPolicyName:"
+ "initWithDomain:retries:method:tlsTrustPinningPolicyName:defaultHeaders:uploadWithOHTTP:"
+ "initWithDonation:keys:taskProv:error:"
+ "initWithDonation:leaderURL:helperURL:error:"
+ "initWithIssuer:origin:redemptionContext:"
+ "initWithMajorVersion:minorVersion:patchVersion:"
+ "initWithString:error:"
+ "initWithToken:withChallenge:"
+ "initWithTokenPath:"
+ "initWithURL:"
+ "inputShareInfoString"
+ "insertIfPossibleObj:intoJSONDictionary:withKey:"
+ "integerValue"
+ "invalidateAndCancel"
+ "is available in "
+ "is available in UInt16."
+ "is available in UInt32."
+ "is available in UInt64."
+ "is available in UInt8."
+ "isBackwardCompatibleWithVersion:"
+ "isDataCollectionEnabled"
+ "isDonationValidWithError:"
+ "isFeatureEnabled:withError:"
+ "isOHTTPEnabledWithError:"
+ "isPrivateAccessTokenEnabledWithError:"
+ "isTaskConfigValidWithError:"
+ "isTelemetryAllowed"
+ "isValidJSONObject:"
+ "issuer"
+ "issuer-url"
+ "issuerURL"
+ "jsonRepresentationForMetadata"
+ "jsonRepresentationFromParameters:"
+ "key value "
+ "leaderHPKEConfigID"
+ "leaderURL"
+ "logAndStoreInError:"
+ "majorVersion"
+ "maxBatchSize"
+ "maxRetries"
+ "minBatchSize"
+ "minorVersion"
+ "nextObject"
+ "not-before"
+ "numberOfRanges"
+ "of it to decode TLS number type "
+ "origin"
+ "originNameKey"
+ "patchVersion"
+ "path"
+ "payloadEncoderForDonation:keys:error:"
+ "private-access-token-issuers"
+ "queue"
+ "randomFileForAggregator:"
+ "randomTokenForAggregator:"
+ "rangeAtIndex:"
+ "redemptionContext"
+ "removeItemAtPath:error:"
+ "removeObjectAtIndex:"
+ "reportAuthForAggregator:"
+ "reportID"
+ "response"
+ "saveTokens:toFileInPath:forAggregator:"
+ "secondsSinceEpochWithPrecision"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "setBaseURL:"
+ "setBundleID:"
+ "setChallenge:"
+ "setData:"
+ "setDateFormat:"
+ "setDeserializedConfig:"
+ "setEncodedTaskConfig:"
+ "setExtensions:"
+ "setIssuerURL:"
+ "setMaxRetries:"
+ "setReportID:"
+ "setSystemClient:"
+ "setTaskID:"
+ "setToken:"
+ "setTokenFields:"
+ "setTokensDirectoryPath:"
+ "setUploadWithOHTTP:"
+ "setUseOHTTP:"
+ "setWait:"
+ "set_usesNWLoader:"
+ "skipDescendents"
+ "startDownload"
+ "strictOHTTPDisabled"
+ "stringByAppendingFormat:"
+ "stringByAppendingPathComponent:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringFromDate:"
+ "substringToIndex:"
+ "synthesizeWithTokenType:"
+ "taskExpiration"
+ "taskID"
+ "taskIDWithError:"
+ "taskInfoWithError:"
+ "taskProv"
+ "taskProvFromDonation:leaderURL:helperURL:error:"
+ "toBase64URLEncoded:"
+ "token"
+ "token-key"
+ "token-keys"
+ "token-type"
+ "tokenFields"
+ "tokenKey"
+ "tokenType"
+ "tokensDirectoryPath"
+ "unsignedIntegerValue"
+ "unspecified"
+ "updateTokenFileWithTokenArray:inPath:"
+ "uploadDAPPayload:withEncoder:withKeys:useOHTTP:"
+ "uploadPayload:withEncoder:"
+ "uploadWithHTTPBody:withHTTPHeaders:withFullURL:"
+ "uploadWithOHTTP"
+ "useOHTTP"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDownloadTask\"24@\"NSURL\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDownloadTask\"24q32q40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24q32@?40"
+ "v48@0:8@16@24q32q40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionDownloadTask\"24q32q40q48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8@16@24q32q40q48"
+ "vdafType"
+ "vdafTypeFromDonation:error:"
+ "version"
+ "wait"
+ "writeToFile:atomically:"
+ "writeToFile:options:error:"
- "\x01\x13"
- "\x04"
- "\x0f\x04"
- "\x15"
- "#"
- "%@ Not submitting shares"
- "/AppleInternal/Tests/DifferentialPrivacy/DifferentialPrivacy_tests.xctest/"
- "/var/mobile/Library/Logs/ExposureNotification"
- "@\"ENManager\""
- "@\"_DPDediscoKeyConfiguration\""
- "@\"_DPENService\""
- "@\"_DPPrioSubmissionManager\""
- "@20@0:8B16"
- "@40@0:8#16@24#32"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16Q24@32@40@48"
- "@60@0:8@16@24@32@40@48B56"
- "@64@0:8@16@24@32@40@48^@56"
- "Algorithm"
- "Algorithm Parameters"
- "B48@0:8@16^{__SecPolicy=}24@32@40"
- "BAA Signature: '%@'"
- "Certificate validation failed."
- "CountryCode"
- "ENReportsDirectoryPath"
- "Empty metadata provided - fetching current metadata from EN Service"
- "Error while evaluating %@ certificate chain: %@"
- "Exposure Notification Opt-In is turned off, skipping send"
- "Exposure Notification Telemetry Autorization is off, skipping send"
- "Extension data length exceeds 64KB."
- "Failed to create a trust object from %@ certificate chain: %d"
- "Failed to create payload handler for Dedisco V2"
- "Failed to extract public keys from public leaf certificates."
- "Failed to extract subject names from leaf certificates."
- "Failed to fetch EN Config, error: %@"
- "Failed to fetch EN Server Config, error: %@"
- "Failed to fetch EN Server Config, timeout (%lld sec)"
- "Failed to fetch metadata, error: %@"
- "Failed to fetch metadata, timeout (%lld sec)"
- "Failed to obtain EN Config: timeout (%lld sec)"
- "Failed to submit payload because of the error on networking client: %@"
- "Failed to submit payload with error: %@"
- "Failed to submit payload: timeout on client (%lld sec)"
- "Fetched current metadata from EN Service, success: %d"
- "Finished submitting shares successfully"
- "Found EN Config for (\"%@\",\"%@\")"
- "Found EN Server Config for (\"%@\",\"%@\")"
- "Going to submit payload, (length of data: %lu)"
- "Helper encrypted key length exceeds 64KB."
- "Helper encrypted payload length exceeds 4GB."
- "Key"
- "Leader encrypted key length exceeds 64KB."
- "Leader encrypted payload length exceeds 4GB."
- "Malformed batch size parameters in metadata, minimum batch size (%d) should be no larger than maximum batch size (%d)."
- "Malformed batch size parameters in plist, expected numbers."
- "Malformed batch size parameters in plist, minimum batch size (%d) should be no larger than maximum batch size (%d)."
- "Partner"
- "Partner Server Endpoint"
- "Partner Server Public Key"
- "Payload was uploaded successfully"
- "Poplar1AES128"
- "Prio3AES128Count"
- "Prio3AES128Histogram"
- "Prio3AES128Sum"
- "PrioPiRappor"
- "PrioPlusPlus"
- "Public Health Authority"
- "Public Health Authority Server Endpoint"
- "Public Health Authority Server Public Key"
- "PublicHealthAuthority and facilitator can not have the same public key."
- "Shares submission was unsuccessful, error: %@"
- "State"
- "Submitting payload using Networking Client"
- "T#,N,V_certificateValidatorClass"
- "T#,N,V_networkingServiceClass"
- "T@\"ENManager\",&,N,V_enManager"
- "T@\"NSData\",&,N,V_extension"
- "T@\"NSData\",&,N,V_extensionData"
- "T@\"NSData\",&,N,V_nonce"
- "T@\"NSData\",&,N,V_queryConfig"
- "T@\"NSData\",&,N,V_taskId"
- "T@\"NSData\",&,N,V_taskInfo"
- "T@\"NSData\",&,N,V_time"
- "T@\"NSData\",&,N,V_vdafConfig"
- "T@\"NSDictionary\",R,N,V_metadata"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_submissionQueue"
- "T@\"NSString\",&,N,V_collectionID"
- "T@\"NSString\",R,C,N,V_appleTelemetryEndpoint"
- "T@\"NSString\",R,C,N,V_facilitator"
- "T@\"NSString\",R,C,N,V_partnerTelemetryEndpoint"
- "T@\"NSString\",R,C,N,V_partnerTelemetryPublicCertificateChain"
- "T@\"NSString\",R,C,N,V_phaTelemetryEndpoint"
- "T@\"NSString\",R,C,N,V_phaTelemetryPublicCertificateChain"
- "T@\"NSString\",R,C,N,V_publicHealtAuthority"
- "T@\"_DPDediscoKeyConfiguration\",R,N,V_keys"
- "T@\"_DPENService\",&,N,V_enService"
- "T@\"_DPPrioSubmissionManager\",&,N,V_prioManager"
- "T@,R,N,V_publicHealtAuthorityPublicKey"
- "TB,N,V_optInStatus"
- "TB,R,N,V_telemetryAuthorization"
- "The VDAF algorithm type %@ is currently not supported."
- "Unable to encrypt helper share with HPKE."
- "Unable to encrypt leader share with HPKE."
- "Unable to find EN Config for (\"%@\",\"%@\")"
- "Unable to find EN Server Config for (\"%@\",\"%@\")"
- "Unable to get EN config."
- "Unable to get valid EN server config."
- "Unable to serialize upload payload dictionary"
- "Unable to serialize upload payload dictionary, error: %@"
- "Unknown VDAF algorithm type: %@."
- "_DPDediscoPayloadHandler"
- "_DPENCertificateValidator"
- "_DPENCertificateValidatorResult"
- "_DPENConfig"
- "_DPENServerConfig"
- "_DPENService"
- "_DPPrioError"
- "_DPPrioNetworkingService"
- "_DPPrioSubmissionManager"
- "_TtCV19DPSubmissionService14EncryptedWordsP33_797879B5922A3E2ABC74B7FA43CAD23013_StorageClass"
- "_TtCV19DPSubmissionService21EncryptedWordsPayloadP33_797879B5922A3E2ABC74B7FA43CAD23013_StorageClass"
- "_appleTelemetryEndpoint"
- "_certificateValidatorClass"
- "_enManager"
- "_enRegion:matchesCountryCode:subdivisionCode:"
- "_enService"
- "_extension"
- "_extensionData"
- "_facilitator"
- "_networkingServiceClass"
- "_nonce"
- "_optInStatus"
- "_partnerTelemetryEndpoint"
- "_partnerTelemetryPublicCertificateChain"
- "_payload"
- "_phaTelemetryEndpoint"
- "_phaTelemetryPublicCertificateChain"
- "_prioManager"
- "_publicHealtAuthority"
- "_publicHealtAuthorityPublicKey"
- "_queryConfig"
- "_submissionQueue"
- "_taskId"
- "_telemetryAuthorization"
- "_vdafConfig"
- "_words"
- "allRegionConfigurationsWithCompletion:"
- "allRegionServerConfigurationsWithCompletion:"
- "appleTelemetryEndpoint"
- "baaCertificate"
- "baaSignature"
- "certificateValidatorClass"
- "com.apple.DPPrio"
- "com.apple.dpSubmissionService.csQueue"
- "com.apple.dprivacyd.upload"
- "configWithWithOptInStatus:"
- "countryCode"
- "dap-02 input share"
- "differentialPrivacyConsent"
- "differentialPrivacyMetadata"
- "enManager"
- "enService"
- "encodeExtensionDataWithError:"
- "encodeExtensionWithError:"
- "encodeInfoForServerRole:"
- "encodeNonce"
- "encodeQueryConfig"
- "encodeReportWithError:"
- "encodeTaskIdWithError:"
- "encodeTaskInfoWithError:"
- "encodeTime"
- "encodeVDAFConfigWithError:"
- "evaluateCerts:policy:name:overrideVerifyDate:"
- "extension"
- "extensionData"
- "facilitator"
- "fetchConfigForCountryCode:subdivisionCode:"
- "fetchMetadata"
- "fetchServerConfigForCountryCode:subdivisionCode:"
- "getInfoForKey:completion:"
- "handlePrioSubmissionShare1:share2:key:parameters:metadata:error:"
- "histogram"
- "initWithDomain:"
- "initWithDomain:retries:method:tlsTrustPinningPolicyName:defaultHeaders:"
- "initWithNetworkingServiceClass:enService:certificateValidatorClass:"
- "initWithOptInStatus:"
- "initWithPhaTelemetryPublicCertificateChain:partnerTelemetryPublicCertificateChain:appleTelemetryEndpoint:phaTelemetryEndpoint:partnerTelemetryEndpoint:telemetryAuthorization:"
- "initWithPublicHealtAuthority:facilitator:publicHealtAuthorityPublicKey:facilitatorPublicKey:"
- "isEqualToData:"
- "networkingServiceClass"
- "nonce"
- "numberWithDouble:"
- "numberWithUnsignedInt:"
- "optInStatus"
- "partnerEncryptedPacket"
- "partnerPublicKey"
- "partnerTelemetryEndpoint"
- "partnerTelemetryPublicCertificateChain"
- "payload"
- "phaTelemetryEndpoint"
- "phaTelemetryPublicCertificateChain"
- "prepareBAACertificateFromSignature:"
- "prioManager"
- "public health authority"
- "publicHealtAuthority"
- "publicHealtAuthorityPublicKey"
- "publicHealthAuthorityEncryptedPacket"
- "publicHealthAuthorityPublicKey"
- "publicHealthAuthorityTelemetryEndpoint"
- "queryConfig"
- "region"
- "result"
- "serverConfigWithPhaTelemetryPublicCertificateChain:partnerTelemetryPublicCertificateChain:appleTelemetryEndpoint:phaTelemetryEndpoint:partnerTelemetryEndpoint:telemetryAuthorization:"
- "setCertificateValidatorClass:"
- "setCollectionID:"
- "setEnManager:"
- "setEnService:"
- "setExtension:"
- "setExtensionData:"
- "setNetworkingServiceClass:"
- "setNonce:"
- "setOptInStatus:"
- "setPrioManager:"
- "setQueryConfig:"
- "setSubmissionQueue:"
- "setTaskId:"
- "setTaskInfo:"
- "setTime:"
- "setVdafConfig:"
- "set_sourceApplicationSecondaryIdentifier:"
- "subdivisionCode"
- "submissionQueue"
- "submitSyncronouslyWithPayload:signature:"
- "submitToPrioShare1:share2:key:parameters:metadata:withReply:"
- "taskId"
- "telemetryAuthorization"
- "timestamp"
- "unitTestInputDirectoryPath"
- "usePrivacyProxy"
- "userConsent"
- "uuid"
- "v24@0:8#16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@8@\"NSError\"16"
- "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSDictionary\"40@\"NSDictionary\"48@?<v@?B@\"NSError\"@\"NSDictionary\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "validatePublicHealthAuthorityCertificateChain:facilitatorCertificateChain:"
- "validatePublicHealthAuthorityCertificateChain:facilitatorCertificateChain:overrideVerifyDate:"
- "validatorResultWithPublicHealtAuthority:facilitator:publicHealtAuthorityPublicKey:facilitatorPublicKey:"
- "vdafConfig"
- "verifyParamsWithError:"
- "versionConfigHash"
- "words"

```
