## com.apple.driver.RTBuddy

> `com.apple.driver.RTBuddy`

```diff

-693.80.3.0.1
-  __TEXT.__cstring: 0x991d
-  __TEXT.__os_log: 0x4e6
-  __TEXT.__const: 0x2e0
-  __TEXT_EXEC.__text: 0x46b6c
+693.100.47.0.0
+  __TEXT.__cstring: 0x9ae7
+  __TEXT.__os_log: 0x652
+  __TEXT.__const: 0x280
+  __TEXT_EXEC.__text: 0x420b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0xb98
-  __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__mod_init_func: 0x148
-  __DATA_CONST.__mod_term_func: 0x148
-  __DATA_CONST.__const: 0xb7c8
-  __DATA_CONST.__kalloc_type: 0x1380
+  __DATA.__common: 0xbc0
+  __DATA_CONST.__auth_got: 0x548
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__mod_init_func: 0x150
+  __DATA_CONST.__mod_term_func: 0x150
+  __DATA_CONST.__const: 0xbf58
+  __DATA_CONST.__kalloc_type: 0x13c0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: ED0D5853-6C14-3310-BED4-15CCFE2069FB
-  Functions: 2343
+  UUID: 7400EA77-8438-3366-AD71-DDE0DA4D1BC3
+  Functions: 2407
   Symbols:   0
-  CStrings:  1088
+  CStrings:  1099
 
CStrings:
+ "\"RTBuddy(%s)::%s \" \"EDT property '%s' is not supported in RTBuddyARG.\" \"\\n%s\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"Invalid Pstate passed: %d\" \"\\n%s\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"Unexpected flow, somehow already sent AP state\" \"\\n%s\" @%s:%d"
+ "\"RTBuddy(%s)::%s \" \"remote-only must be defined for RTBuddyARG\" \"\\n%s\" @%s:%d"
+ "1211111212221212111211112221111122212222221212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211111211111111111111212122222211112"
+ "1212222111122"
+ "23:05:07"
+ "Feb  4 2026"
+ "RTBuddy(%s): %s"
+ "RTBuddy(%s): %s%s"
+ "RTBuddy(%s): Boot args override: %s = %d"
+ "RTBuddy(%s): Boot args override: %s = %lld"
+ "RTBuddy(%s): Failed to send flush completion message to IOP - %x"
+ "RTBuddy(%s): Finding route %d"
+ "RTBuddy(%s): IOP start disabled by device tree"
+ "RTBuddy(%s): IOP start disabled in restore"
+ "RTBuddy(%s): IOP start explicitly disabled by boot-arg"
+ "RTBuddy(%s): Loaded firmware: %s - %s\n"
+ "RTBuddy(%s): OSLog endpoint registering to logd(uuid: %s, role: %s, range_start: %u, range_end: %u, fw_type: %u)"
+ "RTBuddy(%s): OSLog log_coalescer_entry from source %s is corrupt, dropping buffer"
+ "RTBuddy(%s): OSLog log_entry from source %s is corrupt, dropping buffer"
+ "RTBuddy(%s): OSLog log_entry from source has corrupt source_info, dropping entry"
+ "RTBuddy(%s): OSLog log_entry size from source %s is corrupt, dropping buffer"
+ "RTBuddy(%s): OSLog segment methods. uuid %s. method %u\n"
+ "RTBuddy(%s): Resuming...\n"
+ "RTBuddy(%s): Success route %d"
+ "RTBuddy(%s): Time out, failed to process kdebug traces before power gating\n"
+ "RTBuddy(%s): Unimplemented syslog command: %x"
+ "RTBuddy(%s): WARNING: Bypassing firmware validation."
+ "RTBuddy(%s): WARNING: failed to send ping."
+ "RTBuddy(%s): WARNING: ping timeout."
+ "RTBuddy(%s): added oslog segment slice. uuid %s. offset %d. len %d\n"
+ "RTBuddy(%s): cL4 coredump region identified"
+ "RTBuddy(%s): copy oslog. found oslog slice for uuid %s. length is %llu. offset is %llu\n"
+ "RTBuddy(%s): could not find oslog slice for role %s\n"
+ "RTBuddy(%s): oslog segment size. found oslog slice for uuid %s. length is %llu\n"
+ "RTBuddyARG"
+ "RTBuddyARG.cpp"
+ "_checkForUnsupportedEDTProperties"
+ "_onPowerStateGated"
+ "automatic-rail-gating-enabled"
+ "setPowerPolicy"
+ "should-control-sram"
+ "site.RTBuddyARG"
- "12111112122212121112111122211111222122222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111121111111111111121212222221111"
- "121222111122"
- "20:53:17"
- "Boot args override: %s = %d"
- "Boot args override: %s = %lld"
- "Failed to send flush completion message to IOP - %x"
- "Finding route %d"
- "IOP start disabled by device tree"
- "IOP start disabled in restore"
- "IOP start explicitly disabled by boot-arg"
- "Jan 26 2026"
- "Loaded firmware: %s - %s\n"
- "OSLog endpoint registering to logd(uuid: %s, role: %s, range_start: %u, range_end: %u, fw_type: %u)"
- "OSLog log_coalescer_entry from source %s is corrupt, dropping buffer"
- "OSLog log_entry from source %s is corrupt, dropping buffer"
- "OSLog log_entry from source has corrupt source_info, dropping entry"
- "OSLog log_entry size from source %s is corrupt, dropping buffer"
- "OSLog segment methods. uuid %s. method %u\n"
- "Resuming...\n"
- "Success route %d"
- "Time out, failed to process kdebug traces before power gating\n"
- "Unimplemented syslog command: %x"
- "WARNING: Bypassing firmware validation."
- "WARNING: failed to send ping."
- "WARNING: ping timeout."
- "added oslog segment slice. uuid %s. offset %d. len %d\n"
- "cL4 coredump region identified"
- "copy oslog. found oslog slice for uuid %s. length is %llu. offset is %llu\n"
- "could not find oslog slice for role %s\n"
- "oslog segment size. found oslog slice for uuid %s. length is %llu\n"
- "sram-index"

```
