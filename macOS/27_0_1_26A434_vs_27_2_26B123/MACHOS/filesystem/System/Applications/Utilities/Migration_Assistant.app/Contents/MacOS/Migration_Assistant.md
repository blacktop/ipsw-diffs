## Migration Assistant

> `/System/Applications/Utilities/Migration Assistant.app/Contents/MacOS/Migration Assistant`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_imageinfo`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_doubleobj`

```diff

-973.0.0.0.0
-  __TEXT.__text: 0x6d88
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x1d60
-  __TEXT.__objc_methlist: 0xb4c
-  __TEXT.__const: 0x78
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x22a8
-  __TEXT.__objc_methtype: 0x710
-  __TEXT.__cstring: 0xc4c
+975.2.2.0.0
+  __TEXT.__text: 0xc0a4
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0xc5c
+  __TEXT.__const: 0x5f4
+  __TEXT.__objc_classname: 0x1a3
+  __TEXT.__objc_methname: 0x24d7
+  __TEXT.__objc_methtype: 0x735
+  __TEXT.__cstring: 0xe8d
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x288
-  __DATA_CONST.__const: 0x298
-  __DATA_CONST.__cfstring: 0xd80
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__swift5_typeref: 0x152
+  __TEXT.__swift5_capture: 0xcc
+  __TEXT.__constg_swiftt: 0x134
+  __TEXT.__swift5_reflstr: 0x253
+  __TEXT.__swift5_fieldmd: 0x1d0
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__eh_frame: 0x40
+  __DATA_CONST.__const: 0x908
+  __DATA_CONST.__cfstring: 0xe80
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x1c8
-  __DATA.__objc_const: 0x10b8
-  __DATA.__objc_selrefs: 0xa60
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_ptr: 0xb8
+  __DATA.__objc_const: 0x1290
+  __DATA.__objc_selrefs: 0xae8
   __DATA.__objc_ivar: 0x94
-  __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x38
+  __DATA.__objc_data: 0x540
+  __DATA.__data: 0x298
+  __DATA.__bss: 0x640
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 200
-  Symbols:   140
-  CStrings:  617
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 381
+  Symbols:   253
+  CStrings:  674
 
Symbols:
+ _$s10Foundation5NSLogyySS_s7CVarArg_pdtF
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$s8Dispatch0A3QoSV11unspecifiedACvgZ
+ _$s8Dispatch0A3QoSVMa
+ _$s8RawValueSYTl
+ _$sBOWV
+ _$sBi64_WV
+ _$sBoWV
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS6appendyySSF
+ _$sSSN
+ _$sSSSHsWP
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sSayxGSTsMc
+ _$sSbN
+ _$sSdN
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMa
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMn
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVs10SetAlgebraACMc
+ _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyO7inherityA2EmFWC
+ _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyOMa
+ _$sSo17OS_dispatch_queueC8DispatchE4sync7executexxyKXE_tKlF
+ _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _$sSo17OS_dispatch_queueC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0D3QoSVAbCE10AttributesVAbCE011AutoreleaseI0OABSgtcfC
+ _$sSo8NSObjectCs7CVarArg10ObjectiveCMc
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss11_StringGutsV4growyySiF
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss20__StaticArrayStorageCN
+ _$ss21_findStringSwitchCase5cases6stringSiSays06StaticB0VG_SStF
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV8_combineyySuF
+ _$ss6HasherV9_finalizeSiyF
+ _$ss6UInt32VMn
+ _$ss6UInt32VN
+ _$ss7CVarArgMp
+ _$sypN
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _bzero
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_setDeallocating
+ _swift_stdlib_random
CStrings:
+ "@24@0:8q16"
+ "AuthResult"
+ "Authentication"
+ "BuddyStartupDuration"
+ "Duplicate values for key: '"
+ "FUSLogout"
+ "Failed"
+ "Fatal error"
+ "HandoffInitiated"
+ "HandoffTargetLanding"
+ "I16@0:8"
+ "IsLogoutSuccessful"
+ "IsManaged"
+ "LaunchReason"
+ "LogOutSuccessCode"
+ "Logout"
+ "SessionID"
+ "StateDuration"
+ "StateStartTime"
+ "StateTracker"
+ "Success"
+ "Swift/NativeDictionary.swift"
+ "T@\"_TtC19Migration_Assistant18MATelemetryHandler\",N,R"
+ "TI,N,R"
+ "TelemetryType"
+ "TotalDuration"
+ "TransitionDuration"
+ "Welcome"
+ "[MATelemetryHandler] Sending telemetry: %@"
+ "_TtC19Migration_Assistant17MATelemetryHelper"
+ "_TtC19Migration_Assistant18MATelemetryHandler"
+ "_TtC19Migration_AssistantP33_B5828EA8BF9874043077B7189EBFFA3519ResourceBundleClass"
+ "appLaunchTime"
+ "com.apple.MATelemetry"
+ "com.apple.MigrationAssistant"
+ "numberWithUnsignedInt:"
+ "paneVisibleTime"
+ "payload"
+ "queue"
+ "recordAuthResult:"
+ "recordBuddyStartupDuration:"
+ "recordHandoffInitiated:"
+ "recordIsLogoutSuccessful:"
+ "recordIsManaged:"
+ "recordLaunchReason:"
+ "recordLogOutSuccessCode:"
+ "recordStateTracker:"
+ "recordTelemetryType:"
+ "recordTransitionDuration:"
+ "sendEvent"
+ "sessionID"
+ "shared"
+ "stringFromAuthResult:"
+ "stringFromLaunchReason:"
+ "stringFromTelemetryEventType:"
+ "telemetrySessionID"
+ "v24@0:8q16"
```
