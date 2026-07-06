## MediaFoundation

> `/System/Library/PrivateFrameworks/MediaFoundation.framework/Versions/A/MediaFoundation`

```diff

-  __TEXT.__text: 0x26734
-  __TEXT.__const: 0x4b48
-  __TEXT.__cstring: 0x63b
-  __TEXT.__swift5_typeref: 0x1097
-  __TEXT.__swift5_capture: 0x1f8
-  __TEXT.__swift5_reflstr: 0xeac
+  __TEXT.__text: 0x293a4
+  __TEXT.__const: 0x4b78
+  __TEXT.__cstring: 0x69a
+  __TEXT.__swift5_typeref: 0x10a7
+  __TEXT.__swift5_capture: 0x278
+  __TEXT.__swift5_reflstr: 0xedc
   __TEXT.__swift5_assocty: 0x218
-  __TEXT.__swift5_fieldmd: 0x13d0
+  __TEXT.__swift5_fieldmd: 0x13e8
   __TEXT.__constg_swiftt: 0x10f8
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_mpenum: 0x54

   __TEXT.__swift5_proto: 0x1d0
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_types2: 0x38
-  __TEXT.__unwind_info: 0x1128
-  __TEXT.__eh_frame: 0x18c0
+  __TEXT.__oslogstring: 0x26a
+  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__eh_frame: 0x19a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2dc8
+  __AUTH_CONST.__const: 0x2f38
   __AUTH_CONST.__objc_const: 0x248
-  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH.__data: 0xd0
-  __DATA.__data: 0x4b8
+  __DATA.__data: 0x518
   __DATA.__bss: 0x2e10
+  __DATA.__common: 0x18
   __DATA_DIRTY.__data: 0x898
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1744
-  Symbols:   1011
-  CStrings:  53
+  Functions: 1821
+  Symbols:   1063
+  CStrings:  65
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSObject
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy26_8
+ ___swift_memcpy58_8
+ ___swift_project_value_buffer
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MediaFoundation
+ __swift_stdlib_bridgeErrorToNSError
+ _os_log_type_enabled
+ _parameter-flags
+ _sqlite3_busy_timeout
+ _swift_bridgeObjectRelease_n
+ _swift_errorRetain
+ _swift_getFunctionTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_getObjectType
+ _swift_unknownObjectRetain
+ _symbolic SdSg
+ _symbolic So8NSObjectCIego_
+ _symbolic So8NSObjectCSgIego_
+ _symbolic ______pIego_ s5ErrorP
- ___swift_memcpy34_8
- ___swift_memcpy9_1
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata 15MediaFoundation11SQLDatabaseV10ConnectionV noncopyable
- get_type_metadata 15MediaFoundation4_SQLO10ConnectionV noncopyable
- get_type_metadata 15MediaFoundation4_SQLO7ContextV noncopyable
- get_type_metadata 15MediaFoundation4_SQLO9IndexInfoV noncopyable
- get_type_metadata 15MediaFoundation4_SQLO9StatementV noncopyable
- get_type_metadata Rvz15MediaFoundation11SQLDatabaseV18ValueRepresentableRzlAA4_SQLO8IteratorV noncopyable
CStrings:
+ "Could not commit transaction: %{public}@."
+ "PRAGMA foreign_keys"
+ "PRAGMA foreign_keys = "
+ "Unable to get PRAGMA foreign_key: %{public}@. Defaulting to FALSE."
+ "Unable to get PRAGMA journal_mode: %{public}@. Defaulting to DELETE."
+ "Unable to get PRAGMA locking_mode: %{public}@. Defaulting to NORMAL."
+ "Unable to set PRAGMA foreign_key to %{bool,public}d: %{public}@."
+ "Unable to set PRAGMA journal_mode to %{public}s: %{public}@."
+ "Unable to set PRAGMA locking_mode to %{public}s: %{public}@."
+ "Unable to set busy timeout: %{public}@."
+ "While closing connection, unable to run PRAGMA optimize: %{public}@."
+ "com.apple.MediaFoundation"

```
