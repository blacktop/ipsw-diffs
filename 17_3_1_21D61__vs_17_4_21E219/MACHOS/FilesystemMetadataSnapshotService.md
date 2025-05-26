## FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x2cf24
+1003.0.0.0.0
+  __TEXT.__text: 0x2ed28
   __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x1960
-  __TEXT.__objc_methlist: 0x72c
-  __TEXT.__cstring: 0x27f4d
-  __TEXT.__oslogstring: 0x16a5
-  __TEXT.__objc_methname: 0x232d
+  __TEXT.__objc_stubs: 0x1a40
+  __TEXT.__objc_methlist: 0x7a4
+  __TEXT.__cstring: 0x28750
+  __TEXT.__oslogstring: 0x17a4
+  __TEXT.__objc_methname: 0x262b
   __TEXT.__objc_classname: 0x136
   __TEXT.__objc_methtype: 0x564
-  __TEXT.__const: 0xd0
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x2c8
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x3f4
+  __TEXT.__unwind_info: 0x420
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x560
-  __DATA_CONST.__cfstring: 0x1280
+  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__cfstring: 0x1340
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1510
-  __DATA.__objc_selrefs: 0x718
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x100
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0xd8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x1630
+  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_ivar: 0xf0
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x578
-  __DATA.__bss: 0x10e
+  __DATA.__bss: 0x11e
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 457
-  Symbols:   327
-  CStrings:  3532
+  Functions: 495
+  Symbols:   330
+  CStrings:  3616
 
Symbols:
+ _kVolumeDirStatsDataListFilenameKey
+ _kVolumePurgeableRecordsListFilenameKey
+ _kVolumeSharedExtentsListFilenameKey
CStrings:
+ "\"7\x11"
+ "%llu\t%llu\t%llu\t%llu\n"
+ "%llu\t%llu\t%llu\t%u\n"
+ "%s\t%d\n"
+ "%s\t%s\t%s\t%s\n"
+ "1003"
+ "2.7"
+ "APFSIOC_DIR_STATS_OP failed for %s with error %s"
+ "APFSIOC_GET_SHARED_EXTENTS failed for %s with error %s"
+ "APFSIOC_PURGEABLE_GET_BULK_INFO not supported"
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): Cannot add 14 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): (#15) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): Cannot add 15 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrAborts(696) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrFullyDone(699) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrResumeSent(689) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrSkippedBlocks(758) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterDestinations(721) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterWrites(722) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): Cannot add 14 elements to context"
+ "Attrlist failed with error (%s) (%s)"
+ "DirStatsDataFilename"
+ "Failed to get hashed path for %s (isDir: 1)"
+ "Failed to get hashed path for %s (isDir: 1)\n"
+ "GCReadSequential"
+ "GCReadSequential_"
+ "Inode-Number"
+ "Last-Access-Time"
+ "Owning-Obj-Id"
+ "Physical-Block-Number"
+ "Purgeable-Flags"
+ "Purgeable-Size"
+ "PurgeableRecordsFilename"
+ "Reference-Count"
+ "SAFDirStats"
+ "SharedExtentsFilename"
+ "Size"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,V_safeFilenameForDirStatsDataListing"
+ "T@\"NSString\",R,V_safeFilenameForPurgeableRecordsListing"
+ "T@\"NSString\",R,V_safeFilenameForSharedExtentsListing"
+ "TB,R,V_shouldCollectDirStatsData"
+ "TB,R,V_supportsPurgeableRecords"
+ "TB,R,V_supportsSharedExtents"
+ "__checkDirStatsDataCapabilityForVolume:"
+ "_getDirStatsType:reply:"
+ "_getPurgeableRecordsInfo:reply:"
+ "_getSharedExtensInfo:reply:"
+ "_safeFilenameForDirStatsDataListing"
+ "_safeFilenameForPurgeableRecordsListing"
+ "_safeFilenameForSharedExtentsListing"
+ "_shouldCollectDirStatsData"
+ "_supportsPurgeableRecords"
+ "_supportsSharedExtents"
+ "bandsAgeBinsReadSectors"
+ "bandsAgeBinsReadSectors_"
+ "bandsAgeBinsSnapshot"
+ "bandsAgeBinsSnapshot_"
+ "bandsAgeBinsV2"
+ "bandsAgeBinsV2_"
+ "can't malloc %llu bytes"
+ "cbdrAborts"
+ "cbdrFullyDone"
+ "cbdrResumeSent"
+ "cbdrSkippedBlocks"
+ "dirstatsdatalisting"
+ "gcPDusterDestinations"
+ "gcPDusterWrites"
+ "gcwamp"
+ "gcwamp_"
+ "hostReadSequential"
+ "hostReadSequential_"
+ "purgeablerecordslisting"
+ "safeFilenameForDirStatsDataListing"
+ "safeFilenameForPurgeableRecordsListing"
+ "safeFilenameForSharedExtentsListing"
+ "sharedextentslisting"
+ "shouldCollectDirStatsData"
+ "supportsPurgeableRecords"
+ "supportsSharedExtents"
+ "v24@?0@\"NSString\"8B16B20"
+ "v36@?0Q8Q16Q24I32"
+ "v40@?0Q8Q16Q24Q32"
+ "\xe1"
- "\x124\x11"
- "2.3"
- "62"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): (#10) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): Cannot add 10 elements to context"
- "fwaHistogram"
- "fwaHistogram_"
- "\xa1"

```
