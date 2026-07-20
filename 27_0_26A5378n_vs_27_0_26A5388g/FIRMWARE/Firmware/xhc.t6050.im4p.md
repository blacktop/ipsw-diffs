## xhc.t6050.im4p

> `Firmware/xhc.t6050.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_vtor`
- `__TEXT.__const`
- `__TEXT._rtk_mtab`
- `__DATA.__data`
- `__DATA.__zerofill`
- `__OS_LOG.__string`
- `__VTOR._rtk_vtor_patch`

```diff

-  __TEXT.__text: 0x15d34
+  __TEXT.__text: 0x15d88
   __TEXT._rtk_vtor: 0x300
   __TEXT.__const: 0x7d4
   __TEXT._rtk_mtab: 0x194
CStrings:
+ "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-242.0.1~498.t6050)"
- "main.c:32::XHC firmware started (FW build version: AppleXHCFirmware-242.0.1~119.t6050)"
```
