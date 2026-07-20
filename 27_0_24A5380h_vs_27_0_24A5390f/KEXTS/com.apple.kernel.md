## com.apple.kernel

> `com.apple.kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__copyio_vectors`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__exclaves_bt`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__auth_ptr`
- `__LASTDATA_CONST.__mod_init_func`
- `__KLDDATA.__const`
- `__KLDDATA.__mod_init_func`
- `__KLDDATA.__mod_term_func`
- `__BOOTDATA.__static_if`
- `__BOOTDATA.__static_ifinit`

```diff

-13432.0.50.502.2
-  __TEXT.__const: 0x36d30
+13432.0.94.502.2
+  __TEXT.__const: 0x370b0
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x8f388
-  __TEXT.__os_log: 0x418ba
+  __TEXT.__cstring: 0x8f4f0
+  __TEXT.__os_log: 0x41aa8
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__const: 0x120450
-  __DATA_CONST.__kalloc_type: 0x15380
-  __DATA_CONST.__assert: 0x1284
+  __DATA_CONST.__const: 0x120640
+  __DATA_CONST.__kalloc_type: 0x15300
+  __DATA_CONST.__assert: 0x139c
   __DATA_CONST.__kalloc_var: 0x7e90
   __DATA_CONST.__exclaves_bt: 0xc0
   __DATA_CONST.__kern_brk_desc: 0x78

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x4c000
   __TEXT_EXEC.__exc: 0x1000
-  __TEXT_EXEC.__text: 0x9060ac
+  __TEXT_EXEC.__text: 0x909650
   __TEXT_EXEC.__hib_text: 0x10d8
   __TEXT_BOOT_EXEC.__bootcode: 0x69a0
   __KLD.__text: 0x173c

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x181e9
-  __DATA.__lock_grp: 0x5d28
+  __DATA.__data: 0x18269
+  __DATA.__lock_grp: 0x5d80
   __DATA.__percpu: 0x78b0
-  __DATA.__common: 0x7b808
-  __DATA.__bss: 0xa5290
+  __DATA.__common: 0x7b848
+  __DATA.__bss: 0xa52f0
   __BOOTDATA.__data: 0x18000
   __BOOTDATA.__static_if: 0x1000
-  __BOOTDATA.__init_entry_set: 0x145f8
-  __BOOTDATA.__init: 0x17800
+  __BOOTDATA.__init_entry_set: 0x14820
+  __BOOTDATA.__init: 0x178b8
   __BOOTDATA.__static_ifinit: 0x20
   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x48cf3
-  Functions: 21972
+  Functions: 21981
   Symbols:   0
-  CStrings:  21291
+  CStrings:  21312
 
CStrings:
+ "%s: %s %s DHCP dp_flags 0x%x -> 0x%x"
+ "%s: %s: dir %s action %s reqid 0x%x sa_handle 0x%llx handle 0x%llx\n"
+ "%s: %s: spi 0x%x reqid 0x%x handle 0x%llx dir %s src %s[%u] dst %s[%u] proto %u\n"
+ "%s: refusing cross-protocol ifa change on route with llinfo"
+ "(%u): HMAC verification failed: %d\n"
+ "111122211111222211112111121222122"
+ "12120000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000122222222222222222221221211111111221122000000000"
+ "122112211222111"
+ "ALLOW"
+ "B16@?0^{proc=(?={?=^{proc}^^{proc}}{smr_node=^{smr_node}^?})^{proc}^{proc_ro}iiIIIIIIiIQ{?=[2Q]}iCccc{?=^{proc}^^{proc}}{?=^{proc}^^{proc}}{?=^{proc}}{?=^{uthread}^^{uthread}}{smrq_slink={?=^{smrq_slink}}}^{persona}{?=^{proc}^^{proc}}{?=[2Q]}{filedesc={?=[2Q]}CCSiiiii^^{fileproc}*^{klist}^{kqworkq}^{vnode}^{vnode}{?=[2Q]}{?=[2Q]}Q^{kqwllist}{?=[2Q]}Q^{klist}}^{pstats}{?=^{plimit}}{?=^{pgrp}}{sigacts=[32Q][32Q][32I]IIIIIAIi}{?=[2Q]}iIIIIAIAIiiiIi{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}{itimerval={timeval=qi}{timeval=qi}}{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}ii^v^viIII^vii(?={?=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C]Q[16C]ii}{proc_forkcopy_data=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C]Q[16C]ii}){?=^{aio_workq_entry}^^{aio_workq_entry}}{?=^{aio_workq_entry}^^{aio_workq_entry}}{klist=^{knote}}^{rusage_superset}^{thread}^{thread}^{thread}iSSQQiIQA^{workqueue}A^{workq_aio_s}{timeval=qi}^v^vQQ*QQQQQQQ{timeval=qi}SCBBCIiiiI{?=^{proc}^^{proc}}QQQQiiiiIIII[3AS]IQII^{os_reason}^{virtual_env}}8"
+ "DISCARD"
+ "Disabled MTE soft mode because process was ptraced\n"
+ "FWD"
+ "bridge_mac_nat_dhcp_adjust_flags"
+ "com.apple.private.kernel.cpu-counters-info"
+ "com.apple.private.shared-region.config"
+ "flow_registration_count"
+ "ipsec_nonoffload_policy_count > 0"
+ "key_build_offload_policy: unsupported policy action %u for offload\n"
+ "key_build_offload_sa: authentication key too long %u\n"
+ "key_build_offload_sa: encryption key too long %u\n"
+ "key_parse: invalid address extension.\n"
+ "key_setsaval: ESN flag requires an offload interface (offload_if); software ESN is not supported\n"
+ "key_setsaval: offload SA must specify exactly one direction (IN or OUT)\n"
+ "necp_client.c"
+ "necp_flow_registration_count underflow @%s:%d"
+ "offload_fastpath_in"
+ "offload_fastpath_out"
+ "pf_socket_lookup -1 returns due to ipi_lock contention"
+ "rBBR best-effort receive-side throttling enabled"
+ "rt_setif"
+ "socket_lookup_contended"
+ "stale RACK segment [%u, %u) flags 0x%x below snd_una %u"
+ "tag_storage_compressed"
+ "tcp_rack_output"
+ "throttle_be"
- "%s: %s %s DHCP dp_flags 0x%x"
- "%s: %s: reqid 0x%x sa_handle 0x%llx handle 0x%llx\n"
- "%s: %s: spi 0x%x, reqid 0x%x handle 0x%llx\n"
- "(%u): HMAC verfication failed: %d\n"
- "11112221111122221111211112122212"
- "12120000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000112000000000000011200000000000001120000000000000122222222222222222221221211111111221220000000000"
- "12211211222111"
- "B16@?0^{proc=(?={?=^{proc}^^{proc}}{smr_node=^{smr_node}^?})^{proc}^{proc_ro}iiIIIIIIiIQ{?=[2Q]}iCccc{?=^{proc}^^{proc}}{?=^{proc}^^{proc}}{?=^{proc}}{?=^{uthread}^^{uthread}}{smrq_slink={?=^{smrq_slink}}}^{persona}{?=^{proc}^^{proc}}{?=[2Q]}{filedesc={?=[2Q]}CCSiiiii^^{fileproc}*^{klist}^{kqworkq}^{vnode}^{vnode}{?=[2Q]}{?=[2Q]}Q^{kqwllist}{?=[2Q]}Q^{klist}}^{pstats}{?=^{plimit}}{?=^{pgrp}}{sigacts=[32Q][32Q][32I]IIIIIAIi}{?=[2Q]}iIIIIAIAIiiiIi{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}{itimerval={timeval=qi}{timeval=qi}}{itimerval={timeval=qi}{timeval=qi}}{timeval=qi}ii^v^viIII^vii(?={?=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C]Q[16C]ii}{proc_forkcopy_data=IiQ^{vnode}qIIIICCcC[17c][33c]CiI[16C]Q[16C]ii}){?=^{aio_workq_entry}^^{aio_workq_entry}}{?=^{aio_workq_entry}^^{aio_workq_entry}}{klist=^{knote}}^{rusage_superset}^{thread}^{thread}^{thread}iSSQQiIQA^{workqueue}A^{workq_aio_s}{timeval=qi}^v^vQQ*QQQQQQ{timeval=qi}SCBBCIiiiI{?=^{proc}^^{proc}}QQQQiiiiIIII[3AS]IQII^{os_reason}^{virtual_env}}8"
- "ERROR - the creation of new shared region namespaces is restricted by entitlement"
- "Soft mode disabled because process was ptraced\n"
- "Unexpected debugger trap while SP1 selected"
- "bridge_mac_nat_dhcp_flags"
- "internal-isa-vm-allowed"
- "tcp_rack.c"
- "tcp_rack_output: stale segment %p [%u, %u) flags 0x%x below snd_una %u @%s:%d"
```
