## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Versions/A/DeviceRecovery`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_imageinfo`

```diff

-150.0.2.0.0
-  __TEXT.__text: 0xfa44
-  __TEXT.__objc_methlist: 0x6b8
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x1145
-  __TEXT.__cstring: 0x27a6
+150.40.9.0.0
+  __TEXT.__text: 0x115e4
+  __TEXT.__objc_methlist: 0x778
+  __TEXT.__const: 0xe2
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__cstring: 0x28f9
+  __TEXT.__oslogstring: 0x11e7
+  __TEXT.__constg_swiftt: 0x78
+  __TEXT.__swift5_typeref: 0x38
+  __TEXT.__swift5_reflstr: 0x20
+  __TEXT.__swift5_fieldmd: 0x34
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2e0
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x338
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d0
+  __DATA_CONST.__objc_selrefs: 0x530
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0x790
+  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__objc_const: 0x898
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0x188
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_ptr: 0x0
+  __DATA.__objc_ivar: 0x58
+  __DATA.__data: 0x28
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__objc_data: 0x1f0
+  __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 511
-  Symbols:   603
-  CStrings:  306
+  - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 551
+  Symbols:   668
+  CStrings:  317
 
Symbols:
+ -[DeviceRecoveryController addEraseAndUpdateRestrictionForClient:completion:]
+ -[DeviceRecoveryController eraseAndUpdateRestricted]
+ -[DeviceRecoveryController removeEraseAndUpdateRestrictionForClient:completion:]
+ -[DeviceRecoveryController setEraseAndUpdateRestricted:]
+ -[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]
+ OBJC_IVAR_$_DeviceRecoveryController._eraseAndUpdateRestricted
+ _DRServiceAttributeEraseAndUpdateRestricted
+ _OBJC_CLASS_$__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ _OBJC_METACLASS_$__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ __78-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]_block_invoke
+ __DATA__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ __INSTANCE_METHODS__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ __IVARS__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ __METACLASS_DATA__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ __PROPERTIES__TtC14DeviceRecovery34DeviceRecoveryFileStreamJSONWriter
+ ___78-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]_block_invoke
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftAppleArchive_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_DeviceRecovery
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_DeviceRecovery
+ __swift_stdlib_reportUnimplementedInitializer
+ _memcpy
+ _objc_autorelease
+ _objc_msgSend$addEraseAndUpdateRestrictionForClient:completion:
+ _objc_msgSend$removeEraseAndUpdateRestrictionForClient:completion:
+ _objc_msgSend$setEraseAndUpdateRestricted:
+ _objc_msgSend$setEraseAndUpdateRestriction:forClient:completion:
+ _objc_opt_self
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _symbolic Si
+ _symbolic So12NSFileHandleC
+ _symbolic So8NSObjectC
+ _symbolic _____ 10Foundation11JSONEncoderC
+ _symbolic _____ 14DeviceRecovery0aB20FileStreamJSONWriterC
+ _symbolic ______p 10Foundation15ContiguousBytesP
CStrings:
+ "%{public}s: Could not update EACS / Software Update restriction: %{public}@"
+ "%{public}s: Framework: %{public}s EACS / Software Update restriction for '%{public}@'"
+ "-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]"
+ "-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]_block_invoke"
+ "DeviceRecovery.DeviceRecoveryFileStreamJSONWriter"
+ "EraseAndUpdateRestricted"
+ "adding"
+ "clientIdentifier.length > 0"
+ "init()"
+ "no client identifier provided"
+ "removing"
```
