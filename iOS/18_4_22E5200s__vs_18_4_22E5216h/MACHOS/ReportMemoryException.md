## ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

-281.100.4.0.0
-  __TEXT.__text: 0x91b8
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x38
+281.100.5.0.0
+  __TEXT.__text: 0x800c
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x14
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0xab4
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__objc_methname: 0xb0a
-  __TEXT.__oslogstring: 0x194a
-  __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methtype: 0x4d
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x388
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x450
-  __DATA_CONST.__cfstring: 0xa00
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__cstring: 0xa16
+  __TEXT.__const: 0xd8
+  __TEXT.__objc_classname: 0xe
+  __TEXT.__objc_methtype: 0x31
+  __TEXT.__oslogstring: 0x195a
+  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__objc_methname: 0x9b9
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x148
-  __DATA.__objc_selrefs: 0x400
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x380
+  __DATA.__objc_data: 0x50
   __DATA.__data: 0x58
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x8
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 62
-  Symbols:   164
-  CStrings:  332
+  Functions: 48
+  Symbols:   159
+  CStrings:  304
 
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
- "\x01"
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
