## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-1015.5.1.0.0
-  __TEXT.__text: 0x17c184
-  __TEXT.__objc_methlist: 0xb0c
+1015.8.1.0.0
+  __TEXT.__text: 0x17caf8
+  __TEXT.__objc_methlist: 0xb2c
   __TEXT.__const: 0x2762b
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x89c
-  __TEXT.__cstring: 0x33e1f
+  __TEXT.__cstring: 0x341c2
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__unwind_info: 0x1d18
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20b8
   __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc00
+  __DATA_CONST.__objc_selrefs: 0xc20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__got: 0x9c8
   __AUTH_CONST.__const: 0x9440
-  __AUTH_CONST.__cfstring: 0xbc80
-  __AUTH_CONST.__objc_const: 0x1560
+  __AUTH_CONST.__cfstring: 0xbd80
+  __AUTH_CONST.__objc_const: 0x15a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1ed8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1730
-  Symbols:   3648
-  CStrings:  5271
+  Functions: 1736
+  Symbols:   3660
+  CStrings:  5289
 
Symbols:
+ -[AVAudioSession(APAVAudioSessionManager) ap_setIsAirPlayOdeonSetupSession:error:]
+ -[AVAudioSession(APAVAudioSessionManager) ap_setMXSessionPropertyWithLogging:value:error:]
+ GCC_except_table1029
+ GCC_except_table1144
+ GCC_except_table1163
+ GCC_except_table1214
+ GCC_except_table1218
+ GCC_except_table1271
+ GCC_except_table1279
+ GCC_except_table1281
+ GCC_except_table1325
+ GCC_except_table1391
+ GCC_except_table429
+ GCC_except_table495
+ GCC_except_table545
+ GCC_except_table605
+ GCC_except_table609
+ GCC_except_table616
+ GCC_except_table624
+ GCC_except_table762
+ __HandleLikelyResumableInterruptionTimeout
+ __OBJC_$_CATEGORY_AVAudioSession_$_APAVAudioSessionManager
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVAudioSession_$_APAVAudioSessionManager
+ __PauseOnMediaAudioInterruption
+ __TerminateSessionOnAudioInterruption
+ _airplayReqProcessor_ensurePairingServices
+ _kFigEndpointPlaybackSessionState_Paused
+ _kFigEndpointPlaybackSessionState_Playing
+ _kFigEndpointPlaybackSessionState_Stopped
+ _kMXSessionProperty_IsAirPlayOdeonSetupSession
- GCC_except_table1026
- GCC_except_table1141
- GCC_except_table1160
- GCC_except_table1211
- GCC_except_table1215
- GCC_except_table1268
- GCC_except_table1276
- GCC_except_table1278
- GCC_except_table1322
- GCC_except_table1385
- GCC_except_table427
- GCC_except_table493
- GCC_except_table543
- GCC_except_table603
- GCC_except_table607
- GCC_except_table614
- GCC_except_table622
- GCC_except_table760
CStrings:
+ " (denied by MX: insufficient priority)"
+ "### Failed to %sactivate media AVAudioSession due to error: %@%s\n"
+ "-[AVAudioSession(APAVAudioSessionManager) ap_setMXSessionPropertyWithLogging:value:error:]"
+ "1015.8.1"
+ "AVAudioSessionInterruptionEndLikelyToBeResumableKey"
+ "Audio Interruption: %@-%@, options: %@\n"
+ "CoreUtils"
+ "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, APPairingServicesRef *)"
+ "OSStatus _StartServers(AirPlayReceiverServerRef)"
+ "OSStatus airplayReqProcessor_ensurePairingServices(APReceiverRequestProcessorRef, Boolean, APSTransportMessageProcessingStatus *)"
+ "OSStatus coreUtilsPairing_HandleSetup(APPairingServicesRef, CFStringRef, CFDataRef, CFDataRef *, Boolean *)"
+ "Video ended, restoring MR playback state %u from sender\n"
+ "[%@] %@ property set to %@.\n"
+ "[%@] Failed to set %@ property with err: %@.\n"
+ "[%{ptr}] APPairingServicesCoreUtils created.\n"
+ "[%{ptr}] Audio interruption is likely resumable. Survive it for up to %u seconds.\n"
+ "[%{ptr}] Created %s pairing services [%{ptr}]\n"
+ "[%{ptr}] Ignoring MR playback state %u from sender while the video player owns it\n"
+ "[%{ptr}] Likely-resumable audio interruption did not end in %u seconds. Terminate session.\n"
+ "[%{ptr}] Likely-resumable audio interruption ended and it is resumable. Cancel the timer.\n"
+ "[%{ptr}] Likely-resumable audio interruption ended, but it is not resumable. Terminate session.\n"
+ "[%{ptr}] Media audio session was paused on resumable interruption.\n"
+ "[%{ptr}] Not paused on media audio interruption. Do nothing.\n"
+ "[%{ptr}] Publishing video player state %@ as MR playback state %u\n"
+ "[%{ptr}] Started %u seconds timer for likely-resumable audio interruption.\n"
+ "_StartLikelyResumableInterruptionTimer"
+ "_StartServers"
+ "airplayReqProcessor_ensurePairingServices"
+ "disablePairSetupThrottling"
+ "isLikelyResumable"
+ "legacy"
+ "likelyResumableInterruptionTimeoutSecs"
+ "mrPlaybackStateFromSender"
+ "updateVideoPlaybackState"
+ "void _HandleLikelyResumableInterruptionTimeout(void *)"
+ "void _PauseOnMediaAudioInterruption(AirPlayReceiverSessionRef)"
+ "void _StartLikelyResumableInterruptionTimer(AirPlayReceiverSessionRef)"
- "### Failed to %sactivate media AVAudioSession due to error: %@\n"
- "1015.5.1"
- "Audio Interruption: %@-%@\n"
- "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, Boolean, APPairingServicesRef *)"
- "OSStatus coreUtilsPairing_HandleSetup(APPairingServicesRef, CFStringRef, APSecurityMode, CFDataRef, CFDataRef *, Boolean *)"
- "[%@] Failed to set IsAirPlayReceiverSession property with err: %@.\n"
- "[%@] Failed to set IsEligibleForNowPlayingAppConsideration property with err: %@.\n"
- "[%@] IsAirPlayReceiverSession property set to YES.\n"
- "[%@] IsEligibleForNowPlayingAppConsideration property set to NO.\n"
- "[%{ptr}-%s] Prefer No Interruption set to true for audio mode: %@ with return %d.\n"
- "[%{ptr}] APPairingServicesCoreUtils (%s) created.\n"
- "[%{ptr}] Created legacy pairing services [%{ptr}]\n"
- "[%{ptr}] Created pairing services [%{ptr}] for pair-setup.\n"
- "[%{ptr}] Created pairing services [%{ptr}] for pair-verify\n"
- "[%{ptr}] Sender doesn't support SurviveAudioInterruption. Do nothing. \n"
- "[%{ptr}] Sender supports resumable interruption. Was paused on media audio interruption? %s.\n"
- "private"
- "public"
- "void _StartServers(AirPlayReceiverServerRef)"
```
