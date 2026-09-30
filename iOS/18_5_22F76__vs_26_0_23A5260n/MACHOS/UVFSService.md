## UVFSService

> `/System/Library/PrivateFrameworks/UVFSXPCService.framework/XPCServices/UVFSService.xpc/UVFSService`

```diff

-716.120.2.0.0
-  __TEXT.__text: 0x23dc4
+741.0.0.0.0
+  __TEXT.__text: 0x2393c
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x1560
-  __TEXT.__cstring: 0x1180
-  __TEXT.__objc_classname: 0x1eb
-  __TEXT.__objc_methname: 0x40d8
-  __TEXT.__objc_methtype: 0x14d2
-  __TEXT.__oslogstring: 0x3f6b
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x950
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__objc_stubs: 0x2fe0
+  __TEXT.__objc_methlist: 0x1580
+  __TEXT.__cstring: 0x11b7
+  __TEXT.__objc_classname: 0x1e9
+  __TEXT.__objc_methname: 0x410a
+  __TEXT.__objc_methtype: 0x14f4
+  __TEXT.__oslogstring: 0x3e4a
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x8bc
+  __TEXT.__unwind_info: 0x580
   __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x740
-  __DATA_CONST.__cfstring: 0xc20
+  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x23c8
-  __DATA.__objc_selrefs: 0x1020
+  __DATA.__objc_selrefs: 0x1028
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x278

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50C6108B-FC6A-35C2-8841-07E2823CCF42
-  Functions: 738
+  UUID: ED2F2FF0-F3A5-3B8A-8DEE-9FD4999C6317
+  Functions: 746
   Symbols:   287
-  CStrings:  1552
+  CStrings:  1535
 
CStrings:
+ "%s: failed to getNodeForFH %s %d"
+ "%s: file handle mismatch: %@ != %@: ENOENT"
+ "%s: name mismatch: %@ != %@: ENOENT"
+ "%s: silence the ENOENT error"
+ "%s:CHECK_AND_REPAIR:failed:%@"
+ "%s:CHECK_AND_REPAIR:pass:%@"
+ "%s:CHECK_AND_REPAIR:start:%@"
+ "%s:FSmount:failed"
+ "%s:QUICK_CHECK:ENOTSUP:%@"
+ "%s:QUICK_CHECK:failed:%@"
+ "%s:QUICK_CHECK:pass:%@"
+ "%s:QUICK_CHECK:start:%@"
+ "-[LIFSPreVolume checkVolumeWithCreds:]"
+ "-[LIFSPreVolume mountVolumeWithCreds:resultRootNode:]"
+ "-[UVFSAnalytics addVolumeProperties:volumeCount:loadStatus:loadErrorReason:]"
+ "-[userFSVolume otherAttributeOf:named:requestID:reply:]"
+ "-[userFSVolume removeItem:from:named:usingFlags:requestID:reply:]"
+ "LISetXattr: empty finder info: got ENOATTR from setXAttr: silence the error"
+ "LISetXattr:LIXattrHowRemove:appledouble:enoent:return:ENOATTR"
+ "LISetXattr:LIXattrHowRemove:appledouble:enoent:setEmptyFinderInfo:return:0"
+ "LISetXattr[ad]: empty finder info: got ENOATTR from removeXattrNamed: silence the error"
+ "TB,V_useMetadataBuf"
+ "Volume analytics of %@:\n  Count: %d\n  LoadStatus: %@\n  LoadErrorReason: %@\n  Disk analytics:\n    Type: %@\n    Size: %lu\n    BlockSize: %lu\n    Partition Table Type: %@\n    Partitions (%lu):\n"
+ "_useMetadataBuf"
+ "addVolumeProperties:volumeCount:loadStatus:loadErrorReason:"
+ "checkVolumeWithCreds:"
+ "com.apple.FinderInfo"
+ "errorForCheckOrMountReturnValue:"
+ "forceUpdateLinkCount"
+ "getVolumeFromDevice:mountVolumeWithCreds:EAUTH"
+ "getVolumeFromDevice:mountVolumeWithCreds:error:skipping"
+ "getVolumeFromDevice:mountVolumeWithCreds:fsck:error:skipping"
+ "i24@0:8^{_UVFSVolumeCredential=*I}16"
+ "isNodeReclaimable"
+ "mountVolumeWithCreds:resultRootNode:"
+ "otherAttributeOf:named:reply:"
+ "setUseMetadataBuf:"
+ "useMetadataBuf"
+ "v40@0:8@16i24i28@32"
- "\""
- "-[UVFSAnalytics addVolumeProperties:volumeCount:isDCIM:loadStatus:loadErrorReason:]"
- "/System/Library/Frameworks/ImageCaptureCore.framework/DeviceMatchingInfo.plist"
- "DCIM"
- "ExFATCameraDeviceManager"
- "LISetXattr:LIXattrHowRemove:appledouble:enoent:return:0"
- "TB,V_isDCIM"
- "Volume analytics of %@:\n  Count: %d\n  isDcim: %d\n  LoadStatus: %@\n  LoadErrorReason: %@\n  Disk analytics:\n    Type: %@\n    Size: %lu\n    BlockSize: %lu\n    Partition Table Type: %@\n    Partitions (%lu):\n"
- "_S_f_type"
- "_isDCIM"
- "addVolumeProperties:volumeCount:isDCIM:loadStatus:loadErrorReason:"
- "arrayWithObject:"
- "cameraClasses"
- "checkAndMountVolumeWithCreds:resultRootNode:"
- "errorForCheckAndMountReturnValue:"
- "fat"
- "getVolumeFromDevice:CHECK_AND_REPAIR:failed:%@"
- "getVolumeFromDevice:CHECK_AND_REPAIR:pass:%@"
- "getVolumeFromDevice:CHECK_AND_REPAIR:start:%@"
- "getVolumeFromDevice:FSmount:failed"
- "getVolumeFromDevice:QUICK_CHECK:ENOTSUP:%@"
- "getVolumeFromDevice:QUICK_CHECK:failed:%@"
- "getVolumeFromDevice:QUICK_CHECK:pass:%@"
- "getVolumeFromDevice:QUICK_CHECK:start:%@"
- "getVolumeFromDevice:checkAndMountVolumeWithCreds:EAUTH"
- "getVolumeFromDevice:checkAndMountVolumeWithCreds:error:skipping"
- "getVolumeFromDevice:checkAndMountVolumeWithCreds:fsck:error:skipping"
- "initWithContentsOfFile:"
- "isDCIM"
- "isDCIM: !! MISSING !! %@"
- "isDCIM: Got following paths: %@"
- "isDCIM: LIGetFSAttr(): Got result %d, with value: %p, fsClass: %@"
- "isDCIM: LIGetFSAttr(): returning NO"
- "isDCIM: LILookup result: %d"
- "isDCIM: LILookup(%@)"
- "isDCIM: Photos does not support: %s"
- "isDCIM: found the name, but type is wrong, setting ENOENT"
- "isDCIM: returning NO"
- "isDCIM: returning YES"
- "isDCIM: will check if FAT/exFAT volume should handled by Photos"
- "lifa: at:%lu mt:%lu   ct:%lu"
- "lifa: s:%llu as:%llu fid:%llu"
- "lifa: vm:%#016llx t:%d m:%#05o nl:%u u:%d g:%d"
- "numberWithBool:"
- "setIsDCIM:"
- "v44@0:8@16i24B28i32@36"
- "volumeInfo"

```
