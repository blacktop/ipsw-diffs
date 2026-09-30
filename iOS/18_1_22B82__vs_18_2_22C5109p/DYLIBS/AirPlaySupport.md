## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-830.10.1.1.0
-  __TEXT.__text: 0x703e0
-  __TEXT.__auth_stubs: 0x2c40
+835.13.1.11.1
+  __TEXT.__text: 0x709b4
+  __TEXT.__auth_stubs: 0x2c60
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0xcc8
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x1d1d9
+  __TEXT.__cstring: 0x1d4ea
   __TEXT.__oslogstring: 0x6c
-  __TEXT.__unwind_info: 0x12e8
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x68f
   __TEXT.__objc_methtype: 0x25
   __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x1a78
+  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__const: 0x1a98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x1638
-  __AUTH_CONST.__const: 0x22e8
+  __AUTH_CONST.__auth_got: 0x1648
+  __AUTH_CONST.__const: 0x2388
   __AUTH_CONST.__cfstring: 0x4340
   __AUTH_CONST.__objc_const: 0x130
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x188
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x19c8
-  __DATA.__bss: 0x8a8
+  __DATA.__data: 0x1a38
+  __DATA.__bss: 0x908
   __DATA_DIRTY.__data: 0x780
   __DATA_DIRTY.__bss: 0x4b0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1576
-  Symbols:   2643
-  CStrings:  2879
+  Functions: 1584
+  Symbols:   2654
+  CStrings:  2911
 
Symbols:
+ _APSCopyAirPlayNonSystemPeers
+ _APSGetAirPlayNonSystemPeersCount
+ _APSRemoveAirPlayNonSystemPeers
+ _APSSaveAirPlayNonSystemPeer
+ _APSStallMonitorActivityBegin
+ _APSStallMonitorActivityCreate
+ _APSStallMonitorActivityEnd
+ _APSStallMonitorActivityGetTypeID
+ _FigSignalErrorAt3
+ _FigUserStackshotWithMessage
+ _FigUserTailspinWithMessage
+ _MGRegisterForUpdates
+ _PairingSessionCopyPeers
+ _PairingSessionSavePeer
+ _SecondsToUpTicks
+ _kAPSStallMonitorActivityNotification_DidStall
+ _kSecAttrSynchronizable
+ _kSecAttrSynchronizableAny
- _APSGetCurrentLocalTimeString
- _FigSignalErrorAt
- _PairingSessionDeleteIdentity
- _gettimeofday
- _kAPSNetworkClockNotification_GrandmasterChanged
- _kCM8021ASClockNotification_GrandmasterDidChange
- _localtime
- _strftime
CStrings:
+ "### stackshot failed!"
+ "### tailspin failed!"
+ "%!@(MISSING){f=0x%!x(MISSING)} stalled for >= %!u(MISSING)s"
+ "%!@(MISSING){f=0x%!x(MISSING)} stalled for >= %!u(MISSING)s\n"
+ "%!@(MISSING){f=0x%!x(MISSING)}, "
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "(Fig)"
+ "-108"
+ "-877"
+ "-878"
+ "-879"
+ "-880"
+ "APSAPAPExtensionLoudnessInfoUtils.c"
+ "APSAudioFormatDescription.c"
+ "APSAudioFormatDescriptionList.c"
+ "APSCopyAirPlayNonSystemPeers"
+ "APSRemoveAirPlayNonSystemPeers"
+ "APSSaveAirPlayNonSystemPeer"
+ "APSSharedRingBuffer.c"
+ "APSStallMonitor"
+ "APSStallMonitor.notification"
+ "APSStallMonitor: [%!@(MISSING)]"
+ "APSStallMonitorActivity"
+ "APSStallMonitorActivityCreate"
+ "AirPlay - Stall Monitor"
+ "CFArrayRef APSCopyAirPlayNonSystemPeers(void)"
+ "Cached device name changed from '%!@(MISSING)' => '%!@(MISSING)'."
+ "Copied AirPlay Non-System peers from the Keychain (count: %!d(MISSING))\n"
+ "Could not allocate APSAudioFormatDescription"
+ "Could not allocate APSAudioFormatDescriptionList"
+ "DidStall"
+ "Failed to create bufferMemObject"
+ "Failed to create stateMemObject"
+ "OSStatus APSSaveAirPlayNonSystemPeer(const char *, const char *)"
+ "Saving AirPlay Non-System peer to the Keychain (identifier: %!s(MISSING), publicKey: %!s(MISSING))\n"
+ "TTR: %!@(MISSING)"
+ "[%!{(MISSING)ptr}] Adding all peers to peer list (legacy: %!s(MISSING))\n"
+ "[%!{(MISSING)ptr}] Using %!s(MISSING) (NoExtraHub) clock topology"
+ "bufferMemory region maps to NULL"
+ "bufferMemorySize is zero"
+ "collecting TapToRadar \"%!@(MISSING)\"...\n%!@(MISSING)"
+ "collecting tailspin \"%!@(MISSING)\"..."
+ "kCMBaseObjectError_AllocationFailed"
+ "kParamErr"
+ "loudness key missing"
+ "sample peak key missing"
+ "stallMonitorReportBackoffSecs"
+ "stallMonitor_activityApplier"
+ "stallMonitor_timerFire"
+ "stateMemObject maps to NULL"
+ "stateMemoryLength < sizeof(RingState)"
+ "systemUtils_updateCachedDeviceName"
+ "taking stackshot \"%!@(MISSING)\"..."
+ "true peak key missing"
+ "v24@?0^{__CFString=}8^{__CFDictionary=}16"
+ "void stallMonitor_activityApplier(const void *, void *)"
+ "void stallMonitor_timerFire(void *)"
+ "void systemUtils_updateCachedDeviceName(FigSimpleMutexRef, CFStringRef *)"
+ "{%!k(MISSING)O=%!O(MISSING)%!k(MISSING)O=%!O(MISSING)%!k(MISSING)O=%!i(MISSING)%!k(MISSING)O=%!?(MISSING).*s%!k(MISSING)O=%!O(MISSING)%!k(MISSING)O=%!O(MISSING)%!k(MISSING)O=%!O(MISSING)}"
- " (NoExtraHub)"
- "%!Y(MISSING)-%!m(MISSING)-%!d(MISSING) %!H(MISSING):%!M(MISSING):%!S(MISSING)"
- "%!s(MISSING).%!u(MISSING)%!s(MISSING)"
- "%!z(MISSING)"
- "APSGetCurrentLocalTimeString"
- "AirPlayPerf_PTPNoExtraHub"
- "GrandmasterChanged"
- "[%!{(MISSING)ptr}] Adding all peers to peer list (hub: %!s(MISSING), legacy: %!s(MISSING))\n"
- "[%!{(MISSING)ptr}] Adding hub peer to peer list\n"
- "[%!{(MISSING)ptr}] Cancelling GM stabilization timer.\n"
- "[%!{(MISSING)ptr}] Clock hub peer %!s(MISSING) %!@(MISSING)"
- "[%!{(MISSING)ptr}] GM stabilization timer has fired after %!u(MISSING) ms.\n"
- "[%!{(MISSING)ptr}] GMID: 0x%!l(MISSING)lx --> 0x%!l(MISSING)lx, GM peer is: %!'(MISSING)@\n"
- "[%!{(MISSING)ptr}] Hub peer info updated"
- "[%!{(MISSING)ptr}] Last clock hub peer info %!@(MISSING)"
- "[%!{(MISSING)ptr}] Local hub peer info updated: %!@(MISSING)"
- "[%!{(MISSING)ptr}] No change in hub info %!@(MISSING)"
- "[%!{(MISSING)ptr}] Started a %!u(MISSING)-ms GM stabilization timer.\n"
- "[%!{(MISSING)ptr}] Using %!s(MISSING)%!?(MISSING)s clock topology%!?(MISSING){end} and %!u(MISSING)-ms GM stabilization timer\n"
- "info updated to"
- "ptpGMStableTimerMs"
- "replaced with"
- "void ptpClock_gmDidStabilize(void *)"
- "void ptpClock_gmStabilizationTimerCancelled(void *)"
- "void ptpClock_startGMStabilizationTimer(void *)"
- "void ptpClock_updateGMIDAndHubPeerAndEnablePortsIfNeeded(APSNetworkClockRef, Boolean *)"
- "void ptpClock_updateHubPeer(APSNetworkClockRef, CFDictionaryRef, Boolean *)"

```
