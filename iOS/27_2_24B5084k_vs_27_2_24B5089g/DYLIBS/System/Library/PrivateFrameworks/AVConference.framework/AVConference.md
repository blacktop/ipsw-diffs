## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2260.9.1.0.0
-  __TEXT.__text: 0x7d5e08
-  __TEXT.__objc_methlist: 0x3ab38
+2260.11.1.0.0
+  __TEXT.__text: 0x7d6d8c
+  __TEXT.__objc_methlist: 0x3ac38
   __TEXT.__const: 0xc680
-  __TEXT.__cstring: 0x9f767
-  __TEXT.__oslogstring: 0x1431d7
-  __TEXT.__gcc_except_tab: 0x2dbc
+  __TEXT.__cstring: 0x9f784
+  __TEXT.__oslogstring: 0x1435e0
+  __TEXT.__gcc_except_tab: 0x2dc8
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1b6a8
+  __TEXT.__unwind_info: 0x1b6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18dd0
+  __DATA_CONST.__objc_selrefs: 0x18e40
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1260
   __DATA_CONST.__objc_arraydata: 0x27d8
-  __DATA_CONST.__got: 0x1e48
+  __DATA_CONST.__got: 0x1dd8
   __AUTH_CONST.__const: 0x4588
-  __AUTH_CONST.__cfstring: 0x29de0
-  __AUTH_CONST.__objc_const: 0x6d0e8
+  __AUTH_CONST.__cfstring: 0x29e00
+  __AUTH_CONST.__objc_const: 0x6d1d8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52f8
   __AUTH_CONST.__objc_arrayobj: 0x1d88
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x2c60
+  __AUTH_CONST.__auth_got: 0x2c68
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x772c
-  __DATA.__data: 0x7ce8
+  __DATA.__objc_ivar: 0x7748
+  __DATA.__data: 0x7c68
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xcee0
   __DATA_DIRTY.__data: 0x420

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35478
-  Symbols:   53127
-  CStrings:  34109
+  Functions: 35503
+  Symbols:   53162
+  CStrings:  34121
 
Symbols:
+ +[VCAudioToolboxAudioComponentMock activeInstanceCount]
+ +[VCAudioToolboxAudioComponentMock isMockingSessionActive]
+ -[VCAVFoundationCapture secondaryCameraRequestSizeForAspectRatio:]
+ -[VCAudioToolboxAudioComponentMock autorelease]
+ -[VCAudioToolboxAudioComponentMock release]
+ -[VCAudioToolboxAudioComponentMock retainCount]
+ -[VCAudioToolboxAudioComponentMock retain]
+ -[VCAudioTransmitterConfig setShouldCapBitrateForWatchRelay:]
+ -[VCAudioTransmitterConfig shouldCapBitrateForWatchRelay]
+ -[VCCallSession isRemoteWatchRelayDeviceWithDeviceType:]
+ -[VCCoreAudio_AudioUnitMock autorelease]
+ -[VCCoreAudio_AudioUnitMock beginSession]
+ -[VCCoreAudio_AudioUnitMock endSession]
+ -[VCCoreAudio_AudioUnitMock isMockingEnabled]
+ -[VCCoreAudio_AudioUnitMock release]
+ -[VCCoreAudio_AudioUnitMock retainCount]
+ -[VCCoreAudio_AudioUnitMock retain]
+ -[VCRTPHistory dealloc]
+ -[VCVideoStream canReuseTransportsForStreamConfigs:]
+ -[VCVideoStream expectedTransportArrayCountForStreamConfigs:]
+ -[VCVideoStream transportArrayContainsRTXTransport]
+ -[VCVideoStream transportStreamCountForStreamConfig:]
+ -[VCVideoStream willCreateRTXTransportForStreamConfig:]
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table210
+ GCC_except_table314
+ GCC_except_table368
+ GCC_except_table452
+ _OBJC_IVAR_$_VCAVFoundationCapture._dualCaptureRear1440x1080
+ _OBJC_IVAR_$_VCAudioToolboxAudioComponentMock._instancesLock
+ _OBJC_IVAR_$_VCAudioTransmitter._shouldCapBitrateForWatchRelay
+ _OBJC_IVAR_$_VCAudioTransmitterConfig._shouldCapBitrateForWatchRelay
+ _OBJC_IVAR_$_VCMockIDSDatagramChannel._enqueueLock
+ _OBJC_IVAR_$_VCMockIDSDatagramChannel._queueLock
+ _OBJC_IVAR_$_VCSession._remoteParticipantsMapLock
+ _objc_getAssociatedObject
+ _objc_msgSend$activeInstanceCount
+ _objc_msgSend$canReuseTransportsForStreamConfigs:
+ _objc_msgSend$expectedTransportArrayCountForStreamConfigs:
+ _objc_msgSend$isMockingEnabled
+ _objc_msgSend$isMockingSessionActive
+ _objc_msgSend$isRemoteWatchRelayDeviceWithDeviceType:
+ _objc_msgSend$secondaryCameraRequestSizeForAspectRatio:
+ _objc_msgSend$setShouldCapBitrateForWatchRelay:
+ _objc_msgSend$shouldCapBitrateForWatchRelay
+ _objc_msgSend$transportArrayContainsRTXTransport
+ _objc_msgSend$transportStreamCountForStreamConfig:
+ _objc_msgSend$willCreateRTXTransportForStreamConfig:
+ _objc_setAssociatedObject
- -[VCAudioToolboxAudioComponentMock dealloc]
- -[VCCoreAudio_AudioUnitMock dealloc]
- GCC_except_table138
- GCC_except_table140
- GCC_except_table142
- GCC_except_table144
- GCC_except_table146
- GCC_except_table211
- GCC_except_table313
- GCC_except_table36
- GCC_except_table367
- GCC_except_table451
- ___30-[VCSession participantForID:]_block_invoke
- __audioComponentMockLock
- __audioUnitMockLock
- __weakAudioComponentMockInstance
- __weakAudioUnitMockInstance
- _objc_loadWeakRetained
CStrings:
+ " [%s] %s:%d %@(%p) Failed to allocate the active instances set"
+ " [%s] %s:%d %@(%p) Failed to init the instances lock"
+ " [%s] %s:%d %@(%p) [FTDC] No desired secondary capture formats: no video device format matches width=%d, height=%d, aspectRatio=%d among %lu multicam candidates of %lu total"
+ " [%s] %s:%d %@(%p) [FTDC] No exact %dx%d rear format (picker chose %dx%d); falling back to %dx%d"
+ " [%s] %s:%d Failed to allocate _enqueueLock"
+ " [%s] %s:%d Failed to allocate _queueLock"
+ " [%s] %s:%d Failed to allocate the active instances set"
+ " [%s] %s:%d Failed to init the instances lock"
+ " [%s] %s:%d [FTDC] No desired secondary capture formats: no video device format matches width=%d, height=%d, aspectRatio=%d among %lu multicam candidates of %lu total"
+ " [%s] %s:%d [FTDC] No exact %dx%d rear format (picker chose %dx%d); falling back to %dx%d"
+ " [%s] %s:%d beginSession: %lu audio unit mock instance(s) carried over from a previous session"
+ " [%s] %s:%d beginSession: %lu component mock instance(s) leaked from a previous session (never disposed)"
+ "-[VCAudioToolboxAudioComponentMock init]"
+ "-[VCCoreAudio_AudioUnitMock beginSession]"
+ "2260.11.1"
+ "VCVideoStream [%s] %s:%d %@(%p) Rebuilding transports for reconfigure. currentCount=%u expectedCount=%u localSSRCChanged=%d canReuse=%d"
+ "VCVideoStream [%s] %s:%d Rebuilding transports for reconfigure. currentCount=%u expectedCount=%u localSSRCChanged=%d canReuse=%d"
+ "dualCaptureRear1440x1080"
- " [%s] %s:%d %@(%p) no streams available"
- " [%s] %s:%d no streams available"
- "-[VCSessionUplinkVideoStreamController anchorStreamIDWithCappedVideoStreamIDs:]"
- "2260.9.1"
- "VCVideoStream [%s] %s:%d %@(%p) Reconfiguring VCVideoStream with a different number of transports."
- "VCVideoStream [%s] %s:%d Reconfiguring VCVideoStream with a different number of transports."
```
