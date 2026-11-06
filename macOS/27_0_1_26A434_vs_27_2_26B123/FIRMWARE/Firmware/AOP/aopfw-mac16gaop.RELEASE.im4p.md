## aopfw-mac16gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16gaop.RELEASE.im4p`

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

-  __TEXT.__text: 0xb3718
-  __TEXT.__const: 0xa8a0
-  __TEXT.__cstring: 0x5adc
+  __TEXT.__text: 0xb37f8
+  __TEXT.__const: 0xa874
+  __TEXT.__cstring: 0x5add
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
-  __ETEXT.__text: 0x13474
+  __DATA.__zerofill: 0xab7b8
+  __ETEXT.__text: 0x1346c
   __ETEXT.__StaticInit: 0x2110
   __ETEXT.__const: 0x580
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x2ce11
+  __OS_LOG.__string: 0x2ce10
   __MISC.__apf_list: 0x30
   __CMA.__cma_log_string: 0x1259
-  Functions: 2776
+  Functions: 2775
   Symbols:   0
   CStrings:  2942
 
CStrings:
+ "13:48:46"
+ "13:53:15"
+ "13:53:16"
+ "AppleSPUFirmware-2444.41.1~32"
+ "Oct  3 2026"
+ "[AUD] RTKitAudioFramework v610.1 ('%s' built %s %s) ready!! {%zu nodes}"
- "13:01:27"
- "13:06:06"
- "13:06:07"
- "AppleSPUFirmware-2444.1.1~64"
- "Aug  8 2026"
- "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
```
