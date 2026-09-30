## t8132dcp_restore.im4p

> `Firmware/dcp/t8132dcp_restore.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`

```diff

-  __TEXT.__text: 0x382554
-  __TEXT.__const: 0x47c53c
+  __TEXT.__text: 0x38308c
+  __TEXT.__const: 0x47c5b4
   __TEXT.__chain_starts: 0x3c
-  __TEXT.__cstring: 0x3d488
+  __TEXT.__cstring: 0x3d5f9
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x5ac30
+  __DATA.__const: 0x5ad08
   __DATA.__data: 0x15c17c
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x6a0

   __DATA._afk_sys_objt: 0xc70
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x6ba80
+  __DATA.__zerofill: 0x6c6b0
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA._rtk_mtab: 0x828
   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
-  __OS_LOG.__string: 0x2549c
+  __OS_LOG.__string: 0x254e9
   Functions: 8142
   Symbols:   0
-  CStrings:  9507
+  CStrings:  9522
 
CStrings:
+ " [AppleDCPDPTXController.cpp::%d] DCPAV[%d] %s::%s color de-saturation WA %s"
+ "%s: connected sink advertises %u max DSC slices per line"
+ "%s: no vi for DSC caps"
+ "A442_callback__"
+ "A444_callback__"
+ "A450_callback__"
+ "BIC pool exhausted (no free buffer)"
+ "BICS do_gain failed [0x%X]"
+ "BICS do_tbics_gain failed [0x%X]"
+ "BICSDaemonPanicOnStartFail"
+ "Could not determine blend space; assuming sRGB"
+ "Link integrity failure, aborting.."
+ "TBICS gain calc: %s"
+ "This monitor has timing with vblank=%d us < spec threshold of %d us"
+ "av_cp_integrity_panic"
+ "color de-saturation WA %s"
+ "getPlatformExtDisplayLimits"
+ "iomfb_RuntimeProperty_useBAEForSBIM"
+ "iomfb_bics_daemon_start_fail_panic"
+ "no TBICS params"
+ "useBAEForSBIM"
- "%s: VI elements null (color=%p timing=%p)"
- "A440_callback__"
- "A443_callback__"
- "A449_callback__"
- "IOMFB removing mode: %d x %d @ %d Hz (vertical blanking %dus < %dus)"
- "This monitor has timing with vblank=%d us < spec threshold of 300us \n"
```
