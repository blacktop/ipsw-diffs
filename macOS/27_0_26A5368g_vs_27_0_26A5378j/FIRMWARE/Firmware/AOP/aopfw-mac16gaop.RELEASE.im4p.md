## aopfw-mac16gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16gaop.RELEASE.im4p`

```diff

-  __TEXT.__text: 0xb2d5c
-  __TEXT.__const: 0xa838
-  __TEXT.__cstring: 0x5a7c
+  __TEXT.__text: 0xb2a84
+  __TEXT.__const: 0xa848
+  __TEXT.__cstring: 0x5a3b
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x14240
-  __DATA.__const: 0xefc0
+  __DATA.__const: 0xefa8
   __DATA.__data: 0x72c0
   __DATA._rtk_patchbay: 0x2fa
   __DATA._rtk_mtab: 0x5e0

   __DATA._spu_service: 0x390
   __DATA._spu_endpoint: 0x40
   __DATA._rtk_power: 0x3b8
-  __DATA.__cmevent: 0x3d8
+  __DATA.__cmevent: 0x3c0
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x6a0
   __DATA.__mod_init_func: 0x120

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xab1d8
-  __ETEXT.__text: 0x133c4
-  __ETEXT.__StaticInit: 0x2120
+  __DATA.__zerofill: 0xab0f8
+  __ETEXT.__text: 0x133dc
+  __ETEXT.__StaticInit: 0x2110
   __ETEXT.__const: 0x570
-  __ETEXT.__eh_frame: 0x40
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x2ccaf
+  __OS_LOG.__string: 0x2cd2a
   __MISC.__apf_list: 0x30
   __CMA.__cma_log_string: 0x1213
-  Functions: 2820
+  Functions: 2795
   Symbols:   0
-  CStrings:  2936
+  CStrings:  2939
 
Sections:
~ __TEXT.__chain_starts : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__version : content changed
~ __DATA._spu_service : content changed
~ __DATA._spu_endpoint : content changed
~ __DATA._rtk_power : content changed
~ __DATA.__mod_init_func : content changed
CStrings:
+ "%s:hDr"
+ "%s:hON"
+ "%s:idx"
+ "%s:lDr"
+ "%s:lOF"
+ "%s:lON"
+ "%s:mnD"
+ "%s:mxD"
+ "%s:nAP"
+ "%s:nON"
+ "%s:tON"
+ "19:45:46"
+ "23:28:01"
+ "23:28:03"
+ "AppleSPUFirmware-2444.0.11~143"
+ "Jun 26 2026"
+ "WKP-STATS-%c"
+ "[AUD] RTK exp \"RTK_stack_guard_guard(&stackBase, stackSize)\" fail, %s(), ln 60, stat %#x"
+ "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
+ "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 44, stat %#x"
+ "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 91, stat %#x"
+ "[AUD] fail, stat %#x, %s(), ln 52"
- "00:20:36"
- "00:25:02"
- "00:25:03"
- "AP alr on"
- "AppleSPUFirmware-2444.0.1.0.1~439"
- "Dur history (us)"
- "Jun 13 2026"
- "Last OFF (us)"
- "Last ON (us)"
- "Last dur (us)"
- "Max dur (us)"
- "Min dur (us)"
- "Num ON trans"
- "ON time history (us)"
- "Total ON (us)"
- "WKP-%c-%s"
- "[AUD] RTKitAudioFramework v601.36 ('%s' built %s %s) ready!! {%zu nodes}"
- "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 31, stat %#x"
- "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 57, stat %#x"

```
