## PBBridgeSupport

> `/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`

```diff

-1310.1.0.0.0
+1310.1.1.0.0
   __TEXT.__text: 0x43160
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x512c
+  __TEXT.__objc_methlist: 0x513c
   __TEXT.__cstring: 0x5e41
   __TEXT.__const: 0x9c0
   __TEXT.__oslogstring: 0x277c

   __TEXT.__ustring: 0xe
   __TEXT.__unwind_info: 0xf98
   __TEXT.__objc_classname: 0xb03
-  __TEXT.__objc_methname: 0x92af
-  __TEXT.__objc_methtype: 0x171b
+  __TEXT.__objc_methname: 0x92ef
+  __TEXT.__objc_methtype: 0x1773
   __TEXT.__objc_stubs: 0x5620
   __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__const: 0x1408

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2530
+  __DATA_CONST.__objc_selrefs: 0x2538
   __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x5f8
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x5840
-  __AUTH_CONST.__objc_const: 0x7180
+  __AUTH_CONST.__objc_const: 0x7188
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E08649F-1C0D-3329-9115-A65BFC20D205
+  UUID: CC8F4D7C-D120-30E6-B0AB-7AC30BC673F6
   Functions: 1839
   Symbols:   5796
-  CStrings:  3727
+  CStrings:  3730
 
Symbols:
+ ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.318
+ ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.331
+ ___53-[PBBridgeCompanionController _processActivationData]_block_invoke.590
+ ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke.319
+ ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.293
+ ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.305
+ ___81-[PBBridgeCompanionController refreshTimeoutTimerWithNewActivationGranularState:]_block_invoke.619
+ ___block_literal_global.327
- ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.309
- ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.322
- ___53-[PBBridgeCompanionController _processActivationData]_block_invoke.581
- ___59-[PBBridgeAssetsManager _startAssetDownload:downloadGroup:]_block_invoke.310
- ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.284
- ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.296
- ___81-[PBBridgeCompanionController refreshTimeoutTimerWithNewActivationGranularState:]_block_invoke.610
- ___block_literal_global.318
CStrings:
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
