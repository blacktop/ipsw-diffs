## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

```diff

-579.5.1.0.0
-  __TEXT.__text: 0x2d95c
+579.5.2.0.0
+  __TEXT.__text: 0x2da1c
   __TEXT.__auth_stubs: 0x1490
   __TEXT.__delay_stubs: 0x280
   __TEXT.__delay_helper: 0x564

   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: F275E2B4-1B15-3746-BC83-006741029F41
+  UUID: 05082B48-5C14-35C4-9EBF-0C41906BFA09
   Functions: 637
   Symbols:   1945
   CStrings:  610
Symbols:
+ __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PPK10__CFNumberSB_PP9__CFError
+ __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PPK10__CFNumberSB_PP9__CFError.cold.1
+ __ZL28createBookmarkWithURLAtDepthPK13__CFAllocatorPK7__CFURLmS4_PK9__CFArrayR19BookmarkMutableDatajbPPK10__CFNumberSD_PP9__CFError
- __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PP9__CFError
- __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PP9__CFError.cold.1
- __ZL28createBookmarkWithURLAtDepthPK13__CFAllocatorPK7__CFURLmS4_PK9__CFArrayR19BookmarkMutableDatajbPP9__CFError
Functions:
~ __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PP9__CFError -> __Z25__CFURLCreateBookmarkDataPK13__CFAllocatorPK7__CFURLmPK9__CFArrayS4_PPK10__CFNumberSB_PP9__CFError : 424 -> 444
~ __ZL28createBookmarkWithURLAtDepthPK13__CFAllocatorPK7__CFURLmS4_PK9__CFArrayR19BookmarkMutableDatajbPP9__CFError -> __ZL28createBookmarkWithURLAtDepthPK13__CFAllocatorPK7__CFURLmS4_PK9__CFArrayR19BookmarkMutableDatajbPPK10__CFNumberSD_PP9__CFError : 4876 -> 5004
~ __CFURLCreateBookmarkData : 408 -> 448
~ __ZL29addVolumeInfoForURLToBookmarkPK13__CFAllocatorR19BookmarkMutableDataPK7__CFURLmjPK9__CFArrayPP9__CFError : 1112 -> 1116

```
