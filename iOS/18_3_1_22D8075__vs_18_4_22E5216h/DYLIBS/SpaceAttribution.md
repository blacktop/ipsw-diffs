## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-322.80.5.0.1
-  __TEXT.__text: 0x114b0
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x1088
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x674
-  __TEXT.__cstring: 0xe11
-  __TEXT.__oslogstring: 0xfab
-  __TEXT.__unwind_info: 0x588
-  __TEXT.__objc_classname: 0x170
-  __TEXT.__objc_methname: 0x2a37
-  __TEXT.__objc_methtype: 0x804
-  __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0x120
+322.100.56.0.1
+  __TEXT.__text: 0xf100
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x1138
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0xd78
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__oslogstring: 0xa1d
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__objc_classname: 0x162
+  __TEXT.__objc_methname: 0x2882
+  __TEXT.__objc_methtype: 0x6ce
+  __TEXT.__objc_stubs: 0x1aa0
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x400
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xf20
-  __AUTH_CONST.__objc_const: 0x1ee0
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x110
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0x180
-  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
   - /System/Library/PrivateFrameworks/StorageKit.framework/StorageKit
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 506
-  Symbols:   671
-  CStrings:  888
+  Functions: 455
+  Symbols:   604
+  CStrings:  831
 
Symbols:
+ _OBJC_CLASS_$_SABGSystemTask
+ _OBJC_METACLASS_$_SABGSystemTask
+ _dispatch_async
- _MGCopyAnswer
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_SAActivity
- _OBJC_METACLASS_$_SAActivity
- _free
- _fsctl
- _fsgetpath
- _getmntinfo_r_np
- _gettimeofday
- _objc_copyStruct
- _objc_retainBlock
- _stat
- _strerror
CStrings:
+ "\x02Kq\""
+ "%s: Volume %@, %@ %@"
+ "%s: supplied array in nil"
+ "@\"BGSystemTask\""
+ "@\"SAAppSize\""
+ "Failed to split array (count: %ld) to %d parts. Bailing out"
+ "RawDiskedUsed"
+ "RawSystemDataSize"
+ "SABGSystemTask"
+ "T@\"BGSystemTask\",&,V_task"
+ "T@\"SAAppSize\",R,V_systemApp"
+ "T@\"SAAppSize\",R,V_systemDataApp"
+ "TB,R,V_shouldDefer"
+ "TQ,V_rawDiskedUsed"
+ "TQ,V_totalCDAppsCacheSize"
+ "TQ,V_totalCDPluginsSize"
+ "TQ,V_totalPurgeableDataSize"
+ "TQ,V_totalSAFAppsCacheSize"
+ "TQ,V_totalSAFPluginsSize"
+ "TotalCDAppsCacheSize"
+ "TotalCDPluginsSize"
+ "TotalPurgeableDataSize"
+ "TotalSAFAppsCacheSize"
+ "TotalSAFPluginsSize"
+ "Tq,V_rawSystemDataSize"
+ "Unable to get %@, purgeable size is set to 0: %@"
+ "_rawDiskedUsed"
+ "_rawSystemDataSize"
+ "_shouldDefer"
+ "_systemApp"
+ "_systemDataApp"
+ "_task"
+ "_totalCDAppsCacheSize"
+ "_totalCDPluginsSize"
+ "_totalPurgeableDataSize"
+ "_totalSAFAppsCacheSize"
+ "_totalSAFPluginsSize"
+ "adjustDenomAgeBy:reply:"
+ "collectPathSizeInfo:info:"
+ "deferTask"
+ "getPhySizeForAppSet:"
+ "initWithBGTask:"
+ "newWithBGTask:"
+ "numberWithLongLong:"
+ "processArrayConcurrently:number:queue:group:block:"
+ "rawDiskedUsed"
+ "rawSystemDataSize"
+ "setForceSDAAbort:"
+ "setRawDiskedUsed:"
+ "setRawSystemDataSize:"
+ "setTask:"
+ "setTotalCDAppsCacheSize:"
+ "setTotalCDPluginsSize:"
+ "setTotalPurgeableDataSize:"
+ "setTotalSAFAppsCacheSize:"
+ "setTotalSAFPluginsSize:"
+ "systemApp"
+ "systemDataApp"
+ "task"
+ "totalCDAppsCacheSize"
+ "totalCDPluginsSize"
+ "totalPurgeableDataSize"
+ "totalSAFAppsCacheSize"
+ "totalSAFPluginsSize"
+ "v52@0:8@16i24@28@36@?44"
- "%@: Failed to get FSPurgeable data of urgency (%llu) with error: %s"
- "%s: Can't get volume size for %s (err %li)"
- "%s: Failed to get path (%s) mount point with error %d (%s)"
- "%s: Failed to resolve path (%s) with error %d (%s)"
- "%s: Invalid VOL_CAP_FMT_CLONE_MAPPING flag for volume %@"
- "%s: Invalid VOL_CAP_INT_ATTRIBUTION_TAG flag for volume %@"
- "%s: Volume %@, CACHE_DELETE_TOTAL_AVAILABLE %@"
- "%s: statfs failed for %@ with error %s"
- "%s:%s:used:%llu:reserved:%llu:capacity:%llu"
- "'System' not found, creating"
- "+[SASupport getResolvedURL:]"
- "+[SASupport getURLMountPoint:]"
- "+[SASupport getVolSizeFromAttrList:completionHandler:]"
- "+[SASupport isItemMountedOnSystemVolume:]"
- "+[SASupport volumeSupportsAttributionTags:]"
- "+[SASupport volumeSupportsCloneMapping:]"
- "@\"NSBackgroundActivityScheduler\""
- "@32@0:8@16@?24"
- "@32@0:8Q16^{fsid=[2i]}24"
- "@32@0:8Q16^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}24"
- "APFSIOC_DIR_STATS_OP : DIR_STATS_OP_SET failed for %s : %s"
- "APFSIOC_DIR_STATS_OP: DIR_STATS_OP_GET failed for %@ : %s"
- "APFSIOC_GET_VOLUME_ROLE returned with error: %s"
- "APFS_PURGEABLE_HIGH_URGENCY"
- "APFS_PURGEABLE_LOW_URGENCY"
- "APFS_PURGEABLE_MED_URGENCY"
- "APFS_PURGEABLE_SU_URGENCY"
- "Adding for %@ - data size: %llu, fixed size: %llu"
- "B24@0:8r*16"
- "DeviceName"
- "DirStatForOriginID: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "END: App Sizer %@ (%lf)"
- "END: Unknown phase %@"
- "Enabled APFSIOC_DIR_STATS_OP for %s with flags 0x%llx"
- "Failed to get volume (%@) attribution tag capability"
- "Failed to get volume (%@) clone mapping capability"
- "Failed to stat path %@"
- "HomePod"
- "INodeForDirStatKey: APFSIOC_DIR_STATS_OP for %llu returned errno %u"
- "K#"
- "NO_RESPECT_0_SIZE"
- "Q32@0:8Q16*24"
- "Q36@0:8@16Q24B32"
- "RESPECT_0_SIZE"
- "SAActivity"
- "SASupport"
- "SATimeVal"
- "START: App Sizer %@"
- "T@\"NSBackgroundActivityScheduler\",&,V_activity"
- "T@?,C,V_completionHandler"
- "TB,V_deferActivity"
- "TB,V_shouldStop"
- "T{timeval=qi},V_timeVal"
- "Unable to get CACHE_DELETE_TOTAL_AVAILABLE, purgeable size is set to 0: %@"
- "^{timeval=qi}16@0:8"
- "_activity"
- "_completionHandler"
- "_deferActivity"
- "_shouldStop"
- "_timeVal"
- "activity"
- "addSystemVolumeWithCapacity:used:withReplyBlock:"
- "completionHandler"
- "deferActivity"
- "dir-stat for %@ (attributes 0x%llx) does not count clones and purgeables."
- "dir-stat for %@ (flags 0x%llx) is not in saf mode."
- "dir-stats for %@ does not have hierarchy on (0x%llx)."
- "dir-stats for %@ is possibly inconsistent."
- "enableDirStatInfoForPath:withOptions:andGetInfo:"
- "enableDirStatsForPath:withOptions:"
- "fileURLWithPath:isDirectory:"
- "fsctl APFSIOC_GET_CLONE_INFO failed with error: %s"
- "fsctl APFSIOC_GET_PURGEABLE_FILE_FLAGS failed with error: %s"
- "fsgetpath returned errno %d for nodeID %llu"
- "getCloneDstreamIDForPath:"
- "getDirStatInfoForPath:withOptions:info:"
- "getDirStatKeyForOriginID:ofMount:"
- "getEnterpriseVolumesPaths"
- "getFSPurgeableDataOnVolumes:"
- "getFSPurgeableOnVolume:purgeableUrgency:respectZeroSizeFiles:"
- "getINodeForDirStatKey:ofMount:"
- "getInodeIDForPath:"
- "getLSAppRecordForBundle:reply:"
- "getPathOfNodeID:FSid:"
- "getPathOfiNode:inVolume:"
- "getResolvedURL:"
- "getTimeValAddr"
- "getURLMountPoint:"
- "getVolSizeFromAttrList:completionHandler:"
- "getVolumesPaths"
- "i32@0:8@16q24"
- "i40@0:8@16q24^{?=QQQQ}32"
- "initWithActivity:completionHandler:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "intValue"
- "isEqualToString:"
- "isFileCloned:"
- "isFilePurgeable:"
- "isItemMountedOnSystemVolume:"
- "markTimeEndForPhase:"
- "markTimeStartForPhase:"
- "mtrAoWJ3gsq+I90ZnQ0vQw"
- "newWithActivity:andCompletionHandler:"
- "runFullScan:"
- "setActivity:"
- "setActivityResult:"
- "setCompletionHandler:"
- "setDeferActivity:"
- "setDiskUsed:andCapacity:"
- "setShouldStop:"
- "setTimeVal:"
- "shouldStop"
- "stringWithCString:encoding:"
- "stringWithUTF8String:"
- "targetDeviceIsHomePod"
- "targetDeviceIsIpad"
- "targetDeviceIsWatch"
- "timeVal"
- "unable to get mounts: %s (%d)\n"
- "v32@0:8Q16Q24"
- "v32@0:8r*16@?24"
- "v32@0:8{timeval=qi}16"
- "v40@0:8Q16Q24@?32"
- "valueForKey:"
- "volumeSupportsAttributionTags:"
- "volumeSupportsCloneMapping:"
- "{timeval=\"tv_sec\"q\"tv_usec\"i}"
- "{timeval=qi}16@0:8"

```
