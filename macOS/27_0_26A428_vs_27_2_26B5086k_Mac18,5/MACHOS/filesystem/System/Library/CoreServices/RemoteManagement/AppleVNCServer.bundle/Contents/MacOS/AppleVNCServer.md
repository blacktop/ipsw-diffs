## AppleVNCServer

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/MacOS/AppleVNCServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x8656c
-  __TEXT.__auth_stubs: 0x2630
+766.5.0.0.0
+  __TEXT.__text: 0x87278
+  __TEXT.__auth_stubs: 0x2650
   __TEXT.__objc_stubs: 0x34a0
   __TEXT.__objc_methlist: 0x1490
-  __TEXT.__cstring: 0x2032f
-  __TEXT.__oslogstring: 0xebf3
-  __TEXT.__const: 0x2092
+  __TEXT.__cstring: 0x20640
+  __TEXT.__oslogstring: 0xf035
+  __TEXT.__const: 0x20b8
   __TEXT.__objc_methname: 0x45b4
   __TEXT.__objc_classname: 0x203
   __TEXT.__objc_methtype: 0x2a6b
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__unwind_info: 0x1358
-  __DATA_CONST.__const: 0xe90
+  __TEXT.__unwind_info: 0x1398
+  __DATA_CONST.__const: 0xef0
   __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x1328
+  __DATA_CONST.__auth_got: 0x1338
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x1a90
   __DATA.__objc_selrefs: 0x11a0
   __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x3668
+  __DATA.__data: 0x3678
   __DATA.__common: 0x6cc1
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1304
-  Symbols:   769
-  CStrings:  3816
+  Functions: 1324
+  Symbols:   771
+  CStrings:  3842
 
Symbols:
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
+ "Ignore file copy command"
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "Too many receivers"
+ "block device"
+ "character device"
+ "could not open the log"
+ "directory"
+ "fifo"
+ "logfile"
+ "not a regular file"
+ "path does not name the inode we opened, or that inode has other links"
+ "regular file"
+ "rejecting auth because client sent invalid RSA plain data (rsaDataLen: %u, need: %zu)"
+ "rejecting auth because client sent invalid length: %u (opcode: %u needs: %zu)"
+ "socket"
+ "symlink"
+ "truncated scrap: %ld byte(s) remain, need %lu for flavorDataLength"
+ "unable to allocate %u bytes for RSA auth data"
+ "uncompressed size = %ld (declared %u)"
- "Clipboard: inflate error %d\n"
- "Clipboard: inflate init error %d\n"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "uncompressed size = %ld"
```
