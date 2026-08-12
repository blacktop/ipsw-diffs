## PolarisBufferService

> `/System/Library/PrivateFrameworks/PolarisBufferService.framework/PolarisBufferService`

```diff

-256.0.3.0.0
-  __TEXT.__text: 0x5d3f4
+256.0.5.0.0
+  __TEXT.__text: 0x5d25c
   __TEXT.__const: 0x171c
-  __TEXT.__gcc_except_tab: 0x2d70
-  __TEXT.__cstring: 0x7a49
-  __TEXT.__oslogstring: 0xa99e
+  __TEXT.__gcc_except_tab: 0x2d80
+  __TEXT.__cstring: 0x7ab9
+  __TEXT.__oslogstring: 0xa961
   __TEXT.__unwind_info: 0x1d98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x740
+  __DATA_CONST.__const: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__objc_selrefs: 0x38

   __AUTH_CONST.__const: 0x2260
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x6a8
   __AUTH.__data: 0x10
-  __AUTH.__thread_vars: 0x18
-  __AUTH.__thread_bss: 0x8
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x28
   __DATA.__data: 0x3acc
   __DATA.__bss: 0x180
   __DATA_DIRTY.__common: 0x30d8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1993
-  Symbols:   2270
-  CStrings:  1542
+  Functions: 1992
+  Symbols:   2276
+  CStrings:  1546
 
Symbols:
+ __ZL16targetModuleNamei
+ __ZN13PSCommsServer12add_cli_infoEPcS0_b15target_module_tP18callback_context_t
+ __ZN20comms_message_recv_t16deallocate_portsEv
+ __ZN20comms_message_recv_t6rejectEv
+ __ZZL16targetModuleNameiE3buf
+ __ZZL16targetModuleNameiE3buf$tlv$init
+ _mach_msg_destroy
+ _objc_release_x26
+ _objc_retain_x26
- __ZN13PSCommsServer12add_cli_infoEPcS0_b
- __ZN13PSCommsServer23invokeRegisteryCallbackE15target_module_tP14comms_cb_arg_t
- _ps_comms_invoke_registry_callback
CStrings:
+ "(unknown:%#x)"
+ "PLS_MOD_COMMS_SERVER"
+ "PLS_MOD_MANIFEST_AGENT_SERVICE"
+ "PLS_MOD_RESOURCE_FACTORY"
+ "PLS_MOD_STREAM_SERVER"
+ "PLS_MOD_SYSTEM_TRANSITION_SERVICE"
+ "PLS_MOD_SYS_GRAPH"
+ "PSCommsServer: %s\n"
+ "PSCommsServer: %s not registered for port \"%s\", rejecting"
+ "PSCommsServer: %s on port \"%s\", rejecting"
+ "PSCommsServer: Unknown message received on port \"%s\", msgh_id=%#x, rejecting"
+ "PSCommsServer: cannot register server \"%s\", MAX_CLI_INFO (%d) reached"
+ "reply port %#x\n"
- "%s:%d PSCommsServer: Unknow message recevied! msgh_id=%#x\n"
- "PSCommsServer: PLS_MOD_MANIFEST_AGENT_SERVICE\n"
- "PSCommsServer: PLS_MOD_RESOURCE_FACTORY\n"
- "PSCommsServer: PLS_MOD_STREAM_SERVER\n"
- "PSCommsServer: PLS_MOD_SYSTEM_TRANSITION_SERVICE\n"
- "PSCommsServer: PLS_MOD_SYS_GRAPH\n"
- "PSCommsServer: Unknow message recevied! msgh_id=%#x\n"
- "Resource factory overwriting callback for target module:%u"
- "reply port %d\n"
```
