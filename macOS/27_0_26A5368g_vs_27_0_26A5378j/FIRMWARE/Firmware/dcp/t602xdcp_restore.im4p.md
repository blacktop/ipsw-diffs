## t602xdcp_restore.im4p

> `Firmware/dcp/t602xdcp_restore.im4p`

```diff

-  __TEXT.__text: 0x2f76a8
-  __TEXT.__const: 0x3aa230
+  __TEXT.__text: 0x2f7190
+  __TEXT.__const: 0x3aa258
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x38469
+  __TEXT.__cstring: 0x38565
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x37dd0
+  __DATA.__const: 0x37db8
   __DATA.__data: 0x118468
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x5b0

   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
   __OS_LOG.__string: 0x23834
-  Functions: 7228
+  Functions: 7230
   Symbols:   0
-  CStrings:  8795
+  CStrings:  8799
 
Sections:
~ __TEXT.__chain_starts : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__mod_init_func : content changed
~ __DATA._afk_sys_objt : content changed
~ __DATA._rtk_data_uuid : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__constructor : content changed
~ __OS_LOG.__string : content changed
CStrings:
+ "%s: VI elements null (color=%p timing=%p)"
+ "%s: min_bright 0x%x %strusted, max_bright 0x%x %strusted, max_user_reachable_brightness 0x%x\n"
+ "IOMFB: vblank_duration_us %u (v_total %u height %u line_time %d)\n"
+ "MaxSrcRectHeightForPipe"
+ "MaxSrcRectWidthForPipe"
+ "VI elements null (color=%p timing=%p), display unplugged during modeset; dropping color setup"
+ "parseSDPLineTrigger"
+ "vblank_duration_us"
- "%s: min_bright 0x%x %strusted, max_bright 0x%x %strusted\n"
- "MaxSrcRectTotal"
- "MaxSrcRectWidth"
- "set_external_sync_gated sync_clock: %d\n"

```
