## TeaFoundation

> `/System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation`

```diff

-1214.0.0.0.0
-  __TEXT.__text: 0x185bb4
-  __TEXT.__auth_stubs: 0x3de0
+1215.0.0.0.0
+  __TEXT.__text: 0x18d0d8
+  __TEXT.__auth_stubs: 0x3ec0
   __TEXT.__objc_methlist: 0xe78
-  __TEXT.__const: 0xd6a0
-  __TEXT.__cstring: 0x3f77
-  __TEXT.__oslogstring: 0x2200
-  __TEXT.__constg_swiftt: 0x591c
-  __TEXT.__swift5_typeref: 0x499c
-  __TEXT.__swift5_reflstr: 0x2c27
-  __TEXT.__swift5_fieldmd: 0x41b8
+  __TEXT.__const: 0xd960
+  __TEXT.__cstring: 0x40a7
+  __TEXT.__oslogstring: 0x2520
+  __TEXT.__constg_swiftt: 0x5b98
+  __TEXT.__swift5_typeref: 0x4a7a
+  __TEXT.__swift5_reflstr: 0x2cf7
+  __TEXT.__swift5_fieldmd: 0x42a8
   __TEXT.__swift5_builtin: 0x26c
   __TEXT.__swift5_assocty: 0x7e8
-  __TEXT.__swift5_proto: 0x7fc
-  __TEXT.__swift5_types: 0x58c
-  __TEXT.__swift5_capture: 0x6db0
+  __TEXT.__swift5_proto: 0x818
+  __TEXT.__swift5_types: 0x59c
+  __TEXT.__swift5_capture: 0x6f20
   __TEXT.__swift5_mpenum: 0xf0
-  __TEXT.__swift_as_entry: 0x114
-  __TEXT.__swift_as_ret: 0x110
-  __TEXT.__swift5_protos: 0xe8
-  __TEXT.__unwind_info: 0x6c80
-  __TEXT.__eh_frame: 0xa008
+  __TEXT.__swift_as_entry: 0x154
+  __TEXT.__swift_as_ret: 0x12c
+  __TEXT.__swift5_protos: 0xf0
+  __TEXT.__unwind_info: 0x6f08
+  __TEXT.__eh_frame: 0xa558
   __TEXT.__objc_classname: 0x1b8
-  __TEXT.__objc_methname: 0x1f50
+  __TEXT.__objc_methname: 0x1f6e
   __TEXT.__objc_methtype: 0xf2c
   __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0xaf0
-  __DATA_CONST.__objc_classlist: 0x2e8
+  __DATA_CONST.__got: 0xc70
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x918
+  __DATA_CONST.__objc_selrefs: 0x920
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1ef8
-  __AUTH_CONST.__auth_ptr: 0x1400
-  __AUTH_CONST.__const: 0x10f98
+  __AUTH_CONST.__auth_got: 0x1f68
+  __AUTH_CONST.__auth_ptr: 0x1450
+  __AUTH_CONST.__const: 0x113f0
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x6948
+  __AUTH_CONST.__objc_const: 0x6b08
   __AUTH.__objc_data: 0x758
-  __AUTH.__data: 0x890
+  __AUTH.__data: 0x9c0
   __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x2320
+  __DATA.__data: 0x2590
   __DATA.__common: 0x448
-  __DATA.__bss: 0x8980
+  __DATA.__bss: 0x8d00
   __DATA_DIRTY.__objc_data: 0x8d0
-  __DATA_DIRTY.__data: 0x6fc8
+  __DATA_DIRTY.__data: 0x6fb8
   __DATA_DIRTY.__bss: 0x3ea0
   __DATA_DIRTY.__common: 0x518
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11159
-  Symbols:   2776
-  CStrings:  1150
+  Functions: 11377
+  Symbols:   2867
+  CStrings:  1173
 
Symbols:
+ _OBJC_CLASS_$_NSError
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
CStrings:
+ "$defaultActor"
+ "Activating network activity, activity=%s"
+ "Associating network activity with parent, activity=%s, parentActivity=%s"
+ "Attempting to activate a network activity that is already started, activity=%s"
+ "Attempting to complete a Network Activity that is already started, activity=%s"
+ "Child network activity was activated, parentActivity=%s, childActivity=%s"
+ "Child network activity was completed, parentActivity=%s, childActivity=%s, result=%s"
+ "Completing network activity, activity=%s, result=%s"
+ "Completing parent activity because all its children have completed, parentActivity=%s, result=%s"
+ "NetworkActivities"
+ "Not completing parent activity because not all of its children have completed yet, parentActivity=%s"
+ "Please provide the missing unknown enum case."
+ "Retrying network activity, activity=%s"
+ "TeaFoundation/NetworkActivitySession.swift"
+ "_TtC13TeaFoundation22NetworkActivitySession"
+ "childSessions"
+ "hasBeenActive"
+ "initWithDomain:code:userInfo:"
+ "loggingDescription"
+ "networkActivitySession"
+ "nwActivity"
+ "parentSession"

```
