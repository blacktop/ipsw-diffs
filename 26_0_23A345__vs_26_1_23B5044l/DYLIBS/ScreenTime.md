## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-605.0.1.0.0
-  __TEXT.__text: 0x5844
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x784
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x306
-  __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__oslogstring: 0x548
-  __TEXT.__unwind_info: 0x280
-  __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x1667
+605.1.8.0.0
+  __TEXT.__text: 0x4a48
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x71c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x2ea
+  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__oslogstring: 0x4a6
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_classname: 0x102
+  __TEXT.__objc_methname: 0x1644
   __TEXT.__objc_methtype: 0x538
-  __TEXT.__objc_stubs: 0x1000
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x38
+  __TEXT.__objc_stubs: 0xfe0
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x5c0
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1d8
-  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0xf20
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__objc_const: 0xe60
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x50
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86787819-78A9-37FB-942A-1B3F12FBB0BD
-  Functions: 183
-  Symbols:   810
-  CStrings:  367
+  UUID: E3C35391-B4B8-3E9A-BFBD-4C1D81FC4BF9
+  Functions: 163
+  Symbols:   737
+  CStrings:  359
 
Symbols:
+ ___32-[STWebHistory deleteAllHistory]_block_invoke.cold.1
+ ___32-[STWebHistory deleteAllHistory]_block_invoke.cold.2
+ ___36-[STWebHistory deleteHistoryForURL:]_block_invoke.cold.1
+ ___36-[STWebHistory deleteHistoryForURL:]_block_invoke.cold.2
+ ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.cold.1
+ ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.cold.2
+ ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke.cold.1
- +[STPublicServiceConnection newConnection]
- -[STScreenTimeConfigurationObserver _requestConfiguration].cold.1
- -[STWebHistory deleteAllHistory].cold.1
- -[STWebHistory deleteAllHistory].cold.2
- -[STWebHistory deleteHistoryDuringInterval:].cold.1
- -[STWebHistory deleteHistoryDuringInterval:].cold.2
- -[STWebHistory deleteHistoryForURL:].cold.1
- -[STWebHistory deleteHistoryForURL:].cold.2
- GCC_except_table11
- GCC_except_table18
- GCC_except_table23
- _OBJC_CLASS_$_STPublicServiceConnection
- _OBJC_METACLASS_$_STPublicServiceConnection
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _STPublicMachServiceName
- __Block_object_dispose
- __OBJC_$_CLASS_METHODS_STPublicServiceConnection
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_STPublicServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_STPublicServiceProtocol
- __OBJC_CLASS_RO_$_STPublicServiceConnection
- __OBJC_LABEL_PROTOCOL_$_STPublicServiceProtocol
- __OBJC_METACLASS_RO_$_STPublicServiceConnection
- __OBJC_PROTOCOL_$_STPublicServiceProtocol
- __OBJC_PROTOCOL_REFERENCE_$_STPublicServiceProtocol
- ___32-[STWebHistory deleteAllHistory]_block_invoke.19
- ___32-[STWebHistory deleteAllHistory]_block_invoke.19.cold.1
- ___32-[STWebHistory deleteAllHistory]_block_invoke.19.cold.2
- ___32-[STWebHistory deleteAllHistory]_block_invoke_2.20
- ___32-[STWebHistory deleteAllHistory]_block_invoke_2.20.cold.1
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke.15
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke.15.cold.1
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke.15.cold.2
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.16
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.16.cold.1
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17.cold.1
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17.cold.2
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.18
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.18.cold.1
- ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke.38
- ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke.38.cold.1
- ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke_2.39
- ___58-[STScreenTimeConfigurationObserver _requestConfiguration]_block_invoke_2.39.cold.1
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- __os_feature_enabled_impl
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_retain_x23
CStrings:
- "Failed to delete all web history with error: %{public}@"
- "Failed to fetch ScreenTime Agent proxy: %{public}@"
- "Failed to retrieve ScreenTime Configuration %{public}@"
- "STPublicServiceConnection"
- "STPublicServiceProtocol"
- "ScreenTime"
- "remoteObjectProxyWithErrorHandler:"
- "simplified_agent"

```
