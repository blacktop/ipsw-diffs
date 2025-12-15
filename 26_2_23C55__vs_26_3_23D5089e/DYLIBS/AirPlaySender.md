## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-925.5.1.1.0
-  __TEXT.__text: 0x21401c
+935.3.1.0.0
+  __TEXT.__text: 0x214440
   __TEXT.__auth_stubs: 0x5690
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x83734
+  __TEXT.__cstring: 0x83a88
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__dlopen_cstrs: 0x671

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27B0FDC2-DAEC-39C5-A4ED-7E50649AB803
-  Functions: 9788
-  Symbols:   24646
-  CStrings:  13571
+  UUID: 4389F737-4ECF-32F9-9F29-B82E4C079860
+  Functions: 9792
+  Symbols:   24658
+  CStrings:  13601
 
Symbols:
+ _FigSignalErrorAt3
+ ___block_descriptor_tmp.124
- _FigSignalErrorAtGM
Functions:
~ _OUTLINED_FUNCTION_4 : 20 -> 12
+ _OUTLINED_FUNCTION_4
~ _OUTLINED_FUNCTION_2 : 12 -> 16
~ _OUTLINED_FUNCTION_9 : 40 -> 24
~ _OUTLINED_FUNCTION_9 : 12 -> 40
+ _OUTLINED_FUNCTION_137
~ _OUTLINED_FUNCTION_1 : 28 -> 20
~ _OUTLINED_FUNCTION_7 : 24 -> 12
~ _OUTLINED_FUNCTION_7 : 12 -> 20
~ _OUTLINED_FUNCTION_7 : 20 -> 12
~ _OUTLINED_FUNCTION_10 : 24 -> 12
~ _OUTLINED_FUNCTION_3 : 12 -> 16
- _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_12
~ _OUTLINED_FUNCTION_5 : 12 -> 20
- _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_11
~ _session_PerformRemoteAction : 1032 -> 1072
+ _OUTLINED_FUNCTION_15
~ _APVirtualDisplayTestSinkCreate.cold.3 : 140 -> 196
~ _APEndpointStreamAggregateAudioCreate.cold.7 : 104 -> 160
~ _audioEngineBufferedAdapter_Resume_Stage1.cold.21 : 120 -> 176
~ _endpoint_updateVideoPlaybackIsActive.cold.2 : 128 -> 172
~ _session_handleRemoteControlSessionEvent : 632 -> 692
~ _session_handleRemoteControlSessionEventInternal : 1364 -> 1432
~ _session_performActionUnhandledURLResponseCompletion : 424 -> 492
~ _session_createDataFromDictionary.cold.1 : 92 -> 140
~ _session_Play.cold.1 : 100 -> 132
~ _session_InsertPlayQueueItem.cold.1 : 100 -> 132
~ _session_InsertPlayQueueItem.cold.2 : 96 -> 140
~ _session_PerformRemoteAction.cold.2 : 100 -> 136
~ _session_PerformRemoteAction.cold.3 : 100 -> 136
~ _session_addPendingRequest.cold.1 : 116 -> 160
~ _session_addPendingRequest.cold.2 : 104 -> 140
~ _session_addPendingRequest.cold.3 : 104 -> 140
~ _session_createDictionaryFromData.cold.1 : 112 -> 164
~ _session_insertPlayQueueItemInternal.cold.1 : 100 -> 132
~ _session_insertPlayQueueItemInternal.cold.13 : 108 -> 160
~ _session_insertPlayQueueItemInternal.cold.14 : 96 -> 140
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "935.3.1"
+ "APAudioEngineBufferedAdapter.c"
+ "APEndpoint.m"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APVirtualDisplayTestSink.c"
+ "Action not supported"
+ "Allocation error"
+ "Cannot register path"
+ "Failed allocating audio buffer"
+ "Failed to create deep copy"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Item is NULL"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "Object invalidated"
+ "alloc failed"
+ "can't find valid video track"
+ "err"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "kFigEndpointStreamAudioEngineError_AllocationFailed"
+ "messageID is missing in response event"
+ "type is missing in response event"
- "%s signalled err=%d at <>:%d"
- "925.5.1.1"

```
