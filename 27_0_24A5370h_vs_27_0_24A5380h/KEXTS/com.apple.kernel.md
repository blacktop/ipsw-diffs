## com.apple.kernel

> `com.apple.kernel`

```diff

-  __TEXT.__const: 0x36bf0
+  __TEXT.__const: 0x36d30
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x8e2c3
-  __TEXT.__os_log: 0x4136c
+  __TEXT.__cstring: 0x8f388
+  __TEXT.__os_log: 0x418ba
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x11f8f8
-  __DATA_CONST.__kalloc_type: 0x15340
-  __DATA_CONST.__assert: 0x1298
-  __DATA_CONST.__kalloc_var: 0x7e40
+  __DATA_CONST.__const: 0x120450
+  __DATA_CONST.__kalloc_type: 0x15380
+  __DATA_CONST.__assert: 0x1284
+  __DATA_CONST.__kalloc_var: 0x7e90
   __DATA_CONST.__exclaves_bt: 0xc0
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_CONST.__mod_init_func: 0x2d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x4c000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x900a68
+  __TEXT_EXEC.__text: 0x9060ac
   __TEXT_EXEC.__hib_text: 0x10d8
-  __TEXT_BOOT_EXEC.__bootcode: 0x698c
-  __KLD.__text: 0x1728
+  __TEXT_BOOT_EXEC.__bootcode: 0x69a0
+  __KLD.__text: 0x173c
   __LASTDATA_CONST.__mod_init_func: 0x8
   __LAST.__pinst: 0x8
   __LAST.__last: 0x0
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3cf8
+  __KLDDATA.__const: 0x3e08
   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
   __DATA.__data: 0x181e9
-  __DATA.__lock_grp: 0x5cd0
+  __DATA.__lock_grp: 0x5d28
   __DATA.__percpu: 0x78b0
-  __DATA.__common: 0x7b478
-  __DATA.__bss: 0x9fb38
+  __DATA.__common: 0x7b808
+  __DATA.__bss: 0xa5290
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0xfd0
-  __BOOTDATA.__init_entry_set: 0x14208
-  __BOOTDATA.__init: 0x17798
+  __BOOTDATA.__static_if: 0x1000
+  __BOOTDATA.__init_entry_set: 0x145f8
+  __BOOTDATA.__init: 0x17800
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48cf3
-  Functions: 21923
+  Functions: 21972
   Symbols:   0
-  CStrings:  21301
+  CStrings:  21438
 
Sections:
~ __TEXT.__copyio_vectors : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__exclaves_bt : content changed
~ __DATA_CONST.__kern_brk_desc : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __LASTDATA_CONST.__mod_init_func : content changed
~ __KLDDATA.__mod_init_func : content changed
~ __KLDDATA.__mod_term_func : content changed
~ __DATA.__data : content changed
~ __BOOTDATA.__static_ifinit : content changed
CStrings:
+ " AOT"
+ "%s: bpf%u already attached to %s error %d"
+ "%s: bpf%u and bpf%u have incompatible flags 0x%x != 0x%x error %d"
+ "%s: bpf%u and bpf%u have incompatible interfaces %s and %s error %d"
+ "%s: d_from is closing or detached error %d"
+ "%s: d_to is closing or detaching error %d"
+ "%s: downgrading VM entry [%p, %p) from JIT to non-JIT"
+ "%s: interface %s not supported error %d"
+ "%s: proc %s[%d] uses FSIOC_SET_FSTYPENAME_OVERRIDE\n"
+ "%s: refusing NDP update from %s on %s claiming our own link-layer address\n"
+ "%{public}s:%d pid %d (%{public}s) is unable to transmit packets on %{public}s\n"
+ ","
+ "122122"
+ "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122111111111112222222222222222222222222222222222222222222222222222222112222222121122222222222221211122222222222222212222221122222122222222222222212211111112222222222222"
+ "22121222222222222222222222222222"
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
+ "PROBE_RTT"
+ "PROBE_RWND"
+ "Receive-side CC for BG traffic (rBBR=1 or rLEDBAT=2)"
+ "SK[%u]: %-30s %s(%d) failed to validate flow_uuid %s (err %d)\n"
+ "SK[%u]: %-30s %s(%d) flags 0x%x start %u stuff %u len %u headroom %u\n"
+ "SK[%u]: %-30s Unable to get address family\n"
+ "SK[%u]: %-30s can't find flow %s\n"
+ "SK[%u]: %-30s fe %s %snon_via %d withdrawn %d\n"
+ "SPTM (Secure Page Table Monitor)"
+ "SPTM boot timestamps for performance analysis"
+ "TRACKER - %s:%d Could not dump entries, entry tlv size %lu exceeds scratch pad size %lu\n"
+ "TRACKER - %s:%d Could not dump entry, buffer too small\n"
+ "The current number of allocated swapfiles"
+ "The maximum number of swapfiles that can be allocated"
+ "The maximum size (in bytes) of each swapfile"
+ "The minimum size (in bytes) of each swapfile"
+ "Timestamp (timebase ticks) of Exclaves/cL4 bootstrap completion; 0 if Exclaves absent"
+ "Timestamp (timebase ticks) of Exclaves/cL4 bootstrap start; 0 if Exclaves absent"
+ "Timestamp (timebase ticks) of SPTM initialization"
+ "Timestamp (timebase ticks) of TXM bootstrap completion"
+ "Timestamp (timebase ticks) of TXM bootstrap start"
+ "Timestamp (timebase ticks) of XNU bootstrap start"
+ "Whether ktrace ownership requires entitlement on non-macOS."
+ "_dmaReferences overflow @%s:%d"
+ "allocated_bytes"
+ "allocated_bytes_hwm"
+ "aotSleep at %04d/%02d/%d %02d:%02d:%02d\n"
+ "aotWake at %04d/%02d/%d %02d:%02d:%02d\n"
+ "ap-wake-interrupts"
+ "boot_timestamps"
+ "clearing recv_bg bg_throttle=%d is_local=%d"
+ "connection:0x00000001 rtt:0x00000002 ka:0x00000004 log:0x00000008 loop:0x00000010 local:0x00000020 gw:0x00000040 syn:0x00000100 fin:0x00000200 rst:0x00000400 dropnecp:0x00001000 droppcb:0x00002000 droppkt:0x00004000 fswflow:0x00008000 state:0x00010000 synrxmt:0x00020000 output:0x00040000 bind:0x00080000 bbr:0x00100000 "
+ "enabling recv_bg (BE throttle) be_throttle=%d is_local=%d"
+ "enabling recv_bg bg_throttle=%d bg_sys=%d is_local=%d"
+ "exclaves: Scheduler: clock update failed (%d) @%s:%d"
+ "exclaves: unexpected exclaves_run return value %d @%s:%d"
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
+ "highwater_bytes"
+ "inp_restricted_recv"
+ "inp_restricted_send"
+ "intcoproc_unrestricted"
+ "ip_output_list"
+ "kif->pfik_ifp == NULL || kif->pfik_ifp == ifp"
+ "kif->pfik_ifp == ifp"
+ "matchmaker for conclave %s became unready @%s:%d"
+ "mem_entry_wimg_non_writable"
+ "nd6_na_input: tgt lladdr equals own lladdr for %s on %s\n"
+ "nd6_ns_input: src lladdr equals own lladdr from %s on %s\n"
+ "no_linger "
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
+ "reclaim_min_bytes"
+ "reclaim_threshold_bytes"
+ "setInterruptWakes %p\n"
+ "set_tcp_stream_priority"
+ "sigsuspend"
+ "site.struct tcp_rbbr_state"
+ "sk_bootstrap"
+ "sk_complete"
+ "soc-die-id"
+ "sptm_init"
+ "swapfile_cnt"
+ "swapfile_limit"
+ "swapfile_size_max"
+ "swapfile_size_min"
+ "switching to %s bg=%d recv_cc_algo=%u"
+ "tcp_bbr (%s:%d) [%s:%u<->%s:%u] interface: %s (skipped: %lu)\nso_gencnt: %llu t_state: %s process: %s:%u %s"
+ "tcp_set_recv_bg"
+ "txm_bootstrap"
+ "txm_complete"
+ "used_bytes"
+ "used_bytes_hwm"
+ "vm: Maximum number of VM swap files: %d\n"
+ "vm_map_copyout_update_entry"
+ "vm_map_remap"
+ "vm_page_telemetry_init"
+ "wired-mem-exhaustion"
+ "xnu_bootstrap"
- "%s: d_from is closing error %d"
- "%s: d_to is closing error %d"
- "2211111111111112222222112222211222221111112222111111222222222111211112122222222222222222222222222222222222222222222222222222222212222221122111111111112222222222222222222222222222222222222222222222222222222112222222121122222222222221211122222222222222212222221122222122222222222222222222222222222222222222222222222222222211111112222222222222"
- "2212122222222222222222222222222"
- "Receive background CC algorithm (0=rLEDBAT, 1=rBBR)"
- "SK[%u]: %-30s %s(%d) flags 0x%x start %u stuff %u len %u\n"
- "SK[%u]: %-30s can't find flow\n"
- "SK[%u]: %-30s fe \"%s\" [fo %p] non_via %d withdrawn %d\n"
- "bpf_setif"
- "connection:0x00000001 rtt:0x00000002 ka:0x00000004 log:0x00000008 loop:0x00000010 local:0x00000020 gw:0x00000040 syn:0x00000100 fin:0x00000200 rst:0x00000400 dropnecp:0x00001000 droppcb:0x00002000 droppkt:0x00004000 fswflow:0x00008000 state:0x00010000 synrxmt:0x00020000 output:0x00040000 bind:0x00080000 "
- "device_pager_populate_object: list_req failed @%s:%d"
- "exclaves: timer update requested when calling watchdog panic @%s:%d"
- "exclaves: timer update requested when updating timer @%s:%d"
- "exclaves: unexpected exclaves_run return value %u\n @%s:%d"
- "exclaves_xnuproxy_endpoint_call: resume returned bad value %d @%s:%d"
- "flow_entry_teardown"
- "label.io_state == IO_STATE_IN_SPACE"
- "rBBR PROBE_RTT interval in seconds (rounded to factor of 60: 5,10,15,20,30,60)"

```
