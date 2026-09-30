## asr

> `/usr/sbin/asr`

```diff

-  __TEXT.__text: 0x45f8c
-  __TEXT.__auth_stubs: 0x22a0
+  __TEXT.__text: 0x403a0
+  __TEXT.__auth_stubs: 0x2290
   __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0xec
-  __TEXT.__const: 0x588
-  __TEXT.__cstring: 0x8332
+  __TEXT.__const: 0x508
+  __TEXT.__cstring: 0x7703
   __TEXT.__ustring: 0x3dbe
   __TEXT.__objc_methname: 0x476
   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methtype: 0x3c5
   __TEXT.__oslogstring: 0x2c
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x6b8
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x6060
+  __TEXT.__unwind_info: 0x688
+  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__cfstring: 0x5e00
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x1160
+  __DATA_CONST.__auth_got: 0x1158
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0xf8
   __DATA.__objc_const: 0x3e0
   __DATA.__objc_selrefs: 0x198
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0xcb8
+  __DATA.__data: 0xbf8
   __DATA.__common: 0x80
-  __DATA.__bss: 0xfb0
+  __DATA.__bss: 0xb98
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 563
-  Symbols:   625
-  CStrings:  2108
+  Functions: 548
+  Symbols:   624
+  CStrings:  1999
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Symbols:
- _sysctlbyname
CStrings:
- "    %s freeze --target <target partition/volume> [--testsize <size>]\n                        [--retestsize <size>] [--recoverysize <size>]\n"
- "    %s thaw --target <volume> [--recovery] [--modifyrecovery]\n"
- "%s partition failed to verify"
- "%s/System/Library/CoreServices"
- "%s/boot.efi"
- "%s/usr/standalone/i386/apfs.efi"
- "--bootefi"
- "--partial, --modifyrecovery and --recovery are mutually exclusive."
- "/dev/disk%d"
- "Apple_Recovery"
- "Attaching disk subrange <%lld,%lld>\n"
- "BLLoadFile failed with error %d, line %d"
- "CSConvert"
- "Can't thaw because customer partition is mounted."
- "CopyFirstUUIDFolderName failed with error %d, line %d"
- "Could not run fsck_hfs on device"
- "Couldn't copy volume contents from source image - error %d"
- "Couldn't find system volume in container, line %d"
- "Couldn't get volume group information for device %s - %d"
- "Couldn't unmount all apfs volume - error %d"
- "Couldn't wipe/add Preboot volume - error %d"
- "Couldn't wipe/add Recovery volume - error %d"
- "Customer partition failed to verify"
- "DevEntryCopyRegistryProperty failed with error %d, line %d"
- "DevMountPartitionWithOptions failed with error %d, line %d"
- "DevUnmountAllPartitions failed with error %d, line %d"
- "DevUnmountPartition failed with error %d, line %d"
- "Device %s is no longer a valid partition."
- "Doing fsck of container..."
- "EmbedAPFSDriver failed with error %d, line %d"
- "Extras"
- "FAIL"
- "GetContainer failed with error %d, line %d"
- "GetRecoveryVolume failed with error %d, line %d"
- "GetRoledVolume failed with error %d, line %d"
- "IOMedia has no UUID, line %d"
- "Invalid argument \"%s\" for option modifyrecovery"
- "Invalid partition layout - unrecognized partition type before target partition"
- "Invalid target for freeze mode: %s"
- "Invalid target for thaw mode: %s"
- "It is not legal to use the \"max\" option with an external recovery partition"
- "No --target for freeze mode"
- "No --target for thaw mode"
- "No volume UUID information for LV"
- "Not a valid manufacturing partition layout - test partition can't be first or last"
- "Not a valid partition layout - customer partition not found"
- "Not a valid partition layout - test partition not in correct location"
- "Not a valid partition layout - too many partitions before the test partition"
- "Not doing a Core Storage conversion, but there's a header partition present."
- "Op"
- "Personalization"
- "Personalization failed with error %d, line %d"
- "PrFile"
- "Recovery PV is external but no extra PVs were specified."
- "Recovery PV not found in list of extra PVs."
- "Recovery modification canceled\n"
- "Return code was %d\n"
- "RunBless failed with error %d, line %d"
- "RunBlessOnVolume failed with error %d, line %d"
- "SetAPFSContainerSize failed with error %d, line %d"
- "Source"
- "TAODevEntryToVol failed with error %d, line %d"
- "Thaw target cannot be a whole disk."
- "Thawing failed: %s"
- "The given partition is not HFS or APFS, so it's not a valid MaxDisk partition"
- "Vol"
- "XERR\tMounted volume!"
- "XSTA\tfsck"
- "XSTA\tfsck %s"
- "XSTA\tfsck recovery"
- "XSTA\tstart\t%s\tthaw"
- "XSTA\tthaw"
- "booter"
- "booter  "
- "customer"
- "disk"
- "freeze"
- "fsck_apfs"
- "hw.memsize"
- "max"
- "modifyrecovery"
- "nocsconvert"
- "p"
- "partial"
- "recovery"
- "section-length"
- "section-start"
- "skip-in-use-check"
- "thaw"
- "thaw --partial has been deprecated.  Use adjust instead."

```
