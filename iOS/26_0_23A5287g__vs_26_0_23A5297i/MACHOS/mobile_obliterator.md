## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-350.0.0.0.0
-  __TEXT.__text: 0x17c24
+353.0.0.0.0
+  __TEXT.__text: 0x17f34
   __TEXT.__auth_stubs: 0x1430
   __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0xa0ea
+  __TEXT.__cstring: 0xa292
   __TEXT.__const: 0x6c8
   __TEXT.__objc_methname: 0x4ec
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x3d8
   __DATA_CONST.__auth_got: 0xa28
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x668
-  __DATA_CONST.__cfstring: 0x17a0
+  __DATA_CONST.__const: 0x678
+  __DATA_CONST.__cfstring: 0x17e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 41BA4F00-7A57-3CDB-AF8D-46A1F6F663D2
+  UUID: A9F292F4-36F2-3E55-B0F2-617D4952020D
   Functions: 240
   Symbols:   374
-  CStrings:  1417
+  CStrings:  1430
 
CStrings:
+ " (sim-fail DATA_VOLUME_DELETION)"
+ " (sim-fail DATA_VOLUME_UNMOUNT)"
+ " (sim-fail USER_VOLUME_DELETION)"
+ " (sim-fail USER_VOLUME_SETUP_UM)"
+ " (sim-fail USER_VOLUME_UNMOUNT)"
+ "%s: %s%s: Calling newfs_apfs for the %s volume on container %s"
+ "%s: %sBricking"
+ "%s: %sBricking but preserving user data..."
+ "%s: %sCleaning Hardware volume"
+ "%s: %sObliterating the Data volume"
+ "%s: %sPopulating USER volume with mastered content"
+ "%s: %sRebuilding the %sData volume"
+ "%s: %sRemoving preserved files from storage"
+ "%s: %sSetting up UM/AKS for the new Data volume"
+ "%s: Could not delete existing non fstab APFS volumes%s"
+ "%s: Could not delete the Data volume %s (error: %d)%s"
+ "%s: Failed to re-set the user volume in RRTS mode%s"
+ "%s: Failed to set up the data volume in multiuser mode%s"
+ "%s: RRTS: %sCalling AKSVolumeUnmap() with disk:%s of the User"
+ "%s: RRTS: %sRe-setting UM/AKS of the new User volume"
+ "%s: RRTS: %sRestoring Data volume content"
+ "%s: RRTS: Could not delete existing non fstab APFS volumes%s"
+ "%s: RRTS: not need to obliterate the Data volume, %sdeleting non-fstab volumes"
+ "%s: SafeWipe: Could not unmount the Data volume %s (error: %d)%s"
+ "%s: SafeWipe: Could not unmount the User volume %s (error: %d)%s"
+ "ObliterationManagedDeviceSkipRestore"
+ "[Skip] "
+ "private/var/db/com.apple.mdmclient.EACSPreserve.SkipSetup.Restore"
- "%s: %s: Calling newfs_apfs for the %s volume on container %s"
- "%s: Bricking but preserving user data..."
- "%s: Cleaning Hardware volume"
- "%s: Could not delete existing non fstab APFS volumes"
- "%s: Could not delete the Data volume %s (error: %d)"
- "%s: Failed to set up the data volume in multiuser mode"
- "%s: Obliterating the Data volume"
- "%s: Populating USER volume with mastered content"
- "%s: RRTS: Calling AKSVolumeUnmap() with disk:%s of the User"
- "%s: RRTS: Could not delete existing non fstab APFS volumes"
- "%s: RRTS: Re-setting UM/AKS of the new User volume"
- "%s: RRTS: Restoring Data volume content"
- "%s: RRTS: skip obliterating the Data volume, deleting non-fstab volumes"
- "%s: Rebuilding the %sData volume"
- "%s: SafeWipe: Could not unmount the Data volume %s (error: %d)"
- "%s: SafeWipe: Could not unmount the User volume %s (error: %d)"
- "%s: Setting up UM/AKS for the new Data volume"

```
