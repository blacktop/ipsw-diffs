## LockScreen

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/Support/LockScreen.app/Contents/MacOS/LockScreen`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x363c
-  __TEXT.__auth_stubs: 0x730
+766.5.0.0.0
+  __TEXT.__text: 0x3be8
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0xc46
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0xca6
   __TEXT.__objc_methname: 0xc71
-  __TEXT.__oslogstring: 0x433
+  __TEXT.__oslogstring: 0x5ff
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x626
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__const: 0x80
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x560
   __DATA.__objc_selrefs: 0x450
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x108
+  __DATA.__data: 0x118
   __DATA.__common: 0x1
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 54
-  Symbols:   150
-  CStrings:  331
+  Functions: 61
+  Symbols:   156
+  CStrings:  347
 
Symbols:
+ _bzero
+ _fstat
+ _lstat
+ _os_log_create
+ _pthread_once
+ _readlink
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
