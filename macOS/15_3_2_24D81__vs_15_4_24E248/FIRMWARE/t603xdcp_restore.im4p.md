## t603xdcp_restore.im4p

> `t603xdcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2b5a04
-  __TEXT.__const: 0x3a9d78
+  __TEXT.__text: 0x2b8aa8
+  __TEXT.__const: 0x3a9b5c
   __TEXT.__chain_starts: 0x5c
-  __TEXT.__cstring: 0x30d9f
-  __DATA.__const: 0x31bc0
-  __DATA.__data: 0x11eee4
-  __DATA._rtk_patchbay: 0x714
+  __TEXT.__cstring: 0x310f7
+  __TEXT.__lcxx_override: 0x64
+  __DATA.__const: 0x33108
+  __DATA.__data: 0x11ef14
+  __DATA._rtk_patchbay: 0x734
   __DATA.__constructor: 0x8
   __DATA._rtk_tunables: 0x5b0
   __DATA._rtk_boot: 0x9000

   __DATA._rtk_init_stack: 0xa000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
-  __DATA._afk_sys_drv: 0xe80
-  __DATA.__mod_init_func: 0x88
-  __DATA._afk_sys_objt: 0xb80
+  __DATA._afk_sys_drv: 0xea0
+  __DATA.__mod_init_func: 0x80
+  __DATA._afk_sys_objt: 0xb90
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x343d8
+  __DATA.__zerofill: 0x34440
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA.__gxf_data: 0x10
   __DATA._rtk_mtab: 0x580
-  __OS_LOG.__string: 0x21ae8
-  UUID: 049761B2-6D14-36A9-830B-0C2510434F7D
-  Functions: 6366
+  __OS_LOG.__string: 0x22020
+  UUID: BD56D1E0-A0CE-36FF-8AA6-0C69384DA457
+  Functions: 6710
   Symbols:   0
-  CStrings:  6158
+  CStrings:  6181
 
CStrings:
+ "%s timeout polling AutonomousModeStatus\n"
+ "%s: Couldn't create command gate\n"
+ "%s: cannot allocate command gate\n"
+ "%s::%s(): STATE=%x STA=%x AUX_CH_STA=%x AUX_RX_COMM=%x AUX_DEBUG_STATUS=%x FUNC_EN_2=%x status=0x%08x time=%llu/%llu/%llu/%llu/%llu"
+ "AOC"
+ "ASSERT!%s:%d PPS SDP setup failed"
+ "Aborting filterElements - service is inactive"
+ "AppleDCPPS196"
+ "Autonomous"
+ "Autonomous mode FRL training timed out"
+ "Autonomous mode training result %llu"
+ "Custom BS interval, %s set"
+ "DELL U3224KB"
+ "DPBSIntervalVariationOverride"
+ "DP_TX_PPS_SDP"
+ "Downstream device indicates autonomous mode: %s"
+ "FRL Autonomous mode failed, falling back to TMDS"
+ "FRL link is not valid"
+ "Failed to read DPCD_ADDR_SINK_COUNT"
+ "Forcing backlight factor to unity for indicator brightness\n"
+ "IOMFB removing mode with odd Hactive : %d\n"
+ "IOMFB: TC: empty idx\n"
+ "IOMFB: VideoInterfaceIOAV::plug, thread \n"
+ "IOMFB: VideoInterfaceIOAV::unplug \n"
+ "IOMFBLTPOFlashMitigationNeeded"
+ "Mode: id=%llu %ux%u@%u.%uHz, pEnc=0x%x, type=%u, st=%u, v=%u, cc=%u, pCl=%u, sc=%u\n"
+ "Mode: sType=%u total=%ux%u, hBack=%u, vBack=%u, hFront=%u, vFront=%u, hSync=%u, vSync=%u, apCl=%u, ar=%u, cr=%u\n"
+ "Set FRL(autonomous) link bitrate to %lld"
+ "Sink count is 0\n"
+ "Starting waiting for link training on sink side"
+ "This monitor has timing with vblank=%d us < spec threshold of 300us \n"
+ "Time Elapsed between Hotplugs: %llu\n"
+ "Unable to clear FRL error counters\n"
+ "Unable to read FRL link config status"
+ "Unable to read autonomous mode awareness"
+ "Update autonomous mode support: %s"
+ "[AFK]%s: DCPDSB_PACKET_READ Error: read_buff_size (0x%zx) or read_length(0x%x) is invalid"
+ "__cxa_guard_acquire"
+ "__cxa_guard_release"
+ "ap_link: %s: overflow detected, payload too big: (%zu + %u + %u)\n"
+ "ap_link: %s: overflow detected, paylod too big: (%zu + %u + %u)"
+ "ap_link: %s: payload too big: %u + %u > %u"
+ "ap_link: link_msg_int_handler: OOB access in remote_stream: %u/%lu"
+ "checkAutonomousFRLTrainingState"
+ "checkAutonomousFRLTrainingState failed"
+ "clearFRLCharacterErrorCounters"
+ "exiting processFRLAutonomousTraining"
+ "failed to read LTTPR ret=0x%08x"
+ "genpipe_one_scale"
+ "genpipe_two_scale"
+ "getEDIDAttributes"
+ "getSupportsAutonomousFRLDPCD"
+ "getSupportsEARC"
+ "hdmi21_autonomous_exp"
+ "hpdExitPSR"
+ "ignoring unexpected VDB in CEA Extension v3"
+ "iomfb_num_frames_before_power_on_ready"
+ "max-ext-lane-count"
+ "min-ext-lane-count"
+ "one_genpipe"
+ "pollAutonomousModeStatus"
+ "processFRLAutonomousTraining"
+ "ps196G"
+ "setEDIDAttributes"
+ "setEDIDAttributesGated ret=0x%08x"
+ "two_genpipe"
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
+ "unknown"
+ "updateAutonomousCapabilities"
+ "virtual IOReturn DCPDP13Service::pollAutonomousModeStatus()"
+ "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedDataGeneric *, uint32_t, IOMFB::Surface **)"
- "%s: acquiring IOAVVideoInterface %s\n"
- "%s: calling stopLink()\n"
- "%s: calling willStopLink()\n"
- "%s: getting property %s failed\n"
- "%s: invalid blitID: %d\n"
- "%s::%s(): STATE=%x STA=%x AUX_CH_STA=%x AUX_RX_COMM=%x AUX_DEBUG_STATUS=%x FUNC_EN_2=%x"
- "CXXGrdAcq"
- "CXXPureVirt"
- "CXXnew:%zu"
- "CXXnew[]:%zu"
- "DPBSIntervalVariationOverrideX59"
- "Failed to get is fastsim"
- "IOMFB %s: illegal enumerant\n"
- "IOMFB %s: missing support for version %d\n"
- "IOMFB:  VideoInterfaceIOAV::plug \n"
- "IOMFBStatus UnifiedPipeline::getProp(uint32_t, uint32_t *)"
- "K59 or J59 detected, %s set"
- "Synaptics branch detected, %s set"
- "Unable to read FRL error counters\n"
- "VFP:%d, VBP: %d, VSYNC_WIDTH: %d, HTOTAL:%d, VTOTAL:%d, pixel clock: %d, linetime: %d (ns)"
- "[AFK]%s: DCPDSB_PACKET_READ Error: read_buff_size (0x%zx) is too small for read_length(0x%x)"
- "ap_link: %s: payload too big: %u > %u"
- "condition_variable wait failed"
- "condition_variable::wait: mutex not locked"
- "e: DPCl: Data size insufficient for the taps \n"
- "e: DPCl: More brightness taps( %d ) then expected (%d) \n"
- "e: DPCl: More temperature taps( %d ) then expected (%d) \n"
- "e: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
- "e: invalid header\n"
- "e: set DPCl data failed\n"
- "e: set HSPC data failed\n"
- "e: set TLSC data failed\n"
- "e: set TLSC data failed. Too many frequency levels. \n"
- "e: set USPC data failed\n"
- "failed to set 8b/10b coding ret=0x%08x"
- "failed to set transparent mode ret=0x%08x"
- "getPhysicalAddress"
- "i: set DPCl data succeeded\n"
- "i: set HSPC data succeeded\n"
- "i: set TLSC data succeeded\n"
- "i: set USPC data succeeded\n"
- "mutex lock failed"
- "secure-mipi"
- "setPhysicalAddress"
- "setPhysicalAddressGated ret=0x%08x"
- "succeed"
- "unplug"
- "void IOMobileFramebuffer::blit_surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"
- "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"

```
