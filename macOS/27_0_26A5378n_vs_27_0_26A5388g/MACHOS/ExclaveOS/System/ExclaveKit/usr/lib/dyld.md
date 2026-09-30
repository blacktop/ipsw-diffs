## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27059.3.0.0.0
-  __TEXT.__text: 0x5bc7c
+27060.0.0.0.0
+  __TEXT.__text: 0x5bc9c
   __TEXT.__const: 0x1c0a8
-  __TEXT.__cstring: 0xeaa5
-  __TEXT.__unwind_info: 0x1ea0
+  __TEXT.__cstring: 0xeaa3
+  __TEXT.__unwind_info: 0x1e98
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0xaf0
   __AUTH_CONST.__const: 0x3f18

   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x550
-  __DATA.__bss: 0xba3f8
+  __DATA.__bss: 0xba408
   __DATA_DIRTY.__all_image_info: 0x170
   Functions: 2746
   Symbols:   2423
Functions:
~ __ZN5dyld4L14initializeLibcEPNS_10KernelArgsEPv : 148 -> 152
~ ____ZN5dyld3L26verboseSharedCacheMappingsEPK15DyldSharedCache_block_invoke : 76 -> 72
~ _plat_common_parse_entry_vec -> _xrt__platform_entry_args : 68 -> 20
~ _xrt__platform_entry_args -> _plat_common_parse_entry_vec : 20 -> 68
~ _xrt__platform_parse_entry_vec : 668 -> 692
~ sub_26958 -> sub_26970 : 172 -> 180
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1pcAQ4/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dx86rx/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dx86rx/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dx86rx/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dx86rx/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dx86rx/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.F9H0Vv/Sources/libclosure_exclavekit/runtime.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/Array.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/CString.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/MachOLayout.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/common/Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/Loader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/lsl/Allocator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/lsl/Allocator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/lsl/Vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/mach_o/Header.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/mach_o/Image.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/mach_o/Platform.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kW5eE8/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
+ "27060"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qjqnf0/Sources/libclosure_exclavekit/runtime.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cXXn6Z/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oMNIk0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/Array.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/CString.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/MachOLayout.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/common/Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/Loader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Allocator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Allocator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/lsl/Vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Header.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Image.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Platform.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xgBOqI/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
- "27059.3"
```
