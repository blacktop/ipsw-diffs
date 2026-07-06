## kernel

> `/System/Library/Kernels/kernel`

```diff

-  __TEXT.__text: 0x8fa190
-  __TEXT.__const: 0x45380
-  __TEXT.__os_log: 0x4b71b
-  __TEXT.__cstring: 0xa1e3e
+  __TEXT.__text: 0x900ed0
+  __TEXT.__const: 0x45460
+  __TEXT.__os_log: 0x4bfcb
+  __TEXT.__cstring: 0xa29ae
   __TEXT.__eh_frame: 0x118
-  __DATA.__lock_grp: 0x162e8
-  __DATA.__data: 0x82b40
-  __DATA.__percpu: 0x3e18
-  __DATA.__common: 0x1bdd50
-  __DATA.__bss: 0x7e5f0
-  __DATA_CONST.__const: 0xa3668
-  __DATA_CONST.__kalloc_type: 0x17ac0
-  __DATA_CONST.__kalloc_var: 0x7e90
-  __DATA_CONST.__assert: 0xf3c
+  __DATA.__lock_grp: 0x16430
+  __DATA.__data: 0x82bc0
+  __DATA.__percpu: 0x3e28
+  __DATA.__common: 0x1bdd20
+  __DATA.__bss: 0x86910
+  __DATA_CONST.__const: 0xa29b8
+  __DATA_CONST.__kalloc_type: 0x17b00
+  __DATA_CONST.__kalloc_var: 0x7ee0
+  __DATA_CONST.__assert: 0xd34
   __DATA_CONST.__kern_brk_desc: 0x60
-  __DATA_CONST.__sdt_cstring: 0x71f2
-  __DATA_CONST.__sdt: 0xf228
+  __DATA_CONST.__sdt_cstring: 0x7232
+  __DATA_CONST.__sdt: 0xf2b8
   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
-  __KLDDATA.__init: 0x11c30
-  __KLDDATA.__init_entry_set: 0x14190
-  __KLDDATA.__const: 0x9360
+  __KLDDATA.__init: 0x11c80
+  __KLDDATA.__init_entry_set: 0x13de8
+  __KLDDATA.__const: 0x93e0
   __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__cstring: 0x79c
   __KLDDATA.__mod_init_func: 0x8

   __HIB.__bss: 0x200
   __HIB.__common: 0x114
   __VECTORS.__recover: 0x150
-  __KLD.__text: 0x11c7e
+  __KLD.__text: 0x11c6e
   __LAST.__last: 0x0
   __LASTDATA_CONST.__mod_init_func: 0x8
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __LINKINFO.__symbolsets: 0x4e2c5
-  __CTF.__ctf: 0xd8146
-  Functions: 27052
-  Symbols:   24275
-  CStrings:  26411
+  __CTF.__ctf: 0xd351a
+  Functions: 27097
+  Symbols:   24331
+  CStrings:  26493
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__kern_brk_desc : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__got : content changed
~ __KLDDATA.__static_ifinit : content changed
~ __KLDDATA.__mod_init_func : content changed
~ __KLDDATA.__mod_term_func : content changed
~ __HIB.__cstring : content changed
~ __LASTDATA_CONST.__mod_init_func : content changed
Symbols:
+ __ZN16IOPlatformExpert17setInterruptWakesEj
+ __ZN21IOInterruptController16registerInternalEv
+ __ZN21IOInterruptController17setInterruptWakesEj
+ __ZN21IOInterruptController19claimInterruptWakesEPNS_11APWakeStateE
+ __ZN9IOService10isOnForAOTEv
+ __ca_event_format_vm_page_event
+ __ca_event_format_vm_zero_wired_pages
+ __kind_track_by_cpu
+ __track_by_kind
+ _c_age_count
+ _c_age_list_head
+ _c_bad_count
+ _c_bad_list_head
+ _c_early_swapout_count
+ _c_early_swapout_list_head
+ _c_early_swappedin_count
+ _c_early_swappedin_list_head
+ _c_empty_count
+ _c_filling_count
+ _c_filling_list_head
+ _c_late_swapout_count
+ _c_late_swapout_list_head
+ _c_late_swappedin_count
+ _c_late_swappedin_list_head
+ _c_major_count
+ _c_major_list_head
+ _c_minor_count
+ _c_minor_list_head
+ _c_regular_swapout_count
+ _c_regular_swapout_list_head
+ _c_regular_swappedin_count
+ _c_regular_swappedin_list_head
+ _c_swapio_count
+ _c_swapio_list_head
+ _c_swappedout_count
+ _c_swappedout_list_head
+ _c_swappedout_sparse_count
+ _c_swappedout_sparse_list_head
+ _compaction_swapper_awakened
+ _flow_mgr_clear_embedded_scope_id
+ _flow_mgr_flow_get_af_sport
+ _gIOWakeSourceInterruptController
+ _icmp_fraglimit
+ _icmp_fragtimeout
+ _kdebug_is_secure
+ _mac_proc_check_service_port_derive
+ _memorystatus_respond_to_wired_mem_exhaustion
+ _memstat_wired_max_proc_pct
+ _rbbr_drain_gain
+ _rbbr_drain_probe_rtt_gain
+ _rbbr_low_utilization_thresh
+ _rbbr_queue_detect_drop_pct
+ _rbbr_queue_detect_fraction_pct
+ _rbbr_queue_detect_increases
+ _rbbr_queue_detect_noise_base_ms
+ _rbbr_queue_detect_noise_mad_mult
+ _rbbr_startup_gain
+ _recount_cpu_kind_index
+ _sysctl_handle_int_rd_trunc
+ _sysctl_handle_quad_rd_trunc
+ _task_get_proc_uniqueid
+ _task_get_uniqueid
+ _tcp_log_bbr
+ _vm_compressor_pool_size
+ _vm_compressor_swapout_conditions_met
+ _vm_fault_copy_begin_backoff_threshold
+ _vm_fault_copy_collisions_bailout_threshold
+ _vm_global_wire_exhaustion_limit
+ _vm_mem_entry_wimg_non_writable
+ _vm_page_telemetry_emit
+ _vm_page_telemetry_emit_zwp
+ _vm_pressure_level_transition_threshold
+ _vm_swap_file_max_size
+ _vm_swap_file_min_size
+ _vm_wired_mem_in_exhaustion
- __topo_cpu_kinds
- _c_compactor_backoff_ns
- _c_major_fragmentation_threshold_mb
- _c_major_fragmentation_threshold_pct
- _c_minor_list
- _c_queues
- _cswap_trigger_cond
- _cswap_trigger_gate
- _cswap_trigger_thread
- _get_task_uniqueid
- _mac_proc_notify_service_port_derive
- _mach_absolute_speculative_time
- _memorystatus_lock_group
- _memorystatus_wait_for_healthy_system
- _memstat_policy_mtx
- _swap_bytes_used
- _vm_compressor_pages_occupied
- _vm_pressure_notification_backoff_abs
- _vm_pressure_notification_backoff_sec
CStrings:
+ "%s: PKTP_CMD_FILTER_GET copyout - error %d"
+ "%s: PKTP_CMD_FILTER_SET validate - error %d"
+ "%s: bpf%u already attached to %s error %d"
+ "%s: bpf%u and bpf%u have incompatible flags 0x%x != 0x%x error %d"
+ "%s: bpf%u and bpf%u have incompatible interfaces %s and %s error %d"
+ "%s: d_from is closing or detached error %d"
+ "%s: d_to is closing or detaching error %d"
+ "%s: downgrading VM entry [%p, %p) from JIT to non-JIT"
+ "%s: droptap mbuf shorter than DROPTAP_HDR_SIZE (%zu)"
+ "%s: droptap mbuf too short (%zu < %zu)"
+ "%s: interface %s not supported error %d"
+ "%s: invalid pth_length %zu (pkt %zu)"
+ "%s: mbuf_copydata droptap prefix failed %d"
+ "%s: mbuf_copydata droptap_header failed %d"
+ "%s: proc %s[%d] uses FSIOC_SET_FSTYPENAME_OVERRIDE\n"
+ "%s: refusing NDP update from %s on %s claiming our own link-layer address\n"
+ "%{public}s:%d pid %d (%{public}s) is unable to transmit packets on %{public}s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/dev/dtrace/dtrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/kern_control.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/kern_event.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/kpi_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/kpi_socket.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/kpi_socketfilter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/socket_flows.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/subr_eventhandler.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/sys_domain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/tracker.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_domain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_mbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_mbuf2.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_proto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_socket.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_socket2.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/uipc_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/kern/vsock_domain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/aop/kpi_aop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/bpf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/classq/classq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/classq/classq_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/content_filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/dlil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/dlil_ctl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/dlil_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/dlil_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/dlil_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/droptap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/flowadv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_bond.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_bridge.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_fake.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_ipsec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_llreach.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_loop.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_ports_used.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_redirect.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_utun.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/if_vlan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/kpi_interface.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/mblist.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/nat464_utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/ndrv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/necp_client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/net_thread_marks.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/network_agent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/ntstat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/nwk_wq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf_if.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf_ioctl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf_norm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf_pbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pf_table.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pktap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pktsched/pktsched.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/pktsched/pktsched_ops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/route.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/net/rtsock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/cpu_in_cksum_gen.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/flow_divert.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/igmp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_arp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_mcast.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_pcb.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_proto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_rmx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/in_tclass.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/ip_dummynet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/ip_encap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/ip_icmp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/ip_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/ip_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mp_pcb.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mp_pcb.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mp_proto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp_opt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/mptcp_var.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/raw_ip.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_ack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_cache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_cubic.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_fastopen.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_handshake.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_ledbat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_mss.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_prague.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_rtt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_sack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_segment.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_subr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_timer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/tcp_utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet/udp_usrreq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ah_core.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ah_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ah_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/esp_core.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/esp_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/esp_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/esp_rijndael.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/frag6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/icmp6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_cga.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_ifattach.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_mcast.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_pcb.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_proto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_rmx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/in6_src.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ip6_forward.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ip6_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ip6_input.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ip6_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ipsec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/ipsec.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/mld6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6_nbr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6_rti.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6_rtr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/nd6_send.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/scope6.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netinet6/udp6_output.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netkey/key.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/netkey/keysock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/channel/channel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/core/skywalk.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/core/skywalk_var.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/namespace/netns.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/namespace/protons.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule_eth.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule_inet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/iokit/Kernel/IOHibernateRestoreKernel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/osfmk/i386/cpu_threads.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/osfmk/x86_64/xcpm/xcpm_config.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/osfmk/x86_64/xcpm/xcpm_dvfs.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/osfmk/x86_64/xcpm/xcpm_idle.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uweP7r/Sources/xnu/osfmk/x86_64/xcpm/xcpm_ioctl.c"
+ "111222222222222222222222222222222222222222222222222222"
+ "122122"
+ "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122111111111112222222222222222222222222222222222222222222222222222222112222222121122222222222221211122222222222222212222221122222122222222222222212211111112222222222222"
+ "BIOCSETIF"
+ "BIOCSEXTHDR"
+ "BIOCSPKTHDRV2"
+ "BIOCSTRUNCATE"
+ "CRUISE"
+ "DRAIN"
+ "DRAIN_PROBE_RTT"
+ "Disable INTCOPROC ifioctl restrictions (DEBUG/DEVELOPMENT-writable; exists so darwintests can briefly clear INTCOPROC subfamily on a synthetic feth long enough to destroy it during T_ATEND cleanup)"
+ "ICMP/ICMPv6 fragment reassembly timeout (seconds)"
+ "Maximum fragments per ICMP/ICMPv6 packet"
+ "Number of (early) ready-to-swap segments"
+ "Number of (early) swapped-in segments"
+ "Number of (late) ready-to-swap segments"
+ "Number of (late) swapped-in segments"
+ "Number of (non-sparse) swapped-out segments"
+ "Number of (regular) ready-to-swap segments"
+ "Number of (regular) swapped-in segments"
+ "Number of (sparse) swapped-out segments"
+ "Number of aging segments"
+ "Number of bad segments"
+ "Number of empty segments"
+ "Number of filling segments"
+ "Number of recently-compacted segments"
+ "Number of swapping-out segments"
+ "PROBE_RTT"
+ "PROBE_RWND"
+ "Receive-side CC for BG traffic (rBBR=1 or rLEDBAT=2)"
+ "SK[%u]: %-30s %s(%d) failed to validate flow_uuid %s (err %d)\n"
+ "SK[%u]: %-30s %s(%d) flags 0x%x start %u stuff %u len %u headroom %u\n"
+ "SK[%u]: %-30s Unable to get address family\n"
+ "SK[%u]: %-30s can't find flow %s\n"
+ "SK[%u]: %-30s fe %s %snon_via %d withdrawn %d\n"
+ "TRACKER - %s:%d Could not dump entries, entry tlv size %lu exceeds scratch pad size %lu\n"
+ "TRACKER - %s:%d Could not dump entry, buffer too small\n"
+ "The current number of allocated swapfiles"
+ "The maximum number of swapfiles that can be allocated"
+ "The maximum size (in bytes) of each swapfile"
+ "The minimum size (in bytes) of each swapfile"
+ "VM Swap Subsystem is ON\n"
+ "Whether ktrace ownership requires entitlement on non-macOS."
+ "_dmaReferences overflow @%s:%d"
+ "allocated_bytes_hwm"
+ "aotSleep at %04d/%02d/%d %02d:%02d:%02d\n"
+ "aotWake at %04d/%02d/%d %02d:%02d:%02d\n"
+ "ap-wake-interrupts"
+ "c_seg %p has bad c_state = %d @%s:%d"
+ "c_seg %p requesting bad c_state = %d @%s:%d"
+ "clearing recv_bg bg_throttle=%d is_local=%d"
+ "connection:0x00000001 rtt:0x00000002 ka:0x00000004 log:0x00000008 loop:0x00000010 local:0x00000020 gw:0x00000040 syn:0x00000100 fin:0x00000200 rst:0x00000400 dropnecp:0x00001000 droppcb:0x00002000 droppkt:0x00004000 fswflow:0x00008000 state:0x00010000 synrxmt:0x00020000 output:0x00040000 bind:0x00080000 bbr:0x00100000 "
+ "enabling recv_bg (BE throttle) be_throttle=%d is_local=%d"
+ "enabling recv_bg bg_throttle=%d bg_sys=%d is_local=%d"
+ "fe_log_conflicting"
+ "fe_log_entry"
+ "fe_log_index_alloc"
+ "flow_entry_destroy"
+ "flow_mgr_flow_get_af_sport"
+ "flow_req_validate"
+ "fraglimit"
+ "fragtimeout"
+ "fsctl_internal"
+ "fsw_log_uuid_collision"
+ "global_wire_exhaustion_limit"
+ "inp_restricted_recv"
+ "intcoproc_unrestricted"
+ "kif->pfik_ifp == NULL || kif->pfik_ifp == ifp"
+ "kif->pfik_ifp == ifp"
+ "mac__call__proc_check_service_port_derive"
+ "mac__call__vnode_check_readlink2"
+ "mac__rslt__proc_check_service_port_derive"
+ "mac__rslt__vnode_check_readlink2"
+ "majorcompact"
+ "mem_entry_wimg_non_writable"
+ "memorystatus: %s [%d] has %llu%% of wired memory (%llu MiB of %llu MiB total wired), killing\n\n"
+ "memorystatus: top wired consumer pid %d has %llu MiB wired (<%llu%% of total wired), showing dialog\n\n"
+ "memorystatus: triggering wired memory exhaustion action\n\n"
+ "memorystatus: wired memory exhaustion - sending out-of-application memory knote\n\n"
+ "memorystatus: {\"compressor_exhausted\": %d, \"zone_map_is_exhausted\": %d, \"swap_low\": %d, \"swap_exhausted\": %d, \"wired_mem_exhaustion\": %d}\n"
+ "nd6_na_input: tgt lladdr equals own lladdr for %s on %s\n"
+ "nd6_ns_input: src lladdr equals own lladdr from %s on %s\n"
+ "no_linger "
+ "option section too small"
+ "pf: BAD ICMP %d:%d outer dst != inner src\n"
+ "pid %d (%s) is unable to receive packets on %s"
+ "pid %d (%s) is unable to transmit packets on %s"
+ "rBBR DRAIN gain as percentage (75 = 0.75x) after failed PROBE_RWND"
+ "rBBR DRAIN_PROBE_RTT gain as percentage (75 = 0.75x) before entering PROBE_RTT"
+ "rBBR MAD multiplier for noise threshold"
+ "rBBR PROBE_RTT interval in seconds"
+ "rBBR base noise threshold (ms) for RTT increase detection"
+ "rBBR minimum consecutive RTT increases to form valid sawtooth chain"
+ "rBBR minimum fraction (%) of CRUISE cycles in sawtooth to detect competition"
+ "rBBR percentage drop in RTT to detect queue drain (sawtooth reset)"
+ "rBBR pre-congestion PROBE_RWND gain as percentage (200 = 2.0x exponential growth)"
+ "rBBR sender utilization threshold (%) below which RWND growth is suppressed"
+ "rbbr: CRUISE backoff old_win=%u new_win=%u backoff_count=%u median_rtt=%u rtt_mad=%u delay_threshold=%u"
+ "rbbr: CRUISE delay exceeded median_delay=%u delay_threshold=%u win=%u rwnd_est=%u"
+ "rbbr: PROBE_RWND delay exceeded cycle=%u median_delay=%u delay_threshold=%u win=%u rwnd_est=%u"
+ "rbbr: enter CRUISE win=%u rwnd_est=%u median_rtt=%u rtt_mad=%u delay_thresh=%u backoff_count=%u"
+ "rbbr: enter DRAIN win=%u rwnd_est=%u median_rtt=%u delay_thresh=%u"
+ "rbbr: enter DRAIN_PROBE_RTT win=%u rwnd_est=%u median_rtt=%u queue_competition=%u sawtooth_cycles=%u"
+ "rbbr: enter PROBE_RTT win=%u rwnd_est=%u skip_restrict=%u next_probe=%u"
+ "rbbr: enter PROBE_RWND win=%u rwnd_est=%u delay_thresh=%u median_rtt=%u rtt_mad=%u"
+ "rbbr: exit %s -> %s dur=%ums median_rtt=%u rtt_mad=%u delay_thresh=%u rwnd_est=%u win=%u win_ws=%u samples=%u skip_restrict=%u"
+ "rbbr: low utilization bytes_rcvd=%llu expected=%llu measure_ms=%u win=%u cycle_rtt=%u median_rtt=%u"
+ "rbbr: queue competition detected, skipping RWND restrict sawtooth_cycles=%u total_cycles=%u fraction=%u%% threshold=%u%%"
+ "rbbr: resuming RWND restriction"
+ "rbbr_apply_cruise_backoff"
+ "rbbr_drain_gain"
+ "rbbr_drain_probe_rtt_gain"
+ "rbbr_enter_cruise"
+ "rbbr_enter_drain"
+ "rbbr_enter_drain_probe_rtt"
+ "rbbr_enter_probe_rtt"
+ "rbbr_enter_probe_rwnd"
+ "rbbr_finalize_sawtooth_detection"
+ "rbbr_log_phase_end"
+ "rbbr_low_utilization_thresh"
+ "rbbr_process_probe_rwnd_cycle"
+ "rbbr_queue_detect_drop_pct"
+ "rbbr_queue_detect_fraction_pct"
+ "rbbr_queue_detect_increases"
+ "rbbr_queue_detect_noise_base_ms"
+ "rbbr_queue_detect_noise_mad_mult"
+ "rbbr_sender_utilizing_rwnd"
+ "rbbr_startup_gain"
+ "rbbr_update_phase"
+ "remote virtual interface"
+ "rvi_getdrvspec"
+ "rvi_setdrvspec"
+ "setInterruptWakes %p\n"
+ "set_tcp_stream_priority"
+ "site.struct tcp_rbbr_state"
+ "supports droptap"
+ "swapfile_cnt"
+ "swapfile_limit"
+ "swapfile_size_max"
+ "swapfile_size_min"
+ "switching to %s bg=%d recv_cc_algo=%u"
+ "tcp_bbr (%s:%d) [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u %s"
+ "tcp_set_recv_bg"
+ "used_bytes_hwm"
+ "vm: Maximum number of VM swap files: %d\n"
+ "vm_map_copyout_update_entry"
+ "vm_map_remap"
+ "vm_page_telemetry.c"
+ "vm_page_telemetry: failed to allocate drain thread @%s:%d"
+ "vm_page_telemetry_init"
+ "vm_pressure_level_transition_threshold"
+ "vm_shared_region_slide_sanity_check_v5: page_starts[%u] exceeds valid range. %u > %lu\n"
+ "vm_shared_region_slide_sanity_check_v5: page_starts[%u] is not aligned. %u\n"
+ "wired-mem-exhaustion"
+ "wired_max_proc_pct"
- "%s: d_from is closing error %d"
- "%s: d_to is closing error %d"
- "%s:%d pid %d (%s) is unable to transmit packets on %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/nexus_common.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Binaries/xnu/install/TempContent/Objects/EXPORT_HDRS/bsd/skywalk/packet_common.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/dev/dtrace/dtrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/kern_control.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/kern_event.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/kpi_mbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/kpi_socket.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/kpi_socketfilter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/socket_flows.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/subr_eventhandler.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/sys_domain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/tracker.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_domain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_mbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_mbuf2.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_proto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_socket.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_socket2.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_syscalls.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/uipc_usrreq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/kern/vsock_domain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/aop/kpi_aop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/bpf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/classq/classq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/classq/classq_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/classq/classq_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/content_filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/dlil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/dlil_ctl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/dlil_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/dlil_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/dlil_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/droptap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/flowadv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_bond.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_bridge.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_fake.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_ipsec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_llreach.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_loop.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_ports_used.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_redirect.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_utun.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/if_vlan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/kpi_interface.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/mblist.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/nat464_utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/ndrv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/necp_client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/net_thread_marks.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/network_agent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/ntstat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/nwk_wq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf_if.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf_ioctl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf_norm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf_pbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pf_table.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pktap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pktsched/pktsched.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pktsched/pktsched_fq_codel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pktsched/pktsched_netem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/pktsched/pktsched_ops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/route.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/net/rtsock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/cpu_in_cksum_gen.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/flow_divert.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/igmp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_arp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_mcast.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_pcb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_proto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_rmx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/in_tclass.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/ip_dummynet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/ip_encap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/ip_icmp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/ip_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/ip_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/kpi_ipfilter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mp_pcb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mp_pcb.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mp_proto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp_opt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp_timer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/mptcp_var.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/raw_ip.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_ack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_cache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_cubic.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_fastopen.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_handshake.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_ledbat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_mss.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_prague.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_rtt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_sack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_segment.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_subr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_timer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/tcp_utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet/udp_usrreq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ah_core.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ah_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ah_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/esp_chachapoly.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/esp_core.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/esp_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/esp_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/esp_rijndael.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/frag6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/icmp6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_cga.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_ifattach.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_mcast.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_pcb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_proto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_rmx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/in6_src.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ip6_forward.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ip6_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ip6_input.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ip6_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ipsec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/ipsec.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/mld6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6_nbr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6_prproxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6_rti.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6_rtr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/nd6_send.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/scope6.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netinet6/udp6_output.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netkey/key.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/netkey/keysock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/channel/channel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/channel/channel_kern.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/channel/channel_ring.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/channel/channel_syscalls.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/core/skywalk.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/core/skywalk_var.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/lib/net_filter_event.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem_arena.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem_cache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem_cache_var.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem_region.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/mem/skmem_slab.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/namespace/flowidns.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/namespace/netns.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/namespace/protons.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_agg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_classifier.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_entry.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_manager.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_owner.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_route.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_stats.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_track.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/flow/flow_var.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_dp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ethernet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_ip_frag.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/fsw_vp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/flowswitch/nx_flowswitch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/kpipe/nx_kernel_pipe.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_compat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_compat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_native.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_filter_vp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_flow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_gso.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_host.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_llink.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_mit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_poll.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/netif/nx_netif_vp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_adapter.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_kern.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_mbq.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_pktq.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule_eth.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/nexus_traffic_rule_inet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/nexus/upipe/nx_user_pipe.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/packet/packet_copy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/packet/packet_kern.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/packet/pbufpool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/bsd/skywalk/packet/pbufpool_kern.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/iokit/Kernel/IODeviceTreeSupport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/iokit/Kernel/IOHibernateRestoreKernel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/osfmk/i386/cpu_threads.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/osfmk/x86_64/xcpm/xcpm_config.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/osfmk/x86_64/xcpm/xcpm_dvfs.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/osfmk/x86_64/xcpm/xcpm_idle.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.sypYlJ/Sources/xnu/osfmk/x86_64/xcpm/xcpm_ioctl.c"
- "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122111111111112222222222222222222222222222222222222222222222222222222112222222121122222222222221211122222222222222212222221122222122222222222222222222222222222222222222222222222222222211111112222222222222"
- "Aging"
- "Agingbytes of compressed data"
- "Agingbytes used to store compressed data"
- "Bad"
- "Badbytes of compressed data"
- "Badbytes used to store compressed data"
- "Empty"
- "Emptybytes of compressed data"
- "Emptybytes used to store compressed data"
- "Filling"
- "Fillingbytes of compressed data"
- "Fillingbytes used to store compressed data"
- "Major-compacted"
- "Major-compactedbytes of compressed data"
- "Major-compactedbytes used to store compressed data"
- "Maximum number of VM swap files: %d\n"
- "Receive background CC algorithm (0=rLEDBAT, 1=rBBR)"
- "SK[%u]: %-30s %s(%d) flags 0x%x start %u stuff %u len %u\n"
- "SK[%u]: %-30s can't find flow\n"
- "SK[%u]: %-30s fe \"%s\" [fo %p] non_via %d withdrawn %d\n"
- "Segments queued for minor compaction"
- "Swap I/O"
- "Swap I/Obytes of compressed data"
- "Swap I/Obytes used to store compressed data"
- "Swapout (early)"
- "Swapout (early)bytes of compressed data"
- "Swapout (early)bytes used to store compressed data"
- "Swapout (late)"
- "Swapout (late)bytes of compressed data"
- "Swapout (late)bytes used to store compressed data"
- "Swapout (regular)"
- "Swapout (regular)bytes of compressed data"
- "Swapout (regular)bytes used to store compressed data"
- "Swapped-in (early)"
- "Swapped-in (early)bytes of compressed data"
- "Swapped-in (early)bytes used to store compressed data"
- "Swapped-in (late)"
- "Swapped-in (late)bytes of compressed data"
- "Swapped-in (late)bytes used to store compressed data"
- "Swapped-in (regular)"
- "Swapped-in (regular)bytes of compressed data"
- "Swapped-in (regular)bytes used to store compressed data"
- "Swapped-out & sparse"
- "Swapped-out & sparsebytes of compressed data"
- "Swapped-out & sparsebytes used to store compressed data"
- "Swappedout"
- "Swappedoutbytes of compressed data"
- "Swappedoutbytes used to store compressed data"
- "The number of bytes in compressor physical pages lost to fragmentation"
- "The number of bytes in the swapfile which hold data"
- "The number of bytes used to store compressed data (excluding fragmentation)"
- "The number of physical pages used to store compressed data"
- "The total number of times cswap_trigger has been awoken"
- "VM Compressor Swapper Wakeup Stats"
- "VM Swapfile Statistics"
- "bpf_setif"
- "bytes_inuse"
- "bytes_unused"
- "connection:0x00000001 rtt:0x00000002 ka:0x00000004 log:0x00000008 loop:0x00000010 local:0x00000020 gw:0x00000040 syn:0x00000100 fin:0x00000200 rst:0x00000400 dropnecp:0x00001000 droppcb:0x00002000 droppkt:0x00004000 fswflow:0x00008000 state:0x00010000 synrxmt:0x00020000 output:0x00040000 bind:0x00080000 "
- "external_q_throttled"
- "flow_entry_teardown"
- "fragmentation_detected"
- "free_below_reserved"
- "label.io_state == IO_STATE_IN_SPACE"
- "mac__call__proc_notify_service_port_derive"
- "mac__rslt__proc_notify_service_port_derive"
- "major"
- "max_allocated_bytes"
- "max_used_bytes"
- "memorystatus: {\"compressor_exhausted\": %d, \"zone_map_is_exhausted\": %d, \"swap_low\": %d, \"swap_exhausted\": %d}\n"
- "minor"
- "minor_compactions"
- "occupied_bytes"
- "pages_occupied"
- "pid %d (%s) is unable to receive packets on %s\n"
- "rBBR PROBE_RTT interval in seconds (rounded to factor of 60: 5,10,15,20,30,60)"
- "scavenger"
- "segment count"
- "swap_bytes_inuse"
- "swap_threshold_exceeded"
- "swapfile"
- "swapins_defrag"
- "swapins_reclaim"
- "swapouts_under_300s"
- "swapouts_under_30s"
- "swapouts_under_60s"
- "target_age"
- "thrashing_detected"
- "vm: VM Swap Subsystem is ON\n"
- "wakeups"

```
