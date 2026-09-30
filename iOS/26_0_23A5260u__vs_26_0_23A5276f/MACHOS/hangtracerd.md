## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-375.0.0.0.0
-  __TEXT.__text: 0x34b48
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_stubs: 0x5620
-  __TEXT.__objc_methlist: 0x20cc
+378.0.0.0.0
+  __TEXT.__text: 0x33a28
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_stubs: 0x5560
+  __TEXT.__objc_methlist: 0x209c
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x519d
-  __TEXT.__oslogstring: 0x630f
-  __TEXT.__objc_classname: 0x341
-  __TEXT.__objc_methname: 0x8964
-  __TEXT.__objc_methtype: 0x103a
-  __TEXT.__gcc_except_tab: 0x57c
-  __TEXT.__unwind_info: 0xa30
-  __DATA_CONST.__auth_got: 0x820
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2010
-  __DATA_CONST.__cfstring: 0x6a20
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__cstring: 0x4873
+  __TEXT.__oslogstring: 0x639b
+  __TEXT.__objc_classname: 0x328
+  __TEXT.__objc_methname: 0x88c8
+  __TEXT.__objc_methtype: 0x1051
+  __TEXT.__gcc_except_tab: 0x3b8
+  __TEXT.__unwind_info: 0xa20
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x1f08
+  __DATA_CONST.__cfstring: 0x5e00
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x4aa0
-  __DATA.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA.__objc_const: 0x4a10
+  __DATA.__objc_selrefs: 0x1b00
   __DATA.__objc_ivar: 0x42c
-  __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x548
-  __DATA.__bss: 0xac0
+  __DATA.__objc_data: 0x960
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x538
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: D1694CDA-9E16-3B90-8DFC-F555D3D86266
-  Functions: 1164
-  Symbols:   412
-  CStrings:  3830
+  UUID: B24819D2-9633-38A5-9DDD-BD6CDA1EE705
+  Functions: 1158
+  Symbols:   389
+  CStrings:  3622
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
- _ADClientAddValueForScalarKey
- _ADClientPushValueForDistributionKey
- _ADClientSetValueForScalarKey
- _NSLog
- _NSStringFromSelector
- __CFCopyServerVersionDictionary
- __CFCopySupplementalVersionDictionary
- ___strlcat_chk
- ___strlcpy_chk
- __kCFSystemVersionBuildVersionKey
- __kCFSystemVersionProductNameKey
- __kCFSystemVersionProductVersionKey
- _host_statistics64
- _ledger
- _mach_host_self
- _mach_memory_info
- _memorystatus_control
- _pid_for_task
- _rename
- _strlen
- _uname
- _vm_deallocate
- _vm_kernel_page_size
- _write
CStrings:
+ "@128@0:8i16Q20Q28Q36Q44Q52q60B68B72B76@80@88@96@104@112@120"
+ "@92@0:8@16Q24Q32Q40B48q52@60B68@72B80@84"
+ "Invalid object(s) of class '%@' and '%@' passed into StateInfo timestamp comparator."
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary '%@' during sorting."
+ "Recent State Info for process with pid '%d': %{public}@"
+ "StateInfo"
+ "T@\"NSArray\",R,C,N,V_recentStateInfo"
+ "T@\"NSArray\",R,C,V_recentStateInfo"
+ "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB[10{HTRBStateInfo=QC}]AQ}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
+ "_recentStateInfo"
+ "initWithPid:threadID:startTime:endTime:reportedTime:blownFenceID:hangSubtype:isFirstPartyApp:isThirdPartyDevSupportModeHang:displayedInHUD:serviceName:reason:processName:processPath:userActionData:recentStateInfo:"
+ "initWithServiceName:threadID:startTime:endTime:saveTailspin:subType:userActionData:isThirdPartyDevSupportModeHang:processInfo:captureMicroHang:recentStateInfo:"
+ "q24@?0@8@16"
+ "received incoming work notification from %s, adding increment block to queue '%s' for com.apple.hangtracerd.processing"
+ "received work completion notification from %s, adding decrement block to queue '%s'"
+ "recentStateInfo"
+ "recordHang:threadID:startTime:endTime:saveTailspin:subtype:userActionData:isThirdPartyDevSupportModeHang:captureMicroHang:recentStateInfo:"
+ "stateInfo"
+ "taskEnum"
+ "timestamp"
+ "v84@0:8@16Q24Q32Q40B48q52@60B68B72@76"
- "\"%@\" : %lu"
- "\"Accessory\""
- "\"Audio\""
- "\"Bg_Content_Fetch\""
- "\"Bg_Continuous\""
- "\"Bg_Download\""
- "\"Bg_Finish_Task\""
- "\"Bg_Finish_Task_Aft_Bg_Content_Fetch\""
- "\"Bg_Finish_Task_Aft_Bg_Download\""
- "\"Bg_Finish_Task_Aft_Periodic_Task\""
- "\"Bg_Finish_Task_Unbounded\""
- "\"Bg_Periodic_Task\""
- "\"Bg_Resume\""
- "\"Bg_Suspend\""
- "\"Bg_Transient_Wakeup\""
- "\"Bg_UI\""
- "\"Bluetooth\""
- "\"Continuity\""
- "\"Extension\""
- "\"Finish_Task_Aft_Notification\""
- "\"Foreground\""
- "\"InterApp_Audio\""
- "\"Location\""
- "\"Network_Auth\""
- "\"Newsstand_Download\""
- "\"Notification_Handling\""
- "\"Processes\" :\n[\n"
- "\"UnknownAssertion_%d\""
- "\"ViewService\""
- "\"VoIP\""
- "\"Zones\" :\n[\n"
- "\"}\n"
- "%@ %@ (%@)"
- "%@]"
- ","
- ", \"Assertions\":["
- "/"
- "/Library/Logs/CrashReporter//%@"
- "/var/root/Library/Caches/hangtracerd//%@"
- "???"
- "@120@0:8i16Q20Q28Q36Q44Q52q60B68B72B76@80@88@96@104@112"
- "@84@0:8@16Q24Q32Q40B48q52@60B68@72B80"
- "Could not create file - won't take a memory snapshot: %s %s"
- "HTPrefsObserver_hangtracerd"
- "HangTracerEnableMemoryLogging"
- "HangTracerMemoryLoggingInterval"
- "Memory Logging Disabled"
- "Memory Logging Enabled"
- "N"
- "No_Name"
- "Recieved incoming work notification from %s, adding increment block to queue '%s' for com.apple.hangtracerd.processing"
- "Recieved work completion notification from %s, adding decrement block to queue '%s'"
- "TB,R,V_memoryLoggingEnabled"
- "TI,V_memoryLoggingIntervalSec"
- "UnknownProcess_%d"
- "Y"
- "]\n"
- "],\n"
- "^{?=II[8{hangEvent=QQdAiCCCC^{_opaque_pthread_t}Qi[64c][256c]B^?AQAQAQBB}][10{HTAssertionInfo=QQQQ[64c]B}]iQAQ}"
- "_memoryLoggingEnabled"
- "_memoryLoggingIntervalSec"
- "active_count"
- "com.apple.hangtracer.%@.%@"
- "com.apple.hangtracer.DaemonTimeout.HangCount"
- "com.apple.hangtracer.HTFenceLogsGeneratedAtDailyReset"
- "com.apple.hangtracer.HTLogsFenceHang.PreTailspin"
- "com.apple.hangtracer.HTLogsGeneratedAtDailyReset"
- "com.apple.hangtracer.HTLogsMissedDueToGlobalLimit.%@"
- "com.apple.hangtracer.HTLogsMissedDueToGlobalLimit.Total"
- "com.apple.hangtracer.HTLogsMissedDueToProcessLimit.%@"
- "com.apple.hangtracer.HTLogsMissedDueToProcessLimit.Total"
- "com.apple.hangtracer.HTLongLogsGeneratedAtDailyReset"
- "com.apple.hangtracer.HTMicroHangLogsGeneratedAtDailyReset"
- "com.apple.hangtracer.HTShortLogsGeneratedAtDailyReset"
- "com.apple.hangtracer.HTThirdPartyLogsGeneratedAtDailyReset"
- "com.apple.ht_always_on.%s.%@"
- "com.apple.ht_app_exit_hang.%s.%s"
- "com.apple.ht_app_exit_hang.count"
- "com.apple.ht_app_exit_hang.log_capture"
- "com.apple.ht_assertion_stats.hang_overlap_ms"
- "com.apple.ht_assertion_stats.hang_overlap_percent"
- "com.apple.ht_debugger_attached.%@.%s"
- "compressions"
- "compressor_page_count"
- "cow_faults"
- "decompressions"
- "dictionaryWithCapacity:"
- "external_page_count"
- "faults"
- "free_count"
- "hits"
- "host_statistics64 failed"
- "iOS"
- "iPhone OS"
- "inactive_count"
- "initPropertyMemoryLoggingIntervalSec:"
- "initWithPid:threadID:startTime:endTime:reportedTime:blownFenceID:hangSubtype:isFirstPartyApp:isThirdPartyDevSupportModeHang:displayedInHUD:serviceName:reason:processName:processPath:userActionData:"
- "initWithServiceName:threadID:startTime:endTime:saveTailspin:subType:userActionData:isThirdPartyDevSupportModeHang:processInfo:captureMicroHang:"
- "internal_page_count"
- "lookups"
- "memory-snapshot-%@.ips"
- "memoryLoggingEnabled"
- "memoryLoggingInterval changed %u -> %u"
- "memoryLoggingIntervalSec"
- "numberWithUnsignedLong:"
- "page_size"
- "pageins"
- "pageouts"
- "phys_footprint"
- "purgeable_count"
- "purges"
- "reactivations"
- "recordHang:threadID:startTime:endTime:saveTailspin:subtype:userActionData:isThirdPartyDevSupportModeHang:captureMicroHang:"
- "setMemoryLoggingIntervalSec:"
- "speculative_count"
- "stringWithCapacity:"
- "substringFromIndex:"
- "swapins"
- "swapouts"
- "throttled_count"
- "total_uncompressed_pages_in_compressor"
- "v20@0:8I16"
- "v32@?0@8@\"NSNumber\"16^B24"
- "v76@0:8@16Q24Q32Q40B48q52@60B68B72"
- "wire_count"
- "zero_fill_count"
- "{\n\"Model\" : \"%s\",\n\"Timestamp\" : \"%@\",\n\"OSVersion\" : \"%@\"\n}\n"
- "{ \"Name\" : \"%s\", \"Pages\" : %llu }"
- "{\"ProcessName\":\"%@\", \"Priority\":%d, \"Footprint\":%d, \"Dirty\":\"%s\""
- "{\"bug_type\":\"152\",\"os_version\":\""
- "}"
- "}\n"

```
