## sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

-131.0.0.0.0
-  __TEXT.__text: 0xcd5c
-  __TEXT.__auth_stubs: 0x4d0
+136.0.0.0.0
+  __TEXT.__text: 0xd350
+  __TEXT.__auth_stubs: 0x540
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x5a4
-  __TEXT.__cstring: 0x760
-  __TEXT.__const: 0x4a4
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__cstring: 0x8e0
+  __TEXT.__oslogstring: 0x45
+  __TEXT.__const: 0x498
+  __TEXT.__unwind_info: 0x5b4
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__cfstring: 0x40
   __DATA.__common: 0x78

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 269
-  Symbols:   101
-  CStrings:  64
+  Functions: 279
+  Symbols:   109
+  CStrings:  69
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ __os_log_default
+ __os_log_fault_impl
+ _ferror
+ _fgets
+ _os_log_type_enabled
+ _sscanf
+ _vm_deallocate
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- _sysctl
CStrings:
+ "/private/var/mobile/Library/MemoryMaintenance/system_hwm"
+ "Kernel memory exceeded limit on first pass, but not second pass, not rebooting\n"
+ "Warning: writing user hwm state while a system hwm state file exists"
+ "perform_u_reboot=%llu uhwm_level=%llu uhwm_limit=%llu perform_k_reboot=%llu khwm_level=%llu khwm_limit=%llu\n"
+ "pressure: could not retrieve collectable bytes\n"
+ "pressure: could not retrieve memory level\n"
+ "pressure: could not retrieve memory size\n"
+ "pressure: could not retrieve zone memory info\n"
+ "pressure: raw level %u -> corrected %u, excluded bytes %llu of which collectable %llu, diag %llu, kext site %llu, kext named %llu\n"
+ "r"
- "could not call mach_memory_info\n"
- "could not retrieve collectable bytes\n"
- "could not retrieve kdebug trace bytes\n"
- "could not retrieve memory level\n"
- "could not retrieve memory size\n"

```
