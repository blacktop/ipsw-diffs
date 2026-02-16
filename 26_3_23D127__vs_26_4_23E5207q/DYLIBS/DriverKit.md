## DriverKit

> `/System/Library/Frameworks/DriverKit.framework/DriverKit`

```diff

-451.0.0.0.0
-  __TEXT.__text: 0x367a0
-  __TEXT.__auth_stubs: 0xbc0
+456.100.10.0.0
+  __TEXT.__text: 0x36138
+  __TEXT.__auth_stubs: 0xbd0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x5d44
+  __TEXT.__const: 0x5f3c
   __TEXT.__cstring: 0x2e7d
   __TEXT.__oslogstring: 0xe
   __TEXT.__unwind_info: 0x190

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__structlayouts: 0x10
   __DATA_CONST.__osclassinfo: 0x158
-  __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH_CONST.__const: 0x5698
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x56f8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x170
-  __DATA.__bss: 0x440
+  __DATA.__bss: 0x448
   __DATA_DIRTY.__common: 0x300
   __DATA_DIRTY.__bss: 0x1008
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: B52DCCC3-D6D7-3A4F-B731-B22B662F1340
-  Functions: 1528
-  Symbols:   2927
+  UUID: F3F0EADE-87D5-39B4-A553-FC51D6A659EB
+  Functions: 1555
+  Symbols:   2980
   CStrings:  470
 
Symbols:
+ _IOKernelPanic
+ _IOSysCtlByName
+ _IOUserServerMain.cold.11
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespecb
+ __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespecb.cold.1
+ __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespecb.cold.2
+ __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespecb.cold.3
+ __ZN12IOUserServer12Panic_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcE
+ __ZN12IOUserServer5PanicEPKcPFiP15OSMetaClassBase5IORPCE
+ ____ZL31IOInterruptDispatchSourceThreadPv_block_invoke.253
+ ____ZL31IOInterruptDispatchSourceThreadPv_block_invoke_3
+ ___block_descriptor_tmp.252
+ ___block_descriptor_tmp.256
+ _pthread_cond_timedwait_relative_np
- __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespec
- __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespec.cold.1
- __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespec.cold.2
- __ZL21_IODispatchQueueSleepP26IODispatchQueue_LocalIVarsyPv8timespec.cold.3
- __ZL39OSCreateObjectFromSerializationInternalP15OSSerializationj.cold.3

```
