## rans.t603x_ASP3.release.im4p

> `Firmware/rans.t603x_ASP3.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA._rtk_patchbay`
- `__DATA.__data`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x207e10
+  __TEXT.__text: 0x208524
   __TEXT.shared: 0xead4
   __TEXT.read: 0x7734
   __TEXT.__const: 0x6c68
-  __TEXT.__cstring: 0x2658c
+  __TEXT.__cstring: 0x2678d
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_mtab: 0x540
   __DATA.__data: 0x83f8
-  __DATA.__const: 0x4280
+  __DATA.__const: 0x42b0
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5825e8
-  Functions: 2316
+  __DATA.__zerofill: 0x5825f8
+  Functions: 2322
   Symbols:   0
-  CStrings:  4169
+  CStrings:  4173
 
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
