## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent`

```diff

-1.5.4.70.0
-  __TEXT.__text: 0x686c0c
+1.5.5.20.0
+  __TEXT.__text: 0x687180
   __TEXT.__auth_stubs: 0x56b0
   __TEXT.__objc_stubs: 0x8220
   __TEXT.__init_offsets: 0x9c
   __TEXT.__objc_methlist: 0x1e1c
-  __TEXT.__const: 0x83568
-  __TEXT.__gcc_except_tab: 0x2d5a0
-  __TEXT.__cstring: 0x5fa54
-  __TEXT.__oslogstring: 0x1ad3f
+  __TEXT.__const: 0x838f8
+  __TEXT.__gcc_except_tab: 0x2d60c
+  __TEXT.__cstring: 0x5fa8a
+  __TEXT.__oslogstring: 0x1ad00
   __TEXT.__objc_classname: 0x355
   __TEXT.__objc_methname: 0x8c13
   __TEXT.__objc_methtype: 0x2a67
-  __TEXT.__unwind_info: 0x11c10
+  __TEXT.__unwind_info: 0x11c50
   __TEXT.__eh_frame: 0x1ec
   __DATA_CONST.__auth_got: 0x2b70
   __DATA_CONST.__got: 0xe28
   __DATA_CONST.__auth_ptr: 0x188
-  __DATA_CONST.__const: 0x579f0
+  __DATA_CONST.__const: 0x57b30
   __DATA_CONST.__cfstring: 0x13820
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x40

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17541
+  Functions: 17566
   Symbols:   1889
-  CStrings:  19639
+  CStrings:  19637
 
CStrings:
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10515, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11335, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15680, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15738, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18063, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8461, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "1.5.5"
+ "1.5.5.20"
+ "13.5.5"
+ "13.5.5.20"
+ "AMPDevicesAgent: 1.5.5.20"
+ "JRFileSpecIsValid(&promisedFileItem.sourceFileSpec)"
+ "assetIdentifier.IsValid()"
+ "assetPath.IsEmpty() == false"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1304, true))"
+ "completeFileName.IsEmpty() == false"
+ "folderPath[0] != 0"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
+ "not JRFileSpecIsValid(&promisedFileItem.sourceFileSpec)"
+ "not promisedFileItem.thumbnailData.IsValid()"
+ "promisedFileItem.assetPath.NotEmpty()"
+ "promisedFileItem.thumbnailData.IsValid()"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10500, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11320, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15665, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15723, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18048, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8446, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "1.5.4"
- "1.5.4.70"
- "13.5.4"
- "13.5.4.70"
- "AMPDevicesAgent: 1.5.4.70"
- "airtraffic> can't accept photo video \"%{public}s\" (%{public}s)"
- "assertUUIDITString.IsEmpty() == false"
- "assetPathITString.IsEmpty() == false"
- "assetPathString != nullptr"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1304, true))"
- "completeFileNameITString.IsEmpty() == false"
- "extensionUString[0] != 0"
- "folderPathUString[0] != 0"
- "iTunesPhotoSync"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
- "mthmb"
- "promisedFileItem.finalAssetPathString != nullptr"
- "workItem != nullptr"

```
