## NRDUpdated

> `/usr/libexec/NRDUpdated`

```diff

-2422.120.23.0.9
-  __TEXT.__text: 0xc24c
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x1b40
+2717.0.0.0.0
+  __TEXT.__text: 0xb24c
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x1be0
   __TEXT.__objc_methlist: 0xc54
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x10b0
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__objc_methname: 0x1a65
-  __TEXT.__objc_classname: 0x20f
+  __TEXT.__cstring: 0x119a
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__objc_methname: 0x1af1
+  __TEXT.__objc_classname: 0x204
   __TEXT.__objc_methtype: 0x833
-  __TEXT.__oslogstring: 0x1792
-  __TEXT.__unwind_info: 0x3e0
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x168
+  __TEXT.__oslogstring: 0x17bd
+  __TEXT.__unwind_info: 0x350
   __DATA_CONST.__const: 0x6b0
-  __DATA_CONST.__cfstring: 0xe40
+  __DATA_CONST.__cfstring: 0xf80
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0x170
   __DATA.__objc_const: 0x10c8
-  __DATA.__objc_selrefs: 0x858
+  __DATA.__objc_selrefs: 0x880
   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x540

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/BrainTrust.framework/BrainTrust
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7DC5407D-C35C-3307-A85F-41319B3414C5
-  Functions: 277
+  UUID: 568EC0E9-69A3-3086-9563-6B0049C23E36
+  Functions: 275
   Symbols:   2182
-  CStrings:  846
+  CStrings:  872
 
Symbols:
+ -[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScanWithBGActivityAllowed:]
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/MSUShims.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDBackgroundActivitySchedulerServerImpl.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDRemoteableBlock.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateBrainClientImpl.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateBrainLoader.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateDCore.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateDaemonServerImpl.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/nrd_log.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/trust_cache.o
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/NRDBackgroundActivityScheduler/client/
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/NRDBackgroundActivityScheduler/server/
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/NRDUpdateBrainService/client/
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/NRDUpdated/server/
+ /Library/Caches/com.apple.xbs/5EEBAFAD-A4AB-45EC-9640-1C61E2886B9C/TemporaryDirectory.wNp2sM/Sources/MobileSoftwareUpdate_MainOSOnly/UpdateMetrics/Tests/
+ _OBJC_CLASS_$_BrainTrust
+ _OBJC_CLASS_$_NSMutableDictionary
+ __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.503
+ __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.503.cold.1
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.374
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.374.cold.1
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.378
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.379
+ __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.381
+ __47-[NRDUpdateDCore scheduleNRDUpdateBrainReScan:]_block_invoke.535
+ __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.407
+ __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.407.cold.1
+ __74-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScanWithBGActivityAllowed:]_block_invoke.553
+ ___74-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScanWithBGActivityAllowed:]_block_invoke
+ __block_literal_global.343
+ __block_literal_global.406
+ __block_literal_global.409
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$dictionary
+ _objc_msgSend$initWithType:bundlePath:
+ _objc_msgSend$personalizationRequired
+ _objc_msgSend$personalizeAndLoadWithError:
+ _objc_msgSend$scheduleNRDUpdateBrainPeriodicScanWithBGActivityAllowed:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_release_x28
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x3
- -[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScan]
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/MSUShims.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDBackgroundActivitySchedulerServerImpl.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDRemoteableBlock.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateBrainClientImpl.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateBrainLoader.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateDCore.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/NRDUpdateDaemonServerImpl.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/main.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/nrd_log.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Binaries/MobileSoftwareUpdate_MainOSOnly/install/TempContent/Objects/MobileSoftwareUpdate.build/NRDUpdated.build/Objects-normal/arm64e/trust_cache.o
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/NRDBackgroundActivityScheduler/client/
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/NRDBackgroundActivityScheduler/server/
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/NRDUpdateBrainService/client/
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/NRDUpdated/server/
- /Library/Caches/com.apple.xbs/2975F388-11A1-4D1D-8DF7-44F444E7537B/TemporaryDirectory.OTDafU/Sources/MobileSoftwareUpdate_MainOSOnly/UpdateMetrics/Tests/
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.483
- __37-[NRDUpdateDCore actionPeriodicScan:]_block_invoke.483.cold.1
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.353
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.353.cold.1
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.357
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.358
- __41-[NRDUpdateDaemonServerImpl runUntilExit]_block_invoke.360
- __47-[NRDUpdateDCore scheduleNRDUpdateBrainReScan:]_block_invoke.515
- __52-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScan]_block_invoke.533
- __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.386
- __64-[NRDUpdateDaemonServerImpl listener:shouldAcceptNewConnection:]_block_invoke.386.cold.1
- ___52-[NRDUpdateDCore scheduleNRDUpdateBrainPeriodicScan]_block_invoke
- __block_literal_global.356
- __block_literal_global.385
- __block_literal_global.388
- _kSUCoreFilesystemBaseDirDefault
- _objc_msgSend$scheduleNRDUpdateBrainPeriodicScan
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "/var/MobileSoftwareUpdate/Controller/SoftwareUpdateCore_NRD"
+ "10:55:44"
+ "Activity %{public}@ is not allowed, finish"
+ "BaseSystem"
+ "BaseSystem-arm64e"
+ "BaseSystem-x86-64"
+ "Cryptex1,AppOS"
+ "Cryptex1,RosettaOS"
+ "Cryptex1,SystemOS"
+ "May 21 2026"
+ "cryptex-app"
+ "cryptex-system-arm64e"
+ "cryptex-system-rosetta"
+ "dictionary"
+ "initWithType:bundlePath:"
+ "personalizationRequired"
+ "personalizeAndLoadWithError:"
+ "scheduleNRDUpdateBrainPeriodicScanWithBGActivityAllowed:"
+ "setObject:forKeyedSubscript:"
+ "x86,BaseSystem"
- "%@_NRD"
- "20:23:29"
- "Apr 18 2026"
- "scheduleNRDUpdateBrainPeriodicScan"

```
