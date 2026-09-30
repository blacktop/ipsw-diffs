## SSPasteboardHelper

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/Support/SSPasteboardHelper.bundle/Contents/MacOS/SSPasteboardHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x59b8
-  __TEXT.__auth_stubs: 0x790
+766.5.0.0.0
+  __TEXT.__text: 0x63ec
+  __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x13c3
-  __TEXT.__oslogstring: 0x980
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x159c
+  __TEXT.__oslogstring: 0xcc4
   __TEXT.__objc_methname: 0xf8
   __TEXT.__objc_classname: 0x8
   __TEXT.__objc_methtype: 0x63
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__const: 0x80
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0x110
   __DATA.__objc_selrefs: 0x70
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x40
+  __DATA.__data: 0x50
   __DATA.__common: 0x1
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 79
-  Symbols:   147
-  CStrings:  179
+  Functions: 91
+  Symbols:   153
+  CStrings:  200
 
Symbols:
+ _bzero
+ _close
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
+ "socket"
+ "symlink"
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "uncompressed size = %ld (declared %u)"
+ "unknown"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
- "uncompressed size = %ld"
```
