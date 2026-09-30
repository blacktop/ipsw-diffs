## rans.t604x.release.im4p

> `Firmware/rans.t604x.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x200e88
+  __TEXT.__text: 0x2015ec
   __TEXT.shared: 0xe9ac
   __TEXT.read: 0x7728
   __TEXT.__const: 0x66e8
-  __TEXT.__cstring: 0x261bf
+  __TEXT.__cstring: 0x263c0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x400
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x540
-  __DATA.__data: 0x7900
-  __DATA.__const: 0x36d0
+  __DATA.__data: 0x7908
+  __DATA.__const: 0x3700
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x594da8
-  Functions: 2182
+  __DATA.__zerofill: 0x594db8
+  Functions: 2188
   Symbols:   0
-  CStrings:  4094
+  CStrings:  4098
 
CStrings:
+ "241.0.12"
+ "241.0.12~652"
+ "AppleStorageFirmwareASP3-241.0.12~652"
+ "{ 'trace_id': 'CACHE_EVICT', 'tp_func': %d, 'timestamp': %llu, 'todo': %u, 'dirty': %u, 'evict': %u, 'hostq': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_PICK', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'thresh': %u, 'reason': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_PICK_PREV', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'thresh': %u, 'reason': %u }\n"
+ "{ 'trace_id': 'PUSH_FLOW_TOPUP', 'tp_func': %d, 'timestamp': %llu, 'oldFlow': %u, 'writeq': %u, 'stripe': %u, 'moved': %u }\n"
+ "{ 'trace_id': 'PUSH_HOST_STALL', 'tp_func': %d, 'timestamp': %llu, 'flow': %u, 'writeq': %u, 'hostq': %u, 'secleft': %u }\n"
- "241.0.6"
- "241.0.6~139"
- "AppleStorageFirmwareASP3-241.0.6~139"
- "{ 'trace_id': 'CACHE_EVICT', 'tp_func': %d, 'timestamp': %llu, 'todo': %u, 'dirty': %u, 'evict': %u }\n"
```
