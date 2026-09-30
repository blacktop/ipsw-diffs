## aopfw-mac13jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac13jaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__const`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_mtab`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._spu_endpoint`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x805f8
-  __TEXT.__const: 0x5150
-  __TEXT.__cstring: 0x13109
+  __TEXT.__text: 0x80678
+  __TEXT.__const: 0x5148
+  __TEXT.__cstring: 0x1310e
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x2000
   __DATA._rtk_page_tables: 0x4000
-  __DATA._spu_stack: 0x5000
+  __DATA._spu_stack: 0x6000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x12768
   __DATA.__const: 0x84b0
-  __DATA.__data: 0x8c70
+  __DATA.__data: 0x8c68
   __DATA._rtk_patchbay: 0x31e
   __DATA._rtk_mtab: 0x628
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x703b0
-  __ETEXT.__text: 0xfae4
+  __DATA.__zerofill: 0x70690
+  __ETEXT.__text: 0xfad4
   __ETEXT.__StaticInit: 0x73b8
   __ETEXT.__const: 0x47b
   __EDATA.__data: 0x1cc0
CStrings:
+ "AppleSPUFirmware-2444.40.15.0.1~21"
+ "RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "AppleSPUFirmware-2444.1.1~64"
- "RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
