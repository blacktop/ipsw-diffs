## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-622.1.19.10.4
-  __TEXT.__text: 0xa0bb8
+622.1.21.10.3
+  __TEXT.__text: 0xa0ddc
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_methlist: 0x83b4
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0xb294
+  __TEXT.__gcc_except_tab: 0xb2d8
   __TEXT.__cstring: 0xe06c
-  __TEXT.__oslogstring: 0x82d7
+  __TEXT.__oslogstring: 0x840c
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C15377F-63A8-3798-B7A4-3E2534AADD1F
+  UUID: 1FEF045C-B1A2-3EDA-B344-3882AD66C927
   Functions: 3561
   Symbols:   12173
-  CStrings:  6314
+  CStrings:  6317
 
Functions:
~ -[WebBookmarkCollection _moveBookmark:fromIndex:toIndex:] : 660 -> 1068
~ -[WBTabGroupManager _addTabsInTabGroups:toParentIdentifierInTabsToParentIdentifiersDictionary:] : 588 -> 584
~ -[WBTabGroupManager _updateTabsAndCacheTabGroup:withTabsByParentIdentifiers:creatorDeviceUUID:] : 360 -> 504
CStrings:
+ "Failed to update bookmarks order for bookmark %{public}@ where toIndex = (%d) and currentRecordGeneration = (%d) with error = (%@)"
+ "Failed to update siblings for bookmark %{public}@ where parentID = (%d), fromIndex = (%d), and toIndex = (%d) with error = %@"
+ "Updating tabGroup %{public}@ with an empty tab list"

```
