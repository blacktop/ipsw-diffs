## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Versions/A/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/Contents/MacOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2171.101.1.0.0
-  __TEXT.__text: 0xa24dc
+2171.120.23.501.1
+  __TEXT.__text: 0xa26fc
   __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_stubs: 0x4a80
-  __TEXT.__objc_methlist: 0x1d7c
-  __TEXT.__cstring: 0x18c95
+  __TEXT.__objc_stubs: 0x4b60
+  __TEXT.__objc_methlist: 0x1d94
+  __TEXT.__cstring: 0x18d6b
   __TEXT.__const: 0x77b40
   __TEXT.__oslogstring: 0x19fe
   __TEXT.__objc_classname: 0x273
   __TEXT.__gcc_except_tab: 0x4c0
-  __TEXT.__objc_methname: 0x511a
+  __TEXT.__objc_methname: 0x51bb
   __TEXT.__objc_methtype: 0xfdb
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x12b8
+  __TEXT.__unwind_info: 0x12c0
   __TEXT.__eh_frame: 0x318
   __DATA_CONST.__auth_got: 0xd88
-  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x70
   __DATA_CONST.__const: 0x2ac8
-  __DATA_CONST.__cfstring: 0xc4e0
+  __DATA_CONST.__cfstring: 0xc580
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA.__objc_const: 0x26e8
-  __DATA.__objc_selrefs: 0x16d8
+  __DATA.__objc_selrefs: 0x1710
   __DATA.__objc_ivar: 0x1b4
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x560

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 1846
-  Symbols:   8894
-  CStrings:  4426
+  Functions: 1849
+  Symbols:   8917
+  CStrings:  4438
 
Symbols:
+ -[MSUTargetController targetVolumeIsRoot]
+ -[MSUTargetController volumeIsRoot:]
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUBootObjectCopier.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libbless2.a(bless2.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libbless2.a(log.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libBuildInfo.a(BIDeviceInformation.o)
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUApplicationManager.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUAssetStager.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUFreeSpaceManager.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUResultState.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUSFRTargetController.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUTargetController.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/NeRDSPI.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/boot_policy_support.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_handlers.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_service.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/clientServerIPC.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-21eb89572409f4f5ee695d65cb051d7f.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-3b69fe07e8e9325dc0823d0aa24d810a.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/log.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_log.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_nvram.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/restore_log.o
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/BuildInfo/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/CleanupPreparePathService/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUAssetStager/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
+ /AppleInternal/Library/BuildRoots/085b443a-0b9f-11f0-a561-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/UpdateMetrics/UpdateMetrics/
+ /AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/libusbrestore/
+ /AppleInternal/Library/BuildRoots/16a97422-050f-11f0-bd0c-122ba06eff56/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/ramrod/
+ /AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/bless_libraries/bless2/libbless2/
+ /AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ramrod/MSUBootFirmwareUpdater/
+ /AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/
+ /AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/macOS/
+ /AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ramrod/restored/AsyncCheckpoint/
+ MSUCleanupPreboot.cold.1
+ _OBJC_CLASS_$_NSBundle
+ __block_literal_global.94
+ __block_literal_global.96
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$_initUniqueWithURL:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$operatingSystemVersion
+ _objc_msgSend$targetVolumeIsRoot
+ _objc_msgSend$volumeIsRoot:
- /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/libusbrestore/
- /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/PurpleRestore_libpartition/ramrod/
- /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/bless_libraries/bless2/libbless2/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUBootObjectCopier.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libbless2.a(bless2.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libbless2.a(log.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/Symbols/BuiltProducts/libBuildInfo.a(BIDeviceInformation.o)
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUApplicationManager.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUAssetStager.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUFreeSpaceManager.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSULogAnnotatedSum.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUResultState.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUSFRTargetController.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MSUTargetController.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdateConstants.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/MobileSoftwareUpdatePreferences.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/NeRDSPI.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/boot_policy_support.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_handlers.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/cleanup_prepare_path_service.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/clientServerIPC.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-21eb89572409f4f5ee695d65cb051d7f.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-3b69fe07e8e9325dc0823d0aa24d810a.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/log.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_log.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/msu_nvram.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/restore_log.o
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/BuildInfo/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/CleanupPreparePathService/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUAssetStager/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate/UpdateBrainService/MSUBrain/
- /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/UpdateMetrics/UpdateMetrics/
- /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/MSUBootFirmwareUpdater/
- /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/
- /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/ramrod/macOS/
- /AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/ramrod/restored/AsyncCheckpoint/
- __block_literal_global.68
- __block_literal_global.70
CStrings:
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBasicStreams.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBuffers.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPool.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyBaseSystemPatch.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyPatches.c"
+ "/System/Volumes/Preboot/Cryptexes/App/System/Applications/Safari.app"
+ "Failed to remove downlevel from %@: %@\n"
+ "Found mismatched Safari downlevel (%@ != %ld.*) at %@\n"
+ "LSMinimumSystemVersion"
+ "Removed downlevel from %@\n"
+ "URLByAppendingPathComponent:isDirectory:"
+ "_initUniqueWithURL:"
+ "fileURLWithPath:isDirectory:"
+ "infoDictionary"
+ "operatingSystemVersion"
+ "targetVolumeIsRoot"
+ "volumeIsRoot:"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBasicStreams.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBuffers.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPool.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyBaseSystemPatch.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyImagePatch.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelPatch/MSU/ApplyPatches.c"

```
