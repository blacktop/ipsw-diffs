## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-  __TEXT.__text: 0x34ee0
-  __TEXT.__const: 0xc80
+  __TEXT.__text: 0x34f00
+  __TEXT.__const: 0xc90
   __TEXT.__cstring: 0x5cda
   __TEXT.__unwind_info: 0x11f8
   __DATA_CONST.__const: 0x28d8

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x680
-  Functions: 1554
-  Symbols:   1778
+  Functions: 1555
+  Symbols:   1779
   CStrings:  915
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _exclaves_device_state
Functions:
~ _mach_msg_destroy : 328 -> 324
~ ___sfi_ctl : 52 -> 56
~ __libkernel_strlen : 264 -> 256
~ __libkernel_memset : 140 -> 128
+ _exclaves_device_state
~ __mach_vsnprintf : 392 -> 404
~ _inet_rule_iterate : 176 -> 184
~ _eth_rule_iterate : 176 -> 184
~ _host_get_boot_info : 536 -> 528
~ _host_kernel_version : 520 -> 512
~ __kernelrpc_mach_port_kobject_description : 576 -> 568
~ _netname_version : 420 -> 416

```
