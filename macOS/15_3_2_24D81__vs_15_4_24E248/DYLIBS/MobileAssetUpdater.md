## MobileAssetUpdater

> `/System/Library/PrivateFrameworks/MobileAssetUpdater.framework/Versions/A/MobileAssetUpdater`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x1674
+1207.100.66.0.0
+  __TEXT.__text: 0x168c
   __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x200
   __TEXT.__const: 0x10

   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6A41411B-18D3-3CBE-9A06-F23AF5FDB60E
-  Functions: 54
-  Symbols:   178
+  UUID: EF190CE7-881B-3A95-9371-C350BA22D900
+  Functions: 58
+  Symbols:   183
   CStrings:  231
 
Symbols:
+ -[MobileAssetUpdater downloadAsset:].cold.1
+ -[MobileAssetUpdater purgeAsset].cold.1
+ -[MobileAssetUpdater queryComplete:remote:status:completion:].cold.1
+ _OUTLINED_FUNCTION_0
+ __43-[MobileAssetUpdater findAsset:completion:]_block_invoke.cold.1
Functions:
~ -[MobileAssetUpdater findAsset:completion:] : 1448 -> 1444
~ ___43-[MobileAssetUpdater findAsset:completion:]_block_invoke : 252 -> 208
~ -[MobileAssetUpdater queryComplete:remote:status:completion:] : 880 -> 872
- -[MobileAssetUpdater filterAsset:osBuild:osVersion:]
~ -[MobileAssetUpdater purgeAsset] : 240 -> 204
~ -[MobileAssetUpdater downloadAsset:] : 440 -> 424
- ___36-[MobileAssetUpdater downloadAsset:]_block_invoke
~ -[MobileAssetUpdater doneWithAsset] : 136 -> 128

```
