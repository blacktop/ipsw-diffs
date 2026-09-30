## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

-276.0.0.0.0
-  __TEXT.__text: 0x9f8c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__cstring: 0xb66
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__objc_methname: 0xaac
-  __TEXT.__oslogstring: 0x1889
-  __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methtype: 0x4d
+281.100.5.0.0
+  __TEXT.__text: 0x8c34
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_stubs: 0xda0
+  __TEXT.__objc_methlist: 0x14
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x4c8
-  __DATA_CONST.__cfstring: 0x9e0
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__cstring: 0xac8
+  __TEXT.__const: 0xe0
+  __TEXT.__objc_classname: 0xe
+  __TEXT.__objc_methtype: 0x31
+  __TEXT.__oslogstring: 0x1899
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__objc_methname: 0x95b
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__cfstring: 0x960
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x3e8
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x368
+  __DATA.__objc_data: 0x50
   __DATA.__data: 0x58
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport

   - /usr/lib/libMemoryResourceException.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 68BD51BC-2706-3A4C-B59D-55827BD03024
-  Functions: 81
-  Symbols:   148
-  CStrings:  403
+  UUID: E3B9FCAC-4A2A-3B06-A2F9-35798B581310
+  Functions: 67
+  Symbols:   143
+  CStrings:  372
 
Symbols:
+ __os_log_fault_impl
+ _ffsctl
+ _open
- _CFRetain
- _CacheDeleteRegisterInfoCallbacks
- _NSFileTypeDirectory
- _dirstat_np
- _objc_msgSendSuper2
- _objc_opt_self
- _objc_storeStrong
- _strerror
CStrings:
+ "Error marking purgable via ffsctl for path %@ fd %i, error: %i"
+ "Error opening file to mark purgable for path %@"
+ "Marking purgable %@"
- ".cxx_destruct"
- "@\"NSString\""
- "@16@0:8"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_VOLUME"
- "Can purge %lu from %@"
- "Directory sizing for %@ failed with error %s"
- "RMECacheDeleter"
- "Removing applicable files older than %{public}@"
- "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
- "_"
- "_archivesDirectory"
- "com.apple.ReportMemoryException.CacheDelete"
- "dateWithTimeIntervalSinceNow:"
- "fileCreationDate"
- "fileSystemRepresentation"
- "fileType"
- "init"
- "initCacheEnumeratorWithVolume:"
- "keysSortedByValueUsingComparator:"
- "numberWithUnsignedInteger:"
- "path"
- "q24@?0@\"NSURL\"8@\"NSURL\"16"
- "rangeOfString:"
- "reverseObjectEnumerator"
- "sortUsingComparator:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringWithRange:"
- "v16@0:8"

```
