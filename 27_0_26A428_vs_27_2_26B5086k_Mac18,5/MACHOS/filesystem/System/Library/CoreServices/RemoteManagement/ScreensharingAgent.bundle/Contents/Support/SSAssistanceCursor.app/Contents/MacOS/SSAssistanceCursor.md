## SSAssistanceCursor

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/Support/SSAssistanceCursor.app/Contents/MacOS/SSAssistanceCursor`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0xa7e4
-  __TEXT.__auth_stubs: 0x920
+766.5.0.0.0
+  __TEXT.__text: 0xad90
+  __TEXT.__auth_stubs: 0x970
   __TEXT.__objc_stubs: 0x2080
   __TEXT.__objc_methlist: 0xc6c
-  __TEXT.__const: 0xc8
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__cstring: 0x1705
+  __TEXT.__cstring: 0x1765
   __TEXT.__objc_methname: 0x2472
-  __TEXT.__oslogstring: 0x629
+  __TEXT.__oslogstring: 0x7f5
   __TEXT.__objc_classname: 0xcb
   __TEXT.__objc_methtype: 0x785
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__const: 0x2e8
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__auth_got: 0x4c8
   __DATA_CONST.__got: 0x1d0
   __DATA.__objc_const: 0x1340
   __DATA.__objc_selrefs: 0xae0
   __DATA.__objc_ivar: 0xe4
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x160
+  __DATA.__data: 0x170
   __DATA.__common: 0x1
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/Versions/A/PhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 247
-  Symbols:   215
-  CStrings:  718
+  Functions: 254
+  Symbols:   220
+  CStrings:  734
 
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
