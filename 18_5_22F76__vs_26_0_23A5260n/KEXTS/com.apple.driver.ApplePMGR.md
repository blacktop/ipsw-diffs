## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

```diff

-1555.120.3.0.0
-  __TEXT.__const: 0x258
-  __TEXT.__cstring: 0xeca4
-  __TEXT_EXEC.__text: 0x547b4
+1774.0.4.0.0
+  __TEXT.__cstring: 0xf1c3
+  __TEXT.__const: 0x280
+  __TEXT_EXEC.__text: 0x66214
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x100
-  __DATA.__common: 0x470
-  __DATA.__bss: 0x40
-  __DATA_CONST.__auth_got: 0x388
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__mod_init_func: 0x18
-  __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x7a70
-  __DATA_CONST.__kalloc_type: 0x700
+  __DATA.__data: 0x138
+  __DATA.__common: 0x5b0
+  __DATA.__bss: 0xe8
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__mod_init_func: 0x40
+  __DATA_CONST.__mod_term_func: 0x40
+  __DATA_CONST.__const: 0xb5c8
+  __DATA_CONST.__kalloc_type: 0x980
   __DATA_CONST.__kalloc_var: 0xe60
-  UUID: B01CCF7A-87FA-3119-8A49-5020092211AF
-  Functions: 2179
+  UUID: F57CEA2B-97B2-3701-84C4-582BD8047DC9
+  Functions: 2700
   Symbols:   0
-  CStrings:  1615
+  CStrings:  1721
 
CStrings:
+ "!getFeatureValue(kFeatureAPWakeSourcesDisable)"
+ "\"%s, Out of Memory \\n\" @%s:%d"
+ "\"ApplePMGR: %s:%u \" \"addr 0x%lx map %d (%s) 0x%x & 0x%llx is 0x%llx vs. 0x%llx after %u ticks die %u\\n\" @%s:%d"
+ "\"ApplePMGRUserClient: %s:%u REQUIRE failed: %s\" @%s:%d"
+ "\"addr 0x%lx map %d (%s) offset 0x%x (%s) val 0x%x & mask 0x%x != 0x%x (expected) after %u ticks die %u\\n\" @%s:%d"
+ "111111111112222222212212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112"
+ "12111112122212121"
+ "1211111212221212111111111111"
+ "121111121222121211222111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112111211121112112121221222222111121111112221121112121111"
+ "12222222222222222222222222"
+ "AbstractPMGR"
+ "AbstractPMGR *ApplePMGRv2::getChildPMGRInstance(UInt32) const"
+ "AnalyticsFactory.cpp"
+ "ApplePMGRAnalytics *PMGR_CA_FACTORY::getAnalyticsManager(IOService *, ApplePMGRAnalytics::ca_pmgr_type_t, ApplePMGRAnalytics::ca_ps_state_t, UInt32)"
+ "ApplePMGRArmFunctions.cpp"
+ "ApplePMGRBase"
+ "ApplePMGRFunctionEnablePSDService"
+ "ApplePMGRFunctionGetServiceState"
+ "ApplePMGRFunctionResetPSDService"
+ "ApplePMGRFunctionVoteCriticalLltMode"
+ "ApplePMGRUserClient"
+ "ApplePMGRUserClient.cpp"
+ "ApplePMGRv2"
+ "ApplePMGRv2.cpp"
+ "ApplePMGRv2.h"
+ "ApplePMGRv2: %s, Num instances: %d\n"
+ "ApplePMGRv2: Found Remote/Child PMGR Instance:%u @ 0x%p\n"
+ "ApplePMGRv2: Started %s\n"
+ "ApplePMGRv2: Starting %s\n"
+ "CLOCK_GATE_LAT_OFF"
+ "CLOCK_GATE_LAT_ON"
+ "DEV0x%x"
+ "FAB"
+ "IOReturn ApplePMGR::getBootProgressRegister(UInt32 *)"
+ "IOUserClientDefaultLocking"
+ "IOUserClientDefaultLockingSetProperties"
+ "IOUserClientDefaultLockingSingleThreadExternalMethod"
+ "IOUserClientEntitlements"
+ "LatencyEvents.cpp"
+ "PMGR-CoreAnalytics Send Event Failure: 0x%x \n"
+ "POWER_GATE_LAT_OFF"
+ "POWER_GATE_LAT_ON"
+ "PSAnalytics.cpp"
+ "PSAnalytics::PSAnalytics(IOService *, ca_pmgr_type_t, ca_ps_state_t, UInt32)"
+ "PS_RESET_LAT"
+ "SERVICE_GATE_LAT_OFF"
+ "SERVICE_GATE_LAT_ON"
+ "SERVICE_RESET_LAT_ON"
+ "UInt32 ApplePMGRv2::_getParamValue(Param)"
+ "_analyticsLockGrp"
+ "_analyticsTimer"
+ "_gPMGR[CPU_CHIPLET]"
+ "_gPMGR[chiplet]"
+ "_gPMGR[id]"
+ "_latencyObjCount >= count"
+ "_lockGrp"
+ "_pmgr"
+ "ap-wake-source-flags"
+ "ap-wake-sources-disable"
+ "avgTime"
+ "bool ApplePMGRv2::_validParam(Param)"
+ "bpr"
+ "ca-pmgr-group"
+ "chiplet-count"
+ "chipletCount >= chipInstances"
+ "com.apple.private.ApplePMGRUserClient.access"
+ "com.apple.private.ApplePMGRUserClient.get-bpr"
+ "com.apple.socpm.DIE%u.%s"
+ "cpmgr"
+ "die < ApplePMGRAnalytics::kPSMaxNumDies"
+ "die < _target->getDieCount()"
+ "die < getDieCount()"
+ "flag.index < kAPWakeSourceMaxCount"
+ "getPMGRChildInstances"
+ "id < chipInstances"
+ "inst"
+ "m:0x%-6llx, M:0x%-6llx, A:0x%-6llx, N:0x%-2x"
+ "maxTime"
+ "minTime"
+ "name"
+ "ncalls"
+ "operator new"
+ "perfLimitReason >= ApplePMGRNub::kPerfLimitingReasonDVDFactor1Count"
+ "pmgr-analytics"
+ "pmgr-ver"
+ "ptr"
+ "ret == kIOReturnSuccess"
+ "site.AbstractPMGR"
+ "site.ApplePMGRBase"
+ "site.ApplePMGRFunctionEnablePSDService"
+ "site.ApplePMGRFunctionGetServiceState"
+ "site.ApplePMGRFunctionResetPSDService"
+ "site.ApplePMGRFunctionVoteCriticalLltMode"
+ "site.ApplePMGRUserClient"
+ "site.ApplePMGRv2"
+ "site.LatencyEvents"
+ "site.PSAnalytics"
+ "state < NUM_LOGICAL_PS_STATE"
+ "static void *PSAnalytics::operator new(size_t)"
+ "type < NUM_CA_PMGR_EVENT"
+ "virtual IOReturn ApplePMGR::_getClockReqMemory(unsigned int, void *)"
+ "virtual IOReturn ApplePMGR::_getPTDRangeInfo(UInt32, ApplePMGRNub::PTDRangeInfo *, UInt32 *)"
+ "virtual IOReturn ApplePMGRFunctionVoteCriticalLltMode::callFunction(void *, void *, void *)"
+ "virtual SInt32 ApplePMGR::getEnergyNodeProperties(UInt32, UInt32, UInt32)"
+ "virtual UInt32 ApplePMGR::_getCIOClusterIndex(UInt32)"
+ "virtual UInt32 ApplePMGR::_getPerformanceLimit(UInt32)"
+ "virtual UInt32 ApplePMGR::_returnCPUPerfStateInfo(UInt32, UInt32, UInt32 *, UInt32 *, double *)"
+ "virtual UInt64 ApplePMGR::_getDeviceIdleTime(UInt32, UInt32)"
+ "virtual UInt64 ApplePMGR::_getEnergyCounter(UInt32, UInt32)"
+ "virtual UInt64 ApplePMGR::_getEventActiveTime(UInt32, UInt32)"
+ "virtual UInt64 ApplePMGR::_getEventCount(UInt32, UInt32)"
+ "virtual UInt64 ApplePMGR::getPerfCycleCount(UInt32, UInt32, UInt32)"
+ "virtual bool ApplePMC::getBWRMemory(UInt32, UInt64 *)"
+ "virtual bool ApplePMGR::_getDeviceStatus(DeviceID, UInt32)"
+ "virtual bool ApplePMGRUserClient::start(IOService *)"
+ "virtual bool ApplePMGRv2::start(IOService *)"
+ "virtual bool LatencyEvents::getLatStats(UInt64 *, UInt64 *, UInt64 *, UInt32 *)"
+ "virtual void ApplePMC::restorePMC(UInt32)"
+ "virtual void ApplePMC::stateChange(bool, UInt32, UInt32, bool)"
+ "virtual void ApplePMGR::_cpuIdleInit(ml_processor_info_t *)"
+ "virtual void ApplePMGR::_enableDevice(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "virtual void ApplePMGR::_enableDeviceAutoClockGatingGated(uintptr_t, uintptr_t, uintptr_t)"
+ "virtual void ApplePMGR::_handleCPUPerfRequest(UInt32, UInt32, bool, UInt32, ApplePMGRNub::PerfLimitingReason)"
+ "virtual void ApplePMGR::_handleCPUPerfStateRequest(UInt32, UInt32, bool)"
+ "virtual void ApplePMGR::_handlePerfStateRequest(UInt32, PerfDomainID, UInt32)"
+ "virtual void ApplePMGR::_pmPerformanceBoost(UInt32)"
+ "virtual void ApplePMGR::configMiscCores(UInt64, bool)"
+ "virtual void ApplePMGR::getCurrentCoreComplex(UInt32 *, UInt32 *)"
+ "virtual void ApplePMGRv2::_enableDevice(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
+ "virtual void ApplePMGRv2::_enablePSDService(uintptr_t, uintptr_t, uintptr_t, uintptr_t, char *)"
+ "virtual void PSAnalytics::publish()"
+ "void ApplePMC::_enableDynamicVoterInterface(bool, UInt16, UInt32)"
+ "void ApplePMC::_enableStaticVoterInterface(UInt32, bool, UInt32)"
+ "void ApplePMGR::_initAnalyticsTimer()"
+ "void ApplePMGR::_initUserClient()"
+ "void ApplePMGR::setATCDpClockSourceGated(UInt32, UInt32, UInt32, UInt32)"
+ "void ApplePMGR::submitVoteCriticalLltModeGated(bool, UInt32, UInt32)"
+ "void ApplePMGRv2::_initAnalyticsTimer()"
+ "void ApplePMGRv2::_publishNubs(IORegistryEntry *)"
+ "void ApplePMGRv2::getPMGRChildInstances()"
+ "voterID < sizeof(_criticalLltModeVotes[0]) * CHAR_BIT"
- "\"ApplePMGR: %s:%u \" \"map %d (%s) 0x%x & 0x%llx is 0x%llx vs. 0x%llx after %u ticks die %u\\n\" @%s:%d"
- "\"map %d (%s) offset 0x%x (%s) val 0x%x & mask 0x%x != 0x%x (expected) after %d ticks die %u\\n\" @%s:%d"
- "%sCPU%u%u"
- "12222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111111111111111111111111111111111111111222222221122222222212111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221"
- "IOReturn ApplePMGR::_getClockReqMemory(unsigned int, void *)"
- "IOReturn ApplePMGR::_getPTDRangeInfo(UInt32, ApplePMGRNub::PTDRangeInfo *, UInt32 *)"
- "OSDictionary *ApplePMGRNub::getPerfDomainInfoForCPUClusterID(UInt32)"
- "UInt32 ApplePMGR::_getCIOClusterIndex(DeviceID)"
- "UInt32 ApplePMGRNub::getCPUPerfStateInfo(UInt32, UInt32, UInt32 *, UInt32 *, double *)"
- "UInt32 ApplePMGRNub::getCPUPerformanceLimit(UInt32)"
- "UInt64 ApplePMGR::_getDeviceIdleTime(DeviceID, UInt32)"
- "UInt64 ApplePMGR::_getEnergyCounter(EnergyCounterID, UInt32)"
- "UInt64 ApplePMGR::_getEventActiveTime(EventID, UInt32)"
- "UInt64 ApplePMGR::_getEventCount(EventID, UInt32)"
- "UInt64 ApplePMGR::getPerfCycleCount(PerfRegGroup, UInt32, UInt32)"
- "bool ApplePMGR::_getDeviceStatus(DeviceID, UInt32)"
- "cluster_id < _provider->_cpuComplexCount"
- "complex < _provider->_cpuComplexCount"
- "die < _target->_dieCount"
- "perfLimitReason >= kPerfLimitingReasonDVDFactor1Count"
- "virtual bool ApplePMC::getBWRMemory(UInt16, UInt64 *)"
- "virtual void ApplePMC::restorePMC()"
- "virtual void ApplePMC::stateChange(bool, UInt16, UInt32, bool)"
- "virtual void ApplePMGR::configMiscCores(UInt32, bool)"
- "void ApplePMC::_enableDynamicVoterInterface(bool, UInt16)"
- "void ApplePMC::_enableStaticVoterInterface(UInt32, bool)"
- "void ApplePMGR::_cpuIdleInit(ml_processor_info_t *)"
- "void ApplePMGR::_enableDevice(uintptr_t, uintptr_t, uintptr_t, uintptr_t)"
- "void ApplePMGR::_enableDeviceAutoClockGatingGated(uintptr_t, uintptr_t, uintptr_t)"
- "void ApplePMGR::_handlePerfStateRequest(UInt32, PerfDomainID, UInt32)"
- "void ApplePMGR::_pmPerformanceBoost(UInt32)"
- "void ApplePMGR::getCurrentCoreComplex(UInt32 *, UInt32 *)"
- "void ApplePMGR::setATCDpClockSourceGated(UInt32, UInt32, UInt32)"
- "void ApplePMGRNub::requestCPUPerfState(UInt32, UInt32)"
- "void ApplePMGRNub::requestCPUPerformance(UInt32, UInt32, UInt32, PerfLimitingReason)"

```
