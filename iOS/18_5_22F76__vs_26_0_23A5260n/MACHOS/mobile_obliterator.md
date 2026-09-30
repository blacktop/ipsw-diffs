## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-320.120.5.0.0
-  __TEXT.__text: 0x15f84
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_stubs: 0x620
+346.0.0.0.0
+  __TEXT.__text: 0x17c18
+  __TEXT.__auth_stubs: 0x1430
+  __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x941e
+  __TEXT.__cstring: 0xa06c
   __TEXT.__const: 0x6c8
-  __TEXT.__objc_methname: 0x478
+  __TEXT.__objc_methname: 0x4ec
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__auth_got: 0xa10
+  __TEXT.__unwind_info: 0x3d8
+  __DATA_CONST.__auth_got: 0xa28
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x628
-  __DATA_CONST.__cfstring: 0x1580
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__cfstring: 0x1760
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x198
+  __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xd20
+  __DATA.__data: 0x120
   __DATA.__common: 0x200
-  __DATA.__bss: 0x520
+  __DATA.__bss: 0x2938
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5A95DF7E-87E6-342C-B724-84D5897F3BC8
-  Functions: 230
-  Symbols:   371
-  CStrings:  1313
+  UUID: 53B3B37C-DD78-3A3D-909B-E7C49B81AA80
+  Functions: 241
+  Symbols:   374
+  CStrings:  1410
 
Symbols:
+ _AKSVolumeUnmap
+ _fs_snapshot_list
+ _fs_snapshot_revert
CStrings:
+ "%@/((|mandev-)appv|(|mansta-|mandev-)fCfg|pcrt|scrt|seal|ChMf|SCfT)-%@/ "
+ "%s Done"
+ "%s failed with [gF: 0x%016llX] Attempt: 1"
+ "%s%s"
+ "%s/alt_root"
+ "%s/mobile"
+ "%s/tmp"
+ "%s: %s failed with error %d"
+ "%s: %s: Error: expected exactly one volume with role 0x%x"
+ "%s: %s: new volume dev node is %s"
+ "%s: APFSVolumeRoleFind returned %@"
+ "%s: ERRTS: UID = %d; UID = %d; PID = %d; PPID = %d."
+ "%s: Failed to re-set the user volume in RRTS mode"
+ "%s: Found Data volume device, default mount point '%s'"
+ "%s: No RRTS BSToken specified in the options"
+ "%s: No RRTS snapshot to revert to specified in the options"
+ "%s: RRTS BSToken is not CFData"
+ "%s: RRTS snapshot name is not CFString"
+ "%s: RRTS: AKS IdentityLoad succeeded"
+ "%s: RRTS: AKS VolumeMapPath succeeded"
+ "%s: RRTS: Calling AKSVolumeUnmap() with disk:%s of the User"
+ "%s: RRTS: Completed deletion of non fstab APFS volumes if present"
+ "%s: RRTS: Could not delete existing non fstab APFS volumes"
+ "%s: RRTS: Failed to convert data mount point string %s to NSString"
+ "%s: RRTS: Failed to obtain shared UserManagement instance"
+ "%s: RRTS: Failed to set convert snapshot name to cstring"
+ "%s: RRTS: Old mask has value %o; New mask has value %o."
+ "%s: RRTS: Re-setting UM/AKS of the new User volume"
+ "%s: RRTS: Refresh of the default user identity succeeded"
+ "%s: RRTS: Restoring Data volume content"
+ "%s: RRTS: Unable to open data volume directory: %s (%d)\n"
+ "%s: RRTS: Unable to restore filesystem stuff."
+ "%s: RRTS: checking if snapshot '%s' exists on the data volume"
+ "%s: RRTS: failed to set revert to snapshot: %s (%d)\n"
+ "%s: RRTS: fs_snapshot_list() failed with error %d"
+ "%s: RRTS: setting revert-to-snapshot for '%s' on the data volume"
+ "%s: RRTS: skip cleaning up the hardware volume"
+ "%s: RRTS: skip creating overprovisioning file and mobile path"
+ "%s: RRTS: skip obliterating the Data volume, deleting non-fstab volumes"
+ "%s: RRTS: skip reformatting the Data volume"
+ "%s: RRTS: skip shared-iPad reboot stage"
+ "%s: RRTS: snapshot %s"
+ "%s: RRTS: successfully set revert to snapshot"
+ "%s: RRTS: volume has snapshot with name '%s'"
+ "%s: Rapid Return to Service is in progress..."
+ "%s: Safe %s failed, returning %d"
+ "%s: Unable to find any FSSpec nodes in fstab"
+ "%s: Unable to find snapshot '%s'"
+ "%s: safeObliterate: mount Data volume %s"
+ "%s: safeObliterate: unmount Data volume %s"
+ "%s: safeObliteration is in progress..."
+ "%s: safeRRTS is in progress..."
+ "%s: safeRRTS: Calling AKSVolumeUnmap() with disk:%s of the User"
+ "%s: safeRRTS: Completed deletion of non fstab APFS volumes if present"
+ "%s: safeRRTS: Could not delete existing non fstab APFS volumes"
+ "%s: safeRRTS: EUID = %d; UID = %d; PID = %d; PPID = %d."
+ "%s: safeRRTS: Old mask has value %o; New mask has value %o."
+ "%s: safeRRTS: Re-setting UM/AKS of the new User volume"
+ "%s: safeRRTS: Restoring Data volume content"
+ "%s: safeRRTS: Unable to restore filesystem stuff."
+ "%s: safeRRTS: skip cleaning up the hardware volume"
+ "%s: safeRRTS: skip obliterating the Data volume, deleting non-fstab volumes"
+ "-r"
+ "-t"
+ "-w"
+ "/private/var/MobileSoftwareUpdate"
+ "/private/var/hardware"
+ "/private/xarts"
+ "AKSVolumeUnmap returned %@"
+ "EACS"
+ "Oblit"
+ "Obliteration"
+ "ObliterationTypeRRTS"
+ "RRTS"
+ "RRTS snapshot '%@' does not exist on data volume"
+ "RRTS: AKSIdentityLoad for UUID %@ failed with error:%@"
+ "RRTS: AKSVolumeMap failed with error:%@"
+ "RRTS: Got shared UserManagement instance: %@"
+ "RRTS: Primary user re-load with uuid: %@ and session uid:%d"
+ "RRTS: Refresh of the default user identity failed with %@"
+ "RRTS: calling volume map for User Data Volume on %@"
+ "RRTS: primaryUserOnSharedDataVolumePath() failed, error %@"
+ "RRTS: rebuild"
+ "RRTSBootStrapToken"
+ "RRTSRevertToSnapshotName"
+ "Safe%s done @%ld, Err:%d, By:%s"
+ "Safe%s failed with [gF: 0x%016llX] Attempt: %ld"
+ "apfs"
+ "create_fsspec_nodes_list"
+ "does not exist"
+ "failed"
+ "lookup_volume_by_role"
+ "oblit-rrts-bstoken"
+ "oblit-rrts-snapshot"
+ "primaryUserOnSharedDataVolumePath:withError:"
+ "refreshPrimaryUserOnSharedDataVolumePath:withBootstrapToken:withError:"
+ "rrts_revert_data_volume_to_snapshot"
+ "rrts_setup_user_and_data_volumes"
+ "safeObliterate: Found BST %@ and Snapshot %@"
+ "succeeded"
+ "var"
+ "verified to exist"
+ "verify_snapshot_exists"
- "%@/(appv|(|mansta-)fCfg|pcrt|scrt|seal|ChMf|SCfT)-%@/ "
- "%s: %s: APFSVolumeRoleFind returned %s"
- "%s: %s: Error: expected exactly one volume with '%s' role"
- "%s: %s: newfs_apfs new volume dev node is %s"
- "%s: Binding shared data volume to primary identity"
- "%s: Data Obliteration failed with error %d"
- "%s: Safe Obliteration failed, returning %d"
- "%s: Unable to find any FSSpec nodes in fstab, bailing"
- "/private/var/mobile"
- "/private/var/tmp"
- "/private/var/tmp/alt_root"
- "/private/var/tmp/alt_root/private/var"
- "/private/var/tmp/alt_root/private/var/mobile"
- "/sbin/mount_apfs"
- "EACS Done"
- "EACS failed with [gF: 0x%016llX] Attempt: 1"
- "Safe Obliteration failed with [gF: 0x%016llX] Attempt: %ld"
- "SafeOblit done @%ld, Err:%d, By:%s"
- "Unknown obliteration type specified"
- "data"
- "user"

```
