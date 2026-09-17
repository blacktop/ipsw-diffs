## SSInvitationAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/Support/SSInvitationAgent.app/Contents/MacOS/SSInvitationAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x477ec
-  __TEXT.__auth_stubs: 0x1350
+766.5.0.0.0
+  __TEXT.__text: 0x47d98
+  __TEXT.__auth_stubs: 0x1380
   __TEXT.__objc_stubs: 0x8080
   __TEXT.__objc_methlist: 0x37f0
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xd8f0
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0xd948
   __TEXT.__objc_methname: 0xad7a
-  __TEXT.__oslogstring: 0x5a95
+  __TEXT.__oslogstring: 0x5c61
   __TEXT.__objc_classname: 0x43d
   __TEXT.__objc_methtype: 0x20b7
   __TEXT.__gcc_except_tab: 0x6c0
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0xe38
-  __DATA_CONST.__const: 0x8a8
+  __TEXT.__unwind_info: 0xe50
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__cfstring: 0x3640
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__auth_got: 0x9d0
   __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x4448
   __DATA.__objc_selrefs: 0x2c40
   __DATA.__objc_ivar: 0x348
   __DATA.__objc_data: 0x7d0
-  __DATA.__data: 0x898
+  __DATA.__data: 0x8a8
   __DATA.__common: 0x9
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1215
-  Symbols:   559
-  CStrings:  3730
+  Functions: 1222
+  Symbols:   562
+  CStrings:  3744
 
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
+ "symlink"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
```
