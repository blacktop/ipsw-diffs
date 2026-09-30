## ScreensharingAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/MacOS/ScreensharingAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x4a5ac
-  __TEXT.__auth_stubs: 0x1b90
+766.5.0.0.0
+  __TEXT.__text: 0x4b020
+  __TEXT.__auth_stubs: 0x1bc0
   __TEXT.__objc_stubs: 0x2ac0
   __TEXT.__objc_methlist: 0xea8
-  __TEXT.__const: 0x6da
-  __TEXT.__oslogstring: 0x8dcc
-  __TEXT.__cstring: 0x16380
+  __TEXT.__const: 0x700
+  __TEXT.__oslogstring: 0x9129
+  __TEXT.__cstring: 0x165a7
   __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__objc_methname: 0x2fe5
   __TEXT.__objc_classname: 0x1a1
   __TEXT.__objc_methtype: 0xa3c
-  __TEXT.__unwind_info: 0xd58
-  __DATA_CONST.__const: 0x13b8
+  __TEXT.__unwind_info: 0xd90
+  __DATA_CONST.__const: 0x1418
   __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0xdd8
+  __DATA_CONST.__auth_got: 0xdf0
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x14c0
   __DATA.__objc_selrefs: 0xda0
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x3328
+  __DATA.__data: 0x3338
   __DATA.__common: 0x2645
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 910
-  Symbols:   566
-  CStrings:  2300
+  Functions: 924
+  Symbols:   569
+  CStrings:  2323
 
Symbols:
+ _lstat
+ _os_log_create
+ _pthread_once
+ _readlink
- _fchmod
CStrings:
+ " -> "
+ "CheckEntitlement"
+ "Clipboard: %u unconsumed bytes after a complete inflate stream (trailing data in compressed payload)"
+ "Clipboard: declared uncompressed size %u but inflated %ld"
+ "Clipboard: declared uncompressed size %u exceeds maximum %u"
+ "Clipboard: declared uncompressed size %u too small, %u input bytes unconsumed"
+ "Clipboard: inflate error %d"
+ "Clipboard: inflate init error %d"
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "block device"
+ "character device"
+ "could not open the log"
+ "directory"
+ "fifo"
+ "invalid drag sizes %u %u"
+ "logfile"
+ "not a regular file"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "socket"
+ "symlink"
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "uncompressed size = %ld (declared %u)"
+ "unknown"
- "CheckScreenSharingEntitlement"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "uncompressed size = %ld"
```
