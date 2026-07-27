## dyld

> `/System/ExclaveKit/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__AUTH_CONST.__const`
- `__DATA.__bss`
- `__DATA_DIRTY.__all_image_info`

```diff

-1385.0.0.0.0
-  __TEXT.__text: 0x57fa8
+1387.0.0.0.0
+  __TEXT.__text: 0x57fb0
   __TEXT.__const: 0x1bae1
   __TEXT.__cstring: 0xe581
   __TEXT.__unwind_info: 0x848
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/common/Array.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/common/MachOAnalyzer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/common/MachOLayout.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/common/Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/Loader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/lsl/Allocator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/lsl/Allocator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/mach_o/Platform.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7jxJYe/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bL7yy5/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bL7yy5/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bL7yy5/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bL7yy5/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bL7yy5/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fYf9cu/Sources/libclosure_exclavekit/runtime.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xKFWgf/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
+ "1387"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HrKT1K/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HrKT1K/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HrKT1K/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HrKT1K/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HrKT1K/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QZ1vTm/Sources/libclosure_exclavekit/runtime.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/common/Array.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/common/MachOAnalyzer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/common/MachOLayout.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/common/Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/Loader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/lsl/Allocator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/lsl/Allocator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/mach_o/Platform.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iJrMWr/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qrlQxP/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
- "1385"
```
