## MultitouchSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/MultitouchSessionFilter.plugin/Contents/MacOS/MultitouchSessionFilter`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_selrefs`

```diff

-10400.44.0.0.0
-  __TEXT.__text: 0x41dc
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x6e4
-  __TEXT.__const: 0xa2
-  __TEXT.__objc_methname: 0xfd5
-  __TEXT.__cstring: 0x159
-  __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methtype: 0x338
+10410.1.0.0.0
+  __TEXT.__text: 0xcf74
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__objc_methlist: 0x76c
+  __TEXT.__const: 0x380
+  __TEXT.__objc_methname: 0x10d7
+  __TEXT.__cstring: 0x2e7
+  __TEXT.__objc_classname: 0x185
+  __TEXT.__objc_methtype: 0x36a
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__oslogstring: 0x358
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__const: 0x1c8
+  __TEXT.__oslogstring: 0x456
+  __TEXT.__swift5_typeref: 0x23f
+  __TEXT.__constg_swiftt: 0x234
+  __TEXT.__swift5_reflstr: 0xd5
+  __TEXT.__swift5_fieldmd: 0x130
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x430
+  __TEXT.__eh_frame: 0x150
+  __DATA_CONST.__const: 0x418
   __DATA_CONST.__cfstring: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x50
-  __DATA.__objc_const: 0xaa0
+  __DATA_CONST.__auth_got: 0x4b0
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA.__objc_const: 0xd90
   __DATA.__objc_selrefs: 0x498
   __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x120
+  __DATA.__objc_data: 0x330
+  __DATA.__data: 0x4c0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/HID.framework/Versions/A/HID
+  - /System/Library/PrivateFrameworks/HIDPreferences.framework/Versions/A/HIDPreferences
   - /System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/Versions/A/MultitouchSessionFilterSupport
   - /System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 145
-  Symbols:   80
-  CStrings:  311
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 316
+  Symbols:   151
+  CStrings:  345
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFDictionaryGetTypeID
+ _HIDPreferencesCopyForInstance
+ _HIDPreferencesCreateInstance
+ _HIDPreferencesSetForInstance
+ _HIDPreferencesSynchronizeForInstance
+ _OBJC_CLASS_$_MTPreferencesTelemetryManager
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_MTPreferencesTelemetryManager
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftos
+ _bzero
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocBox
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "AppleMultitouchDevice"
+ "ExternalTrackpad"
+ "Failed to create preferences instance"
+ "Failed to fetch settings from service %s"
+ "Failed to schedule telemetry callback: Scheduler not available"
+ "HasExternalTrackpad"
+ "HasInternalTrackpad"
+ "InternalTrackpad"
+ "MTPreferencesTelemetryManager"
+ "Mouse"
+ "MultitouchSettings"
+ "Registered %{public}s service %{public}s"
+ "Scheduling next telemetry event for %{public}s"
+ "T@\"NSDictionary\",N,R"
+ "T@\"OS_dispatch_queue\",N,&"
+ "TrackedServiceCount"
+ "_TtC23MultitouchSessionFilter21HIDServicePreferences"
+ "_TtC23MultitouchSessionFilter21MockDispatchScheduler"
+ "_TtC23MultitouchSessionFilter22DispatchQueueScheduler"
+ "com.apple.hid.MouseSettings"
+ "com.apple.hid.TrackpadSettings"
+ "com.apple.windowserver"
+ "domainKey"
+ "hasExternalTrackpad"
+ "hasInternalTrackpad"
+ "logger"
+ "now"
+ "pending"
+ "preferences"
+ "preferencesInstance"
+ "scheduler"
+ "telemetryTask"
+ "trackedServices"
```
