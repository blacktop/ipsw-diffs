## MusicUI

> `/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI`

```diff

-4024.300.16.0.0
-  __TEXT.__text: 0xced02c
-  __TEXT.__auth_stubs: 0x9e60
+4024.300.28.0.0
+  __TEXT.__text: 0xcfa98c
+  __TEXT.__auth_stubs: 0xa010
   __TEXT.__objc_methlist: 0x1030
-  __TEXT.__const: 0x46234
+  __TEXT.__const: 0x465d4
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0xff06
+  __TEXT.__cstring: 0x1003b
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x17f84
-  __TEXT.__swift5_typeref: 0x600ca
-  __TEXT.__swift5_builtin: 0x3e8
-  __TEXT.__swift5_reflstr: 0x15fdb
-  __TEXT.__swift5_fieldmd: 0x153e8
-  __TEXT.__swift5_assocty: 0x6078
-  __TEXT.__swift5_proto: 0x316c
-  __TEXT.__swift5_types: 0x17d0
-  __TEXT.__oslogstring: 0x6cf7
-  __TEXT.__swift5_capture: 0x69b8
+  __TEXT.__constg_swiftt: 0x1802c
+  __TEXT.__swift5_typeref: 0x6039a
+  __TEXT.__swift5_builtin: 0x3fc
+  __TEXT.__swift5_reflstr: 0x1607b
+  __TEXT.__swift5_fieldmd: 0x15444
+  __TEXT.__swift5_assocty: 0x60d8
+  __TEXT.__swift5_proto: 0x3194
+  __TEXT.__swift5_types: 0x17d8
+  __TEXT.__oslogstring: 0x6dc7
+  __TEXT.__swift5_capture: 0x6b54
   __TEXT.__swift5_protos: 0x180
   __TEXT.__swift5_mpenum: 0x148
-  __TEXT.__unwind_info: 0x1a820
-  __TEXT.__eh_frame: 0x20764
+  __TEXT.__unwind_info: 0x1a770
+  __TEXT.__eh_frame: 0x21454
   __TEXT.__objc_classname: 0x488
-  __TEXT.__objc_methname: 0x5e06
+  __TEXT.__objc_methname: 0x5e33
   __TEXT.__objc_methtype: 0x1f38
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x2c40
+  __DATA_CONST.__got: 0x2cd8
   __DATA_CONST.__const: 0x3f8
-  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1890
+  __DATA_CONST.__objc_selrefs: 0x1898
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __AUTH_CONST.__auth_got: 0x4f40
-  __AUTH_CONST.__auth_ptr: 0x7a00
-  __AUTH_CONST.__const: 0x2b8e8
+  __AUTH_CONST.__auth_got: 0x5018
+  __AUTH_CONST.__auth_ptr: 0x6568
+  __AUTH_CONST.__const: 0x2bb08
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x13c00
-  __AUTH.__objc_data: 0x21f8
-  __AUTH.__data: 0x97d0
-  __DATA.__data: 0x155e0
-  __DATA.__bss: 0x41ea0
-  __DATA.__common: 0x4b0
-  __DATA_DIRTY.__objc_data: 0x20e8
-  __DATA_DIRTY.__data: 0x19e70
-  __DATA_DIRTY.__bss: 0x1b780
+  __AUTH_CONST.__objc_const: 0x13940
+  __AUTH.__objc_data: 0x21a8
+  __AUTH.__data: 0x90d8
+  __DATA.__data: 0x14e30
+  __DATA.__bss: 0x40b58
+  __DATA.__common: 0x460
+  __DATA_DIRTY.__objc_data: 0x20f0
+  __DATA_DIRTY.__data: 0x1ade0
+  __DATA_DIRTY.__bss: 0x1d000
   __DATA_DIRTY.__common: 0x338
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 40455
-  Symbols:   10041
-  CStrings:  3712
+  Functions: 40661
+  Symbols:   10124
+  CStrings:  3736
 
Symbols:
+ _NSFileSize
+ _NSUbiquitousKeyValueStoreChangedKeysKey
+ _NSUbiquitousKeyValueStoreDidChangeExternallyNotification
+ __availability_version_check
+ _dispatch_once_f
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _rewind
+ _sscanf
CStrings:
+ "\nWHERE\n   intent = "
+ "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
+ ",\n   app_state = "
+ ",\n   music_items = "
+ ",\n   page_data = "
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "Awaiting for the objectGraph…"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "CREATE TABLE IF NOT EXISTS pages (\n    intent TEXT NOT NULL PRIMARY KEY,\n    page_version_uuid TEXT NOT NULL,\n    ttl REAL NOT NULL,\n    app_state TEXT NOT NULL,\n    page_data TEXT NOT NULL,\n    music_items TEXT NOT NULL)"
+ "Cache HIT for intent kind %!s(MISSING)"
+ "Cache MISS for intent kind %!s(MISSING)"
+ "Cache entry INVALID: CachePolicy.ExpireDate passed (%!s(MISSING) > %!s(MISSING))"
+ "Calling `selectedTabDidChange` to %!{(MISSING)public}s on the publisher."
+ "Cannot insert entry for intent: %!s(MISSING) with id: %!s(MISSING), missing expiration date"
+ "DROP TABLE IF EXISTS pages"
+ "Database ERROR fetching for intent kind: %!s(MISSING)"
+ "Dropping out of date table with version %!l(MISSING)d"
+ "ERROR attempting to remove all database files during init"
+ "ERROR removing expired model cache entries"
+ "Evicting cached entry for intent kind %!s(MISSING)"
+ "Failed to find mapped item %!s(MISSING)"
+ "INSERT INTO pages (intent, page_version_uuid, ttl, app_state, page_data, music_items)\nVALUES ("
+ "Inserted entry for intent: %!s(MISSING) with id: %!s(MISSING)"
+ "Map.CacheResponse"
+ "Notifying of tab changed to %!{(MISSING)public}s"
+ "ProductVersion"
+ "Received `onSelectedTabChanged` to %!{(MISSING)public}s"
+ "Removing all entries file size has reached max size."
+ "SELECT *\nFROM pages\nWHERE page_version_uuid = "
+ "SELECT page_version_uuid, ttl, app_state, page_data, music_items\nFROM pages\nWHERE intent = "
+ "TabChangePublisher"
+ "UPDATE\n   pages\nSET\n   page_version_uuid ="
+ "attributesOfItemAtPath:error:"
+ "displayScale"
+ "forceModelCache"
+ "issuingIntent"
+ "kCFAllocatorNull"
+ "kvsDidChangeObserver"
+ "observeKVSChanges()"
+ "presentingWindow"
+ "r"
+ "💬 %!s(MISSING)"
+ "💬 %!s(MISSING) Key '%!s(MISSING)' has changed"
+ "💬 %!s(MISSING) Unknown key %!s(MISSING)"
- "\n  WHERE\n    page_version_uuid = "
- "  UPDATE\n    pages\n  SET\n    page_version_uuid = "
- ",\n    app_state = "
- ",\n    page_data = "
- "CREATE TABLE IF NOT EXISTS pages (\n    intent TEXT NOT NULL PRIMARY KEY,\n    page_version_uuid TEXT NOT NULL,\n    ttl REAL NOT NULL,\n    app_state TEXT NOT NULL,\n    page_data TEXT NOT NULL)"
- "Cache HIT for intent %!{(MISSING)public}s:  kind %!{(MISSING)public}s"
- "Cache MISS for intent %!{(MISSING)public}s:  kind %!{(MISSING)public}s"
- "Cache entry INVALID: TTL Expired (%!{(MISSING)public}s > %!{(MISSING)public}s"
- "Cannot insert entry for intent: %!{(MISSING)public}s with id: %!{(MISSING)public}s, missing expiration date"
- "Cannot update entry for page with id: %!{(MISSING)public}s, missing expiration date"
- "Database ERROR fetching for intent: %!{(MISSING)public}s  kind: %!{(MISSING)public}s"
- "Database ERROR updating page with id: %!{(MISSING)public}s"
- "ERROR importing SOD data"
- "Evicting cached entry for intent %!{(MISSING)public}s: kind %!{(MISSING)public}s"
- "INSERT INTO pages (intent, page_version_uuid, ttl, app_state, page_data)\nVALUES ("
- "Importing SOD data for page with id: %!{(MISSING)public}s"
- "SELECT page_version_uuid, ttl, app_state, page_data\nFROM pages"
- "SELECT page_version_uuid, ttl, app_state, page_data\nFROM pages\nWHERE intent = "
- "_TtC7MusicUI21NetworkResponseBuffer"
- "_TtC7MusicUI22UserSocialProfileGraph"
- "_TtC7MusicUI27UserSocialProfileDescriptor"
- "artworkCatalog"
- "currentIndex"
- "entries"
- "followees"
- "followers"
- "isOnboarded"
- "rawMAPIResponses"

```
