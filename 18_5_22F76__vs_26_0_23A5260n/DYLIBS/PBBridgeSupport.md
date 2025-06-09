## PBBridgeSupport

> `/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`

```diff

-1237.25.0.0.0
-  __TEXT.__text: 0x41320
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0x511c
-  __TEXT.__cstring: 0x5db8
+1282.0.0.0.0
+  __TEXT.__text: 0x42df8
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x5124
+  __TEXT.__cstring: 0x5db2
   __TEXT.__const: 0x920
-  __TEXT.__oslogstring: 0x271f
+  __TEXT.__oslogstring: 0x275d
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__dlopen_cstrs: 0x17c
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0xf98
+  __TEXT.__unwind_info: 0xf90
   __TEXT.__objc_classname: 0xb03
-  __TEXT.__objc_methname: 0x9249
-  __TEXT.__objc_methtype: 0x169f
-  __TEXT.__objc_stubs: 0x55a0
-  __DATA_CONST.__got: 0x620
+  __TEXT.__objc_methname: 0x9261
+  __TEXT.__objc_methtype: 0x16c4
+  __TEXT.__objc_stubs: 0x5620
+  __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__const: 0x13c0
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2518
+  __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x5820
-  __AUTH_CONST.__objc_const: 0x7170
+  __AUTH_CONST.__cfstring: 0x5800
+  __AUTH_CONST.__objc_const: 0x7178
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCFEED9C-7A27-34D7-A801-3442A44279C1
-  Functions: 1834
-  Symbols:   5786
-  CStrings:  3716
+  UUID: 3A750E74-D4AE-3DEA-92BD-755B9B168DCC
+  Functions: 1836
+  Symbols:   5787
+  CStrings:  3718
 
Symbols:
+ _PBIsEarlyPairedSyncSupportedForPDRDevice
+ _PBIsEarlyPairedSyncSupportedForPDRDevice.cold.1
+ _PBIsEarlyPairedSyncSupportedForPDRDevice.cold.2
+ _PBVariantSizeForPDRDeviceSize
+ _PDRDeviceSizeForArtworkDeviceSubType
+ _PDRDeviceSizeForProductType
+ ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.307
+ ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.306
+ ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.319
+ ___51-[PBBridgeGizmoController ingestTinkerCredentials:]_block_invoke.386
+ ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.281
+ ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.293
+ ___81-[PBBridgeCompanionController refreshTimeoutTimerWithNewActivationGranularState:]_block_invoke.606
+ ___PBDumpLogsWithBlock_block_invoke.293
+ ___PBDumpLogsWithBlock_block_invoke.293.cold.1
+ ___PBDumpLogsWithBlock_block_invoke.297
+ ___block_literal_global.278
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.299
+ ___block_literal_global.307
+ ___block_literal_global.315
+ ___block_literal_global.322
+ ___block_literal_global.35
+ ___block_literal_global.65
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _NRDevicePropertyIsAltAccount
- _NRDevicePropertyIsArchived
- _OBJC_CLASS_$_NSUUID
- _PBIsEarlyPairedSyncSupportedForDevice.cold.1
- _PBVariantSizeForNRDeviceSize
- ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.304
- ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.303
- ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.316
- ___51-[PBBridgeGizmoController ingestTinkerCredentials:]_block_invoke.383
- ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.278
- ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.290
- ___81-[PBBridgeCompanionController refreshTimeoutTimerWithNewActivationGranularState:]_block_invoke.597
- ___PBDumpLogsWithBlock_block_invoke.294.cold.1
- ___PBDumpLogsWithBlock_block_invoke.295
- ___PBDumpLogsWithBlock_block_invoke.298
- ___block_literal_global.279
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.300
- ___block_literal_global.308
- ___block_literal_global.312
- ___block_literal_global.327
- ___block_literal_global.38
- ___block_literal_global.68
- _objc_msgSend$initWithUUIDString:
CStrings:
+ "@\"<RemoteUITelemetryDelegate>\"16@0:8"
+ "Alum-JetBlack"
+ "_setError"
+ "getBytes:range:"
+ "nil device passed to PBIsEarlyPairedSyncSupportedForPDRDevice"
+ "telemetryDelegate"
+ "vp-Gold"
+ "vp-NewNatural"
+ "vp-SilverTwo-Zeus"
+ "vp-Slate"
- "6F13FF03-6511-4180-BBF3-4C231C10D458"
- "Alum-34"
- "initWithUUIDString:"
- "vp-23"
- "vp-36"
- "vp-38"
- "vp-39"

```
