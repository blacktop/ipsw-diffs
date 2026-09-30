## RelevanceEngine

> `/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine`

```diff

-492.0.0.0.0
-  __TEXT.__text: 0xec480
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_methlist: 0xe958
-  __TEXT.__const: 0xf60
-  __TEXT.__cstring: 0x75bb
+495.0.0.0.0
+  __TEXT.__text: 0xf0648
+  __TEXT.__auth_stubs: 0x17a0
+  __TEXT.__objc_methlist: 0xe9d0
+  __TEXT.__const: 0xfaa
+  __TEXT.__cstring: 0x7910
   __TEXT.__gcc_except_tab: 0x39f4
-  __TEXT.__oslogstring: 0x3518
+  __TEXT.__oslogstring: 0x367d
   __TEXT.__dlopen_cstrs: 0xb3d
   __TEXT.__ustring: 0x168
-  __TEXT.__unwind_info: 0x4c78
+  __TEXT.__swift5_typeref: 0x4d
+  __TEXT.__constg_swiftt: 0x84
+  __TEXT.__swift5_reflstr: 0x13
+  __TEXT.__swift5_fieldmd: 0x28
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x4d30
   __TEXT.__objc_classname: 0x3080
-  __TEXT.__objc_methname: 0x1850b
-  __TEXT.__objc_methtype: 0x5b96
-  __TEXT.__objc_stubs: 0x13940
-  __DATA_CONST.__got: 0xef8
-  __DATA_CONST.__const: 0x4798
-  __DATA_CONST.__objc_classlist: 0xb48
+  __TEXT.__objc_methname: 0x18616
+  __TEXT.__objc_methtype: 0x5ba8
+  __TEXT.__objc_stubs: 0x139e0
+  __DATA_CONST.__got: 0xf90
+  __DATA_CONST.__const: 0x4858
+  __DATA_CONST.__objc_classlist: 0xb50
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c88
+  __DATA_CONST.__objc_selrefs: 0x5cf8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x920
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__const: 0x28f0
-  __AUTH_CONST.__cfstring: 0x7980
-  __AUTH_CONST.__objc_const: 0x20400
+  __AUTH_CONST.__cfstring: 0x79a0
+  __AUTH_CONST.__objc_const: 0x204d8
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x3570
-  __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x1060
-  __DATA.__data: 0x2b10
-  __DATA.__bss: 0xac8
+  __AUTH.__objc_data: 0x3670
+  __AUTH.__data: 0x80
+  __DATA.__objc_ivar: 0x1064
+  __DATA.__data: 0x2b68
+  __DATA.__bss: 0xad0
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x3b60
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x960
+  __DATA_DIRTY.__bss: 0x970
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6584
-  Symbols:   8095
-  CStrings:  6928
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 6650
+  Symbols:   8158
+  CStrings:  6979
 
Symbols:
+ _HKSPDayForNSGregorianCalendarDay
+ _HKSPWeekdaysFromDay
+ _OBJC_CLASS_$_HKSPSleepScheduleOccurrence
+ _OBJC_CLASS_$_HKSPSleepStore
+ _OBJC_CLASS_$__TtC15RelevanceEngine20RESleepScheduleEntry
+ _OBJC_METACLASS_$__TtC15RelevanceEngine20RESleepScheduleEntry
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _memcpy
+ _objc_allocWithZone
+ _objc_opt_self
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_endAccess
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
CStrings:
+ "%!f(MISSING) distance to %!@(MISSING)"
+ "@\"HKSPSleepStore\""
+ "Device location is unknown"
+ "Distance is negative"
+ "Fatal error"
+ "Gettng the bedtime for currentDate"
+ "Insufficient space allocated to copy string contents"
+ "Now is after currentDate's wakeupTime. gettng the bedtime for nextOccurrence"
+ "Obtaining the schedule for %!s(MISSING)"
+ "RelevanceEngine.RESleepScheduleEntry"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSDate\",N,C"
+ "The bedtime(startDate) is %!s(MISSING)"
+ "The wakeup(endDate) time is %!s(MISSING)"
+ "Unable to get the current sleep schedule: %!@(MISSING)"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC15RelevanceEngine20RESleepScheduleEntry"
+ "_sleepStore"
+ "bedtime"
+ "bedtime"
+ "bedtimeComponents"
+ "com.apple.RelevanceEngine.REPeriodOfDayPredictor"
+ "crossesDayBoundary"
+ "currentSleepScheduleWithError:"
+ "eveningStart is: %!@(MISSING)"
+ "init()"
+ "initWithIdentifier:"
+ "initWithWakeupTime:bedtime:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isEnabled"
+ "occurrences"
+ "setBedtime:"
+ "setWakeupTime:"
+ "sleepEntryForDatesWithCurrent:next:schedule:"
+ "wakeUpComponents"
+ "wakeupTime"
+ "wakeupTime"
+ "weekdays"

```
