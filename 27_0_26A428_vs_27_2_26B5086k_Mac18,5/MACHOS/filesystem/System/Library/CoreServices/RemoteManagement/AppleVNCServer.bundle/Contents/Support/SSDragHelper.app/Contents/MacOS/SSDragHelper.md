## SSDragHelper

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/SSDragHelper.app/Contents/MacOS/SSDragHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x9288
-  __TEXT.__auth_stubs: 0xc20
+766.5.0.0.0
+  __TEXT.__text: 0x9d74
+  __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_stubs: 0x480
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x70
+  __TEXT.__const: 0x90
   __TEXT.__objc_methname: 0x2e9
-  __TEXT.__oslogstring: 0x14c5
-  __TEXT.__cstring: 0x1eee
+  __TEXT.__oslogstring: 0x1853
+  __TEXT.__cstring: 0x2110
   __TEXT.__objc_classname: 0x8
   __TEXT.__objc_methtype: 0x63
-  __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__const: 0xc0
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x618
+  __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x110
   __DATA.__objc_selrefs: 0x140
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x58
+  __DATA.__data: 0x68
   __DATA.__common: 0x1
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 88
-  Symbols:   232
-  CStrings:  294
+  Functions: 102
+  Symbols:   236
+  CStrings:  317
 
Symbols:
+ _fstat
+ _lstat
+ _os_log_create
+ _pthread_once
+ _readlink
- _fchmod
CStrings:
+ " -> "
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
+ "logfile"
+ "not a regular file"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "scrap sizes out of range - %u / %u"
+ "socket"
+ "symlink"
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "unable to allocate memory for scrapBuf"
+ "uncompressed size = %ld (declared %u)"
+ "unknown"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
- "uncompressed size = %ld"
```
