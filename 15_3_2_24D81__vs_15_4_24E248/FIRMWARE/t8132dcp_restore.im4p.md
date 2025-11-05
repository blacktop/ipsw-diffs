## t8132dcp_restore.im4p

> `t8132dcp_restore.im4p`

```diff

 
-  __TEXT.__text: 0x32c210
-  __TEXT.__const: 0x46984c
+  __TEXT.__text: 0x33bee0
+  __TEXT.__const: 0x4697e4
   __TEXT.__chain_starts: 0x88
-  __TEXT.__cstring: 0x34f39
-  __DATA.__const: 0x4e368
-  __DATA.__data: 0x14b464
-  __DATA._rtk_patchbay: 0x714
+  __TEXT.__cstring: 0x3576e
+  __TEXT.__lcxx_override: 0x64
+  __DATA.__const: 0x50930
+  __DATA.__data: 0x14b494
+  __DATA._rtk_patchbay: 0x734
   __DATA.__constructor: 0x8
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_boot: 0x8000

   __DATA._rtk_init_stack: 0xa000
   __DATA._rtk_irq_stack: 0x1000
   __DATA._rtk_exc_stack: 0x1000
-  __DATA._afk_sys_drv: 0xb40
-  __DATA.__mod_init_func: 0x88
-  __DATA._afk_sys_objt: 0xbd0
+  __DATA._afk_sys_drv: 0xb60
+  __DATA.__mod_init_func: 0x80
+  __DATA._afk_sys_objt: 0xc10
   __DATA._rtk_heap: 0x30000
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x345a0
+  __DATA.__zerofill: 0x345e0
   __DATA.__afk_obj_num: 0x210
   __DATA._rtk_data_uuid: 0x40
   __DATA.__gxf_data: 0x10
   __DATA._rtk_mtab: 0x6c8
-  __OS_LOG.__string: 0x21ac0
-  UUID: D0796C54-1579-3B09-A9A3-9636CAD4A073
-  Functions: 7023
+  __OS_LOG.__string: 0x232a1
+  UUID: 62FC214F-0154-3385-95B0-1299689354D3
+  Functions: 7477
   Symbols:   0
-  CStrings:  6662
+  CStrings:  6720
 
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
+ "CDS DONE @ laneCount=%u linkRate=%llu bps"
+ "CR_DONE %d is not matching with lane count %d"
+ "Custom BS interval, %s set"
+ "DCPDP2XService"
+ "DCPDPTXMSTManager"
+ "DCPDPTXMSTPort"
+ "DELL U3224KB"
+ "DPBSIntervalVariationOverride"
+ "DPRX_128b132b_CAPS"
+ "DP_TX_PPS_SDP"
+ "Downstream device indicates autonomous mode: %s"
+ "FRL Autonomous mode failed, falling back to TMDS"
+ "FRL link is not valid"
+ "Failed to enable panel replay"
+ "Failed to read DPCD_ADDR_SINK_COUNT"
+ "Failed to set training pattern TPS2 and levels"
+ "Forcing backlight factor to unity for indicator brightness\n"
+ "IOMFB removing mode with odd Hactive : %d\n"
+ "IOMFB: TC: empty idx\n"
+ "IOMFB: VideoInterfaceIOAV::plug, thread \n"
+ "IOMFB: VideoInterfaceIOAV::unplug \n"
+ "IOMFBLTPOFlashMitigationNeeded"
+ "LANE ALIGN STATUS 0x%x"
+ "LANE%d_STATUS=0x%02x: LANE%u_CHANNEL_EQ_DONE=%u"
+ "LANE%d_STATUS=0x%02x: LANE%u_SYMBOL_LOCKED=%u"
+ "LTTPR is not supported"
+ "Link Training Error in CDS 128b132b stage, aborting.."
+ "Link Training Error in EQ 128b132b stage, aborting.."
+ "Mode: id=%llu %ux%u@%u.%uHz, pEnc=0x%x, type=%u, st=%u, v=%u, cc=%u, pCl=%u, sc=%u\n"
+ "Mode: sType=%u total=%ux%u, hBack=%u, vBack=%u, hFront=%u, vFront=%u, hSync=%u, vSync=%u, apCl=%u, ar=%u, cr=%u\n"
+ "PixelFormat not RGB - can't keep ImmediateSwapControl enabled in Auto mode - disabling\n"
+ "Primary MST port PBN:%d"
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
+ "adjusted video bw %llu, normalized bw %d, current bw %d"
+ "alignmentStatus=%x"
+ "allocate payload failed 0x%08x (ignored)"
+ "allocateTunnelBW"
+ "allocated tunnel bandwidth 0x%llu, ret=0x%08x"
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
+ "didTrainLink"
+ "dp2-ignore-bw-alloc-failure"
+ "dp2-no-mst"
+ "eqDoneCount %d laneCount %d alignmentStatus 0x%x"
+ "estimated bw %d, target bw %d"
+ "exiting processFRLAutonomousTraining"
+ "failed to allocate tunneling bw (ignored)"
+ "failed to disable MST mode ret=0x%x"
+ "failed to enum path resources ret=0x%x (ignored)"
+ "failed to read LTTPR ret=0x%08x"
+ "failed to setup MST link ret=0x%x"
+ "failed to update MSTM_CTRL ret=0x%x"
+ "failed to update tunnel BW, ret=0x%08x"
+ "genpipe_one_scale"
+ "genpipe_two_scale"
+ "getEDIDAttributes"
+ "getSupportsAutonomousFRLDPCD"
+ "getSupportsEARC"
+ "getVideoTunnelBW"
+ "handleCacheCapabilities"
+ "hdmi21_autonomous_exp"
+ "hpdExitPSR"
+ "i32@?0^v8{span<unsigned char, 18446744073709551615UL>=*Q}16"
+ "ignoring unexpected VDB in CEA Extension v3"
+ "invalid granularity"
+ "link bw %llu bps, video bw %llu, ratio 0x%x, tunnel bw %llu"
+ "max-ext-lane-count"
+ "min-ext-lane-count"
+ "next link rate 0x%x lane count %u"
+ "one_genpipe"
+ "pollAutonomousModeStatus"
+ "powerbuf size mismatch %zu %d lut->x \n"
+ "processFRLAutonomousTraining"
+ "processLinkStateCDSTraining128b132b"
+ "processLinkStateClockRecovery8b10b"
+ "processLinkStateEQTraining128b132b"
+ "processLinkStateEQTraining8b10b"
+ "processLinkStateFallback"
+ "ps196G"
+ "read_bcon_register_safe"
+ "read_lume_register_safe"
+ "setEDIDAttributes"
+ "setEDIDAttributesGated ret=0x%08x"
+ "set_LUT_hilo_safe"
+ "set_LUT_lcd_safe"
+ "set_luts_safe"
+ "two_genpipe"
+ "unknown"
+ "updateAutonomousCapabilities"
+ "updateTunnelBW"
+ "virtual IOReturn DCPDP13Service::pollAutonomousModeStatus()"
+ "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedDataGeneric *, uint32_t, IOMFB::Surface **)"
+ "willTrainLink"
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
- "Error: Unknown M3 FW variant specified\n"
- "Failed to get is fastsim"
- "IOMFB %s: illegal enumerant\n"
- "IOMFB %s: missing support for version %d\n"
- "IOMFB BICS %s: Illegal enumerant\n"
- "IOMFB:  VideoInterfaceIOAV::plug \n"
- "IOMFBStatus UnifiedPipeline::getProp(uint32_t, uint32_t *)"
- "K59 or J59 detected, %s set"
- "Size mismatch %d %d lut->x \n"
- "Synaptics branch detected, %s set"
- "Unable to read FRL error counters\n"
- "VFP:%d, VBP: %d, VSYNC_WIDTH: %d, HTOTAL:%d, VTOTAL:%d, pixel clock: %d, linetime: %d (ns)"
- "[AFK]%s: DCPDSB_PACKET_READ Error: read_buff_size (0x%zx) is too small for read_length(0x%x)"
- "ap_link: %s: payload too big: %u > %u"
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBELVSLUTs *, const uint64_t *, uint32_t, void *, uint32_t) const"
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, IOMFBMaxVTPowerData *, const uint64_t *, uint32_t, void *, uint32_t) const"
- "auto IOMFB::UPPipeDCP_H16GSC::did_boot(AppleRegisterStream *)::(anonymous class)::operator()(void *, const IOMFBBigBlock *, const uint64_t *, uint32_t, const void *, uint32_t) const"
- "buf_size"
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
- "set_luts"
- "succeed"
- "unique_lock::unlock: not locked"
- "unplug"
- "void IOMobileFramebuffer::blit_surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"
- "void IOMobileFramebuffer::surface_complete(IOMFB::DisplayedData *, uint32_t, IOMFB::Surface **)"
- "writeBlock_gated"
- "write_bcon_register"
- "write_lume_register"

```
