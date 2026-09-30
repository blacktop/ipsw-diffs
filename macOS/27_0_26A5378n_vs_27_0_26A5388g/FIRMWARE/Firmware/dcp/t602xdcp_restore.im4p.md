## t602xdcp_restore.im4p

> `Firmware/dcp/t602xdcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x2f7190
+  __TEXT.__text: 0x2f715c
   __TEXT.__const: 0x3aa258
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x38565
+  __TEXT.__cstring: 0x3859a
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x37db8

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x23834
-  Functions: 7230
+  Functions: 7228
   Symbols:   0
-  CStrings:  8799
+  CStrings:  8800
 
CStrings:
+ "!MIDR: 0x%x"
+ "update_hdcp_encryption_status: startThread failed 0x%x"
- "!MIDR: 0x%llx"
```
