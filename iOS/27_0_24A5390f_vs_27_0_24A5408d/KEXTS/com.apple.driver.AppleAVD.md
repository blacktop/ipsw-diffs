## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

-991.0.0.0.0
-  __TEXT.__os_log: 0x1b1cb
-  __TEXT.__cstring: 0x7d1b
+993.1.0.0.0
+  __TEXT.__os_log: 0x1b321
+  __TEXT.__cstring: 0x7cfe
   __TEXT.__const: 0xcc129
-  __TEXT_EXEC.__text: 0x5ff10
+  __TEXT_EXEC.__text: 0x5fe18
   __TEXT_EXEC.__auth_stubs: 0x6f0
   __DATA.__data: 0x1334
   __DATA.__common: 0x78

   __DATA_CONST.__auth_ptr: 0x10
   Functions: 2162
   Symbols:   0
-  CStrings:  1771
+  CStrings:  1772
 
Functions:
~ __ZN25AppleAVDFrameParamManager15wakeIfAvailableEv : 168 -> 112
~ __ZN25AppleAVDFrameParamManager15resetFrameQslotEii : 232 -> 332
~ __ZN25AppleAVDFrameParamManager20checkForAvailabilityEj : 228 -> 252
~ __ZN17AppleAVDScheduler9addWaiterEj : 188 -> 192
~ __ZN17AppleAVDScheduler12removeWaiterEj : 220 -> 232
~ __ZN17AppleAVDScheduler24getHighestPriorityWaiterEv : 84 -> 124
~ __os_log_internal : 13980 -> 13320
~ __ZN8AppleAVD4initEP12OSDictionary : 916 -> 944
~ __ZN8AppleAVD12powerCoreOffEj24eAppleAvdIOPMPowerStates -> sub_fffffe00086b6740 : 532 -> 460
~ __ZN13PriorityQueueC2EPvP14CAvdRegisterIO : 408 -> 400
~ __ZN22AppleAVDCommandPatcher9mapMemoryEjy11eAvdMemType11eAvdMapTypebbbyyhP20_avd_client_mem_info : 1044 -> 1308
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
