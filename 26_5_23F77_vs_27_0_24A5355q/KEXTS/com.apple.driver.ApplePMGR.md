## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

```diff

-1774.120.2.0.0
-  __TEXT.__cstring: 0xf5ab
+1966.0.0.0.0
+  __TEXT.__cstring: 0xfe42
   __TEXT.__const: 0x2b0
-  __TEXT_EXEC.__text: 0x5ed34
+  __TEXT_EXEC.__text: 0x60f88
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x138
   __DATA.__common: 0x5e0
-  __DATA.__bss: 0xe0
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__bss: 0x160
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0xb838
-  __DATA_CONST.__kalloc_type: 0x9c0
+  __DATA_CONST.__const: 0xb9d8
+  __DATA_CONST.__kalloc_type: 0xb40
   __DATA_CONST.__kalloc_var: 0xfa0
-  UUID: A31F6739-C4AD-3223-9BB6-D82935D5A7EE
-  Functions: 2804
+  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: 62AC9651-973E-3FB3-AC9C-4B0F29C57FDD
+  Functions: 2853
   Symbols:   0
-  CStrings:  1751
+  CStrings:  1799
 
CStrings:
+ "11111111111111111112222222212212"
+ "11111111111111111112222222212212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112"
+ "12111112122212121122211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121121212212222221111211111122211211121211112222222222222222222222222222222222222222222222222"
+ "122222222222"
+ "ACCSlewRateAnalytics.cpp"
+ "ACCSlewRateAnalytics: CoreAnalytics Send Event Failure: 0x%x\n"
+ "ACCSlewRateAnalytics: Failed to create event dictionary\n"
+ "ACCSlewRateAnalytics: Failed to create event name string\n"
+ "ACCSlewRateAnalytics::ACCSlewRateAnalytics(IOService *, ca_pmgr_type_t)"
+ "ApplePMGR: CPU topology initialized from XNU: %u cores, %u complexes\n"
+ "ApplePMGR: Device 0x%x Vote Perf Domain %x Perf State %x on Power-Off \n"
+ "ApplePMGR: Error: DIE1 %s voltage state %u has perfLimit=0, reverting to shared\n"
+ "ApplePMGR: Single-die system, skipping DIE1 voltage state patching\n"
+ "ApplePMGR: Skipping %s (die=%u, not DIE1)\n"
+ "ApplePMGR: Skipping %s (type=%u, not CPU)\n"
+ "ApplePMGR: State[%u]: voltageState=%u, voltage=%u mV, perfLimit=0x%x\n"
+ "ApplePMGR: Warning: DIE1 %s Invalid DVFMStates array (dvfmStates=%p, count=%u)\n"
+ "ApplePMGR: Warning: DIE1 %s infoDict is missing\n"
+ "ApplePMGR: Warning: DIE1 voltage state count mismatch for %s: %u vs %u, using shared\n"
+ "ApplePMGR: [Die 1] %s: Skipping (voltageStatesID %u not in mapping table)\n"
+ "ApplePMGR: [Die 1] %s: Updated DVFMStates in infoDict with new voltage/frequency data\n"
+ "ApplePMGR: [Die 1] %s: Using shared voltage states (no %s property)\n"
+ "UInt32 ApplePMGRv2::_getComplexToDie(UInt32)"
+ "UInt32 ApplePMGRv2::_getCoreToDie(UInt32)"
+ "_cpuComplexCount <= kClusterIDMaxCount"
+ "_dieCount <= kDieMaxCount"
+ "com.apple.private.pmgr.nrg.reporting"
+ "com.apple.socpm.slew_rate"
+ "cpu < _cpuCoreCount"
+ "cpu-power-gate-latency-ns"
+ "dieID < _dieCount"
+ "dieId < _dieCount"
+ "dr"
+ "eh"
+ "handle->getAnalyticsType() == type"
+ "md"
+ "ns"
+ "site.ACCSlewRateAnalytics"
+ "site.SlewRateEvents"
+ "slew_rate"
+ "sn"
+ "static void *ACCSlewRateAnalytics::operator new(size_t)"
+ "tp"
+ "virtual ApplePMGRAnalytics *ApplePMGR::getAnalyticsManager(ApplePMGRAnalytics::ca_pmgr_type_t, ApplePMGRAnalytics::ca_ps_state_t, UInt32)"
+ "virtual ApplePMGRAnalytics *ApplePMGRv2::getAnalyticsManager(ApplePMGRAnalytics::ca_pmgr_type_t, ApplePMGRAnalytics::ca_ps_state_t, UInt32)"
+ "virtual void ApplePMGRv2::enableCPUCores(UInt64, bool)"
+ "void ApplePMGR::updateDie1CPUVoltages()"
+ "void ApplePMGRv2::_cpuTopologyInit()"
+ "voltageState < perfDomain->voltageStateCount"
+ "xnuTopology"
- "111111111112222222212212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112"
- "1211111212221212112221112111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112112121221222222111121111112221121112121111"

```
