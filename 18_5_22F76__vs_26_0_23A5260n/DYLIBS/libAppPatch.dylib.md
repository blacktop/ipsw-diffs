## libAppPatch.dylib

> `/usr/lib/libAppPatch.dylib`

```diff

-1378.100.35.0.0
-  __TEXT.__text: 0x133e8
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x45c
-  __TEXT.__cstring: 0x5687
-  __TEXT.__const: 0x60
+1513.0.8.0.2
+  __TEXT.__text: 0x145c4
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x4c4
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x5933
   __TEXT.__oslogstring: 0x23a
-  __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__gcc_except_tab: 0x2c8
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0x162b
-  __TEXT.__objc_methtype: 0x3ed
-  __TEXT.__objc_stubs: 0xea0
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x358
+  __TEXT.__objc_methname: 0x1784
+  __TEXT.__objc_methtype: 0x438
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x3620
+  __AUTH_CONST.__cfstring: 0x36c0
   __AUTH_CONST.__objc_const: 0x278
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D320B25-9C33-305D-8F58-48A4D26B3526
-  Functions: 209
-  Symbols:   879
-  CStrings:  1228
+  UUID: 563F74B7-CCD5-3930-BD18-5F5A44DE5F61
+  Functions: 223
+  Symbols:   927
+  CStrings:  1260
 
Symbols:
+ -[MIFileManager _firstAvailableParentForURL:error:]
+ -[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]
+ -[MIFileManager copyVolumeInfo:forURL:error:]
+ -[MIFileManager createRelativeDirectoryPath:inBaseDirectory:mode:class:error:]
+ -[MIFileManager enumerateExternalVolumesWithBlock:]
+ -[MIFileManager mountPointForURL:error:]
+ -[MIFileManager mountPointForVolumeUUID:error:]
+ -[MIFileManager setOwnershipAtURL:toUID:gid:error:]
+ -[MIFileManager volumeUUIDForURL:error:]
+ GCC_except_table105
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table69
+ _CFBundleCopyBundleURL
+ _MICreateCFBundle
+ _MILoadInfoPlistFromBundleWithError
+ _OBJC_CLASS_$_NSUUID
+ ___47-[MIFileManager mountPointForVolumeUUID:error:]_block_invoke
+ ___51-[MIFileManager _firstAvailableParentForURL:error:]_block_invoke
+ ___51-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke
+ ___58-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke
+ ___block_descriptor_104_e8_32s40r48r56r64r72r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8r48l8r56l8r64l8r72l8s32l8
+ ___block_descriptor_40_e8_32bs_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e97_"NSError"24?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16lr32l8
+ ___block_descriptor_41_e8_32bs_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8
+ ___block_descriptor_48_e8_32r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr32l8
+ ___block_descriptor_48_e8_32s40r_e30_v32?0"NSURL"8"NSUUID"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8
+ ___block_descriptor_49_e8_32s40r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8s40l8r48l8
+ ___block_descriptor_66_e8_32s40r48r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16lr40l8s32l8r48l8
+ ___block_descriptor_85_e8_32s40s48s56r64r_e32_B24?0^{?=Qq*Q*QIIIIIIISBC}8^B16ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.124
+ _getattrlist
+ _getmntinfo_r_np
+ _libAppPatchVersionNumber
+ _libAppPatchVersionString
+ _objc_msgSend$_firstAvailableParentForURL:error:
+ _objc_msgSend$_traverseUntilFirstAvailableParentOfURL:withBlock:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:mode:error:
+ _objc_msgSend$enumerateExternalVolumesWithBlock:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$volumeUUIDForURL:error:
+ _statfs_ext
- GCC_except_table26
- GCC_except_table31
- GCC_except_table35
- GCC_except_table37
- GCC_except_table44
- GCC_except_table92
- __CreateCFBundle
- ___block_descriptor_104_e8_32s40r48r56r64r72r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8r48l8r56l8r64l8r72l8s32l8
- ___block_descriptor_40_e8_32bs_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8
- ___block_descriptor_41_e8_32bs_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8
- ___block_descriptor_48_e8_32s40r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8
- ___block_descriptor_49_e8_32s40r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8s40l8r48l8
- ___block_descriptor_66_e8_32s40r48r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16lr40l8s32l8r48l8
- ___block_descriptor_85_e8_32s40s48s56r64r_e32_B24?0^{?=Qq*Q*QQIIIIIISBC}8^B16ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.105
CStrings:
+ "-[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]"
+ "-[MIFileManager copyVolumeInfo:forURL:error:]"
+ "-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke"
+ "-[MIFileManager enumerateExternalVolumesWithBlock:]"
+ "-[MIFileManager mountPointForURL:error:]"
+ "-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke"
+ "-[MIFileManager volumeUUIDForURL:error:]"
+ "@\"NSError\"24@?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16"
+ "@24@0:8@?16"
+ "@48@0:8@16@24S32i36^@40"
+ "@48@0:8@16q24@32^@40"
+ "@52@0:8@16q24@32i40^@44"
+ "@52@0:8@16q24i32@36^@44"
+ "B24@?0^{?=Qq*Q*QIIIIIIISBC}8^B16"
+ "B40@0:8^{?=[16C][16c][1024c]}16@24^@32"
+ "Couldn't get data from xattr named %s on \"%s\""
+ "Couldn't get length for xattr named %s on \"%s\""
+ "MICreateCFBundle"
+ "MILoadInfoPlistFromBundleWithError"
+ "[f]getxattr failed for xattr named %s path %s fd %d"
+ "[f]getxattr failed to get length for xattr named %s path %s fd %d"
+ "_firstAvailableParentForURL:error:"
+ "_traverseUntilFirstAvailableParentOfURL:withBlock:"
+ "apfs"
+ "copyVolumeInfo:forURL:error:"
+ "createRelativeDirectoryPath:inBaseDirectory:mode:class:error:"
+ "enumerateExternalVolumesWithBlock:"
+ "getattrlist failed for %@: %s"
+ "getmntinfo_r_np failed: %s"
+ "getxattr for xattr named %s on \"%s\" returned %zd (expected %zu)"
+ "initWithUUIDBytes:"
+ "mountPointForURL:error:"
+ "mountPointForVolumeUUID:error:"
+ "setOwnershipAtURL:toUID:gid:error:"
+ "statfs failed for %@: %s"
+ "v32@?0@\"NSURL\"8@\"NSUUID\"16^B24"
+ "volumeUUIDForURL:error:"
+ "xattr named %s not present on \"%s\""
- "-[MIFileManager deviceForURLOrFirstAvailableParent:error:]"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "@52@0:8@16Q24i32@36^@44"
- "Attr named %s not present on \"%s\""
- "B24@?0^{?=Qq*Q*QQIIIIIISBC}8^B16"
- "Couldn't get data from EA named %s on \"%s\": %s"
- "MILoadInfoPlistWithError"
- "[f]getxattr failed for path %s fd %d"
- "_CreateCFBundle"
- "getxattr for EA named %s on \"%s\" returned %zd (expected %zu)"

```
