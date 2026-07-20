## t6030dcp_restore.im4p

> `Firmware/dcp/t6030dcp_restore.im4p`

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

-  __TEXT.__text: 0x2e4bb8
+  __TEXT.__text: 0x2e4b5c
   __TEXT.__const: 0x3ab478
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x381ef
+  __TEXT.__cstring: 0x38224
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x37408

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x23f41
-  Functions: 7213
+  Functions: 7211
   Symbols:   0
-  CStrings:  8835
+  CStrings:  8836
 
CStrings:
+ "!MIDR: 0x%x"
+ "update_hdcp_encryption_status: startThread failed 0x%x"
- "!MIDR: 0x%llx"
```
