## dasd

> `/usr/libexec/dasd`

```diff

-2109.40.18.0.0
-  __TEXT.__text: 0x12a218
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_stubs: 0x17f40
-  __TEXT.__objc_methlist: 0x11540
+2109.42.2.0.0
+  __TEXT.__text: 0x12b5a4
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x17fe0
+  __TEXT.__objc_methlist: 0x11620
   __TEXT.__const: 0x938
-  __TEXT.__objc_methname: 0x2906b
-  __TEXT.__cstring: 0xe6b0
-  __TEXT.__oslogstring: 0x11898
-  __TEXT.__objc_classname: 0x1907
+  __TEXT.__objc_methname: 0x292a8
+  __TEXT.__cstring: 0xea0e
+  __TEXT.__oslogstring: 0x11a58
+  __TEXT.__objc_classname: 0x1909
   __TEXT.__objc_methtype: 0x3ad0
   __TEXT.__gcc_except_tab: 0x510c
   __TEXT.__dlopen_cstrs: 0x4e2
-  __TEXT.__unwind_info: 0x42b0
-  __DATA_CONST.__auth_got: 0x9c0
+  __TEXT.__unwind_info: 0x42d0
+  __DATA_CONST.__auth_got: 0x9d0
   __DATA_CONST.__got: 0xa90
   __DATA_CONST.__const: 0x3d20
-  __DATA_CONST.__cfstring: 0xf360
+  __DATA_CONST.__cfstring: 0xf760
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1c0

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x540
   __DATA_CONST.__objc_intobj: 0x13e0
-  __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA.__objc_const: 0x2f6f8
-  __DATA.__objc_selrefs: 0x8d70
-  __DATA.__objc_ivar: 0x1404
+  __DATA.__objc_const: 0x2f818
+  __DATA.__objc_selrefs: 0x8de8
+  __DATA.__objc_ivar: 0x141c
   __DATA.__objc_data: 0x3d40
   __DATA.__data: 0x1650
   __DATA.__bss: 0xc10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 5E9C053D-03E1-3382-895E-27479B8FE392
-  Functions: 7032
-  Symbols:   664
-  CStrings:  13059
+  UUID: 88F73B08-B336-3054-8098-BC75700E1CDE
+  Functions: 7058
+  Symbols:   666
+  CStrings:  13163
 
Symbols:
+ _host_statistics64
+ _mach_host_self
CStrings:
+ "9"
+ "ConfigState"
+ "Dock State %@"
+ "DockCount"
+ "DockFootprint"
+ "DockState"
+ "Error memorystatus_control : MEMORYSTATUS_CMD_GET_PRIORITY_LIST_V2"
+ "Error with allocation for memorystatus_priority_entry"
+ "Error with initializing ledger indices"
+ "Failed to call sysctl %@ with %d"
+ "Failed to register for test PPS donation notification: %u"
+ "FileBacked"
+ "Free"
+ "Freezer State %@"
+ "FreezerCount"
+ "FreezerFrozenSize"
+ "FreezerResidentSize"
+ "FreezerState"
+ "FreezerThawedCount"
+ "FreezerThawedResidentSize"
+ "Idle Band State %@"
+ "IdleBandState"
+ "IdleCount"
+ "IdleFootprint"
+ "Memory State %@"
+ "MemoryState"
+ "OSIMemory"
+ "Parameter"
+ "Successfully registered for test PPS donation notification"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_ppsDonationQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_ppsDonationTimer"
+ "TB,N,V_indicesInitialized"
+ "Ti,N,V_footprintIndex"
+ "Ti,N,V_frozenToSwapIndex"
+ "Value"
+ "_footprintIndex"
+ "_frozenToSwapIndex"
+ "_indicesInitialized"
+ "_ppsDonationQueue"
+ "_ppsDonationTimer"
+ "com.apple.aprs.testPPSDonation"
+ "com.apple.dasd.appresume.ppsDonation"
+ "footprint"
+ "footprintIndex"
+ "frozenSize"
+ "frozenToSwapIndex"
+ "getProcessMemoryInfoForPID:"
+ "get_vm_stats: host_statistics64 failed to get vm stats\n"
+ "indicesInitialized"
+ "kern.memorystatus_freeze_budget_multiplier"
+ "kern.memorystatus_freeze_budget_pages_remaining"
+ "kern.memorystatus_freeze_max_candidate_band"
+ "kern.memorystatus_freeze_min_processes"
+ "kern.memorystatus_freezer_use_demotion_list"
+ "kern.memorystatus_freezer_use_ordered_list"
+ "kern.memorystatus_min_thaw_refreeze_threshold"
+ "kern.trial.memorystatus_freeze_last_processes_thawed_cache_size"
+ "kern.trial.memorystatus_freeze_last_processes_thawed_prevent_refreeze_seconds"
+ "kern.trial.memorystatus_freeze_prevent_refreeze_of_recently_thawed"
+ "metricRecorder"
+ "ppsDonationQueue"
+ "ppsDonationTimer"
+ "recordConfigState"
+ "recordMemoryMetrics"
+ "registerForPPSDonation"
+ "residentSize"
+ "schedulePPSTimer"
+ "setFootprintIndex:"
+ "setFrozenToSwapIndex:"
+ "setIndicesInitialized:"
+ "setPpsDonationQueue:"
+ "setPpsDonationTimer:"
+ "sysctl %@ : %ld"
- "appResume.caEvent"

```
