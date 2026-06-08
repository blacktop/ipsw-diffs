## SidebarFileDispatcherService

> `/System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/XPCServices/SidebarFileDispatcherService.xpc/SidebarFileDispatcherService`

```diff

-659.122.1.0.0
-  __TEXT.__text: 0x4044
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x25c
+835.0.0.0.0
+  __TEXT.__text: 0x1680
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x214
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x57a
-  __TEXT.__objc_methname: 0x571
-  __TEXT.__oslogstring: 0x750
-  __TEXT.__objc_classname: 0x8c
-  __TEXT.__objc_methtype: 0x20d
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x560
+  __TEXT.__cstring: 0x19e
+  __TEXT.__objc_methname: 0x4d8
+  __TEXT.__oslogstring: 0x432
+  __TEXT.__objc_classname: 0x8a
+  __TEXT.__objc_methtype: 0x190
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x4c8
-  __DATA.__objc_selrefs: 0x1f0
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x70
+  __DATA.__objc_const: 0x438
+  __DATA.__objc_selrefs: 0x1b8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73B8EC77-AB2F-3FE3-A159-9217F3748A12
-  Functions: 46
-  Symbols:   89
-  CStrings:  238
+  UUID: A87610BA-EA33-3310-86C9-FBAFE3423CDB
+  Functions: 32
+  Symbols:   84
+  CStrings:  138
 
Symbols:
+ _AppleNVMeSideBarGetErrorStringForStatus
+ _AppleNVMeSideBarNamespaceWrite
+ _SidebarFileDispatcherServiceErrorDomain
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x8
- _NSLocalizedFailureReasonErrorKey
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSString
- __os_log_debug_impl
- _bzero
- _fstat
- _ftruncate
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
- _qsort
- _write
CStrings:
+ "Failed to allocate buffer for sidebar send"
+ "Failed to read sidebar entries from file"
+ "Failed to read sidebar entries from file: read %zd of %llu bytes, error: %s"
+ "Failed to seek in sidebar buffer file"
+ "Failed to seek in sidebar buffer file: %s"
+ "Failed to write namespace data with API error: %u (%s)\n"
+ "Failed to write namespace data with NVMe error"
+ "Failed to write namespace data with NVMe error: 0x%x\n"
+ "IS_TEST_MODE_LEAKS enabled - sleeping for 10 seconds to allow leaks tool"
+ "Processing file handle fd: %d"
+ "Processing sidebar buffer: handle=%@, size=%llu, deviceID=%llu, lba=%llu"
+ "Sending a sidebar write with sbarLba=0x%llx, size=0x%llx, version=0x%x\n"
+ "SideBar buffer processing completed successfully"
+ "SideBar buffer processing failed: %{public}@"
+ "SidebarFileDispatcherService initialized with testModes=0x%x"
+ "SidebarFileDispatcherServiceErrorDomain"
+ "TI,N,V_testModes"
+ "_testModes"
+ "processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:"
+ "setTestModes:"
+ "testModes"
+ "v56@0:8@\"NSFileHandle\"16Q24Q32Q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16Q24Q32Q40@?48"
- "=== End of entries ==="
- "=== Purgeable File Entries: %u total ==="
- "Do not hang service, dTestModes=%u"
- "Empty file"
- "Empty file - no entries to print"
- "Entry %u: Range [0x%llx - 0x%llx], Size: %llu sectors"
- "Failed to allocate %zu bytes for %u entries"
- "Failed to allocate buffer for reading entries"
- "Failed to allocate buffer for sorting entries"
- "Failed to allocate buffer for today's entries"
- "Failed to get file statistics"
- "Failed to get file stats for sorting: %s"
- "Failed to get file stats: %s"
- "Failed to read entries"
- "Failed to read entries for sorting: %s"
- "Failed to read entries: %s"
- "Failed to read today's entries: %s"
- "Failed to read today's file"
- "Failed to read yesterday's entry"
- "Failed to seek to beginning"
- "Failed to seek to beginning for sorting: %s"
- "Failed to seek to beginning for writing sorted entries: %s"
- "Failed to seek to beginning of today's file: %s"
- "Failed to seek to beginning of yesterday's file: %s"
- "Failed to seek to beginning: %s"
- "Failed to truncate file"
- "Failed to truncate file to deduplicated size: %s"
- "Failed to write sorted entries"
- "Failed to write sorted entries: %s"
- "File seek failed"
- "File size %lld bytes exceeds %d byte limit"
- "File size (%lld bytes) does not contain complete entries"
- "Hang service, dTestModes=%u"
- "Invalid file handle"
- "Loaded %u today entries into memory (%zu bytes)"
- "Match purgeable positions completed successfully"
- "Match purgeable positions failed: %{public}@"
- "Match results: LBAs only in yesterday=%llu, only in today=%llu, in both=%llu"
- "Matching: today has %u entries, yesterday has %u entries"
- "Memory allocation failed"
- "No complete entries"
- "No complete entries in file"
- "One or both file descriptors are < 0"
- "One or both file handles are nil"
- "Overlapping entry detected! Previous: LBA=0x%llx size=%llu, Current: LBA=0x%llx size=%llu, Overlap: %llu sectors"
- "Print entries completed successfully"
- "Print entries failed: %{public}@"
- "Purgable processing completed successfully, status %d"
- "Purgable processing failed: %{public}@, status %d"
- "Sorted and removed overlapping entries: original=%u, unique=%u"
- "TI,N,V_dTestModes"
- "The file descriptor is < 0"
- "The file descriptor provided is <0"
- "The file descriptor provided is invalid"
- "The file handle provided is nil"
- "The purgeable file is empty with no entries to sort"
- "Today's file exceeds memory limit"
- "_dTestModes"
- "bytesExpected"
- "bytesRead"
- "bytesWritten"
- "com.sidebar.filedispatchererror"
- "dataWithBytes:length:"
- "errno"
- "fstat failed: %s"
- "ftruncate to %zu bytes failed: %s"
- "lseek failed: %s"
- "lseek on today's file failed: %s"
- "lseek on yesterday's file failed: %s"
- "lseek to beginning failed: %s"
- "lseek to beginning for write failed: %s"
- "matchPurgeablePositionsToday:yesterdayF:reply:"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithUnsignedLong:"
- "printPurgeableFileEntries:reply:"
- "read failed at index %u"
- "read failed: expected %zu bytes, got %zd: %s"
- "setDTestModes:"
- "sortAndDeduplicatePurgeableFile:reply:"
- "stringWithFormat:"
- "targetSize"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSFileHandle\"16@?<v@?IQ@\"NSData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@?0I8Q12@\"NSData\"20@\"NSError\"28"
- "v40@0:8@\"NSFileHandle\"16@\"NSFileHandle\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "write failed: expected %zu bytes, wrote %zd: %s"

```
