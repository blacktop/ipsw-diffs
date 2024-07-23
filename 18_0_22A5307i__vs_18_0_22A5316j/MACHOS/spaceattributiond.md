## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x30bdc
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x4ee0
-  __TEXT.__objc_methlist: 0x1fe0
-  __TEXT.__const: 0x1a0
-  __TEXT.__gcc_except_tab: 0x193c
-  __TEXT.__oslogstring: 0x3cdf
-  __TEXT.__cstring: 0x2725
-  __TEXT.__objc_methname: 0x59c5
-  __TEXT.__objc_classname: 0x2d8
-  __TEXT.__objc_methtype: 0xe00
-  __TEXT.__unwind_info: 0xad0
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x1b8
+317.0.0.0.0
+  __TEXT.__text: 0x31be4
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x5260
+  __TEXT.__objc_methlist: 0x21b8
+  __TEXT.__const: 0x1b0
+  __TEXT.__gcc_except_tab: 0x18b8
+  __TEXT.__oslogstring: 0x3ee7
+  __TEXT.__cstring: 0x25b0
+  __TEXT.__objc_methname: 0x5e94
+  __TEXT.__objc_classname: 0x2ec
+  __TEXT.__objc_methtype: 0xe42
+  __TEXT.__unwind_info: 0xb28
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0xf40
-  __DATA_CONST.__cfstring: 0x2200
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__cfstring: 0x20c0
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __DATA_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x200
+  __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_intobj: 0x510
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3a28
-  __DATA.__objc_selrefs: 0x1888
-  __DATA.__objc_ivar: 0x248
-  __DATA.__objc_data: 0xc30
+  __DATA.__objc_const: 0x3d38
+  __DATA.__objc_selrefs: 0x1960
+  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_data: 0xc80
   __DATA.__data: 0x248
   __DATA.__bss: 0x1d8
-  __DATA.__common: 0x1
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution
-  - /System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1055
-  Symbols:   215
-  CStrings:  2017
+  Functions: 1093
+  Symbols:   212
+  CStrings:  2071
 
Symbols:
- _OBJC_CLASS_$_ICQCloudStorageDataController
- _OBJC_CLASS_$_ICQCloudStorageSummary
- _getopt
CStrings:
+ "\x17\x12"
+ "\"5d"
+ "%!s(MISSING) failed to find bundleSet for dirKey %!l(MISSING)lu in the dirKeyCache"
+ "%!s(MISSING): Volume (%!@(MISSING)) doesn't support clone mapping"
+ "%!s(MISSING): Volume (%!@(MISSING)) doesn't support tagging"
+ "+[SAHelper isSAFSupported]"
+ "+[SAPurgeableRecords processAttributionTagsPurgeableWithReply:]"
+ "-[SAPurgeableRecords asyncStartProcessingSUPurgeableUrgencyFilesUsingPathList:andDirKeyCacheList:]_block_invoke"
+ "-[SAVolumeScanner updateAppSizerResultsWithSUPurgeableUrgencySizes]_block_invoke"
+ "@\"NSDictionary\""
+ "@\"SAActivity\""
+ "@\"SAPurgeableRecords\""
+ "Adding %!l(MISSING)lu to %!@(MISSING)"
+ "Calling Handlers with intermittent results"
+ "End: App Sizer SU Purgeable Processing"
+ "Failed to get the dirStats ID for path %!@(MISSING) with error %!s(MISSING)"
+ "Failed to get the purgeable records for volume %!@(MISSING) with error %!s(MISSING)"
+ "Failed to get volume (%!@(MISSING)) attribution tag capability"
+ "Failed to get volume (%!@(MISSING)) clone mapping capability"
+ "Q32@0:8@16Q24"
+ "SAPurgeableRecords"
+ "START: App Sizer Calculate DiskUsed And diskCapacity"
+ "START: App Sizer Check For Sizes OverFlow"
+ "START: App Sizer SU Purgeable Processing"
+ "SUPurgeableUrgencyData"
+ "Space Attribution Framework is NOT supported"
+ "T@\"NSDictionary\",&,V_SUPurgeableUrgencyData"
+ "T@\"NSMutableDictionary\",&,V_dirKeyCacheList"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"SAActivity\",&,V_activity"
+ "T@\"SAPurgeableRecords\",&,V_purgeableRecords"
+ "TQ,V_dataVolumeSizeUsed"
+ "TQ,V_softwareUpdateVolumeUsedSpace"
+ "TQ,V_systemVolumeUsedSpace"
+ "TQ,V_totalHiddenAppSize"
+ "TQ,V_totalPurgeableDataSize"
+ "TQ,V_totalVisibleAppSize"
+ "Total SU purgeable urgency size for %!@(MISSING) is %!l(MISSING)lu"
+ "_SUPurgeableUrgencyData"
+ "_dataVolumeSizeUsed"
+ "_dirKeyCacheList"
+ "_purgeableRecords"
+ "_queue"
+ "_softwareUpdateVolumeUsedSpace"
+ "_systemVolumeUsedSpace"
+ "_totalHiddenAppSize"
+ "_totalPurgeableDataSize"
+ "_totalVisibleAppSize"
+ "accountSUPurgeableFor:purgeableSize:"
+ "asyncStartProcessingSUPurgeableUrgencyFilesUsingPathList:andDirKeyCacheList:"
+ "calculateDiskUsedAndCapacity"
+ "calculateSystemDataSize"
+ "can't find saf dir for dir-key %!l(MISSING)lu file path %!@(MISSING)"
+ "checkForSizesOverflow"
+ "com.apple.MobileAsset.SystemEnvironmentAsset"
+ "dataVolumeSizeUsed"
+ "dirKeyCacheList"
+ "getFSPurgeableOnVolume:purgeableUrgency:"
+ "initWithActivity:"
+ "isSAFSupported"
+ "newWithActivity:"
+ "processAttributionTagsPurgeableWithReply:"
+ "purgeableRecords"
+ "queue"
+ "setDataVolumeSizeUsed:"
+ "setDirKeyCacheList:"
+ "setPurgeableRecords:"
+ "setQueue:"
+ "setSUPurgeableUrgencyData:"
+ "setSoftwareUpdateVolumeUsedSpace:"
+ "setSystemVolumeUsedSpace:"
+ "setTotalHiddenAppSize:"
+ "setTotalPurgeableDataSize:"
+ "setTotalVisibleAppSize:"
+ "softwareUpdateVolumeUsedSpace"
+ "systemVolumeUsedSpace"
+ "totalHiddenAppSize"
+ "totalPurgeableDataSize"
+ "totalVisibleAppSize"
+ "updateAppSet:withSUPurgeableSize:"
+ "updateAppSizerResultsWithSUPurgeableUrgencySizes"
+ "volumeSupportsAttributionTags:"
+ "volumeSupportsCloneMapping:"
+ "waitForProcessingSUPurgeableUrgencyFiles"
- "\x18\x12"
- "\"5"
- "%!@(MISSING) Clone Map dataSize: %!l(MISSING)lu < 0"
- "%!@(MISSING): Path (%!@(MISSING)) dir-stat cloneSize %!l(MISSING)ld > physicalSize: %!l(MISSING)ld"
- "%!@(MISSING): Path (%!@(MISSING)) dir-stat purgeableSize %!l(MISSING)ld > physicalSize: %!l(MISSING)ld"
- "%!@(MISSING): dataSize: %!l(MISSING)lu > purgeableSize: %!l(MISSING)lu by %!l(MISSING)u% with iCloud plan available: %!l(MISSING)lu GB"
- "%!@(MISSING): dataSize: %!l(MISSING)lu is greater than purgeableSize: %!l(MISSING)lu by %!l(MISSING)u% with iCloud plan available: %!l(MISSING)lu"
- "+[SAAttributionTag processAttributionTagsPurgeableForVol:withReply:]"
- "Available iCloud storage: %!@(MISSING)"
- "Bundle set %!@(MISSING) dataSize (%!l(MISSING)lu) overflowed"
- "Bundle set %!@(MISSING) fixedSize (%!l(MISSING)lu) overflowed"
- "Group %!@(MISSING) cacheSize: %!l(MISSING)lu > existing dataSize: %!l(MISSING)lu"
- "No ACAccount and ICQCloudStorage classes implemented."
- "T@\"NSNumber\",&,V_icloudPlanAvailable"
- "Timed out waiting for iCloud storage information."
- "_icloudPlanAvailable"
- "attributionTag %!l(MISSING)lu for bundleID %!@(MISSING) phySize: %!l(MISSING)lu < cloneSize: %!l(MISSING)lu"
- "checkPhotosPurgeableSizeAndSendTTR:"
- "com.apple.fakeapp.Environments"
- "fetchStorageSummaryWithCompletion:"
- "freeStorage"
- "getiCloudPlanAvailable"
- "icloudPlanAvailable"
- "initWithAccount:"
- "processAttributionTagsPurgeableForVol:withReply:"
- "setIcloudPlanAvailable:"
- "v24@?0@\"ICQCloudStorageSummary\"8@\"NSError\"16"

```
