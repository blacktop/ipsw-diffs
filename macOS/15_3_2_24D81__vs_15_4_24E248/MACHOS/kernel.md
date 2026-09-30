## kernel

> `/System/Library/Kernels/kernel`

```diff

-11215.81.4.0.0
-  __TEXT.__text: 0x861900
-  __TEXT.__const: 0x42414
-  __TEXT.__cstring: 0x933e0
-  __TEXT.__os_log: 0x300ab
+11417.101.15.0.0
+  __TEXT.__text: 0x86ba90
+  __TEXT.__const: 0x42774
+  __TEXT.__cstring: 0x95f3a
+  __TEXT.__os_log: 0x3150b
   __TEXT.__eh_frame: 0x118
   __DATA.__llvm_prf_cnts: 0x0
   __DATA.__llvm_prf_data: 0x0
   __DATA.__lock_grp: 0x16058
-  __DATA.__data: 0x71750
-  __DATA.__percpu: 0x2ef8
+  __DATA.__data: 0x71b50
+  __DATA.__percpu: 0x3888
+  __DATA.__llvm_prf_bits: 0x0
   __DATA.__llvm_prf_names: 0x0
   __DATA.__llvm_prf_vnds: 0x0
+  __DATA.__llvm_prf_vns: 0x0
+  __DATA.__llvm_prf_vtab: 0x0
   __DATA.__llvm_orderfile: 0x0
-  __DATA.__common: 0x18f170
-  __DATA.__bss: 0x76a00
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__mod_init_func: 0x2b8
-  __DATA_CONST.__const: 0x9a8a0
-  __DATA_CONST.__kalloc_var: 0x8200
-  __DATA_CONST.__kalloc_type: 0x16800
+  __DATA.__common: 0x1926d0
+  __DATA.__bss: 0x76950
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__mod_init_func: 0x2c8
+  __DATA_CONST.__const: 0x9c100
+  __DATA_CONST.__kalloc_var: 0x8250
+  __DATA_CONST.__kalloc_type: 0x16a80
   __DATA_CONST.__brk_desc: 0x60
-  __DATA_CONST.__sdt_cstring: 0x6a43
-  __DATA_CONST.__sdt: 0x10e00
-  __KLDDATA.__init: 0x22890
-  __KLDDATA.__init_entry_set: 0x11880
+  __DATA_CONST.__sdt_cstring: 0x6a93
+  __DATA_CONST.__sdt: 0x10fb0
+  __DATA_CONST.__assert: 0xf0
+  __KLDDATA.__init: 0x22800
+  __KLDDATA.__init_entry_set: 0x11be0
   __KLDDATA.__cstring: 0x79c
-  __KLDDATA.__const: 0x81f0
+  __KLDDATA.__const: 0x88d0
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
+  __KLDDATA.__static_if: 0x0
+  __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__bss: 0x1
-  __HIB.__text: 0x4482
+  __HIB.__text: 0x454c
   __HIB.__bootPT: 0x6000
   __HIB.__desc: 0x8b000
   __HIB.__data: 0x4070

   __LAST.__last: 0x0
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
-  __LINKINFO.__symbolsets: 0x4bb2f
-  __CTF.__ctf: 0xa9421
-  UUID: 0FA106B0-CE42-3EF5-98D6-610845FB1DE7
-  Functions: 25990
-  Symbols:   23168
-  CStrings:  23501
+  __LINKINFO.__symbolsets: 0x4c491
+  __CTF.__ctf: 0xa7814
+  UUID: 640DC745-E487-30ED-B928-A283AF557559
+  Functions: 26256
+  Symbols:   23393
+  CStrings:  23776
 
Symbols:
+ _IOVnodeGetBooleanEntitlement
+ _KHEAP_DATA_SHARED
+ _KHEAP_EARLY
+ _PE_read_socd_client_buffer
+ _SYSCTL_EXTRACT_HEAP_ARG
+ _SYSCTL_READY_HEAP_ARG
+ __Z16IOPolledFileOpenPKcjyyyPvmPP18IOPolledFileIOVarsPP6OSDataPhPm
+ __Z34IOInterruptDispatchSourceInterruptP8OSObjectPvP9IOServicei
+ __ZN13OSValueObjectIiE9MetaClassC1Ev
+ __ZN13OSValueObjectIiE9MetaClassC2Ev
+ __ZN16IONVRAMV3Handler10getVarDictER11OSSharedPtrI12OSDictionaryE
+ __ZN16IONVRAMV3Handler4initEP9IODTNVRAMPKhy
+ __ZN16IONVRAMV3HandlerC1Ev
+ __ZN16IONVRAMV3HandlerC2Ev
+ __ZN18IONVRAMCHRPHandler10getVarDictER11OSSharedPtrI12OSDictionaryE
+ __ZN18IONVRAMCHRPHandler4initEP9IODTNVRAMPKhy
+ __ZN18IONVRAMCHRPHandlerC1Ev
+ __ZN18IONVRAMCHRPHandlerC2Ev
+ __ZN24IOProviderPropertyMerger10gMetaClassE
+ __ZN24IOProviderPropertyMerger10superClassE
+ __ZN24IOProviderPropertyMerger11setPropertyEPK8OSSymbolP8OSObject
+ __ZN24IOProviderPropertyMerger16setPropertyTableEP12OSDictionary
+ __ZN24IOProviderPropertyMerger4initEP12OSDictionary
+ __ZN24IOProviderPropertyMerger9MetaClassC1Ev
+ __ZN24IOProviderPropertyMerger9MetaClassC2Ev
+ __ZN24IOProviderPropertyMerger9metaClassE
+ __ZN24IOProviderPropertyMergerC1EPK11OSMetaClass
+ __ZN24IOProviderPropertyMergerC1Ev
+ __ZN24IOProviderPropertyMergerC2EPK11OSMetaClass
+ __ZN24IOProviderPropertyMergerC2Ev
+ __ZN24IOProviderPropertyMergerD0Ev
+ __ZN24IOProviderPropertyMergerD1Ev
+ __ZN24IOProviderPropertyMergerD2Ev
+ __ZN24IOProviderPropertyMergerdlEPvm
+ __ZN24IOProviderPropertyMergernwEm
+ __ZN25IOGeneralMemoryDescriptor10writeBytesEyPKvy
+ __ZN25IOGeneralMemoryDescriptor9readBytesEyPvy
+ __ZN9IODTNVRAM10getVarDictER11OSSharedPtrI12OSDictionaryE
+ __ZN9IOService25get_watchdog_elapsed_timeEv
+ __ZNK24IOProviderPropertyMerger12getMetaClassEv
+ __ZNK24IOProviderPropertyMerger9MetaClass5allocEv
+ __ZTV24IOProviderPropertyMerger
+ __ZTVN24IOProviderPropertyMerger9MetaClassE
+ __ca_event_format_trap_telemetry_internal
+ __dlil_if_release
+ __telemetry_kernel_notified
+ _bootprofile_type_name
+ _bridge_allow_lro_num_seg
+ _cansignal_nomac
+ _choose_processor_smt
+ _cluster_direct_write_wired
+ _csblob_get_auxiliary_info
+ _csblob_get_trust_level
+ _csblob_set_auxiliary_info
+ _dlif_bufsize
+ _dlif_filt_alloc
+ _dlif_filt_free
+ _dlif_filt_zone
+ _dlif_ifnet_alloc
+ _dlif_ifnet_free
+ _dlif_proto_alloc
+ _dlif_proto_free
+ _dlif_proto_zone
+ _dlif_size
+ _dlif_tcpstat_alloc
+ _dlif_tcpstat_bufsize
+ _dlif_tcpstat_free
+ _dlif_tcpstat_size
+ _dlif_tcpstat_zone
+ _dlif_udpstat_alloc
+ _dlif_udpstat_bufsize
+ _dlif_udpstat_free
+ _dlif_udpstat_size
+ _dlif_udpstat_zone
+ _dlif_zone
+ _dlil_affinity_set
+ _dlil_alloc_lladdr
+ _dlil_allocation_zones_init
+ _dlil_clat46
+ _dlil_clat64
+ _dlil_clean_threading_info
+ _dlil_create_input_thread
+ _dlil_decr_pending_thread_count
+ _dlil_dt_tcall_fn
+ _dlil_if_trace
+ _dlil_ifnet_head
+ _dlil_ifnet_lock
+ _dlil_incr_pending_thread_count
+ _dlil_input_stats_add
+ _dlil_input_stats_sync
+ _dlil_is_clat_needed
+ _dlil_is_native_netif_nexus
+ _dlil_is_rxpoll_input
+ _dlil_lck_attributes
+ _dlil_lock_group
+ _dlil_main_input_thread
+ _dlil_pending_thread_cnt
+ _dlil_terminate_input_thread
+ _dlil_thread_sync_lock
+ _err_monitor
+ _exit_with_mach_exception_using_ast
+ _find_attached_proto
+ _gIOKitPageableMap
+ _if_copy_link_heuristics_stats
+ _if_flt_monitor_busy
+ _if_flt_monitor_enter
+ _if_flt_monitor_leave
+ _if_flt_monitor_unbusy
+ _if_link_heuristics_delay
+ _if_link_heuristics_flags
+ _if_link_heuristics_lqm_max
+ _if_mcasts_update_async
+ _if_proto_free
+ _if_proto_ref
+ _if_update_link_heuristic
+ _ifnet_debug
+ _ifnet_get_congested_link
+ _ifnet_head_lock
+ _ifnet_head_lock_group
+ _ifnet_rcv_lock_group
+ _ifnet_set_congested_link
+ _ifnet_snd_lock_group
+ _in6_pcblookup_hash_try
+ _in_pcblookup_hash_try
+ _ipc_policy_violations_rb
+ _ipc_port_lock
+ _ipc_port_lock_check_aligned
+ _ipc_port_lock_try
+ _ipc_pset_lock
+ _ipc_telemetry_lock
+ _ipc_telemetry_lock_grp
+ _kalloc_shared_data
+ _kalloc_shared_data_external
+ _kfree_shared_data
+ _kfree_shared_data_addr
+ _kfree_shared_data_addr_external
+ _kfree_shared_data_external
+ _kill_on_no_paging_space
+ _kppet_lightweight_start_time
+ _kppet_mark_sampled
+ _kppet_set_period
+ _krealloc_shared_data
+ _krealloc_shared_data_external
+ _log_hexdump
+ _m_drop_if
+ _mac_mount_notify_mount
+ _mach_continuous_speculative_time
+ _mach_exception_ast
+ _mach_vm_deferred_reclamation_buffer_allocate
+ _mach_vm_deferred_reclamation_buffer_flush
+ _mach_vm_deferred_reclamation_buffer_resize
+ _mbuf_get_gso_info
+ _mbuf_get_lro_info
+ _mbuf_set_gso_info
+ _mbuf_set_lro_info
+ _memorystatus_aging_stuck_delay_time
+ _memorystatus_get_reaper_page_shortage_threshold
+ _memorystatus_idle_exit_kill_count
+ _memorystatus_kill_counts
+ _memorystatus_reaper_enabled
+ _memorystatus_reaper_minimum_age_seconds
+ _memorystatus_reaper_rescan_delay_seconds
+ _memorystatus_reaper_threshold_mb
+ _memorystatus_respond_to_compressor_exhaustion
+ _memorystatus_respond_to_swap_exhaustion
+ _memstat_aging_stuck_time_s
+ _memstat_get_idle_proccnt
+ _memstat_get_proccnt_upto_priority
+ _memstat_kill_idle_process
+ _memstat_oldest_reapable_proc_info_expiration_ts_matu
+ _memstat_oldest_reapable_proc_prio_start
+ _memstat_oldest_reapable_proc_will_be_reapable_at_ts_matu
+ _memstat_reaper_can_run_after_ts_matu
+ _memstat_reaper_cumulative_memory_freed_mb
+ _memstat_reaper_cumulative_stats
+ _memstat_reaper_current_sweep_stats
+ _memstat_reaper_enabled
+ _memstat_reaper_is_currently_sweeping
+ _memstat_reaper_max_priority
+ _memstat_reaper_min_age_secs
+ _memstat_reaper_reap_relaunch_mask
+ _memstat_reaper_rescan_secs
+ _memstat_reaper_start_ts_matu
+ _memstat_reaper_threshold
+ _mpsc_ring_cursor_advance
+ _mpsc_ring_cursor_commit
+ _mpsc_ring_init
+ _mpsc_ring_read_cancel
+ _mpsc_ring_read_finish
+ _mpsc_ring_read_start
+ _mpsc_ring_write
+ _munge_wlwwlww
+ _nop_monitor
+ _num_engineering_trust_caches
+ _num_loadable_trust_caches
+ _num_static_trust_caches
+ _os_ref_panic_last
+ _oslog_coproc
+ _oslog_coproc_reg
+ _packet_has_vlan_tag
+ _panic_assert_format
+ _percpu_slot_panic_reason
+ _pmap_enter_object_options_check
+ _pmap_enter_options_check
+ _pmap_is_page_restricted
+ _pmap_zero_page_with_options
+ _proc_find_audit_token
+ _proc_ident
+ _proc_orig_ppidversion
+ _proc_support_long_paths
+ _reclaim_buffers_lock
+ _sched_get_quantum_us
+ _sk_netif_queue_stat_enable
+ _task_get_cs_auxiliary_info_kdp
+ _task_ledger_settle
+ _task_ledger_settle_dirty_time_locked
+ _task_set_ast_mach_exception
+ _task_set_cs_auxiliary_info
+ _task_set_jit_flags
+ _tb_message_decode_buffer
+ _tb_message_get_size
+ _tb_transport_client_activate
+ _tb_transport_construct_message_buffer
+ _tb_transport_destruct_message_buffer
+ _tb_transport_reset_message
+ _tb_transport_send_message
+ _tb_transport_service_activate
+ _tcp_l4s_developer
+ _tcp_link_heuristics_flags
+ _tcp_link_heuristics_rto_min
+ _tcp_reass_qent_alloc
+ _tcp_reass_qent_free
+ _tcp_rxt_seg_qent_alloc
+ _tcp_rxt_seg_qent_free
+ _tcp_seg_sent_qent_alloc
+ _tcp_seg_sent_qent_free
+ _tcp_set_link_heur_rtomin
+ _telemetry_buffer_size
+ _telemetry_kernel_buffer_size_pow_2
+ _telemetry_kernel_gather
+ _telemetry_notification_leeway
+ _thread_ast_mach_exception
+ _thread_wakeup_nthreads_prim
+ _total_corpses_allowed
+ _trap_telemetry_report_exception
+ _trap_telemetry_report_simulated_trap
+ _trap_telemetry_report_simulated_trap_with_backtrace
+ _trap_telemetry_tree_SPLAY
+ _trap_telemetry_tree_SPLAY_INSERT
+ _trap_telemetry_tree_SPLAY_MINMAX
+ _trap_telemetry_tree_SPLAY_REMOVE
+ _udp_log_drop_pcb
+ _uio_restore
+ _unload_trust_cache
+ _upl_has_wired_pages
+ _upl_pages_wired_busy
+ _vfs_exclave_fs_query_volume_group
+ _vfs_exclave_fs_root_ex
+ _vfs_vnodecovered_noblock
+ _vm_compressor_incore_fragmentation_wasted_pages
+ _vm_convert_port_to_copy_object
+ _vm_deferred_reclamation_buffer_allocate_internal
+ _vm_deferred_reclamation_buffer_flush_internal
+ _vm_deferred_reclamation_buffer_resize_internal
+ _vm_deferred_reclamation_gc
+ _vm_deferred_reclamation_ring_disown
+ _vm_deferred_reclamation_ring_own
+ _vm_deferred_reclamation_task_drain
+ _vm_deferred_reclamation_task_fork
+ _vm_deferred_reclamation_task_fork_register
+ _vm_deferred_reclamation_task_has_ring
+ _vm_deferred_reclamation_task_suspend
+ _vm_map_guard_exception
+ _vm_map_is_map_size_valid
+ _vm_map_setup
+ _vm_map_switch_back
+ _vm_map_switch_to
+ _vm_object_copy_delayed_paging_wait_disable
+ _vm_page_create_canonical
+ _vm_page_create_fictitious
+ _vm_page_create_guard
+ _vm_page_create_private
+ _vm_page_get_memory_class
+ _vm_page_is_canonical
+ _vm_page_is_fictitious
+ _vm_page_is_guard
+ _vm_page_is_private
+ _vm_page_is_relocatable
+ _vm_page_is_restricted
+ _vm_page_make_private
+ _vm_page_put_list_on_free_queue
+ _vm_page_relocate
+ _vm_page_reset_private
+ _vm_page_steal_free_page
+ _vm_pageout_gc_cond
+ _vm_pages_array_finalize
+ _vm_pages_end
+ _vm_pre_fault_with_info
+ _vm_reclaim_abandonment_threshold
+ _vm_reclaim_autotrim_pct_critical
+ _vm_reclaim_autotrim_pct_normal
+ _vm_reclaim_autotrim_pct_pressure
+ _vm_reclaim_buffer_count
+ _vm_reclaim_enabled
+ _vm_reclaim_gc_epoch
+ _vm_reclaim_gc_reclaim_count
+ _vm_reclaim_log_handle
+ _vm_reclaim_sampling_period_abs
+ _vm_reclaim_sampling_period_ns
+ _vm_reclaim_wma_denom
+ _vm_reclaim_wma_weight_base
+ _vm_reclaim_wma_weight_cur
+ _vnode_memoryobject
+ _wdt
- _KHEAP_SHARED
- __Z16IOPolledFileOpenPKcjyyPvmPP18IOPolledFileIOVarsPP6OSDataPhPm
- __Z16IOPolledFileOpenPKcjyyPvmPP18IOPolledFileIOVarsR11OSSharedPtrI6OSDataEPhPm
- __ZN16IONVRAMV3Handler4initEP9IODTNVRAMPKhyR11OSSharedPtrI12OSDictionaryE
- __ZN16IONVRAMV3HandlerC1ER11OSSharedPtrI12OSDictionaryE
- __ZN16IONVRAMV3HandlerC2ER11OSSharedPtrI12OSDictionaryE
- __ZN18IONVRAMCHRPHandler4initEP9IODTNVRAMPKhyR11OSSharedPtrI12OSDictionaryE
- __ZN18IONVRAMCHRPHandlerC1ER11OSSharedPtrI12OSDictionaryE
- __ZN18IONVRAMCHRPHandlerC2ER11OSSharedPtrI12OSDictionaryE
- ___smr_linkage_invalid
- ___smr_stail_invalid
- ___smr_tail_invalid
- _async_reclamation_buffers_lock
- _bootprofile_init
- _ca_entries_lck
- _ca_entries_lock_grp
- _choose_processor
- _delay_above_pnum
- _guard_ast
- _if_rtproto_del
- _ifnet_decr_pending_thread_count
- _ip_violates_reply_port_semantics
- _ip_violates_rigid_reply_port_semantics
- _ipc_right_check
- _ipc_right_copyin
- _ipc_right_copyin_check_reply
- _ipc_right_copyin_two
- _ipc_right_copyout
- _ipc_right_dealloc
- _ipc_right_delta
- _ipc_right_destroy
- _ipc_right_destruct
- _ipc_right_info
- _ipc_right_inuse
- _ipc_right_lookup_read
- _ipc_right_lookup_two_write
- _ipc_right_lookup_write
- _ipc_right_request_alloc
- _ipc_right_reverse
- _ipc_right_terminate
- _kppet_gencount
- _kppet_lightweight_active
- _m_devget
- _mac_proc_check_delegated_signal
- _mach_port_guard_exception
- _mach_port_guard_exception_immovable
- _mach_port_guard_exception_pinned
- _mach_vm_deferred_reclamation_buffer_init
- _mach_vm_deferred_reclamation_buffer_synchronize
- _max_kill_priority
- _memorystatus_get_proccnt_upto_priority
- _memorystatus_idle_exit_from_VM
- _no_paging_space_action
- _primary_processor_avail_count
- _processor_state_update_explicit
- _reclamation_buffers_lock
- _reply_port_semantics_violations_rb
- _reply_port_telemetry_lock
- _reply_port_telemetry_lock_grp
- _service_port_defense_enabled
- _task_set_jit_exception_fatal_flag
- _task_store_owned_vmobject_info
- _telemetry_init
- _telemetry_kernel_brk
- _telemetry_mark_curthread
- _telemetry_needs_record
- _telemetry_needs_timer_arming_record
- _telemetry_sample_rate
- _vm_deferred_reclamation_buffer_disown
- _vm_deferred_reclamation_buffer_fork
- _vm_deferred_reclamation_buffer_init_internal
- _vm_deferred_reclamation_buffer_own
- _vm_deferred_reclamation_buffer_synchronize_internal
- _vm_deferred_reclamation_buffer_uninstall
- _vm_deferred_reclamation_reclaim_all_memory
- _vm_deferred_reclamation_reclaim_from_task_async
- _vm_deferred_reclamation_reclaim_from_task_sync
- _vm_deferred_reclamation_reclaim_memory
- _vm_delayed_count
- _vm_map_switch
- _vm_page_array_beginning_addr
- _vm_page_array_ending_addr
- _vm_page_create
- _vm_page_created
- _vm_page_grab_fictitious
- _vm_page_grab_guard
- _vm_page_release_fictitious
- _vm_reclaim_max_threshold
- _vm_reclaim_trim_divisor
CStrings:
+ "\nTotal number of packets transmitted: %u\n"
+ "\"TB_ASSERT: \" \"tb_priv(transport)->static_vtable != NULL\" @%s:%d"
+ "\"TB_ASSERT: \" \"tp_priv->static_vtable != NULL\" @%s:%d"
+ "%llx@%x\n"
+ "%lu.%03d memorystatus: killing_specific_process pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu\n"
+ "%lu.%03d memorystatus: killing_top_process_elevated%d pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu\n"
+ "%lx@!\n"
+ "%s at 0x%016llx, %sregisters:\nCR0: 0x%016llx, CR2: 0x%016llx, CR3: 0x%016llx, CR4: 0x%016llx\nRAX: 0x%016llx, RBX: 0x%016llx, RCX: 0x%016llx, RDX: 0x%016llx\nRSP: 0x%016llx, RBP: 0x%016llx, RSI: 0x%016llx, RDI: 0x%016llx\nR8:  0x%016llx, R9:  0x%016llx, R10: 0x%016llx, R11: 0x%016llx\nR12: 0x%016llx, R13: 0x%016llx, R14: 0x%016llx, R15: 0x%016llx\nRFL: 0x%016llx, RIP: 0x%016llx, CS:  0x%016llx, SS:  0x%016llx\nFault CR2: 0x%016llx, Error code: 0x%016llx, Fault CPU: 0x%x%s%s%s%s, PL: %d, VF: %d\n"
+ "%s detached"
+ "%s detaching"
+ "%s-%s-%u.%u.%u.%u-%x%s"
+ "%s: %s (%s) append %d bytes mss %d op %d"
+ "%s: %s bridge_get_tcp_header failed %d"
+ "%s: %s bridge_get_tcp_header failed %d (%s)"
+ "%s: %s bridge_offload_checksum failed %d"
+ "%s: %s failed: %d @%s:%d"
+ "%s: %s supports LRO_NUM_SEG, leaving LRO enabled"
+ "%s: %s: does %ssupport checksum"
+ "%s: %s: mss %d = len %d / seg cnt %d"
+ "%s: Unregister message size too small for UUID: (%zu < %zu)\n"
+ "%s: WARNING: more than %d leaders in priority band [%d]\n"
+ "%s: entitlement is not OSBoolean @%s:%d"
+ "%s: vm_fault_page() return unexpected error 0x%x\n @%s:%d"
+ "%s:%d Assertion failed: %s %s %s (%p %s %p)"
+ "%s:%d Assertion failed: %s %s %s (0x%lx %s 0x%lx, %ld %s %ld)"
+ "%s:%d Assertion failed: %s %s %s (0x%lx %s 0x%lx, %lu %s %lu)"
+ "%s:%d in6_pcblookup_hash_try no pcb %s\n"
+ "%s:%d in_pcblookup_hash_try no pcb %s\n"
+ "%s:%d pid %d (%s) is unable to transmit packets on %s\n"
+ "%s::init in provider %s[0x%qx] fails\n"
+ "%s[0x%qx]::attach(%s[0x%qx])\n"
+ "%s[0x%qx]::probe fails\n"
+ "%s[0x%qx]::probe(%s)\n"
+ "%s[0x%qx]::start took %ld ms\n"
+ "%s[0x%qx]::start(%s) <%d>\n"
+ "%s[0x%qx]::start(%s[0x%qx]) <%d> failed\n"
+ "((intptr_t)base + object_size) <= ((intptr_t)buf + buffer_size)"
+ "(tag & kIOHibernateTagSigMask) == kIOHibernateTagSignature"
+ "*proto_family == PF_INET6"
+ "-bsdmgroot-ramdisk"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/mcache.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_ctl.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil_subr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/net_thread_marks.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/cpu_in_cksum_gen.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IOHibernateRestoreKernel.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/i386/cpu_threads.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_config.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_dvfs.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_idle.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_ioctl.c"
+ "111111111111112222222222222222"
+ "11112221122222211121"
+ "11122221222222222222222112"
+ "1122112121222222222222"
+ "12111111211111122222212212212222122222212211222211222221111222221222221111211111112"
+ "12111112122212121111112"
+ "12211211222111"
+ "1221121221211"
+ "2211111111111112222222112222211222221111112222111111122222222211121111211111222222222222222222222222222222222220122222211221222222222222222222222222222222222222222222222222222222221122222221211222222222222221211122222222222221222222112222222212222222222222222221111111222222222200"
+ "22211112"
+ "222121112211221122111022222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222022222111111212111122222111222122222222222222112220"
+ "22222222122222222112222222222222222211111112212222111121"
+ "322222222222222222222222222222"
+ "About to kill %p due to %d with subcode %lld\n @%s:%d"
+ "AppleAPFSVolume"
+ "B16@?0^{proc=(?={?=^{proc}^^{proc}}{smr_node=^{smr_node}^?})^{proc}^{proc_ro}iiIIIIIIiQ{?=[2Q]}icccc{?=^{proc}^^{proc}}{?=^{proc}^^{proc}}{?=^{proc}}{?=^{uthread}^^{uthread}}{smrq_slink={?=^{smrq_slink}}}^{persona}{?=^{proc}^^{proc}}{?=[2Q]}{?=[2Q]}{filedesc={?=[2Q]}CCSiiiii^^{fileproc}*^{klist}^{kqworkq}^{vnode}^{vnode}{?=[2Q]}{?=[2Q]}Q^{kqwllist}{?=[2Q]}Q^{klist}}^{pstats}{?=^{plimit}}{?=^{pgrp}}{sigacts=[32Q][32Q][32I]IIIIIIAIiiii}{?=[10Q]}iIIIIAIAIiiiIi{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}{itimerval={timeval=qi}{timeval=qi}}{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}ii^v^viIII^viiiICQQ{?=[2Q]}^{dtrace_ptss_page}^{dtrace_ptss_page_entry}^{dtrace_helpers}^{dof_ioctl_data}(?={?=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C][16C]ii}{proc_forkcopy_data=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C][16C]ii}){?=^{aio_workq_entry}^^{aio_workq_entry}}{?=^{aio_workq_entry}^^{aio_workq_entry}}{klist=^{knote}}^{rusage_superset}^{thread}^{thread}iSSQQiIQA^{workqueue}{timeval=qi}^v^vQQQQQQQQ{timeval=qi}CBBIiiiI{?=^{proc}^^{proc}}QQQQiiiiAIIQII^{os_reason}Q*}8"
+ "B16@?0^{task={lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}[4^{ipc_port}]^{ipc_port}^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^{user_ldt}^vQQQi^Q^Q^Q^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCC^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}b16b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}Q}8"
+ "Bridge allow LRO_NUM_SEG to keep LRO enabled"
+ "Cannot place with a max_address constraint @%s:%d"
+ "Cannot place with multiple min_address constraints @%s:%d"
+ "Could not find UUID in cache but cache was full @%s:%d"
+ "DK: %s-0x%qx->Stop(%s-0x%qx)\n"
+ "DK: %s-0x%qx->Stop(%s-0x%qx) returned %x\n"
+ "DK: %s-0x%qx->Stop_async(%s-0x%qx)\n"
+ "DK: %s-0x%qx: %s: instantiate failed 0x%x\n"
+ "DK: %s-0x%qx: %s::Dispatch kernel 0x%qx\n"
+ "DK: %s-0x%qx: %s::Dispatch kernel 0x%qx result 0x%x\n"
+ "DK: %s-0x%qx::LoadModule 0x%x %s\n"
+ "DK: %s-0x%qx::clientClose(%p)\n"
+ "DK: %s-0x%qx::exit(%s)\n"
+ "DK: %s-0x%qx::finalize(%p)\n"
+ "DK: %s-0x%qx::finalize(%p) could not find fCheckInToken\n"
+ "DK: %s-0x%qx::finalize(%p) dext was replaced, do not rematch current dext\n"
+ "DK: %s-0x%qx::kill(%s)\n"
+ "DK: %s-0x%qx::powerOff(%d) %d\n"
+ "DK: %s-0x%qx::registerClass %s, %d, %d\n"
+ "DK: %s-0x%qx::serviceAttach(%s-0x%qx, %s-0x%qx)\n"
+ "DK: %s-0x%qx::serviceClose(%s-0x%qx, %s-0x%qx) -> %x\n"
+ "DK: %s-0x%qx::serviceStop(%s-0x%qx, %s-0x%qx)\n"
+ "DK: %s-0x%qx::serviceStop(%s-0x%qx, %s-0x%qx): could not find service\n"
+ "DK: %s-0x%qx::systemHalt()\n"
+ "DK: %s-0x%qx::terminate(%s-0x%qx)\n"
+ "DK: %s-0x%qx::terminate(%s-0x%qx) server exit before start()\n"
+ "DK: %s[0x%qx]::willTerminate serviceWillTerminate not called\n"
+ "DK: serviceDidStop(%s-0x%qx, %s-0x%qx) -> complete %d\n"
+ "DK: serviceDidTerminate(%s-0x%qx, %s-0x%qx) -> defer %d\n"
+ "DK: serviceWillTerminate(%s-0x%qx, %s-0x%qx)\n"
+ "Debugger re-entry scheduled in %u milliseconds\n"
+ "Deferred Memory Reclamation"
+ "Developer L4S mode (0: system, 1: force enable L4S, 2: force disable L4S"
+ "Error copying pipe from user, %d"
+ "Expected to have usecount or iocount on vnode @%s:%d"
+ "Failed to add hardened heap string with error %d\n"
+ "Failed to allocate drain callout! @%s:%d"
+ "IOPageableMapForAddress: address out of range @%s:%d"
+ "IOProviderMergeProperties"
+ "IOProviderParentMergeProperties"
+ "IOProviderPropertyMerger"
+ "IOVnodeGetBooleanEntitlement"
+ "IPv6 only with IPv4 mapped error EINVAL"
+ "Invalid relocation reason %u @%s:%d"
+ "KT_NOEARLY used w/o private accounting for view %s @%s:%d"
+ "Kernel trap"
+ "MCLGET error ENOBUFS"
+ "MGETHDR error ENOBUFS"
+ "M_PREPEND error ENOBUFS"
+ "Max value to enable link heuristics"
+ "Not allowed to register multiple agents"
+ "OSValueObject<int>"
+ "Overflowed vm_reclaim_buffer_count @%s:%d"
+ "Panic server returned error %u, retrying\n"
+ "Request for unregistration of all agents"
+ "Request to enable session mode"
+ "Route logging verbosity level"
+ "Routing through specified router IP %s (%u)\n"
+ "SKMEM_SLAB_MEMBER(sl, SKMEM_MEMTAG_STRIP_TAG(buf, skm->skm_objsize))"
+ "SYN data invalid"
+ "SYN in ESTABLISHED state"
+ "Session already has agent registered"
+ "Session has no matching agent"
+ "Sleep transition timed out after %qd seconds"
+ "Stoping flow set copy after %d elements to avoid overflow; mem: available=%lu, required=%lu"
+ "System L4S mode (0: disable, 1: enable L4S"
+ "System is unhealthy but compressor, swap, and zone map are not exhausted @%s:%d"
+ "TCP LQM heuristics flags (1:rxmtcomp 2:noackpro 4:synrxmt 8:stealth 0x10:rtomin 0x20:notlp)"
+ "Unable to create VM reclaim thread, %d @%s:%d"
+ "Underflowed vm_reclaim_buffer_count @%s:%d"
+ "Unexpected telemetry CA event: %u\n @%s:%d"
+ "Unexpectedly could not acquire telemetry lock (nested acquire will deadlock) @%s:%d"
+ "Unrecognized heap selector"
+ "Unrecognized relocation reason %u\n @%s:%d"
+ "Unrecognized remove reason %u @%s:%d"
+ "VM_PAGE_PACK_PTR failed on vm_pages - %p @%s:%d"
+ "VM_PAGE_PACK_PTR failed on vm_pages_end - %p @%s:%d"
+ "VM_reclaim_scavenger"
+ "VolGroupUUID"
+ "Wake transition timed out after %qd seconds"
+ "XNU Trust Caches"
+ "[trap_telemetry] \t0x%08lx\n"
+ "[trap_telemetry] Triggered trap at PC=0x%08lx (type=%u, code=0x%04llx). Backtrace:\n"
+ "[trap_telemetry] trap_telemetry_init\n"
+ "_memstat_proc_is_reapable: %s [%d] is reapable; priority=%d, age=%d, relaunch_probability_acceptable_mask=0x%02X\n"
+ "_memstat_proc_is_reapable: %s [%d] not reapable because age (%llu) is below min age (%d)\n"
+ "_memstat_proc_is_reapable: %s [%d] not reapable because priority (%d) is above threshold (%d)\n"
+ "_memstat_proc_is_reapable: %s [%d] not reapable because relaunch probability bitmask (0x%02X) does not match with the memstat_reaper_reap_relaunch_mask (0x%02X).\n"
+ "allow_lro_num_seg"
+ "already connected error EISCONN"
+ "apple_protect_pager_data_request"
+ "apt-carveout-size-mb"
+ "attempting to unload trust cache with UUID: %s\n"
+ "bad RST in ESTABLISHED state"
+ "bad address family error EAFNOSUPPORT"
+ "bad option error %d"
+ "bad scope error EINVAL"
+ "calling task not permitted to unload trust caches\n"
+ "cluster_direct_write_wired"
+ "com.apple.developer.hardened-process"
+ "com.apple.developer.hardened-process.hardened-heap"
+ "com.apple.private.AppleProcessorTrace.CarveoutProperty"
+ "com.apple.private.coprocessor-logging"
+ "com.apple.private.networking.elevated-logging"
+ "com.apple.private.unload-trust-cache"
+ "com.apple.private.vfs.support-long-paths"
+ "com.apple.private.vfs.system-volume-unmount"
+ "cp_pipe_to_64_user"
+ "data_shared."
+ "data_shared.kalloc"
+ "di_root_image"
+ "di_root_ramfile_buf"
+ "dlil_ctl.c"
+ "dlil_subr.c"
+ "dn_copy_set_32"
+ "dn_copy_set_64"
+ "dummynet: dn_heap_get_node_offset from middle not supported on this heap!!!"
+ "dummynet: dn_heap_get_node_offset, offset %d out of bound 0..%d\n"
+ "dummynet_get"
+ "early."
+ "early.kalloc"
+ "error:%d\n"
+ "fixed"
+ "flow controlled error ENOBUFS"
+ "gIOKitPageableFixed"
+ "gso_tcp"
+ "hardened_heap=1"
+ "heap->offset + sizeof(int) <= ent->obj_size"
+ "heap->offset + sizeof(int) <= obj_size"
+ "heap->size <= node"
+ "hibernate_page_list_setall preflight pageCount %d est comp %qd setfilemin %qd setfilemax %qd min %qd\n"
+ "if_disable_link_heuristics: %s IFXF_LINK_HEURISTICS cleared"
+ "if_link_heuristics"
+ "if_update_link_heuristic: %s IFXF_LINK_HEURISTICS set"
+ "if_update_link_heuristic: %s delay already in progress"
+ "if_update_link_heuristic: %s delay cancelled"
+ "if_update_link_heuristic: %s scheduled"
+ "if_update_link_heuristic: %s scheduled with delay"
+ "ifp->if_link_heuristics_tcall != NULL"
+ "ifp->if_proto_hash != NULL"
+ "imageboot_read_file"
+ "in6_pcbsetport error %d"
+ "in_pcbconnect error %d"
+ "in_pcbladdr error %d"
+ "inp_restricted_send"
+ "interface %s congested_link set to %d"
+ "interface_supports_hw_checksum"
+ "invalid compression type 0x%llxin kcdata_finish_compression @%s:%d"
+ "ip address: %u.%u.%u.%u\n"
+ "ip6_savecontrol error %d"
+ "ip_dn_debug %s:%d : Advancing bp_inner old=0x%llx new=0x%llx end=0x%llx available=%lu\n"
+ "ip_dn_debug %s:%d : Asked to copy set_32: available=%ld, required=%lu\n"
+ "ip_dn_debug %s:%d : Asked to copy set_64: available=%ld\n"
+ "ip_dn_debug %s:%d : Insufficient space to copy: available=%ld, required=%lu\n"
+ "ip_dn_debug %s:%d : Iter=%d to copied=%d available=%ld\n"
+ "ip_dn_debug %s:%d : Overflow detected old=0x%llx end=0x%llx\n"
+ "ip_dn_debug %s:%d : Overflow detected old=0x%llx end=0x%llx available=%lu required=%lu\n"
+ "ip_dn_debug %s:%d : Returning 0x%llx overflow=%d bp=0x%llx bp_inner=0x%llx bp_end=0x%llx available=%ld total_required=%d total_available=%lu\n"
+ "ip_dn_debug %s:%d : Would overflow: available=%ld\n"
+ "ip_dn_debug %s:%d : advancing bp: old=0x%llx new=0x%llx end=0x%llx\n"
+ "ip_savecontrol error %d"
+ "ipc_object_copyin_from_kernel: strange rights"
+ "ipc_object_copyout_dest: strange rights"
+ "ipc_object_destroy: strange rights"
+ "ipc_object_destroy_dest: strange rights"
+ "ipc_right_copyout: strange rights"
+ "ipc_right_destroy: strange type"
+ "ipsec_setsocket error ENOBUFS"
+ "kdp_crashdump_pkt_size is too large. Reverting to %u\n"
+ "kdp_send: packet too large (%u > %d)"
+ "kdp_set_dump_info: Skipping invalid panicd port %u (using %d)\n"
+ "kern_direct_file(%s): using reduced size %qd\n"
+ "kern_memorystatus_policy.c"
+ "killing_idle_process_aggressive"
+ "killing_top_process_aggressive"
+ "kmem_range_init: vm_map_locate_space failing for claim %s, size 0x%llx @%s:%d"
+ "kr == 0"
+ "l4s_developer"
+ "len %d too big error EMSGSIZE"
+ "link heuristics"
+ "link_heuristics_delay"
+ "link_heuristics_flags"
+ "link_heuristics_lqm_max"
+ "link_heuristics_rto_min"
+ "load_code_signature: %s: failed to allocate space for reason string (os_reason_alloc_buffer error: %d, kcdata error: %d, length: %lu)\n"
+ "load_code_signature: %s: failed to copy reason string (kcdata_memcpy error: %d, length: %lu)\n"
+ "long-idle-exit"
+ "m_copym_mode error ENOBUFS"
+ "m_copym_with_hdrs error ENOBUFS"
+ "mac__call__mount_notify_mount"
+ "mac__rslt__mount_notify_mount"
+ "mach_vm_address_t"
+ "mach_vm_reclaim_action_t"
+ "mach_vm_reclaim_count_t"
+ "mach_vm_recliam_action_t"
+ "main_input"
+ "med"
+ "memorystatus: %s [%d] exceeded diag threshold limit: %d MB \n"
+ "memorystatus: %s [%d] exceeded mem limit: %s%s %d MB (%s)\n"
+ "memorystatus: %s pid %d [%s] (%s %d %llus rf:%s) %lluKB - memorystatus_available_pages: %llu compressor_size:%u\n"
+ "memorystatus: %s%d pid %d [%s] (%s %d %llus rf:%s - memorystatus_available_pages: %llu\n"
+ "memorystatus: _memstat_refresh_oldest_reapable_proc_info: re-using existing data\n"
+ "memorystatus: _memstat_refresh_oldest_reapable_proc_info: rescanning proc list\n"
+ "memorystatus: aggressive%d: rewinding band %d, %s(%d) moved or exiting.\n"
+ "memorystatus: aggressive%d: skipping %d [%s] (exiting?)\n"
+ "memorystatus: aggressively killing up to %d processes below band %d.\n"
+ "memorystatus: apcs_proc_count = %d, apcs_total_size = %qd\n"
+ "memorystatus: attempt to unkill pid %s [%d] ignored\n"
+ "memorystatus: attempting pcontrol on [%d]\n"
+ "memorystatus: cannot find process for [%d] -- may have exited\n"
+ "memorystatus: doing pcontrol on %s [%d]\n"
+ "memorystatus: failed to allocate jetsam reason\n"
+ "memorystatus: giving up aggressive kill after killing %d processes below band %d.\n"
+ "memorystatus: killing %s [%d] due to swap exhaustion\n"
+ "memorystatus: killing %s [%d] in band %d with high relaunch probability\n"
+ "memorystatus: killing due to \"%s\" - compression_ratio=%u\n"
+ "memorystatus: killing largest compressed process %s [%d] %llu MB\n"
+ "memorystatus: memorystatus_kill_top_process: found reapable long-idle process %s [%d]\n"
+ "memorystatus: memorystatus_kill_top_process: skipping non-reapable process %s [%d]\n"
+ "memorystatus: not tracking idle exit kill for priority %d\n"
+ "memorystatus: not tracking kill with invalid priority %d / cause %d\n"
+ "memorystatus: npcs_proc_count = %d, npcs_total_size = %qd, npcs_max_size = %qd\n"
+ "memorystatus: overflowed kill count for priority %d + cause %d\n"
+ "memorystatus: pcs_proc_count = %d, pcs_total_size = %qd, pcs_max_size = %qd\n"
+ "memorystatus: post-jetsam compressor fragmentation_level=%u\n"
+ "memorystatus: prio_start > mach_absolute_time for %s(%d)? Using delta of 0.\n"
+ "memorystatus: resuming %s [%d]\n"
+ "memorystatus: skipping %s [%d] without pcontrol\n"
+ "memorystatus: skipping idle but not idle-exitable process %s [%d] (0x%x)\n"
+ "memorystatus: suspending %s [%d] due to swap exhaustion\n"
+ "memorystatus: throttling %s [%d] due to swap exhaustion\n"
+ "memorystatus: triggering no paging space action\n"
+ "memorystatus: unable to find any eligible processes to take action on\n"
+ "memorystatus: unthrottling %s [%d]\n"
+ "memorystatus: {\"compressor_exhausted\": %d, \"zone_map_is_exhausted\": %d, \"swap_low\": %d, \"swap_exhausted\": %d}\n"
+ "memorystatus_do_action: Processing swapin queue of length: %u memorystatus_available_pages: %llu\n"
+ "memorystatus_do_action: Waking up swap thread. memorystatus_available_pages: %llu\n"
+ "memorystatus_kill_processes_aggressive: failed to allocate exit reason\n"
+ "memorystatus_perform_idle_demotion() timed out stuck process %d [%s], moving to idle band\n"
+ "memorystatus_sort_by_largest_coalition_locked"
+ "microstackshot: kernel sample magic is invalid @%s:%d"
+ "mpsc_ring.c"
+ "mpsc_ring_init: failed to allocate %u bytes for buffer @%s:%d"
+ "mpsc_ring_init: failed to allocate %zu bytes for holds @%s:%d"
+ "netagent_handle_enable_session_mode_setopt"
+ "netagent_handle_unregister_message"
+ "netagent_handle_unregister_setopt"
+ "netagent_unregister_all_session_registrations"
+ "netagent_unregister_one_session_registration"
+ "not a pair of copy/move-send"
+ "not connected error ENOTCONN"
+ "num_engineering"
+ "num_loadable"
+ "num_static"
+ "number of engineering trust caches loaded"
+ "number of loadable trust caches loaded"
+ "number of static trust caches loaded"
+ "oiddescr"
+ "os_refcnt: expected release of final reference but rc %p!=0\n @%s:%d"
+ "oslog_coproc"
+ "oslog_coproc_reg"
+ "pages_grabbed_iopl"
+ "pages_grabbed_kern"
+ "pages_grabbed_upl"
+ "panic: corrupt list around element %p"
+ "panic: string operation caused an overflow"
+ "realtime"
+ "reclaim_drain"
+ "reclaim_entry"
+ "reclaim_flush"
+ "reclaim_ring_allocate"
+ "reclaim_ring_resize"
+ "reclaim_sample"
+ "reclaim_trim"
+ "register custom esp: invalid proto %u\n"
+ "rotating bpf buffers during read @%s:%d"
+ "save_summary: pmap traversal failed: %d\n"
+ "sbappendaddr full receive socket buffer"
+ "scheduler: thread %s [%llx] in process %s [%d] triggered fail-safe by spinning for at least %dus at %s priority\n"
+ "sin6_port 0 error EADDRNOTAVAIL"
+ "site.IOProviderPropertyMerger"
+ "site.struct if_linkheuristics"
+ "site.struct netagent_registration"
+ "site.trap_telemetry_tree_entry_s"
+ "sizeof(struct dn_pkt_tag) <= tag->m_tag_len"
+ "socket already connected error EISCONN"
+ "source address not available error EADDRNOTAVAIL"
+ "stats_count <= MPTCP_ITFSTATS_SIZE"
+ "tag %u has same device 0x%x as tag %u\n"
+ "tcp6_connect"
+ "tcp6_usr_listen"
+ "tcp_attach"
+ "tcp_connect"
+ "tcp_connection_summary (%s:%d)[%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u Duration: %u.%03u sec Conn_Time: %u.%03u sec bytes in/out: %llu/%llu pkts in/out: %llu/%llu pkt rxmit: %u ooo pkts: %u dup bytes in: %u ACKs delayed: %u delayed ACKs sent: %u\nrtt: %u.%03u ms rttvar: %u.%03u ms base rtt: %u ms so_error: %d svc/tc: %u flow: 0x%x"
+ "tcp_drop"
+ "tcp_init: set tcp_link_heuristics_flags to 0x%x"
+ "tcp_link_heuristics"
+ "tcp_state_changed (%s:%d) [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u %s "
+ "tcp_usr_listen"
+ "tcp_usrclosed"
+ "telemetry.c"
+ "telemetry: allocation failed: %d\n"
+ "telemetry_init: failed to allocate kernel notification thread call @%s:%d"
+ "thread_wakeup_nthreads_prim"
+ "trap_telemetry.c"
+ "trap_telemetry_init"
+ "trustcaches"
+ "type = %d=%s #%#04hx, "
+ "type = %d=%s, "
+ "udp drop %s[%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu so_state: 0x%04x process: %s:%u so_error: %d reason: %s"
+ "udp6_append"
+ "udp6_input"
+ "udp6_output"
+ "udp_append"
+ "udp_check_pktinfo error %d"
+ "udp_output"
+ "unable to unload trust cache with UUID: %s | %d\n"
+ "validation_disables"
+ "vm_page_bootstrap: %d free pages, %d wired pages, (up to %d of which are delayed free)%c"
+ "vm_page_grab_options_internal"
+ "vm_reclaim: %s [%d] failed to allocate VA for reclaim buffer (%d)\n"
+ "vm_reclaim: Force-exiting %s [%d]\n"
+ "vm_reclaim: Killing [%d] due to copy I/O error\n"
+ "vm_reclaim: Skipping non fatal guard exception for %s [%d]\n"
+ "vm_reclaim: Tail < head! Userspace is likely attempting a cancellation; aborting reclamation | head: %llu (0x%llx) > tail: %llu (0x%llx) | busy = %llu (0x%llx)\n"
+ "vm_reclaim: Userspace modified head or busy pointer! head: %llu (0x%llx) | busy: %llu (0x%llx) | tail = %llu (0x%llx)\n"
+ "vm_reclaim: [%d] Failed to free(reusable) (0x%llx, 0x%llx) err=%d\n"
+ "vm_reclaim: [%d] Killing due to deallocation failure at (0x%llx, 0x%llx) err=%d\n"
+ "vm_reclaim: [%d] Killing due to virtual-memory guard at (0x%llx, 0x%llx)\n"
+ "vm_reclaim: denying request to allocate ringbuffer of size %llu KiB (max %llu KiB)\n"
+ "vm_reclaim: failed to initialize deferred reclamation buffer - vm_reclaim is disabled\n"
+ "vm_reclaim: unexpected vm_pressure_level %d @%s:%d"
+ "vm_reclaim_entry"
- "\nTotal number of packets transmitted: %d\n"
- "#67"
- "#68"
- "%lu.%03d memorystatus: killing_specific_process pid %d [%s] (%s %d) %lluKB - memorystatus_available_pages: %llu\n"
- "%lu.%03d memorystatus: killing_top_process_elevated%d pid %d [%s] (%s %d) %lluKB - memorystatus_available_pages: %llu\n"
- "%s #%#04hx"
- "%s-%s-%d.%d.%d.%d-%x%s"
- "%s:  broadcast: %02x:%02x:%02x:%02x:%02x:%02x"
- "%s: %s %sfrom %s m 0x%llx data 0x%llx"
- "%s: %s (%s) append %d bytes op %d"
- "%s: %s bridge_host_filter failed"
- "%s: %s bridge_send(%s) len %d op %d"
- "%s: %s m 0x%llx"
- "%s: %s mcast for us"
- "%s: %s.%dbrhf_dhcp_bad_chaddr"
- "%s: %s.%dbrhf_dhcp_bad_ciaddr"
- "%s: %s.%dbrhf_dhcp_bad_hlen"
- "%s: %s.%dbrhf_dhcp_bad_htype"
- "%s: %s.%dbrhf_dhcp_bad_op"
- "%s: %s.%dbrhf_dhcp_too_small"
- "%s: %s.%dbrhf_ip_bad_srcaddr"
- "%s: %s.%dbrhf_ip_too_small"
- "%s: detached\n"
- "%s: detaching\n"
- "%s: large non IP packet"
- "%s: large non IPv4/IPv6 packet"
- "%s: pid %d refc: %u != 0 @%s:%d"
- "%s:%d in6_pcblookup_hash no pcb %s\n"
- "%s:%d in_pcblookup_hash no pcb %s\n"
- "%s::attach(%s)\n"
- "%s::detach(%s)\n"
- "%s::init fails\n"
- "%s::probe fails\n"
- "%s::probe(%s)\n"
- "%s::start took %ld ms\n"
- "%s::start(%s) <%d>\n"
- "%s::start(%s) <%d> failed\n"
- "((intptr_t)base + dlif_size) <= ((intptr_t)buf + dlif_bufsize)"
- "((intptr_t)base + dlif_tcpstat_size) <= ((intptr_t)buf + dlif_tcpstat_bufsize)"
- "((intptr_t)base + dlif_udpstat_size) <= ((intptr_t)buf + dlif_udpstat_bufsize)"
- "(tag & ~kIOHibernateTagLength) == kIOHibernateTagSignature"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/dev/dtrace/dtrace.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_control.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kern_event.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_mbuf.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socket.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/kpi_socketfilter.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/mcache.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/socket_flows.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/subr_eventhandler.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/sys_domain.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/tracker.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_domain.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_mbuf2.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_proto.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_socket2.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_syscalls.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/uipc_usrreq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/kern/vsock_domain.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/bpf.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/classq/classq_subr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/content_filter.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/dlil.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/droptap.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/flowadv.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bond.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_bridge.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_fake.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ipsec.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_llreach.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_loop.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_ports_used.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_redirect.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_utun.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/if_vlan.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/iptap.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/kpi_interface.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/mblist.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nat464_utils.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ndrv.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/necp_client.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/network_agent.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/ntstat.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/nwk_wq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_if.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_ioctl.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_norm.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_pbuf.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pf_table.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktap.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/route.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/net/rtsock.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/cpu_in_cksum_gen.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/flow_divert.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/igmp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_arp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_mcast.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_pcb.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_proto.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_rmx.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/in_tclass.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_dummynet.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_encap.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_icmp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_input.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/ip_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_pcb.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mp_proto.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_opt.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_subr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_timer.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/mptcp_var.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/raw_ip.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cache.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_cubic.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_input.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_ledbat.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_prague.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_sack.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_subr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_timer.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/tcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet/udp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_core.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_input.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ah_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_core.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_input.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/esp_rijndael.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/frag6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/icmp6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_cga.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_ifattach.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_mcast.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_pcb.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_proto.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_rmx.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/in6_src.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_forward.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_id.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_input.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ip6_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/ipsec.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/mld6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_nbr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rti.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_rtr.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/nd6_send.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/scope6.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netinet6/udp6_output.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/key.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/netkey/keysock.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/core/skywalk.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/netns.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/namespace/protons.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_classq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/monitor/nx_monitor.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/iokit/Kernel/IOHibernateRestoreKernel.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/i386/cpu_threads.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_config.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_dvfs.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_idle.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/xnu/osfmk/x86_64/xcpm/xcpm_ioctl.c"
- "11111111111112222222222222222"
- "11112211212122222222"
- "111222212222222222222112"
- "11222112222221111"
- "1211111121111112222212212212222122222212211222211222221111222221222221111211111112"
- "12111112122212121111111112"
- "122112112221"
- "12211212212"
- "2211111111111112222222112222211222221111112222111111122222222211121111211111222222222222222222222222222222222220122222211221222222222222222222222222222222222222222222222222222222221122222221211222222222222221211122222222222221222222112222222212222222222222222211111112222222222000"
- "222111"
- "2221211122112211221110222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220222221111112121111222221112221222222222222221122"
- "2222222212222222211222222222222222211111112212222111121"
- "32222222222222222222222222222"
- "Allocate kernel policy id failed.\n"
- "Allocate string id failed.\n"
- "Allocate trie id failed.\n"
- "B16@?0^{proc=(?={?=^{proc}^^{proc}}{smr_node=^{smr_node}^?})^{proc}^{proc_ro}iiiIIIIIIiQ{?=[2Q]}icccc{?=^{proc}^^{proc}}{?=^{proc}^^{proc}}{?=^{proc}}{?=^{uthread}^^{uthread}}{smrq_slink={?=^{smrq_slink}}}^{persona}{?=^{proc}^^{proc}}{?=[2Q]}{?=[2Q]}{filedesc={?=[2Q]}CCSiiiii^^{fileproc}*^{klist}^{kqworkq}^{vnode}^{vnode}{?=[2Q]}{?=[2Q]}Q^{kqwllist}{?=[2Q]}Q^{klist}}^{pstats}{?=^{plimit}}{?=^{pgrp}}{sigacts=[32Q][32Q][32I]IIIIIIAIiiii}{?=[10Q]}iIIIIAIAIiiiIi{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}{itimerval={timeval=qi}{timeval=qi}}{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}ii^v^viIII^viiiICQQ{?=[2Q]}^{dtrace_ptss_page}^{dtrace_ptss_page_entry}^{dtrace_helpers}^{dof_ioctl_data}(?={?=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C][16C]ii}{proc_forkcopy_data=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C][16C]ii}){?=^{aio_workq_entry}^^{aio_workq_entry}}{?=^{aio_workq_entry}^^{aio_workq_entry}}{klist=^{knote}}^{rusage_superset}^{thread}^{thread}iSSQQiIQA^{workqueue}{timeval=qi}^v^vQQQQQQQQ{timeval=qi}CBBIiiiI{?=^{proc}^^{proc}}QQQQiiiiAIIQII^{os_reason}Q*}8"
- "B16@?0^{task={lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}[4^{ipc_port}]^{ipc_port}^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^{user_ldt}^vQQQi^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQIBBBBb4b4b4b4CCCC^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b17}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b29}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27b1b1b1b1b28^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}b16b1b1b1b1[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQ[16C]Q^{_vmobject_list_output_}Q^{vm_deferred_reclamation_metadata_s}}8"
- "Bridge interface enable segmentation"
- "DK: %s: instantiate failed 0x%x\n"
- "DK: %s::Dispatch kernel 0x%qx\n"
- "DK: %s::Dispatch kernel 0x%qx result 0x%x\n"
- "DK: %s::LoadModule 0x%x %s\n"
- "DK: %s::clientClose(%p)\n"
- "DK: %s::exit(%s)\n"
- "DK: %s::finalize(%p)\n"
- "DK: %s::finalize(%p) could not find fCheckInToken\n"
- "DK: %s::finalize(%p) dext was replaced, do not rematch current dext\n"
- "DK: %s::kill(%s)\n"
- "DK: %s::powerOff(%d) %d\n"
- "DK: %s::registerClass %s, %d, %d\n"
- "DK: %s::systemHalt()\n"
- "DK: %s::terminate(%s-0x%qx)\n"
- "DK: %s::terminate(%s-0x%qx) server exit before start()\n"
- "Debugger re-entry scheduled in %d milliseconds\n"
- "ESTABLISHED rfc5961 challenge ACK"
- "ESTABLISHED rfc5961 rate limited"
- "EXC_RESOURCE -> %s[%d] exceeded diag threshold limit: %d MB \n"
- "EXC_RESOURCE -> %s[%d] exceeded mem limit: %s%s %d MB (%s)\n"
- "IOPageableMapForAddress: null @%s:%d"
- "Invalid queue linkage: elt:%p next:%p next->prev:%p @%s:%d"
- "Invalid queue tail (early end): elt:%p tail:%p @%s:%d"
- "Invalid queue tail (element past end): elt:%p elt->next:%p @%s:%d"
- "KT_NOSHARED used w/o private accounting for view %s @%s:%d"
- "Kernel trap at 0x%016llx, type %d=%s, registers:\nCR0: 0x%016llx, CR2: 0x%016llx, CR3: 0x%016llx, CR4: 0x%016llx\nRAX: 0x%016llx, RBX: 0x%016llx, RCX: 0x%016llx, RDX: 0x%016llx\nRSP: 0x%016llx, RBP: 0x%016llx, RSI: 0x%016llx, RDI: 0x%016llx\nR8:  0x%016llx, R9:  0x%016llx, R10: 0x%016llx, R11: 0x%016llx\nR12: 0x%016llx, R13: 0x%016llx, R14: 0x%016llx, R15: 0x%016llx\nRFL: 0x%016llx, RIP: 0x%016llx, CS:  0x%016llx, SS:  0x%016llx\nFault CR2: 0x%016llx, Error code: 0x%016llx, Fault CPU: 0x%x%s%s%s%s, PL: %d, VF: %d\n"
- "L4S mode (0: disable, 1: enable L4S"
- "MACH_MAKE_MEMORY_ENTRY"
- "MACH_MEMORY_ENTRY_MAP_SIZE"
- "MADVISE"
- "MINCORE"
- "MINHERIT"
- "MMAP"
- "MPROTECT"
- "MREMAP_ENCRYPTED"
- "MSYNC"
- "MUNMAP"
- "Panic server returned error %d, retrying\n"
- "Routing through specified router IP %s (%d)\n"
- "SKMEM_SLAB_MEMBER(sl, buf)"
- "Sleep transition timed out after %d seconds"
- "Spurious inference as either tsecr (%u) doesn't lie between xmit_ts(%u) and now (%u) OR the rtt (%u) is less than base-rtt (%u). end_seq is:%u"
- "TE_SENDIPECT flag is set but TCP_L4S_ENABLED is not"
- "Telemetry: Allocation failed: %d\n"
- "Unexpected reclaim action %d @%s:%d"
- "VM_ALLOCATE_FIXED"
- "VM_BEHAVIOR_SET"
- "VM_DEALLOCATE"
- "VM_MAP_COPYIN"
- "VM_MAP_COPY_OVERWRITE"
- "VM_MAP_INHERIT"
- "VM_MAP_MACHINE_ATTRIBUTE"
- "VM_MAP_MSYNC"
- "VM_MAP_PAGE_RANGE_INFO"
- "VM_MAP_PAGE_RANGE_QUERY"
- "VM_MAP_PROTECT"
- "VM_MAP_READ_USER"
- "VM_MAP_UNWIRE"
- "VM_MAP_WRITE_USER"
- "VM_PAGE_PACK_PTR failed on &vm_pages[0] - %p @%s:%d"
- "VM_PAGE_PACK_PTR failed on &vm_pages[vm_pages_count-1] - %p @%s:%d"
- "VM_reclaim"
- "VSLOCK"
- "VSUNLOCK"
- "Wake transition timed out after %d seconds"
- "apple_protect_pager_data_request: vm_fault_page() unexpected error 0x%x\n @%s:%d"
- "bcast_mcast "
- "bootprofile_buffer_size"
- "bootprofile_init"
- "bootprofile_interval_ms"
- "bootprofile_proc_name"
- "bootprofile_stackshot_flags"
- "bootprofile_type"
- "bridge_dhcp_filter"
- "bridge_enqueue_multi"
- "bridge_forward"
- "bridge_host_filter"
- "bridge_ifp->if_bridge == NULL"
- "bridge_input"
- "bridge_interface_input"
- "cmd == DIOCOSFPGET"
- "com.apple.feth"
- "dst_ifp != NULL"
- "dummynet: heap_extract from middle not supported on this heap!!! @%s:%d"
- "dummynet: heap_extract, father %d out of bound 0..%d\n"
- "dyld_pager_data_request: vm_fault_page() unexpected error 0x%x\n @%s:%d"
- "fileproc_free"
- "fill"
- "gIOKitPageableFixed0"
- "gIOKitPageableFixed1"
- "gIOKitPageableFixed2"
- "gIOKitPageableFixed3"
- "hibernate_page_list_setall preflight pageCount %d est comp %qd setfile %qd min %qd\n"
- "icmp6_input"
- "interrupt-based sampling rate in Hz"
- "interrupt_sample_rate"
- "ip address: %d.%d.%d.%d\n"
- "ipc_object_copyin_from_kernel: strange rights @%s:%d"
- "ipc_object_copyout_dest: strange rights @%s:%d"
- "ipc_object_destroy: strange rights @%s:%d"
- "ipc_object_destroy_dest: strange rights @%s:%d"
- "ipc_right_copyout: strange rights @%s:%d"
- "ipc_right_delta: strange right %d for 0x%x (%p) in space:%p @%s:%d"
- "ipc_right_destroy: strange type @%s:%d"
- "kaudit_to_bsm returned %d @%s:%d"
- "kdp_crashdump_pkt_size is too large. Reverting to %d\n"
- "kdp_send: packet too large (%d > %u)"
- "kdp_set_dump_info: Skipping invalid panicd port %d (using %d)\n"
- "kill_idle_exit_proc: failed to allocate jetsam reason\n"
- "kmem_range_init: vm_map_locate_space failing for claim %s @%s:%d"
- "lck_mtx_lock_spinwait_x86 returned %d for mutex %p @%s:%d"
- "load_code_signature: %s: failed to allocate space for reason string (os_reason_alloc_buffer error: %d, kcdata error: %d, length: %ld)\n"
- "load_code_signature: %s: failed to copy reason string (kcdata_memcpy error: %d, length: %ld)\n"
- "low swap: attempt to unkill pid %d (%s) ignored\n"
- "low swap: killing largest compressed process with pid %d (%s) and size %llu MB\n"
- "low swap: killing pid %d (%s)\n"
- "low swap: resuming pid %d (%s)\n"
- "low swap: suspending pid %d (%s)\n"
- "low swap: throttling pid %d (%s)\n"
- "low swap: triggering no paging space action\n"
- "low swap: unable to find any eligible processes to take action on\n"
- "low swap: unthrottling pid %d (%s)\n"
- "m != NULL && t != NULL"
- "mac__call__proc_check_delegated_signal"
- "mac__rslt__proc_check_delegated_signal"
- "mbuf %p redzone violation with value 0x%x (instead of 0x%x, using cookie 0x%x)\n"
- "memorystatus: %s pid %d [%s] (%s %d) %lluKB - memorystatus_available_pages: %llu compressor_size:%u\n"
- "memorystatus: zone_map_is_exhausted=%d\n"
- "netagent_unregister_session_wrapper"
- "nicmp6 is NULL in %s, which isn't good! @%s:%d"
- "outif == NULL"
- "pid %d (%s) is unable to transmit packets on %s\n"
- "rfc5961 bad SYN challenge ack"
- "rfc5961 bad SYN rate limited"
- "segmentation"
- "shared."
- "shared.kalloc"
- "shared_region_pager_data_request: vm_fault_page() unexpected error 0x%x\n @%s:%d"
- "site.struct netagent_wrapper"
- "skmflag & (SKMEM_NOSLEEP | SKMEM_FAILOK)"
- "src_if == m->m_pkthdr.rcvif"
- "strange task flavor @%s:%d"
- "strange thread flavor @%s:%d"
- "tcp_connection_summary [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u Duration: %u.%03u sec Conn_Time: %u.%03u sec bytes in/out: %llu/%llu pkts in/out: %llu/%llu pkt rxmit: %u ooo pkts: %u dup bytes in: %u ACKs delayed: %u delayed ACKs sent: %u\nrtt: %u.%03u ms rttvar: %u.%03u ms base rtt: %u ms so_error: %d svc/tc: %u flow: 0x%x"
- "tcp_rack_update_segment_acked"
- "tcp_state_changed [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u "
- "telemetry_buffer_size"
- "telemetry_init"
- "telemetry_notification_leeway"
- "telemetry_sample_rate"
- "thread_wakeup_prim"
- "udp6_output: IPV6_V6ONLY option was set for a connected socket\n"
- "unable to check for loaded trust cache: interface not supported\n"
- "unable to get static trust cache capabilities: interface not supported\n"
- "unable to load static trust cache: interface not supported\n"
- "unknown kqwl thread qos update operation: %d @%s:%d"
- "vm_fault: unexpected error 0x%x from vm_fault_page()\n @%s:%d"
- "vm_page_bootstrap: %d free pages, %d wired pages, (up to %d of which are delayed free)\n"
- "vm_page_grab_options"
- "vm_reclaim: About to kill %p due to %d with subcode %lld\n @%s:%d"
- "vm_reclaim: Skipping non fatal guard exception.\n"
- "vm_reclaim: Unable to deallocate 0x%llx (%u) from 0x%llx err=%d\n"
- "vm_reclaim: Userspace modified head or busy pointer! head: %llu (0x%llx) != busy: %llu (0x%llx) | tail = %llu (0x%llx)\n"
- "vm_reclaim: Userspace modified head or tail pointer! head: %llu (0x%llx) > tail: %llu (0x%llx) | busy = %llu (0x%llx)\n"
- "vm_reclaim: enquequeing %d for asynchronous reclamation.\n"
- "vm_reclaim: failed to allocate VA for reclaim buffer (%d) - %s [%d]\n"
- "vm_reclaim: failed to initialize vmdr buffer - reclaim is disabled (%llu)\n"
- "vm_reclaim: unable to free(reusable) 0x%llx (%u) for pid %d err=%d\n"
- "vm_reclaim_chunk"

```
