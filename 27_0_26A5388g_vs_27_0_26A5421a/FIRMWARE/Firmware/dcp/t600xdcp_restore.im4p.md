## t600xdcp_restore.im4p

> `Firmware/dcp/t600xdcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`

```diff

-  __TEXT.__text: 0x3221e8
-  __TEXT.__const: 0x3cbcc8
+  __TEXT.__text: 0x323114
+  __TEXT.__const: 0x3cbd78
   __TEXT.__chain_starts: 0x30
-  __TEXT.__cstring: 0x378fb
+  __TEXT.__cstring: 0x37cf0
   __TEXT.__padding1: 0x1
   __TEXT.__padding2: 0x1
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x37ca8
-  __DATA.__data: 0x129690
+  __DATA.__const: 0x37d80
+  __DATA.__data: 0x129688
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x1e8
   __DATA._rtk_boot: 0x9000

   __DATA._afk_sys_objt: 0xba0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x32588
+  __DATA.__zerofill: 0x325a8
   __DATA.__afk_obj_num: 0x210
   __DATA.__padding1: 0x1
   __DATA.__padding2: 0x1

   __DATA._rtk_mtab: 0x430
   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
-  __OS_LOG.__string: 0x227ac
-  Functions: 7304
+  __OS_LOG.__string: 0x227f9
+  Functions: 7313
   Symbols:   0
-  CStrings:  8636
+  CStrings:  8655
 
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
