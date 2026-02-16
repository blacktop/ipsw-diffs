## HeartRateCoordinator

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x3d34
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x6e4
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__oslogstring: 0x3b2
+31.0.0.0.0
+  __TEXT.__text: 0x45e0
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_methlist: 0x784
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x31c
+  __TEXT.__oslogstring: 0x3f8
   __TEXT.__cstring: 0x240
-  __TEXT.__unwind_info: 0x210
-  __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0xfda
-  __TEXT.__objc_methtype: 0x3a8
-  __TEXT.__objc_stubs: 0x8e0
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__unwind_info: 0x268
+  __TEXT.__objc_classname: 0x1ce
+  __TEXT.__objc_methname: 0x11b9
+  __TEXT.__objc_methtype: 0x417
+  __TEXT.__objc_stubs: 0x9a0
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0xf50
+  __AUTH_CONST.__objc_const: 0x10e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xa8
-  __DATA.__data: 0x360
-  __DATA_DIRTY.__objc_data: 0x190
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__data: 0x3c0
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4567A9F-40F3-3D22-BD9E-A9C5BF029FAA
-  Functions: 122
-  Symbols:   572
-  CStrings:  304
+  UUID: E83DF0C7-443B-3A19-98B3-0FFF8A19B3DA
+  Functions: 138
+  Symbols:   621
+  CStrings:  326
 
Symbols:
+ -[HRCHeartRateRequestor handleHeartRateData:].cold.1
+ -[HRCHeartRateRequestor heartRateFeatureEnabled:]
+ -[HRCHeartRateRequestor heartRatePrivacyToggleEnabled]
+ -[HRCHeartRateRequestor initWithDelegate:onQueue:connectionHelper:privacyMonitor:]
+ -[HRCHeartRateRequestor privacyToggleMonitor]
+ -[HRCHeartRateRequestor setHeartRatePrivacyToggleEnabled:]
+ -[HRCHeartRateRequestor setPrivacyToggleMonitor:]
+ -[HRCPrivacyToggleMonitor .cxx_destruct]
+ -[HRCPrivacyToggleMonitor _heartRateFeatureEnabled:]
+ -[HRCPrivacyToggleMonitor dealloc]
+ -[HRCPrivacyToggleMonitor delegate]
+ -[HRCPrivacyToggleMonitor setDelegate:]
+ -[HRCPrivacyToggleMonitor startObservingWithDelegate:onQueue:]
+ GCC_except_table12
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table7
+ GCC_except_table9
+ _OBJC_CLASS_$_HRCPrivacyToggleMonitor
+ _OBJC_IVAR_$_HRCHeartRateRequestor._heartRatePrivacyToggleEnabled
+ _OBJC_IVAR_$_HRCHeartRateRequestor._privacyToggleMonitor
+ _OBJC_IVAR_$_HRCPrivacyToggleMonitor._center
+ _OBJC_IVAR_$_HRCPrivacyToggleMonitor._delegate
+ _OBJC_IVAR_$_HRCPrivacyToggleMonitor._delegateQueue
+ _OBJC_METACLASS_$_HRCPrivacyToggleMonitor
+ _OUTLINED_FUNCTION_0
+ __OBJC_$_INSTANCE_METHODS_HRCPrivacyToggleMonitor
+ __OBJC_$_INSTANCE_VARIABLES_HRCPrivacyToggleMonitor
+ __OBJC_$_PROP_LIST_HRCPrivacyToggleMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HRCPrivacyToggleMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HRCPrivacyToggleMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_HRCPrivacyToggleMonitorDelegate
+ __OBJC_CLASS_RO_$_HRCPrivacyToggleMonitor
+ __OBJC_LABEL_PROTOCOL_$_HRCPrivacyToggleMonitorDelegate
+ __OBJC_METACLASS_RO_$_HRCPrivacyToggleMonitor
+ __OBJC_PROTOCOL_$_HRCPrivacyToggleMonitorDelegate
+ ___52-[HRCPrivacyToggleMonitor _heartRateFeatureEnabled:]_block_invoke
+ ___82-[HRCHeartRateRequestor initWithDelegate:onQueue:connectionHelper:privacyMonitor:]_block_invoke
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ __os_log_debug_impl
+ _objc_msgSend$_heartRateFeatureEnabled:
+ _objc_msgSend$heartRateFeatureEnabled:
+ _objc_msgSend$heartRatePrivacyToggleEnabled
+ _objc_msgSend$initWithDelegate:onQueue:connectionHelper:privacyMonitor:
+ _objc_msgSend$setHeartRatePrivacyToggleEnabled:
+ _objc_msgSend$startObservingWithDelegate:onQueue:
+ _objc_retainAutoreleasedReturnValue
- -[HRCHeartRateRequestor initWithDelegate:onQueue:connectionHelper:]
- GCC_except_table10
- GCC_except_table13
- GCC_except_table5
- GCC_except_table8
- _objc_claimAutoreleasedReturnValue
- _objc_getProperty
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "!"
+ "@\"<HRCPrivacyToggleMonitorDelegate>\""
+ "@\"HRCPrivacyToggleMonitor\""
+ "@48@0:8@16@24@32@40"
+ "HRCPrivacyToggleMonitor"
+ "HRCPrivacyToggleMonitorDelegate"
+ "T@\"<HRCPrivacyToggleMonitorDelegate>\",W,N,V_delegate"
+ "T@\"HRCPrivacyToggleMonitor\",&,N,V_privacyToggleMonitor"
+ "T@\"NSString\",R,N,V_UDIDeviceIdentifier"
+ "T@\"NSString\",R,N,V_bluetoothIdentifier"
+ "T@\"NSString\",R,N,V_firmwareVersion"
+ "T@\"NSString\",R,N,V_hardwareVersion"
+ "T@\"NSString\",R,N,V_localIdentifier"
+ "T@\"NSString\",R,N,V_manufacturer"
+ "T@\"NSString\",R,N,V_model"
+ "T@\"NSString\",R,N,V_name"
+ "T@\"NSString\",R,N,V_softwareVersion"
+ "TB,N,V_heartRatePrivacyToggleEnabled"
+ "^{__CFNotificationCenter=}"
+ "_center"
+ "_heartRateFeatureEnabled:"
+ "_heartRatePrivacyToggleEnabled"
+ "_privacyToggleMonitor"
+ "heart rate feature enabled : %{public, BOOL}d"
+ "heartRateFeatureEnabled:"
+ "heartRatePrivacyToggleEnabled"
+ "initWithDelegate:onQueue:connectionHelper:privacyMonitor:"
+ "privacyToggleMonitor"
+ "received heart rate sample in client process with uuid : %{private}@"
+ "setHeartRatePrivacyToggleEnabled:"
+ "setPrivacyToggleMonitor:"
+ "startObservingWithDelegate:onQueue:"
- "T@\"NSString\",R,V_UDIDeviceIdentifier"
- "T@\"NSString\",R,V_bluetoothIdentifier"
- "T@\"NSString\",R,V_firmwareVersion"
- "T@\"NSString\",R,V_hardwareVersion"
- "T@\"NSString\",R,V_localIdentifier"
- "T@\"NSString\",R,V_manufacturer"
- "T@\"NSString\",R,V_model"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_softwareVersion"
- "received heart rate sample in client process"

```
