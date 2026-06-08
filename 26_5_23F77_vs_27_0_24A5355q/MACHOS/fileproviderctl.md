## fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

-4018.120.24.0.0
-  __TEXT.__text: 0x105a8
-  __TEXT.__auth_stubs: 0xb90
+4780.0.0.502.1
+  __TEXT.__text: 0xff54
+  __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x344
-  __TEXT.__const: 0x2ca
-  __TEXT.__gcc_except_tab: 0x604
-  __TEXT.__cstring: 0x1d41
+  __TEXT.__const: 0x2da
+  __TEXT.__gcc_except_tab: 0x620
+  __TEXT.__cstring: 0x1dd1
   __TEXT.__ustring: 0x65c
   __TEXT.__oslogstring: 0x129
   __TEXT.__objc_methname: 0x1cfe

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0x468
   __TEXT.__eh_frame: 0x1d8
-  __DATA_CONST.__auth_got: 0x5d8
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0xff8
-  __DATA_CONST.__cfstring: 0x18e0
+  __DATA_CONST.__const: 0x1058
+  __DATA_CONST.__cfstring: 0x1900
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__auth_ptr: 0xe0
   __DATA.__objc_const: 0x828
   __DATA.__objc_selrefs: 0x968
   __DATA.__objc_ivar: 0xc

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 65BD0A6E-F7E9-3BBF-B3F8-AC6D561EEB64
-  Functions: 257
-  Symbols:   331
-  CStrings:  812
+  UUID: 16091643-A22B-3111-85C5-7E268BEB4E75
+  Functions: 252
+  Symbols:   343
+  CStrings:  819
 
Symbols:
+ _FPIsCiaoEnabled
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x9
+ _swift_bridgeObjectRetain
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _swift_retain
CStrings:
+ "B:N:M"
+ "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      -l, --limit-dump-size                                                 limit the number of items dumped\n  diagnose                                                       - dump state of fileprovider's daemon in several files \n      -l, --limit-dump-size                                                 limit the number of items dumped\n      -o, --output                                                          output path for the diagnose\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n      -x xpc|daemon                                                     launch in XPC Service (default) vs daemon\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"
+ "Usage: available options: all/no-background/no-downloads/no-uploads"
+ "all"
+ "no-downloads"
+ "no-uploads"
+ "option must be valid"
+ "stabilize-mode"
- "B:N"
- "File Provider control utility.\n%s <command> <options>\n\nCommands:\n  dump [<domain|provider>]                                       - dump state of fileprovider's daemon\n      -l, --limit-dump-size                                                 limit the number of items dumped\n  diagnose                                                       - dump state of fileprovider's daemon in several files \n      -l, --limit-dump-size                                                 limit the number of items dumped\n      -o, --output                                                          output path for the diagnose\n  evaluate <item>                                                - evaluate finder actions and decorations on item\n  evaluate <action> [<item>] <target item>                       - evaluate finder interactions\n  check | repair                                                 - run FPCK\n      -f                                                                perform a full dump (all items)\n      -a <path>                                                         perform check under path\n      -b <path>                                                         operate on an already created DB backup. If this is set you need to set -a to point to the domain root\n      -o <path>                                                         write output into file at path\n      -P                                                                no-pager output\n      -d                                                                dimisss low-importance invariants\n      -v                                                                print out files with broken invariants\n      -m [<providerDomainID>]                                           perform check on the d2d migration backup\n      -x xpc|daemon                                                     launch in XPC Service vs daemon (default)\n  obfuscate [<filename>/<path>...]                               - return the obfuscated form of the filename\n"

```
