## DMCApps

> `/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps`

```diff

-4.34.0.0.0
-  __TEXT.__text: 0x11a14
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__const: 0x90c
-  __TEXT.__cstring: 0x4a4
-  __TEXT.__swift5_typeref: 0x341
-  __TEXT.__constg_swiftt: 0x6ec
+4.40.0.0.0
+  __TEXT.__text: 0x16ddc
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x91c
+  __TEXT.__cstring: 0x524
+  __TEXT.__swift5_typeref: 0x36d
+  __TEXT.__constg_swiftt: 0x754
   __TEXT.__swift5_reflstr: 0x3cc
   __TEXT.__swift5_fieldmd: 0x4b8
   __TEXT.__swift5_proto: 0x68

   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__oslogstring: 0x31c
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__eh_frame: 0x1338
-  __TEXT.__objc_methname: 0x308
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__oslogstring: 0x4ea
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__eh_frame: 0x1668
+  __TEXT.__objc_methname: 0x36e
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148
-  __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__auth_ptr: 0x140
-  __AUTH_CONST.__const: 0xad0
+  __DATA_CONST.__objc_selrefs: 0x178
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_ptr: 0x150
+  __AUTH_CONST.__const: 0xaf0
   __AUTH_CONST.__objc_const: 0x1d8
-  __AUTH.__data: 0x428
-  __DATA.__data: 0x2e8
+  __AUTH.__data: 0x470
+  __DATA.__data: 0x370
   __DATA.__bss: 0x780
-  __DATA.__common: 0x28
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 519
-  Symbols:   129
-  CStrings:  83
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 574
+  Symbols:   147
+  CStrings:  100
 
Symbols:
+ _OBJC_CLASS_$_DMFSetAppAllowUserToHideRequest
+ _OBJC_CLASS_$_DMFSetAppAllowUserToLockRequest
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _bzero
+ _kMDMManagedAppAttributeAllowUserHidden
+ _kMDMManagedAppAttributeAllowUserLocked
+ _swift_arrayInitWithCopy
+ _swift_initStackObject
+ _swift_release_n
+ _swift_stdlib_isStackAllocationSafe
CStrings:
+ "DMF Fetch Apps request returned nil without error!"
+ "DMFSetAppAllowUserToHideRequest"
+ "DMFSetAppAllowUserToLockRequest"
+ "Failed to cast DMFFetchAppsRequest result object as DMFFetchAppsResultObject object. Fatal error"
+ "Failed to create DMF Fetch Apps Request"
+ "Failed to fetch any bundleIDs for protected apps."
+ "Fetch Apps request to DMFConnection failed with error: %!@(MISSING)"
+ "No unhideable apps found!"
+ "No unlockable apps found!"
+ "No unlockable or unhideable apps found!"
+ "UnsafeMutablePointer.initialize with negative count"
+ "allowUserToHide"
+ "allowUserToLock"
+ "boolValue"
+ "setAllowUserToHide:"
+ "setAllowUserToLock:"
+ "setManagedAppsOnly:"

```
