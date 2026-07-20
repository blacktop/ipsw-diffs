## t600xdcp.im4p

> `Firmware/dcp/t600xdcp.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__chain_starts`
- `__DATA.__const`
- `__DATA._rtk_patchbay`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`
- `__DATA._rtk_mtab`

```diff

-  __TEXT.__text: 0x325854
+  __TEXT.__text: 0x325804
   __TEXT.__const: 0x3cbcb8
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x378c6
+  __TEXT.__cstring: 0x378fb
   __TEXT.__padding1: 0x1
   __TEXT.__padding2: 0x1
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x37ca8
-  __DATA.__data: 0x129688
+  __DATA.__data: 0x129690
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x1e8
   __DATA._rtk_boot: 0x9000

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x227ac
-  Functions: 7303
+  Functions: 7301
   Symbols:   0
-  CStrings:  8635
+  CStrings:  8636
 
CStrings:
+ "!MIDR: 0x%x"
+ "update_hdcp_encryption_status: startThread failed 0x%x"
- "!MIDR: 0x%llx"
```
