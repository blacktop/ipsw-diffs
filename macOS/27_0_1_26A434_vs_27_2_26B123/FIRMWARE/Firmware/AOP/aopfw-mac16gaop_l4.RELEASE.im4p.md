## aopfw-mac16gaop_l4.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16gaop_l4.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__const`
- `__DATA.__data`
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
+  __TEXT.__text: 0xb3dd0
+  __TEXT.__const: 0xa85c
+  __TEXT.__cstring: 0x7a55
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000
-  __DATA._spu_stack: 0xe000
+  __DATA._spu_stack: 0xf000
   __DATA._rtk_init_stack: 0x3000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xab518
-  __ETEXT.__text: 0x13470
+  __DATA.__zerofill: 0xab798
+  __ETEXT.__text: 0x13468
   __ETEXT.__StaticInit: 0x2110
   __ETEXT.__const: 0x580
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x29442
+  __OS_LOG.__string: 0x29441
   __MISC.__apf_list: 0x30
   __CMA.__cma_log_string: 0x1259
-  Functions: 2777
+  Functions: 2776
   Symbols:   0
   CStrings:  2945
 
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
