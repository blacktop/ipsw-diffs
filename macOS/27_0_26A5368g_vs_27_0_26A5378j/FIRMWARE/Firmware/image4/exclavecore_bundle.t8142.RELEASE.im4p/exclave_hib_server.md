## exclave_hib_server

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.im4p/exclave_hib_server`

```diff

-  __TEXT.__text: 0x3ec44
+  __TEXT.__text: 0x3ede8
   __TEXT.__const: 0x1c930
-  __TEXT.__cstring: 0xde64
+  __TEXT.__cstring: 0xdee1
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x4ede8
+  __DATA.__bss: 0x4e9a8
   __DATA.__common: 0x1760
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0

   __PDATA.__shared_cache: 0x0
   Functions: 871
   Symbols:   4
-  CStrings:  1238
+  CStrings:  1241
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA.__data : content changed
~ __DATA.__const : content changed
~ __DATA.__auth_ptr : content changed
~ __DATA.__shared_cache : content changed
~ __DATA.__mod_init_func : content changed
Functions:
~ sub_7fff538 : 1100 -> 1076
~ sub_7ffffc0 -> sub_7ffffa8 : 1360 -> 1484
~ sub_8002ac8 -> sub_8002b2c : 112 -> 108
~ sub_800ec24 -> sub_800ec84 : 476 -> 484
~ sub_8014b84 -> sub_8014bec : 1392 -> 1380
~ sub_8017830 -> sub_801788c : 3148 -> 3152
~ sub_8029148 -> sub_80291a8 : 524 -> 548
~ sub_802c984 -> sub_802c9fc : 84 -> 76
~ sub_802ca48 -> sub_802cab8 : 256 -> 272
~ sub_802d4c0 -> sub_802d540 : 484 -> 480
~ sub_802d9cc -> sub_802da48 : 1652 -> 1656
~ sub_802e100 -> sub_802e180 : 964 -> 988
~ sub_802e4c4 -> sub_802e55c : 988 -> 1104
~ sub_802e8a0 -> sub_802e9ac : 304 -> 248
~ sub_802e9d0 -> sub_802eaa4 : 32 -> 208
~ sub_802e9f0 -> sub_802eb74 : 248 -> 232
~ sub_802eae8 -> sub_802ec5c : 536 -> 564
~ sub_802f734 -> sub_802f8c4 : 540 -> 544
~ sub_802f950 -> sub_802fae4 : 108 -> 124
~ sub_80319e0 -> sub_8031b84 : 720 -> 716
~ sub_8031d20 -> sub_8031ec0 : 6424 -> 6392
~ sub_8034710 -> sub_8034890 : 788 -> 828
~ sub_8035460 -> sub_8035608 : 140 -> 136
~ sub_803b620 -> sub_803b7c4 : 616 -> 612
CStrings:
+ "!os_mul_overflow(nu + PAD_ALLOC(align), UNIT_SIZE, &nb)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/hib-server/src/main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.84F0sL/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GMFCKn/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "morecore"
+ "no fixup data for faultable range [%#lx, %#lx) found"
+ "write_float_string"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/hib-server/src/main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DdO8Ac/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kKFJ2p/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "write_float"

```
