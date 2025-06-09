## com.apple.fskit.exfat

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.exfat.appex/com.apple.fskit.exfat`

```diff

-488.120.2.0.0
-  __TEXT.__text: 0xe8bc
-  __TEXT.__auth_stubs: 0x8b0
+522.0.0.0.0
+  __TEXT.__text: 0x101fc
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x204
-  __TEXT.__const: 0x4cdb
-  __TEXT.__cstring: 0x303f
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__objc_methname: 0x79a
-  __TEXT.__oslogstring: 0x51a
-  __TEXT.__objc_classname: 0x5f
-  __TEXT.__objc_methtype: 0x328
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__cfstring: 0x4e0
+  __TEXT.__objc_methlist: 0x214
+  __TEXT.__const: 0x4d0b
+  __TEXT.__cstring: 0x34d3
+  __TEXT.__oslogstring: 0x503
+  __TEXT.__gcc_except_tab: 0x394
+  __TEXT.__objc_methname: 0x75a
+  __TEXT.__objc_classname: 0x62
+  __TEXT.__objc_methtype: 0x343
+  __TEXT.__unwind_info: 0x2a8
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x240
+  __DATA.__objc_const: 0x278
   __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x3d60
-  __DATA.__bss: 0xec610
-  __DATA.__common: 0x1d0
+  __DATA.__data: 0x46e0
+  __DATA.__bss: 0x2018
+  __DATA.__common: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7CA1A7F0-CE4D-3F25-87B4-E5480D11A6BA
-  Functions: 237
-  Symbols:   326
-  CStrings:  565
+  UUID: CFD29FFA-6607-3662-9DF3-FC1397AEB61D
+  Functions: 251
+  Symbols:   339
+  CStrings:  584
 
Symbols:
+ _FSKitErrorDomain
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_FSFileName
+ _OBJC_CLASS_$_FSVolume
+ _OBJC_CLASS_$_NSProgress
+ __os_log_default
+ __os_log_fault_impl
+ _close
+ _dispatch_async
+ _dispatch_get_global_queue
+ _endCallbackFsck
+ _endCallbackNewfs
+ _fsck_exfat_bitmap_deinit
+ _fsck_exfat_filename_exists_in_dir
+ _localizeFSCKMessage
+ _localizeNewFSMessage
+ _newfs_messages_exfat
+ _objc_getProperty
+ _objc_opt_isKindOfClass
+ _objc_release_x1
+ _objc_retain_x25
+ _objc_retain_x9
+ _objc_setProperty_atomic
+ _open
+ _sfm_to_mac
+ _startCallbackFsck
+ _startCallbackNewfs
+ _unlink
- _CFSetCreateMutable
- _CFSetGetCount
- _NSLocalizedFailureReasonErrorKey
- _NSLog
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSNumber
- _OBJC_EHTYPE_$_NSException
- _fprintf
- _kCFTypeSetCallBacks
- _objc_begin_catch
- _objc_end_catch
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "%@%s"
+ "%s: Can't allocate a wipe FS context object\n"
+ "%s: Can't allocate an FSCK context object"
+ "%s: Flushing cached block with idx %u to file"
+ "%s: Given device is not a block device\n"
+ "%s: Reading block with idx %u from file"
+ "%s: Sector size was not initialized, setting to default value (%d)\n"
+ "%s: Total sectors was not initialized, setting to default value (%d)\n"
+ "%s: Wipe resource error: %d\n"
+ "%s: fstat failed, path (%s)\n"
+ "%s: loaded resource with volume ID (%@)"
+ "%s: ran out of buffers!"
+ "%s:start"
+ "-I"
+ "-N"
+ "-R"
+ "-S"
+ "-[exfatFileSystem getVolumeNameAndUUID:useAlt:reply:]"
+ "-[exfatFileSystem loadResource:options:replyHandler:]"
+ "-[exfatFileSystem startCheckWithTask:options:error:]"
+ "-[exfatFileSystem startCheckWithTask:options:error:]_block_invoke"
+ "-[exfatFileSystem startFormatWithTask:options:error:]"
+ "-[exfatFileSystem startFormatWithTask:options:error:]_block_invoke"
+ "-a"
+ "-b"
+ "-c"
+ "-d"
+ "-g"
+ "-n"
+ "-q"
+ "-s"
+ "-v"
+ "-x"
+ "-y"
+ ".cxx_destruct"
+ "@\"FSBlockDeviceResource\""
+ "Check FS: Verify data structure: Failed"
+ "Check FS: Verify data structures"
+ "Continue checking the volume with in-memory bitmap."
+ "Could not allocate bitmap cache block"
+ "Could not allocate cache buffers"
+ "Could not allocate struct fsck_bitmap_cache"
+ "Could not convert name (%s) to precomposed UTF-16 little endian; may be too long\n"
+ "Could not read cluster %u from FAT."
+ "Could not read cluster %u from cache."
+ "Could not release cached buffer. error = %d."
+ "Encountered errors trying to wipe resource\n"
+ "Encountered errors while writing backup boot sector\n"
+ "Encountered errors while writing main boot sector\n"
+ "Failed reading from bitmap cache file with error = %d. offset %u length %u."
+ "Failed to allocate temporary buffer\n"
+ "Failed to create bitmap cache file (%s), error = %d."
+ "Failed to retrieve localized message"
+ "Failed to start phase, error %s\n"
+ "Failed to truncate bitmap cache file (%s), error = %d."
+ "Failed to unlink bitmap cache file (%s), error = %d."
+ "Failed writing to bitmap cache file with error = %d. offset %u length %u."
+ "Format: Check reformat\n"
+ "Format: Check reformat: Failed\n"
+ "Format: Flush data structures\n"
+ "Format: Flush data structures: Failed\n"
+ "Format: Prepare boot region\n"
+ "Format: Prepare boot region: Failed\n"
+ "Format: Preparing\n"
+ "Format: Preparing: Failed\n"
+ "Format: Wipe\n"
+ "Format: Wipe: Failed\n"
+ "Format: Write FAT tables\n"
+ "Format: Write bitmaps\n"
+ "Given volume name (%s) is invalid for this file system\n"
+ "Hash bitmap collision: index: %u\n"
+ "Inconsistent sectors per cluster (%u) and bytes per cluster (%u)\n"
+ "Invalid argument for option -%c: %s\n"
+ "Invalid bytes per cluster (%u); must be a power of two from 512 to 33554432\n"
+ "Invalid bytes per sector (%u); must be a power of two from 512 to 4096\n"
+ "Invalid number of FATs (%u); must be 1 or 2\n"
+ "Invalid number of FATs, or FAT or cluster offset; skipping reformat"
+ "Invalid sectors per cluster (%u); must be a power of two from 1 to 65536\n"
+ "Numeric overflow for option -%c: %s\n"
+ "Partition offset was not initialized , setting to default value (%d)\n"
+ "Sector size (%u) is too large\n"
+ "Sectors per FAT must be non-zero\n"
+ "Sectors per cluster (%u) too large; max is %u\n"
+ "T@\"FSBlockDeviceResource\",&,V_resource"
+ "UUID"
+ "[Error] :"
+ "[Info]: "
+ "_resource"
+ "connection"
+ "containerID"
+ "d: %d task %p msg %s connection %p"
+ "didCompleteWithError:"
+ "format"
+ "fsckMsgsPrintFormat"
+ "fsck_exfat_bitmap_cache_%@"
+ "fsck_exfat_bitmap_get_word"
+ "getVolumeNameAndUUID:useAlt:reply:"
+ "initWithVolumeID:volumeName:"
+ "localizedMessage:table:bundle:arguments:"
+ "name"
+ "nameWithString:"
+ "newfs_appex"
+ "objectAtIndexedSubscript:"
+ "ready"
+ "resource"
+ "result"
+ "setResource:"
+ "stringByAppendingPathComponent:"
+ "v24@0:8@16"
+ "v24@?0@\"FSProbeResult\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"NSUUID\"16@\"NSError\"24"
+ "v36@0:8@16B24@?28"
+ "v8@?0"
+ "volumeIdentifier"
+ "wipefs_alloc(): fd(%d) %s\n"
+ "wipefs_except_blocks(): fd(%d) %s\n"
+ "wipefs_wipe(): fd(%d) %s\n"
- "%@ "
- "%p"
- "%s"
- "%s\n"
- "%s: Can't allocate a FSCK context object"
- "%s: Can't allocate a wipe FS context object"
- "%s: No message connection object, can't log message"
- "%s: Sector size was not initialized, setting to default value (%d)"
- "%s: Total sectors was not initialized, setting to default value (%d)"
- "%s: could not get a device from resource"
- "%s: fstat failed, path (%s)"
- "-[exfatFileSystem checkResource:options:connection:taskID:progress:replyHandler:]"
- "-[exfatFileSystem formatResource:options:connection:taskID:progress:replyHandler:]"
- "-[exfatFileSystem getVolumeNameAndUUID:reply:]"
- "Could not convert name (%@) to precomposed UTF-16 little endian; may be too long"
- "Could not read FAT for cluster %u"
- "Could not read cluster %u"
- "Could not release cluster %u"
- "Encountered errors trying to wipe resource"
- "Failed to allocate temporary buffer"
- "Failed to start phase, error %s"
- "Format: Check reformat"
- "Format: Check reformat: Failed"
- "Format: Flush data structures"
- "Format: Flush data structures: Failed"
- "Format: Prepare boot region"
- "Format: Prepare boot region: Failed"
- "Format: Preparing"
- "Format: Preparing: Failed"
- "Format: Wipe"
- "Format: Wipe: Failed"
- "Format: Write FAT tables"
- "Format: Write bitmaps"
- "Given volume name (%@) is invalid for this file system"
- "I"
- "Inconsistent sectors per cluster (%u) and bytes per cluster (%u)"
- "Invalid argument for option -%c: %s"
- "Invalid bytes per cluster (%@); must be a power of two from 512 to 33554432"
- "Invalid bytes per sector (%@); must be a power of two from 512 to 4096"
- "Invalid number of FATs (%@); must be 1 or 2"
- "Invalid number of FATs, or FAT or cluster offset; skipping reformat\n"
- "Invalid sectors per cluster (%@); must be a power of two from 1 to 65536"
- "N"
- "Numeric overflow for option -%c: %s"
- "Partition offset was not initialized , setting to default value (%d)"
- "R"
- "S"
- "Sector size (%u) is too large"
- "Sectors per FAT must be non-zero"
- "Sectors per cluster (%u) too large; max is %u"
- "[ERROR] "
- "[INFO] "
- "[UNKNOWN] "
- "a"
- "addObject:"
- "b"
- "c"
- "checkResource:options:connection:taskID:progress:replyHandler:"
- "d"
- "didCompleteWithError:completionHandler:"
- "formatResource:options:connection:taskID:progress:replyHandler:"
- "fsck_exfat_bitmap_init"
- "g"
- "g.bitmap == NULL"
- "getVolumeNameAndUUID:reply:"
- "initWithFormat:"
- "initWithFormat:locale:"
- "locale"
- "localizedMessage:table:bundle:"
- "logLocalizedMessage:table:bundle:array:"
- "n"
- "numberWithInt:"
- "numberWithLong:"
- "option"
- "optionValue"
- "options"
- "q"
- "reason"
- "s"
- "stringByAppendingString:"
- "v"
- "v24@?0@\"NSString\"8@\"NSUUID\"16"
- "v64@0:8@16@24@32@40@48@?56"
- "wipefs_alloc(): fd(%d) %s"
- "wipefs_except_blocks(): fd(%d) %s"
- "wipefs_wipe(): fd(%d) %s"
- "writing backup boot sector"
- "writing main boot sector"
- "x"
- "y"

```
