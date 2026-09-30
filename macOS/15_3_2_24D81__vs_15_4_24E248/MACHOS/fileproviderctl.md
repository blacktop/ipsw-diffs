## fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

-2732.81.1.0.0
-  __TEXT.__text: 0xc968
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x1b20
+2882.101.2.0.0
+  __TEXT.__text: 0xdd10
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x1d20
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x458
-  __TEXT.__cstring: 0x1710
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x5b0
+  __TEXT.__cstring: 0x1a2a
   __TEXT.__ustring: 0x654
-  __TEXT.__oslogstring: 0xd3
+  __TEXT.__oslogstring: 0x146
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x1355
+  __TEXT.__objc_methname: 0x14ec
   __TEXT.__objc_methtype: 0x38
   __TEXT.__dlopen_cstrs: 0x53
-  __TEXT.__unwind_info: 0x340
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xd18
-  __DATA_CONST.__cfstring: 0x1440
+  __TEXT.__unwind_info: 0x388
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__cfstring: 0x1680
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x40
-  __DATA.__objc_selrefs: 0x6d0
+  __DATA.__objc_selrefs: 0x750
   __DATA.__common: 0x18
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
-  - /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs
   - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/SpaceAttribution.framework/Versions/A/SpaceAttribution
   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
-  - /usr/lib/libEndpointSecuritySystem.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 3E3972A8-5333-3765-9E0E-A36135BF654E
-  Functions: 181
-  Symbols:   156
-  CStrings:  580
+  UUID: 3CCB8D29-ED5F-3A41-BF0E-7B3586AC4784
+  Functions: 197
+  Symbols:   168
+  CStrings:  638
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_FPTask
+ _OBJC_CLASS_$_NSBundle
+ ___NSDictionary0__struct
+ __dispatch_queue_attr_concurrent
+ __os_log_debug_impl
+ _fp_shouldObfuscateFilenames
+ _fpfs_path_return_assigned_provider_domain_xattr
+ _fpfs_set_support_long_paths_iopolicy
+ _getxattr
+ _malloc_type_malloc
+ _objc_retainAutoreleaseReturnValue
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
+ "URLByAppendingPathComponent:"
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
