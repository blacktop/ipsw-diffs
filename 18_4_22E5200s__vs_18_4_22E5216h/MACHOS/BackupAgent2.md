## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2624.100.67.0.0
-  __TEXT.__text: 0xa6474
+2624.100.98.0.0
+  __TEXT.__text: 0xa6930
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_stubs: 0xe2c0
-  __TEXT.__objc_methlist: 0x7450
+  __TEXT.__objc_stubs: 0xe300
+  __TEXT.__objc_methlist: 0x7440
   __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0x1de2a
-  __TEXT.__oslogstring: 0xe3e7
-  __TEXT.__objc_methname: 0x10cf6
+  __TEXT.__cstring: 0x1e20e
+  __TEXT.__oslogstring: 0xe800
+  __TEXT.__objc_methname: 0x10d09
   __TEXT.__objc_classname: 0xb4e
-  __TEXT.__objc_methtype: 0x2386
+  __TEXT.__objc_methtype: 0x2385
   __TEXT.__gcc_except_tab: 0x28e8
   __TEXT.__unwind_info: 0x1da0
   __DATA_CONST.__auth_got: 0xd10
   __DATA_CONST.__got: 0x560
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x16f8
-  __DATA_CONST.__cfstring: 0xb7a0
+  __DATA_CONST.__cfstring: 0xb760
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0xb248
-  __DATA.__objc_selrefs: 0x4758
+  __DATA.__objc_selrefs: 0x4760
   __DATA.__objc_ivar: 0x68c
   __DATA.__objc_data: 0x2710
   __DATA.__data: 0x8d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2943
+  Functions: 2941
   Symbols:   603
-  CStrings:  8005
+  CStrings:  8016
 
Symbols:
+ _OBJC_CLASS_$_MBManagedPolicy
- _MCFeatureCloudBackupAllowed
CStrings:
+ "=diag= %s does not have associated crypto dstreams"
+ "=restorable= =restorable= Failed to fetch the protection class for %@: %@"
+ "=restorable= =restorable= Failed to set protection class %d at %@: %@"
+ "=restorable= =restorable= Unexpected device lock error for pc:%d"
+ "=restorable= Cannot restore domain root %@ for %@ as symlink"
+ "=restorable= Creating empty file at %@"
+ "=restorable= Creating symbolic link: %@"
+ "=restorable= Directory already exists"
+ "=restorable= Expected failure setting protection class %d -> %d: %@"
+ "=restorable= Failed to clone from %@ to %@: %{errno}d"
+ "=restorable= Failed to get current protection class: %@"
+ "=restorable= Failed to hardlink from %@ to %@: %{errno}d"
+ "=restorable= Failed to move from %@ to %@: %@"
+ "=restorable= Failed to resolve On My iPhone file conflict from %@ to %@(%ld): %@"
+ "=restorable= Failed to restore BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore directory BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore protection class %d instead of %d at %@: %@"
+ "=restorable= Failed to restore regular file BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Failed to restore symlink BSD flags (0x%x) at %@: %{errno}d"
+ "=restorable= Fixing ownership at %@"
+ "=restorable= Making directory at %@ (0%3o)"
+ "=restorable= Making directory: 0%3o"
+ "=restorable= Not re-applying the com.apple.decmpfs xattr yet."
+ "=restorable= Not restoring protection class for symlink at %@"
+ "=restorable= Protection class is already %d, not setting for path: %s"
+ "=restorable= Removing existing %@"
+ "=restorable= Removing existing object %@"
+ "=restorable= Restoring BSD flags: 0x%x"
+ "=restorable= Restoring attributes u/gid %d/%d, b/m/c/atime %ld/%ld/%ld/%ld, permissions 0%o to %@"
+ "=restorable= Restoring directory BSD flags: 0x%x"
+ "=restorable= Restoring directory extended attributes (%ld) at path %@"
+ "=restorable= Restoring directory ownership: %d:%d at path %@"
+ "=restorable= Restoring directory permissions: 0%3o"
+ "=restorable= Restoring last modified time (%@) at %@"
+ "=restorable= Restoring last modified time (%@) for %@"
+ "=restorable= Restoring protection class %d at %@"
+ "=restorable= Restoring protection class %d instead of %d for: %@"
+ "=restorable= Restoring protection class: %d -> %d for path: %s"
+ "=restorable= Restoring regular file BSD flags: 0x%x at %@"
+ "=restorable= Restoring regular file extended attributes (%ld) at %@"
+ "=restorable= Restoring regular file ownership: %d:%d at %@"
+ "=restorable= Restoring regular file permissions: 0%3o at %@"
+ "=restorable= Restoring symbolic link extended attributes"
+ "=restorable= Restoring symbolic link ownership: %d:%d"
+ "=restorable= Restoring symbolic link permissions: 0%3o"
+ "=restorable= Restoring symlink BSD flags: 0x%x"
+ "=restorable= Successfully resolved On My iPhone file conflict from %@ to %@(%ld)"
+ "=restorable= The hashes of existing file and restoring file are the same. Skip re-restoring On My iPhone file at %@"
+ "=restorable= Unexpected failure setting protection class %d -> %d: %@"
+ "=restorable= Unexpected nil extended attribute com.apple.decmpfs for dataless file: %@"
+ "=restorable= Unspecified data class for %@ -> defaulting to %d"
+ "=restorable= Using APFSIOC_MAKE_OBJECT_DATALESS to restore the com.apple.decmpfs xattr on %@: %@"
+ "=restorable= fsctl(APFSIOC_MAKE_OBJECT_DATALESS) failed at %@: %{errno}d"
+ "=restorable= fstatat failed at %s (%ld): %{errno}d"
+ "=scanning= No domain root present for %@ found at %@ under %@"
+ "@28@0:8C16@20"
+ "_openRawEncryptedWithPathFSR:error:"
+ "_setProtectionClass:withPath:"
+ "checkIfDriveBackupIsAllowed:"
+ "checkIfDriveRestoreIsAllowed:"
+ "checkIfEnablingCloudBackupIsAllowed:"
+ "fcntl error setting Cx protection class"
+ "sharedPolicy"
- "/var/tmp/MDMRefuseToEnableCloudBackups"
- "@28@0:8C16r*20"
- "Backup disabled for this device"
- "Cannot restore domain root %@ for %@ as symlink"
- "Cloud backups are disabled via management for this device"
- "Creating empty file at %@"
- "Creating symbolic link: %@"
- "Directory already exists"
- "Failed to clone from %@ to %@: %{errno}d"
- "Failed to hardlink from %@ to %@: %{errno}d"
- "Failed to move from %@ to %@: %@"
- "Failed to resolve On My iPhone file conflict from %@ to %@(%ld): %@"
- "Failed to restore BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore directory BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore protection class %d instead of %d at %@: %@"
- "Failed to restore regular file BSD flags (0x%x) at %@: %{errno}d"
- "Failed to restore symlink BSD flags (0x%x) at %@: %{errno}d"
- "Failed to set protection class %d at %@: %@"
- "Fixing ownership at %@"
- "Making directory at %@ (0%3o)"
- "Making directory: 0%3o"
- "Not re-applying the com.apple.decmpfs xattr yet."
- "Not restoring protection class for symlink at %@"
- "Removing existing %@"
- "Removing existing object %@"
- "Restoring BSD flags: 0x%x"
- "Restoring attributes u/gid %d/%d, b/m/c/atime %ld/%ld/%ld/%ld, permissions 0%o to %@"
- "Restoring directory BSD flags: 0x%x"
- "Restoring directory extended attributes (%ld) at path %@"
- "Restoring directory ownership: %d:%d at path %@"
- "Restoring directory permissions: 0%3o"
- "Restoring last modified time (%@) at %@"
- "Restoring last modified time (%@) for %@"
- "Restoring protection class %d at %@"
- "Restoring protection class %d instead of %d for: %@"
- "Restoring protection class: %d for path: %s"
- "Restoring regular file BSD flags: 0x%x at %@"
- "Restoring regular file extended attributes (%ld) at %@"
- "Restoring regular file ownership: %d:%d at %@"
- "Restoring regular file permissions: 0%3o at %@"
- "Restoring symbolic link extended attributes"
- "Restoring symbolic link ownership: %d:%d"
- "Restoring symbolic link permissions: 0%3o"
- "Restoring symlink BSD flags: 0x%x"
- "Successfully resolved On My iPhone file conflict from %@ to %@(%ld)"
- "The hashes of existing file and restoring file are the same. Skip re-restoring On My iPhone file at %@"
- "Unexpected device lock error for pc:%d"
- "Unexpected nil extended attribute com.apple.decmpfs for dataless file: %@"
- "Unspecified data class for %@ -> defaulting to %d"
- "Using APFSIOC_MAKE_OBJECT_DATALESS to restore the com.apple.decmpfs xattr on %@: %@"
- "_setProtectionClass:withPathFSR:"
- "finfo->dstream_exists"
- "fsctl(APFSIOC_MAKE_OBJECT_DATALESS) failed at %@: %{errno}d"
- "fstatat failed at %s (%ld): %{errno}d"
- "isEphemeralMultiUser"
- "isSettingLockedDownByRestrictions:"
- "openRawEncryptedWithPath:error:"
- "openRawEncryptedWithPathFSR:error:"

```
