## netstat

> `/usr/sbin/netstat`

```diff

-725.0.0.0.0
-  __TEXT.__text: 0x170e8
+726.0.0.0.0
+  __TEXT.__text: 0x17290
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0xadfd
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__cstring: 0xae4c
+  __TEXT.__const: 0xd8
+  __TEXT.__unwind_info: 0x158
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10

   __DATA.__bss: 0xab68
   __DATA.__common: 0x728
   - /usr/lib/libSystem.B.dylib
-  UUID: 8104F819-38D8-3E8A-8E3D-40356F3C2301
-  Functions: 88
-  Symbols:   291
-  CStrings:  1776
+  UUID: 8679ACA2-3D00-3972-B0AE-2892748B6101
+  Functions: 89
+  Symbols:   292
+  CStrings:  1780
 
Symbols:
+ _proc_name
Functions:
~ _bpf_stats : 1044 -> 876
~ _protopr : 2120 -> 2140
~ _print_socket_stats_format : 388 -> 464
~ _print_socket_stats_data : 320 -> 512
~ _systmpr : 1744 -> 1764
~ _unixpr_n : 908 -> 920
+ _proc_name
CStrings:
+ " %05x %08x %016llx %08x %08x %6d %6d %06x"
+ " %5.5s %8.8s %16.16s %8.8s %8.8s %6s %6s %5s"
+ " %7.7s %7.7s %16s:%-6s"
+ " %7.7s %7.7s %16s:%-6s %16s:%-6s"
+ " %7u %7u %16s:%-6u"
+ " %7u %7u %16s:%-6u %16s:%-6s"
+ "eprocess"
+ "process"
- " %016llx %08x %08x %6d %6d %06x"
- " %16.16s %8.8s %8.8s %6s %6s %5s"
- " %7.7s %7.7s %6.6s %6.6s %5.5s %8.8s"
- " %7u %7u %6u %6u %05x %08x"

```
