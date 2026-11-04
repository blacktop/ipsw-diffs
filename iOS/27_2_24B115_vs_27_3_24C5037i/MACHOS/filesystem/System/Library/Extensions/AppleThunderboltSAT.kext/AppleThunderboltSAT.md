## AppleThunderboltSAT

> `/System/Library/Extensions/AppleThunderboltSAT.kext/AppleThunderboltSAT`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__got`

```diff

-122.0.0.0.1
-  __TEXT.__cstring: 0x10ee6
-  __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0x23dd0
-  __TEXT_EXEC.__auth_stubs: 0x590
+125.60.2.0.0
+  __TEXT.__cstring: 0x1100e
+  __TEXT.__const: 0x40
+  __TEXT_EXEC.__text: 0x243a8
+  __TEXT_EXEC.__auth_stubs: 0x5a0
   __DATA.__data: 0x7f0
-  __DATA.__common: 0x581
+  __DATA.__common: 0x261
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0x4c30
+  __DATA_CONST.__const: 0x4c38
   __DATA_CONST.__kalloc_type: 0x400
-  __DATA_CONST.__kalloc_var: 0x2d0
-  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__kalloc_var: 0x320
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xe8
-  Functions: 559
-  Symbols:   1118
-  CStrings:  1027
+  Functions: 565
+  Symbols:   1124
+  CStrings:  1030
 
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
