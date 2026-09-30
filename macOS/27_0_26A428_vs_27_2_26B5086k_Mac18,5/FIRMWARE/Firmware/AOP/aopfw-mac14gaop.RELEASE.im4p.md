## aopfw-mac14gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac14gaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__const`
- `__DATA._rtk_mtab`
- `__DATA._rtk_patchbay`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._spu_endpoint`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x87b74
-  __TEXT.__const: 0x5528
-  __TEXT.__cstring: 0x6a7d
+  __TEXT.__text: 0x87bf8
+  __TEXT.__const: 0x5538
+  __TEXT.__cstring: 0x6a83
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
   __DATA._rtk_heap: 0x14b68
   __DATA.__const: 0x8c88
-  __DATA.__data: 0x96f0
+  __DATA.__data: 0x96e0
   __DATA._rtk_mtab: 0x6b8
   __DATA._rtk_patchbay: 0x306
   __DATA.__version: 0x8

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x73640
-  __ETEXT.__text: 0x12de8
+  __DATA.__zerofill: 0x73920
+  __ETEXT.__text: 0x12dd8
   __ETEXT.__StaticInit: 0x62b8
   __ETEXT.__const: 0x47b
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x11975
+  __OS_LOG.__string: 0x11974
   __MISC.__apf_list: 0x90
   __CMA.__cma_log_string: 0x1259
   Functions: 2176
CStrings:
+ "AppleSPUFirmware-2444.40.15.0.1~21"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "AppleSPUFirmware-2444.1.1~64"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
