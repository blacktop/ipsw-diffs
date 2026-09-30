## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-97.0.0.0.0
-  __TEXT.__text: 0x204b4
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0xb8c
-  __TEXT.__cstring: 0x662a
+103.40.3.0.0
+  __TEXT.__text: 0x21388
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_stubs: 0x2140
+  __TEXT.__objc_methlist: 0xba4
+  __TEXT.__cstring: 0x67a0
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x22b8
-  __TEXT.__oslogstring: 0x2fbf
+  __TEXT.__objc_methname: 0x2348
+  __TEXT.__oslogstring: 0x30ec
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x4d7
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__unwind_info: 0x608
-  __DATA_CONST.__auth_got: 0x730
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x620
+  __DATA_CONST.__auth_got: 0x750
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xba8
-  __DATA_CONST.__cfstring: 0x22a0
+  __DATA_CONST.__const: 0xbd0
+  __DATA_CONST.__cfstring: 0x2300
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1370
-  __DATA.__objc_selrefs: 0xa10
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_const: 0x13a0
+  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x220
   __DATA.__bss: 0x1e0

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
+  - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip
   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82AEFB03-E221-3DC1-90A7-C342AC54C20B
-  Functions: 625
-  Symbols:   290
-  CStrings:  1688
+  UUID: DE5A6D6C-EC25-3F20-BBE9-D1A72FF0809C
+  Functions: 643
+  Symbols:   301
+  CStrings:  1718
 
Symbols:
+ _OBJC_CLASS_$_NSDateFormatter
+ _OSLogCreateArchive
+ _SZArchiverCreateStreamableZip
+ _fclose
+ _fopen
+ _kSZArchiverCompressionOptionTryRecompress
+ _kSZArchiverOptionCompressionOptions
+ _kSZArchiverOptionNoCache
+ _kSZArchiverOptionSkipPrescan
+ _kSZArchiverOptionUncompressBloatedFiles
+ _kSZArchiverOptionZlibCompressionLevel
CStrings:
+ "%@/Controller/NeRD/DRE-%@.logarchive"
+ "%{public}s: Error saving logarchive to '%{public}@': %{public}s"
+ "%{public}s: Error saving system logs to '%{public}@': %ul"
+ "%{public}s: Failed to compress logarchive: %{public}@ -> %{public}@"
+ "%{public}s: Failed to remove logarchive '%{public}@': %{public}@"
+ "%{public}s: Saving logarchive to '%{public}@'"
+ "-[DeviceRecoveryService saveSystemLogs]"
+ "-[DeviceRecoveryService saveSystemLogs]_block_invoke"
+ "22:12:17"
+ "Sep 28 2025"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_osaQueue"
+ "Unable to create osa dispatch_queue"
+ "_osaQueue"
+ "_osaQueue != NULL"
+ "com.apple.DeviceRecoveryService.OSAQueue"
+ "compressedLogarchiveFile != NULL"
+ "compressedLogarchivePath != nil"
+ "dd-MM-yyyy-hh-mm-ss"
+ "formatter != nil"
+ "logarchivePath != nil"
+ "osaQueue"
+ "saveSystemLogs"
+ "setDateFormat:"
+ "stringByAppendingPathExtension:"
+ "stringFromDate:"
+ "success"
+ "v16@?0r*8"
+ "w+"
+ "zip"
+ "\xa1"
- "20:48:27"
- "Sep 11 2025"
- "\x91"

```
