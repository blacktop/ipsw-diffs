## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0x5a918
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x560c
-  __TEXT.__gcc_except_tab: 0xa12c
+3774.300.61.2.4
+  __TEXT.__text: 0x5c27c
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_methlist: 0x577c
+  __TEXT.__gcc_except_tab: 0xa3c4
   __TEXT.__const: 0xda
-  __TEXT.__cstring: 0x425b
-  __TEXT.__oslogstring: 0xda3
+  __TEXT.__cstring: 0x43bb
+  __TEXT.__oslogstring: 0xe9a
   __TEXT.__ustring: 0xee
   __TEXT.__swift5_typeref: 0xbd
   __TEXT.__swift5_capture: 0xd0

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x43fc
+  __TEXT.__unwind_info: 0x4518
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0xd6b
-  __TEXT.__objc_methname: 0xaea9
-  __TEXT.__objc_methtype: 0x1af1
-  __TEXT.__objc_stubs: 0x7da0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x1e88
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __TEXT.__objc_classname: 0xdc5
+  __TEXT.__objc_methname: 0xb233
+  __TEXT.__objc_methtype: 0x1b6a
+  __TEXT.__objc_stubs: 0x7f00
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1f18
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x100
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8940
-  __DATA_CONST.__objc_selrefs: 0x2fd8
+  __DATA_CONST.__objc_const: 0x8e38
+  __DATA_CONST.__objc_selrefs: 0x3080
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__objc_const: 0x3548
-  __AUTH_CONST.__const: 0xeb0
-  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0x3668
+  __AUTH_CONST.__const: 0xef0
+  __AUTH_CONST.__cfstring: 0x51e0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x9c0
-  __AUTH.__objc_data: 0x410
+  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x4f8
-  __DATA.__objc_superrefs: 0x340
-  __DATA.__objc_ivar: 0x49c
-  __DATA.__data: 0xf00
+  __DATA.__objc_classrefs: 0x508
+  __DATA.__objc_superrefs: 0x360
+  __DATA.__objc_ivar: 0x4d0
+  __DATA.__data: 0xf60
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0x100
   __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x308

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D08D44AE-3312-3619-BC6C-B6363A9719C3
-  Functions: 2329
-  Symbols:   9016
-  CStrings:  4024
+  UUID: 608CB9C1-CE22-3439-B1AA-A062DEC9A60A
+  Functions: 2372
+  Symbols:   9194
+  CStrings:  4090
 
Symbols:
+ +[EFPrivacy _roundQueryLogCount:maxCount:queryCount:]
+ +[EFPrivacy bucketValueForQueryLogCount:bucketValues:]
+ +[EFPrivacy numberOfDigits:]
+ +[EFPrivacy roundedInteger:]
+ -[EFProtectedFile .cxx_destruct]
+ -[EFProtectedFile assertion]
+ -[EFProtectedFile backgroundProcessingIsAllowed]
+ -[EFProtectedFile file]
+ -[EFProtectedFile initWithFilePath:isSensitive:protectionType:]
+ -[EFProtectedFile initWithFilePath:protectionType:]
+ -[EFProtectedFile initWithSensitiveFilePath:protectionType:]
+ -[EFProtectedFile requestBackgroundProcessingForDuration:error:]
+ -[EFProtectedFileGroup .cxx_destruct]
+ -[EFProtectedFileGroup assertion]
+ -[EFProtectedFileGroup backgroundProcessingIsAllowed]
+ -[EFProtectedFileGroup files]
+ -[EFProtectedFileGroup initWithFilePaths:isSensitive:protectionType:]
+ -[EFProtectedFileGroup initWithFilePaths:protectionType:]
+ -[EFProtectedFileGroup initWithSensitiveFilePaths:protectionType:]
+ -[EFProtectedFileGroup requestBackgroundProcessingForDuration:error:]
+ -[NSArray(EmailFoundationAdditions) ef_longestCommonPrefix]
+ -[_EFBackgroundProcessingAssertion .cxx_destruct]
+ -[_EFBackgroundProcessingAssertion _iterateFilesPerformingAction:error:]
+ -[_EFBackgroundProcessingAssertion _releaseAssertionWithError:]
+ -[_EFBackgroundProcessingAssertion _takeAssertionForDuration:error:]
+ -[_EFBackgroundProcessingAssertion decrementAssertion]
+ -[_EFBackgroundProcessingAssertion decrementAssertion].cold.1
+ -[_EFBackgroundProcessingAssertion incrementAssertionForDuration:error:]
+ -[_EFBackgroundProcessingAssertion initWithProtectedFiles:]
+ -[_EFBackgroundProcessingAssertion isActive]
+ -[_EFProtectedFile .cxx_destruct]
+ -[_EFProtectedFile description]
+ -[_EFProtectedFile ef_publicDescription]
+ -[_EFProtectedFile fileDescriptorWithError:]
+ -[_EFProtectedFile initWithFilePath:isSensitive:protectionType:]
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionCompleteWhenUserInactive
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_EFProtectedFile
+ _OBJC_CLASS_$_EFProtectedFileGroup
+ _OBJC_CLASS_$__EFBackgroundProcessingAssertion
+ _OBJC_CLASS_$__EFProtectedFile
+ _OBJC_IVAR_$_EFProtectedFile._assertion
+ _OBJC_IVAR_$_EFProtectedFile._file
+ _OBJC_IVAR_$_EFProtectedFileGroup._assertion
+ _OBJC_IVAR_$_EFProtectedFileGroup._files
+ _OBJC_IVAR_$__EFBackgroundProcessingAssertion._count
+ _OBJC_IVAR_$__EFBackgroundProcessingAssertion._currentExpiry
+ _OBJC_IVAR_$__EFBackgroundProcessingAssertion._lock
+ _OBJC_IVAR_$__EFBackgroundProcessingAssertion._protectedFiles
+ _OBJC_IVAR_$__EFProtectedFile._fileDescriptor
+ _OBJC_IVAR_$__EFProtectedFile._fileDescriptorLock
+ _OBJC_IVAR_$__EFProtectedFile._filePath
+ _OBJC_IVAR_$__EFProtectedFile._filePathIsSensitive
+ _OBJC_IVAR_$__EFProtectedFile._protectionClass
+ _OBJC_METACLASS_$_EFProtectedFile
+ _OBJC_METACLASS_$_EFProtectedFileGroup
+ _OBJC_METACLASS_$__EFBackgroundProcessingAssertion
+ _OBJC_METACLASS_$__EFProtectedFile
+ __OBJC_$_INSTANCE_METHODS_EFProtectedFile
+ __OBJC_$_INSTANCE_METHODS_EFProtectedFileGroup
+ __OBJC_$_INSTANCE_METHODS__EFBackgroundProcessingAssertion
+ __OBJC_$_INSTANCE_METHODS__EFProtectedFile
+ __OBJC_$_INSTANCE_VARIABLES_EFProtectedFile
+ __OBJC_$_INSTANCE_VARIABLES_EFProtectedFileGroup
+ __OBJC_$_INSTANCE_VARIABLES__EFBackgroundProcessingAssertion
+ __OBJC_$_INSTANCE_VARIABLES__EFProtectedFile
+ __OBJC_$_PROP_LIST_EFProtectedFile
+ __OBJC_$_PROP_LIST_EFProtectedFile.71
+ __OBJC_$_PROP_LIST_EFProtectedFileGroup
+ __OBJC_$_PROP_LIST__EFProtectedFile
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EFProtectedFile
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EFProtectedFile
+ __OBJC_$_PROTOCOL_REFS_EFProtectedFile
+ __OBJC_CLASS_PROTOCOLS_$_EFProtectedFile
+ __OBJC_CLASS_PROTOCOLS_$_EFProtectedFileGroup
+ __OBJC_CLASS_PROTOCOLS_$__EFProtectedFile
+ __OBJC_CLASS_RO_$_EFProtectedFile
+ __OBJC_CLASS_RO_$_EFProtectedFileGroup
+ __OBJC_CLASS_RO_$__EFBackgroundProcessingAssertion
+ __OBJC_CLASS_RO_$__EFProtectedFile
+ __OBJC_LABEL_PROTOCOL_$_EFProtectedFile
+ __OBJC_METACLASS_RO_$_EFProtectedFile
+ __OBJC_METACLASS_RO_$_EFProtectedFileGroup
+ __OBJC_METACLASS_RO_$__EFBackgroundProcessingAssertion
+ __OBJC_METACLASS_RO_$__EFProtectedFile
+ __OBJC_PROTOCOL_$_EFProtectedFile
+ ___59-[NSArray(EmailFoundationAdditions) ef_longestCommonPrefix]_block_invoke
+ ___63-[_EFBackgroundProcessingAssertion _releaseAssertionWithError:]_block_invoke
+ ___64-[EFProtectedFile requestBackgroundProcessingForDuration:error:]_block_invoke
+ ___68-[_EFBackgroundProcessingAssertion _takeAssertionForDuration:error:]_block_invoke
+ ___69-[EFProtectedFileGroup initWithFilePaths:isSensitive:protectionType:]_block_invoke
+ ___69-[EFProtectedFileGroup requestBackgroundProcessingForDuration:error:]_block_invoke
+ ____ef_log_EFProtectedFile_block_invoke
+ ___block_descriptor_32_e8_i12?0i8l
+ ___block_descriptor_40_ea8_32r_e43_"NSString"24?0"NSString"8"<NSObject>"16lr32l8
+ ___block_descriptor_41_ea8_32s_e36_"_EFProtectedFile"16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_i12?0i8l
+ ___block_literal_global.125
+ __ef_log_EFProtectedFile
+ __ef_log_EFProtectedFile.log
+ __ef_log_EFProtectedFile.onceToken
+ _fcntl
+ _objc_msgSend$_iterateFilesPerformingAction:error:
+ _objc_msgSend$_releaseAssertionWithError:
+ _objc_msgSend$_roundQueryLogCount:maxCount:queryCount:
+ _objc_msgSend$_takeAssertionForDuration:error:
+ _objc_msgSend$assertion
+ _objc_msgSend$commonPrefixWithString:options:
+ _objc_msgSend$ef_reduce:
+ _objc_msgSend$initWithFilePath:isSensitive:protectionType:
+ _objc_msgSend$initWithFilePaths:isSensitive:protectionType:
+ _objc_msgSend$logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:
+ _objc_msgSend$numberOfDigits:
+ _objc_msgSend$roundedInteger:placeValueDigits:
+ _open_dprotected_np
- GCC_except_table73
- _objc_msgSend$logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:
CStrings:
+ "\x01!"
+ "+[EFPrivacy bucketValueForQueryLogCount:bucketValues:]"
+ "0 && \"Fail to bucket query count value\""
+ "<depth=%lu>/%@"
+ "@\"<EFCancelable>\"32@0:8d16^@24"
+ "@\"NSString\"24@?0@\"NSString\"8@\"<NSObject>\"16"
+ "@\"_EFBackgroundProcessingAssertion\""
+ "@\"_EFProtectedFile\""
+ "@\"_EFProtectedFile\"16@?0@\"NSString\"8"
+ "B32@0:8d16^@24"
+ "Decrementing assertion when count is already 0"
+ "EFPrivacy.m"
+ "EFProtectedFile"
+ "EFProtectedFile.m"
+ "EFProtectedFileGroup"
+ "Failed to release assertion on files %{public}@ due to error: %{public}@"
+ "Failed to take assertion of duration %f on files %{public}@ due to error: %{public}@"
+ "Invalid number of values in queryBucketValues"
+ "Q40@0:8Q16Q24Q32"
+ "Released assertion on files %{public}@"
+ "T@\"NSArray\",R,N,V_files"
+ "T@\"_EFBackgroundProcessingAssertion\",R,N,V_assertion"
+ "T@\"_EFProtectedFile\",R,N,V_file"
+ "Took assertion of duration %f on files %{public}@"
+ "\\(\\?+(,( )*\\?+)*\\)"
+ "_EFBackgroundProcessingAssertion"
+ "_EFProtectedFile"
+ "_assertion"
+ "_count"
+ "_currentExpiry"
+ "_file"
+ "_fileDescriptor"
+ "_fileDescriptorLock"
+ "_filePath"
+ "_filePathIsSensitive"
+ "_files"
+ "_iterateFilesPerformingAction:error:"
+ "_protectedFiles"
+ "_protectionClass"
+ "_releaseAssertionWithError:"
+ "_roundQueryLogCount:maxCount:queryCount:"
+ "_takeAssertionForDuration:error:"
+ "assertion"
+ "backgroundProcessingIsAllowed"
+ "bucketValueForQueryLogCount:bucketValues:"
+ "commonPrefixWithString:options:"
+ "decrementAssertion"
+ "ef_longestCommonPrefix"
+ "file"
+ "files"
+ "i12@?0i8"
+ "initWithFilePath:isSensitive:protectionType:"
+ "initWithFilePath:protectionType:"
+ "initWithFilePaths:isSensitive:protectionType:"
+ "initWithFilePaths:protectionType:"
+ "initWithSensitiveFilePath:protectionType:"
+ "initWithSensitiveFilePaths:protectionType:"
+ "logQueryString:label:firstRowExecutionTimeInNanoseconds:totalExecutionTimeInNanoseconds:numberOfRows:"
+ "numberOfDigits:"
+ "requestBackgroundProcessingForDuration:error:"
+ "roundedInteger:"
- "\\(\\?+(, \\?+)*\\)"
- "logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:"

```
