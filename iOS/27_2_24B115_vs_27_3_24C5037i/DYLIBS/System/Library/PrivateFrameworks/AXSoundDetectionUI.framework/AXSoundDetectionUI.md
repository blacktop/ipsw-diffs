## AXSoundDetectionUI

> `/System/Library/PrivateFrameworks/AXSoundDetectionUI.framework/AXSoundDetectionUI`

```diff

-543.2.5.0.0
-  __TEXT.__text: 0x54aa8
+543.2.11.0.0
+  __TEXT.__text: 0x54e70
   __TEXT.__objc_methlist: 0x2344
   __TEXT.__const: 0xa18
   __TEXT.__oslogstring: 0x65b6

   __DATA_CONST.__objc_selrefs: 0x15c8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__got: 0x698
+  __DATA_CONST.__got: 0x600
   __AUTH_CONST.__const: 0x1118
   __AUTH_CONST.__cfstring: 0xf60
   __AUTH_CONST.__objc_const: 0x3678
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__auth_got: 0xa20
   __AUTH.__objc_data: 0x1588
   __AUTH.__data: 0x300
   __DATA.__objc_ivar: 0x1b8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1460
-  Symbols:   1671
+  Symbols:   1653
   CStrings:  636
 
Symbols:
+ _AXSDSoundDetectionTypeForSound
- _AXSDSoundDetectionTypeApplianceBeeps
- _AXSDSoundDetectionTypeApplianceBellDings
- _AXSDSoundDetectionTypeApplianceBuzzes
- _AXSDSoundDetectionTypeCarHorns
- _AXSDSoundDetectionTypeCatMeows
- _AXSDSoundDetectionTypeCough
- _AXSDSoundDetectionTypeDistressedBaby
- _AXSDSoundDetectionTypeDogBarks
- _AXSDSoundDetectionTypeDoorKnocks
- _AXSDSoundDetectionTypeDoorbells
- _AXSDSoundDetectionTypeFireAlarms
- _AXSDSoundDetectionTypeGlassBreaking
- _AXSDSoundDetectionTypeKShot
- _AXSDSoundDetectionTypeKettle
- _AXSDSoundDetectionTypeNone
- _AXSDSoundDetectionTypePersonShouting
- _AXSDSoundDetectionTypeSirenAlarms
- _AXSDSoundDetectionTypeSmokeAlarms
- _AXSDSoundDetectionTypeWaterRunning
Functions:
~ _AXSDSoundDetectionGenerateUserNotificationForDetectionTypeFromSource : 1684 -> 1752
~ -[AXUltronModelAssetManager _downloadAssets] : 940 -> 980
~ -[AXUltronModelAssetManager _cacheAsset:] : 452 -> 500
~ -[AXUltronModelAssetManager _supportedTypesFromAssets:] : 836 -> 884
~ ___126-[AXUltronModelAssetManager assetController:asset:downloadProgressTotalWritten:totalExpected:isStalled:expectedTimeRemaining:]_block_invoke : 496 -> 548
~ ___113-[AXUltronModelAssetManager assetController:didFinishDownloadingAsset:wasSuccessful:error:hasRemainingDownloads:]_block_invoke : 900 -> 948
~ +[AXSDDetectorManager initializeModelMap] : 544 -> 804
~ sub_2517f4ba8 -> sub_2550d1ddc : 2980 -> 3260
~ sub_2517f580c -> sub_2550d2b58 : 1020 -> 1144
```
