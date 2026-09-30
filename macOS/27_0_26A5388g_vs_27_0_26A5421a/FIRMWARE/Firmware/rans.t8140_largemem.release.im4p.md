## rans.t8140_largemem.release.im4p

> `Firmware/rans.t8140_largemem.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1e59f0
+  __TEXT.__text: 0x1e6168
   __TEXT.shared: 0xdef0
   __TEXT.read: 0x70e0
   __TEXT.__const: 0x5918
-  __TEXT.__cstring: 0x24e3f
+  __TEXT.__cstring: 0x25040
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x3f4
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x310
-  __DATA.__data: 0x7008
-  __DATA.__const: 0x2420
+  __DATA.__data: 0x7010
+  __DATA.__const: 0x2450
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x162
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x356548
-  Functions: 1974
+  __DATA.__zerofill: 0x356558
+  Functions: 1980
   Symbols:   0
-  CStrings:  3959
+  CStrings:  3963
 
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
