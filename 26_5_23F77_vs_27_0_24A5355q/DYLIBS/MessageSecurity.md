## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

```diff

-195.122.4.0.0
-  __TEXT.__text: 0x463a4
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x2284
-  __TEXT.__const: 0x1474
-  __TEXT.__gcc_except_tab: 0x880
-  __TEXT.__cstring: 0x41a7
-  __TEXT.__oslogstring: 0xcec
-  __TEXT.__swift5_typeref: 0x2b8
+330.0.0.0.0
+  __TEXT.__text: 0x4c784
+  __TEXT.__objc_methlist: 0x2434
+  __TEXT.__const: 0x14a4
+  __TEXT.__gcc_except_tab: 0x78c
+  __TEXT.__cstring: 0x4447
+  __TEXT.__oslogstring: 0xebc
+  __TEXT.__swift5_typeref: 0x2b0
+  __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x3f0
   __TEXT.__swift5_reflstr: 0x4e3
   __TEXT.__swift5_fieldmd: 0x58c

   __TEXT.__swift5_types: 0x74
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x11d0
-  __TEXT.__eh_frame: 0x778
-  __TEXT.__objc_classname: 0x3b4
-  __TEXT.__objc_methname: 0x4da1
-  __TEXT.__objc_methtype: 0x1bbe
-  __TEXT.__objc_stubs: 0x33a0
-  __DATA_CONST.__got: 0x3b8
+  __TEXT.__unwind_info: 0x1250
+  __TEXT.__eh_frame: 0x600
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x45c0
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x880
-  __AUTH_CONST.__const: 0x15d8
-  __AUTH_CONST.__cfstring: 0x3600
-  __AUTH_CONST.__objc_const: 0x4bf8
-  __AUTH.__objc_data: 0x188
-  __DATA.__objc_ivar: 0x210
-  __DATA.__data: 0x1230
-  __DATA.__bss: 0x8a0
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__got: 0x3d0
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x3780
+  __AUTH_CONST.__objc_const: 0x4e38
+  __AUTH_CONST.__auth_got: 0x948
+  __AUTH.__objc_data: 0x98
+  __DATA.__objc_ivar: 0x234
+  __DATA.__data: 0x1228
+  __DATA.__bss: 0x8e0
   __DATA.__common: 0x2711
-  __DATA_DIRTY.__objc_data: 0xad0
+  __DATA_DIRTY.__objc_data: 0xc10
   __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x30
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C726BBC7-6E56-31E5-B076-351A51CDD141
-  Functions: 2165
-  Symbols:   4949
-  CStrings:  2017
+  UUID: 5F288AC0-D271-35A4-8E3B-0D9EB310BB0A
+  Functions: 2219
+  Symbols:   5163
+  CStrings:  1051
 
Symbols:
+ +[MSOID HybridSignatureOIDWithDigestAlgorithm:error:]
+ -[MSCMSAppleTimestampAttribute .cxx_destruct]
+ -[MSCMSAppleTimestampAttribute certificates]
+ -[MSCMSAppleTimestampAttribute digestAlgorithm]
+ -[MSCMSAppleTimestampAttribute encodeAttributeWithError:]
+ -[MSCMSAppleTimestampAttribute initWithAttribute:error:]
+ -[MSCMSAppleTimestampAttribute initWithTimestampToken:]
+ -[MSCMSAppleTimestampAttribute rawTimestampTokenData]
+ -[MSCMSAppleTimestampAttribute setRawTimestampTokenData:]
+ -[MSCMSAppleTimestampAttribute timestampResponse]
+ -[MSCMSAppleTimestampAttribute timestampResponse].cold.1
+ -[MSCMSAppleTimestampAttribute verifyTimestamps:error:]
+ -[MSCMSAppleTimestampAttribute verifyWithSignerInfo:policies:error:]
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:].cold.4
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:].cold.5
+ -[MSCMSTimestampAttribute signerInfo]
+ -[MSOID initHybridSignatureOIDWithDigestAlgorithm:error:]
+ -[MSOID initHybridSignatureOIDWithDigestAlgorithm:error:].cold.1
+ -[MSTimestampRequest fetchStartTime]
+ -[MSTimestampRequest fetchTimestampWithError:].cold.1
+ -[MSTimestampRequest finishAsyncFetch:error:onQueue:completion:]
+ -[MSTimestampRequest firstRetryErrorCode]
+ -[MSTimestampRequest invalidateXPCSession]
+ -[MSTimestampRequest isRetryableError:]
+ -[MSTimestampRequest maxRetryAttempts]
+ -[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:]
+ -[MSTimestampRequest performSingleSyncFetchAttempt:]
+ -[MSTimestampRequest retryCount]
+ -[MSTimestampRequest retryDelayForAttempt:]
+ -[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:error:samplingRate:]
+ -[MSTimestampRequest setFetchStartTime:]
+ -[MSTimestampRequest setFirstRetryErrorCode:]
+ -[MSTimestampRequest setMaxRetryAttempts:]
+ -[MSTimestampRequest setRetryCount:]
+ -[MSTimestampResponse certificateHasTimeStampingEKU:]
+ -[MSTimestampResponse certificates]
+ -[MSTimestampResponse initWithTimestampToken:]
+ -[MSTimestampResponse initWithTimestampToken:].cold.1
+ -[MSTimestampResponse initWithTimestampToken:].cold.2
+ -[MSTimestampResponse setCertificates:]
+ -[MSTimestampResponse setTimeStampTokenData:]
+ -[MSTimestampResponse signingCertificate]
+ -[MSTimestampResponse signingCertificate].cold.1
+ -[MSTimestampResponse signingCertificate].cold.2
+ -[MSTimestampResponse signingCertificate].cold.3
+ -[MSTimestampResponse timeStampTokenData]
+ -[MSTimestampResponse verifyWithMessageImprint:policies:error:]
+ -[MSTimestampResponse verifyWithRequest:policies:error:]
+ GCC_except_table2
+ GCC_except_table41
+ GCC_except_table44
+ _MSSignatureAlgorithmHybridSig_MLDSA87_RSA3072PSS_SHA512
+ _MSSignatureAlgorithmHybridSig_MLDSA87_RSA3072PSS_SHA512_draft_13
+ _MSTimestampHTTPErrorDomain
+ _OBJC_CLASS_$_MSCMSAppleTimestampAttribute
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_MSCMSAppleTimestampAttribute._cachedTimestampResponse
+ _OBJC_IVAR_$_MSCMSAppleTimestampAttribute._rawTimestampTokenData
+ _OBJC_IVAR_$_MSCMSAppleTimestampAttribute._timestampResponseParsed
+ _OBJC_IVAR_$_MSCMSTimestampAttribute._signerInfo
+ _OBJC_IVAR_$_MSTimestampRequest._fetchStartTime
+ _OBJC_IVAR_$_MSTimestampRequest._firstRetryErrorCode
+ _OBJC_IVAR_$_MSTimestampRequest._maxRetryAttempts
+ _OBJC_IVAR_$_MSTimestampRequest._retryCount
+ _OBJC_IVAR_$_MSTimestampResponse._certificates
+ _OBJC_IVAR_$_MSTimestampResponse._timeStampTokenData
+ _OBJC_METACLASS_$_MSCMSAppleTimestampAttribute
+ _SecCertificateCopyExtendedKeyUsage
+ __OBJC_$_INSTANCE_METHODS_MSCMSAppleTimestampAttribute
+ __OBJC_$_INSTANCE_VARIABLES_MSCMSAppleTimestampAttribute
+ __OBJC_$_PROP_LIST_MSCMSAppleTimestampAttribute
+ __OBJC_CLASS_RO_$_MSCMSAppleTimestampAttribute
+ __OBJC_METACLASS_RO_$_MSCMSAppleTimestampAttribute
+ ___108-[MSCMSSignerInfo verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:]_block_invoke.93
+ ___28-[MSTimestampResponse init:]_block_invoke.403
+ ___35-[MSCMSSignerInfo verifySignature:]_block_invoke.69
+ ___41-[MSTimestampResponse signingCertificate]_block_invoke
+ ___41-[MSTimestampResponse signingCertificate]_block_invoke.518
+ ___41-[MSTimestampResponse signingCertificate]_block_invoke.521
+ ___42-[MSCMSSignerInfo verifyTimestamps:error:]_block_invoke.102
+ ___43-[MSCMSSignerInfo verifyCountersignatures:]_block_invoke.83
+ ___43-[MSTimestampRequest buildTimestampRequest]_block_invoke.47
+ ___46-[MSTimestampRequest fetchTimestampWithError:]_block_invoke
+ ___46-[MSTimestampResponse initWithTimestampToken:]_block_invoke
+ ___46-[MSTimestampResponse initWithTimestampToken:]_block_invoke.408
+ ___49-[MSCMSAppleTimestampAttribute timestampResponse]_block_invoke
+ ___57-[MSOID initHybridSignatureOIDWithDigestAlgorithm:error:]_block_invoke
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke.120
+ ___64-[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:]_block_invoke_4
+ ___64-[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:error:]_block_invoke_5
+ ___64-[MSTimestampRequest finishAsyncFetch:error:onQueue:completion:]_block_invoke
+ ___78-[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:]_block_invoke
+ ___78-[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:]_block_invoke.116
+ ___78-[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:]_block_invoke.cold.1
+ ___78-[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:]_block_invoke_2
+ ___82-[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:error:samplingRate:]_block_invoke
+ ___block_descriptor_49_e8_32s40s_e30_"NSObject<OS_xpc_object>"8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e61_v24?0"NSObject<OS_xpc_object>"8"NSObject<OS_xpc_object>"16ls32l8s40l8s48l8
+ ___block_literal_global.107
+ ___block_literal_global.115
+ ___block_literal_global.122
+ ___block_literal_global.142
+ ___block_literal_global.146
+ ___block_literal_global.17
+ ___block_literal_global.183
+ ___block_literal_global.188
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.197
+ ___block_literal_global.356
+ ___block_literal_global.37
+ ___block_literal_global.401
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.410
+ ___block_literal_global.425
+ ___block_literal_global.504
+ ___block_literal_global.515
+ ___block_literal_global.517
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.65
+ ___block_literal_global.71
+ ___block_literal_global.753
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.89
+ ___block_literal_global.92
+ ___block_literal_global.98
+ ___findBestMutuallySupportedHybridSignatureAlgorithm_block_invoke
+ ___swift__destructor
+ _arc4random
+ _dispatch_after
+ _dispatch_time
+ _exp2
+ _findBestMutuallySupportedHybridSignatureAlgorithm.hybridPreferences
+ _findBestMutuallySupportedHybridSignatureAlgorithm.onceToken
+ _findBestMutuallySupportedSignatureAlgorithm.cold.3
+ _initHybridSignatureOIDWithDigestAlgorithm:error:.onceToken
+ _initHybridSignatureOIDWithDigestAlgorithm:error:.sDigAlgToSigAlg
+ _initWithCertificate:signatureAlgorithm:error:.onceToken.11
+ _initWithCertificate:signatureAlgorithm:error:.onceToken.7
+ _initWithCertificate:signatureAlgorithm:error:.sAllowedHybridSigAlgs
+ _initWithCertificate:signatureAlgorithm:error:.sAllowedHybridSigAlgs.10
+ _kMSAppleTimestampDomain
+ _kMSAppleTimestampEndpoint_tsa_mldsa87_rsa3072_pss_sha512
+ _kSecKeyAlgorithmHybridSigSignatureDigest
+ _kSecKeyAlgorithmHybridSigSignatureMessage
+ _memset
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$certificateHasTimeStampingEKU:
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$fetchStartTime
+ _objc_msgSend$finishAsyncFetch:error:onQueue:completion:
+ _objc_msgSend$firstObject
+ _objc_msgSend$firstRetryErrorCode
+ _objc_msgSend$initHybridSignatureOIDWithDigestAlgorithm:error:
+ _objc_msgSend$initWithTimestampToken:
+ _objc_msgSend$invalidateXPCSession
+ _objc_msgSend$isRetryableError:
+ _objc_msgSend$maxRetryAttempts
+ _objc_msgSend$performAsyncFetchAttempt:maxAttempts:onQueue:completion:
+ _objc_msgSend$performSingleSyncFetchAttempt:
+ _objc_msgSend$rawTimestampTokenData
+ _objc_msgSend$retryCount
+ _objc_msgSend$retryDelayForAttempt:
+ _objc_msgSend$sendTimestampFetchAnalyticsEvent:success:error:samplingRate:
+ _objc_msgSend$setFetchStartTime:
+ _objc_msgSend$setFirstRetryErrorCode:
+ _objc_msgSend$setRawTimestampTokenData:
+ _objc_msgSend$setRetryCount:
+ _objc_msgSend$setTimeStampTokenData:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeStampTokenData
+ _objc_msgSend$userInfo
+ _objc_msgSend$verifyWithMessageImprint:policies:error:
+ _objc_msgSend$verifyWithRequest:policies:error:
+ _objc_msgSend$xpcQueue
+ _objc_retain_x5
+ _swift_deallocObject
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
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _xpc_dictionary_set_int64
- -[MSCMSTimestampAttribute singerInfo]
- -[MSTimestampRequest handleXPCReply:onQueue:completion:]
- -[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:]
- GCC_except_table13
- GCC_except_table20
- GCC_except_table39
- _OBJC_IVAR_$_MSCMSTimestampAttribute._singerInfo
- _OUTLINED_FUNCTION_10
- ___108-[MSCMSSignerInfo verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:]_block_invoke.86
- ___28-[MSTimestampResponse init:]_block_invoke.350
- ___35-[MSCMSSignerInfo verifySignature:]_block_invoke.62
- ___42-[MSCMSSignerInfo verifyTimestamps:error:]_block_invoke.95
- ___43-[MSCMSSignerInfo verifyCountersignatures:]_block_invoke.76
- ___43-[MSTimestampRequest buildTimestampRequest]_block_invoke.28
- ___56-[MSTimestampRequest handleXPCReply:onQueue:completion:]_block_invoke
- ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke.95
- ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke.98
- ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_2
- ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_3
- ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_4
- ___63-[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:]_block_invoke
- ___block_descriptor_41_e8_32s_e30_"NSObject<OS_xpc_object>"8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56w_e61_v24?0"NSObject<OS_xpc_object>"8"NSObject<OS_xpc_object>"16ls32l8w56l8s48l8s40l8
- ___block_literal_global.135
- ___block_literal_global.147
- ___block_literal_global.178
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.189
- ___block_literal_global.348
- ___block_literal_global.352
- ___block_literal_global.357
- ___block_literal_global.367
- ___block_literal_global.446
- ___block_literal_global.457
- ___block_literal_global.58
- ___block_literal_global.670
- ___block_literal_global.70
- ___block_literal_global.75
- ___block_literal_global.80
- ___block_literal_global.85
- ___block_literal_global.86
- ___block_literal_global.91
- ___block_literal_global.94
- ___block_literal_global.97
- _objc_copyWeak
- _objc_initWeak
- _objc_msgSend$handleXPCReply:onQueue:completion:
- _objc_msgSend$sendTimestampFetchAnalyticsEvent:success:
- _objc_retain_x28
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _symbolic SS_ypt
CStrings:
+ "1.3.6.1.5.5.7.3.8"
+ "1.3.6.1.5.5.7.6.52"
+ "2.16.840.1.114027.80.9.1.15"
+ "Failed to create message imprint for timestamp verification"
+ "Failed to decode timestamp token as MSTimestampResponse"
+ "MSCMSAppleTimestampAttribute: failed to create MSTimestampResponse from token data"
+ "MSCMSAppleTimestampAttribute: no timestamp token data to encode"
+ "MSTimestampHTTPErrorDomain"
+ "MSTimestampRequest: Retryable error (attempt %ld/%ld): %@"
+ "MSTimestampResponse initWithTimestampToken: Cannot initialize with nil token data"
+ "MSTimestampResponse initWithTimestampToken: failed to parse token: %@"
+ "No certificate with id-kp-timeStamping EKU found in certificate chain"
+ "TimeStampToken has multiple signers (%lu), RFC 3161 requires exactly one"
+ "TimeStampToken has no signers"
+ "Timestamp response is missing message imprint or algorithm"
+ "elapsed_ms"
+ "error_code"
+ "first_error_code"
+ "https://timestamp.apple.com/tsa-mldsa87-rsa3072-pss-sha512"
+ "id-aa-timeStampToken attribute has %lu values, expected 1"
+ "retry_count"
+ "timeStampTokenData"
+ "timestamp.apple.com"
+ "underlyingErrorCode"
+ "underlyingErrorDomain"
+ "underlying_error_code"
+ "underlying_error_domain"
- "#16@0:8"
- ".cxx_destruct"
- "?"
- "@\"<MSCMSAttributeCoder>\"32@0:8@\"MSCMSAttribute\"16^@24"
- "@\"<MSCMSMessage>\""
- "@\"<MSCMSMessage>\"16@0:8"
- "@\"MSAlgorithmIdentifier\""
- "@\"MSCMSAttribute\"24@0:8^@16"
- "@\"MSCMSMutableAttributeArray\""
- "@\"MSCMSSignedData\""
- "@\"MSCMSSignerInfo\""
- "@\"MSCMSTimestampAttributeInternal\""
- "@\"MSDecodeOptions\""
- "@\"MSMessageImprint\""
- "@\"MSOID\""
- "@\"MSOID\"16@0:8"
- "@\"MSPKIStatusInfo\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSData\"24@0:8^@16"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_session>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{GeneralName=i(?={GeneralName_otherName={heim_oid=Q^I}{heim_base_data=Q^v}}{heim_base_data=Q^v}{heim_base_data=Q^v}{GeneralName_directoryName=i(?={RDNSequence=I^{RelativeDistinguishedName}})}{heim_base_data=Q^v}{heim_base_data=Q^v}{heim_oid=Q^I})}16"
- "@24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16"
- "@24@0:8^{__SecCertificate=}16"
- "@24@0:8^{__SecIdentity=}16"
- "@28@0:8@16B24"
- "@28@0:8^{__SecCertificate=}16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16^@24"
- "@32@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16^@24"
- "@32@0:8^{__CFString=}16^@24"
- "@32@0:8^{__SecCertificate=}16@24"
- "@32@0:8^{__SecCertificate=}16^@24"
- "@32@0:8^{__SecIdentity=}16^@24"
- "@32@0:8^{heim_base_data=Q^v}16^@24"
- "@32@0:8^{heim_oid=Q^I}16^@24"
- "@36@0:8@16@24B32"
- "@36@0:8@16I24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@\"NSData\"16@\"MSDecodeOptions\"24^@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24^{heim_base_data=Q^v}32"
- "@40@0:8@16Q24@32"
- "@40@0:8^{__SecCertificate=}16@24@32"
- "@40@0:8^{__SecCertificate=}16@24^@32"
- "@40@0:8^{__SecCertificate=}16@24^{__SecIdentity=}32"
- "@40@0:8^{__SecIdentity=}16@24^@32"
- "@44@0:8@16B24@28^@36"
- "@44@0:8^{__SecCertificate=}16@24B32^@36"
- "@44@0:8^{__SecIdentity=}16@24B32^@36"
- "@44@0:8q16@24q32B40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24Q32^@40"
- "@48@0:8@16q24@32@40"
- "@48@0:8^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}{heim_base_data=Q^v}{OriginatorPublicKey={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_bit_string=Q^v}})}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{RecipientEncryptedKeys=I^{RecipientEncryptedKey}}})}16@24@32^@40"
- "@48@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@24@32^@40"
- "@48@0:8^{__SecCertificate=}16@24@32^{__SecIdentity=}40"
- "@52@0:8@16B24@28@36^@44"
- "@52@0:8@16B24@28Q36^@44"
- "@52@0:8I16I20I24@28@36^@44"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8@16q24Q32@40@48"
- "@64@0:8@16q24Q32@40@48*56"
- "Asn1OID"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "B32@0:8@16^@24"
- "B32@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16^@24"
- "B32@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8@16^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}{heim_base_data=Q^v}{OriginatorPublicKey={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_bit_string=Q^v}})}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{RecipientEncryptedKeys=I^{RecipientEncryptedKey}}})}24^@32"
- "B48@0:8@16@24@32^@40"
- "B56@0:8@16@24@32@40^@48"
- "ECSignatureOIDWithDigestAlgorithm:error:"
- "I24@0:8^@16"
- "LAContext"
- "MSAlgorithmIdentifier"
- "MSCMSAppleExpirationTimeAttribute"
- "MSCMSAppleHashAgilityAttribute"
- "MSCMSAppleHashAgilityV2Attribute"
- "MSCMSAttribute"
- "MSCMSAttributeCoder"
- "MSCMSAuthEnvelopedData"
- "MSCMSCompressedData"
- "MSCMSContentInfo"
- "MSCMSContentTypeAttribute"
- "MSCMSCounterSignerInfo"
- "MSCMSCountersignatureAttribute"
- "MSCMSEncryptionKeyPreferenceAttribute"
- "MSCMSEnvelopedData"
- "MSCMSEnvelopedDataInternal"
- "MSCMSIdentifier"
- "MSCMSMessage"
- "MSCMSMessageDigestAttribute"
- "MSCMSMultipleSignaturesAttribute"
- "MSCMSMutableAttributeArray"
- "MSCMSRecipientInfo"
- "MSCMSSMIMECapabilitiesAttribute"
- "MSCMSSignedData"
- "MSCMSSignerInfo"
- "MSCMSSigningTimeAttribute"
- "MSCMSTimestampAttribute"
- "MSCMSTimestampAttributeInternal"
- "MSDecodeOptions"
- "MSError"
- "MSErrorWithDomain:code:errorLevel:underlyingError:description:"
- "MSErrorWithDomain:code:errorLevel:underlyingError:description:arguments:"
- "MSErrorWithDomain:code:underlyingError:description:"
- "MSMessageImprint"
- "MSOID"
- "MSPKIStatusInfo"
- "MSTimestampRequest"
- "MSTimestampResponse"
- "MessageSecurityHexRepresentation"
- "MessageSecurityMessage"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "OIDBytes"
- "OIDString"
- "OIDWithAsn1OID:error:"
- "OIDWithData:error:"
- "OIDWithString:error:"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8^@16"
- "RSASignatureOIDWithDigestAlgorithm:error:"
- "T#,R"
- "T@\"<MSCMSMessage>\",&"
- "T@\"<MSCMSMessage>\",&,V_embeddedContent"
- "T@\"<MSCMSMessage>\",N,&,VembeddedContent"
- "T@\"MSAlgorithmIdentifier\",&,N,V_bodyHashAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,N,V_signatureAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,N,V_signedAttrsHashAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,V_algorithmIdentifier"
- "T@\"MSAlgorithmIdentifier\",&,V_digestAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,V_encryptionAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,V_keyEncryptionAlgorithm"
- "T@\"MSAlgorithmIdentifier\",&,V_signatureAlgorithm"
- "T@\"MSCMSMutableAttributeArray\",&,V_protectedAttributes"
- "T@\"MSCMSMutableAttributeArray\",&,V_unprotectedAttributes"
- "T@\"MSCMSSignedData\",&,V_timeStampToken"
- "T@\"MSCMSSignedData\",W,V_containingSignedData"
- "T@\"MSCMSSignerInfo\",R,V_singerInfo"
- "T@\"MSCMSSignerInfo\",W,N,V_containingSignerInfo"
- "T@\"MSCMSTimestampAttributeInternal\",&,V_timestampAttribute"
- "T@\"MSDecodeOptions\",&,V_options"
- "T@\"MSMessageImprint\",&,V_messageImprint"
- "T@\"MSOID\",&"
- "T@\"MSOID\",&,V_contentType"
- "T@\"MSOID\",&,V_reqPolicyID"
- "T@\"MSOID\",&,V_tsaPolicyID"
- "T@\"MSOID\",N,&,VattributeType"
- "T@\"MSOID\",N,&,VcontentType"
- "T@\"MSOID\",N,&,VencryptionAlgorithm"
- "T@\"MSOID\",N,&,Vtype"
- "T@\"MSOID\",R"
- "T@\"MSOID\",R,&"
- "T@\"MSOID\",R,&,V_attributeType"
- "T@\"MSOID\",R,V_algorithm"
- "T@\"MSOID\",R,V_digestAlgorithm"
- "T@\"MSOID\",R,V_type"
- "T@\"MSPKIStatusInfo\",&,V_status"
- "T@\"NSArray\",&,V_additionalCertificates"
- "T@\"NSArray\",&,V_algorithmCapabilities"
- "T@\"NSArray\",&,V_anchorCertificates"
- "T@\"NSArray\",&,V_encryptedKeys"
- "T@\"NSArray\",&,V_recipientCertificates"
- "T@\"NSArray\",&,V_recipients"
- "T@\"NSArray\",&,V_signerPolicies"
- "T@\"NSArray\",&,V_signers"
- "T@\"NSArray\",N,C"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,&,V_attributeValues"
- "T@\"NSArray\",R,V_certificates"
- "T@\"NSArray\",R,V_signers"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_dataContent"
- "T@\"NSData\",&,N,V_signature"
- "T@\"NSData\",&,V_LAContext"
- "T@\"NSData\",&,V_attributeDERData"
- "T@\"NSData\",&,V_content"
- "T@\"NSData\",&,V_encodedAttributeSet"
- "T@\"NSData\",&,V_encryptedContent"
- "T@\"NSData\",&,V_encryptionKey"
- "T@\"NSData\",&,V_hashedMessage"
- "T@\"NSData\",&,V_identifierData"
- "T@\"NSData\",&,V_issuerNameData"
- "T@\"NSData\",&,V_key"
- "T@\"NSData\",&,V_messageDigest"
- "T@\"NSData\",&,V_nonce"
- "T@\"NSData\",&,V_originatorPubKey"
- "T@\"NSData\",&,V_serialNumber"
- "T@\"NSData\",&,V_serialNumberData"
- "T@\"NSData\",&,V_signedAttrsData"
- "T@\"NSData\",&,V_skidData"
- "T@\"NSData\",&,V_timestampRequest"
- "T@\"NSData\",&,V_timestampResponse"
- "T@\"NSData\",&,V_unsignedAttrsData"
- "T@\"NSData\",&,V_userKeyingMaterial"
- "T@\"NSData\",N,C"
- "T@\"NSData\",R,&,V_hashAgilityValue"
- "T@\"NSData\",R,V_OIDBytes"
- "T@\"NSData\",R,V_parameters"
- "T@\"NSData\",W,N,V_signedAttrsHash"
- "T@\"NSDate\",&,V_timestamp"
- "T@\"NSDate\",&,V_verifyTime"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,&,V_expirationTime"
- "T@\"NSDate\",R,&,V_signingTime"
- "T@\"NSDictionary\",R,&,V_hashAgilityValues"
- "T@\"NSMutableArray\",&,V_attributes"
- "T@\"NSMutableArray\",&,V_genericAttributes"
- "T@\"NSMutableArray\",&,V_originatorCertificates"
- "T@\"NSMutableArray\",&,V_unprotectedAttributes"
- "T@\"NSMutableSet\",&,V_certificates"
- "T@\"NSNumber\",&,V_version"
- "T@\"NSNumber\",R,V_version"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_xpcQueue"
- "T@\"NSObject<OS_xpc_session>\",&,V_xpcSession"
- "T@\"NSSet\",&,V_digestAlgorithms"
- "T@\"NSSet\",R,V_capabilities"
- "T@\"NSString\",&,V_tsa"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_OIDString"
- "T@\"NSString\",R,V_statusString"
- "T@\"NSURL\",&,V_serverURL"
- "T@\"NSURL\",&,V_timestampServer"
- "TB,R"
- "TB,R,V_hasFailInfo"
- "TB,R,V_signatureCalculated"
- "TB,V_certChainRequested"
- "TB,V_certReq"
- "TB,V_contentChanged"
- "TB,V_detached"
- "TB,V_legacyASN1Encoding"
- "TB,V_useIssuerAndSerialNumber"
- "TB,V_verifySignatures"
- "TB,V_verifySigners"
- "TB,V_verifyTimestamps"
- "TQ,R"
- "TQ,V_chainMode"
- "T^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}},R,V_asn1AlgId"
- "T^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}},V_encodedAttribute"
- "T^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}},V_issuerAndSerialNumber"
- "T^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}},V_encodedSignerInfo"
- "T^{__CFString=},R"
- "T^{__SecCertificate=},N,V_originator"
- "T^{__SecCertificate=},N,V_recipientCertificate"
- "T^{__SecCertificate=},R,V_encryptionCertificate"
- "T^{__SecCertificate=},V_signerCertificate"
- "T^{__SecIdentity=},N,V_originatorIdentity"
- "T^{__SecIdentity=},V_identity"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_signerPrivKey"
- "T^{heim_base_data=Q^v},V_subjectKeyId"
- "Ti,V_type"
- "Tq,R,V_failInfo"
- "Tq,R,V_status"
- "Tq,V_version"
- "Tr^{ccdigest_info=QQQQ*^v^?^?i^?},R"
- "T{heim_oid=Q^I},R,V_Asn1OID"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}"
- "^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16@0:8"
- "^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}"
- "^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16@0:8"
- "^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}"
- "^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16@0:8"
- "^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}"
- "^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFData=}24@0:8@16"
- "^{__CFData=}32@0:8@16B24B28"
- "^{__CFString=}16@0:8"
- "^{__SecCertificate=}"
- "^{__SecCertificate=}16@0:8"
- "^{__SecCertificate=}32@0:8Q16^@24"
- "^{__SecIdentity=}"
- "^{__SecIdentity=}16@0:8"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
- "^{__SecTrust=}32@0:8@16^@24"
- "^{__SecTrust=}48@0:8@16@24@32^@40"
- "^{heim_base_data=Q^v}"
- "^{heim_base_data=Q^v}16@0:8"
- "_Asn1OID"
- "_LAContext"
- "_OIDBytes"
- "_OIDString"
- "_additionalCertificates"
- "_algorithm"
- "_algorithmCapabilities"
- "_algorithmIdentifier"
- "_anchorCertificates"
- "_asn1AlgId"
- "_attributeDERData"
- "_attributeType"
- "_attributeValues"
- "_attributes"
- "_bodyHashAlgorithm"
- "_capabilities"
- "_certChainRequested"
- "_certReq"
- "_certificates"
- "_chainMode"
- "_containingSignedData"
- "_containingSignerInfo"
- "_content"
- "_contentChanged"
- "_contentType"
- "_dataContent"
- "_detached"
- "_digestAlgorithm"
- "_digestAlgorithms"
- "_embeddedContent"
- "_encodedAttribute"
- "_encodedAttributeSet"
- "_encodedSignerInfo"
- "_encryptedContent"
- "_encryptedKeys"
- "_encryptionAlgorithm"
- "_encryptionCertificate"
- "_encryptionKey"
- "_expirationTime"
- "_failInfo"
- "_genericAttributes"
- "_hasFailInfo"
- "_hashAgilityValue"
- "_hashAgilityValues"
- "_hashedMessage"
- "_identifierData"
- "_identity"
- "_issuerAndSerialNumber"
- "_issuerNameData"
- "_key"
- "_keyEncryptionAlgorithm"
- "_legacyASN1Encoding"
- "_messageDigest"
- "_messageImprint"
- "_nonce"
- "_options"
- "_originator"
- "_originatorCertificates"
- "_originatorIdentity"
- "_originatorPubKey"
- "_parameters"
- "_protectedAttributes"
- "_recipientCertificate"
- "_recipientCertificates"
- "_recipients"
- "_reqPolicyID"
- "_serialNumber"
- "_serialNumberData"
- "_serverURL"
- "_signature"
- "_signatureAlgorithm"
- "_signatureCalculated"
- "_signedAttrsData"
- "_signedAttrsHash"
- "_signedAttrsHashAlgorithm"
- "_signerCertificate"
- "_signerPolicies"
- "_signerPrivKey"
- "_signers"
- "_signingTime"
- "_singerInfo"
- "_skidData"
- "_status"
- "_statusString"
- "_subjectKeyId"
- "_timeStampToken"
- "_timestamp"
- "_timestampAttribute"
- "_timestampRequest"
- "_timestampResponse"
- "_timestampServer"
- "_tsa"
- "_tsaPolicyID"
- "_type"
- "_unprotectedAttributes"
- "_unsignedAttrsData"
- "_useIssuerAndSerialNumber"
- "_userKeyingMaterial"
- "_verifySignatures"
- "_verifySigners"
- "_verifyTime"
- "_verifyTimestamps"
- "_version"
- "_xpcQueue"
- "_xpcSession"
- "absoluteString"
- "addCertificatesForSigner:mode:error:"
- "addCounterSignerAttribute:"
- "addCounterSignerCertificates:mode:error:"
- "addDigestAlgorithmFromSigner:"
- "addIndex:"
- "addMultipleSignaturesAttribute"
- "addObject:"
- "addObjectsFromArray:"
- "addProtectedAttribute:"
- "addRecipient:"
- "addRecipient:error:"
- "addSMIMECapabilitiesAttribute:"
- "addSMIMEEncryptionKeyPreferenceAttribute:"
- "addSigner:"
- "addSigner:withCertificates:"
- "addSigner:withChainMode:error:"
- "addUnprotectedAttribute:"
- "additionalCertificates"
- "algorithm"
- "algorithmCapabilities"
- "algorithmIdentifier"
- "algorithmIdentifierWithAsn1AlgId:error:"
- "algorithmIdentifierWithOID:"
- "allObjects"
- "anchorCertificates"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "asMessageSecurityHexString"
- "asn1AlgId"
- "attributeDERData"
- "attributeType"
- "attributeValues"
- "attributes"
- "autorelease"
- "blockSize:"
- "bodyHashAlgorithm"
- "boolValue"
- "buildMessageImprintForASN1:error:"
- "buildTimestampRequest"
- "bulkEncryptDecrypt:algorithm:mode:key:iv:error:"
- "bytes"
- "cString"
- "calculateAttributesWithDigest:error:"
- "calculateContentDigestWithAlgorithm:error:"
- "calculateSignatureDigestWithAlgorithm:error:"
- "calculateSignedAttributesDigest:"
- "calculateSignerInfoDigest:"
- "capabilities"
- "caseInsensitiveCompare:"
- "ccAlgorithm:"
- "ccMode:"
- "ccdigest"
- "certChainRequested"
- "certificates"
- "chainMode"
- "characterSetWithCharactersInString:"
- "checkDecryptionResult:"
- "checkSignedPerRFC5652:"
- "class"
- "cleanupMessageImprint:"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "containingSignedData"
- "containingSignerInfo"
- "containsObject:"
- "content"
- "contentChanged"
- "contentType"
- "contentTypeAttributeWithOID:"
- "copy"
- "copyAttributeData:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAttributeArrayFromAttributeSetRaw:error:"
- "createRequiredAttributes:"
- "createSecCMSSharedInfo:"
- "createSharedInfo:"
- "createTrustObjectWithPolicies:error:"
- "createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:"
- "createXPCMessageForTimestampFetch"
- "data"
- "dataContent"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithData:"
- "dataWithLength:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decimalDigitCharacterSet"
- "decode:error:"
- "decodeAttribute:error:"
- "decodeBoolForKey:"
- "decodeIdentifier:error:"
- "decodeIntegerForKey:"
- "decodeKeyAgreeRecipientInfo:certificates:LAContext:error:"
- "decodeKeyTransRecipientInfo:certificates:LAContext:error:"
- "decodeMessageSecurityObject:options:error:"
- "decodeObjectOfClass:forKey:"
- "decodeRecipientInfo:certificates:LAContext:error:"
- "decodeSignerInfo:certificates:LAContext:error:"
- "decryptContent:error:"
- "decryptWrappedKey:kek:iv:"
- "description"
- "detached"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "digestAlgorithm"
- "digestAlgorithmWithSignatureAlgorithm:error:"
- "digestAlgorithms"
- "digestOIDWithSignatureAlgorithm:error:"
- "embeddedContent"
- "encode"
- "encodeAttributeWithError:"
- "encodeAttributesWithError:"
- "encodeBool:forKey:"
- "encodeEncryptionParameters:"
- "encodeImplicitAttributesWithError:"
- "encodeInteger:forKey:"
- "encodeKeyAgreeRecipientInfo:recipientInfo:error:"
- "encodeKeyTransRecipientInfo:recipientInfo:error:"
- "encodeMessageSecurityObject:"
- "encodeObject:forKey:"
- "encodeOriginatorInfoCertificates:error:"
- "encodeRecipientInfo:recipientInfo:error:"
- "encodeSignerInfo:error:"
- "encodeWithCoder:"
- "encodedAttribute"
- "encodedAttributeSet"
- "encodedSignerInfo"
- "encryptBulkKey:"
- "encryptContent:"
- "encryptDecryptContent:ccOperation:error:"
- "encryptedContent"
- "encryptedKeys"
- "encryptionAlgorithm"
- "encryptionCertificate"
- "encryptionKey"
- "ensureXPCSessionExists:"
- "enumerateObjectsAtIndexes:options:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "envelopedData"
- "errorWithDomain:code:userInfo:"
- "expectedHashLength:"
- "expirationTime"
- "fetchTimestampWithCompletionBlock:queue:"
- "fetchTimestampWithError:"
- "findBestEncryptionAlgorithmForNewRecipient:"
- "freeKeyTransRecipientInfo:"
- "freeRecipientInfo:"
- "generateAttributeStruct"
- "generateEncryptionKey:"
- "genericAttributes"
- "getAttributesWithOID:"
- "getAttributesWithType:"
- "getAttributesWithType:protectedAttributes:"
- "getCharacters:range:"
- "getRecipients"
- "getSignerCertificate:error:"
- "handleXPCReply:onQueue:completion:"
- "hash"
- "hashAgilityValue"
- "hashAgilityValues"
- "i"
- "i16@0:8"
- "identifierData"
- "identity"
- "indexOfObjectPassingTest:"
- "indexSet"
- "indexesOfObjectsPassingTest:"
- "init"
- "init:"
- "init:hashedMessage:"
- "init:server:"
- "init:server:nonce:"
- "initCertsOnlyWithCertificates:error:"
- "initDigestAlgorithmWithSignatureAlgorithm:error:"
- "initDigestOIDWithSignatureAlgorithm:error:"
- "initECSignatureOIDWithDigestAlgorithm:error:"
- "initRSASignatureOIDWithDigestAlgorithm:error:"
- "initSignatureOIDWithSecKeyAlgorithm:error:"
- "initWithAsn1AlgId:error:"
- "initWithAsn1OID:error:"
- "initWithAttribute:LAContext:error:"
- "initWithAttribute:certificates:LAContext:containingSignerInfo:error:"
- "initWithAttribute:certificates:LAContext:error:"
- "initWithAttribute:error:"
- "initWithAttributeStruct:error:"
- "initWithAttributeType:values:"
- "initWithBytes:length:"
- "initWithBytes:length:encoding:"
- "initWithCapabilities:"
- "initWithCapacity:"
- "initWithCertificate:"
- "initWithCertificate:algorithmCapabilities:"
- "initWithCertificate:algorithmCapabilities:originator:"
- "initWithCertificate:error:"
- "initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:"
- "initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:"
- "initWithCertificate:legacyKeyWrapAlgorithm:"
- "initWithCertificate:recipientsAlgorithmCapabilities:error:"
- "initWithCertificate:signatureAlgorithm:error:"
- "initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:"
- "initWithCoder:"
- "initWithDER:"
- "initWithData:error:"
- "initWithDataContent:"
- "initWithDataContent:error:"
- "initWithDataContent:isDetached:signer:additionalCertificates:error:"
- "initWithDataContent:isDetached:signer:error:"
- "initWithDataContent:isDetached:signer:signerChainMode:error:"
- "initWithDataContent:recipient:"
- "initWithDataContent:recipient:encryptionAlgorithm:"
- "initWithDecryptionIdentity:"
- "initWithDecryptionKey:"
- "initWithDictionary:"
- "initWithDigest:"
- "initWithDomain:code:userInfo:"
- "initWithEmail:"
- "initWithEmail:LAContext:error:"
- "initWithEmail:algorithmCapabilities:"
- "initWithEmail:keyEncryptionAlgorithm:"
- "initWithEmail:recipientsAlgorithmCapabilities:LAContext:error:"
- "initWithEmail:signatureAlgorithm:LAContext:error:"
- "initWithEmailAddress:"
- "initWithEmbeddedContent:"
- "initWithEmbeddedContent:error:"
- "initWithEmbeddedContent:recipient:"
- "initWithEmbeddedContent:recipient:encryptionAlgorithm:"
- "initWithEmbeddedContent:signer:additionalCertificates:error:"
- "initWithEmbeddedContent:signer:error:"
- "initWithEmbeddedContent:signer:signerChainMode:error:"
- "initWithEncryptionAlgorithm:"
- "initWithEnvelopedData:"
- "initWithExpirationTime:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithHashAgilityValue:"
- "initWithHashAgilityValues:"
- "initWithIdentity:"
- "initWithIdentity:error:"
- "initWithIdentity:recipientsAlgorithmCapabilities:error:"
- "initWithIdentity:signatureAlgorithm:error:"
- "initWithIdentity:signatureAlgorithm:useIssuerAndSerialNumber:error:"
- "initWithIssuerName:serialNumber:"
- "initWithIssuerName:serialNumber:negativeNumber:"
- "initWithLength:"
- "initWithMessageImprint:"
- "initWithOID:"
- "initWithOID:parameters:"
- "initWithServerURL:"
- "initWithServerURL:chainRequested:"
- "initWithSignerInfo:"
- "initWithSignerInfo:additionalCertificates:"
- "initWithSignerInfo:signerChainMode:"
- "initWithSignerInfo:signerChainMode:additionalCertificates:"
- "initWithSigningTime:"
- "initWithSkid:"
- "initWithStatus:statusString:failInfo:hasFailInfo:"
- "initWithString:error:"
- "initWithTimeIntervalSince1970:"
- "initWithTimestampToken:"
- "initWithTimestampToken:error:"
- "initWithUTF8String:"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "invertedSet"
- "isEqual:"
- "isEqualToData:"
- "isEqualToDate:"
- "isEqualToMessageImprint:error:"
- "isEqualToString:"
- "isEqualToTimestampRequest:error:"
- "isEqualToTimestampResponse:error:"
- "isImplementedInObjectiveC"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSupportedHashAlgorithm:"
- "issuerAndSerialNumber"
- "issuerNameData"
- "key"
- "key:"
- "keyEncryptionAlgorithm"
- "keyEncryptionKey:forEncryption:secCMSCompatibility:"
- "keySize:"
- "legacyASN1Encoding"
- "length"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "messageDigest"
- "messageDigestAttributeWithDigest:"
- "mutableBytes"
- "mutableCopy"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "options"
- "originator"
- "originatorCertificates"
- "originatorIdentity"
- "originatorPubKey"
- "parameters"
- "parseFailureInfo:"
- "parseMSTimestampResponseFromReply:error:"
- "parseTSAFromGeneralName:"
- "parseTSTInfo:error:"
- "parseTimeStampToken:error:"
- "parseTimestampResponse:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "protectedAttributes"
- "q"
- "q16@0:8"
- "q24@0:8^{PKIFailureInfo=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
- "r^{ccdigest_info=QQQQ*^v^?^?i^?}16@0:8"
- "rangeOfCharacterFromSet:"
- "recipientCertificate"
- "recipientCertificates"
- "recipients"
- "release"
- "removeAllObjects"
- "removeAttributes:"
- "removeLastObject"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectsAtIndexes:"
- "removeRecipientWithCertificate:error:"
- "removeRecipientWithEmailAddress:error:"
- "removeSignerCertificatesWithIndexes:"
- "removeSignersWithCertificate:error:"
- "removeSignersWithEmailAddress:error:"
- "removeSignersWithIdentity:error:"
- "removeSignersWithIndexes:error:"
- "replaceObjectAtIndex:withObject:"
- "reqPolicyID"
- "reset"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "secKeyAlgorithm"
- "self"
- "sendTimestampFetchAnalyticsEvent:success:"
- "serialNumber"
- "serialNumberData"
- "serverURL"
- "set"
- "setAdditionalCertificates:"
- "setAlgorithmCapabilities:"
- "setAlgorithmIdentifier:"
- "setAnchorCertificates:"
- "setAsn1OidFromOIDString:error:"
- "setAttributeDERData:"
- "setAttributeType:"
- "setAttributes:"
- "setBodyHashAlgorithm:"
- "setCertChainRequested:"
- "setCertReq:"
- "setCertificates:"
- "setChainMode:"
- "setContainingSignedData:"
- "setContainingSignerInfo:"
- "setContent:"
- "setContentChanged:"
- "setContentType:"
- "setContentTypeWithType:"
- "setDataContent:"
- "setDateFormat:"
- "setDateStyle:"
- "setDetached:"
- "setDigestAlgorithm:"
- "setDigestAlgorithms:"
- "setEmbeddedContent:"
- "setEncodedAttribute:"
- "setEncodedAttributeSet:"
- "setEncodedSignerInfo:"
- "setEncryptedContent:"
- "setEncryptedKeys:"
- "setEncryptionAlgorithm:"
- "setEncryptionKey:"
- "setGenericAttributes:"
- "setHashedMessage:"
- "setIdentifierData:"
- "setIdentity:"
- "setIssuerAndSerialNumber:"
- "setIssuerNameData:"
- "setKey:"
- "setKeyEncryptionAlgorithm:"
- "setLAContext:"
- "setLegacyASN1Encoding:"
- "setLength:"
- "setLocale:"
- "setMessageDigest:"
- "setMessageImprint:"
- "setNonce:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOriginator:"
- "setOriginatorCertificates:"
- "setOriginatorIdentity:"
- "setOriginatorPubKey:"
- "setProtectedAttributes:"
- "setRecipientCertificate:"
- "setRecipientCertificates:"
- "setRecipients:"
- "setReqPolicyID:"
- "setSerialNumber:"
- "setSerialNumberData:"
- "setServerURL:"
- "setSignature:"
- "setSignatureAlgorithm:"
- "setSignedAttrsData:"
- "setSignedAttrsHash:"
- "setSignedAttrsHashAlgorithm:"
- "setSignerCertificate:"
- "setSignerPolicies:"
- "setSignerPrivKey:"
- "setSigners:"
- "setSkidData:"
- "setStatus:"
- "setSubjectKeyId:"
- "setTimeStampToken:"
- "setTimeStyle:"
- "setTimeZone:"
- "setTimestamp:"
- "setTimestampAttribute:"
- "setTimestampRequest:"
- "setTimestampResponse:"
- "setTimestampServer:"
- "setTsa:"
- "setTsaPolicyID:"
- "setType:"
- "setUnprotectedAttributes:"
- "setUnsignedAttrsData:"
- "setUseIssuerAndSerialNumber:"
- "setUserKeyingMaterial:"
- "setVerifySignatures:"
- "setVerifySigners:"
- "setVerifyTime:"
- "setVerifyTimestamps:"
- "setVersion:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithSet:"
- "setXpcQueue:"
- "setXpcSession:"
- "sign:"
- "signature"
- "signatureAlgorithm"
- "signatureAlgorithmOIDWithSecKeyAlgorithm:error:"
- "signatureAlgorithmWithDigestAlgorithm:error:"
- "signatureCalculated"
- "signedAttrsData"
- "signedAttrsHash"
- "signedAttrsHashAlgorithm"
- "signedData"
- "signerCertificate"
- "signerPolicies"
- "signerPrivKey"
- "signers"
- "signingTime"
- "singerInfo"
- "skidData"
- "stringByAppendingFormat:"
- "stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:"
- "stringFromDate:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subjectKeyId"
- "superclass"
- "supportsSecureCoding"
- "timeStampToken"
- "timeZoneForSecondsFromGMT:"
- "timeZoneWithName:"
- "timestamp"
- "timestampAttribute"
- "timestampRequest"
- "timestampTime"
- "timestampToken"
- "tsa"
- "tsaPolicyID"
- "tstinfo"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unprotectedAttributes"
- "unsignedAttrsData"
- "unsignedIntValue"
- "useIssuerAndSerialNumber"
- "userKeyingMaterial"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<MSCMSMessage>\"16"
- "v24@0:8@\"MSOID\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16"
- "v24@0:8^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16"
- "v24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16"
- "v24@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16"
- "v24@0:8^{__SecCertificate=}16"
- "v24@0:8^{__SecIdentity=}16"
- "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "v24@0:8^{heim_base_data=Q^v}16"
- "v24@0:8q16"
- "v24@0:8r^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}{heim_base_data=Q^v}{OriginatorPublicKey={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_bit_string=Q^v}})}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{RecipientEncryptedKeys=I^{RecipientEncryptedKey}}})}16"
- "v28@0:8@16B24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8@16^@24"
- "v32@0:8@?16@24"
- "v32@0:8Q16@24"
- "v32@0:8^{__SecCertificate=}16^@24"
- "v32@0:8^{__SecIdentity=}16^@24"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24^@32"
- "validateTimestampRequestData:"
- "verifyContentTypeAttribute:"
- "verifyCountersignatures:"
- "verifyCountersignatures:error:"
- "verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:"
- "verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:signature:error:"
- "verifyMessageDigestAttribute:error:"
- "verifySignature:"
- "verifySignatureAndSignerWithPolicies:verifyTime:anchorCertificates:error:"
- "verifySignatures"
- "verifySignatures:"
- "verifySignaturesAndSignersWithPolicies:verifyTime:anchorCertificates:error:"
- "verifySignaturesAndSignersWithPolicies:verifyTime:error:"
- "verifySigners"
- "verifyTime"
- "verifyTime:"
- "verifyTimestamp:error:"
- "verifyTimestamps"
- "verifyTimestamps:"
- "verifyTimestamps:error:"
- "verifyWithMessageImprint:error:"
- "verifyWithRequest:error:"
- "xpcQueue"
- "xpcSession"
- "zone"
- "{heim_oid=\"length\"Q\"components\"^I}"
- "{heim_oid=Q^I}16@0:8"

```
