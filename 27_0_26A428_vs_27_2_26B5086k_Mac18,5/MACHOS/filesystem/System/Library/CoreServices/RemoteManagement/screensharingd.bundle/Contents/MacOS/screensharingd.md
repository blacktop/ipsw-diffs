## screensharingd

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/MacOS/screensharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-756.36.5.2.0
-  __TEXT.__text: 0x774a4
-  __TEXT.__auth_stubs: 0x1e10
+766.5.0.0.0
+  __TEXT.__text: 0x77534
+  __TEXT.__auth_stubs: 0x1e00
   __TEXT.__objc_stubs: 0x2120
   __TEXT.__objc_methlist: 0xd48
-  __TEXT.__const: 0x2370
-  __TEXT.__oslogstring: 0xcbbf
-  __TEXT.__cstring: 0x14857
+  __TEXT.__const: 0x2388
+  __TEXT.__oslogstring: 0xcceb
+  __TEXT.__cstring: 0x145b6
   __TEXT.__gcc_except_tab: 0x194
   __TEXT.__objc_methname: 0x2340
   __TEXT.__objc_classname: 0xde
   __TEXT.__objc_methtype: 0x6c0
-  __TEXT.__unwind_info: 0x11a0
-  __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__cfstring: 0x14c0
+  __TEXT.__unwind_info: 0x11d0
+  __DATA_CONST.__const: 0xe78
+  __DATA_CONST.__cfstring: 0x1440
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xf18
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__auth_got: 0xf10
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x1080
   __DATA.__objc_selrefs: 0xae8
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x6b8
+  __DATA.__data: 0x6c8
   __DATA.__common: 0x6629
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1135
-  Symbols:   590
-  CStrings:  3002
+  Functions: 1150
+  Symbols:   588
+  CStrings:  3000
 
Symbols:
+ _os_log_create
+ _pthread_once
+ _readlink
- _dlclose
- _dlopen
- _dlsym
- _fchmod
- _kCFCopyStringDictionaryKeyCallBacks
CStrings:
+ " -> "
+ "CheckEntitlement"
+ "Ignore file copy command"
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Found a %{public}s there: uid=%u gid=%u mode=%04o nlink=%u dev=%d ino=%llu%{public}s%{public}s. Left in place on purpose."
+ "Not logging to %{public}s: %{public}s (errno %d: %{public}s). Nothing is at that path now."
+ "Not logging to %{public}s: could not clear O_NONBLOCK (errno %d: %{public}s)."
+ "Not logging to %{public}s: fdopen failed (errno %d: %{public}s)."
+ "Not logging to %{public}s: out of memory."
+ "Too many receivers"
+ "block device"
+ "character device"
+ "com.apple.private.aqua.createSession"
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
+ "unable to allocate %u bytes for RSA auth data"
- "/System/Library/Frameworks/Security.framework/Security"
- "/var/db/.RemoteManagementDebugAdmin"
- "CheckScreenSharingEntitlement"
- "IsCodeSignatureValid"
- "LFOpen failed - Couldn't open '%s'. %d: %s"
- "SecCodeCheckValidity"
- "SecCodeCopyGuestWithAttributes"
- "SecCodeCopyGuestWithAttributes error %d"
- "SecRequirementCreateWithString"
- "SecRequirementCreateWithString error %d"
- "anchor apple"
- "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.7] exists and certificate leaf[subject.CN] = \"3rd Party Mac Developer Application: Apple Inc.\"* and certificate 1[field.1.2.840.113635.100.6.2.1] exists"
- "anchor apple generic and info [CFBundleIdentifier] = \"com.apple.\"* and certificate leaf[field.1.2.840.113635.100.6.1.9.1] exists"
- "anchor apple generic and info [CFBundleIdentifier] = \"com.apple.\"* and certificate leaf[field.1.2.840.113635.100.6.1.9] exists"
- "app qa error %d"
- "app store check errror %d"
- "app store test build error %d"
- "apple check errror %d"
- "create requirements for app production build error %d"
- "create requirements for app qa build error %d"
- "create requirements for app store test build error %d"
- "dlopen failed trying to open lib."
- "dlsym failed %p %p %p"
- "pid"
- "senderis ok %d"
- "start of check"
```
