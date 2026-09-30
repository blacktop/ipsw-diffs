## aopfw-mac14jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac14jaop.RELEASE.im4p`

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

-  __TEXT.__text: 0x82ea4
-  __TEXT.__const: 0x5270
-  __TEXT.__cstring: 0x60be
+  __TEXT.__text: 0x82f28
+  __TEXT.__const: 0x5268
+  __TEXT.__cstring: 0x60bb
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x2000
   __DATA._rtk_page_tables: 0x4000
-  __DATA._spu_stack: 0x1800
+  __DATA._spu_stack: 0x5000
   __DATA._rtk_init_stack: 0x2000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0x71040
-  __ETEXT.__text: 0x11d18
+  __DATA.__zerofill: 0x70fe0
+  __ETEXT.__text: 0x11cec
   __ETEXT.__StaticInit: 0x872c
   __ETEXT.__const: 0x47b
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x1170d
+  __OS_LOG.__string: 0x1172c
   __MISC.__apf_list: 0x70
-  __CMA.__cma_log_string: 0x1213
-  Functions: 2154
+  __CMA.__cma_log_string: 0x123f
+  Functions: 2151
   Symbols:   0
   CStrings:  1893
 
CStrings:
+ "!MIDR: 0x%x"
+ "23:59:37"
+ "AppleSPUFirmware-2444.0.12~90"
+ "Jul  9 2026"
+ "SMCKeys: discarding late reply for timed-out request"
- "!MIDR: 0x%llx"
- "19:45:07"
- "AppleSPUFirmware-2444.0.11~143"
- "Jun 26 2026"
- "SMC: Too many retries"
```
