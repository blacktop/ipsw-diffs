## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-  __TEXT.__text: 0x5bcc
-  __TEXT.__objc_methlist: 0x804
+  __TEXT.__text: 0x6f90
+  __TEXT.__objc_methlist: 0x9d4
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x7c3
-  __TEXT.__oslogstring: 0x702
-  __TEXT.__gcc_except_tab: 0x2ac
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__cstring: 0x938
+  __TEXT.__gcc_except_tab: 0x35c
+  __TEXT.__oslogstring: 0x7a0
+  __TEXT.__unwind_info: 0x300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0xd8
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x5a0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__got: 0xe0
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0x1b88
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x1e0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0xbc
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   848
-  CStrings:  137
+  Functions: 254
+  Symbols:   1033
+  CStrings:  159
 
Sections:
~ __TEXT.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[BIThermalPredictionOutput supportsSecureCoding]
+ -[BIThermalPredictionClient .cxx_destruct]
+ -[BIThermalPredictionClient cachedError]
+ -[BIThermalPredictionClient cachedPrediction]
+ -[BIThermalPredictionClient connection]
+ -[BIThermalPredictionClient dealloc]
+ -[BIThermalPredictionClient delegate]
+ -[BIThermalPredictionClient didReceivePredictionUpdate:error:]
+ -[BIThermalPredictionClient init]
+ -[BIThermalPredictionClient logger]
+ -[BIThermalPredictionClient predictTLCWithError:]
+ -[BIThermalPredictionClient queue]
+ -[BIThermalPredictionClient reconnectToken]
+ -[BIThermalPredictionClient registerForUpdates]
+ -[BIThermalPredictionClient respondToReconnect]
+ -[BIThermalPredictionClient setCachedError:]
+ -[BIThermalPredictionClient setCachedPrediction:]
+ -[BIThermalPredictionClient setConnection:]
+ -[BIThermalPredictionClient setDelegate:]
+ -[BIThermalPredictionClient setLogger:]
+ -[BIThermalPredictionClient setQueue:]
+ -[BIThermalPredictionClient setReconnectToken:]
+ -[BIThermalPredictionClient updatePrediction]
+ -[BIThermalPredictionOutput confidenceScore]
+ -[BIThermalPredictionOutput description]
+ -[BIThermalPredictionOutput encodeWithCoder:]
+ -[BIThermalPredictionOutput initWithCoder:]
+ -[BIThermalPredictionOutput setConfidenceScore:]
+ -[BIThermalPredictionOutput setWillHitTLC:]
+ -[BIThermalPredictionOutput willHitTLC]
+ GCC_except_table0
+ GCC_except_table14
+ GCC_except_table5
+ GCC_except_table9
+ _BIThermalPredictionErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_BIThermalPredictionClient
+ _OBJC_CLASS_$_BIThermalPredictionOutput
+ _OBJC_IVAR_$_BIThermalPredictionClient._cachedError
+ _OBJC_IVAR_$_BIThermalPredictionClient._cachedPrediction
+ _OBJC_IVAR_$_BIThermalPredictionClient._connection
+ _OBJC_IVAR_$_BIThermalPredictionClient._delegate
+ _OBJC_IVAR_$_BIThermalPredictionClient._logger
+ _OBJC_IVAR_$_BIThermalPredictionClient._queue
+ _OBJC_IVAR_$_BIThermalPredictionClient._reconnectToken
+ _OBJC_IVAR_$_BIThermalPredictionOutput._confidenceScore
+ _OBJC_IVAR_$_BIThermalPredictionOutput._willHitTLC
+ _OBJC_METACLASS_$_BIThermalPredictionClient
+ _OBJC_METACLASS_$_BIThermalPredictionOutput
+ __OBJC_$_CLASS_METHODS_BIThermalPredictionOutput
+ __OBJC_$_CLASS_PROP_LIST_BIThermalPredictionOutput
+ __OBJC_$_INSTANCE_METHODS_BIThermalPredictionClient
+ __OBJC_$_INSTANCE_METHODS_BIThermalPredictionOutput
+ __OBJC_$_INSTANCE_VARIABLES_BIThermalPredictionClient
+ __OBJC_$_INSTANCE_VARIABLES_BIThermalPredictionOutput
+ __OBJC_$_PROP_LIST_BIThermalPredictionClient
+ __OBJC_$_PROP_LIST_BIThermalPredictionOutput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BIThermalPredictionClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BIThermalPredictionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BIThermalPredictionClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BIThermalPredictionProtocol
+ __OBJC_$_PROTOCOL_REFS_BIThermalPredictionClientProtocol
+ __OBJC_$_PROTOCOL_REFS_BIThermalPredictionProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BIThermalPredictionClient
+ __OBJC_CLASS_PROTOCOLS_$_BIThermalPredictionOutput
+ __OBJC_CLASS_RO_$_BIThermalPredictionClient
+ __OBJC_CLASS_RO_$_BIThermalPredictionOutput
+ __OBJC_LABEL_PROTOCOL_$_BIThermalPredictionClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_BIThermalPredictionProtocol
+ __OBJC_METACLASS_RO_$_BIThermalPredictionClient
+ __OBJC_METACLASS_RO_$_BIThermalPredictionOutput
+ __OBJC_PROTOCOL_$_BIThermalPredictionClientProtocol
+ __OBJC_PROTOCOL_$_BIThermalPredictionProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BIThermalPredictionClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BIThermalPredictionProtocol
+ ___33-[BIThermalPredictionClient init]_block_invoke
+ ___36-[BIThermalPredictionClient dealloc]_block_invoke
+ ___45-[BIThermalPredictionClient updatePrediction]_block_invoke
+ ___47-[BIThermalPredictionClient registerForUpdates]_block_invoke
+ ___47-[BIThermalPredictionClient registerForUpdates]_block_invoke_2
+ ___49-[BIThermalPredictionClient predictTLCWithError:]_block_invoke
+ ___62-[BIThermalPredictionClient didReceivePredictionUpdate:error:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_40_e8_32w_e47_v24?0"BIThermalPredictionOutput"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0i8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kQueueSpecificKey
+ _objc_getProperty
+ _objc_msgSend$cachedError
+ _objc_msgSend$cachedPrediction
+ _objc_msgSend$connection
+ _objc_msgSend$didUpdateTLCPrediction:error:
+ _objc_msgSend$predictTLCWithHandler:
+ _objc_msgSend$registerForUpdates
+ _objc_msgSend$registerForUpdatesWithClient:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$respondToReconnect
+ _objc_msgSend$setCachedError:
+ _objc_msgSend$setCachedPrediction:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$unregisterClient:
+ _objc_msgSend$updatePrediction
+ _objc_setProperty_atomic
CStrings:
+ "%"
+ "<BIThermalPredictionOutput: willHitTLC=%d, confidence=%.2f>"
+ "BIThermalPredictionClient"
+ "Connection interrupted"
+ "Connection invalidated"
+ "Failed to connect to service"
+ "Re-establishing connection after interruption"
+ "Registration error: %@"
+ "XPC connection invalidated"
+ "XPC error: %@"
+ "com.apple.batteryintelligence.thermal.reconnect"
+ "com.apple.batteryintelligence.thermalprediction"
+ "com.apple.batteryintelligence.thermalpredictionclient"
+ "com.apple.batteryintelligenced.thermalprediction"
+ "v24@?0@\"BIThermalPredictionOutput\"8@\"NSError\"16"
+ "willHitTLC"

```
