## rans.t604x.release.im4p

> `Firmware/rans.t604x.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x201f3c
-  __TEXT.shared: 0xe8d4
-  __TEXT.read: 0x7998
-  __TEXT.__const: 0x6698
-  __TEXT.__cstring: 0x260d8
+  __TEXT.__text: 0x200e88
+  __TEXT.shared: 0xe9ac
+  __TEXT.read: 0x7728
+  __TEXT.__const: 0x66e8
+  __TEXT.__cstring: 0x261bf
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x400
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x540
-  __DATA.__data: 0x78f8
-  __DATA.__const: 0x3698
+  __DATA.__data: 0x7900
+  __DATA.__const: 0x36d0
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x594d78
-  Functions: 2177
+  __DATA.__zerofill: 0x594da8
+  Functions: 2182
   Symbols:   0
-  CStrings:  4092
+  CStrings:  4094
 
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
