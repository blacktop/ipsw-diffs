## com.apple.driver.AppleM2ScalerCSCDriver

> `com.apple.driver.AppleM2ScalerCSCDriver`

```diff

-200.57.0.0.0
-  __TEXT.__const: 0xc3000
-  __TEXT.__cstring: 0x24df3
-  __TEXT_EXEC.__text: 0x13ba60
+200.62.1.0.0
+  __TEXT.__const: 0xc3090
+  __TEXT.__cstring: 0x2515b
+  __TEXT_EXEC.__text: 0x13ba50
   __TEXT_EXEC.__auth_stubs: 0xbd0
   __DATA.__data: 0x22388
-  __DATA.__common: 0x2788
-  __DATA.__bss: 0x2184
-  __DATA_CONST.__mod_init_func: 0x6a8
-  __DATA_CONST.__mod_term_func: 0x680
-  __DATA_CONST.__const: 0x2ae30
-  __DATA_CONST.__kalloc_type: 0x4f00
-  __DATA_CONST.__kalloc_var: 0x1310
+  __DATA.__common: 0x2738
+  __DATA.__bss: 0x2134
+  __DATA_CONST.__mod_init_func: 0x698
+  __DATA_CONST.__mod_term_func: 0x670
+  __DATA_CONST.__const: 0x2abf0
+  __DATA_CONST.__kalloc_type: 0x4e80
+  __DATA_CONST.__kalloc_var: 0x13b0
   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x88
-  Functions: 10278
+  Functions: 10261
   Symbols:   0
-  CStrings:  3690
+  CStrings:  3704
 
CStrings:
+ " >>>> Client %d (%p) (%s) filters %p, Scaling filters %p\n"
+ "\"[%s] \" \"MailBox[%d] credit return_inc check failed on wake\\n\" @%s:%d"
+ "\"[%s] \" \"MailBox[6] credit return_inc check failed on transform completion (req: %d)\\n\" @%s:%d"
+ "%s %s, src to dst ratio index=%d%s:      %s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator_kexts/FirmwareControl/IosaFirmwareControlMSR27Rtk.cpp"
+ "1111222"
+ "12122121221212212122121221212212122121221212212122121221212212122120000020000000122112221200000020000000211112112222211222221122222112222211222221122222112222211222221122222111122211112221111222111122211112221111222111122211112222211212000020000000"
+ "ActiveWindow partiton %dx%d (src %dx%d dst %dx%d rot %d): Dest AW dimension %dx%d\n"
+ "Allocated MailBox: %p (instance id: %d)\n"
+ "Custom Chroma Filter :\n"
+ "Custom Filter :\n"
+ "Failed to allocate ta_pool\n"
+ "MSR Message Box link bring up!\n"
+ "MSR Message Box teardown - STATIC_IDLE_STATUS.static_gate_ready timed out\n"
+ "MSRCPU: IMEM verified against embedded image (%zu words)\n"
+ "MSRCPU: IMEM verify failed: %zu/%zu words mismatched\n"
+ "MSRCPU: IMEM verify mismatch at word %zu: wrote %08X, read %08X\n"
+ "MailBox[%u] outbox drain did not complete\n"
+ "No"
+ "Scaler[%d] startDPE() done\n"
+ "Scaler[%d] stopDPE() done\n"
+ "Yes"
+ "drainOutboxMessages"
+ "findCustomFilterCoefficientsAtNeighboringBin"
+ "site.TileArray"
+ "tearDownMsrMessageBoxLinks_gatedContext"
+ "transform (%dx%d)->(%dx%d): A dimension has src to dst ratio %s%d.%s%u (bin %d) for %s %s has set a custom filter flag without custom coefficients; falling back to default filter for this axis\n"
+ "transform (%dx%d)->(%dx%d): src to dst ratio %s%d.%s%u for %s %s landed on bin %d with no coefficients; using neighboring bin %d instead to absorb client ratio quantization noise\n"
+ "updateWithAllCoefficientsCopy: client=%d (%p) %s: raw hDstToSrcRatio=0x%x vDstToSrcRatio=0x%x (diff=%d) -> hSrcToDstRatioIndex=%d vSrcToDstRatioIndex=%d\n"
- "%s %s, src to dst ratio index=%d%s:\n"
- "%s: TODO\n"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator_kexts/DPEControl/IosaDPEControlMSR26.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOSurfaceAccelerator_kexts/DPEControl/IosaDPEControlMSR27.cpp"
- "12122121221212212122121221212212122121221212212122121221212212122120000020000000122112221200000020000000211112112222211222221122222112222211222221122222112222211222221122222111122211112221111222111122211112221111222111122211112222211200000020000000"
- "ActiveWindow partiton on (%s) %dx%d: Dest AW dimension %dx%d\n"
- "Allocated MailBox: %p\n"
- "IosaDPEControlMSR26"
- "IosaDPEControlMSR27"
- "No filter coefficients!\n"
- "site.IosaDPEControlMSR26"
- "site.IosaDPEControlMSR27"
- "transform (%dx%d)->(%dx%d): A dimension has src to dst ratio %s%d.%s%u (bin %d) for %s %s has set a custom filter flag without custom coefficients\n"
- "virtual void IosaDPEControlMSR26::startDPE()"
- "virtual void IosaDPEControlMSR26::stopDPE()"
```
