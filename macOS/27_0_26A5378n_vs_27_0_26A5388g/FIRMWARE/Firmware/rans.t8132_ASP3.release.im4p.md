## rans.t8132_ASP3.release.im4p

> `Firmware/rans.t8132_ASP3.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`

```diff

   __TEXT.text_first: 0x45a0
-  __TEXT.__text: 0x1f9110
-  __TEXT.shared: 0xe70c
-  __TEXT.read: 0x799c
-  __TEXT.__const: 0x62c8
-  __TEXT.__cstring: 0x25c34
+  __TEXT.__text: 0x1f7f18
+  __TEXT.shared: 0xe7e4
+  __TEXT.read: 0x772c
+  __TEXT.__const: 0x6308
+  __TEXT.__cstring: 0x25d1b
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_boot: 0x4000

   __DATA._rtk_patchbay: 0x400
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_mtab: 0x540
-  __DATA.__data: 0x76b8
-  __DATA.__const: 0x2de0
+  __DATA.__data: 0x76c0
+  __DATA.__const: 0x2e18
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x167
   __DATA._rtk_init_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x3a78f0
-  Functions: 2088
+  __DATA.__zerofill: 0x3a7920
+  Functions: 2093
   Symbols:   0
-  CStrings:  4058
+  CStrings:  4060
 
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
