## AMPDevicesAgent

> `/System/Library/PrivateFrameworks/AMPDevices.framework/Versions/Current/Support/AMPDevicesAgent`

```diff

-  __TEXT.__text: 0x66ab54
-  __TEXT.__auth_stubs: 0x5900
+  __TEXT.__text: 0x66a700
+  __TEXT.__auth_stubs: 0x5910
   __TEXT.__objc_stubs: 0x8300
   __TEXT.__init_offsets: 0x90
   __TEXT.__objc_methlist: 0x1f34
-  __TEXT.__const: 0x85a88
-  __TEXT.__gcc_except_tab: 0x2af48
-  __TEXT.__cstring: 0x60480
-  __TEXT.__oslogstring: 0x1c15f
+  __TEXT.__const: 0x85b08
+  __TEXT.__gcc_except_tab: 0x2af4c
+  __TEXT.__cstring: 0x604b6
+  __TEXT.__oslogstring: 0x1c1ec
   __TEXT.__objc_methname: 0x8e2b
   __TEXT.__objc_classname: 0x374
   __TEXT.__objc_methtype: 0x28fd
-  __TEXT.__unwind_info: 0x12100
+  __TEXT.__unwind_info: 0x12108
   __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__const: 0x53fe8
+  __DATA_CONST.__const: 0x54008
   __DATA_CONST.__cfstring: 0x13e00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x2c98
-  __DATA_CONST.__got: 0xea8
+  __DATA_CONST.__auth_got: 0x2ca0
+  __DATA_CONST.__got: 0xec8
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0x2268
   __DATA.__objc_selrefs: 0x2798

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17929
-  Symbols:   1939
-  CStrings:  22387
+  Functions: 17932
+  Symbols:   1940
+  CStrings:  22391
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
~ __DATA.__bss : content changed
Symbols:
+ _CFPropertyListIsValid
CStrings:
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10536, true)) )"
+ "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11356, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15700, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15758, true)) )"
+ "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18083, true)) )"
+ "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8482, true)) )"
+ "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 676, true))"
+ "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
+ "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
+ "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
+ "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
+ "1.7.0.137"
+ "13.7.0.137"
+ "AMPDevicesAgent: 1.7.0.137"
+ "CFPropertyListIsValid(inValue, kCFPropertyListBinaryFormat_v1_0)"
+ "cfError"
+ "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
+ "error creating property list data: %{public}@"
+ "error parsing plist data: %{public}@"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
+ "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.t7tjLQ/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"
+ "invalid persistent value for key \"%{public}@\": %{public}@"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 10536, true)) )"
- "( ((downloadManager) != __null) && (((downloadManager)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(downloadManager)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 11356, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15700, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 15758, true)) )"
- "( ((inDM) != __null) && (((inDM)->magic == 'down') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inDM)->magic == 'down'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 18083, true)) )"
- "( ((inWorkTaskInfo) != __null) && (((inWorkTaskInfo)->magic == 'dwti') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"(inWorkTaskInfo)->magic == 'dwti'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/DownloadManager.cpp\", 8482, true)) )"
- "((databaseData->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"databaseData->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/Plugins.cpp\", 676, true))"
- "((plugin->magic == 'db  ') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'db  '\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/Plugins.cpp\", 120, true))"
- "((plugin->magic == 'encd') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'encd'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/Plugins.cpp\", 103, true))"
- "((plugin->magic == 'plug') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"plugin->magic == 'plug'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/Application/Plugins.cpp\", 84, true))"
- "((stream->magic == 'strm') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"stream->magic == 'strm'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/Utilities/StreamUtilities.cpp\", 21, true))"
- "1.7.0.130"
- "13.7.0.130"
- "AMPDevicesAgent: 1.7.0.130"
- "cfError != nullptr"
- "clientRef != nullptr && ((clientRef->magic == 'clie') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"clientRef->magic == 'clie'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/iTunes/iPod/iPodSupport.cpp\", 1303, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/Utilities/StreamUtilities.cpp\", 2453, true))"
- "info != nullptr && ((info->magic == 'srai') ? true : HandleAssert(AssertCategory::None, \"Assertion failure (expected to be true)\", \"info->magic == 'srai'\", \"/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qeZmko/Sources/Devices/Utilities/StreamUtilities.cpp\", 752, true))"

```
