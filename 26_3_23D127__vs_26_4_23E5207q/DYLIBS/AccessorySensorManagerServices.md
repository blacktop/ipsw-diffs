## AccessorySensorManagerServices

> `/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`

```diff

-10.12.3.0.0
-  __TEXT.__text: 0x10cc
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_methlist: 0x1bc
+11.27.0.0.1
+  __TEXT.__text: 0x3398
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_methlist: 0x454
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x42e
-  __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0x3bb
-  __TEXT.__objc_methtype: 0x1b8
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x118d
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_classname: 0xcb
+  __TEXT.__objc_methname: 0xa36
+  __TEXT.__objc_methtype: 0x303
+  __TEXT.__objc_stubs: 0x480
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x118
-  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x3b0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x1f0
-  __DATA.__bss: 0x1c
+  __AUTH_CONST.__objc_const: 0xa70
+  __DATA.__objc_ivar: 0x44
+  __DATA.__data: 0x260
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AccessorySensorManagerDefines_Private.framework/AccessorySensorManagerDefines_Private
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 505A9196-6145-3924-8712-5DCD300F3AD7
-  Functions: 52
-  Symbols:   230
-  CStrings:  100
+  UUID: 7B21F9BB-73B6-3BA4-90EA-8B899A639855
+  Functions: 146
+  Symbols:   493
+  CStrings:  199
 
Symbols:
+ +[ASMInertialOdometryServices supportsSecureCoding]
+ +[ASMPeripheralInertialOdometryConfig supportsSecureCoding]
+ -[ASMInertialOdometryServices .cxx_destruct]
+ -[ASMInertialOdometryServices _clearInertialOdometryAvailabilityMap]
+ -[ASMInertialOdometryServices _ensureXPCStarted]
+ -[ASMInertialOdometryServices _interrupted]
+ -[ASMInertialOdometryServices _interrupted].cold.1
+ -[ASMInertialOdometryServices _invalidated]
+ -[ASMInertialOdometryServices _invalidated].cold.1
+ -[ASMInertialOdometryServices _invalidated].cold.2
+ -[ASMInertialOdometryServices _recordInertialOdometryAvailability:forPeripheral:]
+ -[ASMInertialOdometryServices clientID]
+ -[ASMInertialOdometryServices description]
+ -[ASMInertialOdometryServices dispatchQueue]
+ -[ASMInertialOdometryServices encodeWithCoder:]
+ -[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]
+ -[ASMInertialOdometryServices inertialOdometryAvailabilityHandler]
+ -[ASMInertialOdometryServices inertialOdometryDataReceived:]
+ -[ASMInertialOdometryServices inertialOdometryDataReceivedHandler]
+ -[ASMInertialOdometryServices initWithCoder:]
+ -[ASMInertialOdometryServices init]
+ -[ASMInertialOdometryServices interruptionHandler]
+ -[ASMInertialOdometryServices invalidate]
+ -[ASMInertialOdometryServices invalidationHandler]
+ -[ASMInertialOdometryServices isInertialOdometryAvailableForPeripheral:]
+ -[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]
+ -[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]
+ -[ASMInertialOdometryServices setClientID:]
+ -[ASMInertialOdometryServices setDispatchQueue:]
+ -[ASMInertialOdometryServices setInertialOdometryAvailabilityHandler:]
+ -[ASMInertialOdometryServices setInertialOdometryDataReceivedHandler:]
+ -[ASMInertialOdometryServices setInterruptionHandler:]
+ -[ASMInertialOdometryServices setInvalidationHandler:]
+ -[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]
+ -[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]
+ -[ASMInertialOdometryServices subscribeToInertialOdometryData]
+ -[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]
+ -[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]
+ -[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]
+ -[ASMPeripheralConfig copyWithZone:]
+ -[ASMPeripheralInertialOdometryConfig description]
+ -[ASMPeripheralInertialOdometryConfig encodeWithCoder:]
+ -[ASMPeripheralInertialOdometryConfig initWithCoder:]
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table30
+ _OBJC_CLASS_$_ASMInertialOdometryServices
+ _OBJC_CLASS_$_ASMPeripheralInertialOdometryConfig
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_ASMInertialOdometryServices._clientID
+ _OBJC_IVAR_$_ASMInertialOdometryServices._dispatchQueue
+ _OBJC_IVAR_$_ASMInertialOdometryServices._inertialOdometryAvailabilityHandler
+ _OBJC_IVAR_$_ASMInertialOdometryServices._inertialOdometryAvailabilityMap
+ _OBJC_IVAR_$_ASMInertialOdometryServices._inertialOdometryDataReceivedHandler
+ _OBJC_IVAR_$_ASMInertialOdometryServices._interruptionHandler
+ _OBJC_IVAR_$_ASMInertialOdometryServices._invalidateCalled
+ _OBJC_IVAR_$_ASMInertialOdometryServices._invalidateDone
+ _OBJC_IVAR_$_ASMInertialOdometryServices._invalidationHandler
+ _OBJC_IVAR_$_ASMInertialOdometryServices._xpcCnx
+ _OBJC_METACLASS_$_ASMInertialOdometryServices
+ _OBJC_METACLASS_$_ASMPeripheralInertialOdometryConfig
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CLASS_METHODS_ASMInertialOdometryServices
+ __OBJC_$_CLASS_METHODS_ASMPeripheralInertialOdometryConfig
+ __OBJC_$_CLASS_PROP_LIST_ASMInertialOdometryServices
+ __OBJC_$_CLASS_PROP_LIST_ASMPeripheralInertialOdometryConfig
+ __OBJC_$_INSTANCE_METHODS_ASMInertialOdometryServices
+ __OBJC_$_INSTANCE_METHODS_ASMPeripheralInertialOdometryConfig
+ __OBJC_$_INSTANCE_VARIABLES_ASMInertialOdometryServices
+ __OBJC_$_PROP_LIST_ASMInertialOdometryServices
+ __OBJC_CLASS_PROTOCOLS_$_ASMInertialOdometryServices
+ __OBJC_CLASS_PROTOCOLS_$_ASMPeripheralInertialOdometryConfig
+ __OBJC_CLASS_RO_$_ASMInertialOdometryServices
+ __OBJC_CLASS_RO_$_ASMPeripheralInertialOdometryConfig
+ __OBJC_METACLASS_RO_$_ASMInertialOdometryServices
+ __OBJC_METACLASS_RO_$_ASMPeripheralInertialOdometryConfig
+ __Unwind_Resume
+ ___41-[ASMInertialOdometryServices invalidate]_block_invoke
+ ___41-[ASMInertialOdometryServices invalidate]_block_invoke.cold.1
+ ___48-[ASMInertialOdometryServices _ensureXPCStarted]_block_invoke
+ ___48-[ASMInertialOdometryServices _ensureXPCStarted]_block_invoke_2
+ ___60-[ASMInertialOdometryServices inertialOdometryDataReceived:]_block_invoke
+ ___60-[ASMInertialOdometryServices inertialOdometryDataReceived:]_block_invoke.cold.1
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.1
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.2
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke.cold.3
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2
+ ___62-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2.cold.1
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.1
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.2
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke.cold.3
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2
+ ___66-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2.cold.1
+ ___81-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]_block_invoke
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.1
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.2
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.3
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2
+ ___90-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2.cold.1
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.1
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.2
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.3
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2
+ ___91-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2.cold.1
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.1
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.2
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke.cold.3
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2
+ ___94-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2.cold.1
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke.cold.1
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke.cold.2
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke.cold.3
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke_2
+ ___95-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke_2.cold.1
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.1
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.2
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke.cold.3
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2
+ ___95-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2.cold.1
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke.cold.1
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke.cold.2
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke.cold.3
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke_2
+ ___96-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke_2.cold.1
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.48
+ ___block_literal_global.53
+ ___block_literal_global.57
+ ___block_literal_global.64
+ ___block_literal_global.69
+ ___block_literal_global.73
+ ___block_literal_global.77
+ ___objc_personality_v0
+ _gLogCategory_ASMInertialOdometryServices
+ _objc_alloc_init
+ _objc_msgSend$_clearInertialOdometryAvailabilityMap
+ _objc_msgSend$_recordInertialOdometryAvailability:forPeripheral:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$intValue
+ _objc_msgSend$isInertialOdometryAvailableForPeripheral:
+ _objc_msgSend$modifyInertialOdometryWithBtAddress:configuration:btAddress:completion:
+ _objc_msgSend$modifyInertialOdometryWithIdentifier:configuration:identifier:completion:
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:
+ _objc_msgSend$subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:
+ _objc_msgSend$subscribeToInertialOdometryData:
+ _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:
+ _objc_msgSend$unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:
+ _objc_msgSend$unsubscribeFromInertialOdometryData:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x3
+ _objc_sync_enter
+ _objc_sync_exit
- _ASMErrorDomain
- _ASMErrorF
- _ASMXPCGetNextClientID.cold.1
- _ASMXPCGetNextClientID.sNext
- _ASMXPCGetNextClientID.sOnce
- _ASMXPCGetNextConnectionID
- _ASMXPCGetNextConnectionID.cold.1
- _ASMXPCGetNextConnectionID.sNext
- _ASMXPCGetNextConnectionID.sOnce
- _NSErrorV
- _RandomBytes
- ___ASMXPCGetNextClientID_block_invoke
- ___ASMXPCGetNextConnectionID_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_literal_global.3
- _dispatch_once
- _objc_claimAutoreleasedReturnValue
- _objc_release_x23
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x8
CStrings:
+ "### modifyPeripheralInertialOdometryWithBtAddress failed to start XPC"
+ "### modifyPeripheralInertialOdometryWithBtAddress no XPC"
+ "### modifyPeripheralInertialOdometryWithIdentifier failed to start XPC"
+ "### modifyPeripheralInertialOdometryWithIdentifier no XPC"
+ "### subscribeToInertialOdometryAvailabilityChangeWithBtAddress failed to start XPC"
+ "### subscribeToInertialOdometryAvailabilityChangeWithBtAddress no XPC"
+ "### subscribeToInertialOdometryAvailabilityChangeWithIdentifier failed to start XPC"
+ "### subscribeToInertialOdometryAvailabilityChangeWithIdentifier no XPC"
+ "### subscribeToInertialOdometryData failed to start XPC"
+ "### subscribeToInertialOdometryData no XPC"
+ "### unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress failed to start XPC"
+ "### unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress no XPC"
+ "### unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier failed to start XPC"
+ "### unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier no XPC"
+ "### unsubscribeFromInertialOdometryData failed to start XPC"
+ "### unsubscribeFromInertialOdometryData no XPC"
+ "-[ASMInertialOdometryServices _interrupted]"
+ "-[ASMInertialOdometryServices _invalidated]"
+ "-[ASMInertialOdometryServices inertialOdometryAvailabilityChanged:forPeripheral:]_block_invoke"
+ "-[ASMInertialOdometryServices inertialOdometryDataReceived:]_block_invoke"
+ "-[ASMInertialOdometryServices invalidate]_block_invoke"
+ "-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke"
+ "-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithBtAddress:config:completion:]_block_invoke_2"
+ "-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke"
+ "-[ASMInertialOdometryServices modifyPeripheralInertialOdometryWithIdentifier:config:completion:]_block_invoke_2"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke"
+ "-[ASMInertialOdometryServices subscribeToInertialOdometryData]_block_invoke_2"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:]_block_invoke_2"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:]_block_invoke_2"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke"
+ "-[ASMInertialOdometryServices unsubscribeFromInertialOdometryData]_block_invoke_2"
+ "?"
+ "@\"NSMutableDictionary\""
+ "@24@0:8^{_NSZone=}16"
+ "ASMInertialOdometryServices"
+ "ASMInertialOdometryServices, CID 0x%X"
+ "ASMPeripheralInertialOdometryConfig"
+ "Client received inertial odometry data - %@"
+ "Inertial odometry availability has been updated to %s for %@"
+ "No"
+ "T@?,C,N,V_inertialOdometryAvailabilityHandler"
+ "T@?,C,N,V_inertialOdometryDataReceivedHandler"
+ "Unknown"
+ "Yes"
+ "_clearInertialOdometryAvailabilityMap"
+ "_inertialOdometryAvailabilityHandler"
+ "_inertialOdometryAvailabilityMap"
+ "_inertialOdometryDataReceivedHandler"
+ "_recordInertialOdometryAvailability:forPeripheral:"
+ "allocWithZone:"
+ "c24@0:8@16"
+ "copyWithZone:"
+ "inertialOdometryAvailabilityChanged:forPeripheral:"
+ "inertialOdometryAvailabilityHandler"
+ "inertialOdometryDataReceived:"
+ "inertialOdometryDataReceivedHandler"
+ "inom"
+ "intValue"
+ "isInertialOdometryAvailableForPeripheral:"
+ "modifyInertialOdometryWithBtAddress:configuration:btAddress:completion:"
+ "modifyInertialOdometryWithIdentifier:configuration:identifier:completion:"
+ "modifyPeripheralInertialOdometryWithBtAddress:config:completion:"
+ "modifyPeripheralInertialOdometryWithIdentifier:config:completion:"
+ "modifying inertial odometry stream"
+ "numberWithChar:"
+ "objectForKeyedSubscript:"
+ "removeAllObjects"
+ "setInertialOdometryAvailabilityHandler:"
+ "setInertialOdometryDataReceivedHandler:"
+ "setObject:forKeyedSubscript:"
+ "subscribeToInertialOdometryAvailabilityChangeWithBtAddress:"
+ "subscribeToInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:"
+ "subscribeToInertialOdometryAvailabilityChangeWithIdentifier:"
+ "subscribeToInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:"
+ "subscribeToInertialOdometryData"
+ "subscribeToInertialOdometryData:"
+ "subscribing to Asen inertial odometry data"
+ "subscribing to inertial odometry availability"
+ "unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:"
+ "unsubscribeFromInertialOdometryAvailabilityChangeWithBtAddress:forPeripheral:"
+ "unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:"
+ "unsubscribeFromInertialOdometryAvailabilityChangeWithIdentifier:forPeripheral:"
+ "unsubscribeFromInertialOdometryData"
+ "unsubscribeFromInertialOdometryData:"
+ "unsubscribing from Asen inertial odometry data"
+ "unsubscribing from inertial odometry availability"
+ "v24@0:8@\"ASMInertialOdometryServices\"16"
+ "v24@0:8@\"NSData\"16"
+ "v28@0:8c16@\"NSString\"20"
+ "v28@0:8c16@20"
+ "v32@0:8@\"ASMInertialOdometryServices\"16@\"NSString\"24"
+ "v32@0:8@16@24"
+ "v48@0:8@\"ASMInertialOdometryServices\"16@\"ASMPeripheralInertialOdometryConfig\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "ASMErrorDomain"

```
