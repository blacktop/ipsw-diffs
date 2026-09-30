## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-845.6.1.0.0
-  __TEXT.__text: 0x718c0
-  __TEXT.__auth_stubs: 0x2c60
+850.17.1.0.0
+  __TEXT.__text: 0x723d4
+  __TEXT.__auth_stubs: 0x2cf0
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0xcc8
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x1d3fa
+  __TEXT.__const: 0xc28
+  __TEXT.__dlopen_cstrs: 0xac
+  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__cstring: 0x1d94e
   __TEXT.__oslogstring: 0x6c
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x12b0
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x689
   __TEXT.__objc_methtype: 0x25
   __TEXT.__objc_stubs: 0x880
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x1a98
+  __DATA_CONST.__const: 0x1ae8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x1648
-  __AUTH_CONST.__const: 0x2388
-  __AUTH_CONST.__cfstring: 0x4360
+  __AUTH_CONST.__auth_got: 0x1690
+  __AUTH_CONST.__const: 0x23a8
+  __AUTH_CONST.__cfstring: 0x4340
   __AUTH_CONST.__objc_const: 0x130
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x188
+  __AUTH.__data: 0x140
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1a38
-  __DATA.__bss: 0x8f0
+  __DATA.__data: 0x1aa8
+  __DATA.__bss: 0x900
   __DATA_DIRTY.__data: 0x780
   __DATA_DIRTY.__bss: 0x4c8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity
   - /System/Library/PrivateFrameworks/caulk.framework/caulk

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1591
-  Symbols:   2656
-  CStrings:  2893
+  Functions: 1568
+  Symbols:   2675
+  CStrings:  2938
 
Symbols:
+ _APSClockDriftMonitorCreate
+ _APSClockDriftMonitorGetTypeID
+ _APSClockDriftMonitorNotification_DriftThresholdExceeded
+ _APSClockDriftMonitorResume
+ _APSClockDriftMonitorSuspend
+ _APSThreadSafeDictionaryAddEntriesToDictionaryWithRecursion
+ _APSWiFiTransactionUpdateTransaction
+ _CMClockGetTypeID
+ _CMTimeAbsoluteValue
+ _CMTimebaseCreateWithSourceClock
+ _CMTimebaseGetTypeID
+ _CMTimebaseSetRateAndAnchorTime
+ _FigSignalErrorAt3
+ __sl_dlopen
+ _abort_report_np
+ _dispatch_queue_get_label
+ _dlerror
- _FigSignalErrorAt
- _kAPSEndpointStreamAudioHoseProtocolProperty_IsAppleTV
- _kAPSEndpointStreamAudioHoseProtocolProperty_WASCalibrationSupportsMATAtmos
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "-108"
+ "-877"
+ "-878"
+ "-879"
+ "-880"
+ "APSAPAPExtensionLoudnessInfoUtils.c"
+ "APSAudioFormatDescription.c"
+ "APSAudioFormatDescriptionList.c"
+ "APSClockDriftMonitor"
+ "APSClockDriftMonitor already resumed."
+ "APSClockDriftMonitorCreate"
+ "APSClockDriftMonitorQueue"
+ "APSClockDriftMonitorResume"
+ "APSClockDriftMonitorSuspend"
+ "APSPriorityDispatcher.%{ptr}.enf.%d%?{end}.%s"
+ "APSPriorityDispatcher.%{ptr}.pri.%d%?{end}.%s"
+ "APSSharedRingBuffer.c"
+ "APSWiFiTransactionUpdateTransaction"
+ "AirPlayPerf_HLARandomLatency"
+ "Could not allocate APSAudioFormatDescription"
+ "Could not allocate APSAudioFormatDescriptionList"
+ "DriftThresholdExceeded"
+ "Failed to create bufferMemObject"
+ "Failed to create stateMemObject"
+ "OSStatus APSClockDriftMonitorCreate(CMClockOrTimebaseRef, CMClockOrTimebaseRef, uint64_t, uint64_t, APSClockDriftMonitorRef *)"
+ "RemoteTimebase is not running"
+ "SourceTimebase is not running"
+ "Unable to find class %s"
+ "Using random audio latency: %d ms\n"
+ "[%{ptr}] %s %s"
+ "[%{ptr}] Created with source time source %{ptr} and remote time source %{ptr}"
+ "[%{ptr}] Drift from remote timebase exceeded by %1.6f secs"
+ "[%{ptr}] SourceClockOrTimebase and/or RemoteClockOrTimebase type error "
+ "[%{ptr}] TimedManagerTimerTriggerNotification: AudioFormat changed to %s"
+ "apsRadarLogging_radarComponentEntryForAPSRadarComponentID_block_invoke"
+ "bufferMemory region maps to NULL"
+ "bufferMemorySize is zero"
+ "hoseSBAR_handleDriftThresholdExceededNotification"
+ "hoseSBAR_handleTimedManagerTriggeredNotification"
+ "kCMBaseObjectError_AllocationFailed"
+ "kParamErr"
+ "loudness key missing"
+ "sample peak key missing"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
+ "started"
+ "stateMemObject maps to NULL"
+ "stateMemoryLength < sizeof(RingState)"
+ "stopped"
+ "true peak key missing"
+ "void APSWiFiTransactionUpdateTransaction(LogCategory *, void *, APSWiFiTransactionType, Boolean, APSWiFiTransactionRef *)"
+ "void APSZeroTracker_LogZeroInstances(APSZeroTracker *const, const Float64)"
+ "void _APSClockDriftMonitorFinalize(CFTypeRef)"
+ "void hoseSBAR_handleDriftThresholdExceededNotification(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void hoseSBAR_handleTimedManagerTriggeredNotification(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
- "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
- "/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
- "APSEndpointStreamAudioHoseProtocolProperty_IsAppleTV"
- "PTS"
- "[%{ptr}] TimedManagerTimerTriggerNotification: AudioFormat changed to %s at Time %1.4f"
- "[%{ptr}] hoseSBAR_restartSBAROnFormatChange at pts %1.4f\n"
- "hoseSBAR_restartSBAROnFormatChangeInternal"
- "hoseSBAR_timedManagerTimerTriggerNotification"
- "kAPSEndpointStreamAudioHoseProtocolProperty_WASCalibrationSupportsMATAtmos"
- "void APSZeroTracker_LogZeroInstances(APSZeroTracker *const, const CFStringRef, const AudioStreamBasicDescription *)"
- "void hoseSBAR_restartSBAROnFormatChangeInternal(void *)"
- "void hoseSBAR_timedManagerTimerTriggerNotification(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"

```
