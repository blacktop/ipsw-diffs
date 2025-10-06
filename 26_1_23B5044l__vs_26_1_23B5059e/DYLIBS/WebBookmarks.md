## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-622.2.5.10.3
-  __TEXT.__text: 0xa1e6c
+622.2.9.10.3
+  __TEXT.__text: 0xa2100
   __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x83e4
+  __TEXT.__objc_methlist: 0x83fc
   __TEXT.__const: 0x326
-  __TEXT.__gcc_except_tab: 0xb420
-  __TEXT.__cstring: 0xe22c
+  __TEXT.__gcc_except_tab: 0xb47c
+  __TEXT.__cstring: 0xe26c
   __TEXT.__oslogstring: 0x87c2
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x41e0
+  __TEXT.__unwind_info: 0x41f8
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x15c01
-  __TEXT.__objc_methtype: 0x26f5
+  __TEXT.__objc_methname: 0x15c43
+  __TEXT.__objc_methtype: 0x26f8
   __TEXT.__objc_stubs: 0xeb20
   __DATA_CONST.__got: 0x790
-  __DATA_CONST.__const: 0x2e28
+  __DATA_CONST.__const: 0x2e38
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c78
+  __DATA_CONST.__objc_selrefs: 0x4c88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x708
   __AUTH_CONST.__const: 0x11c0
-  __AUTH_CONST.__cfstring: 0x6080
+  __AUTH_CONST.__cfstring: 0x60a0
   __AUTH_CONST.__objc_const: 0x9a48
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 17FB6E7E-7CFF-3D00-99BA-A3D63D34537F
-  Functions: 3574
-  Symbols:   12205
-  CStrings:  6342
+  UUID: 39C1CD4B-799C-3ECC-A138-A54973635645
+  Functions: 3576
+  Symbols:   12214
+  CStrings:  6346
 
Symbols:
+ -[WebBookmark(ReadingList) migrateToBookmarkItem]
+ -[WebBookmark(ReadingList) migrateToReadingListItem]
+ -[WebBookmarkCollection _fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:sortedByOrderIndex:]
+ _BookmarkDictionaryKey
+ ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.833
+ ___Block_byref_object_copy_.1855
+ ___Block_byref_object_dispose_.1856
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1858
+ ___block_literal_global.1021
+ ___block_literal_global.1061
+ ___block_literal_global.1131
+ ___block_literal_global.1141
+ ___block_literal_global.1143
+ ___block_literal_global.1853
+ ___block_literal_global.1860
+ ___block_literal_global.1868
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_WebBookmarks
+ _objc_msgSend$_fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:sortedByOrderIndex:
- -[WebBookmarkCollection _fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:]
- ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.830
- ___Block_byref_object_copy_.1852
- ___Block_byref_object_dispose_.1853
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1855
- ___block_literal_global.1018
- ___block_literal_global.1058
- ___block_literal_global.1128
- ___block_literal_global.1138
- ___block_literal_global.1140
- ___block_literal_global.1847
- ___block_literal_global.1857
- ___block_literal_global.1865
- _objc_msgSend$_fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:
CStrings:
+ "@32@0:8i16B20B24B28"
+ "SELECT id FROM bookmarks WHERE %@ ORDER BY order_index ASC"
+ "_fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:sortedByOrderIndex:"
+ "migrateToBookmarkItem"
+ "migrateToReadingListItem"
- "@28@0:8i16B20B24"
- "_fetchBookmarkIDsInFolder:onlyFolders:includingHiddenBookmarks:"

```
