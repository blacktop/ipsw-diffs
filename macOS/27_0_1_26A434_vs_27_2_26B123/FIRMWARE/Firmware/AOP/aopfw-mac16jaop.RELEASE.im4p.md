## aopfw-mac16jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16jaop.RELEASE.im4p`

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

-  __TEXT.__text: 0xbdb00
-  __TEXT.__const: 0x9e78
-  __TEXT.__cstring: 0x525b
+  __TEXT.__text: 0xbdbc0
+  __TEXT.__const: 0x9e84
+  __TEXT.__cstring: 0x525c
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
   __DATA._rtk_heap: 0x2de20
   __DATA.__const: 0xe008
-  __DATA.__data: 0x7158
+  __DATA.__data: 0x7150
   __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5f8
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xb15a0
-  __ETEXT.__text: 0x12418
+  __DATA.__zerofill: 0xb1840
+  __ETEXT.__text: 0x12410
   __ETEXT.__StaticInit: 0x1c54
   __ETEXT.__const: 0x4c0
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x2c8a1
+  __OS_LOG.__string: 0x2c8a0
   __MISC.__apf_list: 0x80
   __CMA.__cma_log_string: 0x1259
-  Functions: 2652
+  Functions: 2651
   Symbols:   0
   CStrings:  2874
 
CStrings:
+ "13:48:09"
+ "13:53:15"
+ "13:53:16"
+ "AppleSPUFirmware-2444.41.1~32"
+ "Oct  3 2026"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "13:00:56"
- "13:06:06"
- "13:06:07"
- "AppleSPUFirmware-2444.1.1~64"
- "Aug  8 2026"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
