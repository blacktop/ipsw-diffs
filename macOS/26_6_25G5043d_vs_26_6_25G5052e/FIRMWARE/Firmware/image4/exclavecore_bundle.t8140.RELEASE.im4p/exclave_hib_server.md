## exclave_hib_server

> `Firmware/image4/exclavecore_bundle.t8140.RELEASE.im4p/exclave_hib_server`

```diff

-1195.160.7.0.0
+1195.160.7.0.1
   __TEXT.__text: 0x3b624 sha256:045f4d43566dd6044d7a9741780015fccfa4f8c0de161622523eeb26d207f7b9
   __TEXT.__const: 0x1c3d0 sha256:702e1de6e88ecc20ebaaf5b94af67e4a7b8eabfaa996fcdfe3b27e23766d0964
-  __TEXT.__cstring: 0xd23d sha256:ceef56d9e3ccb30ba504566bdd0e0504ec8dfaa1091ce54ffaec47486824db04
+  __TEXT.__cstring: 0xd23d sha256:5555805d05fb03f249724fa4dace928ded0c1baba48ea1be0a30fb409e6d7c09
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
-  __DATA.__bss: 0x479c8 sha256:c5fb635cfe1c5c2afdba73950e5a1b957d822616f16abab0e216d95a8cb1375a
+  __DATA.__bss: 0x479c8 sha256:b5bb08b4004f306cc8a3cecd5839f0765a908bf11363266d2dda31266b912a73
   __DATA.__common: 0x1618
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  UUID: 22F9E052-B641-3CE4-BFC9-FA288E710853
+  UUID: 4D0604E9-89ED-38B7-8294-E5B6C5943F9A
   Functions: 839
   Symbols:   4
   CStrings:  1195
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_-ugBpLpWsHN3Z-AQNERSbXjnWmtHZycnsRy0/Library/Caches/com.apple.xbs/TemporaryDirectory.mMI06S/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/hib-server/src/main.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/4~CSASugDto94LzXHdZR714DXLdcih_oAeW5WHnSw/Library/Caches/com.apple.xbs/TemporaryDirectory.5cRTiI/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/4~CRUgugCdcBv6SuOhCQPunwbJvIKYnjjJm-v6VaA/Library/Caches/com.apple.xbs/TemporaryDirectory.YD1Mi1/Sources/DriverKit_exclavecore/ExclaveDriverKit/DeviceTreeKit/DeviceTreeKit.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/common/platform_vas.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/hib-server/src/main.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/shadow.h"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/span.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/libvas/Source/vas.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/4~CRUkugDHDZVLGxViQPRveXB02UgHKc01nOeyKX4/Library/Caches/com.apple.xbs/TemporaryDirectory.rZwM7N/Sources/ExclavePlatform_services_exclavecore/xrt/xrt/ipc/endpoint.c"

```
