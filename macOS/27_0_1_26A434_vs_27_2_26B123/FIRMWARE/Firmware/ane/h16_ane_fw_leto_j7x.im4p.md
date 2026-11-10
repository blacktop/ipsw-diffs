## h16_ane_fw_leto_j7x.im4p

> `Firmware/ane/h16_ane_fw_leto_j7x.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._fwinfo`
- `__DATA._rtk_mtab`
- `__DATA.__data_copy`

```diff

-  __TEXT.__text: 0x9b63c
-  __TEXT.__cstring: 0x14d58
-  __TEXT.__const: 0x4254
+  __TEXT.__text: 0x9b7a4
+  __TEXT.__const: 0x4258
+  __TEXT.__cstring: 0x14d89
   __TEXT.ce_env: 0x4000
-  __TEXT.text_env: 0x20
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
+  __TEXT.text_env: 0x20
   __DATA.__const: 0x4718
   __DATA._rtk_heap: 0x0
   __DATA.__data: 0xf30

   __DATA._rtk_page_tables: 0x80000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
-  __DATA._rtk_boot_l1: 0x80
-  __DATA._rtk_mtab: 0x2a0
-  __DATA.__gxf_data: 0x10
   __DATA.__data_copy: 0x8000
   __DATA.__sysvars: 0x10
+  __DATA._rtk_mtab: 0x2a0
+  __DATA._rtk_boot_l1: 0x80
+  __DATA.__chain_starts: 0x24
   __DATA.__mod_init_func: 0x0
-  __DATA.__chain_starts: 0x1c
-  __DATA.__zerofill: 0x1f5000
-  Functions: 1373
+  __DATA.__gxf_data: 0x10
+  __DATA.__zerofill: 0x1f9000
+  Functions: 1374
   Symbols:   0
-  CStrings:  2315
+  CStrings:  2316
 
CStrings:
+ "./sne/aneEngine/exeLoop/CAneEngineExeLoopH16.cpp"
+ "22:07:50"
+ "Oct  7 2026"
- "14:58:47"
- "Aug  8 2026"
```
