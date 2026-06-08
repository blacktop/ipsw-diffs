## iWorkFileFormat

> `/System/Library/PrivateFrameworks/iWorkXPC.framework/XPCServices/iWorkFileFormat.xpc/iWorkFileFormat`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x165224
-  __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_stubs: 0x8f40
+30.0.0.0.0
+  __TEXT.__text: 0x16365c
+  __TEXT.__auth_stubs: 0x18e0
+  __TEXT.__objc_stubs: 0x90c0
   __TEXT.__init_offsets: 0x40
-  __TEXT.__objc_methlist: 0x6274
-  __TEXT.__const: 0xa650
-  __TEXT.__objc_classname: 0x1108
-  __TEXT.__objc_methname: 0xe2a7
-  __TEXT.__objc_methtype: 0x2800
-  __TEXT.__gcc_except_tab: 0xd2e4
-  __TEXT.__cstring: 0x12de2
-  __TEXT.__oslogstring: 0x65bf
+  __TEXT.__objc_methlist: 0x639c
+  __TEXT.__const: 0xa710
+  __TEXT.__objc_classname: 0xf0a
+  __TEXT.__objc_methname: 0xe4e3
+  __TEXT.__objc_methtype: 0x287b
+  __TEXT.__gcc_except_tab: 0xcc74
+  __TEXT.__cstring: 0x1340d
+  __TEXT.__oslogstring: 0x66f7
   __TEXT.__ustring: 0x76
-  __TEXT.__unwind_info: 0x8bc8
-  __DATA_CONST.__auth_got: 0xbd0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0xe780
-  __DATA_CONST.__cfstring: 0x2fe0
-  __DATA_CONST.__objc_classlist: 0x388
-  __DATA_CONST.__objc_catlist: 0x120
+  __TEXT.__swift5_typeref: 0x14
+  __TEXT.__unwind_info: 0x8d78
+  __DATA_CONST.__const: 0xe9b0
+  __DATA_CONST.__cfstring: 0x31a0
+  __DATA_CONST.__objc_classlist: 0x3b0
+  __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xa650
-  __DATA.__objc_selrefs: 0x35d8
-  __DATA.__objc_ivar: 0x624
-  __DATA.__objc_data: 0x2350
-  __DATA.__data: 0x2418
-  __DATA.__bss: 0xcb0
-  __DATA.__common: 0x2220
+  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA.__objc_const: 0xa960
+  __DATA.__objc_selrefs: 0x3688
+  __DATA.__objc_ivar: 0x62c
+  __DATA.__objc_data: 0x24e0
+  __DATA.__data: 0x2428
+  __DATA.__bss: 0xcd0
+  __DATA.__common: 0x2218
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D22104A4-D9C2-3B94-9C87-72661CA3A522
-  Functions: 8645
-  Symbols:   4326
-  CStrings:  5230
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 7F79EB22-A187-3360-9A1F-10A4A9234646
+  Functions: 8700
+  Symbols:   4352
+  CStrings:  5300
 
Symbols:
+ _NSURLErrorFailingURLErrorKey
+ _OBJC_CLASS_$_TSFBundleFinder
+ _OBJC_CLASS_$_TSUApplicationExecutionContext
+ _OBJC_CLASS_$_TSUApplicationExtensionExecutionContext
+ _OBJC_CLASS_$_TSUExecutionContext
+ _OBJC_CLASS_$_TSUOSLogSink
+ _OBJC_CLASS_$_TSUStdioLogSink
+ _OBJC_CLASS_$_UIApplication
+ _OBJC_METACLASS_$_TSFBundleFinder
+ _OBJC_METACLASS_$_TSUApplicationExecutionContext
+ _OBJC_METACLASS_$_TSUApplicationExtensionExecutionContext
+ _OBJC_METACLASS_$_TSUExecutionContext
+ _OBJC_METACLASS_$_TSUOSLogSink
+ _OBJC_METACLASS_$_TSUStdioLogSink
+ __os_log_fault_impl
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _arc4random_uniform
+ _fcopyfile
+ _getpwuid
+ _getuid
+ _malloc_size
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x6
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x27
- OBJC_IVAR_$_TSULogCatThreadSafeMutableSet._logCatQueue
- OBJC_IVAR_$_TSULogCatThreadSafeMutableSet._objects
- _OBJC_CLASS_$_TSULogCatThreadSafeMutableSet
- _OBJC_METACLASS_$_TSULogCatThreadSafeMutableSet
- _TSUFrameworkBundle
- _TSUPerformanceCat_init_token
- _TSUPerformanceCat_log_t
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- _objc_release_x10
CStrings:
+ "#%@"
+ "#%@ %s:%d %s"
+ "#Assert *** Assertion failure #%u: %{public}s %{public}s:%d Did not expect nil NSUIApplication!"
+ "#Assert *** Assertion failure #%u: %{public}s %{public}s:%d Setting sharedContext after it has already been set"
+ "%@ %@[%d] %@ %@ %s:%d %@"
+ "%c"
+ "%s\n"
+ "+[SFUCryptoUtils p_sha256HashFromBytes:length:]"
+ "+[TSUExecutionContext beginApplicationContext]"
+ "+[TSUExecutionContext sharedContext]"
+ "-[TSUApplicationExecutionContext performWithApplication:]"
+ "-[TSUExecutionContext application]"
+ "-[TSUExecutionContext isApplicationContext]"
+ "-[TSUExecutionContext isUILayoutRTL]"
+ "-[TSUExecutionContext performWithApplication:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iWorkXPC/shared/utility/TSUExecutionContext.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iWorkXPC/submodules/app-content-hub/fundamentals/TSFundamentals/Casts/TSUCast.m"
+ "@\"NSDateFormatter\""
+ "@32@0:8r^v16Q24"
+ "@?24@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16"
+ "B32@0:8@16d24"
+ "Copy file failed. Error:%s(%d)"
+ "DEADBEEF-DEAD-BEEF-DEAD-"
+ "Did not expect nil NSUIApplication!"
+ "Failed to copy from \"%@\" to \"%@\". Error: errorClass=%{public}@, domain=%{public}@, code=%zd (%@) "
+ "NSUserDefaults_TSULogAdditions"
+ "Open destination file failed. URL:%@, Error:%s(%d)"
+ "Open source file failed. URL:%@, Error:%s(%d)"
+ "Setting sharedContext after it has already been set"
+ "Source file is not a regular file. URL:%@"
+ "Successfully copied single file from \"%@\" to \"%@\"."
+ "T@\"TSUExecutionContext\",&,N"
+ "T@\"UIApplication\",R,N"
+ "T@?,R,C,N"
+ "TSFBundleFinder"
+ "TSUApplicationExecutionContext"
+ "TSUApplicationExtensionExecutionContext"
+ "TSUExecutionContext"
+ "TSUExecutionContextErrorDomain"
+ "TSUOSLogSink"
+ "TSUStdioLogSink"
+ "TSUStdioLogSinkQueue"
+ "Will copy file from \"%@\" to \"%@\"."
+ "[Debug]"
+ "[Error]"
+ "[Fault]"
+ "[Info]"
+ "[Notice]"
+ "_dateFormatter"
+ "_logQueue"
+ "_sharedContext"
+ "application"
+ "beginApplicationContext"
+ "beginApplicationExtensionContext"
+ "characterDirectionForLanguage:"
+ "compressedDataUsingAlgorithm:error:"
+ "fstat failed. URL:%@, Error:%s(%d)"
+ "initWithDocumentIdentifier:"
+ "initWithEphemeralDocumentIdentifier:"
+ "isApplicationContext"
+ "isUILayoutRTL"
+ "logSinkBlock"
+ "logSinkBlockWithFilePointer:"
+ "mainBundle"
+ "makeInvalidContextError"
+ "p_copySingleFileAtURL:toURL:error:"
+ "p_sha256HashFromBytes:length:"
+ "performWithApplication:"
+ "preferredLocalizations"
+ "processIdentifier"
+ "processName"
+ "setDateFormat:"
+ "setFormatterBehavior:"
+ "setSharedContext:"
+ "sha256HashFromCryptoKey:"
+ "sharedApplication"
+ "sharedContext"
+ "tsu_UUIDForFakePremiumContent"
+ "tsu_UUIDZero"
+ "tsu_isAfterDate:byAtLeast:"
+ "tsu_isBeforeDate:byAtLeast:"
+ "tsu_isEqualToUUID:"
+ "userInterfaceLayoutDirection"
+ "v40@?0i8@\"NSString\"12r*20i28@\"NSString\"32"
+ "yyyy-MM-dd HH:mm:ss.SSS"
- "#Assert *** Assertion failure #%u: %{public}s %{public}s:%d overflow  in sha256HashFromData"
- "+[SFUCryptoUtils sha256HashFromData:]"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iWorkXPC/shared/utility/TSUCast.m"
- ";"
- "@24@0:8d16"
- "Defaults"
- "NSUserDefaults_TSUAdditions"
- "TSULogCatQueue"
- "TSULogCatThreadSafeMutableSet"
- "TSUPerformanceCat"
- "Td,R,N"
- "URLForResource:withExtension:"
- "_logCatQueue"
- "_objects"
- "caseInsensitiveCompare:"
- "d16@0:8"
- "dictionaryWithContentsOfURL:"
- "immutableSet"
- "overflow  in sha256HashFromData"
- "plist"
- "proto"
- "registerDefaults:"
- "tsu_CGFloatValue"
- "tsu_isAlmostEqual:"
- "tsu_isFloatingPointType"
- "tsu_numberWithCGFloat:"
- "{"

```
