## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-619.1.22.4.0
-  __TEXT.__text: 0x972b8
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x731c
+619.1.26.20.1
+  __TEXT.__text: 0x97f80
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x7364
   __TEXT.__const: 0x2b0
-  __TEXT.__gcc_except_tab: 0xa9bc
-  __TEXT.__cstring: 0xd322
-  __TEXT.__oslogstring: 0x6d39
+  __TEXT.__gcc_except_tab: 0xabe8
+  __TEXT.__cstring: 0xd5a7
+  __TEXT.__oslogstring: 0x6d82
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0x3f70
+  __TEXT.__unwind_info: 0x3fa0
   __TEXT.__objc_classname: 0x9a7
-  __TEXT.__objc_methname: 0x14e94
+  __TEXT.__objc_methname: 0x14ff0
   __TEXT.__objc_methtype: 0x26e7
-  __TEXT.__objc_stubs: 0xe600
+  __TEXT.__objc_stubs: 0xe740
   __DATA_CONST.__got: 0x780
-  __DATA_CONST.__const: 0x2be0
+  __DATA_CONST.__const: 0x2c28
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49a0
+  __DATA_CONST.__objc_selrefs: 0x49f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d0
-  __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0x10e0
-  __AUTH_CONST.__cfstring: 0x58e0
-  __AUTH_CONST.__objc_const: 0xb0b0
+  __DATA_CONST.__objc_arraydata: 0x350
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__cfstring: 0x5ec0
+  __AUTH_CONST.__objc_const: 0xb0e0
   __AUTH_CONST.__objc_intobj: 0x360
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x5d4
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __DATA.__objc_ivar: 0x5d8
   __DATA.__data: 0xd60
-  __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0x14a0
+  __DATA.__bss: 0xe8
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3371
-  Symbols:   4045
-  CStrings:  5295
+  Functions: 3379
+  Symbols:   4058
+  CStrings:  5355
 
Symbols:
+ _CGImageMetadataCopyTagWithPath
+ _CGImageMetadataTagCopyValue
+ _CGImageSourceCopyMetadataAtIndex
+ _CGImageSourceCreateWithURL
CStrings:
+ "DROP TABLE IF EXISTS %!@(MISSING)"
+ "Failed to copy the mobile asset background image over. Error: %!{(MISSING)public}@"
+ "FileName"
+ "PRAGMA secure_delete = ON"
+ "SELECT name FROM sqlite_master where type='table'"
+ "UPDATE %!@(MISSING) SET %!@(MISSING) = 'redacted'"
+ "URLByAppendingPathComponent:"
+ "UserHasSharedTabGroupsKey"
+ "WBSBackgroundImageMobileAssetDidInstallBackgroundImage"
+ "_installMobileAssetIfApplicableWithURL:"
+ "_setHasSharedTabGroups"
+ "_specialTabsWithUUID:privateBrowsing:"
+ "_userHasSharedTabGroups"
+ "active_profile_id"
+ "active_tab_group_id"
+ "ancestor_id"
+ "date_closed"
+ "device_identifier"
+ "external_uuid"
+ "folder_ancestor"
+ "folder_id"
+ "hidden_ancestor_count"
+ "id"
+ "initWithBookmark:isPrivateBrowsing:"
+ "is_last_session"
+ "key"
+ "keyEnumerator"
+ "last_modified"
+ "last_selected_child"
+ "local_tab_group_id"
+ "modified_attributes"
+ "num_children"
+ "order_index"
+ "parent"
+ "private_tab_group_id"
+ "profile_id"
+ "read"
+ "safari:fileName"
+ "safari_startPageBackgroundImageMobileAssetFolderURL"
+ "scene_id"
+ "select name from PRAGMA_TABLE_INFO('%!@(MISSING)')"
+ "server_id"
+ "setHasSharedTabGroups"
+ "setHasSharedTabGroupsWithCompletionHandler:"
+ "settings"
+ "special_id"
+ "sqlite_sequence"
+ "statement"
+ "stringAtIndex:"
+ "tab_group_id"
+ "userHasSharedTabGroups"
+ "window_id"
+ "windows"
+ "windows_profiles"
+ "windows_tab_groups"
+ "windows_unnamed_tab_groups"
- "ALTER TABLE bookmarks DROP COLUMN extra_attributes"
- "ALTER TABLE bookmarks DROP COLUMN title"
- "UPDATE bookmarks SET url = NULL"
- "UPDATE settings SET value = 'redacted'"
- "_specialTabsWithUUID:"

```
