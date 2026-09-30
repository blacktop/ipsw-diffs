## AACClient

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/Frameworks/AACClient.framework/Versions/A/AACClient`

```diff

-14.2.5.0.0
-  __TEXT.__text: 0x19bb4
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x608
-  __TEXT.__const: 0x1440
-  __TEXT.__cstring: 0x1779
-  __TEXT.__swift5_typeref: 0xe1b
-  __TEXT.__swift5_reflstr: 0x96b
+14.2.9.0.0
+  __TEXT.__text: 0x1b014
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0xb50
+  __TEXT.__const: 0x1380
+  __TEXT.__cstring: 0x1579
+  __TEXT.__swift5_typeref: 0xe0b
+  __TEXT.__swift5_reflstr: 0x99b
   __TEXT.__swift5_assocty: 0xc8
-  __TEXT.__constg_swiftt: 0x135c
+  __TEXT.__constg_swiftt: 0x1340
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_fieldmd: 0x900
-  __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0xb0
-  __TEXT.__swift5_capture: 0x58c
+  __TEXT.__swift5_fieldmd: 0x908
+  __TEXT.__swift5_proto: 0xb8
+  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift5_capture: 0x534
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__oslogstring: 0x36a
-  __TEXT.__unwind_info: 0x858
-  __TEXT.__eh_frame: 0x128
+  __TEXT.__oslogstring: 0x49a
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__eh_frame: 0x480
   __TEXT.__objc_classname: 0x25f
-  __TEXT.__objc_methname: 0x12cd
-  __TEXT.__objc_methtype: 0x7a0
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x160
+  __TEXT.__objc_methname: 0x13bb
+  __TEXT.__objc_methtype: 0x7a8
+  __TEXT.__objc_stubs: 0x620
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x410
+  __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x1bb0
-  __AUTH_CONST.__objc_const: 0x2638
-  __AUTH.__objc_data: 0x710
-  __AUTH.__data: 0xc10
-  __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x11a8
-  __DATA.__bss: 0x1100
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x19b8
+  __AUTH_CONST.__objc_const: 0x1f80
+  __AUTH.__objc_data: 0x6b8
+  __AUTH.__data: 0xbe0
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x11d8
+  __DATA.__bss: 0xf80
   __DATA.__common: 0x80
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Versions/A/Frameworks/AACDependencies.framework/Versions/A/AACDependencies
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AACCore.framework/Versions/A/AACCore
+  - /System/Library/PrivateFrameworks/Catalyst.framework/Versions/A/Catalyst
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FC7CD995-4D47-378A-9856-12162CBFBBC2
-  Functions: 896
-  Symbols:   822
-  CStrings:  477
+  UUID: CDFD35BB-ED07-3E86-A06E-E05E4014CB23
+  Functions: 903
+  Symbols:   831
+  CStrings:  488
 
Symbols:
+ -[AECAssessmentConfigurationWrapper allowsKeyboardMathSolving]
+ -[AECAssessmentConfigurationWrapper allowsMathPaperSolving]
+ -[AECAssessmentConfigurationWrapper setAllowsKeyboardMathSolving:]
+ -[AECAssessmentConfigurationWrapper setAllowsMathPaperSolving:]
+ OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsKeyboardMathSolving
+ OBJC_IVAR_$_AECAssessmentConfigurationWrapper._allowsMathPaperSolving
+ __OBJC_$_PROP_LIST_AEProcessInfoPrimitives
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_boxed_opaque_existential_0
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AACClient
+ _objc_msgSend$allowsKeyboardMathSolving
+ _objc_msgSend$allowsMathPaperSolving
+ _objc_msgSend$setAllowsKeyboardMathSolving:
+ _objc_msgSend$setAllowsMathPaperSolving:
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_willThrow
+ _symbolic Sccy______p______pG So23AEDSingleAppModeSessionP s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic SdSg
+ _symbolic _____ 8Catalyst13CATSerializerC
+ block_copy_helper.12
+ block_copy_helper.29
+ block_descriptor.14
+ block_descriptor.31
+ block_destroy_helper.13
+ block_destroy_helper.30
+ keypath_get.14Tm
+ keypath_set.15Tm
+ objectdestroy.36Tm
- _associated conformance 9AACClient28AECSingleAppModeTogglerErrorOSHAASQ
- _swift_arrayDestroy
- _swift_unknownObjectRetain_n
- _symbolic Sayy______pSgcG s5ErrorP
- _symbolic _____ 9AACClient28AECSingleAppModeTogglerErrorO
- _symbolic ______pSg s5ErrorP
- _symbolic _____yy______pSgcG s23_ContiguousArrayStorageC s5ErrorP
- _symbolic yyc
- block_copy_helper.20
- block_copy_helper.31
- block_copy_helper.37
- block_copy_helper.43
- block_copy_helper.49
- block_descriptor.22
- block_descriptor.33
- block_descriptor.39
- block_descriptor.45
- block_descriptor.51
- block_destroy_helper.21
- block_destroy_helper.32
- block_destroy_helper.38
- block_destroy_helper.44
- block_destroy_helper.50
- keypath_get.12Tm
- keypath_set.13Tm
- objectdestroy.30Tm
- objectdestroy.41Tm
CStrings:
+ "Activated SAM"
+ "Client beginning SAM"
+ "Client ending SAM"
+ "Deactivated SAM"
+ "Failed to activate SAM: %{public}@"
+ "Failed to deactive SAM: %{public}@"
+ "Finished waiting for minimum session duration."
+ "Minimum SAM session duration not reached, waiting %{public}f"
+ "TB,N,V_allowsKeyboardMathSolving"
+ "TB,N,V_allowsMathPaperSolving"
+ "TB,N,VallowsKeyboardMathSolving"
+ "TB,N,VallowsMathPaperSolving"
+ "Td,R"
+ "_allowsKeyboardMathSolving"
+ "_allowsMathPaperSolving"
+ "allowsKeyboardMathSolving"
+ "allowsMathPaperSolving"
+ "beginSessionTimestamp"
+ "d16@0:8"
+ "processInfoPrimitives"
+ "serializer"
+ "setAllowsKeyboardMathSolving:"
+ "setAllowsMathPaperSolving:"
+ "systemUptime"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "beginCompletionHandlers"
- "endCompletionHandlers"
- "invalid Collection: less than 'count' elements in collection"

```
