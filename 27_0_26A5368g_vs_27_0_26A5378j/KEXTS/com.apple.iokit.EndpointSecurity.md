## com.apple.iokit.EndpointSecurity

> `com.apple.iokit.EndpointSecurity`

```diff

   __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x971f
-  __TEXT.__os_log: 0x4b46
-  __TEXT_EXEC.__text: 0xa6498
+  __TEXT.__cstring: 0x970f
+  __TEXT.__os_log: 0x4b26
+  __TEXT_EXEC.__text: 0xa65c4
   __TEXT_EXEC.__auth_stubs: 0xb50
   __DATA.__data: 0x228
   __DATA.__bss: 0x28
-  __DATA.__common: 0xcc
+  __DATA.__common: 0xc4
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x71e0

   __DATA_CONST.__kalloc_var: 0x2260
   __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0xa0
-  Functions: 2616
-  Symbols:   6491
-  CStrings:  865
+  Functions: 2615
+  Symbols:   6488
+  CStrings:  861
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN2es28EndpointSecurityEventManager33es_proc_check_service_port_deriveEP5ucredP22mach_service_port_info
+ _thread_clear_honor_qlimit
+ _thread_set_honor_qlimit
- _PE_parse_boot_argn
- _ZN2es28EndpointSecurityEventManager14sendXpcConnectEP5ucredP22mach_service_port_info
- __ZN2es28EndpointSecurityEventManager14sendXpcConnectEP5ucredP22mach_service_port_info
- __ZN2es28EndpointSecurityEventManager34es_proc_notify_service_port_deriveEP5ucredP22mach_service_port_info
- __ZZN22EndpointSecurityDriver4initEP12OSDictionaryE11_os_log_fmt_2
- _gSkywalkEventsEnabled_
- _mach_msg_destroy_from_kernel_proper
CStrings:
+ "12112221122"
+ "Either<int, es_auth_result_t> es::EndpointSecurityEventManager::sendXpcConnect(kauth_cred_t, struct mach_service_port_info *)"
- "1211222112"
- "Either<int, Unit> es::EndpointSecurityEventManager::sendXpcConnect(kauth_cred_t, struct mach_service_port_info *)"
- "Skywalk events %s via boot-arg\n"
- "disabled"
- "enabled"
- "es_swevents"

```
