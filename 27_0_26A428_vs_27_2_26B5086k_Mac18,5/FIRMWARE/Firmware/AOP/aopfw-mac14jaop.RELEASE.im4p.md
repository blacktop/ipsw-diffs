## aopfw-mac14jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac14jaop.RELEASE.im4p`

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

-  __TEXT.__text: 0x83bd0
-  __TEXT.__const: 0x52c0
-  __TEXT.__cstring: 0x615f
+  __TEXT.__text: 0x83c54
+  __TEXT.__const: 0x52b0
+  __TEXT.__cstring: 0x6165
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x2000
   __DATA._rtk_page_tables: 0x4000
-  __DATA._spu_stack: 0x6000
+  __DATA._spu_stack: 0x7000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x13f68
   __DATA.__const: 0x8c88
-  __DATA.__data: 0x9b80
+  __DATA.__data: 0x9b78
   __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x638
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x71480
-  __ETEXT.__text: 0x11d90
+  __DATA.__zerofill: 0x71740
+  __ETEXT.__text: 0x11d80
   __ETEXT.__StaticInit: 0x8734
   __ETEXT.__const: 0x47b
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x117e6
+  __OS_LOG.__string: 0x117e5
   __MISC.__apf_list: 0x70
   __CMA.__cma_log_string: 0x1259
   Functions: 2135
CStrings:
+ "AppleSPUFirmware-2444.40.15.0.1~21"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "AppleSPUFirmware-2444.1.1~64"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
