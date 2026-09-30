## RFBEventHelperd

> `/System/Library/CoreServices/RFBEventHelper.bundle/Contents/MacOS/RFBEventHelperd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x7768
-  __TEXT.__auth_stubs: 0x910
+766.5.0.0.0
+  __TEXT.__text: 0x7d14
+  __TEXT.__auth_stubs: 0x970
   __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0xf60
-  __TEXT.__cstring: 0x1c3a
+  __TEXT.__oslogstring: 0x112c
+  __TEXT.__cstring: 0x1c9b
   __TEXT.__objc_methname: 0x97a
   __TEXT.__objc_classname: 0x51
   __TEXT.__objc_methtype: 0x2a3
-  __TEXT.__unwind_info: 0x298
-  __DATA_CONST.__const: 0x270
+  __TEXT.__unwind_info: 0x2b0
+  __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0x630
   __DATA.__objc_selrefs: 0x2e8
   __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x168
+  __DATA.__data: 0x178
   __DATA.__common: 0x1
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 160
-  Symbols:   175
-  CStrings:  377
+  Functions: 167
+  Symbols:   181
+  CStrings:  393
 
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
