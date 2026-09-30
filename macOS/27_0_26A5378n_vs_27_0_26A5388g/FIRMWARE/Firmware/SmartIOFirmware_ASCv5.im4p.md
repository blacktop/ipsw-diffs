## SmartIOFirmware_ASCv5.im4p

> `Firmware/SmartIOFirmware_ASCv5.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT._rtk_mtab`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x1a560
-  __TEXT.__cstring: 0x1064
+  __TEXT.__text: 0x1a4dc
+  __TEXT.__cstring: 0x1062
   __TEXT.__const: 0x2c8
   __TEXT._rtk_mtab: 0x290
   __TEXT.__constructor: 0x0

   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
-  __DATA._rtk_boot: 0x1000
+  __DATA._rtk_boot: 0x2000
   __DATA._rtk_page_tables: 0x21000
   __DATA._rtk_patchbay: 0x211
   __DATA._rtk_power: 0x358
CStrings:
+ "!MIDR: 0x%x"
- "!MIDR: 0x%llx"
```
