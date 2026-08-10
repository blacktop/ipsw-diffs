## ansf.t8150.release.im4p

> `Firmware/ansf.t8150.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA._rtk_patchbay`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1f0de8
+  __TEXT.__text: 0x1f1578
   __TEXT.shared: 0xeac8
   __TEXT.read: 0x73f4
   __TEXT.__const: 0x5e08
-  __TEXT.__cstring: 0x26006
+  __TEXT.__cstring: 0x26207
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x474
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x380
-  __DATA.__data: 0x5c28
-  __DATA.__const: 0x1b40
+  __DATA.__data: 0x5c30
+  __DATA.__const: 0x1b70
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x163
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x2a5b18
-  Functions: 2029
+  Functions: 2035
   Symbols:   0
-  CStrings:  4081
+  CStrings:  4085
 
CStrings:
+ "241.0.12"
+ "241.0.12~425"
+ "AppleStorageFirmwareASP3-241.0.12~425"
+ "{ 'trace_id': 'CACHE_EVICT', 'tp_func': %d, 'timestamp': %llu, 'todo': %u, 'dirty': %u, 'evict': %u, 'hostq': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_PICK', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'thresh': %u, 'reason': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_PICK_PREV', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'thresh': %u, 'reason': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_TOPUP', 'tp_func': %d, 'timestamp': %llu, 'oldFlow': %u, 'writeq': %u, 'stripe': %u, 'moved': %u }\n"
+ "{ 'trace_id': 'PUSH_HOST_STALL', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'hostq': %u, 'secleft': %u }\n"
- "241.0.6"
- "241.0.6~137"
- "AppleStorageFirmwareASP3-241.0.6~137"
- "{ 'trace_id': 'CACHE_EVICT', 'tp_func': %d, 'timestamp': %llu, 'todo': %u, 'dirty': %u, 'evict': %u }\n"
```
