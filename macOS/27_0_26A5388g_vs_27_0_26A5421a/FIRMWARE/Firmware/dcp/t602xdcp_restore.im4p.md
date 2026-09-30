## t602xdcp_restore.im4p

> `Firmware/dcp/t602xdcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`

```diff

-  __TEXT.__text: 0x2f715c
-  __TEXT.__const: 0x3aa258
+  __TEXT.__text: 0x2f810c
+  __TEXT.__const: 0x3aa2f8
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x3859a
+  __TEXT.__cstring: 0x3898f
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x37db8
+  __DATA.__const: 0x37e90
   __DATA.__data: 0x118468
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x5b0

   __DATA._afk_sys_objt: 0xba0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x330e0
+  __DATA.__zerofill: 0x33110
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA._rtk_mtab: 0x448
   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
-  __OS_LOG.__string: 0x23834
-  Functions: 7228
+  __OS_LOG.__string: 0x23881
+  Functions: 7236
   Symbols:   0
-  CStrings:  8800
+  CStrings:  8819
 
CStrings:
+ " [AppleDCPDPTXController.cpp::%d] DCPAV[%d] %s::%s color de-saturation WA %s"
+ "%s: connected sink advertises %u max DSC slices per line"
+ "%s: no vi for DSC caps"
+ "A442_callback__"
+ "A444_callback__"
+ "A450_callback__"
+ "BICSDaemonPanicOnStartFail"
+ "Could not determine blend space; assuming sRGB"
+ "Link integrity failure, aborting.."
+ "TE missing for %u seconds"
+ "This monitor has timing with vblank=%d us < spec threshold of %d us"
+ "av_cp_integrity_panic"
+ "color de-saturation WA %s"
+ "getPlatformExtDisplayLimits"
+ "iomfb_RuntimeProperty_useBAEForSBIM"
+ "iomfb_bics_daemon_start_fail_panic"
+ "m3_event_callback_gated: missing TE recovery timer unavailable, recovery panic guard disabled for this outage"
+ "missing_te_display_recovery: TE still not updating after timeout, panicking"
+ "missing_te_display_recovery: TE updating, skipping recovery panic"
+ "missing_te_display_recovery: recovery timer expired but no missing TE was recorded as started, skipping"
+ "setup_missing_te_display_recovery_monitor: failed to register recovery timer monitor, duplicate or invalid index"
+ "setup_missing_te_display_recovery_monitor: no event manager available, recovery timer not set up"
+ "setup_missing_te_display_recovery_monitor: recovery timer expired, invoking missing TE display recovery"
+ "setup_missing_te_display_recovery_monitor: recovery timer set up, timeout %u ms"
+ "useBAEForSBIM"
- "%s: VI elements null (color=%p timing=%p)"
- "A440_callback__"
- "A443_callback__"
- "A449_callback__"
- "IOMFB removing mode: %d x %d @ %d Hz (vertical blanking %dus < %dus)"
- "This monitor has timing with vblank=%d us < spec threshold of 300us \n"
```
