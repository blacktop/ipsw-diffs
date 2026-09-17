## SSFileCopyReceiver

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopyReceiver.bundle/Contents/MacOS/SSFileCopyReceiver`

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
-  __TEXT.__text: 0x8618
-  __TEXT.__auth_stubs: 0x800
+766.5.0.0.0
+  __TEXT.__text: 0x9548
+  __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1b24
-  __TEXT.__oslogstring: 0xacb
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x1d65
+  __TEXT.__oslogstring: 0xe53
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__objc_methname: 0x1a7
   __TEXT.__objc_classname: 0x8
   __TEXT.__objc_methtype: 0x63
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__const: 0x158
+  __TEXT.__unwind_info: 0x1d8
+  __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x410
+  __DATA_CONST.__auth_got: 0x430
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x110
   __DATA.__objc_selrefs: 0xc0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x48
+  __DATA.__data: 0x58
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 70
-  Symbols:   160
-  CStrings:  295
+  Functions: 91
+  Symbols:   164
+  CStrings:  325
 
Symbols:
+ _close
+ _fstat
+ _os_log_create
+ _pthread_once
+ _strnlen
- _fchmod
CStrings:
+ " -> "
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "alt local name is not terminated"
+ "block device"
+ "character device"
+ "could not open the log"
+ "destination path is not terminated"
+ "destination path too long"
+ "destination path too long %u"
+ "directory"
+ "expanded destination path is too long %u %u"
+ "fifo"
+ "g->newItemMsg.level = %d itemName = %s from packet %.*s"
+ "inflate produced %llu of %u bytes"
+ "invalid folder level %d"
+ "invalid symlink data length %llu"
+ "logfile"
+ "not a regular file"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "socket"
+ "start file receive V2 message too small %u"
+ "start file receive message too small %u"
+ "start file receive path does not fit %u"
+ "start file receive strings do not fit %u"
+ "symlink"
+ "too many top level items %d"
+ "unable to allocate %u bytes"
+ "unknown"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "Set_FD_CLOEXEC failed to read current file descriptor flags. %d %s"
- "g->newItemMsg.level = %d itemName = %s from packet %s"
```
