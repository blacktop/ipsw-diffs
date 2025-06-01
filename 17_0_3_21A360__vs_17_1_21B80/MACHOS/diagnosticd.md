## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1481.0.12.0.0
-  __TEXT.__text: 0x5a58
-  __TEXT.__auth_stubs: 0xca0
+1481.40.16.0.0
+  __TEXT.__text: 0x61a8
+  __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x450
-  __TEXT.__cstring: 0x123e
+  __TEXT.__cstring: 0x132d
   __TEXT.__objc_methname: 0x2e9
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0x50
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x658
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__auth_got: 0x698
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x570
+  __DATA_CONST.__const: 0x610
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__crash_info: 0x40
-  __DATA.__data: 0x194
-  __DATA.__bss: 0x180
+  __DATA.__os_assumes_log: 0x8
+  __DATA.__data: 0x1a4
+  __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8CA5FE1-EBCA-393C-977C-F6E38C7071F5
-  Functions: 63
-  Symbols:   247
-  CStrings:  292
+  UUID: 7DA3943D-40F8-38CD-91EC-4B11458DF341
+  Functions: 72
+  Symbols:   255
+  CStrings:  302
 
Symbols:
+ _asprintf
+ _dispatch_get_specific
+ _dispatch_once_f
+ _dispatch_queue_create_with_target$V2
+ _dispatch_queue_set_specific
+ _fchown
+ _getprogname
+ _lseek
+ _strnvis
+ _time
- __os_trace_uuiddb_path
- _strvis
CStrings:
+ "%F %T%z"
+ "%s %s[%d]: %s\n"
+ "%s/%s.0.log"
+ "%s/%s.1.log"
+ "/private/var/db/diagnostics"
+ "/private/var/db/uuidtext"
+ "BUG IN LIBTRACE: failed to create log file path"
+ "BUG IN LIBTRACE: failed to create queue target from subsystem"
+ "com.apple.%s.log"
+ "diagnosticd"

```
