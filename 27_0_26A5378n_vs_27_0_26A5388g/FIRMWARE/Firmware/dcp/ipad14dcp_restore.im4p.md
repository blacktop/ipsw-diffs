## ipad14dcp_restore.im4p

> `Firmware/dcp/ipad14dcp_restore.im4p`

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

-  __TEXT.__text: 0x300098
+  __TEXT.__text: 0x300014
   __TEXT.__const: 0x3cb6c0
   __TEXT.__chain_starts: 0x2c
-  __TEXT.__cstring: 0x37f83
+  __TEXT.__cstring: 0x37fb8
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x37fd8

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x23647
-  Functions: 7298
+  Functions: 7296
   Symbols:   0
-  CStrings:  8744
+  CStrings:  8745
 
CStrings:
+ "!MIDR: 0x%x"
+ "update_hdcp_encryption_status: startThread failed 0x%x"
- "!MIDR: 0x%llx"
```
