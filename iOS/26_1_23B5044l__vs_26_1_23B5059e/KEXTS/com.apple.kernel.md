## com.apple.kernel

> `com.apple.kernel`

```diff

-12377.40.77.502.3
-  __TEXT.__const: 0x34e90
+12377.40.103.502.2
+  __TEXT.__const: 0x35450
   __TEXT.__copyio_vectors: 0x2c0
-  __TEXT.__cstring: 0x7fc3f
-  __TEXT.__os_log: 0x3c38d
+  __TEXT.__cstring: 0x7fd06
+  __TEXT.__os_log: 0x3c50a
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8
-  __DATA_CONST.__const: 0x1170a0
+  __DATA_CONST.__const: 0x117180
   __DATA_CONST.__hib_const: 0x120
-  __DATA_CONST.__kalloc_type: 0x141c0
-  __DATA_CONST.__assert: 0x910
+  __DATA_CONST.__kalloc_type: 0x14200
+  __DATA_CONST.__assert: 0x8fc
   __DATA_CONST.__kalloc_var: 0x7b20
   __DATA_CONST.__exclaves_bt: 0x78
   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
-  __TEXT_EXEC.__text: 0x8b0090
+  __TEXT_EXEC.__text: 0x8b147c
   __TEXT_EXEC.__hib_text: 0xf38
   __TEXT_BOOT_EXEC.__bootcode: 0x51d0
   __KLD.__text: 0x1638

   __KLDDATA.__mod_init_func: 0x8
   __KLDDATA.__mod_term_func: 0x8
   __KLDDATA.__cstring: 0x6e1
-  __KLDDATA.__const: 0x3270
+  __KLDDATA.__const: 0x34c0
   __KLDDATA.__bss: 0x1
-  __DATA.__data: 0x17ee9
+  __DATA.__data: 0x17f79
   __DATA.__lock_grp: 0x5b18
   __DATA.__percpu: 0x6f28
-  __DATA.__common: 0x6eb80
+  __DATA.__common: 0x6ec00
   __DATA.__bss: 0x971c8
   __BOOTDATA.__data: 0x18000
-  __BOOTDATA.__static_if: 0x4d30
-  __BOOTDATA.__init_entry_set: 0x125a0
+  __BOOTDATA.__static_if: 0x4d20
+  __BOOTDATA.__init_entry_set: 0x126d8
   __BOOTDATA.__init: 0x5b2f0
   __BOOTDATA.__static_ifinit: 0x8
   __PRELINK_TEXT.__text: 0x0

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x471ae
-  UUID: C2CE7A94-DE83-3517-8927-AC1BD601C4A4
-  Functions: 20736
+  UUID: ED7299F6-8580-30C4-8E8E-8B6368FB4401
+  Functions: 20743
   Symbols:   0
-  CStrings:  20238
+  CStrings:  20237
 
CStrings:
+ " listener dropped ACK while SYN cookies were enabled"
+ "%s: attempt to create kernel TPRO mapping, will produce kernel RX mapping instead. @%s:%d"
+ "%s: attempted execute-only mapping @%s:%d"
+ "112211212122222222222"
+ "21121121"
+ "21121121122222211111222222"
+ "21121121212"
+ "2112112122221"
+ "211222222"
+ "Expected %u seed bytes from bootloader, but got %u.\n @%s:%d"
+ "Page has error bit set\n"
+ "Segment failed SYNCOOKIE authentication, segment was rejected (either ACK was sent to listener after connection was closed OR spoofed)"
+ "decided to kill-top-process for unknown cause @%s:%d"
+ "kern_memorystatus_policy.c"
+ "memorystatus: all %s victims exhausted @%s:%d"
+ "memorystatus: failed to find a %s victim!\n"
+ "memorystatus: no victim found (action: %d)\n"
+ "memorystatus: resuming/thawing pid %d [%s]\n"
+ "memorystatus: too soon to refreeze pid %d [%s], in memorystatus_freeze_pick_process\n"
+ "memorystatus: too soon to refreeze pid %d [%s], in memorystatus_freeze_pick_refreeze_process\n"
+ "memorystatus_freeze_last_processes_thawed_cache_size"
+ "memorystatus_freeze_last_processes_thawed_prevent_refreeze_seconds"
+ "memorystatus_freeze_prevent_refreeze_of_recently_thawed"
+ "pmap_construct_pte"
+ "v304@?0{exclaveindicatorcontroller_sensorrequestmetrics_s=QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ}8"
+ "vm_reclaim: unexpected vm_pressure_level %d @%s:%d"
- " listen drop with SYN cookies"
- "%s(%s) %s"
- "11221121212222222222"
- "2111121"
- "2111121122222211111222222"
- "2111121212"
- "211112122221"
- "21122222"
- "END OF RECORDS WITH tid=%llu. RECORDS FROM ANOTHER THREAD THAT IS PROBABLY RELATED TO THE CRASH (tid=%llu):\n"
- "Early boot random cchkdf_expand %s failed with err %d @%s:%d"
- "Error reason: %s"
- "Expected %u seed bytes from bootloader, but got %u. @%s:%d"
- "Invalid Error Origin"
- "Page Created as Retired"
- "Page Retired at Startup"
- "Segment failed SYNCOOKIE authentication, segment rejected (probably spoofed)"
- "Setting error bit in vm_page\n"
- "Tried to fault an erroneous vm_page\n"
- "UPL Abort Range (Absent Page)"
- "Uncorrectable ECC Error"
- "Unknown/Unclassified"
- "bootseed_init"
- "entropy_init"
- "memorystatus: all victims exhausted @%s:%d"
- "memorystatus: failed to find a process to kill!\n"
- "prngseed_init"
- "vm_fault_page() failed to get page"

```
