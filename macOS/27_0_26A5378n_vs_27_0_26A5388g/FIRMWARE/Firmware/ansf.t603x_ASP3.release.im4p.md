## ansf.t603x_ASP3.release.im4p

> `Firmware/ansf.t603x_ASP3.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x20907c
-  __TEXT.shared: 0xe9fc
-  __TEXT.read: 0x79a4
-  __TEXT.__const: 0x6c28
-  __TEXT.__cstring: 0x264a5
+  __TEXT.__text: 0x207e10
+  __TEXT.shared: 0xead4
+  __TEXT.read: 0x7734
+  __TEXT.__const: 0x6c68
+  __TEXT.__cstring: 0x2658c
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x400
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_mtab: 0x540
-  __DATA.__data: 0x83f0
-  __DATA.__const: 0x4248
+  __DATA.__data: 0x83f8
+  __DATA.__const: 0x4280
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5825b8
-  Functions: 2311
+  __DATA.__zerofill: 0x5825e8
+  Functions: 2316
   Symbols:   0
-  CStrings:  4167
+  CStrings:  4169
 
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
