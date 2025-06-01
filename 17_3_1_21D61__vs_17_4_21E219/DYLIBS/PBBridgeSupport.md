## PBBridgeSupport

> `/System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport`

```diff

-1158.10.0.0.0
-  __TEXT.__text: 0x3eff4
+1159.12.0.0.0
+  __TEXT.__text: 0x3f3e4
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x4954
-  __TEXT.__cstring: 0x5abb
+  __TEXT.__objc_methlist: 0x49b4
+  __TEXT.__cstring: 0x5bc1
   __TEXT.__oslogstring: 0x264f
   __TEXT.__const: 0x4b8
   __TEXT.__gcc_except_tab: 0x130
   __TEXT.__dlopen_cstrs: 0x17c
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0xed0
+  __TEXT.__unwind_info: 0xee0
   __TEXT.__objc_classname: 0xab9
-  __TEXT.__objc_methname: 0x8daa
-  __TEXT.__objc_methtype: 0x14a0
-  __TEXT.__objc_stubs: 0x5020
+  __TEXT.__objc_methname: 0x8ee8
+  __TEXT.__objc_methtype: 0x14ab
+  __TEXT.__objc_stubs: 0x50a0
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__const: 0x11c8
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x59f0
-  __DATA_CONST.__objc_selrefs: 0x2138
+  __DATA_CONST.__objc_selrefs: 0x2178
+  __DATA_CONST.__objc_classrefs: 0x3f8
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x5200
+  __AUTH_CONST.__cfstring: 0x53e0
   __AUTH_CONST.__objc_const: 0x1ae8
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x90

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0x1860
-  __DATA.__objc_classrefs: 0x3f8
-  __DATA.__objc_superrefs: 0x228
   __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x318
   __DATA.__bss: 0x1a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73DF62E6-4DAE-3101-A059-63CA0694F48C
-  Functions: 1777
-  Symbols:   5504
-  CStrings:  3499
+  UUID: 7AE74CB1-4080-37F3-B1C1-7B5213317978
+  Functions: 1785
+  Symbols:   5529
+  CStrings:  3539
 
Symbols:
+ +[PBBridgeCAReporter _orientationHumanReadable:]
+ +[PBBridgeCAReporter _pairingStyle:]
+ +[PBBridgeCAReporter _reportingPlatform]
+ +[PBBridgeCAReporter _wristChoiceHumanReadable:]
+ +[PBBridgeCAReporter recordPairingInitiatedDeviceOrientationChoice:pairingSelectionType:]
+ +[PBBridgeCAReporter recordPairingInitiatedDeviceWristChoice:pairingSelectionType:]
+ +[PBBridgeCAReporter recordUserInitiatedDeviceOrientationChange:]
+ +[PBBridgeCAReporter recordUserInitiatedDeviceWristChange:]
+ _PBCADeviceOrientation
+ _PBCAUserInitiatedDeviceOrientationChangeEvent
+ _PBCAUserInitiatedDeviceOrientationChangePlatform
+ _PBCAUserInitiatedDeviceWristChangeEvent
+ _PBCAWristChoice
+ ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.250
+ ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.249
+ ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.262
+ ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.233
+ ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.236
+ ___block_literal_global.258
+ _objc_msgSend$_orientationHumanReadable:
+ _objc_msgSend$_pairingStyle:
+ _objc_msgSend$_reportingPlatform
+ _objc_msgSend$_wristChoiceHumanReadable:
- ___45-[PBBridgeAssetsManager _startAssetDownload:]_block_invoke.226
- ___46-[PBBridgeAssetsManager _beginAssetDownloads:]_block_invoke.225
- ___49-[PBBridgeAssetsManager purgeAllAssetsLocalOnly:]_block_invoke.238
- ___75+[PBBridgeAssetsReachabilityMonitor checkServerReachabilityWithCompletion:]_block_invoke.209
- ___75-[PBBridgeAssetsManager _beginPullingAssetsForDeviceAttributes:completion:]_block_invoke.212
- ___block_literal_global.234
CStrings:
+ "@24@0:8q16"
+ "CrownOnLeft"
+ "CrownOnRight"
+ "DeviceOrientation"
+ "LeftHand"
+ "PairingAutomatic"
+ "PairingManual"
+ "PairingUnset"
+ "RightHand"
+ "SettingsPlatform"
+ "T@\"NSString\",?,R,C"
+ "UnsetCrown"
+ "UnsetHand"
+ "WristChoice"
+ "_orientationHumanReadable:"
+ "_pairingStyle:"
+ "_reportingPlatform"
+ "_wristChoiceHumanReadable:"
+ "com.apple.Bridge.UserInitiatedDeviceOrientationChange"
+ "com.apple.Bridge.UserInitiatedDeviceWristChange"
+ "iOS"
+ "recordPairingInitiatedDeviceOrientationChoice:pairingSelectionType:"
+ "recordPairingInitiatedDeviceWristChoice:pairingSelectionType:"
+ "recordUserInitiatedDeviceOrientationChange:"
+ "recordUserInitiatedDeviceWristChange:"

```
