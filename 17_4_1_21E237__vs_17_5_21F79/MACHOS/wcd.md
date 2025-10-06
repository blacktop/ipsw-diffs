## wcd

> `/usr/libexec/wcd`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0x2967c
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x4e60
-  __TEXT.__objc_methlist: 0x22f4
-  __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0x2dad
-  __TEXT.__cstring: 0x1b26
-  __TEXT.__gcc_except_tab: 0x658
-  __TEXT.__objc_methname: 0x704f
+207.600.1.0.0
+  __TEXT.__text: 0x2a86c
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_stubs: 0x5320
+  __TEXT.__objc_methlist: 0x234c
+  __TEXT.__const: 0x90
+  __TEXT.__oslogstring: 0x2fd4
+  __TEXT.__cstring: 0x1c7a
+  __TEXT.__gcc_except_tab: 0x700
+  __TEXT.__objc_methname: 0x7405
   __TEXT.__objc_classname: 0x4c5
-  __TEXT.__objc_methtype: 0x147b
+  __TEXT.__objc_methtype: 0x1486
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x9ec
-  __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__cfstring: 0x1360
+  __TEXT.__unwind_info: 0xa10
+  __DATA_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0xaf8
+  __DATA_CONST.__cfstring: 0x1420
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x2a8
+  __DATA_CONST.__objc_classrefs: 0x2b0
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x6c88
-  __DATA.__objc_selrefs: 0x1730
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_const: 0x6cb8
+  __DATA.__objc_selrefs: 0x1870
+  __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x6d0
   __DATA.__bss: 0x98

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85BB5DBA-B6C6-3059-AA71-BD5ECF79EE66
-  Functions: 981
-  Symbols:   313
-  CStrings:  1908
+  UUID: EDD9BED0-0DCC-3BBC-B1ED-9A43F7D8EBEC
+  Functions: 993
+  Symbols:   322
+  CStrings:  1979
 
Symbols:
+ _IDSSendResourceProgressIdentifier
+ _NSProgressFileOperationKindCopying
+ _OBJC_CLASS_$_NSProgress
+ ___error
+ _close
+ _fclonefileat
+ _open
+ _read
+ _write
CStrings:
+ "$\x13"
+ "%{public}@ Client sending file %{public}@ with metadata %{public}@, "
+ "%{public}s Forcing progress to finished for %{public}@"
+ "%{public}s Missing item to remove (identifier: %{public}@)"
+ "%{public}s Progress cancelled for identifier %@"
+ "%{public}s Progress unpublished for transfer %{public}@"
+ "%{public}s Removing progress for transfer %{public}@"
+ "-[WCDClient copyProgressUpdatesForFileTransfer:fromClonedFileURL:]_block_invoke"
+ "-[WCDClient observeValueForKeyPath:ofObject:change:context:]"
+ "-[WCDClient removeProgressForFileTransfer:]"
+ "@?<v@?>16@?0@\"NSProgress\"8"
+ "B24@0:8i16i20"
+ "Could not create destination file for file transfer"
+ "Could not get create directories. error: %@"
+ "Creating progress copy for originalFile: %@, clonedFile: %@, transferID: %@"
+ "Failed to clone file, trying copying"
+ "Failed to open destination file for copying. Errno: %d"
+ "IDSSendResourceProgressIdentifier"
+ "Published progressCopy with transferID %@, to fileURL: %@, progress: %@"
+ "T@\"NSMutableDictionary\",&,V_outstandingFileTransfers"
+ "URLByAppendingPathComponent:"
+ "UUID"
+ "Warning: missing bytes"
+ "Wed Apr 10 15:08:57 2024"
+ "_outstandingFileTransfers"
+ "_removeSubscriber:"
+ "addObserver:forKeyPath:options:context:"
+ "addSubscriberForFileURL:withPublishingHandler:"
+ "byteCompletedCount"
+ "byteTotalCount"
+ "cancelled"
+ "cloning or copying file to: %@"
+ "closeFile"
+ "completedUnitCount"
+ "copyFile:to:"
+ "copyProgressUpdatesForFileTransfer:fromClonedFileURL:"
+ "fileDescriptor"
+ "fileSystemRepresentation"
+ "finished"
+ "initWithDomain:code:userInfo:"
+ "initWithParent:userInfo:"
+ "isCancellable"
+ "isPausable"
+ "kind"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "outstandingFileTransfers"
+ "progress"
+ "progressToken"
+ "publish"
+ "registerForUpdatesForProgress:"
+ "removeProgressForFileTransfer:"
+ "setByteCompletedCount:"
+ "setByteTotalCount:"
+ "setCancellable:"
+ "setCompletedUnitCount:"
+ "setFileOperationKind:"
+ "setFileURL:"
+ "setKind:"
+ "setOutstandingFileTransfers:"
+ "setPausable:"
+ "setProgressToken:"
+ "setTotalUnitCount:"
+ "setUserInfoObject:forKey:"
+ "standardizedURL"
+ "totalUnitCount"
+ "transferFile:withMetadata:identifier:forClient:destFilePath:errorHandler:"
+ "unpublish"
+ "userInfo.NSProgressByteCompletedCountKey"
+ "v48@0:8@16@24@32^v40"
- "$\x12"
- "%{public}@ Client sending file %{public}@ with metadata %{public}@"
- "Fri Jun 16 15:11:58 2023"
- "fileURL: %{public}@, hasMetadata: %s, identifier: %{public}@, clientID: %{public}@, clientPairingID: %{public}@"
- "transferFile:withMetadata:identifier:forClient:errorHandler:"
- "v56@0:8@16@24@32@40@?48"

```
