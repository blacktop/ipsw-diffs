## aopfw-mac15saop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac15saop.RELEASE.im4p`

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

-  __TEXT.__text: 0x95328
-  __TEXT.__const: 0x5a60
-  __TEXT.__cstring: 0x6785
+  __TEXT.__text: 0x95410
+  __TEXT.__const: 0x5a50
+  __TEXT.__cstring: 0x6786
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000
-  __DATA._spu_stack: 0x6000
+  __DATA._spu_stack: 0x7000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x2ff68
   __DATA.__const: 0xa3f8
-  __DATA.__data: 0x95f8
+  __DATA.__data: 0x95f0
   __DATA._rtk_patchbay: 0x312
   __DATA._rtk_mtab: 0x638
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xbaff8
-  __ETEXT.__text: 0x17494
+  __DATA.__zerofill: 0xbb278
+  __ETEXT.__text: 0x1748c
   __ETEXT.__StaticInit: 0x2a90
   __ETEXT.__const: 0xbe8
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x12f0c
+  __OS_LOG.__string: 0x12f0b
   __MISC.__apf_list: 0x70
   __CMA.__cma_log_string: 0x1259
-  Functions: 2528
+  Functions: 2527
   Symbols:   0
   CStrings:  2061
 
CStrings:
+ "13:48:09"
+ "13:53:11"
+ "AppleSPUFirmware-2444.41.1~32"
+ "Oct  3 2026"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "13:00:56"
- "13:06:01"
- "AppleSPUFirmware-2444.1.1~64"
- "Aug  8 2026"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
