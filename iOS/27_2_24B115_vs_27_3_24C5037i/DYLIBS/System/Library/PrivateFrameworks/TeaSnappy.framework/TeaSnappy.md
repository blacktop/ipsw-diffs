## TeaSnappy

> `/System/Library/PrivateFrameworks/TeaSnappy.framework/TeaSnappy`

```diff

-1517.0.0.0.0
-  __TEXT.__text: 0x4c58
+1556.0.0.0.0
+  __TEXT.__text: 0x5eb8
   __TEXT.__objc_methlist: 0x6fc
-  __TEXT.__const: 0xb2
-  __TEXT.__cstring: 0x223
+  __TEXT.__const: 0x126
+  __TEXT.__cstring: 0x255
   __TEXT.__oslogstring: 0xd5
-  __TEXT.__swift5_typeref: 0x42
-  __TEXT.__swift5_capture: 0x80
-  __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_fieldmd: 0x38
+  __TEXT.__swift5_typeref: 0x48
+  __TEXT.__swift5_capture: 0xb8
+  __TEXT.__constg_swiftt: 0x70
+  __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x13
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x260
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2a0
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
-  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x130
-  __AUTH_CONST.__const: 0x2e8
+  __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1040
-  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH.__objc_data: 0xb0
-  __AUTH.__data: 0x28
+  __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x48
-  __DATA.__data: 0x530
+  __DATA.__data: 0x578
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 165
-  Symbols:   459
-  CStrings:  21
+  Functions: 179
+  Symbols:   142
+  CStrings:  22
 
Symbols:
+ _objc_retain_x26
+ _swift_release_x25
- +[SNAssembly initialize]
- -[SNAssembly .cxx_destruct]
- -[SNAssembly assemblies]
- -[SNAssembly init]
- -[SNTestAssembly loadInRegistry:]
- -[SNTestChain .cxx_destruct]
- -[SNTestChain addLink:]
- -[SNTestChain init]
- -[SNTestChain linkBlocks]
- -[SNTestChain popAndRunWithCompletion:testFailure:]
- -[SNTestChain runWithCompletion:]
- -[SNTestContext .cxx_destruct]
- -[SNTestContext application]
- -[SNTestContext initWithApplication:testName:]
- -[SNTestContext objectForKey:]
- -[SNTestContext objects]
- -[SNTestContext setObject:forKey:]
- -[SNTestContext testName]
- -[SNTestCoordinator .cxx_destruct]
- -[SNTestCoordinator application]
- -[SNTestCoordinator axisForDirection:]
- -[SNTestCoordinator failedTestWithTestName:failureMessage:]
- -[SNTestCoordinator finishedTestWithTestName:waitForCommit:]
- -[SNTestCoordinator initWithApplication:]
- -[SNTestCoordinator launchTestName]
- -[SNTestCoordinator lengthForNumberOfScreens:direction:size:]
- -[SNTestCoordinator recapScrollTestWithTestName:scrollView:]
- -[SNTestCoordinator requiresRotationForOrientation:]
- -[SNTestCoordinator rotateToOrientation:beforeRotation:afterRotation:]
- -[SNTestCoordinator scrollTestWithTestName:scrollView:iterations:offset:direction:]
- -[SNTestCoordinator scrollTestWithTestName:scrollView:iterations:offset:numberOfScreens:direction:]
- -[SNTestCoordinator startedTestWithTestName:]
- -[SNTestFailure .cxx_destruct]
- -[SNTestFailure initWithMessage:]
- -[SNTestFailure initWithMissingClass:]
- -[SNTestFailure message]
- -[SNTestRun .cxx_destruct]
- -[SNTestRun initWithTestCase:testSuite:]
- -[SNTestRun orientation]
- -[SNTestRun runTestWithContext:testCoordinator:completion:]
- -[SNTestRun runTestWithContext:testName:testCoordinator:completion:]
- -[SNTestRun setupWithContext:completion:]
- -[SNTestRun testCase]
- -[SNTestRun testSuite]
- -[SNTestRun waitForCommitToFinish]
- -[SNTestRunner .cxx_destruct]
- -[SNTestRunner application]
- -[SNTestRunner initWithApplication:testCoordinator:testStore:]
- -[SNTestRunner runExtendedLaunchTest]
- -[SNTestRunner runTest:options:]
- -[SNTestRunner runTest:options:fallingBackWith:]
- -[SNTestRunner runTestRun:testName:options:fallingBackWith:]
- -[SNTestRunner testCoordinator]
- -[SNTestRunner testStore]
- -[SNTestStore .cxx_destruct]
- -[SNTestStore addTestCase:]
- -[SNTestStore addTestSuite:]
- -[SNTestStore extendedLaunchTestRun]
- -[SNTestStore extendedLaunchTest]
- -[SNTestStore init]
- -[SNTestStore setExtendedLaunchTest:]
- -[SNTestStore testCases]
- -[SNTestStore testRunForTestName:]
- -[SNTestStore testSuites]
- -[SNTestSuite .cxx_destruct]
- -[SNTestSuite addSubTestSuite:]
- -[SNTestSuite addTestCase:]
- -[SNTestSuite init]
- -[SNTestSuite parentTestSuite]
- -[SNTestSuite setParentTestSuite:]
- -[SNTestSuite subTestSuites]
- -[SNTestSuite testCases]
- -[SNTestSuite testRunForTestName:]
- -[SNTestSuite testSetupList]
- <redacted>
- _OBJC_IVAR_$_SNAssembly._assemblies
- _OBJC_IVAR_$_SNTestChain._linkBlocks
- _OBJC_IVAR_$_SNTestContext._application
- _OBJC_IVAR_$_SNTestContext._objects
- _OBJC_IVAR_$_SNTestContext._testName
- _OBJC_IVAR_$_SNTestCoordinator._application
- _OBJC_IVAR_$_SNTestFailure._message
- _OBJC_IVAR_$_SNTestRun._testCase
- _OBJC_IVAR_$_SNTestRun._testSuite
- _OBJC_IVAR_$_SNTestRunner._application
- _OBJC_IVAR_$_SNTestRunner._testCoordinator
- _OBJC_IVAR_$_SNTestRunner._testStore
- _OBJC_IVAR_$_SNTestStore._extendedLaunchTest
- _OBJC_IVAR_$_SNTestStore._testCases
- _OBJC_IVAR_$_SNTestStore._testSuites
- _OBJC_IVAR_$_SNTestSuite._parentTestSuite
- _OBJC_IVAR_$_SNTestSuite._subTestSuites
- _OBJC_IVAR_$_SNTestSuite._testCases
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _SNSetupLogging.onceToken
- __DATA__TtC9TeaSnappy3PPT
- __INSTANCE_METHODS__TtC9TeaSnappy3PPT
- __METACLASS_DATA__TtC9TeaSnappy3PPT
- __MergedGlobals
- __OBJC_$_CLASS_METHODS_SNAssembly
- __OBJC_$_INSTANCE_METHODS_SNAssembly
- __OBJC_$_INSTANCE_METHODS_SNTestAssembly
- __OBJC_$_INSTANCE_METHODS_SNTestChain
- __OBJC_$_INSTANCE_METHODS_SNTestContext
- __OBJC_$_INSTANCE_METHODS_SNTestCoordinator
- __OBJC_$_INSTANCE_METHODS_SNTestFailure
- __OBJC_$_INSTANCE_METHODS_SNTestRun
- __OBJC_$_INSTANCE_METHODS_SNTestRunner
- __OBJC_$_INSTANCE_METHODS_SNTestStore
- __OBJC_$_INSTANCE_METHODS_SNTestSuite
- __OBJC_$_INSTANCE_VARIABLES_SNAssembly
- __OBJC_$_INSTANCE_VARIABLES_SNTestChain
- __OBJC_$_INSTANCE_VARIABLES_SNTestContext
- __OBJC_$_INSTANCE_VARIABLES_SNTestCoordinator
- __OBJC_$_INSTANCE_VARIABLES_SNTestFailure
- __OBJC_$_INSTANCE_VARIABLES_SNTestRun
- __OBJC_$_INSTANCE_VARIABLES_SNTestRunner
- __OBJC_$_INSTANCE_VARIABLES_SNTestStore
- __OBJC_$_INSTANCE_VARIABLES_SNTestSuite
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROP_LIST_SNAssembly
- __OBJC_$_PROP_LIST_SNTestAssembly
- __OBJC_$_PROP_LIST_SNTestCase
- __OBJC_$_PROP_LIST_SNTestCaseRotate
- __OBJC_$_PROP_LIST_SNTestCaseScroll
- __OBJC_$_PROP_LIST_SNTestChain
- __OBJC_$_PROP_LIST_SNTestContext
- __OBJC_$_PROP_LIST_SNTestCoordinating
- __OBJC_$_PROP_LIST_SNTestCoordinator
- __OBJC_$_PROP_LIST_SNTestFailure
- __OBJC_$_PROP_LIST_SNTestRun
- __OBJC_$_PROP_LIST_SNTestRunFactory
- __OBJC_$_PROP_LIST_SNTestRunOptions
- __OBJC_$_PROP_LIST_SNTestRunner
- __OBJC_$_PROP_LIST_SNTestStore
- __OBJC_$_PROP_LIST_SNTestSuite
- __OBJC_$_PROP_LIST_TFBundleAssembly
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNTestCase
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNTestCaseScroll
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNTestSetup
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestCase
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestCaseRotate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestCaseRun
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestCaseScroll
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestCoordinating
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestRunFactory
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestRunOptions
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNTestRunner
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TFAssembly
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TFBundleAssembly
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestCase
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestCaseRotate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestCaseRun
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestCaseScroll
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestCoordinating
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestRunFactory
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestRunOptions
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestRunner
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNTestSetup
- __OBJC_$_PROTOCOL_METHOD_TYPES_TFAssembly
- __OBJC_$_PROTOCOL_METHOD_TYPES_TFBundleAssembly
- __OBJC_$_PROTOCOL_REFS_SNTestCase
- __OBJC_$_PROTOCOL_REFS_SNTestCaseRotate
- __OBJC_$_PROTOCOL_REFS_SNTestCaseRun
- __OBJC_$_PROTOCOL_REFS_SNTestCaseScroll
- __OBJC_$_PROTOCOL_REFS_SNTestCoordinating
- __OBJC_$_PROTOCOL_REFS_SNTestRunFactory
- __OBJC_$_PROTOCOL_REFS_SNTestRunOptions
- __OBJC_$_PROTOCOL_REFS_SNTestRunner
- __OBJC_$_PROTOCOL_REFS_SNTestSetup
- __OBJC_$_PROTOCOL_REFS_TFAssembly
- __OBJC_$_PROTOCOL_REFS_TFBundleAssembly
- __OBJC_$_PROTOCOL_REFS_TFFrameworkAssembly
- __OBJC_CLASS_PROTOCOLS_$_SNAssembly
- __OBJC_CLASS_PROTOCOLS_$_SNTestAssembly
- __OBJC_CLASS_PROTOCOLS_$_SNTestCoordinator
- __OBJC_CLASS_PROTOCOLS_$_SNTestRun
- __OBJC_CLASS_PROTOCOLS_$_SNTestRunner
- __OBJC_CLASS_PROTOCOLS_$_SNTestStore
- __OBJC_CLASS_RO_$_SNAssembly
- __OBJC_CLASS_RO_$_SNTestAssembly
- __OBJC_CLASS_RO_$_SNTestChain
- __OBJC_CLASS_RO_$_SNTestContext
- __OBJC_CLASS_RO_$_SNTestCoordinator
- __OBJC_CLASS_RO_$_SNTestFailure
- __OBJC_CLASS_RO_$_SNTestRun
- __OBJC_CLASS_RO_$_SNTestRunner
- __OBJC_CLASS_RO_$_SNTestStore
- __OBJC_CLASS_RO_$_SNTestSuite
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_LABEL_PROTOCOL_$_SNTestCase
- __OBJC_LABEL_PROTOCOL_$_SNTestCaseRotate
- __OBJC_LABEL_PROTOCOL_$_SNTestCaseRun
- __OBJC_LABEL_PROTOCOL_$_SNTestCaseScroll
- __OBJC_LABEL_PROTOCOL_$_SNTestCoordinating
- __OBJC_LABEL_PROTOCOL_$_SNTestRunFactory
- __OBJC_LABEL_PROTOCOL_$_SNTestRunOptions
- __OBJC_LABEL_PROTOCOL_$_SNTestRunner
- __OBJC_LABEL_PROTOCOL_$_SNTestSetup
- __OBJC_LABEL_PROTOCOL_$_TFAssembly
- __OBJC_LABEL_PROTOCOL_$_TFBundleAssembly
- __OBJC_LABEL_PROTOCOL_$_TFFrameworkAssembly
- __OBJC_METACLASS_RO_$_SNAssembly
- __OBJC_METACLASS_RO_$_SNTestAssembly
- __OBJC_METACLASS_RO_$_SNTestChain
- __OBJC_METACLASS_RO_$_SNTestContext
- __OBJC_METACLASS_RO_$_SNTestCoordinator
- __OBJC_METACLASS_RO_$_SNTestFailure
- __OBJC_METACLASS_RO_$_SNTestRun
- __OBJC_METACLASS_RO_$_SNTestRunner
- __OBJC_METACLASS_RO_$_SNTestStore
- __OBJC_METACLASS_RO_$_SNTestSuite
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_$_SNTestCase
- __OBJC_PROTOCOL_$_SNTestCaseRotate
- __OBJC_PROTOCOL_$_SNTestCaseRun
- __OBJC_PROTOCOL_$_SNTestCaseScroll
- __OBJC_PROTOCOL_$_SNTestCoordinating
- __OBJC_PROTOCOL_$_SNTestRunFactory
- __OBJC_PROTOCOL_$_SNTestRunOptions
- __OBJC_PROTOCOL_$_SNTestRunner
- __OBJC_PROTOCOL_$_SNTestSetup
- __OBJC_PROTOCOL_$_TFAssembly
- __OBJC_PROTOCOL_$_TFBundleAssembly
- __OBJC_PROTOCOL_$_TFFrameworkAssembly
- __OBJC_PROTOCOL_REFERENCE_$_SNTestCaseRotate
- __OBJC_PROTOCOL_REFERENCE_$_SNTestCaseRun
- __OBJC_PROTOCOL_REFERENCE_$_SNTestCaseScroll
- __OBJC_PROTOCOL_REFERENCE_$_SNTestCoordinating
- __OBJC_PROTOCOL_REFERENCE_$_SNTestRunOptions
- __OBJC_PROTOCOL_REFERENCE_$_SNTestRunner
- __OBJC_PROTOCOL_REFERENCE_$_SNTestSetup
- ___33-[SNTestAssembly loadInRegistry:]_block_invoke
- ___33-[SNTestAssembly loadInRegistry:]_block_invoke_2
- ___33-[SNTestAssembly loadInRegistry:]_block_invoke_3
- ___33-[SNTestAssembly loadInRegistry:]_block_invoke_4
- ___41-[SNTestRun setupWithContext:completion:]_block_invoke
- ___41-[SNTestRun setupWithContext:completion:]_block_invoke_2
- ___51-[SNTestChain popAndRunWithCompletion:testFailure:]_block_invoke
- ___51-[SNTestChain popAndRunWithCompletion:testFailure:]_block_invoke_2
- ___51-[SNTestChain popAndRunWithCompletion:testFailure:]_block_invoke_3
- ___60-[SNTestRunner runTestRun:testName:options:fallingBackWith:]_block_invoke
- ___60-[SNTestRunner runTestRun:testName:options:fallingBackWith:]_block_invoke_2
- ___60-[SNTestRunner runTestRun:testName:options:fallingBackWith:]_block_invoke_3
- ___60-[SNTestRunner runTestRun:testName:options:fallingBackWith:]_block_invoke_4
- ___60-[SNTestRunner runTestRun:testName:options:fallingBackWith:]_block_invoke_5
- ___68-[SNTestRun runTestWithContext:testName:testCoordinator:completion:]_block_invoke
- ___68-[SNTestRun runTestWithContext:testName:testCoordinator:completion:]_block_invoke_2
- ___68-[SNTestRun runTestWithContext:testName:testCoordinator:completion:]_block_invoke_3
- ___68-[SNTestRun runTestWithContext:testName:testCoordinator:completion:]_block_invoke_4
- ___70-[SNTestCoordinator rotateToOrientation:beforeRotation:afterRotation:]_block_invoke
- ___70-[SNTestCoordinator rotateToOrientation:beforeRotation:afterRotation:]_block_invoke_2
- ___SNSetupLogging_block_invoke
- ___block_descriptor_32_e22_16?0"<TFResolver>"8l
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_48_e8_32bs40bs_e23_v16?0"SNTestFailure"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e23_v16?0"SNTestFailure"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e23_v16?0"SNTestFailure"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e30_v16?0?<v?"SNTestFailure">8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls40l8s32l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v16?0?<v?"SNTestFailure">8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e23_v16?0"SNTestFailure"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e30_v16?0?<v?"SNTestFailure">8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v12?0B8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global
- ___swift_closure_destructor
- ___swift_memcpy9_8
- ___swift_noop_void_return
- ___swift_reflection_version
- __swift_FORCE_LOAD_$_swiftCoreFoundation_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftCoreImage_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftDispatch_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftFoundation_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftMetal_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftOSLog_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftObjectiveC_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftQuartzCore_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftSpatial_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftUIKit_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftXPC_$_TeaSnappy
- __swift_FORCE_LOAD_$_swift_Builtin_float_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftos_$_TeaSnappy
- __swift_FORCE_LOAD_$_swiftsimd_$_TeaSnappy
- _block_copy_helper
- _block_descriptor
- _block_destroy_helper
- _swift_release_x19
- _swift_release_x20
- _symbolic Ieg_
- _symbolic Si
- _symbolic So12UIScrollViewC
- _symbolic So8NSObjectC
- _symbolic _____ 12CoreGraphics7CGFloatV
- _symbolic _____ 8Dispatch0A4TimeV
- _symbolic _____ 9TeaSnappy3PPTC
- _symbolic _____ 9TeaSnappy3PPTC13ContentLengthO
CStrings:
+ "TeaSnappy/SNTestModernAssembly.swift"
```
