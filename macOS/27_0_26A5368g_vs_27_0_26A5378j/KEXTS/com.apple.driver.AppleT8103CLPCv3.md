## com.apple.driver.AppleT8103CLPCv3

> `com.apple.driver.AppleT8103CLPCv3`

```diff

-  __TEXT.__cstring: 0x3996
+  __TEXT.__cstring: 0x386c
   __TEXT.__const: 0x9d8
-  __TEXT_EXEC.__text: 0x5baac
+  __TEXT_EXEC.__text: 0x5b818
   __TEXT_EXEC.__auth_stubs: 0x8a0
-  __DATA.__data: 0xb240
+  __DATA.__data: 0xb200
   __DATA.__common: 0xb880
   __DATA.__bss: 0x268
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x5ec8
+  __DATA_CONST.__const: 0x5ec0
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
   __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0xd8
-  Functions: 1321
-  Symbols:   2085
-  CStrings:  505
+  __DATA_CONST.__got: 0xe0
+  Functions: 1318
+  Symbols:   2083
+  CStrings:  503
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
Symbols:
+ __ZN4clpc4CLPC13systemQuiesceEv
+ __ZN4clpc4pmgr17PMCVoterInterface9onQuiesceEv
+ __ZN4clpc4priv6System23setCPUFastDiePowerLimitERNS_4CLPCEjj
+ _gIOPlatformQuiesceActionKey
- _OUTLINED_FUNCTION_19
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/clpc.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/power_map.cpp"
+ "2026-06-30T21:00:01-07:00"
+ "AppleCLPC-1794.0.7.0.2"
+ "SOCAON"
+ "SOCREST"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/clpc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/clpc.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/power_map.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oo3tYQ/Sources/AppleCLPC/CLPC/source/power_telemetry_pusher_impl.hpp"
- "2026-06-15T22:27:10-07:00"
- "AppleCLPC-1782.0.0.0.3"
- "scratch_config.layout.stride == sizeof(uint32_t)"
- "state.base_address"
- "telemetry_pusher.init(powerTelemetryPusherConfig())"

```
