## com.apple.driver.AppleT8103CLPCv3

> `com.apple.driver.AppleT8103CLPCv3`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-1794.0.7.0.2
-  __TEXT.__cstring: 0x386c
+1794.0.24.0.0
+  __TEXT.__cstring: 0x388d
   __TEXT.__const: 0x9d8
-  __TEXT_EXEC.__text: 0x5b818
+  __TEXT_EXEC.__text: 0x5bd8c
   __TEXT_EXEC.__auth_stubs: 0x8a0
-  __DATA.__data: 0xb200
-  __DATA.__common: 0xb880
+  __DATA.__data: 0xb258
+  __DATA.__common: 0xb900
   __DATA.__bss: 0x268
   __DATA_CONST.__mod_init_func: 0x110
   __DATA_CONST.__mod_term_func: 0x18

   __DATA_CONST.__kalloc_var: 0x370
   __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0xe0
-  Functions: 1318
-  Symbols:   1821
-  CStrings:  503
+  Functions: 1326
+  Symbols:   1828
+  CStrings:  504
 
Symbols:
+ __ZN4clpc3ane11JobTracking19sampleJobActiveTimeEjy
+ __ZN4clpc3cpu10DVFManager28updateScaledResidencyCounterEjy
+ __ZN4clpc3cpu10DVFManager33getSharedANEDPEThrottleLimitStateEj
+ __ZN4clpc3cpu10DVFManager33setSharedANEDPEThrottleLimitStateEjh
+ __ZN4clpc3cpu10DVFManager35getSharedANEEfficiencyLPMLimitStateEj
+ __ZN4clpc4CLPC30handleGetDeviceOrientationModeERb
+ __ZN4clpc4CLPC30handleSetDeviceOrientationModeEy
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/clpc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/clpc.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.JxxHhF/Sources/AppleCLPC/CLPC/source/power_map.cpp"
+ "1211111212221212111111"
+ "2026-07-14T21:26:48-07:00"
+ "AppleCLPC-1794.0.24"
+ "setAETSANEMaxControlEffortFunction"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/ane_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/ane_topology.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/apple_clpc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/clpc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/clpc.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_cluster_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_core_memstall_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_core_perf_sampler_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_dvfm_table_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_sched_interface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_temperature_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_timer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_topology.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/cpu_uncore_perf_sampler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/fabric_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/gpu_dvfm_table.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/perf_map_impl.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/pmc_voter_interface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7HWfMm/Sources/AppleCLPC/CLPC/source/power_map.cpp"
- "121111121222121211111"
- "2026-06-30T21:00:01-07:00"
- "AppleCLPC-1794.0.7.0.2"
```
