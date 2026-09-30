## fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

-2732.80.49.0.0
-  __TEXT.__text: 0xbf0c
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x1c00
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__cstring: 0x18e8
+2882.100.413.0.0
+  __TEXT.__text: 0xcff0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x1de0
+  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x62c
+  __TEXT.__cstring: 0x1c02
   __TEXT.__ustring: 0x664
-  __TEXT.__oslogstring: 0xb6
+  __TEXT.__oslogstring: 0x129
   __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methname: 0x1637
+  __TEXT.__objc_methname: 0x17b1
   __TEXT.__objc_methtype: 0x174
   __TEXT.__dlopen_cstrs: 0x94
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xc40
-  __DATA_CONST.__cfstring: 0x1640
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0xdf8
+  __DATA_CONST.__cfstring: 0x1880
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_const: 0x280
+  __DATA.__objc_selrefs: 0x848
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
-  - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 162
-  Symbols:   196
-  CStrings:  501
+  Functions: 176
+  Symbols:   205
+  CStrings:  540
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_FPTask
+ _OBJC_CLASS_$_NSBundle
+ ___NSDictionary0__struct
+ __dispatch_queue_attr_concurrent
+ __os_log_debug_impl
+ _fp_shouldObfuscateFilenames
+ _fpfs_set_support_long_paths_iopolicy
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\nEvicted with clone: %{BOOL}d"
+ "%@. Aborting."
+ "%d (%s): %@"
+ ":"
+ "A file (not dir) already exists at %@."
+ "B:N"
+ "Can't create diagnose folder, error: %@.\n"
+ "Creating diagnose directory at %@.\n"
+ "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      -l, --limit-dump-size                                                 limit the number of items dumped\n  diagnose                                                       - dump state of fileprovider's daemon in several files \n      -l, --limit-dump-size                                                 limit the number of items dumped\n      -o, --output                                                          output path for the diagnose\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n      -x xpc|daemon                                                     launch in XPC Service vs daemon (default)\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"
+ "FileProvider"
+ "FileProviderDiagnose"
+ "Finished dump at %@\n"
+ "Getting domains found error %@.\n"
+ "Getting domains.\n"
+ "Unable to create file for domain dump"
+ "[DEBUG] Running from %@"
+ "[DEBUG] execv'ing to %s"
+ "[ERROR] failed to enable support for long paths in VFS: %{errno}d\n"
+ "_%d"
+ "_dump.log"
+ "concurrent_domain_dump_queue"
+ "connectionProxy"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "default"
+ "diagnose"
+ "dump_domains found error %@.\n"
+ "executablePath"
+ "fp_createPathIfNeeded:"
+ "fp_obfuscatedProviderDomainID"
+ "fp_prettyDescription"
+ "isEvictedWithClone"
+ "lIo:"
+ "mainBundle"
+ "no-background"
+ "pager"
+ "pathComponents"
+ "removeItemAtPath:error:"
+ "removeObjectAtIndex:"
+ "sanitizeStringForFilename:"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "stringByDeletingLastPathComponent"
+ "v32@?0Q8@\"NSURL\"16@\"NSError\"24"
+ "waitForStabilizationOfDomainWithID:mode:completionHandler:"
- "-"
- "B:"
- "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      --limit-dump-size                                                 limit the number of items dumped\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n      -x xpc|daemon                                                     launch in XPC Service vs daemon (default)\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"
- "no-pager"
- "waitForStabilizationOfDomainWithID:completionHandler:"

```
