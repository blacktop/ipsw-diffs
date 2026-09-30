## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent`

```diff

-1.5.0.141.0
-  __TEXT.__text: 0x69945c
+1.5.0.150.0
+  __TEXT.__text: 0x69672c
   __TEXT.__auth_stubs: 0x58b0
-  __TEXT.__objc_stubs: 0x8020
+  __TEXT.__objc_stubs: 0x8000
   __TEXT.__init_offsets: 0xa4
   __TEXT.__objc_methlist: 0x1500
-  __TEXT.__const: 0x82f90
-  __TEXT.__gcc_except_tab: 0x2d548
-  __TEXT.__cstring: 0x6182e
-  __TEXT.__oslogstring: 0x1aa06
+  __TEXT.__const: 0x82f10
+  __TEXT.__gcc_except_tab: 0x2d390
+  __TEXT.__cstring: 0x616ed
+  __TEXT.__oslogstring: 0x1aa51
   __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methname: 0x8b47
+  __TEXT.__objc_methname: 0x8ad3
   __TEXT.__objc_methtype: 0x2ab0
   __TEXT.__info_plist: 0x639
-  __TEXT.__unwind_info: 0x11f08
+  __TEXT.__unwind_info: 0x11eb0
   __TEXT.__eh_frame: 0x1ec
   __DATA_CONST.__auth_got: 0x2c70
   __DATA_CONST.__got: 0xe40
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA_CONST.__const: 0x53520
-  __DATA_CONST.__cfstring: 0x13f00
+  __DATA_CONST.__const: 0x53458
+  __DATA_CONST.__cfstring: 0x13ea0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x3320
+  __DATA.__objc_const: 0x32a0
   __DATA.__objc_selrefs: 0x25c8
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x13d8
   __DATA.__common: 0x3b20

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17812
+  Functions: 17798
   Symbols:   1926
-  CStrings:  16445
+  CStrings:  16435
 
CStrings:
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10501, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11321, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15686, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15744, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18069, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8447, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "1.5.0.150"
+ "13.5.0.150"
+ "AMPDevicesAgent: 1.5.0.150"
+ "PhotoImportOptions::UsePhotosApp(importOptions) || (imageAlbum->sourceID == 0 || imageAlbum->sourceID == sourceID)"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1305, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10501, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11321, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15686, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15744, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18069, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8447, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "1.5.0.141"
- "13.5.0.141"
- "AMPDevicesAgent: 1.5.0.141"
- "DataModelVersion.plist"
- "Database"
- "ITImageAlbumIsValid(projectImageAlbum)"
- "PhotoImportOptions::UseAperture(importOptions) || PhotoImportOptions::UsePhotosApp(importOptions) || (imageAlbum->sourceID == 0 || imageAlbum->sourceID == sourceID)"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1305, true))"
- "com.apple.Aperture"
- "com.apple.iPhoto"
- "databaseUuid"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "isIPhotoApertureMigrated"
- "outMediaSource != nullptr"
- "projectImageAlbum->albumKind == kITImageAlbumKind_ApertureProject"
- "spIPhotoApertureLibraryUUID.get()"

```
