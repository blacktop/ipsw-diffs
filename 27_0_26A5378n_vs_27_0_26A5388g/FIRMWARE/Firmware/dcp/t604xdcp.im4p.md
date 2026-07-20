## t604xdcp.im4p

> `Firmware/dcp/t604xdcp.im4p`

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

-  __TEXT.__text: 0x30a804
+  __TEXT.__text: 0x30a7b8
   __TEXT.__const: 0x3b3a78
   __TEXT.__chain_starts: 0x34
-  __TEXT.__cstring: 0x39cd4
+  __TEXT.__cstring: 0x39d09
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x3add8

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x24133
-  Functions: 7427
+  Functions: 7425
   Symbols:   0
-  CStrings:  8993
+  CStrings:  8994
 
CStrings:
+ "!MIDR: 0x%x"
+ "update_hdcp_encryption_status: startThread failed 0x%x"
- "!MIDR: 0x%llx"
```
