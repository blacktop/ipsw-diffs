## h18_ane0_fw_kirkland_j8xx.im4p

> `Firmware/ane/h18_ane0_fw_kirkland_j8xx.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA._fwinfo`
- `__DATA._rtk_mtab`
- `__DATA.__data_copy`

```diff

-  __TEXT.__text: 0x9f968
+  __TEXT.__text: 0x9fa84
+  __TEXT.__const: 0x4d08
   __TEXT.__cstring: 0x15b1f
-  __TEXT.__const: 0x4cf4
   __TEXT.ce_env: 0x4000
-  __TEXT.text_env: 0x20
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
+  __TEXT.text_env: 0x20
   __DATA.__const: 0x7e28
   __DATA._rtk_heap: 0x0
   __DATA.__data: 0xf10

   __DATA._rtk_page_tables: 0x80000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
-  __DATA._rtk_boot_l1: 0x80
-  __DATA._rtk_mtab: 0x268
-  __DATA.__gxf_data: 0x10
   __DATA.__data_copy: 0x8000
   __DATA.__sysvars: 0x10
+  __DATA._rtk_boot_l1: 0x80
+  __DATA.__chain_starts: 0x20
+  __DATA._rtk_mtab: 0x268
   __DATA.__mod_init_func: 0x0
-  __DATA.__chain_starts: 0x1c
+  __DATA.__gxf_data: 0x10
   __DATA.__zerofill: 0x1f4000
-  Functions: 1432
+  Functions: 1434
   Symbols:   0
   CStrings:  2426
 
CStrings:
+ "22:11:33"
+ "Oct  7 2026"
- "15:08:13"
- "Aug  8 2026"
```
