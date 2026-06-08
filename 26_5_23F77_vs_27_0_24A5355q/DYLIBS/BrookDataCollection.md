## BrookDataCollection

> `/System/Library/PrivateFrameworks/BrookDataCollection.framework/BrookDataCollection`

```diff

-248.0.0.0.0
-  __TEXT.__text: 0x50e4
-  __TEXT.__auth_stubs: 0x620
+252.0.0.0.0
+  __TEXT.__text: 0x4b04
   __TEXT.__objc_methlist: 0x784
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1251
-  __TEXT.__oslogstring: 0x44f
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x1285
+  __TEXT.__oslogstring: 0x470
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x240
-  __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methname: 0x11a7
-  __TEXT.__objc_methtype: 0x3df
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x128
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e0
+  __DATA_CONST.__objc_selrefs: 0x5e8
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x128
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__cfstring: 0x5a0
   __AUTH_CONST.__objc_const: 0x1648
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7C3C29D7-D443-3347-9911-3EE57E97A3E1
-  Functions: 162
-  Symbols:   773
-  CStrings:  437
+  UUID: 8EA454C9-A1CB-3B9D-BB3E-A2AC0377238E
+  Functions: 159
+  Symbols:   771
+  CStrings:  134
 
Symbols:
+ GCC_except_table24
+ ___46-[BRKDataCollectionLogger _purgeOutdatedFiles]_block_invoke
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setBool:forKey:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- GCC_except_table23
- _BRKFileModifiedDate
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
- _objc_msgSend$timeIntervalSinceNow
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "DataCollectionFinalPurgeComplete"
+ "Final data collection purge complete."
+ "Successfully purged data collection storage directory."
- "#16@0:8"
- ".cxx_destruct"
- "@\"BRKDataCollectionScheduler\""
- "@\"BRKSettings\""
- "@\"NSBackgroundActivityScheduler\""
- "@\"NSData\""
- "@\"NSDateFormatter\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSOutputStream\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@40@0:8#16@24@?32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24@32B40"
- "@56@0:8@16@24@32@40@48"
- "AWSAccessKeyID"
- "AWSCanonicalizedResourceWithBucket:FileName:"
- "AWSSecretAccessKey"
- "AWSStringToSignWithHTTPVerb:contentMD5:contentType:date:canonicalizedResource:"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8^@16@24"
- "B32@0:8^s16^q24"
- "B48@0:8@16^@24^@32^@40"
- "BRKAccelerationBufferedFileWriter"
- "BRKAccelerationFileWriter"
- "BRKAccelerationWriter"
- "BRKAudioFileReader"
- "BRKAudioFileWriter"
- "BRKAudioWriter"
- "BRKDataCollectionBundle"
- "BRKDataCollectionLogger"
- "BRKDataCollectionScheduler"
- "BRKLogFileWriter"
- "BRKLogWriter"
- "BRKMetricsLogger"
- "BRKWriter"
- "NSObject"
- "Purged outdated log files"
- "Q"
- "Q16@0:8"
- "S3"
- "S3AccessConfig"
- "S3Content"
- "S3ContentConfig"
- "T#,R"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",&,N,V_content"
- "T@\"NSData\",R,N"
- "T@\"NSString\",&,N,V_AWSAccessKeyID"
- "T@\"NSString\",&,N,V_AWSSecretAccessKey"
- "T@\"NSString\",&,N,V_bucket"
- "T@\"NSString\",&,N,V_filename"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_basePath"
- "T@\"NSString\",R,N,V_folderName"
- "T@\"NSString\",R,N,V_path"
- "TB,N,V_gzip"
- "TB,R,N,V_isPackaged"
- "TQ,R"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unable to remove stale file %@ %@"
- "Vv16@0:8"
- "^{OpaqueExtAudioFile=}"
- "^{_NSZone=}16@0:8"
- "_AWSAccessKeyID"
- "_AWSSecretAccessKey"
- "_audioFile"
- "_basePath"
- "_bucket"
- "_content"
- "_coreAnalyticsKeyForMetricKey:"
- "_dataCollectionEnabled"
- "_dataCollectionIsAllowedToRunInCurrentProcess"
- "_dateFormatter"
- "_deviceIdentifier"
- "_externalDailyDeviceIdentifier"
- "_externalDailySessionUploadCount"
- "_filename"
- "_folderName"
- "_forceUpload"
- "_format"
- "_formatHTTPDate:"
- "_gzip"
- "_gzipCompressData:"
- "_gzipContentCache"
- "_idsFileListPath"
- "_idsFilesList"
- "_init"
- "_internalDeviceIdentifier"
- "_isPackaged"
- "_json"
- "_lock"
- "_lock_close"
- "_lock_openWithDataCount:"
- "_lock_writeJSON:"
- "_lock_writeSamples:count:"
- "_lock_writeX:y:z:timestamp:"
- "_logUploadWithPath:"
- "_manifest"
- "_outputStream"
- "_path"
- "_pathExtension:"
- "_purgeFilesForOSUpdate"
- "_purgeOutdatedFiles"
- "_queue"
- "_queue_schedule:"
- "_queue_setSchedulerCriteria"
- "_refreshExternalDeviceMetadata"
- "_scheduleUploadTimer"
- "_scheduler"
- "_secureRandomOfLength:"
- "_sema"
- "_setAdditionalXPCActivityProperties:"
- "_settings"
- "_shouldAllowDataCollectionUpload"
- "_storageDirectory"
- "_stringByRemovingPathExtension:"
- "_triggerUpload:"
- "_uploadScheduler"
- "_values"
- "_writeData:toFile:updateManifest:"
- "_writerForClass:file:configuration:"
- "_writers"
- "_writersLock"
- "accelerationWriterForFile:"
- "accelerationWriterForFile:valueCount:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addedFiles"
- "allObjects"
- "appendBytes:length:"
- "appendData:"
- "archiveDirectoryAt:deleteOriginal:"
- "array"
- "arrayWithContentsOfFile:"
- "audioWriterForFile:"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "basePath"
- "bucket"
- "bytes"
- "class"
- "clearCollectedData"
- "close"
- "closeWriterForFile:"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "content"
- "copy"
- "copyItemAtPath:toPath:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "date"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultLogDirectory"
- "defaultManager"
- "description"
- "deviceIdentifier"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "fileFrameCount"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filename"
- "folderName"
- "gzip"
- "gzipContent"
- "hasSuffix:"
- "hash"
- "init"
- "initToFileAtPath:append:"
- "initWithAWSAccessKeyID:AWSSecretAccessKey:"
- "initWithBase64EncodedString:options:"
- "initWithContent:filename:bucket:gzip:"
- "initWithFilename:bucket:"
- "initWithFolderNamed:"
- "initWithIdentifier:"
- "initWithPath:"
- "initWithSuiteName:"
- "isDataCollectionEnabled"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPackaged"
- "isProxy"
- "lastObject"
- "lastPathComponent"
- "length"
- "lengthOfBytesUsingEncoding:"
- "logEventName:eventPayLoad:"
- "logWriterForFile:"
- "lowercaseString"
- "markFileForUpload:"
- "mimeType"
- "mutableBytes"
- "mutableCopy"
- "numberWithDouble:"
- "objectForKeyedSubscript:"
- "open"
- "openWithDataCount:"
- "packageBundleToPath:filePrioritization:"
- "path"
- "pathExtension"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithLock:"
- "q16@0:8"
- "readData:count:"
- "release"
- "removeBundle"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeLastObject"
- "removeObject:"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "s3_decryptAESWithCiphertext:key:iv:"
- "s3_encryptAESWithPlaintext:ciphertext:key:iv:"
- "s3_encryptPlaintext:"
- "s3_setS3HeadersWithContent:accessConfig:"
- "schedule:"
- "scheduleWithBlock:"
- "self"
- "set"
- "setAWSAccessKeyID:"
- "setAWSSecretAccessKey:"
- "setBucket:"
- "setContent:"
- "setDateFormat:"
- "setFilename:"
- "setGzip:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setLength:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setTimeZone:"
- "setValue:forHTTPHeaderField:"
- "settingsForActiveDevice"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForKey:"
- "stringFromDate:"
- "stringWithFormat:"
- "substringToIndex:"
- "superclass"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timeZoneWithAbbreviation:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v32@0:8r^s16Q24"
- "v36@0:8@16@24B32"
- "v48@0:8d16d24d32d40"
- "write:maxLength:"
- "writeData:toFile:"
- "writeJSON:"
- "writeJSON:toFile:"
- "writeSamples:count:"
- "writeToFile:atomically:"
- "writeX:y:z:timestamp:"
- "zone"
- "{AudioStreamBasicDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
