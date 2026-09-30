## t604xdcp.im4p

> `Firmware/dcp/t604xdcp.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA._rtk_patchbay`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`
- `__DATA._afk_sys_objt`
- `__DATA._rtk_data_uuid`

```diff

-  __TEXT.__text: 0x30a7b8
-  __TEXT.__const: 0x3b3a78
+  __TEXT.__text: 0x30b294
+  __TEXT.__const: 0x3b3b10
   __TEXT.__chain_starts: 0x34
-  __TEXT.__cstring: 0x39d09
+  __TEXT.__cstring: 0x39df6
   __TEXT.__lcxx_override: 0x24
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x3add8
+  __DATA.__const: 0x3aeb0
   __DATA.__data: 0x11f4c0
   __DATA._rtk_patchbay: 0x75a
   __DATA._rtk_tunables: 0x6a0

   __DATA._afk_sys_objt: 0xbe0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5d5f0
+  __DATA.__zerofill: 0x5d620
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA._rtk_mtab: 0x5a0
   __DATA.__constructor: 0x8
   __DATA.__gxf_data: 0x10
-  __OS_LOG.__string: 0x24133
+  __OS_LOG.__string: 0x24180
   Functions: 7425
   Symbols:   0
-  CStrings:  8994
+  CStrings:  9004
 
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
+ "This monitor has timing with vblank=%d us < spec threshold of %d us"
+ "av_cp_integrity_panic"
+ "color de-saturation WA %s"
+ "getPlatformExtDisplayLimits"
+ "iomfb_RuntimeProperty_useBAEForSBIM"
+ "iomfb_bics_daemon_start_fail_panic"
+ "useBAEForSBIM"
- "%s: VI elements null (color=%p timing=%p)"
- "A440_callback__"
- "A443_callback__"
- "A449_callback__"
- "IOMFB removing mode: %d x %d @ %d Hz (vertical blanking %dus < %dus)"
- "This monitor has timing with vblank=%d us < spec threshold of 300us \n"
```
