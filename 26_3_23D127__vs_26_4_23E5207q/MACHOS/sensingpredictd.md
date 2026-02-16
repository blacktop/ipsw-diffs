## sensingpredictd

> `/usr/libexec/sensingpredictd`

```diff

-10.12.3.0.0
-  __TEXT.__text: 0x7c
-  __TEXT.__auth_stubs: 0x60
-  __TEXT.__cstring: 0x8b
-  __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x30
+11.27.0.0.1
+  __TEXT.__text: 0x7f0
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__const: 0x12
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__oslogstring: 0x19
+  __TEXT.__cstring: 0x19
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__eh_frame: 0xb8
+  __DATA_CONST.__auth_got: 0xc0
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x70
+  __DATA.__data: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
-  - /System/Library/PrivateFrameworks/Polaris.framework/Polaris
-  - /System/Library/PrivateFrameworks/SensingPredictExclaveDaemon.framework/SensingPredictExclaveDaemon
+  - /System/Library/PrivateFrameworks/SensingPredictDaemon.framework/SensingPredictDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D769F073-820B-394C-84BB-5FB12A2097E4
-  Functions: 1
-  Symbols:   8
-  CStrings:  5
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 0DF75157-7DCE-34B5-91E7-B49CD37D949A
+  Functions: 12
+  Symbols:   129
+  CStrings:  2
 
Symbols:
+ 
+ /Library/Caches/com.apple.xbs/AF19AD8A-3646-46E7-90E2-8784D891B2A9/TemporaryDirectory.CaAoaV/Binaries/CoreSensing/install/TempContent/Objects/SensingPredict.build/sensingpredictd.build/Objects-normal/arm64e/Main.o
+ /Library/Caches/com.apple.xbs/AF19AD8A-3646-46E7-90E2-8784D891B2A9/TemporaryDirectory.CaAoaV/Binaries/CoreSensing/install/TempContent/Objects/SensingPredict.build/sensingpredictd.build/Objects-normal/arm64e/sensingpredictd.swiftmodule
+ /Library/Caches/com.apple.xbs/AF19AD8A-3646-46E7-90E2-8784D891B2A9/TemporaryDirectory.CaAoaV/Sources/CoreSensing/SensingPredict/sensingpredictd/
+ Main.swift
+ _$s15sensingpredictd4MainV4mainyyYaKFZTf4d_n
+ _$s15sensingpredictd4MainV4mainyyYaKFZTf4d_nTQ1_
+ _$s15sensingpredictd4MainV4mainyyYaKFZTf4d_nTY0_
+ _$s15sensingpredictd4MainV4mainyyYaKFZTf4d_nTY2_
+ _$s15sensingpredictd4MainV4mainyyYaKFZTf4d_nTu
+ _$s15sensingpredictd6LoggerO6daemon33_EAB00FD9D6F0B3FF93E8CF7F659E281CLL2osABVvpZ
+ _$s15sensingpredictd6LoggerO6daemon33_EAB00FD9D6F0B3FF93E8CF7F659E281CLL_WZ
+ _$s15sensingpredictd6LoggerO6daemon33_EAB00FD9D6F0B3FF93E8CF7F659E281CLL_Wz
+ _$s20SensingPredictDaemon0C4MainO4mainyyYaFZ
+ _$s20SensingPredictDaemon0C4MainO4mainyyYaFZTu
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sIetH_yts5Error_pIegHrzo_TR10async_MainTf3npf_n
+ _$sIetH_yts5Error_pIegHrzo_TR10async_MainTf3npf_nTQ0_
+ _$sIetH_yts5Error_pIegHrzo_TR10async_MainTf3npf_nTY1_
+ _$sIetH_yts5Error_pIegHrzo_TR10async_MainTf3npf_nTY2_
+ _$sIetH_yts5Error_pIegHrzo_TR10async_MainTf3npf_nTu
+ _$sScA15unownedExecutorScevgTj
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sytN
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_sensingpredictd
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_sensingpredictd
+ _exit
+ _main
+ _objc_release_x20
+ _os_log_type_enabled
+ _swift_errorInMain
+ _swift_job_run
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_asyncMainDrainQueue
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_getMainExecutor
+ _swift_task_switch
- _LogControl
- _LogPrintF
- __LogCategory_Initialize
- _dispatch_main
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- radr://5614542
CStrings:
+ "Starting sensingpredictd"
+ "com.apple.sensingpredict"
- "?.*:level=chatty,.*:flags=public"
- "SensingPredictDaemon"
- "Starting SensingPredict Daemon"
- "com.apple.SensingPredict"
- "int main(int, const char **)"

```
