## skywalkctl

> `/usr/sbin/skywalkctl`

```diff

-163.0.1.0.0
-  __TEXT.__text: 0x10b50
+163.0.2.0.0
+  __TEXT.__text: 0x11100
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__cstring: 0xc104
+  __TEXT.__cstring: 0xc21f
   __TEXT.__const: 0x60
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x248
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x42d8
+  __DATA_CONST.__const: 0x42f8
   __DATA.__data: 0x47c
   __DATA.__common: 0xb8
   __DATA.__bss: 0x765
   - /usr/lib/libSystem.B.dylib
-  UUID: 3477ECDC-63BD-32AC-9018-104E5EF63668
-  Functions: 158
+  UUID: 1CBF5A18-FD03-3727-BA35-818762AE4680
+  Functions: 162
   Symbols:   114
-  CStrings:  2065
+  CStrings:  2080
 
CStrings:
+ "%-32s %10d %20s %20s\n"
+ "%-32s %10s %20s %20s\n"
+ "%.2f KB"
+ "%.2f MB"
+ "---"
+ "------"
+ "----------"
+ "--------------------"
+ "-------------------------------"
+ "Memory Size"
+ "Memory Usage By Process:"
+ "PID"
+ "TOTAL"
+ "Usage: memory [ OPTIONS ]   -h, --help          this message\n   -I, --interface=IF  show memory usage matching IF\n   -J, --json          output in JSON format\n   -P, --pid=pid       show memory usage with pid\n   -a, --all           show all available information\n   -A, --arena         show arenas\n   -R, --region        show regions\n   -C, --cache         show caches\n   -g, --group         group memory usage by process\n"
+ "Wired Size"
+ "aAChgI:JP:Rs"
+ "group"
- "Usage: memory [ OPTIONS ]   -h, --help          this message\n   -I, --interface=IF  show memory usage matching IF\n   -J, --json          output in JSON format\n   -P, --pid=pid       show memory usage with pid\n   -a, --all\t\tshow all available information\n   -A, --arena\t\tshow arenas\n   -R, --region\tshow regions\n   -C, --cache\t\tshow caches\n"
- "aAChI:JP:Rs"

```
