## ARDAgent

> `/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0xa08ac
-  __TEXT.__auth_stubs: 0x2860
+766.5.0.0.0
+  __TEXT.__text: 0xa0abc
+  __TEXT.__auth_stubs: 0x2880
   __TEXT.__objc_stubs: 0x2a80
   __TEXT.__objc_methlist: 0xf00
-  __TEXT.__const: 0x1018
-  __TEXT.__oslogstring: 0x6fe5
-  __TEXT.__cstring: 0x22cb5
+  __TEXT.__const: 0x1038
+  __TEXT.__oslogstring: 0x71b1
+  __TEXT.__cstring: 0x22d82
   __TEXT.__objc_methname: 0x2883
   __TEXT.__objc_classname: 0x17f
   __TEXT.__objc_methtype: 0x972
-  __TEXT.__unwind_info: 0x1768
-  __DATA_CONST.__const: 0x938
+  __TEXT.__unwind_info: 0x1780
+  __DATA_CONST.__const: 0x998
   __DATA_CONST.__cfstring: 0x3980
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x1438
+  __DATA_CONST.__auth_got: 0x1448
   __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x1440
   __DATA.__objc_selrefs: 0xd40
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x3d8
+  __DATA.__data: 0x3e8
   __DATA.__common: 0xd7ed
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libpcre2-8.0.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1527
-  Symbols:   813
-  CStrings:  4490
+  Functions: 1534
+  Symbols:   815
+  CStrings:  4506
 
Symbols:
+ _os_log_create
+ _pthread_once
CStrings:
+ " -> "
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "block device"
+ "character device"
+ "could not open the log"
+ "declared uncompressed size %u but inflated %u - rejecting"
+ "directory"
+ "fifo"
+ "logfile"
+ "not a regular file"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "socket"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
```
