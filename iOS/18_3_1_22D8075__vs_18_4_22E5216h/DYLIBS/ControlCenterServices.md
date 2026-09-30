## ControlCenterServices

> `/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices`

```diff

-600.3.3.100.1
-  __TEXT.__text: 0xe05c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0xa18
-  __TEXT.__const: 0x98
+600.4.21.100.0
+  __TEXT.__text: 0xe850
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0xd84
+  __TEXT.__const: 0x9a
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x1898
-  __TEXT.__oslogstring: 0x1171
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__cstring: 0x1969
+  __TEXT.__oslogstring: 0x11a4
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__objc_classname: 0x1b5
-  __TEXT.__objc_methname: 0x290c
+  __TEXT.__objc_methname: 0x291b
   __TEXT.__objc_methtype: 0x60c
-  __TEXT.__objc_stubs: 0x1de0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x850
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__objc_stubs: 0x1dc0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x860
+  __DATA_CONST.__objc_selrefs: 0x9a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x278
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x13c0
-  __AUTH_CONST.__objc_const: 0x19e8
+  __AUTH_CONST.__cfstring: 0x1420
+  __AUTH_CONST.__objc_const: 0x1438
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH.__objc_data: 0x70
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x2a0
-  __DATA.__common: 0x8
+  __DATA.__data: 0x2c0
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x98
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 368
-  Symbols:   543
-  CStrings:  745
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 395
+  Symbols:   595
+  CStrings:  754
 
Symbols:
+ _CCSLoggingSubsystem
+ _OBJC_CLASS_$_CCSControlCenterServicesManager
+ _OBJC_METACLASS_$_CCSControlCenterServicesManager
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
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
+ _objc_allocWithZone
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _swift_beginAccess
+ _swift_endAccess
+ _swift_getObjCClassMetadata
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
CStrings:
+ "CCSControlCenterServicesManager"
+ "ControlCenterServices/ControlCenterServicesManager.swift"
+ "ModuleAllowedList"
+ "Starting Control Center Services..."
+ "com.apple.BarcodeScanner.BarcodeSupportHelper"
+ "com.apple.GameOverlayUIInternal"
+ "com.apple.logind"
+ "isStageManagerAvailable"
+ "startServices"
- "ModuleAllowedList-Yodel"
- "repositoryWithDefaults"

```
