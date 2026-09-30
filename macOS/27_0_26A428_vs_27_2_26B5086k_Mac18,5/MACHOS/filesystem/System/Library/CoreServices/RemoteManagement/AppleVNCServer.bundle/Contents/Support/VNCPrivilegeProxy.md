## VNCPrivilegeProxy

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/VNCPrivilegeProxy`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x2ac8
-  __TEXT.__auth_stubs: 0x5c0
+766.5.0.0.0
+  __TEXT.__text: 0x30a8
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__const: 0x11d8
-  __TEXT.__oslogstring: 0x20c
-  __TEXT.__cstring: 0xa56
+  __TEXT.__const: 0x11f8
+  __TEXT.__oslogstring: 0x3d8
+  __TEXT.__cstring: 0xaaa
   __TEXT.__objc_methname: 0x59
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x58
   __DATA.__objc_selrefs: 0x28
-  __DATA.__data: 0x80
+  __DATA.__data: 0x90
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/Versions/A/DiagnosticLogCollection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 43
-  Symbols:   107
-  CStrings:  83
+  Functions: 51
+  Symbols:   112
+  CStrings:  99
 
Symbols:
+ _bzero
+ _fstat
+ _lstat
+ _os_log_create
+ _pthread_once
+ _readlink
- _fchmod
CStrings:
+ " -> "
+ "CheckEntitlement"
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
- "CheckScreenSharingEntitlement"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
```
