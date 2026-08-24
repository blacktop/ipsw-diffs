## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

-991.0.0.0.0
-  __TEXT.__os_log: 0x18350
-  __TEXT.__cstring: 0x6741
+993.1.0.0.0
+  __TEXT.__os_log: 0x184a6
+  __TEXT.__cstring: 0x6724
   __TEXT.__const: 0x9df99
-  __TEXT_EXEC.__text: 0x538f0
+  __TEXT_EXEC.__text: 0x539e4
   __TEXT_EXEC.__auth_stubs: 0x710
   __DATA.__data: 0x1334
   __DATA.__common: 0x78

   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x10
   Functions: 1720
-  Symbols:   3906
-  CStrings:  1728
+  Symbols:   3909
+  CStrings:  1729
 
Symbols:
+ __ZN17AppleAVDScheduler18scheduleNextWaiterEv
+ __ZZ14AllocKernelMemPvmiS_E21kalloc_type_view_4563
+ __ZZ14AllocKernelMemPvmiS_E21kalloc_type_view_4576
+ __ZZN17AppleAVDScheduler12removeWaiterEjE20kalloc_type_view_108
+ __ZZN17AppleAVDSchedulerdlEPvmE19kalloc_type_view_35
+ __ZZN17AppleAVDSchedulernwEmE19kalloc_type_view_35
+ __ZZN22AppleAVDCommandPatcher11unmapMemoryEP20_avd_client_mem_infobE11_os_log_fmt_5
+ __ZZN22AppleAVDCommandPatcher11unmapMemoryEP20_avd_client_mem_infobE20kalloc_type_view_396
+ __ZZN22AppleAVDCommandPatcher25addSharedMemToMappingListEP20_avd_client_mem_infoE21kalloc_type_view_1057
+ __ZZN22AppleAVDCommandPatcher30removeSharedMemFromMappingListEP20_avd_client_mem_infoE21kalloc_type_view_1134
+ __ZZN22AppleAVDCommandPatcher8unmapAllEvE21kalloc_type_view_1013
+ __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE11_os_log_fmt_6
+ __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE11_os_log_fmt_7
+ __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE20kalloc_type_view_238
+ __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE20kalloc_type_view_265
+ __ZZN22AppleAVDCommandPatcherdlEPvmE19kalloc_type_view_32
+ __ZZN22AppleAVDCommandPatchernwEmE19kalloc_type_view_32
+ __ZZN25AppleAVDFrameParamManager15resetFrameQslotEiiE11_os_log_fmt_0
+ __ZZN25AppleAVDFrameParamManager15resetFrameQslotEiiE11_os_log_fmt_1
+ __ZZN8AppleAVD13avdOutbox0ISREjE21kalloc_type_view_5932
+ __ZZN8AppleAVD14AllocKernelMemEmiPvjE21kalloc_type_view_4604
+ __ZZN8AppleAVD14AllocKernelMemEmiPvjE21kalloc_type_view_4619
+ __ZZN8AppleAVD16DeallocKernelMemEPvjE21kalloc_type_view_4636
+ __ZZN8AppleAVD4freeEvE20kalloc_type_view_571
+ __ZZN8AppleAVD4stopEP9IOServiceE20kalloc_type_view_504
+ __ZZN8AppleAVD9HardResetEii28eAppleAVDHardResetSourceTypeE21kalloc_type_view_1181
+ __ZZN8AppleAVD9HardResetEii28eAppleAVDHardResetSourceTypeE21kalloc_type_view_1432
- __ZN17AppleAVDScheduler24getHighestPriorityWaiterEv
- __ZZ14AllocKernelMemPvmiS_E21kalloc_type_view_4469
- __ZZ14AllocKernelMemPvmiS_E21kalloc_type_view_4482
- __ZZN17AppleAVDScheduler12removeWaiterEjE20kalloc_type_view_106
- __ZZN17AppleAVDSchedulerdlEPvmE19kalloc_type_view_34
- __ZZN17AppleAVDSchedulernwEmE19kalloc_type_view_34
- __ZZN22AppleAVDCommandPatcher11unmapMemoryEP20_avd_client_mem_infobE20kalloc_type_view_347
- __ZZN22AppleAVDCommandPatcher25addSharedMemToMappingListEP20_avd_client_mem_infoE21kalloc_type_view_1008
- __ZZN22AppleAVDCommandPatcher30removeSharedMemFromMappingListEP20_avd_client_mem_infoE21kalloc_type_view_1084
- __ZZN22AppleAVDCommandPatcher8unmapAllEvE20kalloc_type_view_964
- __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE20kalloc_type_view_198
- __ZZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_infoE20kalloc_type_view_224
- __ZZN22AppleAVDCommandPatcherdlEPvmE19kalloc_type_view_31
- __ZZN22AppleAVDCommandPatchernwEmE19kalloc_type_view_31
- __ZZN25AppleAVDFrameParamManager15wakeIfAvailableEvE11_os_log_fmt
- __ZZN8AppleAVD12powerCoreOffEj24eAppleAvdIOPMPowerStatesE11_os_log_fmt
- __ZZN8AppleAVD13avdOutbox0ISREjE21kalloc_type_view_5838
- __ZZN8AppleAVD14AllocKernelMemEmiPvjE21kalloc_type_view_4510
- __ZZN8AppleAVD14AllocKernelMemEmiPvjE21kalloc_type_view_4525
- __ZZN8AppleAVD16DeallocKernelMemEPvjE21kalloc_type_view_4542
- __ZZN8AppleAVD4freeEvE20kalloc_type_view_556
- __ZZN8AppleAVD4stopEP9IOServiceE20kalloc_type_view_489
- __ZZN8AppleAVD9HardResetEii28eAppleAVDHardResetSourceTypeE21kalloc_type_view_1105
- __ZZN8AppleAVD9HardResetEii28eAppleAVDHardResetSourceTypeE21kalloc_type_view_1356
Functions:
~ __ZN25AppleAVDFrameParamManager15wakeIfAvailableEv : 168 -> 112
~ __ZN25AppleAVDFrameParamManager15resetFrameQslotEii : 232 -> 332
~ __ZN25AppleAVDFrameParamManager20checkForAvailabilityEj : 228 -> 252
~ __ZN17AppleAVDScheduler9addWaiterEj : 188 -> 192
~ __ZN17AppleAVDScheduler12removeWaiterEj : 220 -> 232
~ __ZN17AppleAVDScheduler24getHighestPriorityWaiterEv -> __ZN17AppleAVDScheduler18scheduleNextWaiterEv : 84 -> 124
~ __ZN8AppleAVD5startEP9IOService : 13948 -> 13768
~ __ZN8AppleAVD4initEP12OSDictionary : 876 -> 912
~ __ZN8AppleAVD12powerCoreOffEj24eAppleAvdIOPMPowerStates : 640 -> 568
~ __ZN13PriorityQueueC2EPvP14CAvdRegisterIO : 424 -> 416
~ __ZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_info : 1044 -> 1312
~ __ZN22AppleAVDCommandPatcher11unmapMemoryEP20_avd_client_mem_infob : 828 -> 900
~ __ZN22AppleAVDCommandPatcher25addSharedMemToMappingListEP20_avd_client_mem_info : 236 -> 240
CStrings:
+ "AppleAVD: ERROR: %s(): invalid bufIdx %d\n"
+ "AppleAVD: ERROR: %s(): map request (mapType=%d, memType=%d) does not match existing mapping (mapType=%d, memType=%d) for IOSID %d\n\n"
+ "AppleAVD: ERROR: %s(): map_ref_count overflow for IOSID %d, refusing remap\n\n"
+ "AppleAVD: INFO: %s(): existing mapping (IOSID %d) found, reusing it (map_ref_count=%u)\n\n"
+ "AppleAVD: INFO: %s(): mapping still referenced, deferring unmap (map_ref_count=%u), IOSID=%u\n\n"
+ "AppleAVD: WARNING: %s(): bufIdx %d already AVAILABLE, skipping reset to avoid in-flight underflow\n"
- "AppleAVD: ERROR: %s(): Scheduler returned invalid clientID=%u as highest priority\n"
- "AppleAVD: INFO: %s(): Dbg keep power on\n"
- "AppleAVD: INFO: %s(): existing mapping (IOSID %d) found, remap it\n\n"
- "powerCoreOff"
- "wakeIfAvailable"
```
