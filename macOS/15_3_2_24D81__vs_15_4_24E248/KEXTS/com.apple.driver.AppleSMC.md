## com.apple.driver.AppleSMC

> `com.apple.driver.AppleSMC`

```diff

-726.80.2.0.0
-  __TEXT.__cstring: 0x77ab
+728.100.9.0.0
+  __TEXT.__cstring: 0x79cc
   __TEXT.__const: 0x1d0
   __TEXT.__os_log: 0xd26
-  __TEXT_EXEC.__text: 0x25d88
+  __TEXT_EXEC.__text: 0x270bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
-  __DATA.__common: 0x468
+  __DATA.__common: 0x490
   __DATA.__bss: 0xd0
-  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__auth_got: 0x4d8
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__mod_init_func: 0xb0
-  __DATA_CONST.__mod_term_func: 0xa0
-  __DATA_CONST.__const: 0xd4a0
-  __DATA_CONST.__kalloc_type: 0x6c0
+  __DATA_CONST.__mod_init_func: 0xb8
+  __DATA_CONST.__mod_term_func: 0xa8
+  __DATA_CONST.__const: 0xd720
+  __DATA_CONST.__kalloc_type: 0x700
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: B1558B61-A221-315F-B1EB-C6DFB53E8541
-  Functions: 825
-  Symbols:   1729
-  CStrings:  893
+  UUID: 6E99B635-D07F-30CC-B2C0-61E92820A8CA
+  Functions: 845
+  Symbols:   1777
+  CStrings:  906
 
Symbols:
+ _GLOBAL__sub_I_AppleSMCKDebug.cpp
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _ZN14AppleSMCKDebug12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.1
+ _ZN14AppleSMCKDebug12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.2
+ _ZN18AppleSMCACAMDriver5startEP9IOService.cold.2
+ _ZN19AppleSMCEventBuffer12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.1
+ _ZN19AppleSMCEventBuffer12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.2
+ _ZN22AppleSMCAcamLogHandler12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.1
+ _ZN22AppleSMCAcamLogHandler12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo.cold.2
+ _ZN24AppleSMCSensorDispatcher16createTimerEventEj.cold.1
+ _ZN24AppleSMCSensorDispatcher16createTimerEventEj.cold.2
+ _ZN24AppleSMCSensorDispatcher31gpuPerfControllerArrivalHandlerEPvP9IOServiceP10IONotifier.cold.1
+ _ZN8AppleSMC5startEP9IOService.cold.16
+ _ZN8AppleSMC5startEP9IOService.cold.17
+ __ZL18AppleSMCKDebug_ktv
+ __ZN12OSDictionary11withObjectsEPPK8OSObjectPPK8OSStringjj
+ __ZN14AppleSMCClient27check_specific_entitlementsEjhbb
+ __ZN14AppleSMCKDebug10gMetaClassE
+ __ZN14AppleSMCKDebug10superClassE
+ __ZN14AppleSMCKDebug12processEntryEN7libkern11bounded_ptrIK10_log_entryN9os_detail21panic_trapping_policyEEEP13logSourceInfo
+ __ZN14AppleSMCKDebug7logTypeEv
+ __ZN14AppleSMCKDebug9MetaClassC1Ev
+ __ZN14AppleSMCKDebug9MetaClassC2Ev
+ __ZN14AppleSMCKDebug9MetaClassD0Ev
+ __ZN14AppleSMCKDebug9MetaClassD1Ev
+ __ZN14AppleSMCKDebug9metaClassE
+ __ZN14AppleSMCKDebug9setCoreIdEj
+ __ZN14AppleSMCKDebugC1EPK11OSMetaClass
+ __ZN14AppleSMCKDebugC1Ev
+ __ZN14AppleSMCKDebugC2EPK11OSMetaClass
+ __ZN14AppleSMCKDebugC2Ev
+ __ZN14AppleSMCKDebugD0Ev
+ __ZN14AppleSMCKDebugD1Ev
+ __ZN14AppleSMCKDebugD2Ev
+ __ZN14AppleSMCKDebugdlEPvm
+ __ZN14AppleSMCKDebugnwEm
+ __ZN8AppleSMC19_sysCaNotifyHandlerEhhh
+ __ZN9IOService22CoreAnalyticsSendEventEyP8OSStringP12OSDictionaryPFiP15OSMetaClassBase5IORPCE
+ __ZNK14AppleSMCKDebug12getMetaClassEv
+ __ZNK14AppleSMCKDebug9MetaClass5allocEv
+ __ZTV14AppleSMCKDebug
+ __ZTVN14AppleSMCKDebug9MetaClassE
+ _kernel_debug_enter
+ _proc_selfname
+ _proc_selfpid
- _ZN17AppleSMCChargerPS23handlePowerSourceDetectEPK30IOAccessoryPowerSourceBehavior.cold.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbedded.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
+ "1211111212221212111111111111121222"
+ "1211111212221212111212111111111121111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
+ "1211111212221212111212111111111121111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222111222"
+ "21:15:03"
+ "21:15:04"
+ "AppleSMCKDebug"
+ "CoreAnalytics: Failed to send CA event %s\n"
+ "CoreAnalytics: error - unknown subtype %u\n"
+ "CoreAnalytics: event %s = %u, %s = %u\n"
+ "Created eventbuffer log handler"
+ "Error: Invalid KDebug Msg size: %d. Expected: %ld\n"
+ "KDebugCoreID"
+ "Mar 19 2025"
+ "NULL != _smcKDebugLogHandler"
+ "RTKitOS"
+ "SMCC::initWithTask ERROR: SUPER::initWithTask failed for client (%s:%d)\n"
+ "SMCC::initWithTask client (%s:%d) fUCHasEntitlement = %d\n"
+ "SMCC::initWithTask client (%s:%d) fUCHasPrivilege = %d\n"
+ "SMCC::initWithTask found %d specifcally entitled keys for client (%s:%d)\n"
+ "SMCC::smcYPCEventCheck ERROR: accessing key bigger than %u using SMCParamStruct (not SMCLargeParamStruct). (key %s data size %u client %s:%d)\n"
+ "SMCC::smcYPCEventCheck ERROR: client (%s:%d) not authenticated as root (key %s)\n"
+ "SMCC::smcYPCEventCheck ERROR: client (%s:%d) not entitled for key %s\n"
+ "SMCC::smcYPCEventCheck ERROR: client (%s:%d) not entitled to read/write key '%s'\n"
+ "SMCC::smcYPCEventCheck ERROR: client (%s:%d) not specifically entitled to read key '%s'\n"
+ "SMCC::smcYPCEventCheck ERROR: client (%s:%d) not specifically entitled to write key '%s'\n"
+ "SMCC::smcYPCEventCheck ERROR: data size mis-match: %u > %u key %s (client: %s:%d)\n"
+ "SMCC::smcYPCEventCheck ERROR: invalid input structure size:%d key %s (client: %s:%d)\n"
+ "SMCC::smcYPCEventCheck ERROR: output struct sz (%lu) != input struct sz (%u)\n key %s (client: %s:%d)"
+ "SMCC::smcYPCEventCheck client (%s:%d) entitled to read/write '%s'\n"
+ "SMCC::smcYPCEventCheck: changing attribute of key %s because client (%s:%d) not specifically entitled\n"
+ "com.apple.sensor_nv_ov_count"
+ "ov_count"
+ "rec_count"
+ "site.AppleSMCKDebug"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbedded.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
- "1211111212221212111111111111121"
- "121111121222121211121211111111112111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
- "121111121222121211121211111111112111222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222111222"
- "20:46:09"
- "20:46:11"
- "Jan  2 2025"
- "SMCC::initWithTask ERROR: SUPER::initWithTask failed\n"
- "SMCC::initWithTask fUCHasEntitlement = %d\n"
- "SMCC::initWithTask fUCHasPrivilege = %d\n"
- "SMCC::initWithTask found %d specifcally entitled keys\n"
- "SMCC::smcYPCEventCheck ERROR: accessing key bigger than %u using SMCParamStruct (not SMCLargeParamStruct). (key %s data size %u)\n"
- "SMCC::smcYPCEventCheck ERROR: client not entitled to read/write key '%s'\n"
- "SMCC::smcYPCEventCheck ERROR: client not specifically entitled to read key '%s'\n"
- "SMCC::smcYPCEventCheck ERROR: client not specifically entitled to write key '%s'\n"
- "SMCC::smcYPCEventCheck ERROR: data size mis-match: %u > %u key %s\n"
- "SMCC::smcYPCEventCheck ERROR: invalid input structure size:%d key %s\n"
- "SMCC::smcYPCEventCheck ERROR: not authenticated as root (key %s)\n"
- "SMCC::smcYPCEventCheck ERROR: not entitled for key %s\n"
- "SMCC::smcYPCEventCheck ERROR: output struct sz (%lu) != input struct sz (%u)\n key %s"
- "SMCC::smcYPCEventCheck client entitled to read/write '%s'\n"
- "SMCC::smcYPCEventCheck: changing attribute of key %s because client not specifically entitled\n"

```
