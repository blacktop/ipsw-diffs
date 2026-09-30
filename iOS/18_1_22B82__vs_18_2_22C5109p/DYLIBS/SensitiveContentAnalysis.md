## SensitiveContentAnalysis

> `/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis`

```diff

-75.3.105.0.0
-  __TEXT.__text: 0x5a4c
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x3e4
-  __TEXT.__const: 0x11a
-  __TEXT.__cstring: 0x32b
+84.5.0.0.0
+  __TEXT.__text: 0xc8ec
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x438
+  __TEXT.__const: 0xda4
+  __TEXT.__cstring: 0x760
   __TEXT.__oslogstring: 0x456
   __TEXT.__gcc_except_tab: 0x228
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_typeref: 0x40
-  __TEXT.__swift5_reflstr: 0x1a
-  __TEXT.__swift5_fieldmd: 0x34
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x280
-  __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0xe3f
-  __TEXT.__objc_methtype: 0x23c
+  __TEXT.__constg_swiftt: 0x208
+  __TEXT.__swift5_typeref: 0x39f
+  __TEXT.__swift5_reflstr: 0x161
+  __TEXT.__swift5_fieldmd: 0x1c8
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__eh_frame: 0x4f0
+  __TEXT.__objc_classname: 0x97
+  __TEXT.__objc_methname: 0xf08
+  __TEXT.__objc_methtype: 0x23e
   __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_selrefs: 0x3c8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x88
+  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_ptr: 0x268
+  __AUTH_CONST.__const: 0x560
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x718
-  __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x28
-  __DATA.__bss: 0x50
+  __AUTH_CONST.__objc_const: 0x828
+  __AUTH.__objc_data: 0x48
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x20
+  __DATA.__data: 0x200
+  __DATA.__bss: 0x1940
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__objc_data: 0x2a8
+  __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_signal.dylib
   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 159
-  Symbols:   289
-  CStrings:  236
+  Functions: 459
+  Symbols:   338
+  CStrings:  272
 
Symbols:
+ _NSPOSIXErrorDomain
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _objc_allocWithZone
+ _objc_autorelease
+ _swift_allocBox
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_makeBoxUnique
+ _swift_once
+ _swift_retain_n
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
CStrings:
+ "$defaultActor"
+ "@32@0:8@16^@24"
+ "B24@0:8^@16"
+ "Communication Safety (Over 13)"
+ "Communication Safety (Under 13)"
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to encode analysis"
+ "Fatal error"
+ "Invalid number of keys found, expected one."
+ "Sensitive Content Warning"
+ "SensitiveContentAnalysis.SCSensitivityAnalysis"
+ "SensitiveContentAnalysis/SCSensitivityAnalysis+Implementation.swift"
+ "SensitiveContentAnalysis/SensitiveContentPolicy.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/UnsafePointer.swift"
+ "T@\"NSData\",N,R"
+ "TB,N,R"
+ "Unexpected SCAnalysisFeatureEnablement value"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "_TtC24SensitiveContentAnalysisP33_4D89A8A00028CF3643711B7990FDFFDA31PolicyCachingSequenceDispatcher"
+ "_analysis"
+ "analyzeFile:options:progressHandler:completionHandler:"
+ "currentPersonaUniqueID"
+ "currentPolicy"
+ "dataRepresentation"
+ "errorWithDomain:code:userInfo:"
+ "initWithDataRepresentation:error:"
+ "initWithNudityDetectionValue:"
+ "prefetchSensitiveContentPolicy"
+ "shouldAnalyzeMedia:"
+ "shouldAnalyzeMediaWithType:error:"
+ "shouldFilterStickersAndTapbacks"
+ "task"
+ "v16@?0q8"
+ "v48@0:8@16Q24@?32@?40"
+ "waiters"
- "B"
- "TB,GisSensitive,V_sensitive"
- "_sensitive"
- "resultsWithSensitive:"
- "setSensitive:"
- "v20@0:8B16"

```
