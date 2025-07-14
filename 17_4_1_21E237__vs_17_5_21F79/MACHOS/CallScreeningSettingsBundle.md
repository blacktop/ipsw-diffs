## CallScreeningSettingsBundle

> `/System/Library/PreferenceBundles/CallScreeningSettingsBundle.bundle/CallScreeningSettingsBundle`

```diff

-2869.500.151.2.3
-  __TEXT.__text: 0xc0c
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x380
-  __TEXT.__objc_methlist: 0x12c
-  __TEXT.__cstring: 0x122
-  __TEXT.__objc_methname: 0x3d8
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methtype: 0x65
+2869.600.72.2.3
+  __TEXT.__text: 0x21d0
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x168
+  __TEXT.__cstring: 0x520
+  __TEXT.__objc_methname: 0x48c
+  __TEXT.__objc_classname: 0x55
+  __TEXT.__objc_methtype: 0xac
   __TEXT.__oslogstring: 0x29
-  __TEXT.__unwind_info: 0x9c
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__const: 0x72
+  __TEXT.__swift5_typeref: 0x7a
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x10c
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__cfstring: 0x120
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1e0
-  __DATA.__objc_selrefs: 0x120
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_const: 0x258
+  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0x160
+  __DATA.__data: 0x68
   __DATA.__bss: 0x30
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7CB4719F-8C3C-3B5E-B07B-5AE056E2875D
-  Functions: 28
-  Symbols:   68
-  CStrings:  77
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 546D4D3E-0A2E-390A-9629-AE4AF16907D4
+  Functions: 64
+  Symbols:   112
+  CStrings:  107
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$__TtC27CallScreeningSettingsBundle32TUCallScreeningAnalyticsReporter
+ _OBJC_METACLASS_$__TtC27CallScreeningSettingsBundle32TUCallScreeningAnalyticsReporter
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftos
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_opt_self
+ _objc_retain_x20
+ _objc_retain_x23
+ _objc_retain_x24
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
CStrings:
+ "\x01\x11"
+ "@\"NSDictionary\"8@?0"
+ "@\"_TtC27CallScreeningSettingsBundle32TUCallScreeningAnalyticsReporter\""
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"_TtC27CallScreeningSettingsBundle32TUCallScreeningAnalyticsReporter\",R,N,V_analyticsReporter"
+ "TUCallScreeningAnalyticsReporter: logging core analytics for event of %s with dictionary %s"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC27CallScreeningSettingsBundle32TUCallScreeningAnalyticsReporter"
+ "_analyticsReporter"
+ "analyticsReporter"
+ "com.apple.calls.CallScreeningSettingsBundle"
+ "com.apple.liveandvisualvoicemail.lvmToggle"
+ "dealloc"
+ "init"
+ "invalid Collection: less than 'count' elements in collection"
+ "logLiveVoiceMailToggleWithToggledTo:"
+ "new_lvm_enablement_status"
+ "v20@0:8B16"

```
