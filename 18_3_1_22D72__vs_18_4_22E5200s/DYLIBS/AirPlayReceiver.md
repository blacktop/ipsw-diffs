## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-845.6.1.0.0
-  __TEXT.__text: 0x1466fc
+850.14.1.0.0
+  __TEXT.__text: 0x1479bc
   __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__objc_methlist: 0x928
-  __TEXT.__const: 0x322a6
-  __TEXT.__gcc_except_tab: 0x428
-  __TEXT.__cstring: 0x2c993
-  __TEXT.__unwind_info: 0x1658
-  __TEXT.__eh_frame: 0x1b10
+  __TEXT.__objc_methlist: 0xa94
+  __TEXT.__const: 0x322b5
+  __TEXT.__dlopen_cstrs: 0xad
+  __TEXT.__gcc_except_tab: 0x7bc
+  __TEXT.__cstring: 0x2cc2f
+  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__eh_frame: 0x1ae0
   __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methname: 0x2593
-  __TEXT.__objc_methtype: 0x1540
-  __TEXT.__objc_stubs: 0x26a0
-  __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x1b60
+  __TEXT.__objc_methname: 0x2653
+  __TEXT.__objc_methtype: 0x154c
+  __TEXT.__objc_stubs: 0x2780
+  __DATA_CONST.__got: 0x840
+  __DATA_CONST.__const: 0x1b80
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa78
+  __DATA_CONST.__objc_selrefs: 0xb50
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1b78
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0xadd0
-  __AUTH_CONST.__cfstring: 0xa600
-  __AUTH_CONST.__objc_const: 0x1768
+  __AUTH_CONST.__const: 0xadc0
+  __AUTH_CONST.__cfstring: 0xa6a0
+  __AUTH_CONST.__objc_const: 0x14f0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x188
   __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x177f0
-  __DATA.__bss: 0x608
+  __DATA.__data: 0x177e8
+  __DATA.__bss: 0x6d8
   __DATA.__common: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1581
-  Symbols:   2710
-  CStrings:  5203
+  Functions: 1562
+  Symbols:   2711
+  CStrings:  5223
 
Symbols:
+ _AVSystemController_ActiveAudioRouteDidChangeNotification
+ _AVSystemController_ActiveAudioRouteDidChangeNotificationParameter_ShouldPause
+ _FigCFArrayGetFirstValue
+ _FigSimpleMutexCheckIsLockedOnThisThread
+ __sl_dlopen
+ _abort_report_np
+ _dlerror
- _DataBuffer_AppendFile
- _DataBuffer_Commit
- _DataBuffer_RunProcessAndAppendOutput
- _dlopen
- _fmod
CStrings:
+ "-[APAVAudioSessionManager _ifNeededChangeSessionTypeAndRequestNewBufferSize:]"
+ "-[AirPlayReceiverPlatform _avSystemControllerActiveAudioRouteChanged:]"
+ "-[AirPlayReceiverPlatform _avSystemControllerActiveAudioRouteChanged:]_block_invoke"
+ "850.14.1"
+ "Activated"
+ "Activating"
+ "B24@0:8^@16"
+ "BufferedAPAC"
+ "Deactivated"
+ "Deactivating"
+ "Failed to post event: %'@ %#m"
+ "Failed to unregister comm channel %@: unknown comm channel ID (err %#m)"
+ "Histogram_GlitchFreeDuration"
+ "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef *, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
+ "Posted events: %d%?{end}, remaining: %d"
+ "Unable to find class %s"
+ "[%@] Restoring session category=%@ mode=%@ options=0x%x failed. Error=%@\n"
+ "[%@] [%{ptr}-%s] %s session failed. Error=%@\n"
+ "[%@] [%{ptr}-%s] %s session. Buffer frame size=%u isMixable=%d (restored=%d).\n"
+ "[%@] [%{ptr}-%s] Another session is playing with buffer frame size=%u. Setting preferred size=%u (%.3fsec) and isMixable=0 (temporarily)\n"
+ "[%@] [%{ptr}-%s] changing session type failed. Error=%@\n"
+ "[%@] setCategory:Playback mode:Default options:none. Error=%@\n"
+ "[%@] setPreferredIOBufferDuration %f sec. Error=%@\n"
+ "[%{ptr}] <AirPlayVolume> Registering for AVSC notifications\n"
+ "[%{ptr}] <AirPlayVolume> Unregistering for AVSC notifications\n"
+ "[%{ptr}] AVSystemController active audio route changed. Should pause = %s\n"
+ "[%{ptr}] Sending pause command to session [%{ptr}]\n"
+ "_avSystemControllerActiveAudioRouteChanged:"
+ "_ifNeededChangeSessionTypeAndRequestNewBufferSize:"
+ "addObjectsFromArray:"
+ "array"
+ "connectAck"
+ "glitchFreeDurationHistogram"
+ "glitchFreeDurationHistogramCount"
+ "isOtherAudioPlaying"
+ "receiver_reportRTCMetricsIntervalS"
+ "setPreferredIOBufferDuration:error:"
+ "softlink:r:path:/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
+ "void APReceiverMediaRemoteXPCService_enqueueAndPostEvent(CFStringRef, CFDictionaryRef)"
- "### Invalid session type: %d.\n"
- "%@ MATAtmos Playback %s"
- "+-+ syslog +--\n"
- "/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
- "/System/Library/PrivateFrameworks/NearbyInteraction.framework/NearbyInteraction"
- "/log"
- "/logs"
- "/var/mobile/Library/Logs/AirPlay.log"
- "845.6.1"
- "===================\n"
- "APReceiverMediaRemoteXPCService_RegisterCommChannel"
- "APSReceiverAudioSessionBufferedHoseEnableMATAtmosPlayback"
- "AirPlay Diagnostics\n"
- "OSStatus APSReceiverAudioSessionBufferedHoseEnableMATAtmosPlayback(void *, Boolean)"
- "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
- "[%{ptr}] <AirPlayVolume> Registering for AVSC volume notifications\n"
- "[%{ptr}] <AirPlayVolume> Unregistering for AVSC volume notifications\n"
- "airplayReqProcessor_requestProcessGetLog"
- "audioSessionBufferedHose_updatePreferredAudioFormat"
- "matAtmosPlaybackEnabled"
- "syslog"
- "text/plain"

```
