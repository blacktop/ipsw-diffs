## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-2008.60.8.0.0
-  __TEXT.__text: 0x109f8
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x94c
-  __TEXT.__const: 0x108
-  __TEXT.__objc_methname: 0x2183
-  __TEXT.__cstring: 0x34ff
-  __TEXT.__objc_classname: 0x10e
-  __TEXT.__objc_methtype: 0x6db
-  __TEXT.__oslogstring: 0x1684
-  __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x2e4
-  __DATA_CONST.__auth_got: 0x550
+2125.102.2.0.0
+  __TEXT.__text: 0x11b64
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_stubs: 0x1ec0
+  __TEXT.__objc_methlist: 0xa0c
+  __TEXT.__const: 0x124
+  __TEXT.__objc_methname: 0x2379
+  __TEXT.__cstring: 0x39e7
+  __TEXT.__objc_classname: 0x123
+  __TEXT.__objc_methtype: 0x709
+  __TEXT.__oslogstring: 0x1777
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__unwind_info: 0x33c
+  __DATA_CONST.__auth_got: 0x568
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a8
-  __DATA_CONST.__cfstring: 0x12a0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__cfstring: 0x1300
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1020
-  __DATA.__objc_selrefs: 0x9e0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0x1150
+  __DATA.__objc_selrefs: 0xa50
+  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x228
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x198
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 55307FD7-F088-36D8-9F74-CC1C073E55A7
-  Functions: 312
-  Symbols:   266
-  CStrings:  1135
+  UUID: 5AF04A2C-D61A-3A5B-9216-7EDB22E5C889
+  Functions: 348
+  Symbols:   271
+  CStrings:  1204
 
Symbols:
+ _OBJC_CLASS_$_MBTemporaryDirectory
+ _OBJC_METACLASS_$_MBTemporaryDirectory
+ _mkpath_np
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "%s/%s_XXXXXXXXXXXXXXX"
+ "*"
+ "+[MBProtectionClassUtils canOpenWhenLocked:]"
+ "+[MBProtectionClassUtils isProtected:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:]"
+ "+[MBTemporaryDirectory temporaryDirectoryOnSameVolumeAsPath:identifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
+ "-[MBTemporaryDirectory _initWithExistingFsRepPath:identifier:]"
+ "-[MBTemporaryDirectory _purgeContentsAt:error:]"
+ "-[MBTemporaryDirectory dealloc]"
+ "-[MBTemporaryDirectory purgeContentsWithError:]"
+ "/Library/Caches/com.apple.xbs/Sources/MobileBackupFramework/Common/Source/MBTemporaryDirectory.m"
+ "/var/mobile/tmp/com.apple.backup.testing"
+ "/var/tmp/com.apple.backup"
+ "/var/tmp/com.apple.backup.testing"
+ "<%@: %@, path: %s>"
+ "=tmpdir= %@ failed to create new contents directory: %@"
+ "=tmpdir= %@ failed to move contents aside to purge: %@"
+ "=tmpdir= %@ was not disposed before being dealloc'd"
+ "=tmpdir= could not find mount point for %@: %@"
+ "=tmpdir= failed to delete %@: %@"
+ "@32@0:8*16@24"
+ "@40@0:8@16@24^@32"
+ "B24@0:8^@16"
+ "MBProtectionClass.m"
+ "MBTemporaryDirectory"
+ "MBTemporaryDirectory.m"
+ "NO"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N"
+ "_disposed"
+ "_fsRepPath"
+ "_identifier"
+ "_initWithExistingFsRepPath:identifier:"
+ "_mkdtemp"
+ "_mkpath_if_necessary"
+ "_mktemp"
+ "_path"
+ "_purgeContentsAt:error:"
+ "canOpenWhenLocked:"
+ "com.apple.backup"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dealloc"
+ "dispose"
+ "disposeWithError:"
+ "disposeWithoutDeleting"
+ "fsRepPath"
+ "identifier"
+ "identifier.length"
+ "makeTemporaryFilePath"
+ "persona"
+ "purgeContentsWithError:"
+ "root"
+ "sharedTemporaryDirectoryForTest:"
+ "sharedTemporaryDirectoryIdentifiedBy:"
+ "temporaryDirectoryOnSameVolumeAsPath:identifiedBy:error:"
+ "testName.length"
+ "tmp"
+ "userTemporaryDirectoryForPersona:identifiedBy:"
+ "userTemporaryDirectoryForTest:"
- "canBackupWhenLocked:"
- "canRestoreWhenLocked:"
- "shouldCache:"

```
