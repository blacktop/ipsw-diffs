## FindMyCommon

> `/System/Library/PrivateFrameworks/FindMyCommon.framework/FindMyCommon`

```diff

-61.10.7.2.1
-  __TEXT.__text: 0xf0ec
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__const: 0x460
-  __TEXT.__cstring: 0x6d9
-  __TEXT.__swift5_typeref: 0x20d
-  __TEXT.__oslogstring: 0x282
-  __TEXT.__constg_swiftt: 0x368
-  __TEXT.__swift5_reflstr: 0x2f7
-  __TEXT.__swift5_fieldmd: 0x2fc
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x38
+61.30.7.10.7
+  __TEXT.__text: 0x1539c
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__const: 0xe94
+  __TEXT.__cstring: 0x8e4
+  __TEXT.__swift5_typeref: 0x404
+  __TEXT.__oslogstring: 0x362
+  __TEXT.__constg_swiftt: 0x530
+  __TEXT.__swift5_reflstr: 0x500
+  __TEXT.__swift5_fieldmd: 0x5e0
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_proto: 0xb4
+  __TEXT.__swift5_types: 0x70
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x398
-  __TEXT.__eh_frame: 0x410
+  __TEXT.__swift5_assocty: 0x150
+  __TEXT.__swift5_capture: 0x74
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__eh_frame: 0x500
   __TEXT.__objc_methname: 0xff
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x558
-  __AUTH_CONST.__auth_ptr: 0x138
-  __AUTH_CONST.__const: 0x4c8
-  __AUTH_CONST.__objc_const: 0x180
-  __AUTH.__data: 0xa0
-  __DATA.__data: 0x100
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x300
-  __DATA_DIRTY.__data: 0x2c8
+  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__auth_ptr: 0x2b8
+  __AUTH_CONST.__const: 0xb70
+  __AUTH_CONST.__objc_const: 0x230
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0xb0
+  __DATA.__data: 0x278
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x1500
+  __DATA_DIRTY.__data: 0x370
   __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

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
-  Functions: 292
-  Symbols:   126
-  CStrings:  71
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 526
+  Symbols:   156
+  CStrings:  90
 
Symbols:
+ _OBJC_CLASS_$_OS_dispatch_queue
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ _calloc
+ _dispatch_semaphore_create
+ _objc_retain_x21
+ _os_state_add_handler
+ _os_state_remove_handler
+ _strlcpy
+ _swift_arrayInitWithCopy
+ _swift_deallocClassInstance
+ _swift_deallocPartialClassInstance
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_updateClassMetadata2
CStrings:
+ "<StateCaptureHandle: 0x"
+ "Added handler: %!{(MISSING)public}s %!s(MISSING)"
+ "Error from StateCapture handler %!{(MISSING)public}s: %!@(MISSING)"
+ "Negative value is not representable"
+ "NonModularSPI/Sandbox.swift"
+ "NonModularSPI/os_state_private.swift"
+ "Not enough bits to represent the passed value"
+ "Removing handler: %!{(MISSING)public}s %!s(MISSING)"
+ "Running state capture %!{(MISSING)public}s: reason: %!s(MISSING) requestor: %!s(MISSING)"
+ "State capture duration: %!{(MISSING)public}s: %!s(MISSING)"
+ "Swift/Integers.swift"
+ "This method is only supported on macOS!"
+ "UnsafeMutablePointer.initialize with negative count"
+ "[type: .serialized title: "
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_TtC12FindMyCommon12StateCapture"
+ "handle"
+ "id"
+ "queue"

```
