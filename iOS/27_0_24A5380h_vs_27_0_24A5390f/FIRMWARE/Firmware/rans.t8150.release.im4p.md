## rans.t8150.release.im4p

> `Firmware/rans.t8150.release.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1f21e4
-  __TEXT.shared: 0xe9e4
-  __TEXT.read: 0x7664
-  __TEXT.__const: 0x5dc8
-  __TEXT.__cstring: 0x25f1f
+  __TEXT.__text: 0x1f0de8
+  __TEXT.shared: 0xeac8
+  __TEXT.read: 0x73f4
+  __TEXT.__const: 0x5e08
+  __TEXT.__cstring: 0x26006
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_patchbay: 0x474
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x380
-  __DATA.__data: 0x5c20
-  __DATA.__const: 0x1b08
+  __DATA.__data: 0x5c28
+  __DATA.__const: 0x1b40
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x163
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x2a5ae8
-  Functions: 2024
+  __DATA.__zerofill: 0x2a5b18
+  Functions: 2029
   Symbols:   0
-  CStrings:  4079
+  CStrings:  4081
 
CStrings:
+ "!MIDR: 0x%x"
+ "241.0.6"
+ "241.0.6~137"
+ "AppleStorageFirmwareASP3-241.0.6~137"
+ "{ 'trace_id': 'CMD_DRAIN', 'tp_func': %d, 'timestamp': %llu, 'thresh': %u, 'inUseCnt': %u, 'elapsed_us': %u }\n"
+ "{ 'trace_id': 'CMD_IMMEDIATE', 'tp_func': %d, 'timestamp': %llu, 'opType': %u, 'tag': %u, 'elapsed_us': %u }\n"
- "!MIDR: 0x%llx"
- "236"
- "236~174"
- "AppleStorageFirmwareASP3-236~174"
```
