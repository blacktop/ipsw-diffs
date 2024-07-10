## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia`

```diff

-3145.61.2.0.0
-  __TEXT.__text: 0x20712c
-  __TEXT.__auth_stubs: 0x2f80
+3145.65.1.0.0
+  __TEXT.__text: 0x20a394
+  __TEXT.__auth_stubs: 0x2f90
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__const: 0x1784
-  __TEXT.__cstring: 0x49601
-  __TEXT.__oslogstring: 0x22372
+  __TEXT.__cstring: 0x49cba
+  __TEXT.__oslogstring: 0x22b85
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x3a88
+  __TEXT.__unwind_info: 0x3ac8
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x50d
   __TEXT.__objc_methtype: 0xe3
   __TEXT.__objc_stubs: 0x720
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x78d0
+  __DATA_CONST.__const: 0x78e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x17c8
+  __AUTH_CONST.__auth_got: 0x17d0
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x4840
-  __AUTH_CONST.__cfstring: 0x146c0
+  __AUTH_CONST.__const: 0x48b8
+  __AUTH_CONST.__cfstring: 0x14760
   __AUTH_CONST.__objc_const: 0x258
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x238

   __DATA.__data: 0xf38
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x7d0
-  __DATA.__bss: 0x2db0
+  __DATA.__bss: 0x2dc8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5052
-  Symbols:   9616
-  CStrings:  9809
+  Functions: 5066
+  Symbols:   9640
+  CStrings:  9860
 
Symbols:
+ FigMemoryOriginBeginTransactionMakingRegistrationsContingentOnIt.onceToken
+ _FigCFDictionaryGetCountOfKey
+ _FigFileForkWriteIOVecArray
+ _FigFileSetIOPolicy
+ _FigFileSetIOPolicyIfItIsDifferentFromCurrentIOPolicy
+ _FigMemoryOriginBeginTransactionMakingRegistrationsContingentOnIt
+ _FigMemoryOriginCompleteTransaction
+ _FigOSEventLinkRemoteInvalidate
+ ___FigMemoryOriginBeginTransactionMakingRegistrationsContingentOnIt_block_invoke
+ __block_descriptor_tmp.143
+ __block_descriptor_tmp.155
+ __block_descriptor_tmp.204
+ __block_descriptor_tmp.307
+ __block_descriptor_tmp.56
+ __block_descriptor_tmp.66
+ __block_descriptor_tmp.76
+ __block_descriptor_tmp.96
+ __block_literal_global.145
+ __block_literal_global.157
+ __block_literal_global.182
+ __block_literal_global.58
+ __block_literal_global.68
+ __block_literal_global.73
+ __block_literal_global.78
+ __block_literal_global.98
+ _figOSEventLinkResolveMessageStatus
+ _figObjectDependencyDeathDefaultCallback
+ _figXPCCopySanitizedCFDictionary
+ _hevcbridgeAdvanceAcrossBBufDiscontiguity
+ _hevcbridgeSetupBitStreamFromPointerAndLength
+ _kCMSampleAttachmentKey_PostDecodeProcessingMetadata
+ _kFigCAStatsReportingEventName_NSURLProtocolUsage
+ _kFigCAStatsReporting_PayloadKey_SuccessfulDataLoad
+ _kFigSampleBufferConduitNotificationParameter_CollectorCoherenceToken
+ _kFigSampleBufferConduitNotification_CollectorCoherence
+ _pwritev
+ _sFigMemoryOriginTransactionThreadKey
+ _sbufAtomAppendSampleSizes_MissingSampleSizes_LogOnce
+ _transactionThreadDestructor
+ sbufAtomAppendSampleSizes_MissingSampleSizes_LogOnce.cold.1
+ sbufAtom_appendSampleSizes.sSBufAtomAppendSampleSizes_MissingSampleSizeForVideo_InitOnce
- __block_descriptor_tmp.135
- __block_descriptor_tmp.147
- __block_descriptor_tmp.172
- __block_descriptor_tmp.303
- __block_descriptor_tmp.59
- __block_descriptor_tmp.77
- __block_descriptor_tmp.97
- __block_literal_global.137
- __block_literal_global.149
- __block_literal_global.174
- __block_literal_global.61
- __block_literal_global.79
- __block_literal_global.99
- _figObjectDependencyDeathCallback
- _hevcbridgeSetupBitStreamFromPointer
- _kFigSampleAttachmentKey_PostDecodeProcessingMetadata
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/IPC/FigOSEventLink.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Player/ClientServer/FigSampleBufferAtomSerialization.c"
+ "CMSampleBufferGetSampleSizeArray failed"
+ "CodecInfo"
+ "CollectorCoherence"
+ "CollectorCoherenceToken"
+ "FigFileForkWriteOneIOVecArray"
+ "FigFileGetIOPolicy"
+ "FigFileR"
+ "FigFileSetIOPolicy"
+ "FigFileV"
+ "FigFileW"
+ "FigHALAudioConfigChangeSendRequestWithCustomChangeRecord_block_invoke"
+ "FigHALAudioConfigChangeSendRequest_block_invoke"
+ "FigHALAudioPropertySendChanges"
+ "FigHALAudioPropertySendOneChange"
+ "FigMemoryOriginBeginTransactionMakingRegistrationsContingentOnIt"
+ "FigMemoryOriginBeginTransactionMakingRegistrationsContingentOnIt_block_invoke"
+ "FigMemoryOriginCompleteTransaction"
+ "FigOSEventLinkRemoteFillMessageBufferThenSendItAndHandleReply"
+ "FigOSEventLinkRemoteInvalidate"
+ "NULL byteStreamOut"
+ "No active transaction found in current thread"
+ "Resource payload dictionary missing from atom data"
+ "Unexpected status value"
+ "blockBufferSize is zero for blockBuffer"
+ "com.apple.coremedia.nsurlprotocolusage"
+ "eventLinkRemote is NULL"
+ "failed to allocate transaction"
+ "figMemoryOriginTransactionAddBlockSerialNumberToUnregisterInCaseOfUnwind"
+ "figOSEventLinkResolveMessageStatus"
+ "figOSEventLinkServer_finishSendingReply"
+ "figOSEventLinkServer_prepareForSendingReply"
+ "figOSEventLinkServer_processInternalMessage"
+ "figObjectDependencyDeathDefaultCallback"
+ "getSampleSizeErr"
+ "getiopolicy_np failed"
+ "hevcbridgeMeasureSliceHeaderInBlockBuffer"
+ "instance is invalidated"
+ "kFigMemoryOriginError_InvalidState"
+ "kFigOSEventLinkError_Invalid"
+ "kFigOSEventLinkError_MessageHandlerFailure"
+ "message from remote is not Acknowledged"
+ "message is in an invalid state"
+ "message to server is in an invalid state"
+ "message was not handled by server"
+ "originsAndBlockSerialNumbers allocation failed"
+ "pixelBufferSharing_serializePixelBufferAttachmentsInMemory"
+ "pwritev failed"
+ "reply is in an invalid state"
+ "reply not filled"
+ "reply was not handled by client"
+ "setiopolicy_np failed"
+ "successfulDataLoad"
+ "transactionThreadDestructor"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/IPC/FigOSEventLink.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Prototypes/Player/ClientServer/FigSampleBufferAtomSerialization.c"
- "Could not convert non-propagated attachment dict to XPC object"
- "figObjectDependencyDeathCallback"

```
