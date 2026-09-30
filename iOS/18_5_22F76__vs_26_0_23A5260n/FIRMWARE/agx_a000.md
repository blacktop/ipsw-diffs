## agx_a000

> `agx_a000`

```diff

 
-  __TEXT.__text: 0x34dc4
-  __TEXT.__gxf_shr_code: 0x55c
-  __TEXT.__gxf_code: 0x1270
+  __TEXT.__text: 0x37420
+  __TEXT.__gxf_code: 0x5098
   __TEXT.__gxf_code_pad: 0x0
-  __TEXT.__const: 0x1b40
-  __TEXT._rtk_patchbay: 0x228
+  __TEXT.__gxf_shr_code: 0x55c
+  __TEXT.__const: 0x1bf4
+  __TEXT.__cstring: 0x20eb
+  __TEXT._rtk_patchbay: 0x231
   __TEXT._rtk_tunables: 0x6a0
+  __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x230e
-  __DATA.__gxf_data: 0x4200
-  __DATA.__data: 0x14a28
-  __DATA.__const: 0x5d0
+  __DATA.__gxf_data: 0x80b8
+  __DATA.__data: 0x16b38
+  __DATA.__mod_init_func: 0x8
+  __DATA.__const: 0x580
   __DATA._rtk_init_stack: 0x4000
   __DATA._rtk_irq_stack: 0x4000
   __DATA._rtk_exc_stack: 0x4000
   __DATA._rtk_boot_l1: 0x200
   __DATA._rtk_boot: 0xc000
+  __DATA._rtk_mtab: 0x390
   __DATA._rtk_power: 0x3a8
   __DATA._rtk_page_tables: 0x20000
+  __DATA.__xnu_shared: 0x3c000
   __DATA._rtk_data_uuid: 0x0
-  __DATA._rtk_threads: 0x0
-  __DATA.__mod_init_func: 0x8
   __DATA._rtk_heap: 0x0
+  __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__xnu_shared: 0x3c000
-  __DATA._rtk_mtab: 0x390
-  __DATA.__zerofill: 0x58058
-  UUID: 922F3AE6-D26D-3F60-B30C-6D607A4279AC
-  Functions: 417
-  Symbols:   230
-  CStrings:  236
+  __DATA.__zerofill: 0x59818
+  UUID: 5BAF43EA-881A-3EAC-90FC-96CDA8367452
+  Functions: 411
+  Symbols:   191
+  CStrings:  220
 
Symbols:
+ __rtk_gxf_entry
+ __rtk_gxf_initialized
+ __rtk_mmu_gxf_config_swift
+ __rtk_patch_RTK_lock_legacy
- _AGFHALCommandBufferTimestampEnd
- _RTK_dev_syslog_mbi
- _RTK_platform_ack_local_power_state
- _RTK_platform_ack_remote_power_state
- _RTK_platform_hibernate
- _RTK_platform_resume
- _RTK_platform_set_minimum_power_state
- _RTK_vm_memory_map
- __gxf_cache_info
- __gxf_err_info
- __mmu_gxf_enter
- __mmu_gxf_enter_client
- __rtk_arch_unhandled_exception
- __rtk_mc_mappings
- __rtk_mc_num_mappings
- __rtk_mmu_clean_whole_dcache
- __rtk_mmu_disable_shared_region
- __rtk_mmu_gxf_dispatcher
- __rtk_mmu_gxf_dispatcher_entry
- __rtk_mmu_set_shared_region
- __rtk_mmu_switch_region_base_by_contextID
- __rtk_mmu_uat_flush_request
- __rtk_mmu_uat_idle
- __rtk_mmu_uat_wake
- __rtk_tracekit_thread_init
- __rtk_tracekit_transition_context
- __rtk_uppl_client_dispatcher
- _agfHALPerfCtrSourceChipFree
- _agfHALPerfCtrSourceChipSetup
- _agfHALPerfCtrSourceSamplerCleanup
- _agfHALPerfCtrSourceSamplerDutyCycle
- _agfHALPerfCtrSourceSamplerEnableHW
- _agfHALPerfCtrSourceSamplerFlush
- _agfHALPerfCtrSourceSamplerPowerOff
- _agfHALPerfCtrSourceSamplerRDESetupTrigger
- _agfHALPerfCtrSourceSamplerRecovery
- _agfHALPerfCtrSourceSamplerSetup
- _agfHALPerfCtrSourceSamplerStop
- _agfHALPerfCtrSourceSetup
- _agfHALPerfCtrSourceSetupPerflets
- _dekkerlock_lock
- _dekkerlock_unlock
- _rtk_local_boot_config
CStrings:
+ "%s: !!! Fatal Error: Unsupported command type ExternalCSRequest"
+ "AGFKSMCompletionEntryAreParentsReceived"
+ "Context Store Timed Out! DM %u, QueueId %u"
+ "May 30 2025 18:50:29"
+ "kAGFIPIORegionTypeAFRDCPMS"
+ "kAGFIPIORegionTypeFenderRegsKSMFE"
+ "kAGFIPIORegionTypePmgrMiscDie0"
+ "kAGFIPIORegionTypePmgrMiscDie1"
- "!ASLRHeapAlign"
- "!context: %u r=0x%llx v=%x g=%llx"
- "%s: !!! Fatal Error: %s : power %s : Queues have pending kill."
- "%s: !!! Fatal Error: Failed to allocate OOM state index"
- "AGFKSMAreParentsReceived"
- "Apr 22 2025 20:22:57"
- "GXF !op=%x raw=%p"
- "GXF !update_map: v=%#lx, sz=%zu, at=%#x st=%#x"
- "GXF bad error: e=%x"
- "GXF bad range: v=%#lx, p=%#lx, sz=%zu, attr=%#x"
- "GXF double init"
- "PPL handoff !magic: 0x%016llx != 0x%016llx"
- "UAT bad flush: %d %x"
- "agfAllocateOomState"
- "agfaKBValidateStatePowerEvent"
- "kAGFIPIORegionTypeDisplayURMagic"
- "kAGFIPIORegionTypeFenderRegsLegacyDPECfg"
- "kAGFIPIORegionTypeFenderRegsLegacyFenderCfg"
- "kAGFIPIORegionTypeFenderRegsLegacyGFXCfg"
- "kAGFIPIORegionTypeMCacheG11Plane0Registers"
- "kAGFIPIORegionTypeMCacheG11Plane1Registers"
- "kAGFIPIORegionTypeMCacheG11Plane2Registers"
- "kAGFIPIORegionTypeMCacheG11Plane3Registers"
- "kAGFIPIORegionTypeUTRegisters"

```
