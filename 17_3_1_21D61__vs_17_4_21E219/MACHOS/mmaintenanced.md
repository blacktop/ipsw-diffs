## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-131.0.0.0.0
-  __TEXT.__text: 0x1322c
-  __TEXT.__auth_stubs: 0xa60
+136.0.0.0.0
+  __TEXT.__text: 0x13d48
+  __TEXT.__auth_stubs: 0xad0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__oslogstring: 0x162b
-  __TEXT.__cstring: 0xf67
-  __TEXT.__const: 0x4e8
-  __TEXT.__gcc_except_tab: 0x728
-  __TEXT.__unwind_info: 0x6a4
+  __TEXT.__oslogstring: 0x193b
+  __TEXT.__cstring: 0x10a3
+  __TEXT.__const: 0x4d8
+  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__cfstring: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 427
-  Symbols:   218
-  CStrings:  310
+  Functions: 448
+  Symbols:   225
+  CStrings:  324
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ __os_log_fault_impl
+ _analytics_send_event
+ _fgets
+ _memchr
+ _sscanf
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "%s: failed to retrieve vm.vm_ecc_max_db_pages, using fallback limit of %d"
+ "/private/var/mobile/Library/MemoryMaintenance/system_hwm"
+ "Corrupt system hwm state file"
+ "Failed to remove system hwm state file: %s"
+ "Reporting system hwm state from previous reboot action: {did_user_space_reboot=%llu user_hwm_level=%llu user_hwm_limit=%llu did_kernel_reboot=%llu kernel_hwm_level=%llu kernel_hwm_limit=%llu}"
+ "User reclaimable limit not crossed; user reclaimable current: %llu%%. User reclaimable minimum: %llu%%"
+ "Warning: writing user hwm state while a system hwm state file exists"
+ "com.apple.memorytools.stats.systemmemoryreset"
+ "did_kernel_reboot"
+ "did_user_space_reboot"
+ "kernel_hwm_level"
+ "kernel_hwm_limit"
+ "perform_u_reboot=%llu uhwm_level=%llu uhwm_limit=%llu perform_k_reboot=%llu khwm_level=%llu khwm_limit=%llu\n"
+ "pressure: could not retrieve collectable bytes"
+ "pressure: could not retrieve memory level"
+ "pressure: could not retrieve memory size"
+ "pressure: could not retrieve zone memory info"
+ "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, kext site %llu, kext named %llu"
+ "pressure: vmstat anonymous %u compressor %u in_compressor %llu, jetsam level %u available %u p_p_l %u,\n<= FG uncompressed %llu compressed %llu, > FG uncompressed %llu compressed %llu, frozen %llu,\nest reclaimable %llu total_user %llu levels %lld"
+ "user_hwm_level"
+ "user_hwm_limit"
- "%s: failed to retreive vm.vm_ecc_max_db_pages, using fallback limit of %d"
- "User reclaimable limit not crossed"
- "could not call mach_memory_info"
- "could not retrieve collectable bytes"
- "could not retrieve kdebug trace bytes"
- "could not retrieve memory level"
- "could not retrieve memory size"

```
