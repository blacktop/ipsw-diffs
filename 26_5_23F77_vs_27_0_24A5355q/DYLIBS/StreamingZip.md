## StreamingZip

> `/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`

```diff

-252.0.0.0.0
-  __TEXT.__text: 0x124bc
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x16a
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__cstring: 0x1cb9
-  __TEXT.__oslogstring: 0x362e
-  __TEXT.__unwind_info: 0x280
-  __TEXT.__objc_classname: 0xc9
-  __TEXT.__objc_methname: 0xf13
-  __TEXT.__objc_methtype: 0x46e
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0xad8
+256.0.0.0.0
+  __TEXT.__text: 0x123cc
+  __TEXT.__objc_methlist: 0x6b4
+  __TEXT.__const: 0x170
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__cstring: 0x1cf5
+  __TEXT.__oslogstring: 0x3655
+  __TEXT.__unwind_info: 0x2c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xb28
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x628
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x6c0
+  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__objc_const: 0x6f0
+  __AUTH_CONST.__auth_got: 0x610
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x308
-  __DATA.__bss: 0x50
+  __DATA.__data: 0x380
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libAppleArchive.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B326FAC2-E2EB-3E48-A482-D534996C499D
-  Functions: 158
-  Symbols:   853
-  CStrings:  871
+  UUID: 202FFA49-FF84-3BAB-B98A-EFA579C0E623
+  Functions: 171
+  Symbols:   887
+  CStrings:  637
 
Symbols:
+ -[SZExtractor _finishStreamSynchronously:withCompletion:]
+ -[SZExtractor _prepareForExtractionSynchronously:withCompletion:]
+ -[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]
+ -[SZExtractor _supplyBytes:synchronously:withCompletion:]
+ -[SZExtractor _suspendStreamSynchronously:withCompletion:]
+ -[SZExtractor _terminateStreamSynchronously:clientError:withCompletion:]
+ -[SZExtractor finishStreamWithError:]
+ -[SZExtractor prepareForExtractionToPath:resumptionOffset:error:]
+ -[SZExtractor prepareForExtractionWithResumptionOffset:error:]
+ -[SZExtractor supplyBytes:dataComplete:error:]
+ -[SZExtractor suspendStreamWithResumptionOffset:error:]
+ -[SZExtractor terminateStreamWithError:error:]
+ GCC_except_table106
+ GCC_except_table17
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table55
+ GCC_except_table61
+ GCC_except_table69
+ GCC_except_table79
+ __OBJC_$_PROP_LIST_SZExtractor.436
+ ___37-[SZExtractor finishStreamWithError:]_block_invoke
+ ___46-[SZExtractor supplyBytes:dataComplete:error:]_block_invoke
+ ___46-[SZExtractor terminateStreamWithError:error:]_block_invoke
+ ___55-[SZExtractor suspendStreamWithResumptionOffset:error:]_block_invoke
+ ___57-[SZExtractor _finishStreamSynchronously:withCompletion:]_block_invoke
+ ___57-[SZExtractor _finishStreamSynchronously:withCompletion:]_block_invoke_2
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.162
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.175
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.180
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.181
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.183
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.208
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.209
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke.213
+ ___57-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke_2
+ ___58-[SZExtractor _suspendStreamSynchronously:withCompletion:]_block_invoke
+ ___58-[SZExtractor _suspendStreamSynchronously:withCompletion:]_block_invoke_2
+ ___62-[SZExtractor prepareForExtractionWithResumptionOffset:error:]_block_invoke
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_2
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_2.109
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_2.113
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_2.85
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_3
+ ___71-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke_4
+ ___72-[SZExtractor _terminateStreamSynchronously:clientError:withCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e20_v20?0"NSError"8B16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
+ ___block_descriptor_57_e8_32s40r48r_e23_v28?0"NSError"8B16Q20lr40l8r48l8s32l8
+ ___block_descriptor_89_e8_32s40s48s56bs64bs72r80r_e5_v8?0ls32l8s40l8s56l8s48l8s64l8r72l8r80l8
+ ___block_literal_global.95
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_finishStreamSynchronously:withCompletion:
+ _objc_msgSend$_prepareForExtractionSynchronously:withCompletion:
+ _objc_msgSend$_prepareForRemoteExtractionSynchronously:withCompletion:
+ _objc_msgSend$_supplyBytes:synchronously:withCompletion:
+ _objc_msgSend$_suspendStreamSynchronously:withCompletion:
+ _objc_msgSend$_terminateStreamSynchronously:clientError:withCompletion:
+ _objc_msgSend$prepareForExtractionWithResumptionOffset:error:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
- -[SZExtractor _prepareForExtractionSynchronously:withCompletionBlock:]
- -[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]
- -[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:]
- GCC_except_table27
- GCC_except_table33
- GCC_except_table48
- GCC_except_table56
- GCC_except_table66
- GCC_except_table93
- __OBJC_$_PROP_LIST_SZExtractor.412
- ___47-[SZExtractor finishStreamWithCompletionBlock:]_block_invoke
- ___47-[SZExtractor finishStreamWithCompletionBlock:]_block_invoke_2
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.163
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.170
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.175
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.176
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.178
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.203
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.204
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.208
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2
- ___56-[SZExtractor terminateStreamWithError:completionBlock:]_block_invoke
- ___56-[SZExtractor terminateStreamWithError:completionBlock:]_block_invoke_2
- ___73-[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:]_block_invoke
- ___73-[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:]_block_invoke_2
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.110
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.114
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.86
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_3
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_4
- ___block_descriptor_56_e8_32s40r48r_e23_v28?0"NSError"8B16Q20lr40l8r48l8s32l8
- ___block_descriptor_88_e8_32s40s48s56bs64bs72r80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8
- ___block_literal_global.109
- _objc_msgSend$_prepareForExtractionSynchronously:withCompletionBlock:
- _objc_msgSend$_prepareForRemoteExtractionSynchronously:withCompletionBlock:
- _objc_msgSend$_suspendStreamWithCompletionBlockSynchronously:completion:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x9
CStrings:
+ "-[SZExtractor _finishStreamSynchronously:withCompletion:]"
+ "-[SZExtractor _prepareForExtractionSynchronously:withCompletion:]"
+ "-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletion:]_block_invoke"
+ "-[SZExtractor _supplyBytes:synchronously:withCompletion:]"
+ "-[SZExtractor _supplyBytes:synchronously:withCompletion:]_block_invoke_2"
+ "-[SZExtractor _suspendStreamSynchronously:withCompletion:]"
+ "-[SZExtractor _terminateStreamSynchronously:clientError:withCompletion:]"
+ "Failed to create dispatch_group_t"
+ "Failed to create dispatch_group_t : %@"
- "#16@0:8"
- "-[SZExtractor _prepareForExtractionSynchronously:withCompletionBlock:]"
- "-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke"
- "-[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:]"
- "-[SZExtractor finishStreamWithCompletionBlock:]"
- "-[SZExtractor supplyBytes:withCompletionBlock:]"
- "-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2"
- "-[SZExtractor terminateStreamWithError:completionBlock:]"
- ".cxx_destruct"
- "@\"<STExtractorDelegate>\"16@0:8"
- "@\"<SZExtractorDelegate>\""
- "@\"<SZExtractorDelegate>\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"SZExtractorInternalDelegate\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16^Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24^Q32"
- "@48@0:8@16@24Q32^Q40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^Q16"
- "B40@0:8@16@24^@32"
- "KnownImplementations"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PrivateInterfaces"
- "Q"
- "Q16@0:8"
- "STExtractor"
- "SZExtractor"
- "SZExtractorInternalDelegate"
- "StreamingUnzipDelegateProtocol"
- "StreamingUnzipProtocol"
- "T#,R"
- "T@\"<STExtractorDelegate>\",W,N"
- "T@\"<SZExtractorDelegate>\",W,N"
- "T@\"NSDictionary\",R,C,N,V_options"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_serialQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_extractionPath"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",R,N,V_unzipServiceConnection"
- "T@\"SZExtractorInternalDelegate\",R,N,V_internalExtractorDelegate"
- "TB,?,R,D,N"
- "TB,?,R,N"
- "TB,N,V_hasHadPostSetupMethodsCalled"
- "TB,N,V_needsPreparation"
- "TB,N,V_privileged"
- "TB,R"
- "TQ,N,V_lastResumptionOffset"
- "TQ,R"
- "Testing"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_error"
- "_extractionPath"
- "_hasHadPostSetupMethodsCalled"
- "_internalExtractorDelegate"
- "_invalidateObject"
- "_isValidObject"
- "_ivarLock"
- "_lastResumptionOffset"
- "_needsPreparation"
- "_options"
- "_prepareForExtractionSynchronously:withCompletionBlock:"
- "_prepareForRemoteExtractionSynchronously:withCompletionBlock:"
- "_privileged"
- "_runWithLock:"
- "_serialQueue"
- "_serviceConnectionWithError:"
- "_setUpWithPath:options:error:"
- "_suspendStreamWithCompletionBlockSynchronously:completion:"
- "_synchronouslyPrepareForExtractionAtOffset:"
- "_unzipServiceConnection"
- "addObject:"
- "allocWithZone:"
- "autorelease"
- "availableExtractionMemory"
- "boolValue"
- "class"
- "conformsToProtocol:"
- "connection"
- "copy"
- "copyWithZone:"
- "count"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodePropertyListForKey:"
- "defaultManager"
- "delegate"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "doesConsumeExtractedData"
- "enableDebugLogging"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateByteRangesUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "extractionCompleteAtArchivePath:"
- "extractionEnteredPassThroughMode"
- "extractorDelegate"
- "fileExistsAtPath:"
- "fileSystemRepresentationWithPath:"
- "finishStreamWithCompletionBlock:"
- "finishStreamWithReply:"
- "getPidForTestingWithReply:"
- "hasHadPostSetupMethodsCalled"
- "hash"
- "i24@0:8^@16"
- "init"
- "initForLocalExtractionWithPath:options:resumptionOffset:"
- "initForRemoteExtractionWithPath:options:resumptionOffset:"
- "initWithCoder:"
- "initWithFormat:arguments:"
- "initWithOptions:"
- "initWithOptions:error:"
- "initWithPath:md5Hashes:hashedChunkSize:resumptionOffset:"
- "initWithPath:options:"
- "initWithPath:options:error:"
- "initWithPath:options:resumptionOffset:"
- "initWithPath:resumptionOffset:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "internalExtractorDelegate"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "knownSZExtractorImplementations"
- "lastPathComponent"
- "lastResumptionOffset"
- "length"
- "maxAvailableExtractionMemory"
- "needsPreparation"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prepareForExtraction:"
- "prepareForExtractionToPath:completionBlock:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "serialQueue"
- "servicePIDWithError:"
- "setActiveDelegateMethods:"
- "setActiveExtractorDelegateMethods:"
- "setDelegate:"
- "setError:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtractionPath:"
- "setExtractionProgress:"
- "setExtractorDelegate:"
- "setHasHadPostSetupMethodsCalled:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastResumptionOffset:"
- "setNeedsPreparation:"
- "setObject:forKeyedSubscript:"
- "setPrivileged:"
- "setRemoteObjectInterface:"
- "setUnzipServiceConnection:"
- "setWithObject:"
- "setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:"
- "stringByDeletingLastPathComponent"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subdataWithRange:"
- "superclass"
- "supplyBytes:withCompletionBlock:"
- "supplyBytes:withReply:"
- "supportsSecureCoding"
- "suspendStreamWithCompletionBlock:"
- "suspendStreamWithReply:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "terminateStreamWithError:completionBlock:"
- "terminateStreamWithReply:"
- "unzipServiceConnection"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<STExtractorDelegate>\"16"
- "v24@0:8@\"<SZExtractorDelegate>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?i@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8B16@?20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\"B>24"
- "v32@0:8@\"NSError\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@16@?24"
- "v48@0:8@\"NSString\"16*24@\"NSDictionary\"32@?<v@?@\"NSError\"Q>40"
- "v48@0:8@16*24@32@?40"
- "valueForEntitlement:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
