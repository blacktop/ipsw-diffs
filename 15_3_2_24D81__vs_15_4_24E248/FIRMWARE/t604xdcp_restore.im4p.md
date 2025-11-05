## t604xdcp_restore.im4p

> `t604xdcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x2d0dbc
-  __TEXT.__const: 0x3b7f48
+  __TEXT.__text: 0x2d5aac
+  __TEXT.__const: 0x3b7e5c
   __TEXT.__chain_starts: 0x5c
-  __TEXT.__cstring: 0x32412
-  __DATA.__const: 0x33ef8
-  __DATA.__data: 0x11fd40
-  __DATA._rtk_patchbay: 0x714
+  __TEXT.__cstring: 0x32782
+  __TEXT.__lcxx_override: 0x64
+  __DATA.__const: 0x35c40
+  __DATA.__data: 0x11fd70
+  __DATA._rtk_patchbay: 0x734
   __DATA.__constructor: 0x8
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_boot: 0x9000

   __DATA._rtk_init_stack: 0x5000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
-  __DATA._afk_sys_drv: 0xbe0
-  __DATA.__mod_init_func: 0x88
-  __DATA._afk_sys_objt: 0xb90
+  __DATA._afk_sys_drv: 0xc00
+  __DATA.__mod_init_func: 0x80
+  __DATA._afk_sys_objt: 0xba0
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5f2a8
+  __DATA.__zerofill: 0x5f300
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA.__gxf_data: 0x10
   __DATA._rtk_mtab: 0x5a0
-  __OS_LOG.__string: 0x21f02
-  UUID: 38E75E9F-1EE3-3A9E-8938-75AE5E3EE32E
-  Functions: 6530
+  __OS_LOG.__string: 0x2243a
+  UUID: 5F712B6D-B1D9-3D2C-AD2A-2DBDC32A4A0F
+  Functions: 6888
   Symbols:   0
-  CStrings:  6334
+  CStrings:  6355
 
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
+ "PixelFormat not RGB - can't keep ImmediateSwapControl enabled in Auto mode - disabling\n"
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
+ "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBELVSLUTs *, const Uint64Span, const MutableByteSpan) const"
+ "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBMaxVTPowerData *, const Uint64Span, const MutableByteSpan) const"
+ "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, const IOMFBBigBlock *, const Uint64Span, const ByteSpan) const"
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
+ "i32@?0^v8{span<unsigned char, 18446744073709551615UL>=*Q}16"
+ "ignoring unexpected VDB in CEA Extension v3"
+ "max-ext-lane-count"
+ "min-ext-lane-count"
+ "one_genpipe"
+ "pollAutonomousModeStatus"
+ "processFRLAutonomousTraining"
+ "ps196G"
+ "read_bcon_register_safe"
+ "read_lume_register_safe"
+ "setEDIDAttributes"
+ "setEDIDAttributesGated ret=0x%08x"
+ "set_LUT_hilo_safe"
+ "set_LUT_lcd_safe"
+ "two_genpipe"
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
+ "unknown"
+ "updateAutonomousCapabilities"
+ "virtual IOReturn DCPDP13Service::pollAutonomousModeStatus()"
+ "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedDataGeneric *, uint32_t, IOMFB::Surface **)"
+ "writeBlock_gated_safe"
+ "write_bcon_register_safe"
+ "write_lume_register_safe"
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
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBELVSLUTs *, const uint64_t *, uint32_t, void *, uint32_t) const"
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBMaxVTPowerData *, const uint64_t *, uint32_t, void *, uint32_t) const"
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, const IOMFBBigBlock *, const uint64_t *, uint32_t, const void *, uint32_t) const"
- "condition_variable wait failed"
- "condition_variable::wait: mutex not locked"
- "e: DPCl: Data size insufficient for the taps \n"
- "e: DPCl: More brightness taps( %d ) then expected (%d) \n"
- "e: DPCl: More temperature taps( %d ) then expected (%d) \n"
- "e: The data size ( %d )is actually lesser than remaining bytes ( %d )\n"
- "e: data_sz underflow in get_long_value\n"
- "e: data_sz underflow in get_value\n"
- "e: invalid header\n"
- "e: set DPCl data failed\n"
- "e: set HSPC data failed\n"
- "e: set TLSC data failed\n"
- "e: set TLSC data failed. Too many frequency levels. \n"
- "e: set USPC data failed\n"
- "failed to set 8b/10b coding ret=0x%08x"
- "failed to set transparent mode ret=0x%08x"
- "getPhysicalAddress"
- "i28@?0^v8^v16I24"
- "i: set DPCl data succeeded\n"
- "i: set HSPC data succeeded\n"
- "i: set TLSC data succeeded\n"
- "i: set USPC data succeeded\n"
- "mutex lock failed"
- "read_bcon_register"
- "read_lume_register"
- "secure-mipi"
- "setPhysicalAddress"
- "setPhysicalAddressGated ret=0x%08x"
- "set_LUT_hilo"
- "set_LUT_lcd"
- "succeed"
- "unplug"
- "void IOMobileFramebuffer::blit_surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"
- "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"
- "writeBlock_gated"
- "write_bcon_register"
- "write_lume_register"

```
