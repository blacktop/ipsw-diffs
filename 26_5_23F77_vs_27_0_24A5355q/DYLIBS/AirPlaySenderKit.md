## AirPlaySenderKit

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/AirPlaySenderKit`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0xc950
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x42c
+980.58.1.11.1
+  __TEXT.__text: 0xfc48
+  __TEXT.__objc_methlist: 0x5f4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x269c
-  __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x96b
-  __TEXT.__objc_methtype: 0x445
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x788
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x18
+  __TEXT.__cstring: 0x2b45
+  __TEXT.__gcc_except_tab: 0x11c
+  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0x210
   __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x8c8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x230
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0xc10
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xac
+  __DATA.__data: 0x2a8
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 583E51DF-DF97-38F8-A7CD-FEB4501BD340
-  Functions: 398
-  Symbols:   1290
-  CStrings:  454
+  UUID: 7BAA4A5A-0303-3635-AE10-8397F6488335
+  Functions: 514
+  Symbols:   1618
+  CStrings:  294
 
Symbols:
+ -[APSKPlaybackInfo .cxx_destruct]
+ -[APSKPlaybackInfo dictionary]
+ -[APSKPlaybackInfo duration]
+ -[APSKPlaybackInfo initForURL:withDictionary:]
+ -[APSKPlaybackInfo mediaURL]
+ -[APSKPlaybackInfo position]
+ -[APSKPlaybackInfo rate]
+ -[APSKPlaybackInfo readyToPlay]
+ -[APSKPlaybackInfo stallCount]
+ -[APSKSession addPlaybackStream:]
+ -[APSKSession localPerformPlaybackAction:withParams:]
+ -[APSKSession localPerformPlaybackAction:withParams:].cold.1
+ -[APSKSession localPerformPlaybackAction:withParams:].cold.2
+ -[APSKSession localPlaybackInfo]
+ -[APSKSession localPlaybackInfo].cold.1
+ -[APSKSession playbackInfo]
+ -[APSKSession remotePerformPlaybackAction:withParams:]
+ -[APSKSession remotePerformPlaybackAction:withParams:].cold.1
+ -[APSKSession remotePerformPlaybackAction:withParams:].cold.2
+ -[APSKSession remotePerformPlaybackAction:withParams:].cold.3
+ -[APSKSession remotePerformPlaybackAction:withParams:].cold.4
+ -[APSKSession remotePlaybackInfo]
+ -[APSKSession remotePlaybackInfo].cold.1
+ -[APSKSession remotePlaybackInfo].cold.2
+ -[APSKSession remotePlaybackInfo].cold.3
+ -[APSKSession remotePlaybackInfo].cold.4
+ -[APSKSession seekToTime:]
+ -[APSKSession setPlaybackRate:]
+ -[APSKSession startPlaybackWithURLString:]
+ -[APSKSession stopPlayback]
+ -[APSKStreamPlayback .cxx_destruct]
+ -[APSKStreamPlayback active]
+ -[APSKStreamPlayback initWithDelegate:delegateQueue:options:]
+ -[APSKStreamPlayback initWithDelegate:delegateQueue:options:].cold.1
+ -[APSKStreamPlayback init]
+ -[APSKStreamPlayback playbackInfo]
+ -[APSKStreamPlayback playing]
+ -[APSKStreamPlayback seekToTime:]
+ -[APSKStreamPlayback setPlaybackControl:]
+ -[APSKStreamPlayback setPlaybackRate:]
+ -[APSKStreamPlayback startPlaybackWithURL:]
+ -[APSKStreamPlayback stopPlayback]
+ GCC_except_table11
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table50
+ _APMediaSenderCopyPlaybackInfo
+ _APMediaSenderPerformPlaybackAction
+ _APSLogUtilsGetSharedLogCategory
+ _CFDictionaryGetDouble
+ _CFDictionarySetDouble
+ _CMTimeGetSeconds
+ _CMTimeMakeWithSeconds
+ _FigCFDictionaryGetCMTimeIfPresent
+ _FigEndpointManagerGetCMBaseObject
+ _FigEndpointPlaybackSessionGetCMBaseObject
+ _OBJC_CLASS_$_APSKPlaybackInfo
+ _OBJC_CLASS_$_APSKStreamPlayback
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_APSKPlaybackInfo._dictionary
+ _OBJC_IVAR_$_APSKPlaybackInfo._urlString
+ _OBJC_IVAR_$_APSKSession._playbackStream
+ _OBJC_IVAR_$_APSKStreamPlayback._delegate
+ _OBJC_IVAR_$_APSKStreamPlayback._delegateQueue
+ _OBJC_IVAR_$_APSKStreamPlayback._options
+ _OBJC_IVAR_$_APSKStreamPlayback._playbackControl
+ _OBJC_IVAR_$_APSKStreamPlayback._queue
+ _OBJC_IVAR_$_APSKStreamPlayback._url
+ _OBJC_METACLASS_$_APSKPlaybackInfo
+ _OBJC_METACLASS_$_APSKStreamPlayback
+ __FigIsNotCurrentDispatchQueue
+ __OBJC_$_INSTANCE_METHODS_APSKPlaybackInfo
+ __OBJC_$_INSTANCE_METHODS_APSKStreamPlayback
+ __OBJC_$_INSTANCE_VARIABLES_APSKPlaybackInfo
+ __OBJC_$_INSTANCE_VARIABLES_APSKStreamPlayback
+ __OBJC_$_PROP_LIST_APSKPlaybackInfo
+ __OBJC_$_PROP_LIST_APSKStreamPlayback
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_APSKPlaybackControl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_APSKPlaybackControl
+ __OBJC_$_PROTOCOL_REFS_APSKPlaybackControl
+ __OBJC_CLASS_RO_$_APSKPlaybackInfo
+ __OBJC_CLASS_RO_$_APSKStreamPlayback
+ __OBJC_LABEL_PROTOCOL_$_APSKPlaybackControl
+ __OBJC_METACLASS_RO_$_APSKPlaybackInfo
+ __OBJC_METACLASS_RO_$_APSKStreamPlayback
+ __OBJC_PROTOCOL_$_APSKPlaybackControl
+ ___26-[APSKSession seekToTime:]_block_invoke
+ ___26-[APSKSession seekToTime:]_block_invoke.cold.1
+ ___26-[APSKSession seekToTime:]_block_invoke.cold.2
+ ___27-[APSKSession playbackInfo]_block_invoke
+ ___27-[APSKSession playbackInfo]_block_invoke.cold.1
+ ___27-[APSKSession playbackInfo]_block_invoke.cold.2
+ ___27-[APSKSession stopPlayback]_block_invoke
+ ___27-[APSKSession stopPlayback]_block_invoke.cold.1
+ ___27-[APSKSession stopPlayback]_block_invoke.cold.2
+ ___28-[APSKStreamPlayback active]_block_invoke
+ ___29-[APSKStreamPlayback playing]_block_invoke
+ ___30-[APSKSession addAudioStream:]_block_invoke.cold.4
+ ___30-[APSKSession addVideoStream:]_block_invoke.cold.4
+ ___31-[APSKSession setPlaybackRate:]_block_invoke
+ ___31-[APSKSession setPlaybackRate:]_block_invoke.cold.1
+ ___31-[APSKSession setPlaybackRate:]_block_invoke.cold.2
+ ___33-[APSKSession addPlaybackStream:]_block_invoke
+ ___33-[APSKSession addPlaybackStream:]_block_invoke.cold.1
+ ___33-[APSKSession addPlaybackStream:]_block_invoke.cold.2
+ ___33-[APSKSession addPlaybackStream:]_block_invoke.cold.3
+ ___33-[APSKSession addPlaybackStream:]_block_invoke.cold.4
+ ___33-[APSKStreamPlayback seekToTime:]_block_invoke
+ ___34-[APSKStreamPlayback playbackInfo]_block_invoke
+ ___34-[APSKStreamPlayback stopPlayback]_block_invoke
+ ___38-[APSKStreamPlayback setPlaybackRate:]_block_invoke
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke.cold.1
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke.cold.2
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke.cold.3
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke_2
+ ___41-[APSKStreamPlayback setPlaybackControl:]_block_invoke_3
+ ___42-[APSKSession startPlaybackWithURLString:]_block_invoke
+ ___42-[APSKSession startPlaybackWithURLString:]_block_invoke.cold.1
+ ___42-[APSKSession startPlaybackWithURLString:]_block_invoke.cold.2
+ ___43-[APSKStreamPlayback startPlaybackWithURL:]_block_invoke
+ ___APMediaSenderCopyPlaybackInfo_block_invoke
+ ___APMediaSenderCopyPlaybackInfo_block_invoke.cold.1
+ ___APMediaSenderCopyPlaybackInfo_block_invoke.cold.2
+ ___APMediaSenderCopyPlaybackInfo_block_invoke.cold.3
+ ___APMediaSenderCopyPlaybackInfo_block_invoke.cold.4
+ ___APMediaSenderPerformPlaybackAction_block_invoke
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.1
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.10
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.11
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.12
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.13
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.14
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.15
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.16
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.17
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.2
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.3
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.4
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.5
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.6
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.7
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.8
+ ___APMediaSenderPerformPlaybackAction_block_invoke.cold.9
+ ___ausrc_enqueueAudioDataInternal_block_invoke.cold.7
+ ___ausrc_enqueueAudioDataInternal_block_invoke_2.cold.4
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.38
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.57
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.67
+ ___block_literal_global.59
+ _kAPEndpointCreationOption_SenderSessionFactory
+ _kAPEndpointManagerProperty_SenderSessionFactory
+ _kAPMediaSenderPlaybackParam_MediaURL
+ _kAPMediaSenderPlaybackParam_Rate
+ _kAPMediaSenderPlaybackParam_SeekTime
+ _kAPSKServiceMsgParamC2S_PlaybackAction
+ _kAPSKServiceMsgParamC2S_PlaybackParams
+ _kAPSKServiceMsgParamS2C_PlaybackInfo
+ _kCMTimeInvalid
+ _kFigEndpointPlaybackSessionKey_ContentLocation
+ _kFigEndpointPlaybackSessionKey_Rate
+ _kFigEndpointPlaybackSessionKey_UUID
+ _kFigEndpointPlaybackSessionPlaybackInfoKey_Duration
+ _kFigEndpointPlaybackSessionPlaybackInfoKey_Position
+ _kFigEndpointPlaybackSessionPlaybackInfoKey_Rate
+ _kFigEndpointPlaybackSessionPlaybackInfoKey_ReadyToPlay
+ _kFigEndpointPlaybackSessionPlaybackInfoKey_StallCount
+ _malloc_type_malloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$absoluteString
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$initForURL:withDictionary:
+ _objc_msgSend$localPerformPlaybackAction:withParams:
+ _objc_msgSend$localPlaybackInfo
+ _objc_msgSend$longValue
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$playbackInfo
+ _objc_msgSend$playbackStreamDidStart:
+ _objc_msgSend$playbackStreamDidStop:
+ _objc_msgSend$remotePerformPlaybackAction:withParams:
+ _objc_msgSend$remotePlaybackInfo
+ _objc_msgSend$seekToTime:
+ _objc_msgSend$setPlaybackControl:
+ _objc_msgSend$setPlaybackRate:
+ _objc_msgSend$startPlaybackWithURLString:
+ _objc_msgSend$stopPlayback
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
+ _playbackInfoCompletionCallback
+ _playbackSessionEventHandler
- GCC_except_table36
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.56
- ___block_literal_global.48
- _objc_release_x25
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "### [%{ptr}] media sender: get playback info timed out\n"
+ "-[APSKSession addPlaybackStream:]_block_invoke"
+ "-[APSKSession localPerformPlaybackAction:withParams:]"
+ "-[APSKSession localPlaybackInfo]"
+ "-[APSKSession playbackInfo]_block_invoke"
+ "-[APSKSession remotePerformPlaybackAction:withParams:]"
+ "-[APSKSession remotePlaybackInfo]"
+ "-[APSKSession seekToTime:]_block_invoke"
+ "-[APSKSession setPlaybackRate:]_block_invoke"
+ "-[APSKSession startPlaybackWithURLString:]_block_invoke"
+ "-[APSKSession stopPlayback]_block_invoke"
+ "-[APSKStreamPlayback initWithDelegate:delegateQueue:options:]"
+ "-[APSKStreamPlayback setPlaybackControl:]_block_invoke"
+ "APMediaSenderPerformPlaybackAction_block_invoke"
+ "CFDictionaryRef sender_copyPlaybackInfoInternal(APMediaSenderRef)"
+ "MediaURL"
+ "Not running on expected queue at %s:%d"
+ "OSStatus createEndpointForNetworkAddress(APMediaSenderRef, CFStringRef, FigEndpointRef *)"
+ "OSStatus createEndpointForNetworkAddress(APMediaSenderRef, CFStringRef, FigEndpointRef *)_block_invoke"
+ "PlaybackRate"
+ "SeekTime"
+ "[%{ptr}] playback stream initialized"
+ "[%{ptr}] playback stream started"
+ "[%{ptr}] playback stream stopped"
+ "[%{ptr}] session: added playback stream %{ptr}"
+ "com.apple.apskstreamplayback.delegateq"
+ "com.apple.apskstreamplayback.stateq"
+ "playbackAction"
+ "playbackInfo"
+ "playbackInfoCompletionCallback"
+ "playbackParams"
+ "sender_copyPlaybackInfoInternal"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<APSKAudioSender>\""
- "@\"<APSKFrameSender>\""
- "@\"<APSKSessionDelegate>\""
- "@\"<APSKStreamAudioDelegate>\""
- "@\"<APSKStreamVideoDelegate>\""
- "@\"<NSObject>\""
- "@\"APSKStreamAudio\""
- "@\"APSKStreamVideo\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8r^{AudioStreamBasicDescription=dIIIIIIII}16@24@32@40"
- "@?16@0:8"
- "AI"
- "APSKAudioSender"
- "APSKDestination"
- "APSKFrameSender"
- "APSKSession"
- "APSKStreamAudio"
- "APSKStreamVideo"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "I16@0:8"
- "NSObject"
- "OSStatus createEndpointForNetworkAddress(CFStringRef, FigEndpointRef *)"
- "OSStatus createEndpointForNetworkAddress(CFStringRef, FigEndpointRef *)_block_invoke"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,R,N"
- "TB,N"
- "TB,R,N"
- "TQ,R"
- "Ti,R,N"
- "UTF8String"
- "Vv16@0:8"
- "^v"
- "^v16@0:8"
- "^{APSRealTimeSignalPrivate=}"
- "^{APSRingBufferPrivate=}"
- "^{OpaqueAPMediaSender=}"
- "^{OpaqueFigXPCRemoteClient=}"
- "^{_NSZone=}16@0:8"
- "_asbd"
- "_audioSender"
- "_audioStream"
- "_client"
- "_delegate"
- "_delegateQueue"
- "_destinationType"
- "_failurePosted"
- "_frameSender"
- "_height"
- "_objectID"
- "_options"
- "_passcode"
- "_queue"
- "_refreshRate"
- "_remote"
- "_rtQueue"
- "_rtRingBuffer"
- "_rtRingBufferEntries"
- "_rtSignal"
- "_sender"
- "_senderNotifObserver"
- "_state"
- "_useVideoLatency"
- "_value"
- "_videoStream"
- "_width"
- "active"
- "addAudioStream:"
- "addObserverForName:object:queue:usingBlock:"
- "addVideoStream:"
- "asbd"
- "audioStreamDidFail:withError:"
- "audioStreamDidStart:"
- "audioStreamDidStop:"
- "autorelease"
- "boolValue"
- "bytes"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "destinationType"
- "displayRefreshRate"
- "enqueueAudioData:"
- "enqueueAudioDataBlock"
- "enqueueAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:"
- "enqueueFrame:forTime:"
- "handleAuthRequired:"
- "handleFailure:"
- "handleStartCompletion:"
- "handleUpdatedDisplayWidth:height:refreshRate:"
- "handleVideoStreamErrorNotification:"
- "hash"
- "i"
- "i16@0:8"
- "i24@0:8@\"NSData\"16"
- "i24@0:8@16"
- "i32@0:8@16@24"
- "i32@0:8^{__CVBuffer=}16q24"
- "i60@0:8@\"NSData\"16{?=qiIq}24Q48B56"
- "i60@0:8@16{?=qiIq}24Q48B56"
- "init"
- "initWithAudioDescription:delegate:delegateQueue:options:"
- "initWithDelegate:delegateQueue:"
- "initWithDelegate:delegateQueue:options:"
- "initWithDiscoveryInfo:"
- "initWithEndpointID:"
- "initWithEndpointName:"
- "initWithLength:"
- "initWithNetworkAddress:"
- "intValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "localSendAudioData:"
- "localSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:"
- "localSendFrame:forTime:"
- "localSetAuthString:"
- "localStartToDestination:withOptions:"
- "localStop"
- "mutableBytes"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "propertyListWithData:options:format:error:"
- "r^{AudioStreamBasicDescription=dIIIIIIII}16@0:8"
- "release"
- "remoteSendAudioData:"
- "remoteSendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:"
- "remoteSendFrame:forTime:"
- "remoteSetAuthString:"
- "remoteStartToDestination:withOptions:"
- "remoteStop"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAudioData:"
- "sendAudioDataWithTimestamps:forHostTime:forSampleTime:forDiscontinuity:"
- "sendFrame:forTime:"
- "sessionAuthRequired:forAuthType:"
- "sessionDidFail:withError:"
- "setAudioSender:"
- "setAuthString:"
- "setDisplayWidth:height:refreshRate:"
- "setError:"
- "setFrameSender:"
- "setUseVideoLatency:"
- "startToDestination:withOptions:"
- "stop"
- "superclass"
- "usageModes"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v28@0:8i16i20i24"
- "v32@0:8@16@24"
- "value"
- "videoStreamDidFail:withError:"
- "videoStreamDidStart:"
- "videoStreamDidStop:"
- "videoStreamDisplayInfoDidUpdate:"
- "zone"
- "{AudioStreamBasicDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"

```
