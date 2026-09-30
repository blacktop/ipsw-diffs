## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-2082.0.43.0.1
-  __TEXT.__text: 0x33da4
+2082.40.21.0.0
+  __TEXT.__text: 0x341e4
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x3e40
-  __TEXT.__objc_methlist: 0x1958
-  __TEXT.__cstring: 0x10c90
+  __TEXT.__objc_stubs: 0x3e60
+  __TEXT.__objc_methlist: 0x1968
+  __TEXT.__cstring: 0x10fda
   __TEXT.__const: 0x134c
   __TEXT.__oslogstring: 0x13c8
   __TEXT.__gcc_except_tab: 0x4a8
   __TEXT.__objc_classname: 0x219
-  __TEXT.__objc_methname: 0x41be
-  __TEXT.__objc_methtype: 0xe41
-  __TEXT.__unwind_info: 0xa18
+  __TEXT.__objc_methname: 0x41e5
+  __TEXT.__objc_methtype: 0xe44
+  __TEXT.__unwind_info: 0xa28
   __DATA_CONST.__auth_got: 0xc30
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1838
-  __DATA_CONST.__cfstring: 0xa3c0
+  __DATA_CONST.__const: 0x1860
+  __DATA_CONST.__cfstring: 0xa540
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x2608
-  __DATA.__objc_selrefs: 0x12d8
+  __DATA.__objc_selrefs: 0x12e0
   __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x588
-  __DATA.__bss: 0x698
+  __DATA.__bss: 0x6a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 849
-  Symbols:   6340
-  CStrings:  3156
+  Functions: 854
+  Symbols:   6374
+  CStrings:  3169
 
Symbols:
+ +[MSUAssetStager _isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:purging:]
+ +[MSUAssetStager _isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:purging:]
+ +[MSUAssetStager _preSUStagingSupportedInSUCore]
+ +[MSUAssetStager _preSUStagingSupportedInSUCore]
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
+ /AppleInternal/Library/BuildRoots/ee1dacb9-54bf-11ef-bbd7-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
+ __MSUPreferencesCopyValueForDomain
+ __MSUPreferencesCopyValueForDomain
+ __MSUPreferencesGetAppBooleanValue
+ __MSUPreferencesGetAppBooleanValue
+ __MSUPreferencesGetAppBooleanValueWithDefaultValue
+ __MSUPreferencesGetAppBooleanValueWithDefaultValue
+ ____getManagedPreferencesDict_block_invoke
+ ____getManagedPreferencesDict_block_invoke
+ _getManagedPreferencesDict._managedPreferencesCache
+ _getManagedPreferencesDict._managedPreferencesCache
+ _getManagedPreferencesDict.managedPreferencesOnce
+ _getManagedPreferencesDict.managedPreferencesOnce
+ _kMobileSoftwareUpdateDisablePreSoftwareUpdateAssetStagingKey
+ _kMobileSoftwareUpdateDisablePreSoftwareUpdateAssetStagingKey
+ _objc_msgSend$_isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:purging:
+ _objc_msgSend$_preSUStagingSupportedInSUCore
- +[MSUAssetStager _isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:]
- +[MSUAssetStager _isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:]
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(PCIeNANDBootWriter.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncBlockContext.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(MSUCheckpointAsyncContext.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_checkpoint.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_nvram.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSContainer_Private.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhyscialStore_Private.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSPhysicalStore.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPAPFSVolume_Private.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPIOKitHelper.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPLog.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPMedia.o)
- /AppleInternal/Library/BuildRoots/8704f048-4298-11ef-91ae-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libpartition2.a(LPPartitionMedia.o)
- _objc_msgSend$_isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:
CStrings:
+ "%!@(MISSING)/%!@(MISSING).plist"
+ "/Library/Managed Preferences/mobile"
+ "B52@0:8B16@20@28B36B40B44B48"
+ "MSUAssetStager: Only purging is enabled\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging disabled via on-device default; skipping staging\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is disabled for sfr updates\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is disabled for splat updates\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is disabled via asset attributes\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is not enabled running in limited environments\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is only enabled for snapshot based updates\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging is supported in SUCore\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging passed environment pre-checks\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging requires a build version\n"
+ "MSUAssetStager: Pre-SoftwareUpdate Asset Staging requires an os version\n"
+ "_isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:purging:"
+ "_preSUStagingSupportedInSUCore"
- "B48@0:8B16@20@28B36B40B44"
- "MSUAssetStager: Staging support in SUCore; not staging from the update brain\n"
- "_isEnabledWithAdditionalIndicators:options:updateAttributes:snapshotPrepare:splat:sfr:"

```
