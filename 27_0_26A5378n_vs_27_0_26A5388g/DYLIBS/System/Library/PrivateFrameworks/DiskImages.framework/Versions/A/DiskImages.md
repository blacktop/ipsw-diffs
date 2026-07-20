## DiskImages

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-698.0.0.0.0
-  __TEXT.__text: 0x898b0
+701.0.0.0.0
+  __TEXT.__text: 0x89904
   __TEXT.__objc_methlist: 0x364
-  __TEXT.__cstring: 0x248f8
+  __TEXT.__cstring: 0x249da
   __TEXT.__gcc_except_tab: 0x20e0
   __TEXT.__const: 0x1839
   __TEXT.__oslogstring: 0x72f

   - /usr/lib/libz.1.dylib
   Functions: 2465
   Symbols:   3780
-  CStrings:  3420
+  CStrings:  3423
 
Functions:
~ __ZN14CUDIFDiskImage11isValidBLKXEPP10UDIFBlocksx : 1740 -> 1684
~ __ZN14CUDIFDiskImage31generateGlobalBLKXFromBLKXTableEv : 808 -> 920
~ __ZN14CUDIFDiskImage11readSectorsExxPxPv : 1168 -> 1176
~ __ZN14CUDIFDiskImage15readSectorChunkExPxS0_PPv : 516 -> 532
~ __ZN14CUDIFDiskImage12writeSectorsExxPxPKv : 576 -> 580
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nUDr3i/Sources/DiskImages/framework/plugins/DiskImages/CDiskImageCompactor.cp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nUDr3i/Sources/DiskImages/framework/plugins/DiskImages/CSparseDiskImageFile.cpp"
+ "error: chunk %d compressedLength %qd exceeds worst-case compressed size %qd\n"
+ "error: chunk %d uncompressed size %qd exceeds limit %lu\n"
+ "error: compressed run compressedLength %qd exceeds worst-case compressed size %qd\n"
+ "error: compressed run uncompressed size %qd exceeds limit %lu\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.niVqXU/Sources/DiskImages/framework/plugins/DiskImages/CDiskImageCompactor.cp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.niVqXU/Sources/DiskImages/framework/plugins/DiskImages/CSparseDiskImageFile.cpp"
- "error: chunk %d has too many blocks %qd expected %ld\n"
```
