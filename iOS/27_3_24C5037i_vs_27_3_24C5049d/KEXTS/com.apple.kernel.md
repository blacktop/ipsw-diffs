## com.apple.kernel

> `com.apple.kernel`

```diff

-13432.60.57.0.0
-  __TEXT.__const: 0x37970
+13432.60.70.502.1
+  __TEXT.__const: 0x37ac0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x91ee2
-  __TEXT.__os_log: 0x429ac
+  __TEXT.__cstring: 0x921e5
+  __TEXT.__os_log: 0x42a63
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x122108
-  __DATA_CONST.__kalloc_type: 0x15640
-  __DATA_CONST.__assert: 0x1644
+  __DATA_CONST.__const: 0x122080
+  __DATA_CONST.__kalloc_type: 0x15580
+  __DATA_CONST.__assert: 0x170c
   __DATA_CONST.__kalloc_var: 0x8020
   __DATA_CONST.__exclaves_bt: 0xc0
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x4c000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x913fac
+  __TEXT_EXEC.__text: 0x916b0c
   __TEXT_EXEC.__hib_text: 0x10d8
   __TEXT_BOOT_EXEC.__bootcode: 0x6a2c
   __KLD.__text: 0x173c

   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3f90
+  __KLDDATA.__const: 0x3fc8
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x182e9
+  __DATA.__data: 0x183a9
   __DATA.__lock_grp: 0x5ee0
   __DATA.__percpu: 0x7be0
-  __DATA.__common: 0x7bcf8
+  __DATA.__common: 0x7bd38
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0xdd0
-  __BOOTDATA.__init_entry_set: 0x15390
-  __BOOTDATA.__init: 0x17a90
+  __BOOTDATA.__init_entry_set: 0x154c8
+  __BOOTDATA.__init: 0x17ac0
   __BOOTDATA.__static_ifinit: 0x18
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48f5f
-  Functions: 22098
+  Functions: 22112
   Symbols:   0
-  CStrings:  21599
+  CStrings:  21619
 
CStrings:
+ "<unavailable>"
+ "Attempted fault on a copy of a file beyond snapshotted file size\n"
+ "Attempted fault on a copy of a file beyond snapshotted file size via vm_fault_page\n"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}][14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCCACQQQiBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6c[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}^v^vIQCAB{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}AQ}8"
+ "Invalid vmo_snapshot_policy value: %u @%s:%d"
+ "SK[%u]: %-30s fsw %p FREE (unconstructed)\n"
+ "SK[%u]: %-30s nexus %p advisory region \"%s\" alloc failed\n"
+ "bootinfo.scid <= UINT16_MAX"
+ "c->scid <= UINT16_MAX"
+ "com.apple.developer.networking.ipoptions.restricted-access"
+ "ctx"
+ "ctx->scid == scid"
+ "exclaves: Scheduler: Unexpected thread terminate: scid 0x%hx terminated scid 0x%hx\n @%s:%d"
+ "exclaves: panic thread init: failed to find stackshot service @%s:%d"
+ "exclaves: xnu proxy endpoint call failed:\tendpoint id %ld scid 0x%hx status %u\n @%s:%d"
+ "exclaves_ctx.c"
+ "exclaves_memory_pa_page_is_sk_shared_rw( trunc_page_64(ipcb_paddr))"
+ "file copy snapshot statistics"
+ "file copy snapshot violations"
+ "file copy snapshot violations from kernel"
+ "fsw_free_unconstructed"
+ "ipcb"
+ "kernel_violations"
+ "nx_advisory_alloc"
+ "phystokv_reason: illegal phys->kv translation of pa=0x%llx (reasons=0x%b) @%s:%d"
+ "phystokv_reason: invalid reasons 0x%x (pa=0x%llx) @%s:%d"
+ "phystokv_reason_enforce"
+ "pti != NULL && pti->pt_tty == tp"
+ "snapshot"
+ "subtable"
+ "subtable[lo] == NULL"
+ "trunc_page_64(ipcb_paddr) == trunc_page_64( ipcb_paddr + sizeof(Exclaves_L4_IpcBuffer_t) - 1)"
+ "violations"
+ "vnode_link_lock_suspended"
- "21212"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}][14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCCACQQQiBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6c[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}^v^vIQC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}AQ}8"
- "exclaves: Scheduler: Unexpected thread terminate: scid 0x%lx terminated scid 0x%llx\n @%s:%d"
- "exclaves: unexpected exclaves_run return value %d @%s:%d"
- "exclaves: xnu proxy endpoint call failed:\tendpoint id %ld scid 0x%lx status %u\n @%s:%d"
- "exclaves_memory_pa_page_is_sk_shared_rw(trunc_page_64(ipcb_paddr))"
- "object_no_shadowing_extra_refs"
- "object_pageout_clean_but_shadowing"
- "object_pageout_clean_no_shadowing"
- "pageout_clean_but_shadowing"
- "pageout_clean_no_shadowing"
- "site.struct exclaves_ctx"
- "terminated->threadHostId == ctid"
- "trunc_page_64(ipcb_paddr) == trunc_page_64(ipcb_paddr + sizeof(Exclaves_L4_IpcBuffer_t) - 1)"
```
