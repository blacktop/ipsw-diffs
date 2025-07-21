## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-870.10.1.0.0
-  __TEXT.__text: 0x1e1070
-  __TEXT.__auth_stubs: 0x50e0
+870.12.2.0.0
+  __TEXT.__text: 0x1e0a28
+  __TEXT.__auth_stubs: 0x50d0
   __TEXT.__objc_methlist: 0x67c
-  __TEXT.__cstring: 0x744fa
+  __TEXT.__cstring: 0x741f1
   __TEXT.__const: 0xfd80
   __TEXT.__gcc_except_tab: 0x94c
   __TEXT.__dlopen_cstrs: 0x61d
   __TEXT.__oslogstring: 0x6da
-  __TEXT.__unwind_info: 0x49f0
+  __TEXT.__unwind_info: 0x49e0
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x1a01

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7c8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2880
+  __AUTH_CONST.__auth_got: 0x2878
   __AUTH_CONST.__const: 0x77e0
   __AUTH_CONST.__cfstring: 0x10ea0
   __AUTH_CONST.__objc_const: 0xb88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF59C2BE-6F37-34AF-A0E2-54E948C8770F
+  UUID: 9628AEDF-B6A5-305A-97CC-58E975E02B5E
   Functions: 8764
-  Symbols:   22372
-  CStrings:  12080
+  Symbols:   22357
+  CStrings:  12051
 
Symbols:
+ _FigSignalErrorAt
+ ___block_descriptor_tmp.505
+ ___block_descriptor_tmp.547
+ ___block_descriptor_tmp.549
- _FigSignalErrorAt3
- ___block_descriptor_tmp.510
- ___block_descriptor_tmp.514
- ___block_descriptor_tmp.552
- ___block_descriptor_tmp.554
- _fig_log_get_emitter
Functions (modified):
~ _apsession_ensureConnectedInternal : 12372 -> 12376
~ _OUTLINED_FUNCTION_11 : 28 -> 12
~ _session_PerformRemoteAction : 904 -> 856
~ _APVirtualDisplayTestSinkCreate.cold.3 : 196 -> 132
~ _APEndpointStreamAggregateAudioCreate.cold.7 : 160 -> 96
~ _endpoint_updateVideoPlaybackIsActive.cold.2 : 172 -> 84
~ _session_handleRemoteControlSessionEvent : 528 -> 408
~ _session_handleRemoteControlSessionEventInternal : 1276 -> 1112
~ _session_performActionUnhandledURLResponseCompletion : 340 -> 212
~ _session_createDataFromDictionary.cold.1 : 140 -> 64
~ _session_Play.cold.1 : 132 -> 72
~ _session_InsertPlayQueueItem.cold.1 : 132 -> 72
~ _session_InsertPlayQueueItem.cold.2 : 140 -> 72
~ _session_PerformRemoteAction.cold.2 : 136 -> 68
~ _session_PerformRemoteAction.cold.3 : 136 -> 68
~ _session_addPendingRequest.cold.1 : 160 -> 88
~ _session_addPendingRequest.cold.2 : 140 -> 68
~ _session_addPendingRequest.cold.3 : 140 -> 68
~ _session_createDictionaryFromData.cold.1 : 164 -> 76
~ _session_insertPlayQueueItemInternal.cold.1 : 132 -> 72
~ _session_insertPlayQueueItemInternal.cold.13 : 160 -> 72
~ _session_insertPlayQueueItemInternal.cold.14 : 140 -> 72

Functions (added):
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_0
+ _APMessageRingCreate.cold.1
+ _APMessageRingBufferedCreate.cold.2
+ _APEndpointDescriptionGetClassID.cold.1
+ _APSenderSessionGetClassID.cold.1
+ _APAudioHoseManagerBufferedGetClassID.cold.1
+ _APAudioHoseManagerBufferedCreate.cold.1

Functions (removed):
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_1
- [3 functions removed in block]
- sub_1d14c28b4
- sub_1d14e9a00
CStrings:
+ "870.12.2"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "(Fig)"
- "870.10.1"
- "APEndpoint.c"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "Cannot register path"
- "Failed to create deep copy"
- "Failed to de-serialize"
- "Failed to serialize"
- "Item is NULL"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "Object invalidated"
- "alloc failed"
- "can't find valid video track"
- "err"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kFigBaseObjectError_AllocationFailed"
- "kFigBaseObjectError_ValueNotAvailable"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_InvalidParameter"
- "messageID is missing in response event"
- "type is missing in response event"

```
