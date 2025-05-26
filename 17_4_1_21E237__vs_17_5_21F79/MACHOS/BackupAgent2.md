## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2125.102.2.0.0
-  __TEXT.__text: 0x899ac
+2125.120.44.0.1
+  __TEXT.__text: 0x8a1f0
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0xc960
-  __TEXT.__objc_methlist: 0x5f90
+  __TEXT.__objc_stubs: 0xc9e0
+  __TEXT.__objc_methlist: 0x5fd8
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x1e3fc
-  __TEXT.__oslogstring: 0xb356
-  __TEXT.__objc_methname: 0xeba5
-  __TEXT.__objc_classname: 0xa18
-  __TEXT.__objc_methtype: 0x2092
-  __TEXT.__gcc_except_tab: 0x1620
-  __TEXT.__unwind_info: 0x1650
+  __TEXT.__cstring: 0x1e59d
+  __TEXT.__oslogstring: 0xb45f
+  __TEXT.__objc_methname: 0xec57
+  __TEXT.__objc_classname: 0x9fd
+  __TEXT.__objc_methtype: 0x20c9
+  __TEXT.__gcc_except_tab: 0x1648
+  __TEXT.__unwind_info: 0x1668
   __DATA_CONST.__auth_got: 0xc30
   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1110
-  __DATA_CONST.__cfstring: 0xa280
+  __DATA_CONST.__const: 0x1160
+  __DATA_CONST.__cfstring: 0xa260
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x578
+  __DATA_CONST.__objc_classrefs: 0x580
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xa4c0
-  __DATA.__objc_selrefs: 0x3f40
+  __DATA.__objc_const: 0xa518
+  __DATA.__objc_selrefs: 0x3f68
   __DATA.__objc_ivar: 0x60c
   __DATA.__objc_data: 0x2260
   __DATA.__data: 0x7b8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2244
-  Symbols:   568
-  CStrings:  7319
+  Functions: 2250
+  Symbols:   569
+  CStrings:  7334
 
Symbols:
+ _OBJC_CLASS_$_NSByteCountFormatter
CStrings:
+ "-[NSObject(MBRestorableMixin) restoreAttributesToDestination:withUserID:groupID:permissions:error:]"
+ "-[NSObject(MBRestorableMixin) restoreSymbolicLinkAtPath:withTarget:]"
+ "<%@: fileID=%@, domain=%@, relativePath=%@, target=%@, digest=%@, encryptionKey=%@, mode=%@, inodeNumber=%llu, userID=%u, groupID=%u, lastModified=%@, lastStatusChange=%@, birth=%@, size=%llu, protectionClass=%d, priority=%lld extendedAttributes=%@>"
+ "=pc= +canOpenWhenLocked: Invalid protection class: %d"
+ "=pc= +isProtected: Invalid protection class: %d"
+ "=pc= No SQLite open flag known for protection class: %d"
+ "=pc= open_dprotected_np failed at %@: %{errno}d"
+ "=pc= open_dprotected_np failed at %s: %{errno}d"
+ "B32@0:8^{?=SSIIIqqqqQQC{?=b1b1b1}}16@24"
+ "Q32@0:8^@16@24"
+ "RestoreCloudFormatInfo"
+ "RestorePolicy"
+ "Restoring directory extended attributes (%ld) at path %@"
+ "Restoring directory ownership: %d:%d at path %@"
+ "Restoring protection class: %d for path: %s"
+ "Restoring symbolic link permissions: 0%3o"
+ "Restoring uid %u, gid %u, ctime %ld, mtime %ld, atime %ld, permissions %o to %@"
+ "TQ,N,V_priority"
+ "TQ,R,D,N"
+ "adjustVnodeOwnershipAndPermissionsForDataMigratorPlugIn:path:"
+ "backupAnnotationXattrKey"
+ "enumerateWithError:block:"
+ "fetchCountWithError:sql:"
+ "groupInTransaction:"
+ "groupInTransaction:error:"
+ "setProtectionClass:"
+ "size:%lld (%@)/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardLinks:%llu, symLinks:%llu"
+ "stringFromByteCount:countStyle:"
- "0%3o"
- "<%@: fileID=%@, domain=%@, relativePath=%@, target=%@, digest=%@, encryptionKey=%@, mode=%@, inodeNumber=%llu, userID=%u, groupID=%u, lastModified=%@, lastStatusChange=%@, birth=%@, size=%llu, protectionClass=%d, extendedAttributes=%@>"
- "MBForEachAdditions"
- "MBProtectionClass.m"
- "MBRestorableAdditions"
- "MBVnodeForFD"
- "No SQLite open flag known for protection class: %d"
- "Restoring directory extended attributes (%ld)"
- "Restoring directory ownership: %d:%d"
- "Restoring symbolic link permissions: %@"
- "_forEachResultWithError:block:"
- "_shouldRestoreAsMobile"
- "fgetattrlist() error"
- "forEachResultWithError:block:"
- "open_dprotected_np failed at %@: %{errno}d"
- "open_dprotected_np failed at %s: %{errno}d"
- "size:%lld/%lld/%lld, files:%llu, dirs:%llu, clones:%llu/%llu, hardLinks:%llu, symLinks:%llu"

```
