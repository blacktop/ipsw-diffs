## DeviceSharingServicesCore

> `/System/Library/PrivateFrameworks/DeviceSharingServicesCore.framework/DeviceSharingServicesCore`

```diff

-27.60.30.0.1
-  __TEXT.__text: 0xd54c
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x590
-  __TEXT.__swift5_typeref: 0x3a1
-  __TEXT.__swift5_fieldmd: 0x164
-  __TEXT.__constg_swiftt: 0x348
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__cstring: 0x4e4
-  __TEXT.__swift5_reflstr: 0x124
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__swift5_capture: 0x18c
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__oslogstring: 0xa6
-  __TEXT.__unwind_info: 0x5e0
-  __TEXT.__eh_frame: 0x12d0
-  __TEXT.__objc_methname: 0x177
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x8
+27.100.10.0.2
+  __TEXT.__text: 0x141a4
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x70
+  __TEXT.__const: 0x728
+  __TEXT.__cstring: 0x374
+  __TEXT.__oslogstring: 0xeb
+  __TEXT.__swift5_typeref: 0x4b5
+  __TEXT.__swift5_fieldmd: 0x1d4
+  __TEXT.__constg_swiftt: 0x3e4
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift_as_entry: 0xb4
+  __TEXT.__swift_as_ret: 0x90
+  __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_reflstr: 0x1c4
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__eh_frame: 0x1578
+  __TEXT.__objc_methname: 0x1fa
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78
+  __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x450
-  __AUTH_CONST.__auth_ptr: 0x178
-  __AUTH_CONST.__const: 0x588
-  __AUTH_CONST.__objc_const: 0x1f0
-  __AUTH.__objc_data: 0x38
-  __AUTH.__data: 0x178
-  __DATA.__data: 0x388
-  __DATA.__bss: 0x780
-  __DATA.__common: 0x18
+  __AUTH_CONST.__auth_got: 0x4e8
+  __AUTH_CONST.__auth_ptr: 0x1e0
+  __AUTH_CONST.__const: 0x888
+  __AUTH_CONST.__objc_const: 0x260
+  __AUTH.__objc_data: 0xc0
+  __AUTH.__data: 0x1a0
+  __DATA.__data: 0x458
+  __DATA.__bss: 0x980
+  __DATA.__common: 0x48
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 327
-  Symbols:   130
-  CStrings:  51
+  Functions: 441
+  Symbols:   164
+  CStrings:  57
 
Symbols:
+ _OBJC_CLASS_$_DeviceSharingDefaults
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_DeviceSharingDefaults
+ _OBJC_METACLASS_$_NSObject
+ __swiftImmortalRefCount
+ _objc_msgSendSuper2
+ _objc_release_x19
+ _objc_retain
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_deallocPartialClassInstance
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_makeBoxUnique
+ _swift_runtimeSupportsNoncopyableTypes
- _swift_allocateGenericValueMetadata
CStrings:
+ "%{public}s registering handler for %{public}s"
+ ".cxx_destruct"
+ "@16@0:8"
+ "LogPeerConnectionPayloadSize"
+ "RecentlySharedApplications"
+ "[%{public}s] XPC state is %{public}s"
+ "[UserDefaults: com.apple.devicesharingd]"
+ "bundleIdentifier"
+ "com.apple.devicesharingd"
+ "dealloc"
+ "hasSeenGuestUserHandoverPromotion"
+ "init"
+ "initWithSuiteName:"
+ "log"
+ "mainBundle"
+ "objectForKey:"
+ "setObject:forKey:"
+ "standardUserDefaults"
+ "storage"
+ "v16@0:8"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "[%s] XPC state is %s"
- "invalid Collection: less than 'count' elements in collection"

```
