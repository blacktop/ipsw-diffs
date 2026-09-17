## aopfw-mac16gaop_l4.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16gaop_l4.RELEASE.im4p`

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

-  __TEXT.__text: 0xb3cec
-  __TEXT.__const: 0xa878
-  __TEXT.__cstring: 0x7a54
+  __TEXT.__text: 0xb3d9c
+  __TEXT.__const: 0xa85c
+  __TEXT.__cstring: 0x7a5a
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000
-  __DATA._spu_stack: 0xe000
+  __DATA._spu_stack: 0xf000
   __DATA._rtk_init_stack: 0x3000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x14220
   __DATA.__const: 0xefa8
-  __DATA.__data: 0x72c8
+  __DATA.__data: 0x72c0
   __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5e0
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xab518
-  __ETEXT.__text: 0x13470
+  __DATA.__zerofill: 0xab7f8
+  __ETEXT.__text: 0x13460
   __ETEXT.__StaticInit: 0x2110
   __ETEXT.__const: 0x580
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x29442
+  __OS_LOG.__string: 0x29441
   __MISC.__apf_list: 0x30
   __CMA.__cma_log_string: 0x1259
   Functions: 2777
CStrings:
+ "AppleSPUFirmware-2444.40.15.0.1~21"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "AppleSPUFirmware-2444.1.1~64"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
