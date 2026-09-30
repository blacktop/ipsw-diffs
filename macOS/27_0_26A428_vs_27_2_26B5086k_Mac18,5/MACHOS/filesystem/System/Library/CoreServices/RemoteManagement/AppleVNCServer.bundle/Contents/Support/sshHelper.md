## sshHelper

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/sshHelper`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x1120
-  __TEXT.__auth_stubs: 0x400
+766.5.0.0.0
+  __TEXT.__text: 0x16cc
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_stubs: 0x60
-  __TEXT.__cstring: 0x5ab
-  __TEXT.__oslogstring: 0x8d
-  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x60c
+  __TEXT.__oslogstring: 0x259
+  __TEXT.__const: 0x28
   __TEXT.__objc_methname: 0x42
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__const: 0x40
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x48
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x40
+  __DATA.__data: 0x50
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/Versions/A/DiagnosticLogCollection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14
-  Symbols:   77
-  CStrings:  55
+  Functions: 21
+  Symbols:   83
+  CStrings:  71
 
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
+ "unknown"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
```
