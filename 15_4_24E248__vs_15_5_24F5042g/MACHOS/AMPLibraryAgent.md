## AMPLibraryAgent

> `/System/Library/PrivateFrameworks/AMPLibrary.framework/Versions/A/Support/AMPLibraryAgent`

```diff

-1.5.4.70.0
-  __TEXT.__text: 0x5c5ce0
+1.5.5.20.0
+  __TEXT.__text: 0x5c6690
   __TEXT.__auth_stubs: 0x3660
   __TEXT.__objc_stubs: 0x48e0
   __TEXT.__init_offsets: 0xd0
   __TEXT.__objc_methlist: 0x13dc
   __TEXT.__cstring: 0x41567
-  __TEXT.__const: 0x71098
-  __TEXT.__gcc_except_tab: 0x2f9bc
-  __TEXT.__oslogstring: 0x22faa
+  __TEXT.__const: 0x712d8
+  __TEXT.__gcc_except_tab: 0x2f9dc
+  __TEXT.__oslogstring: 0x2335e
   __TEXT.__objc_classname: 0x38e
   __TEXT.__objc_methname: 0x4f50
   __TEXT.__objc_methtype: 0x19f8
-  __TEXT.__unwind_info: 0x11468
+  __TEXT.__unwind_info: 0x11488
   __TEXT.__eh_frame: 0xcc
   __DATA_CONST.__auth_got: 0x1b40
   __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA_CONST.__const: 0x440e8
+  __DATA_CONST.__const: 0x441e8
   __DATA_CONST.__cfstring: 0x110a0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 16622
+  Functions: 16641
   Symbols:   1198
-  CStrings:  12725
+  CStrings:  12734
 
CStrings:
+ "%s/AMPLibraryAgent-1.5.5.20"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 10515, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 11335, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 15738, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 18063, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 8461, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 699, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 21, true))"
+ "**ERROR**: QueueCloudAddCommandDownloads - Attempting to download an artist is not support! artistPID:(%llu)!"
+ "**ERROR**: QueueCloudAddCommandDownloads - Bad ItemKind! cloudID:%{public}s pid:%llu"
+ "**ERROR**: QueueCloudAddCommandDownloads - FindAlbumByPersistentID(%llu) failed!"
+ "**ERROR**: QueueCloudAddCommandDownloads - FindPlaylistByPersistentID(%llu) failed!"
+ "**ERROR**: QueueCloudAddCommandDownloads - FindTrackInfoByPersistentID(%llu)! failed!"
+ "**ERROR**: QueueCloudItemRedownloads - Failed to find track instance for cloudID:%llu"
+ "**WARNING**: Unimplemented function \"%s\" at /AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Core/amplibraryd/amplibrarydStubs.cpp:%d"
+ "1.5.5"
+ "1.5.5.20"
+ "13.5.5.20"
+ "AMPLibraryAgent version: 1.5.5.20"
+ "cloud-edits> Warning: Failed to get update for album with storeCloudID:%{public}s, and failed to find that album in the library for that storeCloudID! cmdID:%llu"
+ "cloud-edits> Warning: Failed to get update for artist with storeCloudID:%{public}s, and failed to find that artist in the library for that storeCloudID! cmdID:%llu"
+ "cloud-edits> Warning: Failed to get update for playlist %{public}s with cloudID:%llu, but playlist is in the library. cmdID:%llu"
+ "cloud-edits> Warning: Failed to get update for playlist with cloudID:%llu, and failed to find that playlist in the library! cmdID:%llu"
+ "icml> Attempting to download %zu tracks post cloud syncing."
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 752, true))"
- "%s/AMPLibraryAgent-1.5.4.70"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 10500, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 11320, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 15723, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 18048, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/DownloadManager.cpp\", 8446, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 699, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 21, true))"
- "**ERROR**: Failed to find track instance for cloudID:%llu"
- "**WARNING**: Unimplemented function \"%s\" at /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Core/amplibraryd/amplibrarydStubs.cpp:%d"
- "1.5.4"
- "1.5.4.70"
- "13.5.4.70"
- "AMPLibraryAgent version: 1.5.4.70"
- "cloud-edits> Warning: Failed to get update for artist/album with storeCloudID:%{public}s, and failed to find that artist/album in the library for that storeCloudID! cmdID:%llu"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/AMPLibrary/Utilities/StreamUtilities.cpp\", 752, true))"

```
