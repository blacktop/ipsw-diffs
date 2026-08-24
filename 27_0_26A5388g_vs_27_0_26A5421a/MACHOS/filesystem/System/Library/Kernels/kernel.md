## kernel

> `/System/Library/Kernels/kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__sdt_cstring`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__got`
- `__KLDDATA.__init`
- `__KLDDATA.__static_ifinit`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`

```diff

-13432.0.94.501.4
-  __TEXT.__text: 0x903790
-  __TEXT.__const: 0x45820
-  __TEXT.__os_log: 0x4c23b
-  __TEXT.__cstring: 0xa2b2f
+13432.1.9.0.0
+  __TEXT.__text: 0x905730
+  __TEXT.__const: 0x45780
+  __TEXT.__os_log: 0x4c2eb
+  __TEXT.__cstring: 0xa336d
   __TEXT.__eh_frame: 0x118
   __DATA.__lock_grp: 0x16578
   __DATA.__data: 0x82bc0
   __DATA.__percpu: 0x3e28
-  __DATA.__common: 0x1bdd60
-  __DATA.__bss: 0x86910
-  __DATA_CONST.__const: 0xa2ba8
+  __DATA.__common: 0x1bddb0
+  __DATA.__bss: 0x86930
+  __DATA_CONST.__const: 0xa3498
   __DATA_CONST.__kalloc_type: 0x17b00
   __DATA_CONST.__kalloc_var: 0x7ee0
-  __DATA_CONST.__assert: 0xe60
+  __DATA_CONST.__assert: 0xe4c
   __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__sdt_cstring: 0x7232
-  __DATA_CONST.__sdt: 0xf2b8
+  __DATA_CONST.__sdt: 0xf348
   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
   __KLDDATA.__init: 0x11d40
-  __KLDDATA.__init_entry_set: 0x14010
-  __KLDDATA.__const: 0x93e0
+  __KLDDATA.__init_entry_set: 0x142e0
+  __KLDDATA.__const: 0x9470
   __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__cstring: 0x79c
   __KLDDATA.__mod_init_func: 0x8

   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __LINKINFO.__symbolsets: 0x4e2fa
-  __CTF.__ctf: 0xd3992
-  Functions: 27109
-  Symbols:   24359
-  CStrings:  25986
+  __CTF.__ctf: 0xd3d96
+  Functions: 27124
+  Symbols:   24380
+  CStrings:  26045
 
Symbols:
+ _c_age_oldest_ts
+ _c_compactor_backoff_ns
+ _c_major_fragmentation_threshold_mb
+ _c_major_fragmentation_threshold_pct
+ _c_major_oldest_ts
+ _cswap_trigger_cond
+ _cswap_trigger_gate
+ _cswap_trigger_thread
+ _get_task_conclave_mem_limit
+ _memory_object_mark_read_only
+ _rbbr_cruise_cycles
+ _rbbr_cycle_rtts
+ _rbbr_reprobe_gain
+ _rbbr_round_min_ms
+ _rbbr_rtt_probe_cycle_rtts
+ _rbbr_rtt_probe_max_duration
+ _rbbr_rtt_probe_plateau_rounds
+ _rbbr_startup_cycle_rtts
+ _sdk_27_0_or_later
+ _vm_compressor_pages_occupied
+ _vm_compressor_set_size
+ _vm_object_pagers_trusted
+ _vm_object_readonly_copy_overwrite
+ _vm_object_readonly_fault
+ _vm_object_readonly_fault_page
+ _vm_object_readonly_iopl_request
- _compaction_swapper_awakened
- _compute_swapout_target_age
- _if_connection_not_idle_reason
- _vm_compressor_pool_size
- _vm_compressor_swapout_conditions_met
CStrings:
+ " [loaded at 0x%08x]"
+ "%s:%d CFIL: Handled previously delayed socket for TCP time wait\n"
+ "%s:%d CFIL: Marked previoulsy delayed socket as DEAD\n"
+ "121221121112"
+ "2211121111111222221112221222212222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111211222222222112222222222221121222122222122222222222222222222222222221121111222222222222221111212211222112221122211222222112222222222222222222222211112212212222222222122122122221111222222222222222221122222222222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
+ "B16@?0^{task={lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^{user_ldt}^vQQQi^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCC^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}b16b1b1b1b1b1b1b1b2b1b6[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
+ "Count"
+ "Lockdown Mode state (public)"
+ "MAIN"
+ "Network.ARPEvent"
+ "Network.EAPOLPacket"
+ "Network.ND6Event"
+ "Network.RAevent"
+ "Network.UDPMagicPacket"
+ "Network.fragment"
+ "Post-boot loaded kexts:\n"
+ "REPROBE"
+ "STARTUP"
+ "The total number of times cswap_trigger has been awoken"
+ "VM Compressor Swapper Wakeup Stats"
+ "VM object is read-only (decmpfs?)\n"
+ "VM_KERN_COUNT_WIRED_DYNAMIC"
+ "baseband.NotIdle"
+ "baseband.fragment"
+ "bt.NotIdle"
+ "bt.fragment"
+ "cfil_sock_service_delayed_dead_actions"
+ "com.apple.developer.lockdown-mode.state"
+ "connection.NotIdle"
+ "external_q_throttled"
+ "fragmentation_detected"
+ "free_below_reserved"
+ "fsw_dev_input_netem_enqueue"
+ "lockdown_mode_state_public"
+ "minor_compactions"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
+ "rBBR CRUISE backoff factor as percentage (90 = 0.90x) when delay exceeded"
+ "rBBR CRUISE monitoring actions before looping back to PROBE_RWND (0 = never)"
+ "rBBR CRUISE reprobe probe gain as percentage (110 = 1.10x)"
+ "rBBR PROBE_RTT RWND in MSS units (also the min window floor)"
+ "rBBR PROBE_RTT maximum duration in ms (cap while waiting for median RTT to plateau)"
+ "rBBR RTT rounds per action after first congestion"
+ "rBBR RTT rounds per action during slow start (before first congestion)"
+ "rBBR RTT rounds per per-round median during PROBE_RTT"
+ "rBBR consecutive non-improving PROBE_RTT rounds to declare the RTT plateaued"
+ "rBBR floor on one RTT round in ms (guards very low-RTT paths)"
+ "rBBR max CRUISE backoffs per phase (default 2)"
+ "rBBR minimum RWND in MSS units (UNUSED; the real window floor is rbbr_rtt_probe_rwnd_mss via rbbr_min_win)"
+ "rBBR sender utilization threshold (%) of RWND that must be in flight to allow RWND growth"
+ "rBBR wall-clock fallback cycle duration in ms (PROBE_RWND/CRUISE; used only when TS/SRTT unavailable — primary cadence is the RTT-round data-clock)"
+ "rbbr: CRUISE cycle median_delay=%u delay_threshold=%u win=%u rwnd_est=%u samples=%u"
+ "rbbr: PROBE_RTT round median=%u min=%u flat=%u n=%u elapsed=%u adv_win=%u win=%u"
+ "rbbr: PROBE_RWND cycle=%u NO SAMPLES win=%u rwnd_est=%u cycle_bytes=%llu"
+ "rbbr: PROBE_RWND exit reason=delay_ceiling cycle=%u"
+ "rbbr: PROBE_RWND exit reason=max_cycles cycle=%u max=%u"
+ "rbbr: PROBE_RWND grow cycle=%u %s gain=%u win %u -> %u rwnd_est=%u"
+ "rbbr: PROBE_RWND hold cycle=%u win=%u rwnd_est=%u"
+ "rbbr: PROBE_RWND ok cycle=%u median_delay=%u delay_thresh=%u win=%u rwnd_est=%u cycle_bytes=%llu utilized=%d n=%u"
+ "rbbr: enter PROBE_RWND reprobe win=%u rwnd_est=%u delay_thresh=%u median_rtt=%u rtt_mad=%u"
+ "rbbr: exit %s -> %s dur=%ums median_rtt=%u rtt_mad=%u delay_thresh=%u rwnd_est=%u win=%u samples=%u skip_restrict=%u"
+ "rbbr: sample rtt=%u adv_win=%u win=%u phase=%u"
+ "rbbr: skip sample, win not converged adv_win=%u win=%u pending=%u"
+ "rbbr_cruise_cycles"
+ "rbbr_cycle_rtts"
+ "rbbr_reprobe_gain"
+ "rbbr_round_min_ms"
+ "rbbr_rtt_probe_cycle_rtts"
+ "rbbr_rtt_probe_max_duration"
+ "rbbr_rtt_probe_plateau_rounds"
+ "rbbr_startup_cycle_rtts"
+ "scavenger"
+ "swap_threshold_exceeded"
+ "swapins_defrag"
+ "swapins_reclaim"
+ "swapouts_under_300s"
+ "swapouts_under_30s"
+ "swapouts_under_60s"
+ "target_age"
+ "tcp_rbbr_data_rcvd"
+ "thrashing_detected"
+ "vfs.disk-space"
+ "vm: configured segment limit would overflow slot mapping index, reducing to %d\n"
+ "wakeups"
+ "wlan.NotIdle"
+ "wlan.fragment"
- " [loaded 0x%08x]"
- "%s: %s: failing SIOCDIFADDR with EPWROFF\n"
- "%s: bpf%u and bpf%u have incompatible flags 0x%x != 0x%x error %d"
- "12122121112"
- "22111211111112222211122212222122222222222222222222222222222222222222222222222222222222222222222222222111111111111111111121122222222211222222222222112122212222212222222222222222222222222222112111122222222222222111121221122211222112221122222211222222222222222222222221111221221222222222212212212222111122222222222222222112222222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
- "B16@?0^{task={lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^{user_ldt}^vQQQi^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCC^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=(?={?=b16b8b1b1b1b1b4}I)III}b16b1b1b1b1b1b1b1b2b7[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}QC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
- "CFIL: Handled previously delayed socket for TCP time wait"
- "CFIL: Marked previoulsy delayed socket as DEAD"
- "DRAIN"
- "DRAIN_PROBE_RTT"
- "Fake interface fail ioctl"
- "fail_ioctl"
- "feth_ioctl"
- "in6p_route_copyout"
- "loaded kexts: (skipped, see boot kernelcache)\n"
- "ptmx_get_ioctl failed because minor number %d was out of range\n"
- "pty_get_ioctl failed because minor number %d exceeded %d\n"
- "pty_get_ioctl: driver->open returned NULL\n"
- "rBBR CRUISE backoff factor as percentage (75 = 0.75x) when delay exceeded"
- "rBBR PROBE_RTT RWND in MSS units"
- "rBBR max CRUISE backoffs per phase (default 1 = one-time backoff)"
- "rBBR minimum RWND in MSS units"
- "rBBR probe cycle duration in ms (used for PROBE_RWND, DRAIN, CRUISE monitoring)"
- "rBBR sender utilization threshold (%) below which RWND growth is suppressed"
- "rbbr: enter DRAIN win=%u rwnd_est=%u median_rtt=%u delay_thresh=%u"
- "rbbr: enter DRAIN_PROBE_RTT win=%u rwnd_est=%u median_rtt=%u queue_competition=%u sawtooth_cycles=%u"
- "rbbr: exit %s -> %s dur=%ums median_rtt=%u rtt_mad=%u delay_thresh=%u rwnd_est=%u win=%u win_ws=%u samples=%u skip_restrict=%u"
- "rbbr_enter_drain"
- "rbbr_enter_drain_probe_rtt"
```
