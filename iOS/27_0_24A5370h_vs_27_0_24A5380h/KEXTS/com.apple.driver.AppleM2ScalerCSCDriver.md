## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-  __TEXT.__const: 0xc3660
-  __TEXT.__cstring: 0x24945
-  __TEXT_EXEC.__text: 0x13a598
+  __TEXT.__const: 0xc3000
+  __TEXT.__cstring: 0x24da7
+  __TEXT_EXEC.__text: 0x13b90c
   __TEXT_EXEC.__auth_stubs: 0xbd0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2788
   __DATA.__bss: 0x2184
   __DATA_CONST.__mod_init_func: 0x6a8
   __DATA_CONST.__mod_term_func: 0x680
-  __DATA_CONST.__const: 0x2adb8
+  __DATA_CONST.__const: 0x2ae30
   __DATA_CONST.__kalloc_type: 0x4f00
   __DATA_CONST.__kalloc_var: 0x1310
   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10260
+  Functions: 10277
   Symbols:   0
-  CStrings:  3662
+  CStrings:  3689
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
CStrings:
+ " (0.%03ux downscale)"
+ " (identity)"
+ " (upscale)"
+ " 0x%08x"
+ "\"[%s] \" \"setPowerState sleep ack watchdog: MSR%u scaler %u sleepStateSPS=%u powerRefCount=%u partitionPower=%u compQueueEmpty=%u running=%u cmdQueueDepth=%u recoveryInProgress=%u resetReason=%u fwLoaded=%u pendingMask=0x%x ticks=%u\\n\" @%s:%d"
+ "\"[%s] \" sd.frame_info.priority @%s:%d"
+ "\"[IOSA] Unexpected frame pri from FW ( %u )\\n\""
+ "%s\n"
+ "%s %s, src to dst ratio index=%d%s:\n"
+ "%s : %s tap %d and tap %d are not close in value as expected\n"
+ "0.25x"
+ "0.375x"
+ "0.5x"
+ "0.625x"
+ "0.75x"
+ "0.875x"
+ "12111112122212121222211122111222022121111111111111000000200000002000000020000000212211111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221121122212"
+ "Custom Chroma Filter [%s]:\n"
+ "Custom Filter [%s]:\n"
+ "Identity"
+ "MSR23BackwardsCompatibleFilter::checkCoefficientsValid...0x%x\n"
+ "MSR23BackwardsCompatibleFilter::updateWithCoefficients srcToDstRatioIndex %d (%s) %p\n"
+ "T(%02d)"
+ "Upscale"
+ "Upscale/Identity"
+ "WA: fake the dashboard interrupt!\n"
+ "[%05X %08X] %03u {%08X %08X} tile %s: f=%08X: tile=[%u,%u]%s%s%s (tdr=%u)"
+ "[%s][%s]getIndexFromSrcToDstRatio filterIndex: %d (%s)\n"
+ "[%s][Chroma] bin mismatch; %s custom filter has ratio match, using %s coefficients\n"
+ "[%s][Chroma] bin mismatch; falling back to default filter bin %d (%s)\n"
+ "[%s][Luma] bin mismatch; %s custom filter has ratio match, using %s coefficients\n"
+ "[%s][Luma] bin mismatch; falling back to default filter bin %d (%s)\n"
+ "[FilterComp] pCoefficients %p Returning 0x%x for t:%d p:%d\n"
+ "[IOSA] Discarding stale SD frame_id %u (all requests flushed, firmware reset pending)\n"
+ "dst format %d pixels align(%d %d)\n"
+ "logPowerStateTrackerEntries"
+ "powerStateTracker[%u]: req=%p transformId=%d reason=%u count=%u\n"
+ "ratio %s%d.%s%u\n"
- "\"[IOSA] Unexpected frame pri from FW ( %u )\\n\" @%s:%d"
- "%s %s, src to dst ratio index=%d:\n"
- "0x%08x "
- "12111112122212121222111221112220221211111111111110000000200000002000000020000000212211111111111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222221122221121122212"
- "Andros WA: fake the dashboard interrupt!\n"
- "T(%02d) "
- "[%05X %08X] %03u {%08X %08X} tile %s: f=%08X: tile=[%u,%u]%s (tdr=%u)"
- "[%s][%s]getIndexFromSrcToDstRatio filterIndex: %d \n"
- "[FilterComp]Returning 0x%x for t:%d p:%d\n"
- "src format %d pixels align(%d %d)\n"
- "tap %d and tap %d are not close in value as expected\n"

```
