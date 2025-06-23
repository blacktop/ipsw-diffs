## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.0.81.0.3
-  __TEXT.__const: 0x34b80
+12377.0.122.0.1
+  __TEXT.__const: 0x34ba0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x7c985
-  __TEXT.__os_log: 0x3bf27
+  __TEXT.__cstring: 0x7d1e2
+  __TEXT.__os_log: 0x3bf1f
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0xac8d0
+  __DATA_CONST.__const: 0xaca48
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x13fc0
+  __DATA_CONST.__kalloc_type: 0x13f80
   __DATA_CONST.__assert: 0x5dc
-  __DATA_CONST.__kalloc_var: 0x7e90
+  __DATA_CONST.__kalloc_var: 0x7a80
   __DATA_CONST.__exclaves_bt: 0x78
-  __DATA_CONST.__brk_desc: 0x78
+  __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x88e1fc
+  __TEXT_EXEC.__text: 0x88ff30
   __TEXT_EXEC.__hib_text: 0xe38
   __TEXT_BOOT_EXEC.__bootcode: 0x5218
   __KLD.__text: 0x1818

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x2fe0
+  __KLDDATA.__const: 0x3098
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17da9
+  __DATA.__data: 0x17de9
   __DATA.__lock_grp: 0x5b70
   __DATA.__percpu: 0x6e88
   __DATA.__common: 0x5c100
   __DATA.__bss: 0x96cc8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4ce0
-  __BOOTDATA.__init_entry_set: 0x11718
-  __BOOTDATA.__init: 0x5b298
+  __BOOTDATA.__static_if: 0x4d10
+  __BOOTDATA.__init_entry_set: 0x11778
+  __BOOTDATA.__init: 0x5b288
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_DATA_CONST.__data: 0x0
   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
-  __LINKINFO.__symbolsets: 0x46f56
-  UUID: 7E655DA4-2A5A-37C2-8DD7-2EE4A53BEB4D
-  Functions: 20591
+  __LINKINFO.__symbolsets: 0x46f97
+  UUID: A9EF4BD6-3A69-3F2A-9698-FFBD6F7B195C
+  Functions: 20601
   Symbols:   0
-  CStrings:  19821
+  CStrings:  19902
 
CStrings:
+ "%%%02x"
+ "%lu.%03d memorystatus: killing_specific_process pid %d [%s] (%s %d %llus rf:%s type:%s) %lluKB - memorystatus_available_pages: %llu\n"
+ "%lu.%03d memorystatus: killing_top_process_elevated%d pid %d [%s] (%s %d %llus rf:%s type:%s) %lluKB - memorystatus_available_pages: %llu\n"
+ "%s as data with size %zu"
+ "%s(0x%qx): stop matching as %s will be relaunched\n"
+ "%s: DATA-TRACE: Socket Policy <so %llx>: (Application %d Real Application %d BoundInterface %d Proto %d) Remove NetagentType %d\n"
+ "%s: initializing the SURT subsystem while it has already been initialized @%s:%d"
+ "%s: process %s[%d] hit an unrecoverable exception\n"
+ "%s:%s:%u - %s: "
+ "112212121222221222222"
+ "11222222121222122222222222222222222222222112222"
+ "2221211122112211221110222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111112121111222221112221222222222222221122222112"
+ "22222222211111"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}][14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b16}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b28}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ{task_security_config=(?={?=b1b1b1b3C}S)}}8"
+ "Failed to find a free agent UUID ID.\n"
+ "Failed to find a free agent type ID.\n"
+ "Failed to find a free app UUID ID.\n"
+ "REMOVE_NETAGENT_TYPE"
+ "RemoveNetAgentType (%s/%s)"
+ "SURT system readiness"
+ "VM_KERN_COUNT_BOOT_STOLEN"
+ "VM_KERN_COUNT_EXCLAVES_CARVEOUT"
+ "VM_KERN_COUNT_LOPAGE"
+ "VM_KERN_COUNT_MANAGED"
+ "VM_KERN_COUNT_MAP_KALLOC_LARGE"
+ "VM_KERN_COUNT_MAP_KALLOC_LARGE_DATA"
+ "VM_KERN_COUNT_MAP_KERNEL"
+ "VM_KERN_COUNT_MAP_KERNEL_DATA"
+ "VM_KERN_COUNT_MAP_ZONE"
+ "VM_KERN_COUNT_RESERVED"
+ "VM_KERN_COUNT_STOLEN"
+ "VM_KERN_COUNT_WIRED"
+ "VM_KERN_COUNT_WIRED_BOOT"
+ "VM_KERN_COUNT_WIRED_MANAGED"
+ "VM_KERN_COUNT_WIRED_STATIC_KERNELCACHE"
+ "VM_KERN_MEMORY_34"
+ "VM_KERN_MEMORY_BSD"
+ "VM_KERN_MEMORY_COMPRESSED_DATA"
+ "VM_KERN_MEMORY_COMPRESSOR"
+ "VM_KERN_MEMORY_CPU"
+ "VM_KERN_MEMORY_DIAG"
+ "VM_KERN_MEMORY_EXCLAVES"
+ "VM_KERN_MEMORY_EXCLAVES_SHARED"
+ "VM_KERN_MEMORY_FILE"
+ "VM_KERN_MEMORY_HV"
+ "VM_KERN_MEMORY_IOKIT"
+ "VM_KERN_MEMORY_IPC"
+ "VM_KERN_MEMORY_KALLOC"
+ "VM_KERN_MEMORY_KALLOC_DATA"
+ "VM_KERN_MEMORY_KALLOC_SHARED"
+ "VM_KERN_MEMORY_KALLOC_TYPE"
+ "VM_KERN_MEMORY_KEXT"
+ "VM_KERN_MEMORY_LIBKERN"
+ "VM_KERN_MEMORY_LOG"
+ "VM_KERN_MEMORY_LTABLE"
+ "VM_KERN_MEMORY_MBUF"
+ "VM_KERN_MEMORY_MLOCK"
+ "VM_KERN_MEMORY_NONE"
+ "VM_KERN_MEMORY_OSFMK"
+ "VM_KERN_MEMORY_OSKEXT"
+ "VM_KERN_MEMORY_PHANTOM_CACHE"
+ "VM_KERN_MEMORY_PMAP"
+ "VM_KERN_MEMORY_PTE"
+ "VM_KERN_MEMORY_REASON"
+ "VM_KERN_MEMORY_RECOUNT"
+ "VM_KERN_MEMORY_RETIRED"
+ "VM_KERN_MEMORY_SECURITY"
+ "VM_KERN_MEMORY_SKYWALK"
+ "VM_KERN_MEMORY_STACK"
+ "VM_KERN_MEMORY_TRIAGE"
+ "VM_KERN_MEMORY_UBC"
+ "VM_KERN_MEMORY_WAITQ"
+ "VM_KERN_MEMORY_ZONE"
+ "_memstat_proc_is_reapable: %s [%d] is reapable; priority=%d, age=%d, relaunch_probability_acceptable_mask=0x%02X, type=%s\n"
+ "_memstat_proc_is_reapable: %s [%d] not reapable because it is an application and age (%llu) is below min age for apps (%d)\n"
+ "app"
+ "com.apple.security.hardened-process"
+ "com.apple.security.hardened-process.dyld-ro"
+ "com.apple.security.hardened-process.enhanced-security-version"
+ "com.apple.security.hardened-process.hardened-heap"
+ "com.apple.security.hardened-process.platform-restrictions"
+ "daemon"
+ "dp != NULL"
+ "dumpData"
+ "extended_idle_timeout"
+ "flow_entry_rx_steering_rule_cleanup"
+ "fsw->fsw_rxstrc_cnt != 0"
+ "fsw_rxstrc_insert"
+ "fsw_rxstrc_remove_internal"
+ "interface probing on %s set to %u by %s:%d"
+ "maybe_unrecoverable_exception_triage"
+ "memorystatus: %s pid %d [%s] (%s %d %llus rf:%s type:%s) %lluKB - memorystatus_available_pages: %llu compressor_size:%u\n"
+ "memorystatus: %s%d pid %d [%s] (%s %d %llus rf:%s type:%s) - memorystatus_available_pages: %llu\n"
+ "necp_get_new_agent_id"
+ "necp_get_new_app_uuid_id"
+ "not enough memory to allocate segment, disabling RACK"
+ "reaper_min_age_apps_secs"
+ "req != NULL"
+ "site.struct necp_agent_type_id_mapping"
+ "split_pagein_io"
+ "surt_init"
+ "surt_ready"
+ "tcp_keepalive (%s:%d) [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u snd_una: %u snd_max: %u SO_KA: %d RSTALL: %d TFOPRB: %d idle_time: %u rtimo_probes: %u adaptive_rtimo: %u KIDLE: %d KINTV: %d KCNT: %d"
+ "tcp_rack_free_and_disable"
+ "tcp_seg_rto_insert_end"
+ "tcp_seg_sent_insert"
+ "tcp_seg_sent_insert_before"
+ "v16@?0^{flow_entry={os_refcnt=AI}{flow_key=SCCSS{flow_ip_addr=(?={in_addr=I}{in6_addr=(?=[16C][8S][4I])}[16C][8S][4I][2Q])}{flow_ip_addr=(?={in_addr=I}{in6_addr=(?=[16C][8S][4I])}[16C][8S][4I][2Q])}[1Q]}II{cuckoo_node=^{cuckoo_node}}[16C]SIIICSI{?=[2Q]}{pktq=^{__kern_packet}^^{__kern_packet}I}{?=^{flow_entry}^^{flow_entry}}^?QIBI{pktq=^{__kern_packet}^^{__kern_packet}I}{?=^{flow_entry}^^{flow_entry}}^?[16C]IiII^{nx_flowswitch}^{ns_token}^{protons_token}^v{flow_track=IIISSCCSII{flow_track_rtt=QQIII}}{flow_track=IIISSCCSII{flow_track_rtt=QQIII}}^{flow_stats}^{flow_route}{?=^{flow_entry}^{flow_entry}^{flow_entry}}{?=^{flow_entry}^^{flow_entry}}QIii[24c][24c]I^{netif_qset}QiI{?=[2Q]}{flow_entry_list=^{flow_entry}^^{flow_entry}}{?=^{flow_entry}^^{flow_entry}}C^{kern_flow_demux_pattern}*{?=^{flow_entry}^^{flow_entry}}}8"
- "%lu.%03d memorystatus: killing_specific_process pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu\n"
- "%lu.%03d memorystatus: killing_top_process_elevated%d pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu\n"
- "%s as data with size %#x"
- "%s: WARNING: more than %d leaders in priority band [%d]\n"
- "%s: necp_session_register_service invalid input (%zu)\n"
- "%s: necp_session_register_service uuid copyin error (%d)\n"
- "%s: necp_session_unregister_service invalid input (%zu)\n"
- "%s: necp_session_unregister_service uuid copyin error (%d)\n"
- "11221212122222122222"
- "112222221212221222222222222222222222222221122222"
- "122111112"
- "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111212111122222111222122222222222222112220"
- "222222222111111"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}][14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQiBBB^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b16}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b28}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vCCCCIQ{queue_entry=^{queue_entry}^{queue_entry}}{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}^v^vIQ{task_security_config=(?={?=b1b1b1}C)}}8"
- "Failed to find a free service UUID.\n"
- "_memstat_proc_is_reapable: %s [%d] is reapable; priority=%d, age=%d, relaunch_probability_acceptable_mask=0x%02X\n"
- "com.apple.developer.hardened-process.platform-restrictions"
- "memorystatus: %s pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu compressor_size:%u\n"
- "memorystatus: %s%d pid %d [%s] (%s %d %llus rf:%s - memorystatus_available_pages: %llu\n"
- "memorystatus_sort_by_largest_coalition_locked"
- "necp_get_new_uuid_id"
- "necp_session_register_service"
- "necp_session_unregister_service"
- "site.struct necp_service_registration"
- "site.uint8_t"
- "tcp_keepalive (%s:%d) [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u snd_una: %u snd_max: %u SO_KA: %d RSTALL: %d TFOPRB: %d idle_time: %u KIDLE: %d KINTV: %d KCNT: %d"
- "v16@?0^{flow_entry={os_refcnt=AI}{flow_key=SCCSS{flow_ip_addr=(?={in_addr=I}{in6_addr=(?=[16C][8S][4I])}[16C][8S][4I][2Q])}{flow_ip_addr=(?={in_addr=I}{in6_addr=(?=[16C][8S][4I])}[16C][8S][4I][2Q])}[1Q]}II{cuckoo_node=^{cuckoo_node}}[16C]SIIICSI{?=[2Q]}{pktq=^{__kern_packet}^^{__kern_packet}I}{?=^{flow_entry}^^{flow_entry}}^?QIBI{pktq=^{__kern_packet}^^{__kern_packet}I}{?=^{flow_entry}^^{flow_entry}}^?[16C]IiII^{nx_flowswitch}^{ns_token}^{protons_token}^v{flow_track=IIISSCCSII{flow_track_rtt=QQIII}}{flow_track=IIISSCCSII{flow_track_rtt=QQIII}}^{flow_stats}^{flow_route}{?=^{flow_entry}^{flow_entry}^{flow_entry}}{?=^{flow_entry}^^{flow_entry}}QIii[24c][24c]I^{netif_qset}QiI{?=[2Q]}{flow_entry_list=^{flow_entry}^^{flow_entry}}{?=^{flow_entry}^^{flow_entry}}C^{kern_flow_demux_pattern}*}8"

```
