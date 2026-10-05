## _CoreLocation_SwiftUI

> `/System/Library/Frameworks/_CoreLocation_SwiftUI.framework/_CoreLocation_SwiftUI`

```diff

-3186.0.17.0.1
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x4a
+3186.0.21.0.0
+  __TEXT.__text: 0x5bfc
+  __TEXT.__objc_methlist: 0x1b4
+  __TEXT.__const: 0x1e4
+  __TEXT.__constg_swiftt: 0x164
+  __TEXT.__swift5_typeref: 0x276
+  __TEXT.__swift5_reflstr: 0x87
+  __TEXT.__swift5_fieldmd: 0xb8
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_capture: 0x60
+  __TEXT.__oslogstring: 0x1b9
+  __TEXT.__cstring: 0xb9
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x90
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0xf0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x198
+  __AUTH_CONST.__objc_const: 0x278
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH.__objc_data: 0xc8
+  __AUTH.__data: 0x148
+  __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 0
-  Symbols:   18
-  CStrings:  0
+  Functions: 111
+  Symbols:   106
+  CStrings:  13
 
Symbols:
+ _OBJC_CLASS_$_CLBodyToken
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_NSObject
+ ___chkstk_darwin
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ _bzero
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_autoreleaseReturnValue
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_retain_x9
+ _os_log_type_enabled
+ _os_unfair_lock_assert_not_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_dynamicCastClass
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getOpaqueTypeConformance2
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x22
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
CStrings:
+ "%{public}s"
+ "Attaching body proxy %@ to manager %@"
+ "Creating body proxy %@"
+ "Destroying body proxy %@"
+ "Detaching body proxy %@ from manager %@"
+ "Notifying body tokens for body proxy %@ of updates: %s"
+ "This body token is already attached to this view."
+ "This body token is not attached to this view."
+ "This manager's headingBody was set directly. The view using locationHeadingAnchor(manager:isEnabled:) is replacing it."
+ "Updating body proxy %@ interfaceAngle to %f"
+ "Updating body proxy %@ motionBodyID to %s"
+ "com.apple.locationd"
+ "com.apple.runtime-issues"
```
