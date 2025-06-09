## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

```diff

-560.4.11.0.0
-  __TEXT.__text: 0x3b980
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x22ac
-  __TEXT.__const: 0x35c
+578.0.1.0.0
+  __TEXT.__text: 0x3a260
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x22d0
+  __TEXT.__const: 0x3fc
   __TEXT.__cstring: 0x1126
-  __TEXT.__oslogstring: 0x32e7
+  __TEXT.__oslogstring: 0x3397
   __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__swift5_typeref: 0x2b7
+  __TEXT.__swift5_typeref: 0x2bf
   __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__constg_swiftt: 0x9c
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_capture: 0x108
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__eh_frame: 0xb70
+  __TEXT.__unwind_info: 0xe70
+  __TEXT.__eh_frame: 0xac0
   __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x6d2a
+  __TEXT.__objc_methname: 0x6db0
   __TEXT.__objc_methtype: 0x1654
-  __TEXT.__objc_stubs: 0x41e0
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0xf20
+  __TEXT.__objc_stubs: 0x4200
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0xf00
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a8
+  __DATA_CONST.__objc_selrefs: 0x14b8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x6c0
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x6e8
   __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x34a8
+  __AUTH_CONST.__objc_const: 0x34b8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x48
+  __AUTH.__objc_data: 0x98
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x670
+  __DATA.__data: 0x5d0
   __DATA.__bss: 0x540
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xc58
+  __DATA_DIRTY.__objc_data: 0xc08
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7C06C162-CDB3-397C-9E29-160E08E48234
-  Functions: 1295
-  Symbols:   3834
-  CStrings:  1670
+  UUID: D7606712-DF4A-3E30-A267-EE2BE1256D2C
+  Functions: 1301
+  Symbols:   3828
+  CStrings:  1675
 
Symbols:
+ -[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]
+ GCC_except_table32
+ ___38-[RMBaseStore metadataReturningError:]_block_invoke.41
+ ___41-[RMBaseStore metadataValueForKey:error:]_block_invoke.43
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.40
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.40.cold.1
+ ___73-[RMBaseStore waitForProcessingOfDeclarations:timeout:completionHandler:]_block_invoke.cold.1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_RemoteManagementStore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_RemoteManagementStore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_RemoteManagementStore
+ _block_copy_helper.57
+ _block_copy_helper.60
+ _block_copy_helper.75
+ _block_copy_helper.78
+ _block_copy_helper.84
+ _block_copy_helper.88
+ _block_descriptor.59
+ _block_descriptor.62
+ _block_descriptor.77
+ _block_descriptor.80
+ _block_descriptor.86
+ _block_descriptor.90
+ _block_destroy_helper.58
+ _block_destroy_helper.61
+ _block_destroy_helper.76
+ _block_destroy_helper.79
+ _block_destroy_helper.85
+ _block_destroy_helper.89
+ _objc_msgSend$waitForProcessingOfDeclarations:timeout:storeIdentifier:completionHandler:
+ _swift_setDeallocating
+ _symbolic SS_SSt
- GCC_except_table29
- ___38-[RMBaseStore metadataReturningError:]_block_invoke.40
- ___41-[RMBaseStore metadataValueForKey:error:]_block_invoke.42
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_RemoteManagementStore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_RemoteManagementStore
- _block_copy_helper.56
- _block_copy_helper.59
- _block_copy_helper.74
- _block_copy_helper.77
- _block_copy_helper.82
- _block_copy_helper.86
- _block_descriptor.58
- _block_descriptor.61
- _block_descriptor.76
- _block_descriptor.79
- _block_descriptor.84
- _block_descriptor.88
- _block_destroy_helper.57
- _block_destroy_helper.60
- _block_destroy_helper.75
- _block_destroy_helper.78
- _block_destroy_helper.83
- _block_destroy_helper.87
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
CStrings:
+ "Declarations to be processed succeeded"
+ "Failed XPC connection while waiting for declarations to be processed: %{public}@"
+ "Failed to wait for declarations to be processed: %{public}@"
+ "waitForProcessingOfDeclarations:timeout:completionHandler:"
+ "waitForProcessingOfDeclarations:timeout:storeIdentifier:completionHandler:"

```
