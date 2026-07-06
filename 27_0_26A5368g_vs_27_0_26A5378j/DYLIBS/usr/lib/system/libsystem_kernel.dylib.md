## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-  __TEXT.__text: 0x3586c
-  __TEXT.__const: 0xcc0
+  __TEXT.__text: 0x3588c
+  __TEXT.__const: 0xcd0
   __TEXT.__cstring: 0x6a03
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x1230
   __DATA_CONST.__const: 0x2b90
   __AUTH_CONST.__const: 0x150
   __DATA.__crash_info: 0x148

   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x40
   __DATA_DIRTY.__common: 0x690
-  Functions: 1566
-  Symbols:   1747
+  Functions: 1567
+  Symbols:   1748
   CStrings:  995
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _exclaves_device_state
Functions:
~ _mach_msg_destroy : 328 -> 324
~ _posix_spawnattr_setexceptionports_np : 68 -> 72
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
