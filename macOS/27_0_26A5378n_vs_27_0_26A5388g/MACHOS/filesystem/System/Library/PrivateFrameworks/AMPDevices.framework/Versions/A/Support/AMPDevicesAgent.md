## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/A/Support/AMPDevicesAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-1.7.0.137.0
-  __TEXT.__text: 0x66a700
+1.7.0.146.0
+  __TEXT.__text: 0x66a814
   __TEXT.__auth_stubs: 0x5910
   __TEXT.__objc_stubs: 0x8300
   __TEXT.__init_offsets: 0x90
   __TEXT.__objc_methlist: 0x1f34
   __TEXT.__const: 0x85b08
-  __TEXT.__gcc_except_tab: 0x2af4c
+  __TEXT.__gcc_except_tab: 0x2af60
   __TEXT.__cstring: 0x604b6
-  __TEXT.__oslogstring: 0x1c1ec
+  __TEXT.__oslogstring: 0x1c3df
   __TEXT.__objc_methname: 0x8e2b
   __TEXT.__objc_classname: 0x374
   __TEXT.__objc_methtype: 0x28fd
-  __TEXT.__unwind_info: 0x12108
+  __TEXT.__unwind_info: 0x12118
   __TEXT.__eh_frame: 0x1b0
   __DATA_CONST.__const: 0x54008
   __DATA_CONST.__cfstring: 0x13e00

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17932
+  Functions: 17934
   Symbols:   1940
-  CStrings:  19803
+  CStrings:  19814
 
CStrings:
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10536, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11356, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15700, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15758, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18083, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8482, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/Plugins.cpp\", 676, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "1.7.0.146"
+ "13.7.0.146"
+ "AMPDevicesAgent: 1.7.0.146"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YbLiBS/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
+ "setup> failed to delete FirstTime file (%d)"
+ "setup> failed to delete Licenses folder (%d)"
+ "setup> failed to delete ShowLicense file (%d)"
+ "setup> failed to delete ShowWarranty file (%d)"
+ "setup> failed to delete Warranty.html file (%d)"
+ "setup> failed to read license file (%d)"
+ "setup> found default license file"
+ "setup> found license file for locale \"%s\""
+ "setup> not using bundle license file for device class"
+ "setup> not using bundle license file for product version %u.%u.%u"
+ "setup> using bundle license file"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10536, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11356, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15700, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15758, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18083, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8482, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 676, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "1.7.0.137"
- "13.7.0.137"
- "AMPDevicesAgent: 1.7.0.137"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
```
