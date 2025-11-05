## kcditto

> `/usr/sbin/kcditto`

```diff

-755.0.0.0.0
-  __TEXT.__text: 0xfe70
+765.100.1.0.0
+  __TEXT.__text: 0xfe3c
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_stubs: 0x200
-  __TEXT.__cstring: 0x46ba
+  __TEXT.__cstring: 0x46b6
   __TEXT.__const: 0x848
   __TEXT.__oslogstring: 0x14e
   __TEXT.__objc_methname: 0x178
   __TEXT.__unwind_info: 0x258
   __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3D3808E-980E-3790-92B3-2D631FF48A03
+  UUID: CD1809D8-50A8-3EEE-B5CF-516FE77B4BD2
   Functions: 145
   Symbols:   274
-  CStrings:  650
+  CStrings:  649
 
Functions:
~ sub_1000022c8 -> sub_100001330 : 280 -> 276
~ sub_100002f58 -> sub_100001fbc : 292 -> 284
~ sub_100003dcc -> sub_100002e28 : 224 -> 220
~ sub_100003eac -> sub_100002f04 : 100 -> 92
~ sub_1000048bc -> sub_10000390c : 1320 -> 1328
~ sub_100004de4 -> sub_100003e3c : 476 -> 492
~ sub_100005dd4 -> sub_100004e3c : 416 -> 412
~ sub_100006430 -> sub_100005494 : 376 -> 360
~ sub_100007ae4 -> sub_100006b38 : 2952 -> 2948
~ sub_100008ad0 -> sub_100007b20 : 512 -> 500
~ sub_10000951c -> sub_100008560 : 532 -> 524
~ sub_100009730 -> sub_10000876c : 328 -> 324
~ sub_100009878 -> sub_1000088b0 : 1828 -> 1852
~ sub_10000a1e4 -> sub_100009234 : 1188 -> 1176
~ sub_10000a888 -> sub_1000098cc : 572 -> 596
~ sub_10000b018 -> sub_10000a074 : 1064 -> 1096
~ sub_10000b65c -> sub_10000a6d8 : 632 -> 628
~ sub_10000ba5c -> sub_10000aad4 : 1084 -> 1072
~ sub_10000c2e8 -> sub_10000b354 : 360 -> 352
~ sub_10000c960 -> sub_10000b9c4 : 3860 -> 3872
~ sub_10000e2b4 -> sub_10000d324 : 2544 -> 2492
~ sub_10001118c -> sub_1000101c8 : 760 -> 748
~ sub_100011648 -> sub_100010678 : 724 -> 720
~ sub_10001191c -> sub_100010948 : 404 -> 412
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"
- "-v="
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.122: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.132: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.188: Could not find volume group UUID for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.222: Could not find preboot volume for volume device path %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.228: Found 0 Preboot volumes.\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.279: Encountered error while inspecting path: %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.295: Error considering KC copy: srcPath = %s, dstPath = %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.29: BOMCopier fatal file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.303: Error copying KC: srcPath = %s, dstPath = %s, error %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.319: Error creating BOMCopier\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.330: error creating / accessing '%s': %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.34: BOMCopier fatal error: %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.379: You must be running as root to manage the kext collection preboot area.\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.386: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.391: Error reading bootcaches for volume %s - no fileset path?\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.398: Couldn't find volume group UUID for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.39: BOMCopier file error: %d at %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.404: Couldn't find preboot mount (or preboot not mounted) for volume %s (%s)\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.432: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.444: Error considering preboot KC path for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.453: Error considering preboot volume for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.458: Error copying KCs (SystemVolumeUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.462: Error copying KCs (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.474: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.485: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.494: Error considering preboot PLK path for %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.499: Error copying prelinked kernels (SystemUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.503: Error copying prelinked kernels (VolGroupUUID): %d\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.542: You must be running as root to manage the prelinked kernel staging area.\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.549: Error reading bootcaches for volume %s...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.554: Error reading bootcaches for volume %s - no plk path?\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.560: Error reading bootcaches for volume %s - no plk staging path?\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.571: Error considering prelinked staging area...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.580: Error considering prelinked destination...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.585: Error copying kernels...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.68: Could not exec %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.78: %s returned non-0 exit status\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kc_staging.m.97: Error creating temp preboot mount point %d (%s)\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.24: kcditto installs previously built kext collections onto the Preboot volume.\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.25: It takes no arguments.\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.33: Can't get executable path for (%d)%s: %s\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.43: Error copying deferred prelinked kernels (standalone)...\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/kext_tools/kcditto_main.m.49: Error copying KCs (standalone)...\n"

```
