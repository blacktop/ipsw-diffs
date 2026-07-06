## kcditto

> `/usr/sbin/kcditto`

```diff

-  __TEXT.__text: 0xfe1c
+  __TEXT.__text: 0xfe18
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_stubs: 0x200
   __TEXT.__cstring: 0x4bdb
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
Functions:
~ sub_100003e80 : 476 -> 480
~ sub_100005f30 -> sub_100005f34 : 236 -> 248
~ sub_10000b954 -> sub_10000b964 : 3876 -> 3868
~ sub_10000f5d0 -> sub_10000f5d8 : 1516 -> 1508
~ sub_10001058c : 208 -> 204
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GmmE85/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NXAB8i/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"

```
