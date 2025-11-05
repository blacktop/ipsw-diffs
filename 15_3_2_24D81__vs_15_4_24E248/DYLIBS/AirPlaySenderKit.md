## AirPlaySenderKit

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/Versions/A/AirPlaySenderKit`

```diff

-845.5.1.0.0
-  __TEXT.__text: 0xc228
+850.19.1.0.0
+  __TEXT.__text: 0xcc04
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x2ec
+  __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x25f0
   __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_classname: 0x75
   __TEXT.__objc_methname: 0x96b
   __TEXT.__objc_methtype: 0x445

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x258
+  __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x8e0
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0xb10
+  __AUTH_CONST.__objc_const: 0x8c8
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x230

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B1CAB1A8-0897-31EA-96B9-C8F6B21BBE18
-  Functions: 220
-  Symbols:   672
+  UUID: A936EBBA-FA96-39BB-992B-6564115C5F88
+  Functions: 401
+  Symbols:   864
   CStrings:  449
 
Symbols:
+ -[APSKSession dealloc].cold.1
+ -[APSKSession initWithDelegate:delegateQueue:].cold.1
+ -[APSKSession localSendAudioData:].cold.1
+ -[APSKSession localSendAudioData:].cold.2
+ -[APSKSession localSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.1
+ -[APSKSession localSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.2
+ -[APSKSession localSendFrame:forTime:].cold.1
+ -[APSKSession localSendFrame:forTime:].cold.2
+ -[APSKSession localSetAuthString:].cold.1
+ -[APSKSession localSetAuthString:].cold.2
+ -[APSKSession remoteSendAudioData:].cold.1
+ -[APSKSession remoteSendAudioData:].cold.2
+ -[APSKSession remoteSendAudioData:].cold.3
+ -[APSKSession remoteSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.1
+ -[APSKSession remoteSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.2
+ -[APSKSession remoteSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.3
+ -[APSKSession remoteSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:].cold.4
+ -[APSKSession remoteSendFrame:forTime:].cold.1
+ -[APSKSession remoteSendFrame:forTime:].cold.2
+ -[APSKSession remoteSendFrame:forTime:].cold.3
+ -[APSKSession remoteSendFrame:forTime:].cold.4
+ -[APSKSession remoteSetAuthString:].cold.1
+ -[APSKSession remoteSetAuthString:].cold.2
+ -[APSKSession remoteSetAuthString:].cold.3
+ -[APSKSession remoteStartToDestination:withOptions:].cold.1
+ -[APSKSession remoteStartToDestination:withOptions:].cold.10
+ -[APSKSession remoteStartToDestination:withOptions:].cold.11
+ -[APSKSession remoteStartToDestination:withOptions:].cold.12
+ -[APSKSession remoteStartToDestination:withOptions:].cold.13
+ -[APSKSession remoteStartToDestination:withOptions:].cold.2
+ -[APSKSession remoteStartToDestination:withOptions:].cold.3
+ -[APSKSession remoteStartToDestination:withOptions:].cold.4
+ -[APSKSession remoteStartToDestination:withOptions:].cold.5
+ -[APSKSession remoteStartToDestination:withOptions:].cold.6
+ -[APSKSession remoteStartToDestination:withOptions:].cold.7
+ -[APSKSession remoteStartToDestination:withOptions:].cold.8
+ -[APSKSession remoteStartToDestination:withOptions:].cold.9
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.1
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.2
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.3
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.4
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.5
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.6
+ -[APSKStreamAudio initWithAudioDescription:delegate:delegateQueue:options:].cold.7
+ -[APSKStreamVideo initWithDelegate:delegateQueue:options:].cold.1
+ APMediaSenderCreate.cold.1
+ APMediaSenderCreate.cold.2
+ APMediaSenderCreate.cold.3
+ APMediaSenderCreate.cold.4
+ APMediaSenderCreate.cold.5
+ APMediaSenderFDVSourceSetDisplayInfoBlock.cold.1
+ APMediaSenderFDVSourceSetWritebackMode.cold.1
+ APMediaSenderFVDSourceCreate.cold.1
+ APMediaSenderFVDSourceCreate.cold.2
+ APMediaSenderGetTypeID.cold.1
+ APMediaSenderStart.cold.1
+ APMediaSenderStop.cold.1
+ APSKServiceDeserializeFrame.cold.1
+ APSKServiceDeserializeFrame.cold.2
+ APSKServiceDeserializeFrame.cold.3
+ APSKServiceDeserializeFrame.cold.4
+ APSKServiceDeserializeFrame.cold.5
+ APSKServiceSerializeFrame.cold.1
+ APSKServiceSerializeFrame.cold.2
+ APSKServiceSerializeFrame.cold.3
+ AudioSBufSourceCreate.cold.1
+ AudioSBufSourceCreate.cold.2
+ AudioSBufSourceCreate.cold.3
+ AudioSBufSourceCreate.cold.4
+ AudioSBufSourceCreate.cold.5
+ AudioSBufSourceGetTypeID.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __29-[APSKSession sendAudioData:]_block_invoke.cold.1
+ __29-[APSKSession sendAudioData:]_block_invoke.cold.2
+ __30-[APSKSession addAudioStream:]_block_invoke.cold.1
+ __30-[APSKSession addAudioStream:]_block_invoke.cold.2
+ __30-[APSKSession addAudioStream:]_block_invoke.cold.3
+ __30-[APSKSession addVideoStream:]_block_invoke.cold.1
+ __30-[APSKSession addVideoStream:]_block_invoke.cold.2
+ __30-[APSKSession addVideoStream:]_block_invoke.cold.3
+ __33-[APSKSession sendFrame:forTime:]_block_invoke.cold.1
+ __33-[APSKSession sendFrame:forTime:]_block_invoke.cold.2
+ __34-[APSKStreamAudio setAudioSender:]_block_invoke.cold.1
+ __34-[APSKStreamAudio setAudioSender:]_block_invoke.cold.2
+ __34-[APSKStreamAudio setAudioSender:]_block_invoke.cold.3
+ __34-[APSKStreamVideo setFrameSender:]_block_invoke.cold.1
+ __34-[APSKStreamVideo setFrameSender:]_block_invoke.cold.2
+ __34-[APSKStreamVideo setFrameSender:]_block_invoke.cold.3
+ __36-[APSKStreamAudio enqueueAudioData:]_block_invoke.5.cold.1
+ __46-[APSKSession startToDestination:withOptions:]_block_invoke.cold.1
+ __86-[APSKSession sendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:]_block_invoke.cold.1
+ __86-[APSKSession sendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:]_block_invoke.cold.2
+ __93-[APSKStreamAudio enqueueAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:]_block_invoke_2.cold.1
+ __APMediaSenderEnqueueAudioDataWithTimestamps_block_invoke.cold.1
+ __APMediaSenderEnqueueAudioDataWithTimestamps_block_invoke.cold.2
+ __APMediaSenderEnqueueAudioDataWithTimestamps_block_invoke.cold.3
+ __APMediaSenderEnqueueAudioDataWithTimestamps_block_invoke.cold.4
+ __APMediaSenderEnqueueAudioData_block_invoke.cold.1
+ __APMediaSenderEnqueueAudioData_block_invoke.cold.2
+ __APMediaSenderEnqueueAudioData_block_invoke.cold.3
+ __APMediaSenderEnqueueAudioData_block_invoke.cold.4
+ __APMediaSenderFVDSourceCreate_block_invoke.cold.1
+ __APMediaSenderFVDSourceCreate_block_invoke.cold.2
+ __APMediaSenderSetAudioDescription_block_invoke.cold.1
+ __APMediaSenderSetAuthBlock_block_invoke.cold.1
+ __APMediaSenderSetDisplayInfoUpdateBlock_block_invoke.cold.1
+ __APMediaSenderSetDisplayInfoUpdateBlock_block_invoke.cold.2
+ __APMediaSenderSetFailureBlock_block_invoke.cold.1
+ __APMediaSenderSetVideoOverrides_block_invoke.cold.1
+ __APMediaSenderSetVideoOverrides_block_invoke.cold.2
+ __APMediaSenderSetVideoPassthroughMode_block_invoke.cold.1
+ __APMediaSenderSetVideoPassthroughMode_block_invoke.cold.2
+ __APMediaSenderSetVideoPassthroughMode_block_invoke.cold.3
+ __APMediaSenderStart_block_invoke.cold.1
+ __APMediaSenderStart_block_invoke.cold.10
+ __APMediaSenderStart_block_invoke.cold.11
+ __APMediaSenderStart_block_invoke.cold.12
+ __APMediaSenderStart_block_invoke.cold.13
+ __APMediaSenderStart_block_invoke.cold.14
+ __APMediaSenderStart_block_invoke.cold.15
+ __APMediaSenderStart_block_invoke.cold.16
+ __APMediaSenderStart_block_invoke.cold.17
+ __APMediaSenderStart_block_invoke.cold.18
+ __APMediaSenderStart_block_invoke.cold.19
+ __APMediaSenderStart_block_invoke.cold.2
+ __APMediaSenderStart_block_invoke.cold.20
+ __APMediaSenderStart_block_invoke.cold.21
+ __APMediaSenderStart_block_invoke.cold.22
+ __APMediaSenderStart_block_invoke.cold.23
+ __APMediaSenderStart_block_invoke.cold.24
+ __APMediaSenderStart_block_invoke.cold.25
+ __APMediaSenderStart_block_invoke.cold.26
+ __APMediaSenderStart_block_invoke.cold.27
+ __APMediaSenderStart_block_invoke.cold.28
+ __APMediaSenderStart_block_invoke.cold.29
+ __APMediaSenderStart_block_invoke.cold.3
+ __APMediaSenderStart_block_invoke.cold.4
+ __APMediaSenderStart_block_invoke.cold.5
+ __APMediaSenderStart_block_invoke.cold.6
+ __APMediaSenderStart_block_invoke.cold.7
+ __APMediaSenderStart_block_invoke.cold.8
+ __APMediaSenderStart_block_invoke.cold.9
+ __APMediaSenderSubmitPixelBuffer_block_invoke.cold.1
+ __APMediaSenderSubmitPixelBuffer_block_invoke.cold.2
+ __APMediaSenderSubmitPixelBuffer_block_invoke.cold.3
+ __APMediaSenderSubmitPixelBuffer_block_invoke.cold.4
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.1
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.2
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.3
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.4
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.5
+ __ausrc_enqueueAudioDataInternal_block_invoke.cold.6
+ __ausrc_enqueueAudioDataInternal_block_invoke_2.cold.1
+ __ausrc_enqueueAudioDataInternal_block_invoke_2.cold.2
+ __ausrc_enqueueAudioDataInternal_block_invoke_2.cold.3
+ __fvdsrc_start_block_invoke.cold.1
+ __fvdsrc_start_block_invoke.cold.2
+ ausrc_enqueueAudioDataInternal.cold.1
+ ausrc_enqueueAudioDataInternal.cold.2
+ ausrc_enqueueAudioDataInternal.cold.3
+ ausrc_enqueueAudioDataInternal.cold.4
+ ausrc_enqueueAudioDataInternal.cold.5
+ ausrc_enqueueAudioDataInternal.cold.6
+ ausrc_enqueueAudioDataInternal.cold.7
+ fvdsrc_finalize.cold.3
+ fvdsrc_plugProcessor.cold.1
+ fvdsrc_submitPixelBufferInternal.cold.1
+ fvdsrc_unplugProcessor.cold.1
+ remoteSessionHandleDeadConnection.cold.1
+ remoteSessionHandleServerDeath.cold.1
+ remoteSessionHandleServerMessage.cold.1
+ sender_finalize.cold.2
+ sender_stopDiscovery.cold.1

```
