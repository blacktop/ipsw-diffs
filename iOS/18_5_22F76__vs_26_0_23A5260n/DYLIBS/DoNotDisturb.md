## DoNotDisturb

> `/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb`

```diff

-433.6.1.0.0
-  __TEXT.__text: 0x461e4
+461.0.0.0.0
+  __TEXT.__text: 0x4665c
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x465c
+  __TEXT.__objc_methlist: 0x46ac
   __TEXT.__const: 0x252
-  __TEXT.__cstring: 0x36d7
-  __TEXT.__gcc_except_tab: 0x1624
-  __TEXT.__oslogstring: 0x53bb
-  __TEXT.__unwind_info: 0x1550
+  __TEXT.__cstring: 0x3727
+  __TEXT.__gcc_except_tab: 0x164c
+  __TEXT.__oslogstring: 0x5469
+  __TEXT.__unwind_info: 0x1568
   __TEXT.__objc_classname: 0xf4b
-  __TEXT.__objc_methname: 0x8e05
-  __TEXT.__objc_methtype: 0x1e7a
-  __TEXT.__objc_stubs: 0x45a0
+  __TEXT.__objc_methname: 0x8f2c
+  __TEXT.__objc_methtype: 0x1e7d
+  __TEXT.__objc_stubs: 0x45e0
   __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x12a8
+  __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a00
+  __DATA_CONST.__objc_selrefs: 0x1a20
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x328
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0xcbe0
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__objc_const: 0xcc28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x3dc
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0xeb0
   __DATA.__bss: 0x10
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x70

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: ACA552A3-6B8C-3CA4-BA17-17E9593381D4
-  Functions: 1672
-  Symbols:   5934
-  CStrings:  2847
+  UUID: 5F467841-46DC-3297-80A4-E74DAC1F0DAE
+  Functions: 1679
+  Symbols:   5931
+  CStrings:  2858
 
Symbols:
+ -[DNDClientEventDetails _initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:shouldAdjustEventBehaviorForMirroring:behavior:forwardingBehavior:title:subtitle:body:]
+ -[DNDClientEventDetails shouldAdjustEventBehaviorForMirroring]
+ -[DNDModeConfigurationService resetAppConfigurationState]
+ -[DNDModeConfigurationService resetAppConfigurationState].cold.1
+ -[DNDMutableClientEventDetails setShouldAdjustEventBehaviorForMirroring:]
+ -[DNDRemoteServiceConnection resetAppConfigurationStateWithRequestDetails:completionHandler:]
+ GCC_except_table58
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table91
+ OBJC_IVAR_$_DNDClientEventDetails._shouldAdjustEventBehaviorForMirroring
+ ___57-[DNDModeConfigurationService resetAppConfigurationState]_block_invoke
+ ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.267
+ ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.270
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.277
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.280
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.284
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.288
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.291
+ ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke_2.283
+ ___93-[DNDRemoteServiceConnection resetAppConfigurationStateWithRequestDetails:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32r_e30_v24?0"NSNumber"8"NSError"16lr32l8
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.272
+ ___block_literal_global.322
+ ___block_literal_global.328
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DoNotDisturb
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DoNotDisturb
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DoNotDisturb
+ _objc_msgSend$_initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:shouldAdjustEventBehaviorForMirroring:behavior:forwardingBehavior:title:subtitle:body:
+ _objc_msgSend$resetAppConfigurationStateWithRequestDetails:completionHandler:
+ _objc_msgSend$shouldAdjustEventBehaviorForMirroring
- -[DNDClientEventDetails _initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:behavior:forwardingBehavior:title:subtitle:body:]
- GCC_except_table55
- GCC_except_table69
- GCC_except_table76
- GCC_except_table79
- GCC_except_table89
- ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.266
- ___62-[DNDRemoteServiceConnection _connectionLock_createConnection]_block_invoke.269
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.276
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.278
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.283
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.286
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke.289
- ___66-[DNDRemoteServiceConnection _monitorLock_createMonitorConnection]_block_invoke_2.282
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.321
- ___block_literal_global.327
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DoNotDisturb
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DoNotDisturb
- _objc_msgSend$_initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:behavior:forwardingBehavior:title:subtitle:body:
CStrings:
+ "<%@: %p; identifier: '%@'; bundleIdentifier: %@; platform: %@; type: %@; urgency: %@; sender: %@; threadIdentifier: %@; filterCritera: %@; notifyAnyway: %d; behavior: %@; forwardingBehavior: %@; title: %@; subtitle: %@; body: %@; shouldAdjustEventBehaviorForMirroring: %d>"
+ "@128@0:8@16@24Q32Q40Q48@56@64@72B80B84Q88@96@104@112@120"
+ "TB,R,N,V_shouldAdjustEventBehaviorForMirroring"
+ "[%{public}@] Failed to reset app configuration state"
+ "[%{public}@] Reset app configuration state"
+ "_initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:shouldAdjustEventBehaviorForMirroring:behavior:forwardingBehavior:title:subtitle:body:"
+ "_shouldAdjustEventBehaviorForMirroring"
+ "com.apple.donotdisturb.DNDModeConfigurationService.resetAppConfigurationState"
+ "resetAppConfigurationState"
+ "resetAppConfigurationStateWithRequestDetails:completionHandler:"
+ "setShouldAdjustEventBehaviorForMirroring:"
+ "shouldAdjustEventBehaviorForMirroring"
- "<%@: %p; identifier: '%@'; bundleIdentifier: %@; platform: %@; type: %@; urgency: %@; sender: %@; threadIdentifier: %@; filterCritera: %@; notifyAnyway: %d; behavior: %@; forwardingBehavior: %@; title: %@; subtitle: %@; body: %@>"
- "@124@0:8@16@24Q32Q40Q48@56@64@72B80Q84@92@100@108@116"
- "_initWithIdentifier:bundleIdentifier:platform:type:urgency:sender:threadIdentifier:filterCriteria:notifyAnyway:behavior:forwardingBehavior:title:subtitle:body:"

```
