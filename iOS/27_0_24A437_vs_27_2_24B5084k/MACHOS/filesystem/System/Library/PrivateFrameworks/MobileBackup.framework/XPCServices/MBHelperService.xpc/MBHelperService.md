## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`

```diff

-3039.2.2.0.0
-  __TEXT.__text: 0x13824
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0xc9c
-  __TEXT.__const: 0x228
-  __TEXT.__objc_methname: 0x2645
-  __TEXT.__cstring: 0x3ab5
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methtype: 0x78b
-  __TEXT.__oslogstring: 0x1f26
+3039.40.8.0.0
+  __TEXT.__text: 0xb748
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x1860
+  __TEXT.__objc_methlist: 0x984
+  __TEXT.__const: 0x130
+  __TEXT.__objc_methname: 0x1e5a
+  __TEXT.__cstring: 0x19a5
+  __TEXT.__objc_classname: 0xf5
+  __TEXT.__objc_methtype: 0x5d0
+  __TEXT.__oslogstring: 0xb49
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x5e8
-  __DATA_CONST.__const: 0x588
-  __DATA_CONST.__cfstring: 0x13c0
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__unwind_info: 0x468
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__cfstring: 0xe00
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__auth_got: 0x5f0
-  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0xfa8
-  __DATA.__objc_selrefs: 0xb88
-  __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x228
+  __DATA.__objc_const: 0xb28
+  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x168
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 400
-  Symbols:   290
-  CStrings:  990
+  Functions: 268
+  Symbols:   241
+  CStrings:  667
 
Symbols:
- _MBDiagnoseFile
- _MBTemporaryPath
- _NSTemporaryDirectory
- _OBJC_CLASS_$_MBFileEncodingTask
- _OBJC_CLASS_$_MBProtectionClassUtils
- _OBJC_METACLASS_$_MBFileEncodingTask
- _OBJC_METACLASS_$_MBProtectionClassUtils
- __Block_object_dispose
- __DefaultRuneLocale
- ___maskrune
- __dispatch_queue_attr_concurrent
- __sqlite3_apple_archive
- __sqlite3_apple_unarchive
- _access
- _bzero
- _closedir
- _compression_stream_destroy
- _compression_stream_init
- _compression_stream_process
- _dispatch_async
- _dispatch_block_create
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _dispatch_group_wait
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _fcntl
- _fdopendir
- _ffsctl
- _fstatfs
- _ftruncate
- _getattrlist
- _getuid
- _getxattr
- _mkstemp
- _objc_retain_x26
- _objc_setProperty_nonatomic_copy
- _open_dprotected_np
- _openbyid_np
- _pread
- _readdir_r
- _sqlite3_free
- _stat
- _unlink
- _write
CStrings:
- "!pa || count == 1"
- "!pa || count >= 1"
- "!self.validate || MBIsInternalInstall()"
- "%u%c%u"
- "%u-%c-%u"
- "*compressionMethod != MBFileCompressionMethodUnspecified && *compressionMethod != MBFileCompressionMethodDefault"
- "-[MBFileEncodingTask _archive]"
- "-[MBFileEncodingTask _compress]"
- "-[MBFileEncodingTask _decompress]"
- "-[MBFileEncodingTask _handleCompressionOperation:algorithm:destinationSize:error:]"
- "-[MBFileEncodingTask _unarchive]"
- "-[MBFileEncodingTask initWithType:encodingMethod:]"
- "-[MBFileEncodingTask start]"
- "-[MBHelperService runEncodingTask:reply:]"
- "/..namedfork/rsrc"
- "/private/var/tmp/backupd-XXXXXXXXXXXXXXX"
- "=diag=       0x%llx:+%lld (crid %llu)"
- "=diag=       class:   %#x"
- "=diag=       exists?  %u"
- "=diag=       flags:   %#x"
- "=diag=       len:     %u"
- "=diag=       os:      %@"
- "=diag=       payload: %u (trunc? %d)"
- "=diag=       refcnt:  %u"
- "=diag=       rev:     %u"
- "=diag=       version: %u.%u"
- "=diag=     class:   %#x"
- "=diag=     exists?  %u"
- "=diag=     flags:   %#x"
- "=diag=     len:     %u"
- "=diag=     os:      %@"
- "=diag=     payload: %u (trunc? %d)"
- "=diag=     refcnt:  %u"
- "=diag=     rev:     %u"
- "=diag=     version: %u.%u"
- "=diag=   alloced_size: %llu"
- "=diag=   default_crid: %llu"
- "=diag=   num extents:  %u"
- "=diag=   refcnt:       %u"
- "=diag=   size:         %llu"
- "=diag= %s does not have associated crypto dstreams"
- "=diag= %s is a compressed file"
- "=diag= %{public}s failed with %d at %{public}@"
- "=diag= 0x%llx:+%lld @ 0x%llx"
- "=diag= Dstream id %llu, dstream size %llu bytes"
- "=diag= Dumping crypto file info"
- "=diag= Dumping diagnostics for %{public}@ (%d)"
- "=diag= Dumping extent information"
- "=diag= Extent offset %lld and length %lld"
- "=diag= Failed to find the file using readdir_r (%u)"
- "=diag= Failed to get the crypto file infos: %{errno}d"
- "=diag= Failed to open the file raw encrypted: %{errno}d"
- "=diag= Finished dumping diagnostics for %{public}@"
- "=diag= Found %u crypto ids for filesize %lld"
- "=diag= Found %u extents"
- "=diag= access(F_OK) failed: %{errno}d"
- "=diag= access(F_OK): %d"
- "=diag= access(R_OK) failed: %{errno}d"
- "=diag= access(R_OK): %d"
- "=diag= fdopendir failed at %{public}s: %{errno}d"
- "=diag= fsctl(APFSIOC_DEBUG_STATS) failed: %{errno}d"
- "=diag= fsctl(APFSIOC_DEBUG_STATS) failed: %{errno}d, cannot get extents at offset %lld"
- "=diag= fsctl(APFSIOC_DEBUG_STATS) for FUSION_DEBUG_STATS_PURE_FEXTS_ONLY returned zero buffer entries at offset %lld"
- "=diag= fsctl(APFSIOC_DEBUG_STATS) returned zero buffer entries"
- "=diag= fsctl(APFSIOC_GET_CLONE_INFO) failed: %{errno}d"
- "=diag= fsctl(APFSIOC_GET_CLONE_INFO): flags 0x%llx, private_id %llu"
- "=diag= fsctl(APFSIOC_GET_INTERNAL_FLAGS) failed: %{errno}d"
- "=diag= fsctl(APFSIOC_GET_INTERNAL_FLAGS): flags 0x%llx"
- "=diag= fsctl(APFSIOC_PURGEABLE_GET_FILE_INFO) failed: %{errno}d"
- "=diag= fsctl(APFSIOC_PURGEABLE_GET_FILE_INFO): file flags: 0x%llx related flags: 0x%llx, file acctime: %llu\n gen count: %llu sync root id: %llu size: %llu"
- "=diag= fstatfs failed at %{public}s: %{errno}d"
- "=diag= fstatfs: bsize %u, iosize %d, blocks %llu, bfree %llu, bavail %llu, files %llu, ffree %llu, fsid {%d, %d}, owner %d, type %d, flags 0x%x, fssubtype %d, flags_ext 0x%x"
- "=diag= getattrlist failed: %{errno}d"
- "=diag= getattrlist: len %u, dev (%d)%d, type (%d)%u, fileId (%d)%llu, uid (%d)%u, gid (%d)%u, access (%d)0%o, flags (%d)0x%x, gencount (%d)%u, protclass (%d)%u, nlink (%d)%u, lgsize (%d)%lld, physize (%d)%lld, realsize (%d)%lld, linkid (%d)%llu"
- "=diag= log2phys failed at 0x%llx: %{errno}d"
- "=diag= nil dir path FSR"
- "=diag= nil name FSR"
- "=diag= nil path FSR"
- "=diag= open failed at %{public}s: %{errno}d"
- "=diag= openbyid_np({%d, %d}, %llu) failed: %{errno}d"
- "=diag= openbyid_np({%d, %d}, %llu) succeeded"
- "=diag= pread failed: %d"
- "=diag= pread returned %ld bytes"
- "=diag= private_id: %llu"
- "=diag= prot_class: %llu (explicit? %d)"
- "=diag= readdir_r failed: %d (%{errno}d)"
- "=diag= readdir_r found file entry (%u), type %d, ino %llu, namelen %d, reclen %d"
- "=diag= stat failed: %{errno}d"
- "=diag= stat: dev %d, ino %llu, mode 0%o, nlink %u, uid %u, gid %u, rdev %d, atime %lu.%ld, mtime %lu.%ld, ctime %lu.%ld, lgsize %lld, physize %lld, blksize %d, flags %u, gen %u"
- "=diag= warning: not a regular file, link info and sizes will be garbage"
- "=pc= +canOpenWhenLocked: Invalid protection class: %d"
- "=pc= +isProtected: Invalid protection class: %d"
- "=pc= No SQLite open flag known for protection class: %d"
- "=pc= open_dprotected_np failed at %@: %{errno}d"
- "=pc= open_dprotected_np failed at %s: %{errno}d"
- "@\"NSData\""
- "@\"NSError\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_group>\""
- "@20@0:8c16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8c16c20"
- "@?"
- "@?16@0:8"
- "B20@0:8C16"
- "B32@0:8i16C20^@24"
- "B36@0:8@16C24^@28"
- "B36@0:8r*16C24^@28"
- "B40@0:8i16i20^Q24^@32"
- "C"
- "C16@0:8"
- "C28@0:8i16^@20"
- "C32@0:8@16^@24"
- "C32@0:8r*16^@24"
- "Failed to create dst file"
- "Failed to create tmp file"
- "Failed to fstat dst file"
- "Failed to mmap the src file"
- "Failed to set Cx protection class, leaving as C on %@, error:%@"
- "Failed to set protection class on the file at %@, error:%@"
- "Failed to stat dst file"
- "Failed to stat src file"
- "Failed to validate the archived SQLite file at %@(%@), e:%ld/0x%lx: %@"
- "Failed to validate the compressed file at %@(%@), e:%ld/0x%lx, error:%@"
- "Failed to write to the %s file"
- "File content unavailable with protection class %d"
- "File encoding cancelled"
- "Finished archiving, srcPath:%@, dstPath:%@, e:%ld/0x%lx, pc:%d, srcMTime:%ld, srcSize:%llu, dstSize:%llu, savings:%.3f, time:%.3fs"
- "Finished compressing, srcPath:%@, dstPath:%@, e:%ld/0x%lx, pc:%d, srcMTime:%ld, srcSize:%llu, dstSize:%llu, savings:%.3f, time:%.3fs, srcDigest:%@, dstDigest:%@"
- "Finished decompressing, srcPath:%@, dstPath:%@, e:%ld/0x%lx, pc:%d, srcSize:%llu, dstSize:%llu, time:%.3fs, srcDigest:%@, dstDigest:%@"
- "Finished task:%@, error:%@"
- "Finished unarchiving, srcPath:%@, dstPath:%@, e:%ld/0x%lx, pc:%d, srcSize:%llu, dstSize:%llu, time:%.3fs"
- "Insufficient space savings, srcSize:%llu, dstSize:%llu"
- "Insufficient space savings: %.3f < %.3f"
- "Invalid argument: no destination path"
- "Invalid arguments: no source path, or unspecified compression or protection class"
- "Invalid compression algorithm %ld"
- "Invalid file compression method %ld"
- "Invalid size(0) for SQLite archive"
- "MBDiagnostics.m"
- "MBFileEncodingTask"
- "MBFileEncodingTask.m"
- "MBHelperService.m"
- "MBIsInternalInstall()"
- "MBProtectionClassUtils"
- "MBTemporaryPath"
- "Mismatched SHA256 for the file at %@, %@ != %@"
- "Mismatched digests, %@ != %@"
- "Mismatched size (%llu != %llu)"
- "NSCoding"
- "NSSecureCoding"
- "Source file is 0 bytes, returning empty 0 byte file at %@"
- "Starting task:%@, sourcePath:%@, destinationPath:%@, encodingMethod:%ld, compressionMethod:%ld, pc:%d"
- "T@\"NSData\",&,N,V_destinationDigest"
- "T@\"NSData\",&,N,V_sourceDigest"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSNumber\",&,N,V_spaceSavingsThreshold"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_group"
- "T@\"NSString\",&,N,V_destinationPath"
- "T@\"NSString\",&,N,V_sourcePath"
- "T@?,C,N,V_cancellationHandler"
- "TB,N,V_sourceIsLive"
- "TB,N,V_validate"
- "TB,R"
- "TC,N,V_protectionClass"
- "TQ,N,V_destinationSize"
- "Tc,N,V_compressionMethod"
- "Tc,N,V_encodingMethod"
- "Tc,N,V_type"
- "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory"
- "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
- "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (strdup)"
- "Unknown encoding method %ld"
- "_archive"
- "_cancellationHandler"
- "_compress"
- "_compressionMethod"
- "_decompress"
- "_destinationDigest"
- "_destinationPath"
- "_destinationSize"
- "_diagnoseFile"
- "_encodingMethod"
- "_error"
- "_finishWithError:"
- "_getNumberOfFileExtents"
- "_group"
- "_handleCompressionOperation:algorithm:destinationSize:error:"
- "_openRawEncryptedWithPathFSR:error:"
- "_protectionClass"
- "_sourceDigest"
- "_sourceIsLive"
- "_sourcePath"
- "_spaceSavingsThreshold"
- "_sqlite3_apple_archive failed, rc:%d, \"%s\""
- "_sqlite3_apple_archive failed, rc:%d, msg:\"%s\", e:%ld/%ld, srcPath:%@, dstPath:%@"
- "_sqlite3_apple_unarchive failed, rc:%d, \"%s\""
- "_sqlite3_apple_unarchive failed, rc:%d, msg:\"%s\", srcPath:%@, dstPath:%@"
- "_type"
- "_unarchive"
- "_validate"
- "c"
- "c16@0:8"
- "canOpenWhenLocked:"
- "cancel"
- "cancellationHandler"
- "com.apple.ResourceFork"
- "com.apple.backupd.decoding"
- "com.apple.backupd.encoding"
- "compressed"
- "compressionMethod"
- "compression_stream_init failed"
- "compression_stream_process failed"
- "compression_stream_process(%ld) failed with status:%ld"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodingTaskWithEncodingMethod:"
- "decompressed"
- "destinationDigest"
- "destinationPath"
- "destinationSize"
- "doubleValue"
- "ds_buffer"
- "dstBuffer"
- "dstCompressionMethod != MBFileCompressionMethodDefault"
- "dstCompressionMethod != MBFileCompressionMethodUnspecified"
- "dstFd == -1"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodingMethod"
- "encodingMethod != MBFileEncodingMethodUnspecified"
- "encodingTaskWithEncodingMethod:"
- "fcntl error getting protection class"
- "fcntl error setting Cx protection class"
- "fcntl error setting protection class"
- "fcntl permission error setting protection class (device locked?)"
- "finfo"
- "getFileSystemRepresentation failed"
- "getFileSystemRepresentation:maxLength:"
- "getWithFD:error:"
- "getWithPath:error:"
- "getWithPathFSR:error:"
- "group"
- "handleCompressionOperation"
- "i20@0:8C16"
- "i32@0:8r*16^@24"
- "initWithCoder:"
- "initWithType:encodingMethod:"
- "initWithUTF8String:"
- "isContentUnavailableDueToCxExpiration:error:"
- "isEqualToData:"
- "isExpectedSetProtectionClassError:"
- "isProtected:"
- "makeFileCompressionMethodFromCompressionAlgorithm"
- "mkstemp failed: %{errno}d"
- "mktemp failed: %{errno}d"
- "open error setting protection class"
- "open error setting protection class (device locked?)"
- "open_dprotected_np"
- "open_dprotected_np error"
- "operation == COMPRESSION_STREAM_ENCODE || operation == COMPRESSION_STREAM_DECODE"
- "pc != MBProtectionClassUnspecified"
- "protectionClass"
- "result"
- "result || localError"
- "runEncodingTask:reply:"
- "self.encodingMethod != MBFileEncodingMethodDefault"
- "self.encodingMethod != MBFileEncodingMethodUnspecified"
- "self.encodingMethod == MBFileEncodingMethodCompressedSQLiteText || self.encodingMethod == MBFileEncodingMethodCompressedSQLiteBinary"
- "self.group"
- "setCancellationHandler:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCompressionMethod:"
- "setDestinationDigest:"
- "setDestinationPath:"
- "setDestinationSize:"
- "setEncodingMethod:"
- "setError:"
- "setGroup:"
- "setProtectionClass:"
- "setSourceDigest:"
- "setSourceIsLive:"
- "setSourcePath:"
- "setSpaceSavingsThreshold:"
- "setType:"
- "setValidate:"
- "setWithFD:value:error:"
- "setWithObjects:"
- "setWithPath:value:error:"
- "setWithPathFSR:value:error:"
- "sourceDigest"
- "sourceIsLive"
- "sourcePath"
- "spaceSavingsThreshold"
- "sqliteOpenFlagForProtectionClass:"
- "srcPath"
- "start"
- "stream.dst_ptr - dstBuffer <= dstBufferSize"
- "stream.dst_size <= dstBufferSize"
- "stream.src_ptr == MAP_FAILED || (stream.src_ptr - srcBuffer) <= srcBufferSize"
- "supportsSecureCoding"
- "task"
- "task.compressionMethod != MBFileCompressionMethodUnspecified"
- "tmpbackupXXXXXXXX"
- "tmpbackupencodeXXXXXXXX"
- "type"
- "type != MBFileEncodingTypeUnspecified"
- "type == MBFileEncodingTypeEncode || type == MBFileEncodingTypeDecode"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8c16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@\"MBFileEncodingTask\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "validate"
- "write"
```
