## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-623.2.4.0.0
-  __TEXT.__text: 0xa0598
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x828c
+623.2.7.0.0
+  __TEXT.__text: 0x9f84c
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_methlist: 0x8214
   __TEXT.__const: 0x326
-  __TEXT.__gcc_except_tab: 0xb80c
-  __TEXT.__cstring: 0xe24c
+  __TEXT.__gcc_except_tab: 0xb6a4
+  __TEXT.__cstring: 0xe22c
   __TEXT.__oslogstring: 0x8d8d
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4278
+  __TEXT.__unwind_info: 0x4260
   __TEXT.__objc_classname: 0x988
-  __TEXT.__objc_methname: 0x15d6f
-  __TEXT.__objc_methtype: 0x2749
-  __TEXT.__objc_stubs: 0xeae0
+  __TEXT.__objc_methname: 0x15ab1
+  __TEXT.__objc_methtype: 0x26ca
+  __TEXT.__objc_stubs: 0xea40
   __DATA_CONST.__got: 0x798
   __DATA_CONST.__const: 0x2e80
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ce0
+  __DATA_CONST.__objc_selrefs: 0x4cb8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__cfstring: 0x5e80
-  __AUTH_CONST.__objc_const: 0x9720
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0x1000
+  __AUTH_CONST.__cfstring: 0x5e60
+  __AUTH_CONST.__objc_const: 0x9690
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5d4
+  __DATA.__objc_ivar: 0x5cc
   __DATA.__data: 0xf48
   __DATA.__bss: 0xbc
   __DATA_DIRTY.__objc_data: 0x1450

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D2FB056-16BE-318A-A4AA-FFD0E7C3C226
-  Functions: 3503
-  Symbols:   12036
-  CStrings:  6340
+  UUID: E68839C0-6776-35F8-8763-9D2F1650E94D
+  Functions: 3492
+  Symbols:   12007
+  CStrings:  6326
 
Symbols:
+ +[WBDeviceParameters localDeviceWithTitle:creationDeviceIdentifier:]
+ +[WBDeviceParameters remoteDeviceWithTitle:]
+ +[WBMutableTabGroup unnamedTabGroupWithUUID:profileIdentifier:]
+ +[WBMutableTabGroup unnamedTabGroup]
+ +[WBTab pinnedTabWithTitle:url:]
+ +[WBTab startPageTab]
+ -[WBMutableTabGroup initWithTitle:profileIdentifier:]
+ -[WBProfile initWithTitle:]
+ -[WBProfile initWithTitle:symbolImageName:favoritesFolderServerID:]
+ -[WBTab initWithTitle:url:]
+ -[WBTab initWithUUID:]
+ -[WBTab initWithUUID:lastVisitTime:]
+ -[WBTab initWithUUID:title:url:]
+ -[WBTab initWithUUID:title:url:isPrivateBrowsing:]
+ -[WBTab initWithUUID:title:url:lastVisitTime:]
+ -[WBTab initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:]
+ -[WBTabGroup initWithTitle:]
+ -[WBTabGroup initWithTitle:uuid:]
+ -[WBWindowState localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:]
+ -[WebBookmark initFolderWithParentID:subtype:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:folder:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:subtype:collectionType:]
+ -[WebBookmark initWithTitle:address:parentID:subtype:collectionType:score:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:collectionType:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:collectionType:skipDecodingSyncData:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:]
+ -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:].cold.1
+ -[WebBookmark(Internal) initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:].cold.2
+ ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.835
+ ___Block_byref_object_copy_.1893
+ ___Block_byref_object_dispose_.1894
+ ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1896
+ ___block_descriptor_48_ea8_32s40s_e24_B24?0"WebBookmark"8q16ls32l8s40l8
+ ___block_literal_global.1023
+ ___block_literal_global.1066
+ ___block_literal_global.1136
+ ___block_literal_global.1148
+ ___block_literal_global.1885
+ ___block_literal_global.1891
+ ___block_literal_global.1898
+ ___block_literal_global.1912
+ ___block_literal_global.212
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.684
+ _objc_msgSend$initFolderWithParentID:subtype:collectionType:
+ _objc_msgSend$initWithSQLiteStatement:collectionType:
+ _objc_msgSend$initWithSQLiteStatement:collectionType:skipDecodingSyncData:
+ _objc_msgSend$initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$initWithTitle:address:parentID:folder:collectionType:
+ _objc_msgSend$initWithTitle:address:parentID:subtype:collectionType:
+ _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:
+ _objc_msgSend$initWithTitle:url:
+ _objc_msgSend$initWithTitle:uuid:
+ _objc_msgSend$initWithUUID:title:url:
+ _objc_msgSend$initWithUUID:title:url:lastVisitTime:
+ _objc_msgSend$initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:
+ _objc_msgSend$initWithValue:generation:
+ _objc_msgSend$initWithValueSource:valueProvider:valueUpdater:generation:
+ _objc_msgSend$localDeviceWithTitle:creationDeviceIdentifier:
+ _objc_msgSend$localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:
+ _objc_msgSend$startPageTab
+ _objc_msgSend$unnamedTabGroupWithUUID:profileIdentifier:
+ _objc_retain_x7
- +[WBDeviceParameters localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:]
- +[WBDeviceParameters remoteDeviceWithTitle:deviceIdentifier:]
- +[WBMutableTabGroup unnamedTabGroupWithDeviceIdentifier:]
- +[WBMutableTabGroup unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:]
- +[WBTab pinnedTabWithTitle:url:deviceIdentifier:]
- +[WBTab startPageTabWithDeviceIdentifier:]
- -[WBDeviceParameters deviceIdentifier]
- -[WBDeviceParameters setDeviceIdentifier:]
- -[WBMutableTabGroup initWithTitle:deviceIdentifier:profileIdentifier:]
- -[WBProfile deviceIdentifier]
- -[WBProfile initWithTitle:deviceIdentifier:]
- -[WBProfile initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:]
- -[WBTab deviceIdentifier]
- -[WBTab initWithTitle:url:deviceIdentifier:]
- -[WBTab initWithUUID:deviceIdentifier:]
- -[WBTab initWithUUID:deviceIdentifier:lastVisitTime:]
- -[WBTab initWithUUID:title:url:deviceIdentifier:]
- -[WBTab initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:]
- -[WBTab initWithUUID:title:url:deviceIdentifier:lastVisitTime:]
- -[WBTab initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:]
- -[WBTabGroup deviceIdentifier]
- -[WBTabGroup initWithDeviceIdentifier:]
- -[WBTabGroup initWithTitle:deviceIdentifier:]
- -[WBTabGroup initWithTitle:uuid:deviceIdentifier:]
- -[WBWindowState localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:]
- -[WebBookmark deviceIdentifier]
- -[WebBookmark initFolderWithParentID:deviceIdentifier:collectionType:]
- -[WebBookmark initFolderWithParentID:subtype:deviceIdentifier:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:deviceIdentifier:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:]
- -[WebBookmark initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:]
- -[WebBookmark setDeviceIdentifier:]
- -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:collectionType:]
- -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:]
- -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:]
- -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:].cold.1
- -[WebBookmark(Internal) initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:].cold.2
- _OBJC_IVAR_$_WBDeviceParameters._deviceIdentifier
- _OBJC_IVAR_$_WebBookmark._deviceIdentifier
- ___35-[WebBookmark setDeviceIdentifier:]_block_invoke
- ___78-[WebBookmarkCollection _saveBookmark:withSpecialID:updateGenerationIfNeeded:]_block_invoke.833
- ___Block_byref_object_copy_.1891
- ___Block_byref_object_dispose_.1892
- ____ZL33prefixEndingWithFirstWordOfStringP8NSString_block_invoke.1894
- ___block_descriptor_56_ea8_32s40s48s_e24_B24?0"WebBookmark"8q16ls32l8s40l8s48l8
- ___block_literal_global.1021
- ___block_literal_global.1064
- ___block_literal_global.1134
- ___block_literal_global.1144
- ___block_literal_global.1883
- ___block_literal_global.1889
- ___block_literal_global.1896
- ___block_literal_global.1910
- ___block_literal_global.215
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.321
- _objc_msgSend$initFolderWithParentID:deviceIdentifier:collectionType:
- _objc_msgSend$initFolderWithParentID:subtype:deviceIdentifier:collectionType:
- _objc_msgSend$initWithDeviceIdentifier:
- _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:collectionType:
- _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:
- _objc_msgSend$initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:
- _objc_msgSend$initWithTitle:address:parentID:deviceIdentifier:collectionType:
- _objc_msgSend$initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:
- _objc_msgSend$initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:
- _objc_msgSend$initWithTitle:deviceIdentifier:
- _objc_msgSend$initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:
- _objc_msgSend$initWithTitle:url:deviceIdentifier:
- _objc_msgSend$initWithTitle:uuid:deviceIdentifier:
- _objc_msgSend$initWithUUID:deviceIdentifier:
- _objc_msgSend$initWithUUID:title:url:deviceIdentifier:
- _objc_msgSend$initWithUUID:title:url:deviceIdentifier:lastVisitTime:
- _objc_msgSend$initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:
- _objc_msgSend$initWithValue:generation:deviceIdentifier:
- _objc_msgSend$initWithValueSource:valueProvider:valueUpdater:generation:deviceIdentifier:
- _objc_msgSend$localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:
- _objc_msgSend$localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:
- _objc_msgSend$setDeviceIdentifier:
- _objc_msgSend$startPageTabWithDeviceIdentifier:
- _objc_msgSend$unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:
CStrings:
+ "@32@0:8^{sqlite3_stmt=}16q24"
+ "@36@0:8^{sqlite3_stmt=}16q24B32"
+ "@36@0:8i16q20q28"
+ "@40@0:8^{sqlite3_stmt=}16B24q28B36"
+ "@48@0:8@16@24i32B36q40"
+ "@52@0:8@16@24i32q36q44"
+ "@60@0:8@16@24i32q36q44@52"
+ "@68@0:8@16@24@32B40@44@52@60"
+ "initFolderWithParentID:subtype:collectionType:"
+ "initWithSQLiteStatement:collectionType:"
+ "initWithSQLiteStatement:collectionType:skipDecodingSyncData:"
+ "initWithSQLiteStatement:hasIcon:collectionType:skipDecodingSyncData:"
+ "initWithTitle:"
+ "initWithTitle:address:parentID:folder:collectionType:"
+ "initWithTitle:address:parentID:subtype:collectionType:"
+ "initWithTitle:address:parentID:subtype:collectionType:score:"
+ "initWithTitle:profileIdentifier:"
+ "initWithTitle:symbolImageName:favoritesFolderServerID:"
+ "initWithTitle:url:"
+ "initWithTitle:uuid:"
+ "initWithUUID:lastVisitTime:"
+ "initWithUUID:title:url:"
+ "initWithUUID:title:url:isPrivateBrowsing:"
+ "initWithUUID:title:url:lastVisitTime:"
+ "initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:"
+ "initWithValue:generation:"
+ "initWithValueSource:valueProvider:valueUpdater:generation:"
+ "localDeviceWithTitle:creationDeviceIdentifier:"
+ "localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:"
+ "pinnedTabWithTitle:url:"
+ "remoteDeviceWithTitle:"
+ "startPageTab"
+ "unnamedTabGroup"
+ "unnamedTabGroupWithUUID:profileIdentifier:"
- "@36@0:8B16@20@28"
- "@36@0:8i16@20q28"
- "@40@0:8^{sqlite3_stmt=}16@24q32"
- "@44@0:8^{sqlite3_stmt=}16@24q32B40"
- "@44@0:8i16q20@28q36"
- "@48@0:8^{sqlite3_stmt=}16@24B32q36B44"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16@24i32@36q44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24i32B36@40q48"
- "@60@0:8@16@24i32q36@44q52"
- "@68@0:8@16@24i32q36@44q52@60"
- "@76@0:8@16@24@32B40@44@52@60@68"
- "T@\"NSString\",C,N,V_deviceIdentifier"
- "_deviceIdentifier"
- "initFolderWithParentID:deviceIdentifier:collectionType:"
- "initFolderWithParentID:subtype:deviceIdentifier:collectionType:"
- "initWithDeviceIdentifier:"
- "initWithSQLiteStatement:deviceIdentifier:collectionType:"
- "initWithSQLiteStatement:deviceIdentifier:collectionType:skipDecodingSyncData:"
- "initWithSQLiteStatement:deviceIdentifier:hasIcon:collectionType:skipDecodingSyncData:"
- "initWithTitle:address:parentID:deviceIdentifier:collectionType:"
- "initWithTitle:address:parentID:folder:deviceIdentifier:collectionType:"
- "initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:"
- "initWithTitle:address:parentID:subtype:deviceIdentifier:collectionType:score:"
- "initWithTitle:deviceIdentifier:"
- "initWithTitle:deviceIdentifier:profileIdentifier:"
- "initWithTitle:symbolImageName:favoritesFolderServerID:deviceIdentifier:"
- "initWithTitle:url:deviceIdentifier:"
- "initWithTitle:uuid:deviceIdentifier:"
- "initWithUUID:deviceIdentifier:"
- "initWithUUID:deviceIdentifier:lastVisitTime:"
- "initWithUUID:title:url:deviceIdentifier:"
- "initWithUUID:title:url:deviceIdentifier:isPrivateBrowsing:"
- "initWithUUID:title:url:deviceIdentifier:lastVisitTime:"
- "initWithUUID:title:url:pinned:pinnedTitle:pinnedURL:localAttributes:deviceIdentifier:"
- "initWithValue:generation:deviceIdentifier:"
- "initWithValueSource:valueProvider:valueUpdater:generation:deviceIdentifier:"
- "localDeviceWithTitle:creationDeviceIdentifier:deviceIdentifier:"
- "localOrUnnamedTabGroupForRestoration:inProfileWithIdentifier:deviceIdentifier:"
- "pinnedTabWithTitle:url:deviceIdentifier:"
- "remoteDeviceWithTitle:deviceIdentifier:"
- "setDeviceIdentifier:"
- "startPageTabWithDeviceIdentifier:"
- "unnamedTabGroupWithDeviceIdentifier:"
- "unnamedTabGroupWithUUID:profileIdentifier:deviceIdentifier:"
- "~DefaultProfileDeviceIdentifier-%@"

```
