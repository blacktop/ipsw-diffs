## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6800.0.0.0.0
-  __TEXT.__cstring: 0x3648e
-  __TEXT.__os_log: 0x2f209
+6800.0.1.0.0
+  __TEXT.__cstring: 0x36578
+  __TEXT.__os_log: 0x2f2f3
   __TEXT.__const: 0xac8
-  __TEXT_EXEC.__text: 0x19e820
+  __TEXT_EXEC.__text: 0x19feb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1378

   __DATA_CONST.__const: 0x1f930
   __DATA_CONST.__kalloc_type: 0x1f40
   __DATA_CONST.__kalloc_var: 0xbe0
-  UUID: B19B5EF2-3BD0-3D43-BA1F-F40F2877F6E3
+  UUID: 42F1367B-708B-35AC-9CBB-92F8F6D04F7F
   Functions: 4967
   Symbols:   0
-  CStrings:  4975
+  CStrings:  4979
 
Functions:
~ __ZN24IOThunderboltXDomainLink20linkStateNegotiationEP28IOThunderboltDispatchContext -> sub_fffffff00a99a37c : 12436 -> 18216
CStrings:
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - context = %p\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - done\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - fRestored = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - last neg width = 0x%x max link width = 0x%x supported speeds = 0x%x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link link_change_command read retry = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link link_change_command read retry = %d done\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link status (2) read retry = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link status (2) read retry = %d done\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link status (2) target link width = 0x%x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link status read retry = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link status read retry = %d done\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_change_command error_code = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_change_command status = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_status_command (2) error_code = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_status_command (2) status = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_status_command error_code = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - link_status_command status = 0x%08x\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - max_link_width = %d current_link_width = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - primary_port_port = %p secondary_port = %p\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - primary_switch = %p secondary_switch = %p\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - read link status\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - secondary_port link is up = %d\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - secondary_port link is up = %d, going to sleep and will retry...\n"
+ "%lldus IOThunderboltXDomainLink<%x>(0x%llx)::linkStateNegotiation - shoud bond\n"
+ "21:42:56"
+ "Jun 30 2025"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - context = %p\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - done\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - fRestored = %d\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - last neg width = 0x%x max link width = 0x%x supported speeds = 0x%x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link link_change_command read retry = %d\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link link_change_command read retry = %d done\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link status (2) read retry = %d\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link status (2) read retry = %d done\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link status (2) target link width = 0x%x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link status read retry = %d\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link status read retry = %d done\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_change_command error_code = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_change_command status = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_status_command (2) error_code = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_status_command (2) status = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_status_command error_code = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - link_status_command status = 0x%08x\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - max_link_width = %d current_link_width = %d\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - primary_port_port = %p secondary_port = %p\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - primary_switch = %p secondary_switch = %p\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - read link status\n"
- "%lldus IOThunderboltXDomainLink<%p>(0x%llx)::linkStateNegotiation - shoud bond\n"
- "23:43:17"
- "Jun 16 2025"

```
