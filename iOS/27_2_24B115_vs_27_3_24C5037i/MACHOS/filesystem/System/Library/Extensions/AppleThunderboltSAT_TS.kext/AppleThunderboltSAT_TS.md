## AppleThunderboltSAT_TS

> `/System/Library/Extensions/AppleThunderboltSAT_TS.kext/AppleThunderboltSAT_TS`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__got`

```diff

-122.0.0.0.1
-  __TEXT.__cstring: 0x11749
+125.60.2.0.0
+  __TEXT.__cstring: 0x11871
   __TEXT.__os_log: 0x277
-  __TEXT.__const: 0xc0
-  __TEXT_EXEC.__text: 0x26304
-  __TEXT_EXEC.__auth_stubs: 0x670
+  __TEXT.__const: 0xb0
+  __TEXT_EXEC.__text: 0x268dc
+  __TEXT_EXEC.__auth_stubs: 0x680
   __DATA.__data: 0x7f0
-  __DATA.__common: 0x5f9
+  __DATA.__common: 0x2d9
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x59f8
+  __DATA_CONST.__const: 0x5a00
   __DATA_CONST.__kalloc_type: 0x4c0
-  __DATA_CONST.__kalloc_var: 0x2d0
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__kalloc_var: 0x320
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x110
-  Functions: 640
-  Symbols:   1263
-  CStrings:  1063
+  Functions: 646
+  Symbols:   1269
+  CStrings:  1066
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ __ZL9gDevPorts
+ __ZN26IOThunderboltConfigCommand24isTopologyDiscoveryProbeEv
+ __ZN31AppleThunderboltSATDevPortTableI29AppleThunderboltSATDevicePortE8check_inEiPS0_
+ __ZN31AppleThunderboltSATDevPortTableI29AppleThunderboltSATDevicePortE8checkoutEi
+ __ZN36AppleThunderboltSATDevicePortBuffers6deinitEv
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_809
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_819
+ __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_883
+ __ZZN29AppleThunderboltSATConnection17newControlCommandEvE21kalloc_type_view_1373
+ __ZZN29AppleThunderboltSATConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommandE21kalloc_type_view_1203
+ __ZZN29AppleThunderboltSATConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommandE21kalloc_type_view_1209
+ __ZZN29AppleThunderboltSATConnection22destroyControlCommandsEvE21kalloc_type_view_1345
+ __ZZN29AppleThunderboltSATDevicePort14destroy_deviceEvE20kalloc_type_view_891
+ __ZZN29AppleThunderboltSATDevicePort4openEiiiP4procE20kalloc_type_view_477
+ __ZZN29AppleThunderboltSATDevicePort5closeEiiiP4procE20kalloc_type_view_518
+ _devfs_remove
- __ZN29AppleThunderboltSATDevicePort12fMaxDevportsE
- __ZN29AppleThunderboltSATDevicePort9fDevPortsE
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_802
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_812
- __ZZN23AppleThunderboltSATPort13sendDirectiveERK15sat_directive_tE20kalloc_type_view_876
- __ZZN29AppleThunderboltSATConnection17newControlCommandEvE21kalloc_type_view_1370
- __ZZN29AppleThunderboltSATConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommandE21kalloc_type_view_1202
- __ZZN29AppleThunderboltSATConnection17rxCommandCallbackEPviP27IOThunderboltReceiveCommandE21kalloc_type_view_1208
- __ZZN29AppleThunderboltSATConnection22destroyControlCommandsEvE21kalloc_type_view_1342
- __ZZN29AppleThunderboltSATDevicePort4openEiiiP4procE20kalloc_type_view_230
- __ZZN29AppleThunderboltSATDevicePort5closeEiiiP4procE20kalloc_type_view_260
CStrings:
+ "1.0.108"
+ "12111112122212121111121"
+ "125.60.2"
+ "212121222"
+ "SATDeviceNode::fetch_queue_entry: unusable queue entry; queue is unrecoverable.\n"
+ "SATDeviceNode::uio_read_wrapper: queue is unrecoverable, refusing to read; reset or reopen this traceport to recover.\n"
+ "SATDevicePort<%p>::destroy_device - ERROR %d cdev callback(s) still in flight, giving up\n"
+ "SATDevicePort<%p>::open - data queue is gone, dev=0x%x\n"
+ "SATTracePort<%p>::read, data queue not (yet) available, provider: %p, buffers %p.\n"
- "1.0.105"
- "1211111212221212111112"
- "122.0.0.0.1"
- "21212"
- "SATTracePort<%p>::read, data queue not (yet) available, provider: %p, uio_buffer %p.\n"
- "set default value of sat_sysctl_lossless_rx to 1"
```
