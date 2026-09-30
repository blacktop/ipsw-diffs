## softwareupdated

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0xba6fc
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x5d00
+2171.101.1.0.0
+  __TEXT.__text: 0xb04a0
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_stubs: 0x59e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2560
-  __TEXT.__const: 0x77978
-  __TEXT.__gcc_except_tab: 0x8e0
-  __TEXT.__cstring: 0x18958
-  __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x652d
-  __TEXT.__objc_methtype: 0x18d3
-  __TEXT.__oslogstring: 0x5a05
+  __TEXT.__objc_methlist: 0x269c
+  __TEXT.__const: 0x778e8
+  __TEXT.__gcc_except_tab: 0x8b4
+  __TEXT.__cstring: 0x18140
+  __TEXT.__objc_classname: 0x4af
+  __TEXT.__objc_methname: 0x6157
+  __TEXT.__objc_methtype: 0x18ae
+  __TEXT.__oslogstring: 0x486e
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x17f0
-  __TEXT.__eh_frame: 0x360
-  __DATA_CONST.__auth_got: 0xf40
-  __DATA_CONST.__got: 0x468
+  __TEXT.__unwind_info: 0x1680
+  __TEXT.__eh_frame: 0x318
+  __DATA_CONST.__auth_got: 0xe08
+  __DATA_CONST.__got: 0x428
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x3bf0
-  __DATA_CONST.__cfstring: 0xd000
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__const: 0x3818
+  __DATA_CONST.__cfstring: 0xc9e0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x110
-  __DATA_CONST.__objc_intobj: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x6f8
   __DATA_CONST.__objc_dictobj: 0x258
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x4438
-  __DATA.__objc_selrefs: 0x1b78
-  __DATA.__objc_ivar: 0x240
-  __DATA.__objc_data: 0xc30
-  __DATA.__data: 0xb60
-  __DATA.__bss: 0x2a0
+  __DATA.__objc_const: 0x35e0
+  __DATA.__objc_selrefs: 0x1b98
+  __DATA.__objc_ivar: 0x23c
+  __DATA.__objc_data: 0xaa0
+  __DATA.__data: 0xab0
+  __DATA.__bss: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libimage4.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 266A4BA9-39BB-3AA1-9C74-8F83EEABDE50
-  Functions: 2277
-  Symbols:   11944
-  CStrings:  6787
+  - /usr/lib/libpartition2_dynamic.dylib
+  UUID: EE5712DE-4D26-3AFD-8875-12E129F1B8EE
+  Functions: 2168
+  Symbols:   11347
+  CStrings:  6494
 
Symbols:
+ +[MSUBootObjectCopier buildManifestFromBuildIdentity:]
+ +[MSUBootObjectCopier buildManifestFromBuildIdentity:].cold.1
+ +[MSUBrainDelegateImpl_softwareupdated sharedInstance].cold.1
+ +[MSUNRDUpdateBrainController sharedInstance].cold.1
+ +[MSUSupport sharedSupport].cold.1
+ +[MSUTargetController sharedController].cold.1
+ +[MSUUpdateBrainLocator locatorsDictionary].cold.1
+ +[MSUUpdateBrainLocator locatorsStateQueue].cold.1
+ +[UMEventRecorder submitQueue].cold.1
+ -[MSUBootObjectCopier _hardwareModel]
+ -[MSUBootObjectCopier _manifestRuleForTag:]
+ -[MSUBootObjectCopier populateSystemRecoveryVolume:buildIdentity:nsih:fetchBootObjectBlock:]
+ -[MSUTargetController populatePairedRecoveryWithVariant:updateBundlePath:buildIdentity:supportStagedBoot:error:]
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.1
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.2
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.3
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.4
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.5
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.6
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.7
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.8
+ -[NVMEiBootUpdater _copyIBICFromPath:withOptions:intoArray:withError:].cold.9
+ -[UMEventRecorder _getMacPlatform].cold.1
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/bless_libraries/bless2/libbless2/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUBootObjectCopier.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libbless2.a(bless2.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libbless2.a(log.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libBuildInfo.a(BIDeviceInformation.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDRemoteableBlock.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDUpdateBrainClientImpl.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(NRDUpdateDaemonClientImpl.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libNRDUpdateClient_static.a(nrd_log.o)
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUAnalytics.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUBrainClientImpl.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUBrainDelegateImpl_softwareupdated.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUNRDUpdateBrain.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUNRDUpdateBrainController.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSURemoteableBlock.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUResultState.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUSupport.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUTTRHandler.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUTargetController.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUUpdateBrainLocator.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdate.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cache_delete.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cleanup_prepare_path_client.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/clientServerIPC.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-21eb89572409f4f5ee695d65cb051d7f.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-3b69fe07e8e9325dc0823d0aa24d810a.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cryptegraft_client.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/gpu_bridge.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/log.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/msu_log.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/msu_nvram.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/nrd_crypto.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/restore_log.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/softwareupdated.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/softwareupdated_handlers.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/trust_cache.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/BuildInfo/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUAnalytics/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDBackgroundActivityScheduler/client/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDUpdateBrainService/client/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDUpdated/client/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/client/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/framework/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/softwareupdated/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/softwareupdated/MSUBrainDelegate/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/UpdateMetrics/UpdateMetrics/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/MSUBootFirmwareUpdater/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/libusbrestore/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/macOS/
+ /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/restored/AsyncCheckpoint/
+ AMRestorePartitionFWCopyTagData.cold.1
+ AMRestorePartitionFWCopyTagData.cold.10
+ AMRestorePartitionFWCopyTagData.cold.2
+ AMRestorePartitionFWCopyTagData.cold.3
+ AMRestorePartitionFWCopyTagData.cold.4
+ AMRestorePartitionFWCopyTagData.cold.5
+ AMRestorePartitionFWCopyTagData.cold.6
+ AMRestorePartitionFWCopyTagData.cold.7
+ AMRestorePartitionFWCopyTagData.cold.8
+ AMRestorePartitionFWCopyTagData.cold.9
+ BrotliFindAllStaticDictionaryMatches.cold.1
+ BrotliFindAllStaticDictionaryMatches.cold.2
+ GCC_except_table205
+ _AMRestorePartitionOpenFileWithURL.cold.1
+ _AMRestorePartitionOpenFileWithURL.cold.2
+ _BIDeviceInfoGetMacPlatformString
+ _BuildAndStoreEntropyCodesDistance
+ _MSUPreferencesCopyValueForDomain.cold.1
+ _OBJC_CLASS_$_LPStaticAPFSContainer
+ _OBJC_CLASS_$_LPStaticAPFSPhysicalStore
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_LPStaticPartitionMedia
+ __BIDeviceInfoGetMacPlatform
+ __copy_shared_cleanup_service_connection_block_invoke.cold.1
+ __copy_shared_cryptegraft_service_connection_block_invoke.cold.1
+ __handle_ma_load_brain_block_invoke.cold.1
+ __main_block_invoke.10.cold.1
+ __main_block_invoke_2.cold.2
+ __main_block_invoke_3.cold.3
+ __main_block_invoke_4.cold.1
+ __perform_self_destruct_block_invoke.cold.1
+ _copy_extra_paths
+ _dirname
+ _objc_msgSend$_hardwareModel
+ _objc_msgSend$_manifestRuleForTag:
+ _objc_msgSend$buildManifestFromBuildIdentity:
+ _string_for_bp_error
+ bless2_install_internal.cold.31
+ copy_extra_paths.cold.1
+ copy_extra_paths.cold.2
+ copy_extra_paths.cold.3
+ copy_extra_paths.cold.4
+ copy_extra_paths.cold.5
+ copy_extra_paths.cold.6
+ copy_extra_paths.cold.7
+ copy_extra_paths.cold.8
+ copy_shared_cleanup_service_connection.cold.1
+ copy_shared_cryptegraft_service_connection.cold.1
+ copy_underlying_error_description.cold.1
+ get_peer_connections_queue.cold.1
+ handle_create_update_brain_connection.cold.1
+ handle_mark_self_dirty.cold.1
+ joinThread.cold.1
+ logfunctionv.cold.1
+ msuSharedLogger.cold.1
+ nrdSharedLogger.cold.1
- +[LPAPFSContainer allAPFSContainers]
- +[LPAPFSContainer diagsContainer]
- +[LPAPFSContainer supportedContentTypes]
- +[LPAPFSPhysicalStore supportedContentTypes]
- +[LPAPFSVolume _loadMountPointTableForMode:]
- +[LPAPFSVolume defaultMountPointGivenRole:]
- +[LPAPFSVolume defaultVolumeNameGivenRole:]
- +[LPAPFSVolume initialize]
- +[LPAPFSVolume supportedContentTypes]
- +[LPMedia _copyIOMediaForDiskWithPath:]
- +[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]
- +[LPMedia allMedia]
- +[LPMedia hasEmbeddedDeviceTypeRoot]
- +[LPMedia liveMediaForSnapshotAtPath:]
- +[LPMedia mediaForBSDNameOrDeviceNode:]
- +[LPMedia mediaForPath:]
- +[LPMedia mediaForPath:isSnapshot:]
- +[LPMedia mediaForPath:snapshotName:]
- +[LPMedia mediaForUUID:]
- +[LPMedia snapshotNameForMediaForPath:]
- +[LPMedia supportedContentTypes]
- +[LPMedia(Private) contentTypeToSubclassMap]
- +[LPMedia(Private) mediaOfCorrectTypeGivenIOMedia:]
- +[LPMedia(Private) waitForBlockStorage]
- +[LPMedia(Private) waitForIOMediaWithDevNode:]
- +[LPPartitionMedia contentTypesForPartitionMedia]
- +[LPPartitionMedia primaryMedia]
- +[LPPartitionMedia supportedContentTypes]
- -[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]
- -[LPAPFSContainer physicalStores]
- -[LPAPFSContainer prebootVolume]
- -[LPAPFSContainer recoveryVolume]
- -[LPAPFSContainer updateVolume]
- -[LPAPFSContainer volumesWithRole:]
- -[LPAPFSContainer volumes]
- -[LPAPFSPhysicalStore container]
- -[LPAPFSPhysicalStore parent]
- -[LPAPFSPhysicalStore role]
- -[LPAPFSVolume _createTemporaryMountPointWithError:]
- -[LPAPFSVolume container]
- -[LPAPFSVolume createSnapshot:error:]
- -[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]
- -[LPAPFSVolume deleteVolumeWithError:]
- -[LPAPFSVolume eraseVolumeWithError:]
- -[LPAPFSVolume isCaseSenstive]
- -[LPAPFSVolume isEncrypted]
- -[LPAPFSVolume isFilevaultEncrypted]
- -[LPAPFSVolume isMounted]
- -[LPAPFSVolume mountAtPath:error:]
- -[LPAPFSVolume mountAtPath:options:error:]
- -[LPAPFSVolume mountAtTemporaryPathWithError:]
- -[LPAPFSVolume mountAtTemporaryPathWithOptions:error:]
- -[LPAPFSVolume mountWithError:]
- -[LPAPFSVolume pairedVolume]
- -[LPAPFSVolume renameSnapshot:to:error:]
- -[LPAPFSVolume revertToSnapshot:error:]
- -[LPAPFSVolume revertToSnapshot:options:error:]
- -[LPAPFSVolume role]
- -[LPAPFSVolume rootToSnapshot:error:]
- -[LPAPFSVolume setRole:withError:]
- -[LPAPFSVolume snapshotInfoWithError:]
- -[LPAPFSVolume snapshotMountPoints]
- -[LPAPFSVolume snapshotsWithError:]
- -[LPAPFSVolume unmountAllWithError:]
- -[LPAPFSVolume unmountWithError:]
- -[LPAPFSVolume unmountWithOptions:error:]
- -[LPAPFSVolume volumeGroupUUID]
- -[LPMedia BSDName]
- -[LPMedia _deviceCharacteristicStringForKey:]
- -[LPMedia content]
- -[LPMedia dealloc]
- -[LPMedia description]
- -[LPMedia devNodePath]
- -[LPMedia deviceModel]
- -[LPMedia initWithIOMediaObject:]
- -[LPMedia ioMedia]
- -[LPMedia isEmbeddedDeviceTypeRoot]
- -[LPMedia isEqual:]
- -[LPMedia isInternal]
- -[LPMedia isJournaled]
- -[LPMedia isPrimaryMedia]
- -[LPMedia isReadOnly]
- -[LPMedia isWhole]
- -[LPMedia mediaUUID]
- -[LPMedia mountPoint]
- -[LPMedia name]
- -[LPMedia setIoMedia:]
- -[LPMedia setName:withError:]
- -[LPMedia storageMedium]
- -[LPMedia vendorName]
- -[LPMedia wholeMediaForMedia]
- -[LPMedia(Private) getBoolPropertyWithName:]
- -[LPMedia(Private) getPropertyWithName:]
- -[LPMedia(Private) getStringPropertyWithName:]
- -[LPPartitionMedia children]
- -[MSUBootObjectCopier populateSystemRecoveryVolume:fromBuildIdentity:withNSIH:fetchBootObjectBlock:]
- -[MSUTargetController populatePairedRecoveryWithVariant:updateBundlePath:buildIdentity:error:]
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUBootObjectCopier.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libbless2.a(bless2.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libbless2.a(log.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUAnalytics.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUBrainClientImpl.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUBrainDelegateImpl_softwareupdated.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUNRDUpdateBrain.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUNRDUpdateBrainController.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSURemoteableBlock.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUResultState.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUSupport.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUTTRHandler.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUTargetController.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MSUUpdateBrainLocator.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdate.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cache_delete.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cleanup_prepare_path_client.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/clientServerIPC.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-21eb89572409f4f5ee695d65cb051d7f.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/common-3b69fe07e8e9325dc0823d0aa24d810a.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/cryptegraft_client.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/gpu_bridge.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/log.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/msu_log.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/msu_nvram.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/nrd_crypto.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/restore_log.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/softwareupdated.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/softwareupdated_handlers.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/softwareupdated.build/Objects-normal/arm64e/trust_cache.o
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Root/usr/local/lib/libBuildInfo.a(BIDeviceInformation.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDRemoteableBlock.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDUpdateBrainClientImpl.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Root/usr/local/lib/libNRDUpdateClient_static.a(NRDUpdateDaemonClientImpl.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Root/usr/local/lib/libNRDUpdateClient_static.a(nrd_log.o)
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/BuildInfo/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/MSUAnalytics/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDBackgroundActivityScheduler/client/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDUpdateBrainService/client/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/NRDUpdated/client/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/client/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/framework/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/softwareupdated/
- /AppleInternal/Library/BuildRoots/51ca780d-ccf8-11ef-8fc9-d285688f7a47/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/softwareupdated/MSUBrainDelegate/
- /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ramrod/MSUBootFirmwareUpdater/
- /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ramrod/libusbrestore/
- /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/
- /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/macOS/
- /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ramrod/restored/AsyncCheckpoint/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/libpartition2/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/UpdateMetrics/UpdateMetrics/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/bless_libraries/bless2/libbless2/
- BIDeviceInfoGetMacPlatform.once
- BIDeviceInfoGetMacPlatform.platform
- GCC_except_table199
- LPAPFSContainer.m
- LPAPFSContainer_Private.m
- LPAPFSPhyscialStore_Private.m
- LPAPFSPhysicalStore.m
- LPAPFSVolume.m
- LPAPFSVolume_Private.m
- LPIOKitHelper.m
- LPLog.m
- LPMedia.m
- LPPartitionMedia.m
- OBJC_IVAR_$_LPMedia._ioMedia
- _APFSVolumeCreate
- _APFSVolumeCreateForMSU
- _APFSVolumeDelete
- _APFSVolumeGetVEKState
- _APFSVolumeRole
- _BIDeviceInfoGetMacPlatform
- _IOIteratorIsValid
- _IOIteratorReset
- _IOObjectIsEqualTo
- _IORegistryIteratorExitEntry
- _IOServiceGetMatchingServices
- _LPAPFSContainerMediaTypeUUID
- _LPAPFSPhysicalStoreDiagsMediaUUID
- _LPAPFSPhysicalStoreMediaUUID
- _LPAPFSPhysicalStoreRecoveryMediaUUID
- _LPAPFSSnapshotPropertyKeyMarkedForRevert
- _LPAPFSSnapshotPropertyKeyMarkedForRoot
- _LPAPFSSnapshotPropertyKeyXID
- _LPAPFSVolumeMediaTypeUUID
- _LPAPFSVolumeMountOptionReadOnly
- _LPAPFSVolumeMountOptionSnapshotName
- _LPAPFSVolumeRevertOptionSkipRemount
- _LPAPFSVolumeSnapshotMountPointKeyMountPoint
- _LPAPFSVolumeSnapshotMountPointKeyName
- _LPAPFSVolumeUnmountOptionAll
- _LPAPFSVolumeUnmountOptionDoNotLock
- _LPAPFSVolumeUnmountOptionForce
- _LPAPFSVolumeUnmountOptionSnapshotName
- _LPLogObject.obj
- _LPLogObject.onceToken
- _NSLocalizedFailureReasonErrorKey
- _NSOSStatusErrorDomain
- _OBJC_CLASS_$_LPAPFSContainer
- _OBJC_CLASS_$_LPAPFSPhysicalStore
- _OBJC_CLASS_$_LPAPFSVolume
- _OBJC_CLASS_$_LPMedia
- _OBJC_CLASS_$_LPPartitionMedia
- _OBJC_METACLASS_$_LPAPFSContainer
- _OBJC_METACLASS_$_LPAPFSPhysicalStore
- _OBJC_METACLASS_$_LPAPFSVolume
- _OBJC_METACLASS_$_LPMedia
- _OBJC_METACLASS_$_LPPartitionMedia
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- __26-[LPAPFSContainer volumes]_block_invoke.20
- __28-[LPPartitionMedia children]_block_invoke.13
- __LPLogObject
- __LPLogPack
- __OBJC_$_CLASS_METHODS_LPAPFSContainer
- __OBJC_$_CLASS_METHODS_LPAPFSPhysicalStore
- __OBJC_$_CLASS_METHODS_LPAPFSVolume
- __OBJC_$_CLASS_METHODS_LPMedia(Private)
- __OBJC_$_CLASS_METHODS_LPPartitionMedia
- __OBJC_$_INSTANCE_METHODS_LPAPFSContainer
- __OBJC_$_INSTANCE_METHODS_LPAPFSPhysicalStore
- __OBJC_$_INSTANCE_METHODS_LPAPFSVolume
- __OBJC_$_INSTANCE_METHODS_LPMedia(Private)
- __OBJC_$_INSTANCE_METHODS_LPPartitionMedia
- __OBJC_$_INSTANCE_VARIABLES_LPMedia
- __OBJC_$_PROP_LIST_LPMedia
- __OBJC_CLASS_RO_$_LPAPFSContainer
- __OBJC_CLASS_RO_$_LPAPFSPhysicalStore
- __OBJC_CLASS_RO_$_LPAPFSVolume
- __OBJC_CLASS_RO_$_LPMedia
- __OBJC_CLASS_RO_$_LPPartitionMedia
- __OBJC_METACLASS_RO_$_LPAPFSContainer
- __OBJC_METACLASS_RO_$_LPAPFSPhysicalStore
- __OBJC_METACLASS_RO_$_LPAPFSVolume
- __OBJC_METACLASS_RO_$_LPMedia
- __OBJC_METACLASS_RO_$_LPPartitionMedia
- ___26-[LPAPFSContainer volumes]_block_invoke
- ___28-[LPPartitionMedia children]_block_invoke
- ___39+[LPMedia snapshotNameForMediaForPath:]_block_invoke
- ___41-[LPAPFSVolume unmountWithOptions:error:]_block_invoke
- ___44+[LPMedia(Private) contentTypeToSubclassMap]_block_invoke
- ___BIDeviceInfoGetMacPlatform_block_invoke
- ___NSArray0__
- ____LPLogObject_block_invoke
- ____is_running_in_ramdisk_block_invoke
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
- ___block_descriptor_44_e8_32r_e8_v12?0I8l
- ___block_descriptor_44_e8_32s_e8_v12?0I8l
- __block_literal_global.164
- __block_literal_global.186
- __execForLibpartition
- __lp2_delete_directory_contents
- __lp2_delete_directory_contents_confirm
- __lp2_delete_directory_contents_error
- __os_log_pack_fill
- __os_log_pack_size
- _dprintf
- _execlogfunction
- _fs_snapshot_create
- _fs_snapshot_delete
- _fs_snapshot_list
- _fs_snapshot_rename
- _fs_snapshot_revert
- _fs_snapshot_root
- _fsctl
- _is_running_in_ramdisk.is_ramdisk
- _is_running_in_ramdisk.onceToken
- _iterateSafely
- _kAPFSVolumeCaseSensitiveKey
- _kAPFSVolumeFSIndexKey
- _kAPFSVolumeGroupSiblingFSIndexKey
- _kAPFSVolumeNameKey
- _kAPFSVolumeNoAutomountAtCreateKey
- _kAPFSVolumeQuotaSizeKey
- _kAPFSVolumeReserveSizeKey
- _kAPFSVolumeRoleKey
- _kLPDefaultLiveOSMountPointTable
- _kLPDefaultMountPointTable
- _kLPDefaultRAMDiskMountPointTable
- _lchflags
- _mkpath_np
- _mkstempsat_np
- _objc_msgSend$_copyIOMediaForDiskWithPath:
- _objc_msgSend$_copyLiveFilesystemIOMediaForRootedSnapshot
- _objc_msgSend$_createTemporaryMountPointWithError:
- _objc_msgSend$_deviceCharacteristicStringForKey:
- _objc_msgSend$_loadMountPointTableForMode:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$content
- _objc_msgSend$contentTypeToSubclassMap
- _objc_msgSend$contentTypesForPartitionMedia
- _objc_msgSend$getBoolPropertyWithName:
- _objc_msgSend$getCString:maxLength:encoding:
- _objc_msgSend$getPropertyWithName:
- _objc_msgSend$getStringPropertyWithName:
- _objc_msgSend$ioMedia
- _objc_msgSend$isEmbeddedDeviceTypeRoot
- _objc_msgSend$isWhole
- _objc_msgSend$mediaForPath:snapshotName:
- _objc_msgSend$mediaOfCorrectTypeGivenIOMedia:
- _objc_msgSend$mountAtTemporaryPathWithOptions:error:
- _objc_msgSend$primaryMedia
- _objc_msgSend$rangeOfString:options:
- _objc_msgSend$setIoMedia:
- _objc_msgSend$snapshotMountPoints
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$supportedContentTypes
- _objc_msgSend$unmountWithOptions:error:
- _objc_msgSend$waitForBlockStorage
- _objc_msgSend$waitForIOMediaWithDevNode:
- _os_log_pack_compose
- _os_log_pack_send
- _pipe
- _posix_spawn
- _posix_spawn_file_actions_addclose
- _posix_spawn_file_actions_adddup2
- _posix_spawn_file_actions_destroy
- _posix_spawn_file_actions_init
- _posix_spawnattr_destroy
- _posix_spawnattr_init
- _posix_spawnattr_setflags
- _removefile
- _removefile_state_alloc
- _removefile_state_free
- _removefile_state_set
- _sConsoleFD
- _sLegacyVolumeNameMapping
- _sLogLevel
- _sLogToConsole
- _sLogToOSLog
- _sLogToStandardOut
- _sMountPointLookupTable
- _sRoleEncodingMapping
- _sRoleLookupTable
- _setattrlist
- _unmount
- contentTypeToSubclassMap.once
- contentTypeToSubclassMap.sharedMap
CStrings:
+ "%s: Build identity seems to be missing marketing version.\n"
+ "%s: Build identity was missing build number.\n"
+ "%s: Build identity was missing supported device model.\n"
+ "%s: Failed to write system recovery build manifest to %s\n"
+ "+[MSUBootObjectCopier buildManifestFromBuildIdentity:]"
+ "-[MSUBootObjectCopier _hardwareModel]"
+ "-[MSUBootObjectCopier populateSystemRecoveryVolume:buildIdentity:nsih:fetchBootObjectBlock:]"
+ "../"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBasicStreams.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBuffers.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPool.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyBaseSystemPatch.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyPatches.c"
+ "@\"LPStaticAPFSContainer\""
+ "@\"LPStaticAPFSVolume\""
+ "Ap,ProductMarketingVersion"
+ "Ap,ProductType"
+ "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24"
+ "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=^{RestoredHostConnection}^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}CC^v^{__CFDictionary}C}24^@32"
+ "B52@0:8@16@24@32B40^@44"
+ "BuildNumber"
+ "ExtraPaths"
+ "MSUBootObjectCopier.m"
+ "ManifestVersion"
+ "Q24@0:8@16"
+ "Required"
+ "SupportedProductTypes"
+ "T@\"LPStaticAPFSContainer\",&,N,V_targetContainer"
+ "T@\"LPStaticAPFSContainer\",&,N,V_updateContainer"
+ "T@\"LPStaticAPFSVolume\",&,N,V_targetVolume"
+ "_hardwareModel"
+ "_manifestRuleForTag:"
+ "buildIdentity"
+ "buildManifestFromBuildIdentity:"
+ "cannot get path for dst_dir: %d\n"
+ "cannot get path for src_dir: %d\n"
+ "copy '%s' -> '%s'\n"
+ "copyfile failed: %d\n"
+ "failed to copy extra paths"
+ "failed to copy extra paths\n"
+ "failed to create containing directory for symlinks %s: %s\n"
+ "failed to create containing directory: %d\n"
+ "ignoring ENOENT"
+ "ignoring ENOENT\n"
+ "invalid %s (not an array)\n"
+ "invalid %s entry\n"
+ "invalid %s entry (traversal)\n"
+ "other"
+ "populatePairedRecoveryWithVariant:updateBundlePath:buildIdentity:supportStagedBoot:error:"
+ "populateSystemRecoveryVolume:buildIdentity:nsih:fetchBootObjectBlock:"
+ "symlinking %@ -> %@\n"
+ "usr/standalone/firmware/arm64eBaseSystem.dmg.staged"
- "%.*s"
- "%@: %@"
- "%@: %@, Mount: %@"
- "%@: %@, UUID: %@"
- "%@s%d"
- "%s : APFSVolumeCreateForMSU exists and we're creating a System volume. Preferring it to APFSVolumeCreate."
- "%s : Add volume failed with error: %d."
- "%s : Can not iterate over physical store services."
- "%s : Container is missing UUID?"
- "%s : Container is somehow missing a BSD name."
- "%s : Container isn't a container?!"
- "%s : Could not open device is not mounted."
- "%s : Could not open device mount %{private}@."
- "%s : Could not set root from snapshot. Errno: %d"
- "%s : Creating APFS volume %s with options: %@"
- "%s : Error in reading attributes for directory entry %d"
- "%s : Failed because target volume is not mounted"
- "%s : Failed to delete snapshot: %{private}@, %d"
- "%s : Failed to encode snapshot name %{private}s for some reason."
- "%s : Failed to get content type."
- "%s : Failed to open media for snapshot delete: %d"
- "%s : IOIterator was still invalid after attempting %d times"
- "%s : Need a valid new snapshot name."
- "%s : Need a valid snapshot name."
- "%s : Need a valid snapshot names."
- "%s : Paired volume is not valid if role is not system."
- "%s : Paired volume must be in the same container"
- "%s : Requested system volume with sibling but the key is not supported."
- "%s : Unable to get parent iterator"
- "%s : Unable to get the iterator for entry."
- "%s : Unable to open mount point %{private}@: %d"
- "%s : Volume name is invalid"
- "%s : Waiting for snapshots to delete timed out"
- "%s : You need to specify a volume name."
- "%s : failed to read value for property named: %@"
- "%s : failed with iokit error: %d"
- "%s : failed with posix error: %d"
- "%s : failed with unknown kern_return_t error: %d"
- "%s : fs_snapshot_list failed with error %d"
- "%s : going to delete apfs volume ( %@ )"
- "%s : volume is missing a dev node somehow"
- "%s called but %{private}@ is not mounted."
- "%s called on device with no dev node"
- "%s was stopped by signal %d"
- "%s was terminated by signal %d"
- "%s: %@ isn't an APFS volume"
- "%s: Error getting snapshot info for %@: %@"
- "%s: Failed to find primary media"
- "%s: Failed to get IOMedia objects"
- "%s: Failed to obtain parent IOMedia for disk at path %{private}@"
- "%s: Failed to remount volume with error: %d"
- "%s: Failed to set name for volume: %s\n"
- "%s: Failed to unmount volume with error: %d"
- "%s: Mount point is %{private}@\n"
- "%s: No disk for %{private}@"
- "%s: No media found for path: %{private}@"
- "%s: No snapshot is tagged for boot and none match the naming scheme"
- "%s: Not on a rooted snapshot disk, will return self: %{private}@"
- "%s: Parent of disk backing %{private}@ is not an APFS volume"
- "%s: Skipping unmount/remount of %@"
- "%s: Successfully set volume name to %{private}@\n"
- "%s: Trying to determine mount point\n"
- "%s: Volume is not mounted. Unable to set name\n"
- "%s: could not look up snapshot by UUID: %d (%s)"
- "%s: could not parse %s %{private}s: %{private}@"
- "%s: failed to get journaled status for %@\n"
- "%s: failed to get read-only status for %@\n"
- "%s: failed to get role. Error: %d"
- "%s: no IOMedia for %@ (device 0x%lx)"
- "%s: no filesystem for %@ (%d): %s"
- "%s: path is a snapshot, but has no name: %{private}@"
- "%s: statfs failed: %d (%s)"
- "%{private}s is a firmlink. Clearing firmlink."
- "+[LPAPFSContainer diagsContainer]"
- "+[LPMedia _copyIOMediaForDiskWithPath:]"
- "+[LPMedia _copyLiveFilesystemIOMediaForRootedSnapshot]"
- "+[LPMedia allMedia]"
- "+[LPMedia liveMediaForSnapshotAtPath:]"
- "+[LPMedia mediaForPath:snapshotName:]"
- "+[LPMedia snapshotNameForMediaForPath:]"
- "-[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:]"
- "-[LPAPFSContainer physicalStores]"
- "-[LPAPFSPhysicalStore container]"
- "-[LPAPFSPhysicalStore parent]"
- "-[LPAPFSPhysicalStore role]"
- "-[LPAPFSVolume createSnapshot:error:]"
- "-[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:]"
- "-[LPAPFSVolume deleteVolumeWithError:]"
- "-[LPAPFSVolume eraseVolumeWithError:]"
- "-[LPAPFSVolume renameSnapshot:to:error:]"
- "-[LPAPFSVolume revertToSnapshot:options:error:]"
- "-[LPAPFSVolume role]"
- "-[LPAPFSVolume rootToSnapshot:error:]"
- "-[LPAPFSVolume snapshotInfoWithError:]"
- "-[LPAPFSVolume snapshotMountPoints]"
- "-[LPMedia isJournaled]"
- "-[LPMedia isReadOnly]"
- "-[LPMedia setName:withError:]"
- "-[LPMedia wholeMediaForMedia]"
- "-[LPMedia(Private) getPropertyWithName:]"
- "-[MSUBootObjectCopier _preservedTicketNameForRunningDeviceWithPersonalization:]"
- "-[MSUBootObjectCopier populateSystemRecoveryVolume:fromBuildIdentity:withNSIH:fetchBootObjectBlock:]"
- "-n"
- "-o"
- "-restore"
- "-s"
- ".XXXXXXXX"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBasicStreams.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBuffers.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPool.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyBaseSystemPatch.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyImagePatch.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyPatches.c"
- "/dev/%@"
- "/mnt1"
- "/mnt10"
- "/mnt11"
- "/mnt2"
- "/mnt3"
- "/mnt4"
- "/mnt5/tmp-mount-XXXXXX"
- "/mnt6"
- "/mnt7"
- "/mnt8"
- "/private/var/"
- "/private/var/hardware"
- "/private/var/internal"
- "/private/var/logs"
- "/private/var/mobile"
- "/private/var/recovery/"
- "/private/var/vm"
- "/private/var/wireless/baseband_data"
- "/private/xarts"
- "/sbin/mount_apfs"
- "/tmp//tmp-mount-XXXXXX"
- "41504653-0000-11AA-AA11-00306543ECAC"
- "@\"LPAPFSContainer\""
- "@\"LPAPFSVolume\""
- "@%@"
- "@32@0:8@16^B24"
- "@64@0:8@16i24B28q32q40@48^@56"
- "AppleAPFSSnapshot"
- "Apple_partition_scheme"
- "B28@0:8i16^@20"
- "B32@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16d24^@32"
- "B40@0:8^{ramrod_update_callbacks=i^?^?^?^?^?^?^?^?^{ramrod_updater}^?^?^?^?^?^?}16^{firmware_update_context=i^{__CFDictionary}^v^{__CFDictionary}^{__CFDictionary}^vCC^v^{__CFDictionary}C}24^@32"
- "B48@0:8@16@24@32^@40"
- "BSD Major"
- "BSD Minor"
- "Baseband Data"
- "Call to APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ returned EEXIST\n"
- "Can not mount (%@) because mount returned %d."
- "Can not mount (%s) because it does not appear to have a device node."
- "Can not mount (%{private}s) because we could not create its mount folder (%{private}s)."
- "CaseSensitive"
- "Could not removefile(3) path %{private}s: %s"
- "Could not reset metadata on %{private}s: %s"
- "Couldn't create a temporary mount point %s"
- "Data"
- "Deleting contents of %{private}s %s (result: %d)."
- "Deleting contents of %{private}s..."
- "EF57347C-0000-11AA-AA11-00306543ECAC"
- "Error: More than one preboot volume found: %{private}@"
- "Error: More than one recovery volume found: %{private}@"
- "Error: More than one update volume found: %{private}@"
- "FDisk_partition_scheme"
- "Failed to call APFS_FSCTL_UNMOUNT_CRYPTO_HINT on %@ with errno %d\n"
- "Failed to clear the firmlink on %s with error: %{private}s"
- "Failed to create container volumes iterator"
- "Failed to create partition media iterator."
- "Failed to find media for %@"
- "Failed to read firm link information for %{private}s: %s"
- "Failed to unmount %@ **FORCING UNMOUNT** error: %d"
- "Failed to unmount %@ retry: %s error: %d"
- "FireWire Vendor Name"
- "GUID_partition_scheme"
- "Hardware"
- "I24@0:8@16"
- "IOKit service wait timed out, volumes may be stale."
- "IOKit wait timed out, volume for media may be stale."
- "LPAPFSContainer"
- "LPAPFSPhysicalStore"
- "LPAPFSSnapshotPropertyKeyMarkedForRevert"
- "LPAPFSSnapshotPropertyKeyMarkedForRoot"
- "LPAPFSSnapshotPropertyKeyName"
- "LPAPFSSnapshotPropertyKeyXID"
- "LPAPFSVolume"
- "LPAPFSVolumeMountOptionNoBrowse"
- "LPAPFSVolumeMountOptionNoFirmlinks"
- "LPAPFSVolumeMountOptionReadOnly"
- "LPAPFSVolumeMountOptionSnapshotName"
- "LPAPFSVolumeRevertOptionSkipRemount"
- "LPAPFSVolumeSnapshotMountPointKeyMountPoint"
- "LPAPFSVolumeSnapshotMountPointKeyName"
- "LPAPFSVolumeUnmountOptionAll"
- "LPAPFSVolumeUnmountOptionDoNotLock"
- "LPAPFSVolumeUnmountOptionForce"
- "LPAPFSVolumeUnmountOptionSnapshotName"
- "LPMedia"
- "LPPartitionMedia"
- "Logs"
- "MSUBootObjectCopierFetchBootObjectBootabilityBundleTag"
- "MSUBootObjectCopierFetchBootObjectGlobalManifestTag"
- "MSUBootObjectCopierFetchBootObjectRestoreVersionTag"
- "MSUBootObjectCopierFetchBootObjectSystemVersionTag"
- "Medium Type"
- "Model"
- "Model Number"
- "Mount failed"
- "Mounted %@ at %{private}@"
- "Mounted %@, Snapshot( %{private}@ ) at %{private}@"
- "Personalize"
- "Private"
- "Scratch"
- "Solid State"
- "T@\"LPAPFSContainer\",&,N,V_targetContainer"
- "T@\"LPAPFSContainer\",&,N,V_updateContainer"
- "T@\"LPAPFSVolume\",&,N,V_targetVolume"
- "T@\"NSArray\",R"
- "T@\"NSDictionary\",R"
- "TI,V_ioMedia"
- "Timed out waiting for: %@"
- "Unmount failed with EINVAL, will assume race. Ignoring error."
- "Unmounted %@ ( %{private}@ )"
- "User"
- "Vendor Name"
- "Volume is already mounted at %@, attempting to re-mount at %@"
- "Volume is already mounted at %@, skipping re-mount"
- "Was asked asked to unmount (%@) but is not mounted."
- "_Bool iterateSafely(io_iterator_t, int, void (^__strong)(io_object_t), void (^__strong)(void))"
- "_copyIOMediaForDiskWithPath:"
- "_copyLiveFilesystemIOMediaForRootedSnapshot"
- "_createTemporaryMountPointWithError:"
- "_deviceCharacteristicStringForKey:"
- "_ioMedia"
- "_loadMountPointTableForMode:"
- "allAPFSContainers"
- "com.apple.IOKit"
- "componentsSeparatedByString:"
- "content"
- "contentTypeToSubclassMap"
- "contentTypesForPartitionMedia"
- "create snapshot operation failed: %d %s"
- "createSnapshot:error:"
- "eraseVolumeWithError:"
- "failed"
- "failed to create containing directory for symlink %s: %s\n"
- "failed to remove existing symlink %s: %s\n"
- "getBoolPropertyWithName:"
- "getCString:maxLength:encoding:"
- "getPropertyWithName:"
- "getStringPropertyWithName:"
- "hasEmbeddedDeviceTypeRoot"
- "initialize"
- "ioMedia"
- "isCaseSenstive"
- "isEmbeddedDeviceTypeRoot"
- "isEncrypted"
- "isFilevaultEncrypted"
- "isJournaled"
- "isReadOnly"
- "isWhole"
- "libpartition2"
- "mediaForPath:snapshotName:"
- "mediaOfCorrectTypeGivenIOMedia:"
- "mountAtTemporaryPathWithOptions:error:"
- "mount_apfs %@ returned %d, retrying (%d)"
- "mount_apfs returned : %d"
- "nobrowse"
- "parent"
- "physicalStores"
- "pipe failed while preparing to execute %s: %s"
- "populatePairedRecoveryWithVariant:updateBundlePath:buildIdentity:error:"
- "populateSystemRecoveryVolume:fromBuildIdentity:withNSIH:fetchBootObjectBlock:"
- "posix_spawn %s failed: %s"
- "primaryMedia"
- "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
- "q24@?0@8@16"
- "rangeOfString:options:"
- "rdonly"
- "rename snapshot operation failed: %d %s"
- "renameSnapshot:to:error:"
- "revert snapshot operation failed: %d %s"
- "revertToSnapshot:error:"
- "rootToSnapshot:error:"
- "s"
- "setIoMedia:"
- "snapshotMountPoints"
- "snapshotsWithError:"
- "stringWithCString:encoding:"
- "succeeded"
- "supportedContentTypes"
- "symlinking %s -> %s\n"
- "unmountAllWithError:"
- "unmountWithOptions:error:"
- "v12@?0I8"
- "virtual_machine"
- "waitForBlockStorage"
- "waitForIOMediaWithDevNode:"
- "waitpid failed for %s: %s"
- "wholeMediaForMedia"
- "xART"
- "{}"

```
