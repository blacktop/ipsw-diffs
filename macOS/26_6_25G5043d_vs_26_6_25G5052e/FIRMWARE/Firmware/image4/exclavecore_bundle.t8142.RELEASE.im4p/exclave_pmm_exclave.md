## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t8142.RELEASE.im4p/exclave_pmm_exclave`

```diff

-1195.160.7.0.0
+1195.160.7.0.1
   __TEXT.__text: 0x48360 sha256:94c3f8bf1170a2ca6f17bcd8337a3340c49e2097210ff988783a313d3eb8841c
   __TEXT.__const: 0x1cbd2 sha256:d9a943fd35e27d70f167e24a8a7e4d57f1df66bd4cb79f5833016cb3da992033
-  __TEXT.__cstring: 0x111c4 sha256:35558346d627d74820924fe9815ec46c40310fb584e5923c424506e43e49dc66
+  __TEXT.__cstring: 0x111c4 sha256:8bd0e6d2a8231412171dfdea18b4e2b8f7c186027ff2c377a147ad8ab59f3a2e
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x47e18 sha256:33e06bf0c619bcd56947b67b33a4eb524158401f313c0fbed5df3da8070f61d4
+  __DATA.__bss: 0x47e18 sha256:6239d7b52162140e67960586ef57114fe8e5c2e2fb4a51a835f7c07543d445c3
   __DATA.__common: 0x9108
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 97BBCA95-561B-30C7-931A-9FB3692D2DD3
+  UUID: 3CDC4853-E811-3536-83B1-B6C3B0042412
   Functions: 1133
   Symbols:   4
   CStrings:  1442
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_8ugCnwrCzVHqhrOSP6LQtuYToKxYFwZOJugo/Library/Caches/com.apple.xbs/TemporaryDirectory.j0n6dI/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/StatsDelegate_C.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/exclaves_upcalls_v2_C.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/bitmap.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/client.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/frame.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/main.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/object.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/pmm.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/xnu_allocator.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX26.6.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Binaries/Tightbeam_exclavecore/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavecore.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/Transports/cL4_large/cL4_large_transport.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/4~CRUeugB2DpCzbyypDzVwU6PuVMCCO8kqFxzgtQk/Library/Caches/com.apple.xbs/TemporaryDirectory.MNuxc7/Sources/Tightbeam_exclavecore/Runtime/Tightbeam/tb_message.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/StatsDelegate_C.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Binaries/ExclavePlatform_services_exclavecore/install/TempContent/Objects/pmm-server.build/pmm-server.build/DerivedSources/exclaves_upcalls_v2_C.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/bitmap.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/client.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/frame.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/main.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/object.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/pmm.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/pmm-server/src/xnu_allocator.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"

```
