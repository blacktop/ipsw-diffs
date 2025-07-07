## PolarisBufferService

> `/System/Library/PrivateFrameworks/PolarisBufferService.framework/PolarisBufferService`

```diff

-220.0.13.0.0
-  __TEXT.__text: 0x65b44
+220.0.17.0.0
+  __TEXT.__text: 0x65690
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__const: 0x180c
-  __TEXT.__cstring: 0x7da7
-  __TEXT.__oslogstring: 0xacb4
+  __TEXT.__const: 0x1814
+  __TEXT.__cstring: 0x7cd9
+  __TEXT.__oslogstring: 0xac15
   __TEXT.__gcc_except_tab: 0x2ae4
-  __TEXT.__unwind_info: 0x1e28
+  __TEXT.__unwind_info: 0x1e10
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1c0
   __TEXT.__objc_stubs: 0x260

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20842008-BA39-377A-B05E-C585704C41C7
-  Functions: 1996
-  Symbols:   5470
-  CStrings:  1625
+  UUID: FDAF8AD4-7C48-3AED-A068-5623848DE759
+  Functions: 1992
+  Symbols:   5493
+  CStrings:  1619
 
Symbols:
+ __ZN13PSCommsClient8send_oolEP14comms_header_tjPvj15target_module_tb
+ __ZN13PSCommsClient8send_oolEP14comms_header_tjPvj15target_module_tb.cold.1
- GCC_except_table67
- __ZN13PSCommsClient28send_ool_and_server_mod_refsEP14comms_header_tjPvj15target_module_t
- __ZN13PSCommsClient28send_ool_and_server_mod_refsEP14comms_header_tjPvj15target_module_t.cold.1
- __ZN13PSCommsClient28send_ool_and_server_mod_refsEP14comms_header_tjPvj15target_module_t.cold.2
- __ZN13PSCommsClient8send_oolEP14comms_header_tjPvj15target_module_t
- __ZN13PSCommsClient8send_oolEP14comms_header_tjPvj15target_module_t.cold.1
- _ps_comms_client_send_ool_and_server_mod_refs
CStrings:
+ "04:06:15"
+ "Jun 26 2025"
- "%s:%d CommsClient: not using reply port for send_ool_and_server_mod_refs\n"
- "%s:%d Failure to mach_port_mod_refs MACH_PORT_RIGHT_SEND for port %#x. kr = %#x (%s)"
- "00:23:48"
- "CommsClient: not using reply port for send_ool_and_server_mod_refs\n"
- "Jun 14 2025"
- "_send_ool_and_server_mod_refs"
- "send_ool_and_server_mod_refs"

```
