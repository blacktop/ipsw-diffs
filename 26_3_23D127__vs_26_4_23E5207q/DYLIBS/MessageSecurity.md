## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

```diff

-195.80.13.0.0
-  __TEXT.__text: 0x3d41c
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x1cf4
-  __TEXT.__const: 0x13d4
-  __TEXT.__gcc_except_tab: 0x834
-  __TEXT.__cstring: 0x357d
-  __TEXT.__oslogstring: 0xabc
-  __TEXT.__swift5_typeref: 0x2a8
-  __TEXT.__swift5_capture: 0x10
+195.100.59.0.0
+  __TEXT.__text: 0x463a0
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x2274
+  __TEXT.__const: 0x1474
+  __TEXT.__gcc_except_tab: 0x880
+  __TEXT.__cstring: 0x41a7
+  __TEXT.__oslogstring: 0xcec
+  __TEXT.__swift5_typeref: 0x2b8
   __TEXT.__constg_swiftt: 0x3f0
   __TEXT.__swift5_reflstr: 0x4e3
   __TEXT.__swift5_fieldmd: 0x58c
+  __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x74
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x1010
-  __TEXT.__eh_frame: 0x7f0
-  __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x4039
-  __TEXT.__objc_methtype: 0x1793
-  __TEXT.__objc_stubs: 0x2860
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x44b0
-  __DATA_CONST.__objc_classlist: 0xe0
+  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__eh_frame: 0x778
+  __TEXT.__objc_classname: 0x3b4
+  __TEXT.__objc_methname: 0x4d91
+  __TEXT.__objc_methtype: 0x1bbe
+  __TEXT.__objc_stubs: 0x3380
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x45c0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea0
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x1480
-  __AUTH_CONST.__cfstring: 0x24e0
-  __AUTH_CONST.__objc_const: 0x3f38
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x1ac
-  __DATA.__data: 0x1170
-  __DATA.__bss: 0x5a0
+  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__const: 0x15d8
+  __AUTH_CONST.__cfstring: 0x3600
+  __AUTH_CONST.__objc_const: 0x4bf8
+  __AUTH.__objc_data: 0x188
+  __DATA.__objc_ivar: 0x210
+  __DATA.__data: 0x1230
+  __DATA.__bss: 0x8a0
   __DATA.__common: 0x2711
   __DATA_DIRTY.__objc_data: 0xad0
-  __DATA_DIRTY.__data: 0xa8
+  __DATA_DIRTY.__data: 0xb0
   __DATA_DIRTY.__bss: 0x30
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8885ABAB-4FF3-327D-86C1-4F94769F980C
-  Functions: 2007
-  Symbols:   4416
-  CStrings:  1580
+  UUID: 1463BB0A-2849-3E86-8C5A-CF5298799AF2
+  Functions: 2164
+  Symbols:   4946
+  CStrings:  2016
 
Symbols:
+ +[MSMessageImprint supportsSecureCoding]
+ +[MSPKIStatusInfo supportsSecureCoding]
+ +[MSTimestampRequest supportsSecureCoding]
+ +[MSTimestampResponse supportsSecureCoding]
+ -[MSMessageImprint .cxx_destruct]
+ -[MSMessageImprint algorithmIdentifier]
+ -[MSMessageImprint debugDescription]
+ -[MSMessageImprint description]
+ -[MSMessageImprint encodeWithCoder:]
+ -[MSMessageImprint expectedHashLength:]
+ -[MSMessageImprint hash]
+ -[MSMessageImprint hashedMessage]
+ -[MSMessageImprint init:hashedMessage:]
+ -[MSMessageImprint initWithCoder:]
+ -[MSMessageImprint initWithMessageImprint:]
+ -[MSMessageImprint initWithMessageImprint:].cold.1
+ -[MSMessageImprint isEqual:]
+ -[MSMessageImprint isEqualToMessageImprint:error:]
+ -[MSMessageImprint isSupportedHashAlgorithm:]
+ -[MSMessageImprint setAlgorithmIdentifier:]
+ -[MSMessageImprint setHashedMessage:]
+ -[MSPKIStatusInfo .cxx_destruct]
+ -[MSPKIStatusInfo encodeWithCoder:]
+ -[MSPKIStatusInfo failInfo]
+ -[MSPKIStatusInfo hasFailInfo]
+ -[MSPKIStatusInfo hash]
+ -[MSPKIStatusInfo initWithCoder:]
+ -[MSPKIStatusInfo initWithStatus:statusString:failInfo:hasFailInfo:]
+ -[MSPKIStatusInfo isEqual:]
+ -[MSPKIStatusInfo statusString]
+ -[MSPKIStatusInfo status]
+ -[MSTimestampRequest .cxx_destruct]
+ -[MSTimestampRequest buildMessageImprintForASN1:error:]
+ -[MSTimestampRequest buildTimestampRequest]
+ -[MSTimestampRequest buildTimestampRequest].cold.1
+ -[MSTimestampRequest buildTimestampRequest].cold.2
+ -[MSTimestampRequest certReq]
+ -[MSTimestampRequest cleanupMessageImprint:]
+ -[MSTimestampRequest createXPCMessageForTimestampFetch]
+ -[MSTimestampRequest createXPCMessageForTimestampFetch].cold.1
+ -[MSTimestampRequest dealloc]
+ -[MSTimestampRequest debugDescription]
+ -[MSTimestampRequest description]
+ -[MSTimestampRequest encodeWithCoder:]
+ -[MSTimestampRequest ensureXPCSessionExists:]
+ -[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]
+ -[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:].cold.1
+ -[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:].cold.2
+ -[MSTimestampRequest fetchTimestampWithError:]
+ -[MSTimestampRequest handleXPCReply:onQueue:completion:]
+ -[MSTimestampRequest hash]
+ -[MSTimestampRequest init:]
+ -[MSTimestampRequest init:server:]
+ -[MSTimestampRequest initWithCoder:]
+ -[MSTimestampRequest isEqual:]
+ -[MSTimestampRequest isEqualToTimestampRequest:error:]
+ -[MSTimestampRequest messageImprint]
+ -[MSTimestampRequest nonce]
+ -[MSTimestampRequest parseMSTimestampResponseFromReply:error:]
+ -[MSTimestampRequest parseMSTimestampResponseFromReply:error:].cold.1
+ -[MSTimestampRequest reqPolicyID]
+ -[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:]
+ -[MSTimestampRequest setCertReq:]
+ -[MSTimestampRequest setMessageImprint:]
+ -[MSTimestampRequest setNonce:]
+ -[MSTimestampRequest setReqPolicyID:]
+ -[MSTimestampRequest setTimestampRequest:]
+ -[MSTimestampRequest setTimestampServer:]
+ -[MSTimestampRequest setVersion:]
+ -[MSTimestampRequest setXpcQueue:]
+ -[MSTimestampRequest setXpcSession:]
+ -[MSTimestampRequest timestampRequest]
+ -[MSTimestampRequest timestampServer]
+ -[MSTimestampRequest validateTimestampRequestData:]
+ -[MSTimestampRequest version]
+ -[MSTimestampRequest xpcQueue]
+ -[MSTimestampRequest xpcSession]
+ -[MSTimestampResponse .cxx_destruct]
+ -[MSTimestampResponse debugDescription]
+ -[MSTimestampResponse description]
+ -[MSTimestampResponse encodeWithCoder:]
+ -[MSTimestampResponse hash]
+ -[MSTimestampResponse init:]
+ -[MSTimestampResponse init:].cold.1
+ -[MSTimestampResponse init:].cold.2
+ -[MSTimestampResponse initWithCoder:]
+ -[MSTimestampResponse isEqual:]
+ -[MSTimestampResponse isEqualToTimestampResponse:error:]
+ -[MSTimestampResponse messageImprint]
+ -[MSTimestampResponse nonce]
+ -[MSTimestampResponse parseFailureInfo:]
+ -[MSTimestampResponse parseTSAFromGeneralName:]
+ -[MSTimestampResponse parseTSTInfo:error:]
+ -[MSTimestampResponse parseTSTInfo:error:].cold.1
+ -[MSTimestampResponse parseTimeStampToken:error:]
+ -[MSTimestampResponse parseTimeStampToken:error:].cold.1
+ -[MSTimestampResponse parseTimestampResponse:]
+ -[MSTimestampResponse parseTimestampResponse:].cold.1
+ -[MSTimestampResponse serialNumber]
+ -[MSTimestampResponse setMessageImprint:]
+ -[MSTimestampResponse setNonce:]
+ -[MSTimestampResponse setSerialNumber:]
+ -[MSTimestampResponse setStatus:]
+ -[MSTimestampResponse setTimeStampToken:]
+ -[MSTimestampResponse setTimestamp:]
+ -[MSTimestampResponse setTimestampResponse:]
+ -[MSTimestampResponse setTsa:]
+ -[MSTimestampResponse setTsaPolicyID:]
+ -[MSTimestampResponse setVersion:]
+ -[MSTimestampResponse status]
+ -[MSTimestampResponse timeStampToken]
+ -[MSTimestampResponse timestampResponse]
+ -[MSTimestampResponse timestamp]
+ -[MSTimestampResponse tsaPolicyID]
+ -[MSTimestampResponse tsa]
+ -[MSTimestampResponse verifyWithMessageImprint:error:]
+ -[MSTimestampResponse verifyWithRequest:error:]
+ -[MSTimestampResponse version]
+ GCC_except_table12
+ _MSTimestampErrorCreate
+ _MSTimestampErrorCreateWithFormat
+ _MSTimestampErrorCreateWithUnderlying
+ _MSTimestampErrorDomain
+ _OBJC_CLASS_$_MSMessageImprint
+ _OBJC_CLASS_$_MSPKIStatusInfo
+ _OBJC_CLASS_$_MSTimestampRequest
+ _OBJC_CLASS_$_MSTimestampResponse
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_MSMessageImprint._algorithmIdentifier
+ _OBJC_IVAR_$_MSMessageImprint._hashedMessage
+ _OBJC_IVAR_$_MSPKIStatusInfo._failInfo
+ _OBJC_IVAR_$_MSPKIStatusInfo._hasFailInfo
+ _OBJC_IVAR_$_MSPKIStatusInfo._status
+ _OBJC_IVAR_$_MSPKIStatusInfo._statusString
+ _OBJC_IVAR_$_MSTimestampRequest._certReq
+ _OBJC_IVAR_$_MSTimestampRequest._messageImprint
+ _OBJC_IVAR_$_MSTimestampRequest._nonce
+ _OBJC_IVAR_$_MSTimestampRequest._reqPolicyID
+ _OBJC_IVAR_$_MSTimestampRequest._timestampRequest
+ _OBJC_IVAR_$_MSTimestampRequest._timestampServer
+ _OBJC_IVAR_$_MSTimestampRequest._version
+ _OBJC_IVAR_$_MSTimestampRequest._xpcQueue
+ _OBJC_IVAR_$_MSTimestampRequest._xpcSession
+ _OBJC_IVAR_$_MSTimestampResponse._messageImprint
+ _OBJC_IVAR_$_MSTimestampResponse._nonce
+ _OBJC_IVAR_$_MSTimestampResponse._serialNumber
+ _OBJC_IVAR_$_MSTimestampResponse._status
+ _OBJC_IVAR_$_MSTimestampResponse._timeStampToken
+ _OBJC_IVAR_$_MSTimestampResponse._timestamp
+ _OBJC_IVAR_$_MSTimestampResponse._timestampResponse
+ _OBJC_IVAR_$_MSTimestampResponse._tsa
+ _OBJC_IVAR_$_MSTimestampResponse._tsaPolicyID
+ _OBJC_IVAR_$_MSTimestampResponse._version
+ _OBJC_METACLASS_$_MSMessageImprint
+ _OBJC_METACLASS_$_MSPKIStatusInfo
+ _OBJC_METACLASS_$_MSTimestampRequest
+ _OBJC_METACLASS_$_MSTimestampResponse
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SecPolicyCreateAppleTimeStamping
+ __OBJC_$_CLASS_METHODS_MSMessageImprint
+ __OBJC_$_CLASS_METHODS_MSPKIStatusInfo
+ __OBJC_$_CLASS_METHODS_MSTimestampRequest
+ __OBJC_$_CLASS_METHODS_MSTimestampResponse
+ __OBJC_$_CLASS_PROP_LIST_MSMessageImprint
+ __OBJC_$_CLASS_PROP_LIST_MSPKIStatusInfo
+ __OBJC_$_CLASS_PROP_LIST_MSTimestampRequest
+ __OBJC_$_CLASS_PROP_LIST_MSTimestampResponse
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_MSMessageImprint
+ __OBJC_$_INSTANCE_METHODS_MSPKIStatusInfo
+ __OBJC_$_INSTANCE_METHODS_MSTimestampRequest
+ __OBJC_$_INSTANCE_METHODS_MSTimestampResponse
+ __OBJC_$_INSTANCE_VARIABLES_MSMessageImprint
+ __OBJC_$_INSTANCE_VARIABLES_MSPKIStatusInfo
+ __OBJC_$_INSTANCE_VARIABLES_MSTimestampRequest
+ __OBJC_$_INSTANCE_VARIABLES_MSTimestampResponse
+ __OBJC_$_PROP_LIST_MSMessageImprint
+ __OBJC_$_PROP_LIST_MSPKIStatusInfo
+ __OBJC_$_PROP_LIST_MSTimestampRequest
+ __OBJC_$_PROP_LIST_MSTimestampResponse
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_MSMessageImprint
+ __OBJC_CLASS_PROTOCOLS_$_MSPKIStatusInfo
+ __OBJC_CLASS_PROTOCOLS_$_MSTimestampRequest
+ __OBJC_CLASS_PROTOCOLS_$_MSTimestampResponse
+ __OBJC_CLASS_RO_$_MSMessageImprint
+ __OBJC_CLASS_RO_$_MSPKIStatusInfo
+ __OBJC_CLASS_RO_$_MSTimestampRequest
+ __OBJC_CLASS_RO_$_MSTimestampResponse
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_MSMessageImprint
+ __OBJC_METACLASS_RO_$_MSPKIStatusInfo
+ __OBJC_METACLASS_RO_$_MSTimestampRequest
+ __OBJC_METACLASS_RO_$_MSTimestampResponse
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_MSCMSMessage
+ __PROTOCOLS_MSCMSAuthEnvelopedData.5
+ ___28-[MSTimestampResponse init:]_block_invoke
+ ___28-[MSTimestampResponse init:]_block_invoke.348
+ ___42-[MSTimestampResponse parseTSTInfo:error:]_block_invoke
+ ___43-[MSMessageImprint initWithMessageImprint:]_block_invoke
+ ___43-[MSTimestampRequest buildTimestampRequest]_block_invoke
+ ___43-[MSTimestampRequest buildTimestampRequest]_block_invoke.28
+ ___46-[MSTimestampResponse parseTimestampResponse:]_block_invoke
+ ___49-[MSTimestampResponse parseTimeStampToken:error:]_block_invoke
+ ___55-[MSTimestampRequest createXPCMessageForTimestampFetch]_block_invoke
+ ___56-[MSTimestampRequest handleXPCReply:onQueue:completion:]_block_invoke
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke.95
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke.98
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_2
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_3
+ ___62-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:]_block_invoke_4
+ ___62-[MSTimestampRequest parseMSTimestampResponseFromReply:error:]_block_invoke
+ ___63-[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:]_block_invoke
+ ___block_descriptor_41_e8_32s_e30_"NSObject<OS_xpc_object>"8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e61_v24?0"NSObject<OS_xpc_object>"8"NSObject<OS_xpc_object>"16ls32l8w56l8s48l8s40l8
+ ___block_literal_global.346
+ ___block_literal_global.350
+ ___block_literal_global.365
+ ___block_literal_global.444
+ ___block_literal_global.455
+ ___block_literal_global.668
+ ___block_literal_global.70
+ ___block_literal_global.86
+ ___block_literal_global.94
+ ___block_literal_global.97
+ _analytics_send_event_lazy
+ _associated conformance So17SecCertificateRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So17SecCertificateRefaSHSCSQ
+ _dispatch_async
+ _dispatch_queue_create
+ _kMSAppleTimestampEndpoint_ECC_ts_ec
+ _kMSAppleTimestampEndpoint_RSA_ts01
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$absoluteString
+ _objc_msgSend$algorithmIdentifier
+ _objc_msgSend$appendString:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$buildMessageImprintForASN1:error:
+ _objc_msgSend$buildTimestampRequest
+ _objc_msgSend$certReq
+ _objc_msgSend$cleanupMessageImprint:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$createXPCMessageForTimestampFetch
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$description
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$embeddedContent
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encodeOriginatorInfoCertificates:error:
+ _objc_msgSend$encodeRecipientInfo:recipientInfo:error:
+ _objc_msgSend$encryptBulkKey:
+ _objc_msgSend$encryptContent:
+ _objc_msgSend$encryptionAlgorithm
+ _objc_msgSend$encryptionKey
+ _objc_msgSend$ensureXPCSessionExists:
+ _objc_msgSend$expectedHashLength:
+ _objc_msgSend$failInfo
+ _objc_msgSend$freeRecipientInfo:
+ _objc_msgSend$getRecipients
+ _objc_msgSend$handleXPCReply:onQueue:completion:
+ _objc_msgSend$hasFailInfo
+ _objc_msgSend$hashedMessage
+ _objc_msgSend$init:
+ _objc_msgSend$init:hashedMessage:
+ _objc_msgSend$init:server:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithMessageImprint:
+ _objc_msgSend$initWithStatus:statusString:failInfo:hasFailInfo:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToMessageImprint:error:
+ _objc_msgSend$isEqualToTimestampRequest:error:
+ _objc_msgSend$isEqualToTimestampResponse:error:
+ _objc_msgSend$isSupportedHashAlgorithm:
+ _objc_msgSend$key
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$messageImprint
+ _objc_msgSend$nonce
+ _objc_msgSend$originator
+ _objc_msgSend$originatorIdentity
+ _objc_msgSend$parseFailureInfo:
+ _objc_msgSend$parseMSTimestampResponseFromReply:error:
+ _objc_msgSend$parseTSAFromGeneralName:
+ _objc_msgSend$parseTSTInfo:error:
+ _objc_msgSend$parseTimeStampToken:error:
+ _objc_msgSend$parseTimestampResponse:
+ _objc_msgSend$reqPolicyID
+ _objc_msgSend$sendTimestampFetchAnalyticsEvent:success:
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setAlgorithmIdentifier:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setHashedMessage:
+ _objc_msgSend$setMessageImprint:
+ _objc_msgSend$setNonce:
+ _objc_msgSend$setSerialNumber:
+ _objc_msgSend$setTimeStampToken:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setTimestampResponse:
+ _objc_msgSend$setTsa:
+ _objc_msgSend$status
+ _objc_msgSend$statusString
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$timeStampToken
+ _objc_msgSend$timeZoneWithName:
+ _objc_msgSend$timestamp
+ _objc_msgSend$timestampRequest
+ _objc_msgSend$timestampResponse
+ _objc_msgSend$timestampServer
+ _objc_msgSend$tsa
+ _objc_msgSend$tsaPolicyID
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$validateTimestampRequestData:
+ _objc_msgSend$verifySignaturesAndSignersWithPolicies:verifyTime:error:
+ _objc_msgSend$verifyWithMessageImprint:error:
+ _objc_sync_enter
+ _objc_sync_exit
+ _xpc_dictionary_create
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_data
+ _xpc_dictionary_set_string
+ _xpc_rich_error_copy_description
+ _xpc_session_cancel
+ _xpc_session_create_xpc_service
+ _xpc_session_send_message_with_reply_async
+ _xpc_session_send_message_with_reply_sync
- __PROTOCOLS_MSCMSAuthEnvelopedData.8
- _memset
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x13
- _objc_retain_x5
- _swift_deallocObject
CStrings:
+ "\n"
+ "\n--- Additional Debug Info ---\n"
+ "  Algorithm OID: %@"
+ "  Algorithm: %@\n"
+ "  Failure Info: %ld\n"
+ "  Gen Time: %@ UTC\n"
+ "  Gen Time: (none)\n"
+ "  Hash: %@ (%lu bytes)"
+ "  Hash: (empty)"
+ "  Message Imprint: %@\n"
+ "  Message Imprint: (none)\n"
+ "  Nonce Length: %lu bytes"
+ "  Nonce: %@ (%lu bytes)\n"
+ "  Nonce: (none)\n"
+ "  Policy OID: %@\n"
+ "  Policy: %@\n"
+ "  Policy: (none)\n"
+ "  Request Certificates: %@\n"
+ "  Request Size: %lu bytes\n"
+ "  Response Size: %lu bytes"
+ "  Serial Number: %@ (%lu bytes)\n"
+ "  Serial Number: (none)\n"
+ "  Server URL: %@"
+ "  Status String: %@\n"
+ "  Status: %@\n"
+ "  TSA: %@\n"
+ "  TimeStampToken: (nil)\n"
+ "  TimeStampToken: Present\n"
+ "  Version: %ld\n"
+ "!"
+ "(nil)"
+ "(not set)"
+ "--- Basic Info ---\n"
+ "; "
+ "<MSMessageImprint:\n"
+ "<MSMessageImprint: %p>\n"
+ "<MSTimestampRequest:\n"
+ "<MSTimestampRequest: %p>\n"
+ "<MSTimestampResponse:\n"
+ "<MSTimestampResponse: %p>\n"
+ ">"
+ "@\"MSMessageImprint\""
+ "@\"MSPKIStatusInfo\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_xpc_object>\"8@?0"
+ "@\"NSObject<OS_xpc_session>\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8^{GeneralName=i(?={GeneralName_otherName={heim_oid=Q^I}{heim_base_data=Q^v}}{heim_base_data=Q^v}{heim_base_data=Q^v}{GeneralName_directoryName=i(?={RDNSequence=I^{RelativeDistinguishedName}})}{heim_base_data=Q^v}{heim_base_data=Q^v}{heim_oid=Q^I})}16"
+ "@24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16"
+ "@44@0:8q16@24q32B40"
+ "Algorithm identifiers do not match"
+ "B32@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16^@24"
+ "Certificate request flags do not match"
+ "Error: SignedData contentType is %@ (expected %@)"
+ "Fail info mismatch"
+ "Fail info presence mismatch"
+ "Failed encoding type TimeStampReq"
+ "Failed to allocate memory for OID components"
+ "Failed to archive MSTimestampRequest: %@"
+ "Failed to build MessageImprint for TimeStampReq: %@"
+ "Failed to create Apple timestamp policy"
+ "Failed to create XPC session"
+ "Failed to create XPC session: %s"
+ "Failed to decode TSTInfo: ASN.1 error %d"
+ "Failed to decode TimeStampResp: ASN.1 error %d"
+ "Failed to decode TimeStampToken as ContentInfo"
+ "Failed to encode TimeStampReq: %@"
+ "Failed to encode TimeStampToken: %@"
+ "Failed to extract TSTInfo from SignedData"
+ "Failed to parse TSA policy OID: %@"
+ "Failed to parse hash algorithm OID: %@"
+ "Failed to unarchive timestamp response"
+ "Granted"
+ "Granted with modifications"
+ "Hashed messages do not match"
+ "Invalid MessageImprint data"
+ "Invalid OID component at index %lu: value %ld is out of valid range [0, %u]"
+ "Invalid OID string format"
+ "MSCMSAuthEnvelopedData"
+ "MSCMSCompressedData"
+ "MSCMSEnvelopedDataInternal"
+ "MSCMSTimestampAttributeInternal"
+ "MSMessageImprint"
+ "MSPKIStatusInfo"
+ "MSTimestampErrorDomain"
+ "MSTimestampRequest"
+ "MSTimestampRequest: Completion block is required"
+ "MSTimestampRequest: Failed to unarchive response: %@"
+ "MSTimestampRequest: Queue is required"
+ "MSTimestampResponse"
+ "MSTimestampResponse: Cannot initialize with nil timestamp response data"
+ "MSTimestampResponse: Failed to parse timestamp response: %@"
+ "Message imprint cannot be nil"
+ "Message imprint presence mismatch"
+ "MessageImprint pointer cannot be NULL"
+ "Missing algorithm OID"
+ "NO"
+ "NSCoding"
+ "NSSecureCoding"
+ "No response object in XPC reply"
+ "No timestamp request data available"
+ "No timestamp response data to parse"
+ "No timestamp server URL specified"
+ "Nonce mismatch"
+ "Nonce values do not match"
+ "Other message imprint cannot be nil"
+ "Other message imprint has nil parameter"
+ "Other message imprint has unsupported hash algorithm"
+ "Other timestamp request cannot be nil"
+ "Other timestamp request has nil parameter"
+ "Other timestamp response cannot be nil"
+ "Other timestamp response has nil parameter"
+ "Q24@0:8@16"
+ "Rejection"
+ "Request contained nonce but response does not"
+ "Request policy OID mismatch"
+ "Revocation notification"
+ "Revocation warning"
+ "SHA-1"
+ "SHA-256"
+ "SHA-384"
+ "SHA-512"
+ "Self message imprint has nil parameter"
+ "Self message imprint has unsupported hash algorithm"
+ "Self timestamp request has nil parameter"
+ "Self timestamp response has nil parameter"
+ "Serial number mismatch"
+ "Server URL mismatch"
+ "SignedData does not contain encapsulated content (TSTInfo)"
+ "Status %ld"
+ "Status mismatch"
+ "Status string mismatch"
+ "T@\"MSAlgorithmIdentifier\",&,V_algorithmIdentifier"
+ "T@\"MSCMSSignedData\",&,V_timeStampToken"
+ "T@\"MSMessageImprint\",&,V_messageImprint"
+ "T@\"MSOID\",&,V_reqPolicyID"
+ "T@\"MSOID\",&,V_tsaPolicyID"
+ "T@\"MSPKIStatusInfo\",&,V_status"
+ "T@\"NSData\",&,V_hashedMessage"
+ "T@\"NSData\",&,V_nonce"
+ "T@\"NSData\",&,V_serialNumber"
+ "T@\"NSData\",&,V_timestampRequest"
+ "T@\"NSData\",&,V_timestampResponse"
+ "T@\"NSDate\",&,V_timestamp"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_xpcQueue"
+ "T@\"NSObject<OS_xpc_session>\",&,V_xpcSession"
+ "T@\"NSString\",&,V_tsa"
+ "T@\"NSString\",R,V_statusString"
+ "T@\"NSURL\",&,V_timestampServer"
+ "TB,R"
+ "TB,R,V_hasFailInfo"
+ "TB,V_certReq"
+ "TSA mismatch"
+ "TSA policy OID mismatch"
+ "TSA policy OIDs do not match"
+ "TSTInfo data is nil"
+ "TimeStampToken data is nil"
+ "TimeStampToken is not SignedData"
+ "Timestamp mismatch"
+ "Timestamp request cannot be nil"
+ "Timestamp request data does not match"
+ "Timestamp request was not granted. Status: %ld"
+ "Timestamp response data mismatch"
+ "Timestamp response does not contain a message imprint"
+ "Timestamp token SignedData not available for verification"
+ "Timestamp token signature and certificate verification failed"
+ "Tq,R,V_failInfo"
+ "Tq,R,V_status"
+ "Tq,V_version"
+ "URLWithString:"
+ "UTC"
+ "UTF8String"
+ "Unknown"
+ "Unknown error"
+ "Version mismatch"
+ "Version numbers do not match"
+ "Waiting"
+ "XPC communication error: %s"
+ "YES"
+ "_algorithmIdentifier"
+ "_certReq"
+ "_failInfo"
+ "_hasFailInfo"
+ "_hashedMessage"
+ "_messageImprint"
+ "_nonce"
+ "_reqPolicyID"
+ "_serialNumber"
+ "_status"
+ "_statusString"
+ "_timeStampToken"
+ "_timestamp"
+ "_timestampRequest"
+ "_timestampResponse"
+ "_timestampServer"
+ "_tsa"
+ "_tsaPolicyID"
+ "_xpcQueue"
+ "_xpcSession"
+ "absoluteString"
+ "algorithmIdentifier"
+ "algorithmOIDString"
+ "algorithmParameters"
+ "appendString:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "buildMessageImprintForASN1:error:"
+ "buildTimestampRequest"
+ "certReq"
+ "cleanupMessageImprint:"
+ "com.apple.MSTimestampXPCService.queue"
+ "com.apple.MessageSecurity.MSTimestampXPCService"
+ "com.apple.messagesecurity.mstimestamp.fetchTimestampWithCompletionBlock_success"
+ "com.apple.messagesecurity.mstimestamp.fetchTimestampWithError_success"
+ "componentsJoinedByString:"
+ "createXPCMessageForTimestampFetch"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "dictionaryWithObject:forKey:"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "ensureXPCSessionExists:"
+ "errorCode"
+ "errorDescription"
+ "expectedHashLength:"
+ "failInfo"
+ "fetch"
+ "fetchTimestampWithCompletionBlock:queue:"
+ "fetchTimestampWithError:"
+ "handleXPCReply:onQueue:completion:"
+ "hasFailInfo"
+ "hashedMessage"
+ "http://timestamp.apple.com/ts-ec"
+ "http://timestamp.apple.com/ts01"
+ "init:"
+ "init:hashedMessage:"
+ "init:server:"
+ "initWithCoder:"
+ "initWithMessageImprint:"
+ "initWithStatus:statusString:failInfo:hasFailInfo:"
+ "isEqualToDate:"
+ "isEqualToMessageImprint:error:"
+ "isEqualToTimestampRequest:error:"
+ "isEqualToTimestampResponse:error:"
+ "isSupportedHashAlgorithm:"
+ "localizedDescription"
+ "messageImprint"
+ "messageType"
+ "nonce"
+ "parseFailureInfo:"
+ "parseMSTimestampResponseFromReply:error:"
+ "parseTSAFromGeneralName:"
+ "parseTSTInfo:error:"
+ "parseTimeStampToken:error:"
+ "parseTimestampResponse:"
+ "q"
+ "q16@0:8"
+ "q24@0:8^{PKIFailureInfo=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16"
+ "reqPolicyID"
+ "reqPolicyOIDString"
+ "requestObject"
+ "responseObject"
+ "sendTimestampFetchAnalyticsEvent:success:"
+ "serialNumber"
+ "setAlgorithmIdentifier:"
+ "setCertReq:"
+ "setDateStyle:"
+ "setHashedMessage:"
+ "setMessageImprint:"
+ "setNonce:"
+ "setReqPolicyID:"
+ "setSerialNumber:"
+ "setStatus:"
+ "setTimeStampToken:"
+ "setTimeStyle:"
+ "setTimestamp:"
+ "setTimestampRequest:"
+ "setTimestampResponse:"
+ "setTimestampServer:"
+ "setTsa:"
+ "setTsaPolicyID:"
+ "setXpcQueue:"
+ "setXpcSession:"
+ "statusString"
+ "stringWithString:"
+ "success"
+ "supportsSecureCoding"
+ "timeStampToken"
+ "timeZoneWithName:"
+ "timestamp"
+ "timestampRequest"
+ "timestampResponse"
+ "timestampServer"
+ "timestamp_server"
+ "tsa"
+ "tsaPolicyID"
+ "unarchivedObjectOfClass:fromData:error:"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16"
+ "v24@0:8q16"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSObject<OS_xpc_object>\"16"
+ "v28@0:8@16B24"
+ "v32@0:8@?16@24"
+ "v40@0:8@16@24@?32"
+ "validateTimestampRequestData:"
+ "verifyWithMessageImprint:error:"
+ "verifyWithRequest:error:"
+ "xpcQueue"
+ "xpcSession"

```
