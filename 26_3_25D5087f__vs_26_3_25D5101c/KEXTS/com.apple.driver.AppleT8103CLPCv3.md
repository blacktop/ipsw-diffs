## com.apple.driver.AppleT8103CLPCv3

> `com.apple.driver.AppleT8103CLPCv3`

```diff

-1454.80.84.0.0
-  __TEXT.__cstring: 0x3463
+1454.80.86.0.1
+  __TEXT.__cstring: 0x3467
   __TEXT.__const: 0x9d0
-  __TEXT_EXEC.__text: 0x57b30
+  __TEXT_EXEC.__text: 0x57f24
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9f10
   __DATA.__common: 0xa200

   __DATA_CONST.__const: 0x5780
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x2d0
-  UUID: C533C4EB-2EFD-39C3-9B77-1D2B22CEE6EB
-  Functions: 1183
-  Symbols:   1936
+  UUID: F5167CC2-FBC3-3E54-80F6-9F12B643968D
+  Functions: 1185
+  Symbols:   1938
   CStrings:  479
 
Symbols:
+ __ZN4clpc3cpu10DVFManager25getNonCriticalLimitReasonEj
+ __ZNK4clpc4CLPC32cpuWorkloadLimiterEffortForStateENS_3cpu16ClusterPerfLevelEj
+ __ZZN4clpc4CLPC27sampleCPUDiscretionaryPowerEyyRNS_23SystemCPUWorkloadSampleERNS_12SamplerFlagsEENK3$_0clEv
- __ZN4clpc7control14PIPowerLimiterIfE6updateIyEEfffRNS0_20PIPowerLimiterConfigIfEET_NS0_12ControlRangeIfEE
Functions:
+ __ZN4clpc3cpu10DVFManager25getNonCriticalLimitReasonEj
+ __ZNK4clpc4CLPC32cpuWorkloadLimiterEffortForStateENS_3cpu16ClusterPerfLevelEj
~ __ZN4clpc4CLPC27sampleCPUDiscretionaryPowerEyyRNS_23SystemCPUWorkloadSampleERNS_12SamplerFlagsE : 1200 -> 1488
~ __ZN4clpc4CLPC24sampleCPUBackgroundPowerEyyRNS_23SystemCPUWorkloadSampleERNS_12SamplerFlagsE : 652 -> 904
~ __ZN4clpc4CLPC29sampleCPUEfficientGroupsPowerEyyRNS_23SystemCPUWorkloadSampleERNS_12SamplerFlagsE : 720 -> 992
~ __ZN4clpc4tgrp20ThreadGroupInterfaceINS0_17NormalThreadGroupEE13runControllerERKNS0_13ControlInputsERNS0_14ControlOutputsERNS0_16ControlReportingE : 29364 -> 29400
- __ZN4clpc7control14PIPowerLimiterIfE6updateIyEEfffRNS0_20PIPowerLimiterConfigIfEET_NS0_12ControlRangeIfEE
+ __ZZN4clpc4CLPC27sampleCPUDiscretionaryPowerEyyRNS_23SystemCPUWorkloadSampleERNS_12SamplerFlagsEENK3$_0clEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_map.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCyugAKsCD9Q-oVpUWuJ1PGjYqdExND6tQpgec/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_telemetry_pusher_impl.hpp"
+ "2026-01-04T19:24:26-08:00"
+ "AppleCLPC-1454.80.86.0.1"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/clpc.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_map.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD21ugB7DyiwVQMyYHH6gh0XUyzzOBpOEldLzQw/Library/Caches/com.apple.xbs/Sources/AppleCLPC/CLPC/source/power_telemetry_pusher_impl.hpp"
- "2025-12-05T22:52:16-08:00"
- "AppleCLPC-1454.80.84"

```
