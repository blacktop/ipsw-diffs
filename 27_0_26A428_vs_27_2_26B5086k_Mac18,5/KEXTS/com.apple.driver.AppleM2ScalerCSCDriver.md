## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.62.3.0.0
-  __TEXT.__const: 0xc30c0
-  __TEXT.__cstring: 0x25869
-  __TEXT_EXEC.__text: 0x13f318
+200.66.0.0.0
+  __TEXT.__const: 0xc3160
+  __TEXT.__cstring: 0x25a59
+  __TEXT_EXEC.__text: 0x13fa8c
   __TEXT_EXEC.__auth_stubs: 0xba0
   __DATA.__data: 0x22388
   __DATA.__common: 0x2710
   __DATA_CONST.__mod_init_func: 0x698
   __DATA_CONST.__mod_term_func: 0x668
-  __DATA_CONST.__const: 0x3d9c8
+  __DATA_CONST.__const: 0x3da68
   __DATA_CONST.__kalloc_type: 0x4e40
   __DATA_CONST.__kalloc_var: 0x13b0
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10195
-  Symbols:   10252
-  CStrings:  3664
+  Functions: 10211
+  Symbols:   10263
+  CStrings:  3674
 
Symbols:
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _ZN16ApiodmaRegStream15arenaReturnPageEPKNS_19ArenaPageDescriptorE
+ __Z23doubleToFixedSaturatingdjj
+ __ZN22AppleM2ScalerCSCDriver41checkAndNotifyLowLatencySharedEvent_gatedEP18M2ScalerCSCRequestP20IOSurfaceSharedEvent
+ __ZN24IosaFirmwareControlMSR2312bootProgressEv
+ __ZN24IosaFirmwareControlMSR2314bootEntryCountEv
+ __ZN24IosaFirmwareControlMSR2318panicFWLoadFailureEPKc
+ __ZN27IosaFirmwareControlMSR23Rtk12bootProgressEv
+ __ZN27IosaFirmwareControlMSR23Rtk14bootEntryCountEv
+ __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3149
+ __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2319
+ __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2309
+ __ZZN16ApiodmaRegStream12arenaReleaseEPNS_5ArenaEE20kalloc_type_view_326
+ __ZZN16ApiodmaRegStream13arenaAllocateEP4taskE20kalloc_type_view_264
+ __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6436
+ __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6415
- __ZZL15logFailedClientP26IOSurfaceAcceleratorClientP4taskP18M2ScalerCSCRequestE21kalloc_type_view_3137
- __ZZN12ActiveWindow18obtainActiveWindowEjjjjE21kalloc_type_view_2308
- __ZZN15ActiveWindowSet7releaseEvE21kalloc_type_view_2298
- __ZZN16ApiodmaRegStream12arenaReleaseEPNS_5ArenaEE20kalloc_type_view_216
- __ZZN16ApiodmaRegStream13arenaAllocateEP4taskE20kalloc_type_view_154
- __ZZN22AppleM2ScalerCSCDriver34setStatTransformEvent_gatedContextEP18M2ScalerCSCRequest14TransformEventE21kalloc_type_view_6424
- __ZZN22AppleM2ScalerCSCDriver36pruneTransformStatQueue_gatedContextEvE21kalloc_type_view_6403
CStrings:
+ "\"[%s] \" \"Failed to load MsrCPU firmware %s: MSR%u scaler %u path=%s embedded=%u imem0=0x%08x apImg0=0x%08x bootProgress=%s(0x%08x) bootEntries=%u running=0x%08x ibootFw=%d ctrrLock=%u ctrrWrDis=%u\\n\" @%s:%d"
+ "%.4s"
+ "12111121221111111222"
+ "121111212211111112222"
+ "12111121221111111222222"
+ "1211112122111111122222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "AP"
+ "Histogram bin count (%ld) exceeds maximum (%d)"
+ "arenaReturnPage"
+ "command %u in use but has no packet sequence (valid=%u)\n"
+ "command %u sequence list spans two requests (%p != %p)\n"
+ "deferring arena release during flush, queue length %u\n"
+ "for PG"
+ "for reset (postInit)"
+ "for reset (resetScaler)"
+ "iBoot"
+ "reclaimed %u PIODMA command(s), released %u MSR power ref(s), refCount now %u\n"
+ "reclaiming PIODMA command idx=%u tag=%u transformId=%d powerRefOutstanding=%d release=%d\n"
- "\"[%s] \" \"Failed to load MsrCPU firmware for PG\\n\" @%s:%d"
- "\"[%s] \" \"Failed to load MsrCPU firmware for reset\\n\" @%s:%d"
- "121111211111111222"
- "1211112111111112222"
- "121111211111111222222"
- "12111121111111122222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "Histogram bin count (%d) exceeds maximum (%d)"
- "command %d not valid!"
```
