## ReportCrashService

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/XPCServices/ReportCrashService.xpc/ReportCrashService`

```diff

-  __TEXT.__text: 0x4fa20
-  __TEXT.__auth_stubs: 0x26d0
-  __TEXT.__objc_stubs: 0x3d40
-  __TEXT.__objc_methlist: 0xfac
-  __TEXT.__const: 0xde0
-  __TEXT.__cstring: 0x59d5
-  __TEXT.__objc_methname: 0x4563
-  __TEXT.__oslogstring: 0x330e
+  __TEXT.__text: 0x53218
+  __TEXT.__auth_stubs: 0x2710
+  __TEXT.__objc_stubs: 0x3de0
+  __TEXT.__objc_methlist: 0x1034
+  __TEXT.__const: 0x12f0
+  __TEXT.__cstring: 0x5ab5
+  __TEXT.__objc_methname: 0x47fd
+  __TEXT.__oslogstring: 0x346e
   __TEXT.__objc_classname: 0x4d1
-  __TEXT.__objc_methtype: 0xd21
+  __TEXT.__objc_methtype: 0xd71
   __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__dlopen_cstrs: 0xa5
-  __TEXT.__swift5_typeref: 0x666
+  __TEXT.__swift5_typeref: 0x75e
   __TEXT.__swift5_capture: 0x2a4
-  __TEXT.__constg_swiftt: 0x428
+  __TEXT.__constg_swiftt: 0x4e8
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x4ef
-  __TEXT.__swift5_fieldmd: 0x6d8
+  __TEXT.__swift5_reflstr: 0x597
+  __TEXT.__swift5_fieldmd: 0x840
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift5_proto: 0x9c
+  __TEXT.__swift5_types: 0x64
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x40
-  __TEXT.__unwind_info: 0xbd8
-  __TEXT.__eh_frame: 0x810
-  __DATA_CONST.__const: 0x16c0
+  __TEXT.__unwind_info: 0xcd8
+  __TEXT.__eh_frame: 0xa10
+  __DATA_CONST.__const: 0x1998
   __DATA_CONST.__cfstring: 0x7a80
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x570
-  __DATA_CONST.__objc_arraydata: 0x390
+  __DATA_CONST.__objc_arraydata: 0x3a0
+  __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA_CONST.__auth_got: 0x1378
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__auth_ptr: 0x358
-  __DATA.__objc_const: 0x2b60
-  __DATA.__objc_selrefs: 0x10e8
-  __DATA.__objc_ivar: 0x278
+  __DATA_CONST.__auth_got: 0x1398
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__auth_ptr: 0x360
+  __DATA.__objc_const: 0x2c10
+  __DATA.__objc_selrefs: 0x1148
+  __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x958
-  __DATA.__data: 0xbc0
+  __DATA.__data: 0xcd0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xab0
+  __DATA.__bss: 0x1530
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1027
-  Symbols:   624
-  CStrings:  3324
+  Functions: 1128
+  Symbols:   623
+  CStrings:  3358
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _IOPMPSRawExternalConnectedKey
+ _OBJC_CLASS_$_NSJSONSerialization
+ _fclose
+ _fdopen
+ _pipe
+ _posix_spawn
+ _posix_spawn_file_actions_addclose
+ _posix_spawn_file_actions_adddup2
+ _posix_spawn_file_actions_destroy
+ _posix_spawn_file_actions_init
+ _runDiagToolWithArg
+ _waitpid
- _IOPSCopyExternalPowerAdapterDetails
- _IOPSCopyPowerSourcesInfo
- _IOPSCopyPowerSourcesList
- _IOPSGetPowerSourceDescription
- _IOPSInternalType
- _IOPSIsChargingKey
- _IOPSRawExternalConnectedKey
- _IOPSTransportTypeKey
- ___stdoutp
- _fflush
- _pclose
- _popen
- _swift_unknownObjectRelease_n
CStrings:
+ "AppleRawExternalConnected"
+ "AppleSmartBattery"
+ "B60@0:8@16i24i28B32^@36^@44^@52"
+ "B76@0:8Q16Q24i32^i36^@44^i52^i60^B68"
+ "Could not read malloc_num_zones at 0x%llx (got %lu bytes, expected %zu)"
+ "ExternalConnected"
+ "Failed to enumerate AppleSmartBattery services"
+ "Failed to read AppleSmartBattery properties"
+ "JSONObjectWithData:options:error:"
+ "MetricKit unavailable, skipping ExcResource pre-extraction"
+ "No AppleSmartBattery service found"
+ "Prefetched filteredLog contained non-string element; ignoring"
+ "Prefetched filteredLog payload was not an array (err=%{public}@); ignoring"
+ "Skipping crash reporter extension for restrictive sandbox profile: %{public}@"
+ "T@\"NSArray\",C,N,V_prefetchedFilteredLog"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,N,V_ktriage_info"
+ "TB,N,V_disallowInProcessSyslogQuery"
+ "TB,R,N,V_is64Bit"
+ "Ti,R,N,V_cpuType"
+ "Ti,R,N,V_ppid"
+ "Unable to allocate argv for '%s'"
+ "Unable to create pipe for '%s' (errno %d)"
+ "Unable to spawn '%s' (error %d)"
+ "Using daemon-prefetched filteredLog (%lu lines)"
+ "_disallowInProcessSyslogQuery"
+ "_prefetchedFilteredLog"
+ "binaryUUIDString"
+ "buildFilteredSyslogQueryForProcName:procID:signal:isDriverkit:outPids:outSenders:outPredicates:"
+ "callStackPayload"
+ "container"
+ "disallowInProcessSyslogQuery"
+ "extractCrashIdentityFromKcdata:size:machException:outPid:outProcName:outSignal:outExceptionType:outIsCorpseFork:"
+ "failed to read syslog"
+ "is64Bit"
+ "ktriage_info"
+ "length > 0"
+ "metricKitClientIdentifier"
+ "ppid"
+ "prefetchedFilteredLog"
+ "prefetched_filtered_log"
+ "setDisallowInProcessSyslogQuery:"
+ "setPrefetchedFilteredLog:"
- "\nError closing pipe of '%s' (errno %d)"
- "%s %@"
- "Failed to get power source description for index %ld"
- "Failed to get power sources info"
- "Failed to get power sources list"
- "Internal"
- "Is Charging"
- "No power sources found"
- "Raw External Connected"
- "Transport Type"
- "Unable to open '%s' (errno %d)"

```
