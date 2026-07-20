## ansf.t6050.release.im4p

> `Firmware/ansf.t6050.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x2003b4
-  __TEXT.shared: 0xed94
-  __TEXT.read: 0x7a20
-  __TEXT.__const: 0x6c78
-  __TEXT.__cstring: 0x26209
+  __TEXT.__text: 0x200714
+  __TEXT.shared: 0xee6c
+  __TEXT.read: 0x77b0
+  __TEXT.__const: 0x6cf8
+  __TEXT.__cstring: 0x262f0
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x480
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x640
-  __DATA.__data: 0x8168
-  __DATA.__const: 0x2288
+  __DATA.__data: 0x8170
+  __DATA.__const: 0x22c0
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x5ad078
-  Functions: 2153
+  __DATA.__zerofill: 0x5ad0a8
+  Functions: 2157
   Symbols:   0
-  CStrings:  4122
+  CStrings:  4124
 
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
