## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-600.24.1.0.0
-  __TEXT.__const: 0x2378 sha256:db78982f7b0778094fec911af258a58983ae839ac24898a6fbe94a95bfee69b8
-  __TEXT.__os_log: 0x9ab8 sha256:19c8d8183c2413e9c9d1544c772ae2ac6d7fbfe3668448b22b942a69ec1fd099
-  __TEXT.__cstring: 0x112a sha256:621bc0fbe506a6ad7d11c4e994f227f51dc4b64c51203f5d3a2b977ece65996c
-  __TEXT_EXEC.__text: 0x4e148 sha256:2d583aa86e451bbc6bf1a309094b6f175eefd2ea5f8f311cfc36aecc87cc09f4
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x448 sha256:48f4f3968f77cea35f2a233ce260e513cfa6321b2fb7428492faa6f9c25e1c7c
+600.38.0.0.0
+  __TEXT.__const: 0x23a8 sha256:16cbc0c644d25671663719d3a3565dd8d5c73917f70a8910daba839ecce3f4d0
+  __TEXT.__os_log: 0x9d00 sha256:297526a3236d88cff6d4bf985aa5dc78337df8fa1333fceb87bc3676aceddc0d
+  __TEXT.__cstring: 0x114b sha256:535c4597a4e8729399ab61cb7bb049dd17e8f1803b17842116484133d7cae3bb
+  __TEXT_EXEC.__text: 0x502d0 sha256:b6e2299045cc0997b8b943a5ad2c27f2681fdae8adf7cd7bd45a7b9a1cfb140a
+  __TEXT_EXEC.__auth_stubs: 0x5e0 sha256:02c5fd635fcce9ada98b2c791952a89a4eb7d50548a176c2b453201566628207
+  __DATA.__data: 0x458 sha256:472d90e771d7603c9efd470701036778803fbae805ce19daa5eff01c351265b6
   __DATA.__common: 0x78 sha256:6edd9f6f9cc92cded36e6c4a580933f9c9f1b90562b46903b806f21902a1a54f
   __DATA.__bss: 0x9a20 sha256:00cfa53b849b1ee01cab49a7c68c2e486dafdd09b4bf832209b4734ca340eefc
-  __DATA_CONST.__mod_init_func: 0x10 sha256:483e0d1dd03a504929c3f6120800cec6505f3c51df0d7d77d8c762dc9ee28dcd
-  __DATA_CONST.__mod_term_func: 0x10 sha256:649cdb0bf402e578af78bfcae9676a3e8e5076075315e0cb5aff23a1cf0216b1
-  __DATA_CONST.__const: 0xb190 sha256:9662ba8024ad1a2ba6f57059b6b0913ebb28ef163e1763007a7891fd39a0be86
-  __DATA_CONST.__kalloc_type: 0x480 sha256:35fe33e9b68334e89a3ee610ad196f4a46e2e2d2bbb409450b69fe663acfb90b
-  __DATA_CONST.__kalloc_var: 0x140 sha256:7491d24331e0baea68f6b7e73a75e476626179903eb7fa6c1755e0997a20af45
-  __DATA_CONST.__auth_got: 0x2f0 sha256:1820b80fc19ba7a01c6b480a7713215b7d62c59c94f295b2644920acf6367df1
-  __DATA_CONST.__got: 0x60 sha256:b1c0b6aea77104b42c7520f499352774077b6d466815d9dea69ea604b857e3da
-  UUID: 6FD4E527-24B1-3D3C-B4A8-33190F4E22F4
-  Functions: 2758
+  __DATA_CONST.__mod_init_func: 0x10 sha256:e0886878d2000e2b1bc403ae73b0b4c702754fd18601073690f720b232423116
+  __DATA_CONST.__mod_term_func: 0x10 sha256:48688d3fb06a690047f6144d0b72d6b7730e52fa0ff4a5c79c0e33621f25c30a
+  __DATA_CONST.__const: 0xba28 sha256:5881f20aee32d9c67e287ea4eb1dfef4f569af1da94b49fac183e35828aeb39f
+  __DATA_CONST.__kalloc_type: 0x480 sha256:c8a950fe5127687af916a034a816e06ad048b0b5829daa077e5af989421c3289
+  __DATA_CONST.__kalloc_var: 0x140 sha256:885aaca4ca7eec8f1c95c29dcf04293bc67e9ddc65d49467e733eac30ca2dc3e
+  __DATA_CONST.__auth_got: 0x2f0 sha256:e3b83121bf9554db223af475ce5dae08c50602794d55f3fbbd46740eef4a8bd3
+  __DATA_CONST.__got: 0x60 sha256:7c2dae33f78eb47f3d0622a53651355adafc6cfdf274b346b8b551bda584dc2d
+  UUID: D113643E-3AFC-3B9B-ACF1-4B86063E4D79
+  Functions: 2818
   Symbols:   0
-  CStrings:  553
+  CStrings:  563
 
CStrings:
+ "121111121222121211221111211111121111112111111211222211112222211112111111211111121111112111111111111111111111111111111121121121121111111111111111111111111111111111111111111111111111111111111111111112222222222222222221111111222221111111111111111212222211112"
+ "AppleProResHW (0x%x): %s(): CurrentClient->perfMode %d pDecodeFrame->perfMode %d\n"
+ "AppleProResHW (0x%x): %s(): ERROR: SPARE readback 0x%x != 0x%x, coreIdx %d\n"
+ "AppleProResHW (0x%x): %s(): TopVersion %u (0x%x) published to IORegistry\n"
+ "AppleProResHW (0x%x): %s(): TopVersion not published: HW verification failed\n"
+ "AppleProResHW (0x%x): %s(): coreIdx %d topVersion 0x%x\n"
+ "AppleProResHW (0x%x): %s(): coreIdx %u: PSD device - cannot set perf state as m_pSetPerfStateFunction is NULL"
+ "AppleProResHW (0x%x): %s(): devFeaturelist: numFramesPendingMultiplier=%d, bUseLegacyTargetSize=%d, bRAWCodec=%d, bAlphaOnlyCodec=%d, bFrameMaxSizeLimit=%d, bLossyInterchangeFormat=%d, bMBsPerSlice=%d, bRAWRateControl=%d, bHWStatsQPMap=%d, bSwapBRRaw=%d, bAlphaProcessing=%d, bDisableBitstream=%d, bRAWV2=%d, bCommandSplitterFix=%d, isDevBinned=%d, eAprDesc=%d, bUseLegacyEncoderID=%d, bWriteDMAStatsReg=%d, bisFastsim=%d "
+ "AppleProResHW (0x%x): %s(): readiness check passed, coreIdx %d\n"
+ "ProRes-fw-enable"
+ "TopVersion"
+ "s0"
+ "verifyHWReadiness"
- "12111112122212121122111121111112111111211111121122221111222221111211111121111112111111211111111111111111111111111111112112112112111111111111111111111111111111111111111111111111111111111111111111111222222222222222222111111122221111111111111111212222211112"
- "AppleProResHW (0x%x): %s(): devFeaturelist: bLossyInterchangeFormat=%d, bRAWCodec=%d, numFramesPendingMultiplier=%d, bFrameMaxSizeLimit=%d, bMBsPerSlice=%d, bAlphaOnlyCodec=%d, bRAWRateControl=%d, bHWStatsQPMap=%d, bCommandSplitterFix=%d, isDevBinned=%d, bAlphaProcessing=%d, bDisableBitstream=%d"
- "aprDeviceEnabled"

```
