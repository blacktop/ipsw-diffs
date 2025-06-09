## com.apple.DiagnosticExtensions.Panic

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Panic.appex/com.apple.DiagnosticExtensions.Panic`

```diff

-326.100.5.0.0
-  __TEXT.__text: 0x78c
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x5b
-  __TEXT.__oslogstring: 0x9e
+363.0.0.0.0
+  __TEXT.__text: 0x1388
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__const: 0x28
+  __TEXT.__cstring: 0x17c
+  __TEXT.__oslogstring: 0x394
   __TEXT.__objc_classname: 0x11
-  __TEXT.__objc_methname: 0x23b
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__cfstring: 0xc0
+  __TEXT.__objc_methname: 0x38a
+  __TEXT.__objc_methtype: 0x22
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80F2E266-1976-3F95-A3B4-C30A3171B9D7
-  Functions: 4
-  Symbols:   36
-  CStrings:  44
+  UUID: 92CB8A39-2CD6-3C79-9D45-79E5D6785060
+  Functions: 9
+  Symbols:   59
+  CStrings:  91
 
Symbols:
+ _OBJC_CLASS_$_DECollectionProgress
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSString
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __os_log_error_impl
+ _dispatch_once
+ _free
+ _malloc_type_malloc
+ _objc_alloc
+ _objc_alloc_init
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x8
+ _os_log_create
+ _sleep
+ _strtoull
+ _sysctlbyname
- _OBJC_CLASS_$_NSMutableString
- __os_log_default
- _objc_retain_x20
CStrings:
+ "(?:^|[ \t\r\n])%@=(0x[a-fA-F0-9]+|-?[0-9]+)(?:[ \t\r\n]|$)"
+ "-corefile_paths"
+ "/var/db/com.apple.DumpPanic.panicLogPathBreadcrumb"
+ "/var/run/com.apple.DumpPanic.finishedThisBoot"
+ "@32@0:8@16@?24"
+ "Attach corefile to TTR: %@"
+ "Attach paniclog to TTR: %@"
+ "Attach retired paniclog to TTR: %@"
+ "DumpPanic done cookie found"
+ "Failed to allocate memory for the boot-args"
+ "Failed to create a regex matching expression: %@"
+ "Failed to get data from DumpPanic breadcrumb, error: %@"
+ "Failed to get kern.bootsessionuuid"
+ "Failed to load data from DumpPanic breadcrumb, error: %@"
+ "Failed to parse the value of the '%@' boot-arg as an integer. Remainder = '%s'"
+ "Failed to query the boot-args. Error: %d"
+ "Failed to query the size of the boot-args. Error: %d"
+ "Got data from DumpPanic breadcrumb: %@"
+ "PanicDiagnosticExtension"
+ "Retired"
+ "The device is not configured to enable corefile dump, skip waiting..."
+ "Timeout to wait for corefile dumping"
+ "Timeout to wait for paniclog generation"
+ "UTF8String"
+ "Update Panic DE log collection progress to TTR: %f"
+ "attachmentWithPath:"
+ "attachmentsForParameters:withProgressHandler:"
+ "boot-args NVRAM variable does not have a '%@'=<value> arg"
+ "boot-args NVRAM variable is either not set or inaccessible"
+ "boot-args NVRAM variable is:%@"
+ "com.apple.DumpPanic"
+ "corefilesKey"
+ "dataWithContentsOfURL:options:error:"
+ "debug"
+ "defaultManager"
+ "fileExistsAtPath:"
+ "firstMatchInString:options:range:"
+ "getFilePathsFromBreadCrumbWithError:withProgressHandler:"
+ "initWithPercentComplete:"
+ "kern.bootargs"
+ "kern.bootsessionuuid"
+ "length"
+ "objectForKey:"
+ "paniclogKey"
+ "propertyListWithData:options:format:error:"
+ "rangeAtIndex:"
+ "readBreadCrumbWithError:"
+ "setObject:forKey:"
+ "stringByAppendingString:"
+ "stringByDeletingLastPathComponent"
+ "stringWithCString:encoding:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "substringWithRange:"
+ "v16@?0d8"
+ "v8@?0"
- ".core."
- "Found %lu coredumps, including all panic related files from : %@"
- "URLByAppendingPathExtension:"
- "URLByDeletingPathExtension"
- "Unable to find date in most recent filename (%@), including this coredump and associated log"
- "attachmentWithPathURL:"
- "attachmentsForParameters:"
- "characterAtIndex:"
- "count"
- "lastObject"
- "log"
- "path"
- "rangeOfString:"
- "stringWithString:"
- "substringToIndex:"

```
