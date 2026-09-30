## com.apple.driver.AppleDisplayManager

> `com.apple.driver.AppleDisplayManager`

```diff

-700.50.97.9.0
+700.50.103.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x2159
-  __TEXT_EXEC.__text: 0x6d38
+  __TEXT.__cstring: 0x2b9e
+  __TEXT_EXEC.__text: 0x944c
   __TEXT_EXEC.__auth_stubs: 0x1c0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__auth_got: 0xe0
   __DATA_CONST.__got: 0x48
-  Functions: 129
-  Symbols:   500
-  CStrings:  200
+  Functions: 132
+  Symbols:   503
+  CStrings:  248
 
Symbols:
+ __ZN19AppleDisplayManager18validate_or_set_exEP22ADMDisplayResourcesSetP35ADMDisplayResourcesValidateOutputExPb
+ __ZN19AppleDisplayManager27apply_seamless_pipe_mappingEPKjhj
+ __ZN19AppleDisplayManager28resolve_seamless_peer_configEjP25IOAVPeerDisplayPipeConfig
CStrings:
+ "%s: skipping display with no matching shim\n"
+ "ADM: AED Flash reduction is %sabled\n"
+ "AED %s: fb %u dual-capable (pipes %u, max %u); skipping rearrange for it\n"
+ "AED %s: fb %u failed to establish dual-pipe pairing (0x%x); rolling back grow\n"
+ "AED %s: fb %u failed to release crossbar pipe after grow rollback (0x%x)\n"
+ "AED %s: fb %u fits single pipe (max_width %u <= %u, max_bw %llu <= %llu); skipping rearrange\n"
+ "AED %s: fb %u invalid pipe id (primary 0x%x secondary 0x%x)\n"
+ "AED %s: fb %u is multi-tile/DP-split, not a VFTG-merge grow; skipping pairing\n"
+ "AED %s: fb %u out of range; skipping rearrange\n"
+ "AED %s: fb %u reports %u pipes post-commit, expected 2\n"
+ "AED %s: fb %u resolved out-of-range secondary dispext index %d (primary ep %u, secondary ep %u)\n"
+ "AED %s: fb %u secondary dispext index %d (primary ep %u secondary ep %u)\n"
+ "AED %s: getDisplayCaps error\n"
+ "AED allocation-set: entry (count %u)\n"
+ "AED rearrange: Disable re arrange optimization\n"
+ "AED rearrange: entry (count %u)\n"
+ "AED reconfig-complete: entry (count %u)\n"
+ "AED reconfig-complete: fb %u out of range; skipping"
+ "AED validate-ex: [%u] fbId=0x%x ver=%u hw_reconfig=%d modeset=%d release=%d\n"
+ "AED validate-ex: entry (count %u)\n"
+ "AED validate-ex: returning 0x%x, setOutput count=%u\n"
+ "AED validate-ex: returning 0x%x, setOutput not populated\n"
+ "AED validate-ex: returning success, setOutput count=%u\n"
+ "AED: %s starting (count %u)\n"
+ "AED: %s: fb %u -> %u pipe(s), pipe_options 0x%x\n"
+ "AED: %s: fb %u max_width %u max_bw %llu\n"
+ "AED: %s: get_displays_and_mapping_set failed (0x%x)\n"
+ "AED: %s: no external display matched a shim\n"
+ "AED: %s: none of the requested displays matched a connection\n"
+ "AED: %s: setDisplayConnectionMapping failed (0x%x)\n"
+ "AED: FB %d: reallocation (1.5->2)\n"
+ "AED: FB %u sink advertises %u DSC slices; dual-pipe disabled\n"
+ "AED: fb %u full dual pipe unavailable; retrying as LIMITED dual pipe (pipe_options 0x%x)\n"
+ "AED: fb %u grow -> %s dual pipe, pipe_options 0x%x (w req %u vs limited %u, bw req %llu vs limited %llu)\n"
+ "AED: fb %u native dual pipe, no reconfig; mode set intent with %d pipes\n"
+ "AED: fb 0x%x reported modeset_required but the allocation failed (0x%x); WindowServer will not commit this grow\n"
+ "AED: grow fb %u to dual (width req %u vs single %u, bw req %llu vs single %llu)\n"
+ "AED: limited dual pipe retry for %u display(s) returned 0x%x\n"
+ "AED: platform ext display pipe limits: max_bw_single=%llu max_bw_double=%llu max_bw_limited=%llu max_w_single=%u max_w_double=%u max_w_limited=%u supportSuppressed=%u\n"
+ "AED: rdar://184680560 workaround - no dual-pipe on 2 DSC slices per line\n"
+ "AppleDisplayManager: getPlatformExtDisplayLimits failed. AED will not be functional\n"
+ "FULL"
+ "HDMI debounce: setting display to zero pipes in re-arrange path\n"
+ "IOMFB: admLock allocation failed!\n"
+ "LIMITED"
+ "Matching shim found!\n"
+ "OSArray - disp_array_ordered init failure\n"
+ "Request to release a used pipe on fb %d!\n"
+ "aed_re_arrange_opt"
+ "apply_seamless_pipe_mapping"
+ "dis"
+ "en"
+ "iomfb_aed_flash_reduction_enable"
+ "resolve_seamless_peer_config"
+ "validate_or_set_ex"
- "AED: %s starting (count %u)"
- "AED: %s starting (stub, count %u)"
- "AED: FB %d: reallocation (1.5->2)"
- "AED: platform ext display pipe limits: max_bw_single=%llu max_bw_double=%llu max_bw_limited=%llu max_w_single=%u max_w_double=%u max_w_limited=%u supportSuppressed=%u"
- "IOMFB: admLock allocation failed!"
- "Matching shim found!"
- "display_reconfig_complete"
```
