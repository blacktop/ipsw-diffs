## aopfw-mac15jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac15jaop.RELEASE.im4p`

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

-  __TEXT.__text: 0xa448c
-  __TEXT.__const: 0x59e8
-  __TEXT.__cstring: 0x6726
+  __TEXT.__text: 0xa450c
+  __TEXT.__const: 0x59e0
+  __TEXT.__cstring: 0x672f
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000
-  __DATA._spu_stack: 0x1800
+  __DATA._spu_stack: 0x5000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xbb438
-  __ETEXT.__text: 0x173d0
+  __DATA.__zerofill: 0xbb3d8
+  __ETEXT.__text: 0x173a4
   __ETEXT.__StaticInit: 0x2c04
   __ETEXT.__const: 0xbe8
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x12eee
+  __OS_LOG.__string: 0x12f0d
   __MISC.__apf_list: 0x70
-  __CMA.__cma_log_string: 0x1213
-  Functions: 3282
+  __CMA.__cma_log_string: 0x123f
+  Functions: 3279
   Symbols:   0
-  CStrings:  2057
+  CStrings:  2058
 
CStrings:
+ "!MIDR: 0x%x"
+ "00:05:40"
+ "23:59:37"
+ "AppleSPUFirmware-2444.0.12~90"
+ "Jul  9 2026"
+ "Jul 10 2026"
+ "SMCKeys: discarding late reply for timed-out request"
- "!MIDR: 0x%llx"
- "19:45:07"
- "23:27:55"
- "AppleSPUFirmware-2444.0.11~143"
- "Jun 26 2026"
- "SMC: Too many retries"
```
