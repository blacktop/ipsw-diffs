## aopfw-mac15saop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac15saop.RELEASE.im4p`

```diff

-  __TEXT.__text: 0x94838
-  __TEXT.__const: 0x59f8
-  __TEXT.__cstring: 0x66c1
+  __TEXT.__text: 0x94464
+  __TEXT.__const: 0x5a08
+  __TEXT.__cstring: 0x66e4
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x2ff68
-  __DATA.__const: 0xa410
+  __DATA.__const: 0xa3e8
   __DATA.__data: 0x95f8
   __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x638

   __DATA._spu_service: 0x3c0
   __DATA._spu_endpoint: 0x60
   __DATA._rtk_power: 0x3b8
-  __DATA.__cmevent: 0x3d8
+  __DATA.__cmevent: 0x3c0
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x5b0
   __DATA.__mod_init_func: 0x130

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xbaaf8
-  __ETEXT.__text: 0x17744
-  __ETEXT.__StaticInit: 0x2a90
+  __DATA.__zerofill: 0xbab38
+  __ETEXT.__text: 0x17400
+  __ETEXT.__StaticInit: 0x2a88
   __ETEXT.__const: 0xbe8
-  __ETEXT.__eh_frame: 0x40
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x12db8
+  __OS_LOG.__string: 0x12e33
   __MISC.__apf_list: 0x70
   __CMA.__cma_log_string: 0x1213
-  Functions: 2575
+  Functions: 2549
   Symbols:   0
-  CStrings:  2054
+  CStrings:  2057
 
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
+ "19:45:07"
+ "23:27:55"
+ "AppleSPUFirmware-2444.0.11~143"
+ "Jun 26 2026"
+ "WKP-STATS-%c"
+ "[AUD] RTK exp \"RTK_stack_guard_guard(&stackBase, stackSize)\" fail, %s(), ln 60, stat %#x"
+ "[AUD] RTKitAudioFramework v601.41 ('%s' built %s %s) ready!! {%zu nodes}"
+ "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 44, stat %#x"
+ "[AUD] cond \"!(mWorkloopPtr != nullptr)\" fail, %s() ln 91, stat %#x"
+ "[AUD] fail, stat %#x, %s(), ln 52"
+ "start + size <= instance->_region.buffer.size"
+ "start == write_offset"
+ "start > instance->_region.buffer.size - 1024 * cache_line_size"
- "00:20:01"
- "00:24:57"
- "1k6filter=["
- "1k6mode=["
- "1k6odr=["
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
