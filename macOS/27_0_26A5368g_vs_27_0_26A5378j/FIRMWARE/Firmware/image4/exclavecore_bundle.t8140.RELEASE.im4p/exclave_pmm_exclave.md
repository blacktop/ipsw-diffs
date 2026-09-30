## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.im4p/exclave_pmm_exclave`

```diff

-  __TEXT.__text: 0x4ca84
+  __TEXT.__text: 0x4cc54
   __TEXT.__const: 0x1d160
-  __TEXT.__cstring: 0x121f3
+  __TEXT.__cstring: 0x12296
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x4f238
+  __DATA.__bss: 0x4edf8
   __DATA.__common: 0x91b0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0

   __PDATA.__shared_cache: 0x0
   Functions: 1210
   Symbols:   4
-  CStrings:  1510
+  CStrings:  1514
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA.__const : content changed
~ __DATA.__data : content changed
~ __DATA.__auth_ptr : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__mod_init_func : content changed
Functions:
~ sub_7fff550 : 448 -> 360
~ sub_7fff710 -> sub_7fff6b8 : 44 -> 140
~ sub_8002dd4 -> sub_8002ddc : 2176 -> 2204
~ sub_8007f7c -> sub_8007fa0 : 1100 -> 1076
~ sub_8008a04 -> sub_8008a10 : 1360 -> 1484
~ sub_800b4f0 -> sub_800b578 : 112 -> 108
~ sub_800dea8 -> sub_800df2c : 644 -> 648
~ sub_80177ec -> sub_8017874 : 476 -> 484
~ sub_801d904 -> sub_801d994 : 1392 -> 1380
~ sub_8020738 -> sub_80207bc : 3156 -> 3152
~ sub_8032778 -> sub_80327f8 : 492 -> 516
~ sub_8036010 -> sub_80360a8 : 88 -> 80
~ sub_80360d8 -> sub_8036168 : 272 -> 256
~ sub_8036b60 -> sub_8036be0 : 484 -> 480
~ sub_8037124 -> sub_80371a0 : 1652 -> 1656
~ sub_8037858 -> sub_80378d8 : 964 -> 988
~ sub_8037c1c -> sub_8037cb4 : 988 -> 1104
~ sub_8037ff8 -> sub_8038104 : 304 -> 248
~ sub_8038128 -> sub_80381fc : 32 -> 208
~ sub_8038148 -> sub_80382cc : 248 -> 232
~ sub_8038240 -> sub_80383b4 : 536 -> 564
~ sub_80386dc -> sub_803886c : 668 -> 672
~ sub_80391b0 -> sub_8039344 : 540 -> 544
~ sub_80393cc -> sub_8039564 : 108 -> 124
~ sub_803b490 -> sub_803b638 : 788 -> 828
CStrings:
+ "!os_mul_overflow(nu + PAD_ALLOC(align), UNIT_SIZE, &nb)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/StatsDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/exclaves_upcalls_v2_C.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/bitmap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/frame.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/object.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/pmm.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/xnu_allocator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m2WWUZ/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "morecore"
+ "no fixup data for faultable range [%#lx, %#lx) found"
+ "pmmtag_l4_decode: unknown tagtype %zu"
+ "write_float_string"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/StatsDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/exclaves_upcalls_v2_C.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/bitmap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/frame.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/object.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/pmm.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/xnu_allocator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rPseBA/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "write_float"

```
