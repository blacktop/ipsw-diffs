## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0x179b44
-  __TEXT.__objc_methlist: 0xaec
+1015.5.1.0.0
+  __TEXT.__text: 0x17c184
+  __TEXT.__objc_methlist: 0xb0c
   __TEXT.__const: 0x2762b
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__cstring: 0x33399
+  __TEXT.__gcc_except_tab: 0x89c
+  __TEXT.__cstring: 0x33e1f
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__unwind_info: 0x1d00
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2048
+  __DATA_CONST.__const: 0x20b8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf0
+  __DATA_CONST.__objc_selrefs: 0xc00
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x998
-  __AUTH_CONST.__const: 0x9420
-  __AUTH_CONST.__cfstring: 0xbaa0
-  __AUTH_CONST.__objc_const: 0x1550
+  __DATA_CONST.__got: 0x9a8
+  __AUTH_CONST.__const: 0x9440
+  __AUTH_CONST.__cfstring: 0xbc80
+  __AUTH_CONST.__objc_const: 0x1560
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1e58
+  __AUTH_CONST.__auth_got: 0x1ed8
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x17c40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1715
-  Symbols:   3610
-  CStrings:  5208
+  Functions: 1730
+  Symbols:   3648
+  CStrings:  5271
 
Symbols:
+ +[APAVAudioSessionManager bidirectionalAudioSessionManager]
+ -[AirPlayReceiverPlatform setIsBidirectionalAudioActive:]
+ GCC_except_table1026
+ GCC_except_table1141
+ GCC_except_table1160
+ GCC_except_table1211
+ GCC_except_table1215
+ GCC_except_table1268
+ GCC_except_table1276
+ GCC_except_table1278
+ GCC_except_table1322
+ GCC_except_table1385
+ GCC_except_table427
+ GCC_except_table493
+ GCC_except_table543
+ GCC_except_table607
+ GCC_except_table614
+ GCC_except_table622
+ GCC_except_table760
+ _APAudioFormatGetSupportedTransportAudioFormatsBidirectionalAudioReceiver
+ _APAudioFormatToASBD
+ _APReceiverAudioSessionRealTimeWriteAudio
+ _APReceiverAudioSessionWriteAudio
+ _APSIsBidirectionalAudioReceiverEnabled
+ _AVAudioSessionModeVoiceChat
+ _AirPlayManagedDefaultsLogging_HandleReceiverManagedDefaultsLoggingChanged
+ _AudioComponentFindNext
+ _AudioComponentInstanceDispose
+ _AudioComponentInstanceNew
+ _AudioOutputUnitStart
+ _AudioOutputUnitStop
+ _AudioUnitRender
+ _AudioUnitUninitialize
+ _CFPreferencesAppSynchronize
+ _LogControlCF
+ _MirroredRingBufferFree
+ _MirroredRingBufferInit
+ __InputAudioEnsureTornDown
+ __InputAudioRenderCallback
+ __PostAdvertisingDidChange
+ __SetUpBidirectionalAudioSessionAndPublishID
+ ___59+[APAVAudioSessionManager bidirectionalAudioSessionManager]_block_invoke
+ ____StartAudioSessionsIfNeeded_block_invoke
+ ___audioSession_createAudioInput_block_invoke
+ ___audioSession_createAudioInput_block_invoke_2
+ ___block_descriptor_48_e8_32r_e15_v24?0r^v8r^v16lr32l8
+ ___block_descriptor_76_e8_32o40o_e8_v12?0i8ls32l8s40l8
+ __dispatch_source_type_data_add
+ _audioSession_audioInputEncoderInputCallback
+ _audioSession_destroyAudioInput
+ _bidirectionalAudioSessionManager.onceToken
+ _bidirectionalAudioSessionManager.sessionManager
+ _dispatch_source_merge_data
+ _kAPReceiverAudioSessionOption_InputEncryptionKey
+ _kAPReceiverAudioSessionOption_InputPeerPort
+ _socket
- GCC_except_table1014
- GCC_except_table1127
- GCC_except_table1146
- GCC_except_table1197
- GCC_except_table1201
- GCC_except_table1254
- GCC_except_table1262
- GCC_except_table1264
- GCC_except_table1308
- GCC_except_table1371
- GCC_except_table419
- GCC_except_table482
- GCC_except_table532
- GCC_except_table592
- GCC_except_table596
- GCC_except_table611
- GCC_except_table748
- ___block_descriptor_68_e8_32o40o_e8_v12?0i8ls32l8s40l8
CStrings:
+ "### AudioInput: AudioConverterNew failed: %#m\n"
+ "### AudioInput: socket() failed: %d\n"
+ "### InputAudio: AudioOutputUnitStart failed: %#m\n"
+ "### InputAudio: no VoiceProcessingIO AudioComponent\n"
+ "### Invalid session type: %d.\n"
+ "### Setting BidirectionalAudio AVAudioSession to [%s] failed with error %@\n"
+ "### [%{ptr}] Bidirectional-audio stream requires a bidirectional-audio session\n"
+ "### [%{ptr}] Bidirectional-audio stream requires stream encryption keys\n"
+ "%@ AudioInput (BidirectionalAudio) destroyed\n"
+ "%@ Created audio input session\n"
+ "%@ Creating audio input session\n"
+ "%@ InputAudio setting up\n"
+ "%@ InputAudio setup complete (%u Hz, %u ch, %u bit)\n"
+ "%@ InputAudio torn down\n"
+ "%@ [AudioInput] Overriding peer port to %d]\n"
+ "-[AirPlayReceiverPlatform setIsBidirectionalAudioActive:]"
+ "1015.5.1"
+ "APReceiverAudioSessionRealTimeWriteAudio"
+ "APReceiverAudioSessionWriteAudio"
+ "Added a new %s session.\n"
+ "AirPlayCALMLoudness"
+ "AirPlayServerLoggingLevel"
+ "AirPlayServerLoggingOutput"
+ "AudioInput: APSCryptorEncryptMessage failed: %#m\n"
+ "AudioInput: AudioConverterFillComplexBuffer failed: %#m\n"
+ "AudioInput: sendto errno=%d\n"
+ "BidirectionalAudio"
+ "BidirectionalAudio recording session id published: %lld\n"
+ "BidirectionalAudioSessionID"
+ "InputEncryptionKey"
+ "InputPeerPort"
+ "MediaControlSenderLogControlCF"
+ "Music/"
+ "OSStatus _InputAudioEnsureSetup(APReceiverAudioSessionPlatformRef)"
+ "OSStatus _StartAudioSessionsIfNeeded(AirPlayReceiverSessionRef)_block_invoke"
+ "OSStatus audioSession_createAudioInput(APReceiverAudioSessionRealTimeStateRef, sockaddr_ip, CFDictionaryRef)"
+ "OSStatus audioSession_createAudioInputEncoder(APReceiverAudioSessionRealTimeStateRef)"
+ "Releasing %s session\n"
+ "ServerConnectionInfo"
+ "ServerPort"
+ "Set BidirectionalAudio AVAudioSession to [%s]\n"
+ "TXTRecord"
+ "[%{ptr}] APReceiverAudioSession [%{ptr}] already started\n"
+ "[%{ptr}] Bidirectional-audio session requires HomeKit or account-owner pair-verify\n"
+ "[%{ptr}] General audio setup, stream type %d\n"
+ "[%{ptr}] Starting APReceiverAudioSession [%{ptr}] set up before prepare for media\n"
+ "_InputAudioEnsureSetup"
+ "_InputAudioRenderCallback"
+ "_StartAudioSessionsIfNeeded_block_invoke"
+ "active"
+ "audioSession_createAudioInput"
+ "audioSession_createAudioInputEncoder"
+ "audioSession_initializeInputCryptor"
+ "audioSession_sendAvailableAudioInput"
+ "bidirectionalAudioStream"
+ "com.apple.airplay.audioinput.sender"
+ "com.apple.airplay.bidirectionalAudioSessionIDDidChange"
+ "inactive"
+ "isBidirectionalAudioActive %d -> %d\n"
+ "isBidirectionalAudioSession"
+ "mediaBidirectionalAudio"
+ "mediaStandard"
+ "networkClockAsyncStartDurationMs"
+ "receiverSessionCount: %d -> %d (media %d -> %d)\n"
+ "void _InputAudioEnsureTornDown(APReceiverAudioSessionPlatformRef)"
+ "void _SetUpBidirectionalAudioSessionAndPublishID(AirPlayReceiverPlatform *)"
+ "void audioSession_destroyAudioInput(APReceiverAudioSessionRealTimeStateRef)"
+ "void audioSession_sendAvailableAudioInput(APReceiverAudioSessionRealTimeStateRef)"
- "1005.13.1.1"
- "Added a new AirPlay session.\n"
- "Releasing AirPlay session\n"
- "[%{ptr}] General audio setup\n"
- "receiverSessionCount: %d -> %d\n"
```
