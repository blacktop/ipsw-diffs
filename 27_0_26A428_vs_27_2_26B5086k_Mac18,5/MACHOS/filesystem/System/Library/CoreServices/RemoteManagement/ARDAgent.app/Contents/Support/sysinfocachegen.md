## sysinfocachegen

> `/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Support/sysinfocachegen`

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
-  __TEXT.__text: 0xf4d4
-  __TEXT.__auth_stubs: 0xe30
+766.5.0.0.0
+  __TEXT.__text: 0xfa80
+  __TEXT.__auth_stubs: 0xe70
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x484b
-  __TEXT.__oslogstring: 0x557
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x48e6
+  __TEXT.__oslogstring: 0x723
   __TEXT.__objc_methname: 0x7cf
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0xea
-  __TEXT.__unwind_info: 0x2a0
-  __DATA_CONST.__const: 0x1f0
+  __TEXT.__unwind_info: 0x2b8
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__cfstring: 0x1180
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x160
   __DATA.__objc_const: 0x270
   __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc8
+  __DATA.__data: 0xd8
   __DATA.__common: 0x1
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/Versions/A/DiagnosticLogCollection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 146
-  Symbols:   279
-  CStrings:  999
+  Functions: 153
+  Symbols:   283
+  CStrings:  1015
 
Symbols:
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
- "LFOpen failed - Couldn't open '%s'. %d: %s"
```
