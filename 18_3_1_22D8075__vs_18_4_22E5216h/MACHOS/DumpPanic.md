## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-320.0.0.0.0
-  __TEXT.__text: 0x224c0
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x600
-  __TEXT.__const: 0x38a
-  __TEXT.__cstring: 0x2923
-  __TEXT.__gcc_except_tab: 0xae4
-  __TEXT.__oslogstring: 0x4578
+326.100.5.0.0
+  __TEXT.__text: 0x2447c
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x608
+  __TEXT.__const: 0x3c2
+  __TEXT.__cstring: 0x2a57
+  __TEXT.__objc_methname: 0x1937
+  __TEXT.__constg_swiftt: 0x70
+  __TEXT.__swift5_typeref: 0x47
+  __TEXT.__swift5_reflstr: 0x1b
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__oslogstring: 0x4745
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0xccc
   __TEXT.__ustring: 0x1c6
-  __TEXT.__objc_classname: 0xfa
-  __TEXT.__objc_methname: 0x18ca
-  __TEXT.__objc_methtype: 0x427
-  __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x640
-  __DATA_CONST.__cfstring: 0x2900
+  __TEXT.__objc_classname: 0xde
+  __TEXT.__objc_methtype: 0x402
+  __TEXT.__unwind_info: 0x5c0
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__cfstring: 0x29c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x198
-  __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA.__objc_const: 0xda0
-  __DATA.__objc_selrefs: 0x840
+  __DATA_CONST.__objc_arraydata: 0x1c0
+  __DATA_CONST.__objc_arrayobj: 0x138
+  __DATA_CONST.__objc_dictobj: 0x118
+  __DATA.__objc_const: 0xd70
+  __DATA.__objc_selrefs: 0x860
   __DATA.__objc_ivar: 0xac
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x108
-  __DATA.__bss: 0xa30
+  __DATA.__objc_data: 0x4b0
+  __DATA.__data: 0x168
+  __DATA.__bss: 0xa70
   __INFO_FILTER.__disable: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 425
-  Symbols:   288
-  CStrings:  1199
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 469
+  Symbols:   356
+  CStrings:  1224
 
Symbols:
+ _$s15CoreDiagnostics14MatchedPatternMp
+ _$s15CoreDiagnostics16PanicPatternInfoC2id4type4path11panicStringACSS_S3Stcfc
+ _$s15CoreDiagnostics16PanicPatternInfoCMa
+ _$s15CoreDiagnostics18PanicPatternActionO13DonateTypeOneyA2CmFWC
+ _$s15CoreDiagnostics18PanicPatternActionO13DonateTypeTwoyA2CmFWC
+ _$s15CoreDiagnostics18PanicPatternActionO8rawValues6UInt32Vvg
+ _$s15CoreDiagnostics18PanicPatternActionOMa
+ _$s15CoreDiagnostics18PanicPatternActionOSQAAMc
+ _$s15CoreDiagnostics19PanicMatchedPatternV12panicActionsSayAA0cE6ActionOGSgvg
+ _$s15CoreDiagnostics19PanicMatchedPatternV4uuidSSvg
+ _$s15CoreDiagnostics19PanicMatchedPatternVMa
+ _$s15CoreDiagnostics19PanicMatchedPatternVMn
+ _$s15CoreDiagnostics25DiagnosticPatternMatchingC02isD16PayloadAvailableSbyF
+ _$s15CoreDiagnostics25DiagnosticPatternMatchingC07lookForD06reportSayAA07MatchedD0_pGSgAA0D4InfoC_tF
+ _$s15CoreDiagnostics25DiagnosticPatternMatchingC4typeACSgSo017pattern_matching_F0V_tcfc
+ _$s15CoreDiagnostics25DiagnosticPatternMatchingCMa
+ _$s15CoreDiagnostics25DiagnosticPatternMatchingCMn
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sBOWV
+ _$sSQ2eeoiySbx_xtFZTj
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsVN
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss5UInt8VMn
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMDiagnosticsPanic
+ __Block_copy
+ __Block_release
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_release_x1
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
- OBJC_IVAR_$_OSAReport._logType
- _NSClassFromString
- _OBJC_CLASS_$_objcDiagnosticPatternMatching
- _OBJC_CLASS_$_objcPanicCriterials
- ___NSArray0__struct
CStrings:
+ "\x03'#"
+ "410"
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "B56@0:8@16@24@32@40@?48"
+ "Debug Testing"
+ "Deleting dumppanic boot-arg..."
+ "Diagnostics"
+ "DumpPanic.PanicPatternMatchingWrapper"
+ "Failed to create Panic Pattern Info object, bailing out pattern matching"
+ "Failed to flush the NVRAM store when setting '%@': Error 0x%04x"
+ "Failed to set the '%@' NVRAM variable. Error 0x%04x"
+ "IONVRAM-FORCESYNCNOW-PROPERTY"
+ "Machine configured for intentional panic"
+ "Multiple panic patterns matched"
+ "No DiagnosticPatternMatching object available"
+ "No panic patterns matched"
+ "Panic"
+ "PanicPatternType"
+ "PanicPatternUUID"
+ "Skip writing ResetCounter log to disk for intentional panic"
+ "Unknown"
+ "_TtC9DumpPanic27PanicPatternMatchingWrapper"
+ "_appleCareDetails"
+ "_biomeProperties"
+ "boot-args"
+ "componentsSeparatedByString:"
+ "donate panic with pattern uuid %@ type %@"
+ "donateToBiome"
+ "failed to delete dumppanic in boot-args"
+ "get_prologue_json"
+ "init()"
+ "initWithAction:"
+ "initWithCaptureTime:incidentID:patternUUID:patternType:"
+ "initWithUnsignedInt:"
+ "lookForKnownPanicWithIncidentId:type:path:panicString:completion:"
+ "panic_pattern_matching"
+ "sendEvent:"
+ "setAppleCareDetails:"
+ "setBiomeProperties:"
+ "source"
+ "substringFromIndex:"
+ "v24@?0@\"NSString\"8@\"NSNumber\"16"
+ "validate_key_in_prologue:present:"
+ "validate_key_in_prologue:withValue:"
- "\x03'!"
- "@\"objcDiagnosticPatternMatching\""
- "@48@0:8@16@24@32@40"
- "Failed to create Panic Criterials object, bailing out pattern matching"
- "No"
- "PanicPatternMatchingSupport"
- "T@\"objcDiagnosticPatternMatching\",&,V_patternMatching"
- "TB,V_takeAction"
- "Yes"
- "_patternMatching"
- "_takeAction"
- "createPanicCriterials::::"
- "getPanicCriterials"
- "initWithCriterials::::"
- "initWithType:"
- "isPatternPayloadAvailable"
- "logType"
- "lookForKnownPanic:"
- "lookForPattern::"
- "objcDiagnosticPatternMatching"
- "objcPanicCriterials"
- "setPatternMatching:"
- "setTakeAction:"

```
