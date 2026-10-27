## t603x_ane0_fw_erebus_ls5x.im4p

> `Firmware/ane/t603x_ane0_fw_erebus_ls5x.im4p`

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

-  __TEXT.__text: 0x9f174
+  __TEXT.__text: 0x9f290
+  __TEXT.__const: 0x10278
   __TEXT.__cstring: 0x154c2
-  __TEXT.__const: 0x10264
-  __TEXT.text_env: 0x20
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
+  __TEXT.text_env: 0x20
   __DATA.__const: 0x52f0
   __DATA._rtk_heap: 0x0
   __DATA.__data: 0xf38

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
+  __DATA.__chain_starts: 0x28
   __DATA.__mod_init_func: 0x0
-  __DATA.__chain_starts: 0x1c
-  __DATA.__zerofill: 0x1e9000
-  Functions: 1402
+  __DATA.__gxf_data: 0x10
+  __DATA.__zerofill: 0x1ed000
+  Functions: 1403
   Symbols:   0
   CStrings:  2363
 
CStrings:
+ "22:00:14"
+ "Oct  7 2026"
- "15:04:08"
- "Aug  8 2026"
```
