## SSFileCopySender

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopySender.bundle/Contents/MacOS/SSFileCopySender`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x6f80
-  __TEXT.__auth_stubs: 0x720
+766.5.0.0.0
+  __TEXT.__text: 0x752c
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x1b03
-  __TEXT.__oslogstring: 0xb36
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x1b64
+  __TEXT.__oslogstring: 0xd02
   __TEXT.__objc_methname: 0x250
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0xa6
-  __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__const: 0x268
+  __TEXT.__unwind_info: 0x210
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__auth_got: 0x3c0
   __DATA_CONST.__got: 0x98
   __DATA.__objc_const: 0x1e8
   __DATA.__objc_selrefs: 0xf0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x40
+  __DATA.__data: 0x50
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 106
-  Symbols:   141
-  CStrings:  297
+  Functions: 113
+  Symbols:   146
+  CStrings:  313
 
Symbols:
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
