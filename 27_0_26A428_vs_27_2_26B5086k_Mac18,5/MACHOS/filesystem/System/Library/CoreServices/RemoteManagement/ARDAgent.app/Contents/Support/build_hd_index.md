## build_hd_index

> `/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Support/build_hd_index`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x7554
-  __TEXT.__auth_stubs: 0x770
+766.5.0.0.0
+  __TEXT.__text: 0x7b00
+  __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x204
-  __TEXT.__const: 0x19c8
+  __TEXT.__const: 0x19e8
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__cstring: 0x1e46
-  __TEXT.__oslogstring: 0x603
+  __TEXT.__cstring: 0x1e9e
+  __TEXT.__oslogstring: 0x7cf
   __TEXT.__objc_methname: 0x3b2
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0x142
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__const: 0x158
+  __TEXT.__unwind_info: 0x1f8
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x370
   __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x290
+  __DATA.__data: 0x2a0
   __DATA.__common: 0xfa9
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/Versions/A/DiagnosticLogCollection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 107
-  Symbols:   143
-  CStrings:  351
+  Functions: 114
+  Symbols:   146
+  CStrings:  366
 
Symbols:
+ _fstat
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
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
```
