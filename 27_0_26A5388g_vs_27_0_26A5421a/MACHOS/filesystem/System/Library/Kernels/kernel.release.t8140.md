## kernel.release.t8140

> `/System/Library/Kernels/kernel.release.t8140`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__hib_const`
- `__DATA_CONST.__sdt_cstring`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__DATA.__data`
- `__HIBDATA.__data`
- `__BOOTDATA.__static_if`
- `__BOOTDATA.__init`
- `__BOOTDATA.__static_ifinit`

```diff

-13432.0.94.501.4
-  __TEXT.__const: 0x38550
-  __TEXT.__copyio_vectors: 0x1c0
-  __TEXT.__cstring: 0xb31ec
-  __TEXT.__os_log: 0x4221b
+13432.1.9.0.0
+  __TEXT.__const: 0x38740
+  __TEXT.__copyio_vectors: 0x150
+  __TEXT.__cstring: 0xb3d61
+  __TEXT.__os_log: 0x422be
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x310
   __DATA_CONST.__sdt_cstring: 0x7254
-  __DATA_CONST.__sdt: 0xeb08
+  __DATA_CONST.__sdt: 0xeb80
   __DATA_CONST.__kalloc_type: 0x18300
-  __DATA_CONST.__const: 0x137540
-  __DATA_CONST.__assert: 0xe9c
+  __DATA_CONST.__const: 0x137df0
+  __DATA_CONST.__assert: 0xf78
   __DATA_CONST.__kalloc_var: 0x85c0
   __DATA_CONST.__exclaves_bt: 0xc0
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x10
   __DATA_SPTM.__const: 0x74000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x9e0edc
+  __TEXT_EXEC.__text: 0x9e432c
   __TEXT_EXEC.__hib_text: 0x19cc
   __TEXT_EXEC.__commpage_text: 0x334
-  __TEXT_BOOT_EXEC.__bootcode: 0x69b8
+  __TEXT_BOOT_EXEC.__bootcode: 0x69d4
   __KLD.__text: 0xb040
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x71f
-  __KLDDATA.__const: 0x9c58
+  __KLDDATA.__const: 0x9ce0
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x20b51
   __DATA.__lock_grp: 0x179f8
   __DATA.__percpu: 0x78b0
-  __DATA.__common: 0x8c420
-  __DATA.__bss: 0xab4c0
+  __DATA.__common: 0x8c4c0
+  __DATA.__bss: 0xab4e0
   __HIBDATA.__data: 0x31
   __HIBDATA.__bss: 0x670
   __HIBDATA.__common: 0x108
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x10a0
   __BOOTDATA.__init: 0x181e0
-  __BOOTDATA.__init_entry_set: 0x14508
+  __BOOTDATA.__init_entry_set: 0x147d8
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x507dd
-  __CTF.__ctf: 0x105eb9
-  Functions: 23706
+  __CTF.__ctf: 0x10652e
+  Functions: 23726
   Symbols:   6947
-  CStrings:  26609
+  CStrings:  26676
 
CStrings:
+ " [loaded at 0x%08x]"
+ "%s:%d CFIL: Handled previously delayed socket for TCP time wait\n"
+ "%s:%d CFIL: Marked previoulsy delayed socket as DEAD\n"
+ "(paddr & PAGE_MASK) == 0"
+ "121221121112"
+ "2211121111111222221112221222212222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111211222222222112222222222221121222122222122222222222222222222222222221121111222222222222221111212211222112221122211222222112222222222222222222222211112212212222222222122122122221111222222222222222221122222222222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
+ "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQi{?=QQAQQ}BBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b1b6[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}IQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}^v^vIQC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
+ "Lockdown Mode state (public)"
+ "MAIN"
+ "Network.fragment"
+ "Post-boot loaded kexts:\n"
+ "REPROBE"
+ "STARTUP"
+ "The total number of times cswap_trigger has been awoken"
+ "VM Compressor Swapper Wakeup Stats"
+ "VM object is read-only (decmpfs?)\n"
+ "VM_KERN_COUNT_WIRED_DYNAMIC"
+ "baseband.fragment"
+ "bt.fragment"
+ "cfil_sock_service_delayed_dead_actions"
+ "com.apple.developer.lockdown-mode.state"
+ "exclaves: Scheduler: Unexpected thread spawn: scid 0x%lx spawned scid 0x%llx @%s:%d"
+ "exclaves: Scheduler: Unexpected thread terminate: scid 0x%lx terminated scid 0x%llx\n @%s:%d"
+ "exclaves: Scheduler: unexpected response during boot: tag 0x%x\n @%s:%d"
+ "exclaves: Scheduler: unexpected response when updating timer: tag 0x%x @%s:%d"
+ "exclaves: Scheduler: unexpected response: tag 0x%x @%s:%d"
+ "exclaves: request to allocate too many pages: %u\n @%s:%d"
+ "exclaves_memory_pa_page_is_sk_shared_ro(paddr)"
+ "exclaves_memory_pa_page_is_sk_shared_ro(page_paddr)"
+ "exclaves_memory_pa_page_is_sk_shared_ro(trunc_page_64(curr_addr))"
+ "exclaves_memory_pa_page_is_sk_shared_rw(trunc_page_64(ipcb_paddr))"
+ "external_q_throttled"
+ "fragmentation_detected"
+ "free_below_reserved"
+ "fsw_dev_input_netem_enqueue"
+ "i < scid_list_count"
+ "idx < page_count"
+ "lockdown_mode_state_public"
+ "minor_compactions"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
+ "output_length <= EXCLAVES_STACKSHOT_BUFFER_SIZE"
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
+ "ret == EXCLAVES_SCHEDULER_SUCCESS"
+ "scavenger"
+ "sk_enter returned RINGGATE_STATUS_ERROR @%s:%d"
+ "sk_enter returned RINGGATE_STATUS_ERROR in exclaves_bootinfo @%s:%d"
+ "swap_threshold_exceeded"
+ "swapins_defrag"
+ "swapins_reclaim"
+ "swapouts_under_300s"
+ "swapouts_under_30s"
+ "swapouts_under_60s"
+ "target_age"
+ "tcp_rbbr_data_rcvd"
+ "terminated->threadHostId == ctid"
+ "thrashing_detected"
+ "trunc_page_64(ipcb_paddr) == trunc_page_64(ipcb_paddr + sizeof(Exclaves_L4_IpcBuffer_t) - 1)"
+ "unexpected ringgate panic status @%s:%d"
+ "unexpected ringgate status %llu @%s:%d"
+ "unknown ringgate status %llu @%s:%d"
+ "vfs.disk-space"
+ "vm: configured segment limit would overflow slot mapping index, reducing to %d\n"
+ "wakeups"
+ "wlan.fragment"
- " [loaded 0x%08x]"
- "%s: %s: failing SIOCDIFADDR with EPWROFF\n"
- "%s: bpf%u and bpf%u have incompatible flags 0x%x != 0x%x error %d"
- "12122121112"
- "22111211111112222211122212222122222222222222222222222222222222222222222222222222222222222222222222222111111111111111111121122222222211222222222222112122212222212222222222222222222222222222112111122222222222222111121221122211222112221122222211222222222222222222222221111221221222222222212212212222111122222222222222222112222222222221121222222222111111121122222222222222222222222222222222222211222221222221211112222122111111111111111111"
- "B16@?0^{task={lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}{os_refcnt=AI}BBBBIIQ^{_vm_map}{queue_entry=^{queue_entry}^{queue_entry}}^{task_watchports}^v{queue_entry=^{queue_entry}^{queue_entry}}^{restartable_ranges}^{processor_set}^{affinity_space}iIiiissiQ{recount_task=^{recount_track}^{recount_usage}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}[4^{ipc_port}]^{ipc_port}[14{exception_action=^{ipc_port}iiii^{label}}]{hardened_exception_action={exception_action=^{ipc_port}iiii^{label}}II}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}^{ipc_port}[3^{ipc_port}]^^{ipc_port}^{ipc_space}^{task_token_data}^{ledger}{queue_entry=^{queue_entry}^{queue_entry}}iI^vQQCACQQQi{?=QQAQQ}BBBBB^Q^Q^Q^Q^Q^QIIIIII^{proc_ro}^{kcdata_descriptor}Q{queue_entry=^{queue_entry}^{queue_entry}}^{label}IIQQ{cpc_task=B}ACBBBBb4b4b4b4CCCCCB*^{vm_shared_region}QQQ^{thread_call}{queue_entry=^{queue_entry}^{queue_entry}}ii^{bank_task}^{ipc_importance_task}{vm_extmod_statistics=qqqqqq}{task_requested_policy=b1b1b2b2b1b1b2b1b3b3b3b1b5b3b3b1b3b1b1b3b1b3b1b1b1b4b12}{task_effective_policy=b1b1b2b1b1b1b2b1b1b3b3b1b1b1b4b1b1b1b3b3b1b1b1b1b1b26}{task_pend_token=(?={?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1}I)}b1b1b1b1b1b27AI^{io_stat_info}{task_writes_counters=QQQQ}{task_writes_counters=QQQQ}{_cpu_time_qos_stats=QQQQQQQ}{_cpu_time_qos_stats=QQQQQQQ}IIQQCCCiii{queue_entry=^{queue_entry}^{queue_entry}}{lck_mtx_s=b24b8I(lck_mtx_state={?=b28b1b1b1b1SS}IQ)}b16b1b1b1b1b1b1b1b2b7[2^{coalition}][2{queue_entry=^{queue_entry}^{queue_entry}}]Q^vIQ{queue_entry=^{queue_entry}^{queue_entry}}iIQQ[16C]Q^{_vmobject_list_output_}II^{vm_deferred_reclamation_metadata_s}^v^vIQC{task_security_config=(?={?=b1b1b1b3b1b1b1b1b1b1C}I)}}8"
- "CFIL: Handled previously delayed socket for TCP time wait"
- "CFIL: Marked previoulsy delayed socket as DEAD"
- "DRAIN"
- "DRAIN_PROBE_RTT"
- "Fake interface fail ioctl"
- "Unexpected ringgate panic status @%s:%d"
- "exclaves: Get bootinfo failed\n @%s:%d"
- "exclaves: Scheduler: clock update failed (%d) @%s:%d"
- "exclaves: early exclaves enter failed\n @%s:%d"
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
