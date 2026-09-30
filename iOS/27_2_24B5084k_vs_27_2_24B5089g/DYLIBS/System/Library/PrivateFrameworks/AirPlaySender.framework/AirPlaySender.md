## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-1005.7.1.0.0
-  __TEXT.__text: 0x239660
+1005.8.1.0.0
+  __TEXT.__text: 0x2399f0
   __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__cstring: 0x8f88f
-  __TEXT.__const: 0x61f0
+  __TEXT.__cstring: 0x8f9e4
+  __TEXT.__const: 0x6190
   __TEXT.__gcc_except_tab: 0xaa4
   __TEXT.__dlopen_cstrs: 0x61a
   __TEXT.__oslogstring: 0x1009
-  __TEXT.__unwind_info: 0x9220
+  __TEXT.__unwind_info: 0x9230
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x170
   __DATA_CONST.__got: 0x23b0
-  __AUTH_CONST.__const: 0x7780
+  __AUTH_CONST.__const: 0x77b0
   __AUTH_CONST.__cfstring: 0x149e0
   __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x878
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x18690
+  __DATA.__data: 0x18620
   __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xf78
+  __DATA_DIRTY.__data: 0xfe8
   __DATA_DIRTY.__bss: 0x788
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11452
-  Symbols:   8952
-  CStrings:  11654
+  Functions: 11460
+  Symbols:   8958
+  CStrings:  11659
 
Symbols:
+ GCC_except_table128
+ GCC_except_table50
+ _APSIsUpdateInfoForwardingEnabled
+ _APTransportDeviceForwardAirPlayInfoToBrowser
+ _FigCFNumberGetCFIndex
+ _carManager_reportBonjourEventToCarKit
+ _carManager_reportBonjourSuccessIfNeeded
+ _endpointCluster_failDelayMSecsForFailureCount.kFailDelayLadderPercent
+ _endpointCluster_failureCountForSubEndpoint
+ _endpoint_forwardUpdateInfo
- GCC_except_table127
- GCC_except_table48
- _carManager_isDisconnectCausedBySignalInterference
- _carManager_reportBonjourFailureToCarKit
CStrings:
+ "1005.8.1"
+ "Eligible for fast reactivate"
+ "Local HT first loss"
+ "[%{ptr}] Bonjour events monitoring: sending Bonjour info to CarKit: %@"
+ "[%{ptr}] Fail delay timer already running, discarding requested delay of %llu ms for subEndpoint [%{ptr}]%?{end}, failure count %ld"
+ "[%{ptr}] Ignoring subEndpoint [%{ptr}] failure, cluster is deactivated"
+ "[%{ptr}] Immediately triggering lost cluster buddy reconnect logic for [%{ptr}] (session state: %s, reason: %s)"
+ "[%{ptr}] Starting fail delay timer for seed %llu, subEndpoint [%{ptr}], with delay of %llu ms%?{end}, failure count %ld"
+ "carManager_reportBonjourEventToCarKit"
+ "endpoint_forwardUpdateInfo"
+ "void carManager_reportBonjourEventToCarKit(FigEndpointManagerRef, Boolean, APCarPlayFailureInfoReason)"
+ "void endpointCluster_startFailDelayTimerIfNeeded(FigEndpointRef, FigEndpointRef)"
- "1005.7.1"
- "[%{ptr}] Bonjour events monitoring: sending Bonjour failure info to CarKit: %@"
- "[%{ptr}] Immediately triggering lost cluster buddy reconnect logic for [%{ptr}] during startup\n"
- "[%{ptr}] Starting fail delay timer for seed %llu with delay of %llu seconds.\n"
- "carManager_reportBonjourFailureToCarKit"
- "void carManager_reportBonjourFailureToCarKit(FigEndpointManagerRef, Boolean, APCarPlayFailureInfoReason)"
- "void endpointCluster_startFailDelayTimerIfNeeded(FigEndpointRef)"
```
