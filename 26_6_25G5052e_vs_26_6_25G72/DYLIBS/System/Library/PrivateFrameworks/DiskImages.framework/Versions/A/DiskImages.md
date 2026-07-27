## DiskImages

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-683.100.3.0.0
-  __TEXT.__text: 0x89678
+683.160.3.0.0
+  __TEXT.__text: 0x89694
   __TEXT.__auth_stubs: 0x2430
   __TEXT.__objc_methlist: 0x364
   __TEXT.__cstring: 0x248c6
Functions:
~ __ZN14CUDIFDiskImage11readSectorsExxPxPv : 1164 -> 1172
~ __ZN14CUDIFDiskImage15readSectorChunkExPxS0_PPv : 516 -> 532
~ __ZN14CUDIFDiskImage12writeSectorsExxPxPKv : 576 -> 580
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.93aMCz/Sources/DiskImages/framework/plugins/DiskImages/CDiskImageCompactor.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.93aMCz/Sources/DiskImages/framework/plugins/DiskImages/CSparseDiskImageFile.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cdPRY7/Sources/DiskImages/framework/plugins/DiskImages/CDiskImageCompactor.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cdPRY7/Sources/DiskImages/framework/plugins/DiskImages/CSparseDiskImageFile.cpp"
```
