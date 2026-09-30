## OctaviaHalogen

> `/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen`

```diff

-3235.10.1.0.0
-  __TEXT.__text: 0x2d5ec
-  __TEXT.__auth_stubs: 0x1270
+3235.12.2.0.0
+  __TEXT.__text: 0x13bfc
+  __TEXT.__auth_stubs: 0x1200
   __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__const: 0x288
-  __TEXT.__cstring: 0x2a70
-  __TEXT.__oslogstring: 0x49a0
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0xe33
+  __TEXT.__oslogstring: 0xb0c
   __TEXT.__objc_methname: 0xb6
-  __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x940
-  __DATA_CONST.__got: 0x468
+  __TEXT.__unwind_info: 0x3f0
+  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x15f8
-  __DATA_CONST.__cfstring: 0xc20
+  __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x70
-  __DATA.__common: 0xb0
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B6988EA-11AC-3EC0-A51A-6335C40B5DDC
-  Functions: 532
-  Symbols:   454
-  CStrings:  774
+  UUID: 34C3D3FD-A712-3B58-A7AB-812C663834AF
+  Functions: 336
+  Symbols:   446
+  CStrings:  292
 
Symbols:
+ _FigSignalErrorAt
- _CMBlockBufferGetDataPointer
- _CMSampleBufferGetDuration
- _CMSampleBufferGetPresentationTimeStamp
- _CMTimeGetSeconds
- _FigSignalErrorAt3
- __DefaultRuneLocale
- ___maskrune
- _fig_note_initialize_category_with_default_work_cf
- _strlen
Functions (modified):
~ _FigNeroEndpointManagerGetShared : 428 -> 372
~ _FigNeroEndpointManagerForCameraPreviewGetShared : 428 -> 372
~ _FigOctaviaHALPlugin_Create : 576 -> 248

Functions (added):
+ sub_1080
+ sub_109c
+ sub_1784
+ sub_21e8
+ [4 functions added in block]
+ sub_265c
+ sub_26b8
+ sub_2914
+ [3 functions added in block]
+ sub_3008
+ sub_36dc
+ sub_385c
+ sub_3ef0
+ sub_4904
+ sub_49a0
+ sub_5644
+ sub_5718
+ sub_5910
+ sub_59ac
+ sub_5a38
+ sub_61c4
+ sub_653c
+ sub_6c70
+ sub_78b4
+ sub_7c84
+ sub_8104
+ sub_856c
+ sub_8634
+ sub_86e8
+ [4 functions added in block]
+ sub_8a4c
+ sub_8b00
+ sub_8ec4
+ sub_91a0
+ sub_91c0
+ sub_9414
+ sub_9594
+ sub_9820
+ [3 functions added in block]
+ sub_9ea4
+ sub_a480
+ sub_a4ac
+ sub_a67c
+ sub_a6dc
+ sub_a780
+ sub_abc4
+ sub_b554
+ sub_b65c
+ sub_b6d8
+ sub_b874
+ sub_bbdc
+ sub_bc8c
+ sub_d5ac
+ sub_e570
+ sub_e74c
+ sub_ea9c
+ sub_ed10
+ [4 functions added in block]
+ sub_fad0
+ sub_fc20
+ sub_10730
+ sub_11290
+ sub_112c0
+ sub_112f0
+ sub_11cfc
+ sub_12120
+ sub_1216c
+ sub_12428
+ sub_12544
+ sub_12558
+ sub_12f24
+ [3 functions added in block]
+ sub_13654
+ sub_137f4
+ sub_13fd4
+ sub_14abc

Functions (removed):
- sub_f48
- sub_1780
- sub_2234
- sub_2414
- sub_2f40
- sub_37f4
- sub_39b0
- [6 functions removed in block]
- sub_507c
- [4 functions removed in block]
- sub_516c
- [3 functions removed in block]
- sub_611c
- sub_6768
- [6 functions removed in block]
- sub_7180
- [3 functions removed in block]
- [4 functions removed in block]
- sub_98cc
- sub_9bac
- sub_9e28
- [6 functions removed in block]
- sub_d1a8
- [3 functions removed in block]
- [3 functions removed in block]
- sub_fa74
- sub_faa4
- sub_fbd0
- sub_10a48
- sub_10d30
- sub_10eb4
- sub_116e4
- sub_11978
- [9 functions removed in block]
- sub_121cc
- sub_1250c
- sub_12710
- sub_12ccc
- sub_13324
- sub_1351c
- [4 functions removed in block]
- [7 functions removed in block]
- [4 functions removed in block]
- sub_13dcc
- sub_13e04
- [3 functions removed in block]
- [4 functions removed in block]
- [22 functions removed in block]
- sub_14188
- sub_141a0
- [6 functions removed in block]
- [5 functions removed in block]
- [4 functions removed in block]
- [4 functions removed in block]
- sub_14750
- sub_14da0
- sub_155c8
- sub_15c1c
- sub_1603c
- sub_165a4
- sub_165c4
- sub_17128
- sub_17484
- sub_17d8c
- sub_17fc0
- sub_18728
- sub_18b78
- sub_18bc4
- [3 functions removed in block]
- sub_18c60
- sub_18c74
- sub_18ca4
- sub_18ccc
- sub_18ce4
- sub_18d24
- sub_18d30
- [7 functions removed in block]
- sub_1a51c
- sub_1b564
- sub_1be9c
- sub_1c33c
- sub_1ce60
- [3 functions removed in block]
- sub_1ea78
- sub_1ec68
- sub_1ef98
- sub_1f344
- sub_1f3f0
- [6 functions removed in block]
- [3 functions removed in block]
- [4 functions removed in block]
- sub_210c0
- [3 functions removed in block]
- sub_21374
- [13 functions removed in block]
- sub_214c8
- sub_214e8
- sub_226cc
- sub_22b44
- sub_22bb4
- sub_22dd0
- sub_22e84
- sub_23070
- sub_2352c
- [13 functions removed in block]
- sub_24654
- [4 functions removed in block]
- sub_25ff0
- sub_27278
- sub_27abc
- [3 functions removed in block]
- [3 functions removed in block]
- [5 functions removed in block]
- [4 functions removed in block]
- sub_2aee4
- [9 functions removed in block]
- sub_2bbe4
- [10 functions removed in block]
- sub_2dfa0
- sub_2e4a8
CStrings:
+ "nmanager_SetProperty_block_invoke_3"
- "! deviceInfo"
- "! endpointID"
- "! endpointOut"
- "! streamOut"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "<<< hud layer >>> %s: %@"
- "<<< neroHALDevice >>>"
- "<<< neroHALDevice >>> %s:   bitsPerChannel   : %d"
- "<<< neroHALDevice >>> %s:   bytesPerFrame    : %d"
- "<<< neroHALDevice >>> %s:   bytesPerPacket   : %d"
- "<<< neroHALDevice >>> %s:   channelsPerFrame : %d"
- "<<< neroHALDevice >>> %s:   formatFlags      : 0x%x"
- "<<< neroHALDevice >>> %s:   formatID         : %c%c%c%c"
- "<<< neroHALDevice >>> %s:   framesPerPacket  : %d"
- "<<< neroHALDevice >>> %s:   kAudioFormatLinearPCM : Clearing kAudioFormatFlagIsNonMixableFlag from the list being sent up to the HAL. Updated formatFlags 0x%x"
- "<<< neroHALDevice >>> %s:   sampleRate       : %.0f"
- "<<< neroHALDevice >>> %s:  Audio Endpoint Stream resume timed out. Continuing Async"
- "<<< neroHALDevice >>> %s:  kAudioFormatLinearPCM : Restoring kAudioFormatFlagIsNonMixable Flag to the formatList being sent to the dongle. Updated formatFlags 0x%x"
- "<<< neroHALDevice >>> %s: %d, %lld, %llu, %llu, hostTime %llu, sampleTime %.0f"
- "<<< neroHALDevice >>> %s: Audio Endpoint Stream suspend timed out."
- "<<< neroHALDevice >>> %s: [%p] called"
- "<<< neroHALDevice >>> %s: created %p transportType %c%c%c%c"
- "<<< neroHALDevice >>> %s: desired sample rate is now %d (was %d)"
- "<<< neroHALDevice >>> %s: format %d: "
- "<<< neroHALDevice >>> %s: not expecting kAudioDevicePropertyAvailableNominalSampleRates to be queried... fix me!"
- "<<< neroHALInputStream >>>"
- "<<< neroHALInputStream >>> %s:   Bits per channel %d"
- "<<< neroHALInputStream >>> %s:   Bytes per Frame %d"
- "<<< neroHALInputStream >>> %s:   Bytes per packet %d"
- "<<< neroHALInputStream >>> %s:   Channels per Frame %d"
- "<<< neroHALInputStream >>> %s:   Format Flags 0x%x"
- "<<< neroHALInputStream >>> %s:   Frames per packet %d"
- "<<< neroHALInputStream >>> %s: Audio format set to %c%c%c%c %.0f"
- "<<< neroHALInputStream >>> %s: [%p] called"
- "<<< neroHALInputStream >>> %s: created %p"
- "<<< neroHALInputStream >>> %s: mSampleRate = %f, mFormatID = %c%c%c%c"
- "<<< neroHALInputStream >>> %s: mSelector = %c%c%c%c"
- "<<< neroHALOutputStream >>>"
- "<<< neroHALOutputStream >>> %s:   Bits per channel %d"
- "<<< neroHALOutputStream >>> %s:   Bytes per Frame %d"
- "<<< neroHALOutputStream >>> %s:   Bytes per packet %d"
- "<<< neroHALOutputStream >>> %s:   Channels per Frame %d"
- "<<< neroHALOutputStream >>> %s:   Format Flags 0x%x"
- "<<< neroHALOutputStream >>> %s:   Frames per packet %d"
- "<<< neroHALOutputStream >>> %s:   bitsPerChannel   : %d"
- "<<< neroHALOutputStream >>> %s:   bytesPerFrame    : %d"
- "<<< neroHALOutputStream >>> %s:   bytesPerPacket   : %d"
- "<<< neroHALOutputStream >>> %s:   channelsPerFrame : %d"
- "<<< neroHALOutputStream >>> %s:   formatFlags      : 0x%x"
- "<<< neroHALOutputStream >>> %s:   formatID         : %c%c%c%c"
- "<<< neroHALOutputStream >>> %s:   framesPerPacket  : %d"
- "<<< neroHALOutputStream >>> %s:   sampleRate       : %.0f"
- "<<< neroHALOutputStream >>> %s:  kAudioFormatLinearPCM: Restoring kAudioFormatFlagIsNonMixable Flag to the formatList being sent to the dongle. Updated formatFlags 0x%x"
- "<<< neroHALOutputStream >>> %s: Audio format set to %c%c%c%c %.0f"
- "<<< neroHALOutputStream >>> %s: [%p] called"
- "<<< neroHALOutputStream >>> %s: created %p"
- "<<< neroHALOutputStream >>> %s: format %d:"
- "<<< neroHALOutputStream >>> %s: mSampleRate = %f, mFormatID = %c%c%c%c"
- "<<< neroHALOutputStream >>> %s: mSelector = %c%c%c%c"
- "<<< neroaudiosink >>> %s: %d: check failed"
- "<<< neroaudiosink >>> %s: %d: false condition"
- "<<< neroaudiosink >>> %s: %d: got error %d"
- "<<< neroaudiosink >>> %s: Fastforwarding read offset to create a sufficient buffer"
- "<<< neroaudiosink >>> %s: FigNeroAudioSink %p created with format %c%c%c%c %.0f Hz %d ch %d bit."
- "<<< neroaudiosink >>> %s: Getting audio format for nero audio sink."
- "<<< neroaudiosink >>> %s: Prefetching over, have %zu bytes"
- "<<< neroaudiosink >>> %s: Resetting jitter buffer by %lf."
- "<<< neroaudiosink >>> %s: Resuming jitter buffer."
- "<<< neroaudiosink >>> %s: Suspending jitter buffer."
- "<<< neroaudiosink >>> %s: Zeroing %lu bytes"
- "<<< neroaudiosource >>>"
- "<<< neroaudiosource >>> %s: %d: false condition"
- "<<< neroaudiosource >>> %s: %d: got error %d"
- "<<< neroaudiosource >>> %s: FigNeroAudioSource %p created with format to %c%c%c%c %.0f Hz."
- "<<< neroendpoint >>>"
- "<<< neroendpoint >>> %s: %@ unsupported"
- "<<< neroendpoint >>> %s: %d: check failed"
- "<<< neroendpoint >>> %s: %d: false condition"
- "<<< neroendpoint >>> %s: %d: got error %d"
- "<<< neroendpoint >>> %s: %s"
- "<<< neroendpoint >>> %s: Attempting to connect to endpoint %@ over TCP because 'neroendpoint_ip' defaults write was set."
- "<<< neroendpoint >>> %s: Connecting to receiver..."
- "<<< neroendpoint >>> %s: Connection message is broken, err = %d"
- "<<< neroendpoint >>> %s: FigNeroEndpoint activation callback notification has been posted."
- "<<< neroendpoint >>> %s: Posting %@ notification for feature %llu after activation completion callback."
- "<<< neroendpoint >>> %s: Status bar override for recording DISABLED because of defaults write."
- "<<< neroendpoint >>> %s: Stevenote mode %d, Valeria mode %d"
- "<<< neroendpoint >>> %s: The activation callback is not complete yet, posting audio notification when it is completed."
- "<<< neroendpoint >>> %s: The activation callback is not complete yet, posting display notification when it is completed."
- "<<< neroendpoint >>> %s: Using port %d"
- "<<< neroendpoint >>> %s: [%p] called"
- "<<< neroendpoint >>> %s: [%p] called. storage->dissociated %s"
- "<<< neroendpoint >>> %s: [%p] called. storage->dissociated %s, propertyKey '%@'"
- "<<< neroendpoint >>> %s: [%p] created nero endpoint audio stream %p"
- "<<< neroendpoint >>> %s: [%p] created storage->neroAudioReceiver %p"
- "<<< neroendpoint >>> %s: [%p] created storage->screenStream %p"
- "<<< neroendpoint >>> %s: [%p] messageType '%c%c%c%c'. storage->dissociated %d storage->isStevenote %d"
- "<<< neroendpoint >>> %s: [%p] storage->audioStream %p"
- "<<< neroendpoint >>> %s: [%p] storage->dissociated %s storage->neroAudioReceiver %p storage->audioStream %p"
- "<<< neroendpoint >>> %s: [%p] storage->neroAudioReceiver %p"
- "<<< neroendpoint >>> %s: [%p] successfully activated nero endpoint"
- "<<< neroendpoint >>> %s: audio sink connected"
- "<<< neroendpoint >>> %s: audio sink disconnected"
- "<<< neroendpoint >>> %s: could not activate the endpoint [%p], error code %d"
- "<<< neroendpoint >>> %s: deviceInfo: %@"
- "<<< neroendpoint >>> %s: display connected"
- "<<< neroendpoint >>> %s: display disconnected"
- "<<< neroendpoint >>> %s: displayInfoDict : %@"
- "<<< neroendpoint >>> %s: receiver connected, receiverVersion = %d"
- "<<< neroendpoint >>> %s: receiver disconnected"
- "<<< neroendpoint >>> %s: unknown message type: '%c%c%c%c'"
- "<<< neroendpointaudiostream >>>"
- "<<< neroendpointaudiostream >>> %s:   default ACL   - channels: %d tag: 0x%08x"
- "<<< neroendpointaudiostream >>> %s:   preferred ACL - channels: %d tag: 0x%08x"
- "<<< neroendpointaudiostream >>> %s: %d: false condition"
- "<<< neroendpointaudiostream >>> %s: %d: got error %d"
- "<<< neroendpointaudiostream >>> %s: AudioQueueDispose failed: %d"
- "<<< neroendpointaudiostream >>> %s: [%p] Send sbuf %p ( %.3f -> %.3f )"
- "<<< neroendpointaudiostream >>> %s: [%p] Silent Audio queue is not present!"
- "<<< neroendpointaudiostream >>> %s: [%p] Valeria is connected"
- "<<< neroendpointaudiostream >>> %s: [%p] called"
- "<<< neroendpointaudiostream >>> %s: [%p] called, desiredSampleRate %.1f Hz"
- "<<< neroendpointaudiostream >>> %s: [%p] called, dissociated %s"
- "<<< neroendpointaudiostream >>> %s: [%p] called, dissociated %s, propertyKey '%@'"
- "<<< neroendpointaudiostream >>> %s: [%p] called. dissociated %s"
- "<<< neroendpointaudiostream >>> %s: [%p] set audio format to %c%c%c%c %.0f Hz"
- "<<< neroendpointaudiostream >>> %s: [%p]: started silent audio"
- "<<< neroendpointaudiostream >>> %s: [%p]: stopped silent audio"
- "<<< neroendpointaudiostream >>> %s: successfully created nero endpoint audio stream %p"
- "<<< neroendpointaudiostream >>> %s: unsupported key '%@'"
- "<<< neroendpointmanager >>> %s: %@ unsupported"
- "<<< neroendpointmanager >>> %s: %d: check failed"
- "<<< neroendpointmanager >>> %s: %d: false condition"
- "<<< neroendpointmanager >>> %s: %d: got error %d"
- "<<< neroendpointmanager >>> %s: Attached: %@"
- "<<< neroendpointmanager >>> %s: Attempt %d of %d: lockdown_copy_trustedHostAttached() returned %@"
- "<<< neroendpointmanager >>> %s: Custom endpoints disabled because of defaults write."
- "<<< neroendpointmanager >>> %s: Detached: %@"
- "<<< neroendpointmanager >>> %s: Discovery stopped unexpectedly, restarting in 10 seconds..."
- "<<< neroendpointmanager >>> %s: FigNeroEndpointManager disabled because of defaults write (neroendpoint)."
- "<<< neroendpointmanager >>> %s: Ignoring request to connect from untrusted host"
- "<<< neroendpointmanager >>> %s: Ignoring request to start Valeria discovery because it is already active."
- "<<< neroendpointmanager >>> %s: Ignoring request to start Valeria discovery because this is Stevenote."
- "<<< neroendpointmanager >>> %s: Ignoring request to start Valeria discovery in airplayd"
- "<<< neroendpointmanager >>> %s: Ignoring request to stop Valeria discovery because this is Stevenote."
- "<<< neroendpointmanager >>> %s: Restarting discovery...."
- "<<< neroendpointmanager >>> %s: Stopped listening for incoming Valeria connections."
- "<<< neroendpointmanager >>> %s: Valeria already connected"
- "<<< neroendpointmanager >>> %s: Valeria connected"
- "<<< neroendpointmanager >>> %s: Valeria disconnected"
- "<<< neroendpointmanager >>> %s: Valeria discovery not active, nothing to do."
- "<<< neroendpointmanager >>> %s: Waiting for a Valeria connection..."
- "<<< neroendpointmanager >>> %s: [%p] called"
- "<<< neroendpointmanager >>> %s: [%p] called. storage->invalid %s, propertyKey '%@'"
- "<<< neroendpointmanager >>> %s: [%p] messageType '%c%c%c%c'. storage->invalid %d endpoint %p"
- "<<< neroendpointmanager >>> %s: called"
- "<<< neroendpointmanager >>> %s: called, isValeriaEndpoint=%d"
- "<<< neroendpointmanager >>> %s: discoveryMode %@"
- "<<< neroendpointmanager >>> %s: neroendpoint_autopublish is set, publishing nero endpoint in 5 sec"
- "<<< neroendpointmanager >>> %s: publish nero endpoint"
- "<<< neroendpointmanager >>> %s: storage->discoveryStarted %d"
- "<<< neroendpointmanager >>> %s: storage->neroEndpoint %p already created"
- "<<< neroendpointmanager >>> %s: successfully created nero endpoint manager %p"
- "<<< neroendpointmanager >>> %s: successfully created nero endpoint manager with no discovery %p"
- "<<< neroendpointscreenstream >>>"
- "<<< neroendpointscreenstream >>> %s: %@ unsupported"
- "<<< neroendpointscreenstream >>> %s: %d: check failed"
- "<<< neroendpointscreenstream >>> %s: %d: false condition"
- "<<< neroendpointscreenstream >>> %s: %d: got error %d"
- "<<< neroendpointscreenstream >>> %s: Creating custom samplebuffer processor for audio accessory device"
- "<<< neroendpointscreenstream >>> %s: Creating null display source with custom samplebuffer processor for audio accessory device"
- "<<< neroendpointscreenstream >>> %s: FigVirtualDisplaySessionDeactivate() failed with err %d"
- "<<< neroendpointscreenstream >>> %s: [%p] Dissociate called, dissociated %s"
- "<<< neroendpointscreenstream >>> %s: [%p] Resume called, dissociated %s"
- "<<< neroendpointscreenstream >>> %s: [%p] Suspend called, dissociated %s"
- "<<< neroendpointscreenstream >>> %s: [%p] called"
- "<<< neroendpointscreenstream >>> %s: [%p] called, dissociated %s, propertyKey '%@'"
- "<<< neroendpointscreenstream >>> %s: [%p] called, propertyKey '%@'"
- "<<< neroendpointscreenstream >>> %s: [%p] successfully created nero endpoint video stream"
- "<<< neroendpointscreenstream >>> %s: display size is %.1f x %.1f isOverscanned=%d"
- "<<< neroendpointscreenstream >>> %s: displayInfoDict : %@"
- "<<< neroendpointscreenstream >>> %s: sessionOptions = %@"
- "<<< neroendpointscreenstream >>> %s: sinkOptions = %@"
- "<<< neromessenger >>> %s: FigNeroMessenger %p created."
- "<<< octaviaHALPlugin >>> %s: FigNeroEndpointManager = [%p]"
- "<<< octaviaHALPlugin >>> %s: called"
- "<<< stevenote >>>"
- "<<< stevenote >>> %s: <%#x>"
- "<<< stevenote >>> %s: BKSDisplayServicesSetCloneMirroringMode(%d) called"
- "<<< stevenote >>> %s: Current amperage %@ mA"
- "<<< stevenote >>> %s: Feature flags: 0x%x -> 0x%x"
- "<<< stevenote >>> %s: HUD enabled: %d -> %d"
- "<<< stevenote >>> %s: I didn't start NLC -- doing nothing."
- "<<< stevenote >>> %s: IOAccessoryManagerGetUSBCurrentLimit returned 0x%8x"
- "<<< stevenote >>> %s: IOAccessoryManagerGetUSBCurrentLimit returned current %d mA"
- "<<< stevenote >>> %s: IOAccessoryManagerSetUSBCurrentLimitBase error 0x%8x"
- "<<< stevenote >>> %s: IOServiceAddInterestNotification error 0x%8x"
- "<<< stevenote >>> %s: NLC is already running. Do nothing"
- "<<< stevenote >>> %s: NLC is not running -- doing nothing."
- "<<< stevenote >>> %s: NLC started"
- "<<< stevenote >>> %s: NLC stopped"
- "<<< stevenote >>> %s: NLC: plr %f latency %d bandwidth %d"
- "<<< stevenote >>> %s: NULL pCmd"
- "<<< stevenote >>> %s: Power assertion failed %d"
- "<<< stevenote >>> %s: Resetting orientation"
- "<<< stevenote >>> %s: SCDynamicStoreSetDispatchQueue() disable notifications error"
- "<<< stevenote >>> %s: SCDynamicStoreSetDispatchQueue() enable notifications error"
- "<<< stevenote >>> %s: SCDynamicStoreSetNotificationKeys() observe IPV4 changes"
- "<<< stevenote >>> %s: Set USB current limit base to %d mA"
- "<<< stevenote >>> %s: Set speaker behavior to %d because of defaults write"
- "<<< stevenote >>> %s: Unknown msg_type %d"
- "<<< stevenote >>> %s: _nlc_connect error %d"
- "<<< stevenote >>> %s: _nlc_get_status error %d"
- "<<< stevenote >>> %s: _nlc_stop_simulation error %d"
- "<<< stevenote >>> %s: called"
- "<<< stevenote >>> %s: called %d"
- "<<< stevenote >>> %s: device UDID: %@"
- "<<< stevenote >>> %s: device build: %@"
- "<<< stevenote >>> %s: device color: %@"
- "<<< stevenote >>> %s: device enclosure color: %@"
- "<<< stevenote >>> %s: device model: %@"
- "<<< stevenote >>> %s: deviceInfo: %@"
- "<<< stevenote >>> %s: kIOAccessoryManagerMessageUSBCurrentLimitChange received. Stevenote: %s"
- "<<< stevenote >>> %s: neroNLCIssueCommand error"
- "<<<< FigVirtualDisplaySinkOctavia >>>>"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %d: check failed"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %d: false condition"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %d: got error %d"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %f secs already enqueued, dropping next %d frames"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %f secs already enqueued, should drop frame"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: %p"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: (%p)"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: (%p) %@"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: (%p) %@ %@"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: -> %p"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Adjust destRect: new x = %.2f, new y = %.2f, new h = %.2f, new w = %.2f"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Adjust destRect: old x = %.2f, old y = %.2f, old h = %.2f, old w = %.2f"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Failed to enqueue frame, requesting key frame again"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Internal display mode (Stevenote/Valeria): advertising one mode that is %d x %d"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Nero PTS is too close to previous frame for Valeria (%.3f ms); adjusting PTS and signalling wirelessdisplay to drop the next frame"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: PTS quantize: nero clock is faster than octavia clock; skipping ahead one frame interval on nero to resync"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: PTS quantize: octavia clock faster than nero clock; time since last frame (%.3f) is less than 1/60, signalling wirelessdisplay to drop the next frame"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: PTS quantize: octavia clock faster than nero clock; time since last frame (%.3f) is more than 1/60, so squeezing frame in"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: Posting event '%@'\n"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: displayInfo = %@"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: dropping frame due to queue occupancy restriction (%d)"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: frame delay is %d frames"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: no event block set -- we're going to drift out of sync!"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: no octaviaClock. setting DisplayImmediately"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: octavia_mirroring_resolution preference: %@"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: options : %@"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: sending frame with PTS: %1.3f  octaviaPTS: %1.3f (%.3f ms since last frame) [neroPTS: %1.3f neroPTSQuantized: %1.3f delta: %.3f ms]"
- "<<<< FigVirtualDisplaySinkOctavia >>>> %s: setting nero display size to %f x %f"
- "Could not allocate FigHALNeroAudioSharedState"
- "Device was unplugged"
- "Endpoint must be activated"
- "EndpointStream has NULL ID"
- "Expecting ReadInput operation"
- "Expecting WriteMix operation"
- "Failed allocating dictionary"
- "FigHALNeroAudioDevice.c"
- "FigHALNeroAudioDeviceCreateForEndpointStream"
- "FigHALNeroAudioInputStream.c"
- "FigHALNeroAudioInputStreamCreate"
- "FigHALNeroAudioOutputStream.c"
- "FigHALNeroAudioOutputStreamCreate"
- "FigHUDLayerUtilityLogHUDLabels"
- "FigHUDLayerUtilityLogHUDValues"
- "FigNeroAudioSinkCreate"
- "FigNeroAudioSource.c"
- "FigNeroAudioSourceCreate"
- "FigNeroAudioSourceSetBytesWrittenHandler"
- "FigNeroEndpoint.c"
- "FigNeroEndpointAudioStream.c"
- "FigNeroEndpointAudioStreamCreateWithDeviceInfo"
- "FigNeroEndpointAudioStreamEnqueueAudioInput"
- "FigNeroEndpointAudioStreamGetDesiredSampleRate"
- "FigNeroEndpointAudioStreamSetFormatCreatingNewChannelLayouts"
- "FigNeroEndpointScreenStream.c"
- "FigNeroEndpointScreenStreamCreateWithDeviceInfo"
- "FigNeroEndpointSelfActivate_block_invoke"
- "FigNeroMessengerCreate"
- "FigOctaviaHALPlugin_Create"
- "FigOctaviaIsAudioAccessoryDevice_block_invoke"
- "FigOctaviaSetCloneMirroringMode"
- "FigVirtualDisplaySinkOctavia.c"
- "FigVirtualDisplaySinkOctaviaCreateWithOptions"
- "IOAccessoryManager not initialized"
- "IOAccessoryManagerGetServiceWithPrimaryPort failed"
- "Must supply an audio endpointStream"
- "NULL PCM formats"
- "Need at least one supported PCM format from endpointStream"
- "NeroCreateIdleSleepPreventor"
- "NeroStevenoteUtilities.m"
- "No"
- "Unknown change action"
- "YES"
- "Yes"
- "both queue and handler must be either NULL or non-NULL"
- "cannot set audio sink while endpoint stream is resumed"
- "cannot set audio source while endpoint stream is resumed"
- "invalidated"
- "kAudioHardwareBadDeviceError"
- "kAudioHardwareIllegalOperationError"
- "kAudioHardwareUnsupportedOperationError"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kFigEndpointAudioSourceError_InvalidParameter"
- "kFigEndpointAudioSourceError_UnexpectedState"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointError_InvalidParameter"
- "kFigEndpointStreamError_InvalidParameter"
- "kFigHALAudioObjectError_AllocationFailed"
- "kFigHALAudioObjectError_InvalidParameter"
- "nendpoint_ActivateWithCompletionCallback"
- "nendpoint_ActivateWithCompletionCallback_block_invoke"
- "nendpoint_ActivateWithCompletionCallback_block_invoke_2"
- "nendpoint_CopyProperty"
- "nendpoint_DeactivateWithCompletionCallback"
- "nendpoint_Dissociate"
- "nendpoint_Finalize"
- "nendpoint_audioEnqueueAudio"
- "nendpoint_audioSinkWasAttached"
- "nendpoint_audioSinkWasDetached"
- "nendpoint_createActivationPayload"
- "nendpoint_createNeroAudioReceiver"
- "nendpoint_createStreamsChangedPayload"
- "nendpoint_createTransport"
- "nendpoint_endpointAsyncMessageHandler"
- "nendpoint_handleNoteMessage"
- "nendpoint_postStreamChangedNotification_block_invoke"
- "nendpoint_releaseNeroAudioReceiver"
- "nendpoint_rootObjectAsyncMessageHandler"
- "nendpoint_rootObjectSyncMessageHandler"
- "neroAudio_CopyProperty"
- "neroAudio_Dissociate"
- "neroAudio_Finalize"
- "neroAudio_ResumeWithCompletionCallback"
- "neroAudio_SetProperty"
- "neroAudio_SuspendWithCompletionCallback"
- "neroAudio_activateInternal"
- "neroAudio_copySupportedOutputFormats"
- "neroAudio_resumeInternal"
- "neroAudio_sendSBuf"
- "neroAudio_setAudioSink"
- "neroAudio_setAudioSource"
- "neroAudio_startAudioQueue"
- "neroAudio_startAudioQueue_block_invoke"
- "neroAudio_stopAudioQueue"
- "neroAudio_stopAudioQueue_block_invoke"
- "neroAudio_suspendInternal"
- "neroDeviceOrientationChanged"
- "neroDevice_Finalize"
- "neroDevice_GetPropertyData"
- "neroDevice_PerformConfigChange"
- "neroDevice_clearNonMixableBitFromPrevailingSupportedPCMFormats"
- "neroDevice_endpointStreamWentAway"
- "neroDevice_setupSharedState"
- "neroDevice_updateDesiredSampleRate"
- "neroFeatureFlagsChangedCallback"
- "neroHIDSendReset3DRotation"
- "neroHIDToggle3DDeviceRotation"
- "neroHUDEnabledChangedCallback"
- "neroIOAccessoryCopyAdapterAmperage"
- "neroIOAccessoryInitialize"
- "neroIOAccessorySetChargeCurrent"
- "neroIOAccessoryStateChangedCallback"
- "neroIOAccessoryUninitialize"
- "neroIPAddressChangedCallback"
- "neroInputStream_DoIOOperation"
- "neroInputStream_Finalize"
- "neroInputStream_GetCurrentFormat"
- "neroInputStream_PerformConfigChange"
- "neroInputStream_SetPropertyData"
- "neroInputStream_initializeDefaultInputFormat"
- "neroInputStream_setPrevailingASBD"
- "neroNLCInitialize"
- "neroNLCIsRunning"
- "neroNLCIssueCommand"
- "neroNLCUninitialize"
- "neroOutputStream_DoIOOperation"
- "neroOutputStream_Finalize"
- "neroOutputStream_GetCurrentFormat"
- "neroOutputStream_PerformConfigChange"
- "neroOutputStream_SetPropertyData"
- "neroOutputStream_initializeDefaultOutputFormat"
- "neroOutputStream_setPrevailingASBD"
- "neroRegisterIPAddressChangedNotification"
- "neroRegisterIPAddressChangedNotification_block_invoke"
- "neroRegisterUSBCurrentChangedNotification"
- "neroSendDeviceInfoUpdate"
- "neroSendDeviceInfoUpdate_block_invoke"
- "neroSink_AcquireBuffer_block_invoke"
- "neroSink_CommitBuffer_block_invoke"
- "neroSink_GetAudioFormat"
- "neroSink_Read"
- "neroSink_Read_block_invoke"
- "neroSink_Reset"
- "neroSink_Resume"
- "neroSink_Suspend"
- "neroSink_getAvailableBytesForRead"
- "neroSink_getAvailableBytesForWrite"
- "neroSource_WriteBytes"
- "neroSource_writeBBuf"
- "neroTearDownAndReleaseHIDClient"
- "neroUnregisterIPAddressChangedNotification"
- "neroUnregisterUSBCurrentChangedNotification"
- "neroaudiosink_trace"
- "neroaudiosource_trace"
- "neroendpoint_trace"
- "neroendpointaudiostream_trace"
- "neroendpointmanager_trace"
- "neroendpointscreenstream_trace"
- "nerohal_trace"
- "neromessenger_trace"
- "nmanager_CopyProperty"
- "nmanager_Invalidate"
- "nmanager_SetDiscoveryMode"
- "nmanager_SetProperty_block_invoke_2"
- "nmanager_StartDiscovery"
- "nmanager_StopDiscovery"
- "nmanager_asyncRegisterFigNeroHALDriver"
- "nmanager_createManagerWithNoDiscovery"
- "nmanager_createValeriaTransport"
- "nmanager_create_block_invoke"
- "nmanager_discoveryHandler_block_invoke"
- "nmanager_handleEndpointActivationChanged"
- "nmanager_publishEndpoint"
- "nmanager_registerManager"
- "nmanager_rootObjectAsyncMessageHandler"
- "nmanager_rootObjectSyncMessageHandler"
- "nmanager_startValeriaDiscovery"
- "nmanager_stopValeriaDiscovery"
- "nmanager_unpublishEndpoint"
- "nmanager_valeriaDisconnected"
- "no"
- "no output formats"
- "nscreen_CopyProperty"
- "nscreen_Dissociate_block_invoke"
- "nscreen_Finalize"
- "nscreen_ResumeWithCompletionCallback_block_invoke"
- "nscreen_SetProperty"
- "nscreen_SuspendWithCompletionCallback_block_invoke"
- "octPlugin_instantiateNeroEndpointManager"
- "octaviaSink_CopyProperty"
- "octaviaSink_Finalize"
- "octaviaSink_GetPropertyAsync"
- "octaviaSink_Invalidate"
- "octaviaSink_Perform"
- "octaviaSink_Resume"
- "octaviaSink_SetDispatchQueue"
- "octaviaSink_SetEventHandler"
- "octaviaSink_SetProperty"
- "octaviaSink_ShouldDropFrame"
- "octaviaSink_Start"
- "octaviaSink_Stop"
- "octaviaSink_Suspend"
- "octaviaSink_acknowledgeFrameIfRequired"
- "octaviaSink_buildSupportedResolutionsList"
- "octaviaSink_buildSupportedResolutionsListForStevenoteOrValeria"
- "octaviaSink_createClockForRenderPipeline"
- "octaviaSink_createColorAndTimingModeArrays"
- "octaviaSink_enqueueBuffer"
- "octaviaSink_getInternalDisplayMirroringDimensions"
- "octaviaSink_getPreferredDimensionsFromPrefs"
- "octaviaSink_postEvent"
- "octaviaSink_syncTimeStampsToOctaviaClock"
- "octaviaSink_syncToOctaviaClockAndEnqueueBuffer"
- "sStorage->chargeInfo.connection is NULL"
- "sharedState is NULL"
- "stevenote_trace"
- "transport already exists!"
- "wirelessdisplaysinkoctavia_trace"

```
