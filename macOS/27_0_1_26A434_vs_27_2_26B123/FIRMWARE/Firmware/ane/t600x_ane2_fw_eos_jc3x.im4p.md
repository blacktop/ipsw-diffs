## t600x_ane2_fw_eos_jc3x.im4p

> `Firmware/ane/t600x_ane2_fw_eos_jc3x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__data_copy`

```diff

-  __TEXT.__text: 0xa1908
+  __TEXT.__text: 0xa1a70
+  __TEXT.__const: 0x3bb48
   __TEXT.__cstring: 0x15ccd
-  __TEXT.__const: 0x3bb54
-  __TEXT.text_env: 0x28
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
+  __TEXT.text_env: 0x28
   __DATA.__const: 0x53e8
   __DATA._rtk_heap: 0x0
   __DATA.__data: 0xe30

   __DATA._rtk_page_tables: 0x3c0000
   __DATA._rtk_threads: 0x0
   __DATA._fwinfo: 0x100
-  __DATA._rtk_boot_l1: 0x80
-  __DATA._rtk_mtab: 0x288
-  __DATA.__gxf_data: 0x10
   __DATA.__data_copy: 0x8000
   __DATA.__sysvars: 0x10
+  __DATA._rtk_mtab: 0x288
+  __DATA._rtk_boot_l1: 0x80
+  __DATA.__chain_starts: 0x28
   __DATA.__mod_init_func: 0x0
-  __DATA.__chain_starts: 0x1c
+  __DATA.__gxf_data: 0x10
   __DATA.__zerofill: 0x201000
-  Functions: 1361
+  Functions: 1362
   Symbols:   0
   CStrings:  2391
 
CStrings:
+ "21:55:54"
+ "Oct  7 2026"
- "14:59:32"
- "Aug  8 2026"
```
