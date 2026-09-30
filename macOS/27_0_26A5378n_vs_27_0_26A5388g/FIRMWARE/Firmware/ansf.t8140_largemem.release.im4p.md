## ansf.t8140_largemem.release.im4p

> `Firmware/ansf.t8140_largemem.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1e6cc0
-  __TEXT.shared: 0xde0c
-  __TEXT.read: 0x7350
-  __TEXT.__const: 0x58d8
-  __TEXT.__cstring: 0x24d58
+  __TEXT.__text: 0x1e59f0
+  __TEXT.shared: 0xdef0
+  __TEXT.read: 0x70e0
+  __TEXT.__const: 0x5918
+  __TEXT.__cstring: 0x24e3f
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x3f4
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x310
-  __DATA.__data: 0x7000
-  __DATA.__const: 0x23e8
+  __DATA.__data: 0x7008
+  __DATA.__const: 0x2420
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x162
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x356518
-  Functions: 1969
+  __DATA.__zerofill: 0x356548
+  Functions: 1974
   Symbols:   0
-  CStrings:  3957
+  CStrings:  3959
 
CStrings:
+ "!MIDR: 0x%x"
+ "241.0.6"
+ "241.0.6~139"
+ "AppleStorageFirmwareASP3-241.0.6~139"
+ "{ 'trace_id': 'CMD_DRAIN', 'tp_func': %d, 'timestamp': %llu, 'thresh': %u, 'inUseCnt': %u, 'elapsed_us': %u }\n"
+ "{ 'trace_id': 'CMD_IMMEDIATE', 'tp_func': %d, 'timestamp': %llu, 'opType': %u, 'tag': %u, 'elapsed_us': %u }\n"
- "!MIDR: 0x%llx"
- "236"
- "236~187"
- "AppleStorageFirmwareASP3-236~187"
```
