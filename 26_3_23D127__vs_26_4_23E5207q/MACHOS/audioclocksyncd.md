## audioclocksyncd

> `/usr/libexec/audioclocksyncd`

```diff

-1420.2.0.0.0
-  __TEXT.__text: 0x30c34
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x4ca0
-  __TEXT.__objc_methlist: 0x3028
+1440.23.0.0.0
+  __TEXT.__text: 0x2ef3c
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_stubs: 0x4e20
+  __TEXT.__objc_methlist: 0x3120
   __TEXT.__const: 0x170
-  __TEXT.__oslogstring: 0x3716
-  __TEXT.__cstring: 0x2739
-  __TEXT.__gcc_except_tab: 0x11c4
-  __TEXT.__objc_methname: 0x81d0
-  __TEXT.__objc_classname: 0x45c
-  __TEXT.__objc_methtype: 0x14fc
-  __TEXT.__unwind_info: 0xca0
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x198
+  __TEXT.__oslogstring: 0x3798
+  __TEXT.__cstring: 0x2bb9
+  __TEXT.__gcc_except_tab: 0x1284
+  __TEXT.__objc_methname: 0x849a
+  __TEXT.__objc_classname: 0x492
+  __TEXT.__objc_methtype: 0x1427
+  __TEXT.__unwind_info: 0xce0
+  __DATA_CONST.__auth_got: 0x4c8
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x23c0
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__cfstring: 0x24c0
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x5870
-  __DATA.__objc_selrefs: 0x19b0
-  __DATA.__objc_ivar: 0x49c
-  __DATA.__objc_data: 0xdc0
-  __DATA.__data: 0x360
+  __DATA.__objc_const: 0x5b08
+  __DATA.__objc_selrefs: 0x1a30
+  __DATA.__objc_ivar: 0x4bc
+  __DATA.__objc_data: 0xe10
+  __DATA.__data: 0x420
   __DATA.__bss: 0x138
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5525556E-7DE4-35E1-9F26-64BED925358F
-  Functions: 1274
-  Symbols:   203
-  CStrings:  2403
+  UUID: CBFE4529-3E5D-38CC-B59C-7AB4E44265BE
+  Functions: 1310
+  Symbols:   206
+  CStrings:  2465
 
Symbols:
+ _OBJC_CLASS_$_NSSet
+ _close
+ _connect
+ _fcntl
+ _if_nametoindex
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x27
+ _socket
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "%s failed to create socket"
+ "%s failed to set flag on the socket"
+ "%s sin6_scope_id =%d"
+ "+%s"
+ "-[TSDgPTPClock pokeRemoteIPv6Destination:withDestinationAddress:]"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/MSG/TSDMSGClockSession.mm"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
+ "/Library/Caches/com.apple.xbs/76DF28AD-4D00-4334-AF3A-0CF666CDDAF8/TemporaryDirectory.UuoToT/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
+ "1440.23"
+ "2"
+ "@\"TSXExternalSyncConfigData\""
+ "@24@0:8@\"NSCoder\"16"
+ "@32@0:8@16@?24"
+ "@88@0:8{?=II{?=QQ}{?=QQ}QQQ*}16"
+ "A"
+ "B32@0:8@16r*24"
+ "I36@0:8@16i24@?28"
+ "NSCoding"
+ "NSSecureCoding"
+ "None"
+ "Simulation file path: %s\n"
+ "T@\"NSString\",R,C,N,V_simulationFilePath"
+ "T@\"TSXExternalSyncConfigData\",R,N,V_config"
+ "TB,R"
+ "TI,R,N,V_triggerId"
+ "TQ,R,N,V_timeoutNs"
+ "TQ,R,N,V_toleranceExternalTriggerNs"
+ "TQ,R,N,V_toleranceSyncOutputNs"
+ "TSXExternalSyncConfigData"
+ "T{?=QQ},R,N,V_nominalTriggerDuration"
+ "T{?=QQ},R,N,V_syncMultiplier"
+ "_nominalTriggerDuration"
+ "_simulationFilePath"
+ "_syncMultiplier"
+ "_timeoutNs"
+ "_toleranceExternalTriggerNs"
+ "_toleranceSyncOutputNs"
+ "_triggerId"
+ "alignToExternalSync args:\nminTargetFrameDur: %llu\nmaxTargetFrameDur: %llu\nminOutputFrameDur: %llu\nmaxOutputFrameDur: %llu\nnominalSystemFramerate: %u\nfrequencyMultiplier: %u\ntriggerId: %u\nsyncId: %u\nisSimulation: %i\npenroseCSV: %s\n"
+ "decodeObjectOfClass:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "i36@0:8@16i24@?28"
+ "initWithCoder:"
+ "initWithConfigData:"
+ "nominalTriggerDuration"
+ "nominalTriggerDuration.denominator"
+ "nominalTriggerDuration.numerator"
+ "pokeRemoteIPv6Destination:withDestinationAddress:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setWithObject:"
+ "simulationFilePath"
+ "supportsSecureCoding"
+ "syncMultiplier.denominator"
+ "syncMultiplier.numerator"
+ "timeoutNs"
+ "toleranceExternalTriggerNs"
+ "toleranceSyncOutputNs"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"TSXExternalSyncConfigData\"16@?<v@?I>24"
+ "v32@0:8@16@?24"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockDiagnosticsManager.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/Diagnostics/TSDClockStatistics.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDClockSync.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDDaemonService.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKernelClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDKextNotifier.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDUserFilteredClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPManager.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/IOKit/TSDgPTPPort.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/MSG/TSDMSGClockSession.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/TSDDaemon.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync_exec/clocksyncd/XPC/TSDDaemonServiceServer.m"
- "1420.2"
- "@32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
- "I36@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16i24@?28"
- "T{?=II{?=QQ}{?=QQ}QQQ*},R,N,V_config"
- "alignToExternalSync args:\nminTargetFrameDur: %llu\nmaxTargetFrameDur: %llu\nminOutputFrameDur: %llu\nmaxOutputFrameDur: %llu\nnominalSystemFramerate: %u\nfrequencyMultiplier: %u\ntriggerId: %u\nsyncId: %u\nisSimulation: %i"
- "i36@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16i24@?28"
- "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
- "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?<v@?I>24"
- "{?=\"syncId\"I\"triggerId\"I\"nominalTriggerDuration\"{?=\"numerator\"Q\"denominator\"Q}\"syncMultiplier\"{?=\"numerator\"Q\"denominator\"Q}\"toleranceExternalTriggerNs\"Q\"toleranceSyncOutputNs\"Q\"timeoutNs\"Q\"simulationFilePath\"*}"
- "{?=II{?=QQ}{?=QQ}QQQ*}16@0:8"

```
