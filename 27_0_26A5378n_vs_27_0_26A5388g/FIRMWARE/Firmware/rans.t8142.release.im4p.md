## rans.t8142.release.im4p

> `Firmware/rans.t8142.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1f7364
-  __TEXT.shared: 0xe624
-  __TEXT.read: 0x733c
-  __TEXT.__const: 0x5c98
-  __TEXT.__cstring: 0x260d9
+  __TEXT.__text: 0x1f6420
+  __TEXT.shared: 0xe6fc
+  __TEXT.read: 0x70cc
+  __TEXT.__const: 0x5cf8
+  __TEXT.__cstring: 0x261c0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x400
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x3a0
-  __DATA.__data: 0x7980
-  __DATA.__const: 0x2618
+  __DATA.__data: 0x7988
+  __DATA.__const: 0x2650
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x166
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x3a1ac0
-  Functions: 2045
+  __DATA.__zerofill: 0x3a1af0
+  Functions: 2050
   Symbols:   0
-  CStrings:  4106
+  CStrings:  4108
 
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
