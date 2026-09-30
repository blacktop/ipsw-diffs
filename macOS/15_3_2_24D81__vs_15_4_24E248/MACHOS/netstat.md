## netstat

> `/usr/sbin/netstat`

```diff

-698.60.4.0.0
-  __TEXT.__text: 0x15ae8
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xa5b4
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__auth_got: 0x258
+705.100.5.0.0
+  __TEXT.__text: 0x16330
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0xa93d
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x14b8
-  __DATA.__data: 0x834
+  __DATA.__data: 0x85c
   __DATA.__bss: 0xac08
-  __DATA.__common: 0x724
+  __DATA.__common: 0x728
   - /usr/lib/libSystem.B.dylib
-  UUID: 519144FE-96BD-3BCC-8D96-8CA0BE4B310F
-  Functions: 90
-  Symbols:   84
-  CStrings:  1723
+  UUID: E13D0EFA-8D94-3CC6-9B00-9783ED76CABE
+  Functions: 88
+  Symbols:   83
+  CStrings:  1749
 
Symbols:
- _sprintf
CStrings:
+ "\t%llu TCP SYN retransmission%s standard backoff\n"
+ "\t%llu TCP data retransmission%s compressed\n"
+ "\t%llu TCP packet%s ACK/SYN no prioritized\n"
+ "\t%llu TCP retransmission%s delayed to floor\n"
+ "\t%llu stealth TCP packet%s to closed port\n"
+ "\t%llu stealth UDP packet%s to closed port\n"
+ "\t%llu time%s bad link quality enabled\n"
+ "\t%llu time%s good link quality enabled\n"
+ "\t%llu time%s link congested enabled\n"
+ "\t%llu time%s link heuristics enabled\n"
+ "\t%llu time%s minimally viable link quality enabled\n"
+ "\t%llu time%s poor link quality enabled\n"
+ "\t%llu.%03llu seconds link congested\n"
+ "\t%llu.%03llu seconds link heuristics enabled\n"
+ "\t%llu.%03llu seconds of bad link quality\n"
+ "\t%llu.%03llu seconds of good link quality\n"
+ "\t%llu.%03llu seconds of minimally viable link quality\n"
+ "\t%llu.%03llu seconds of poor link quality\n"
+ "\tenabled: %s\n"
+ "false"
+ "ioctl SIOCGLINKHEURISTICS"
+ "link heuristics on %s\n"
+ "link_heuristics"
+ "socket"
+ "sysctl IFDATA_LINKHEURISTICS"
+ "true"

```
