## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.0.4.0.0
-  __TEXT.__text: 0x62858
+548.0.6.0.0
+  __TEXT.__text: 0x62e5c
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x856c
+  __TEXT.__objc_methlist: 0x85bc
   __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0xd6c
-  __TEXT.__cstring: 0x4fcb
-  __TEXT.__oslogstring: 0x6d2c
-  __TEXT.__unwind_info: 0x16f0
-  __TEXT.__objc_classname: 0xd39
-  __TEXT.__objc_methname: 0xf74d
-  __TEXT.__objc_methtype: 0x29d8
-  __TEXT.__objc_stubs: 0x9940
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x1798
+  __TEXT.__gcc_except_tab: 0xd9c
+  __TEXT.__cstring: 0x4ffb
+  __TEXT.__oslogstring: 0x6d76
+  __TEXT.__unwind_info: 0x1710
+  __TEXT.__objc_classname: 0xd38
+  __TEXT.__objc_methname: 0xf7a0
+  __TEXT.__objc_methtype: 0x29eb
+  __TEXT.__objc_stubs: 0x9980
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x1800
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b20
+  __DATA_CONST.__objc_selrefs: 0x3b38
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH_CONST.__const: 0x518
-  __AUTH_CONST.__cfstring: 0x6c60
-  __AUTH_CONST.__objc_const: 0xcf80
+  __AUTH_CONST.__const: 0x538
+  __AUTH_CONST.__cfstring: 0x6d20
+  __AUTH_CONST.__objc_const: 0xcfc8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x21c0
-  __DATA.__objc_ivar: 0x8a8
+  __DATA.__objc_ivar: 0x8ac
   __DATA.__data: 0xb50
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C694CB3E-0487-3001-BC80-22712AB3ECF1
-  Functions: 2788
-  Symbols:   9043
-  CStrings:  5626
+  UUID: B7506CBA-BC89-3346-89F3-10A34FE49287
+  Functions: 2799
+  Symbols:   9073
+  CStrings:  5642
 
Symbols:
+ -[TVRCHMServiceWrapper connectionState]
+ -[TVRCMatchPointDeviceImpl connectionState]
+ -[TVRCRPCompanionLinkClientWrapper connectionState]
+ -[TVRCRPCompanionLinkClientWrapper sendTouchEvent:].cold.2
+ -[TVRCRapportDeviceImpl connectionState]
+ -[TVRCRapportDeviceQuery setSystemMonitor:]
+ -[TVRCRapportDeviceQuery systemMonitor]
+ GCC_except_table30
+ GCC_except_table44
+ GCC_except_table69
+ GCC_except_table70
+ _OBJC_CLASS_$_CUSystemMonitor
+ _OBJC_IVAR_$_TVRCHMServiceWrapper._connectionState
+ _OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._connectionState
+ _OBJC_IVAR_$_TVRCRapportDeviceQuery._systemMonitor
+ _OUTLINED_FUNCTION_9
+ _TVRCDeviceConnectionStateDescription
+ ___30-[TVRCRapportDeviceQuery init]_block_invoke
+ ___30-[TVRCRapportDeviceQuery init]_block_invoke.60
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.67
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.68
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.69.cold.1
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.74
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.77
+ ___31-[TVRCRapportDeviceQuery start]_block_invoke.77.cold.1
+ ___38-[TVRCRapportDeviceQuery _deviceLost:]_block_invoke.89
+ ___39-[TVRCRapportDeviceQuery _deviceFound:]_block_invoke.86
+ ___block_descriptor_48_e8_32s40w_e31_v16?0"RPCompanionLinkDevice"8lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.76
+ ___block_literal_global.80
+ _objc_msgSend$screenState
+ _objc_msgSend$setScreenStateChangedHandler:
+ _objc_msgSend$systemMonitor
- -[TVRCRapportDeviceImpl isConnected]
- GCC_except_table65
- _OBJC_IVAR_$_TVRCRapportDeviceImpl._isConnected
- _OBJC_IVAR_$_TVRXDevice._connectionState
- ___31-[TVRCRapportDeviceQuery start]_block_invoke.62
- ___31-[TVRCRapportDeviceQuery start]_block_invoke.65
- ___31-[TVRCRapportDeviceQuery start]_block_invoke.66.cold.1
- ___31-[TVRCRapportDeviceQuery start]_block_invoke.71
- ___31-[TVRCRapportDeviceQuery start]_block_invoke.72.cold.1
- ___38-[TVRCRapportDeviceQuery _deviceLost:]_block_invoke.84
- ___39-[TVRCRapportDeviceQuery _deviceFound:]_block_invoke.81
- ___block_literal_global.75
- _objc_msgSend$isConnected
CStrings:
+ "7"
+ "<TVRXDevice %p> device is not in the connected state, ignoring notification. Current state is: %{public}@"
+ "@\"CUSystemMonitor\""
+ "ActiveDimmed"
+ "ActiveOn"
+ "CUScreenState: %{public}@"
+ "Connecting"
+ "Device is not connected over Infra and screen is not active, ignoring the device lost notification - device: %{public}@"
+ "Device was %{public}@ while lost, sending TVRCErrorCodeDeviceNotFoundError"
+ "InactiveOn"
+ "Off"
+ "Screen state monitor activated"
+ "T@\"CUSystemMonitor\",&,N,V_systemMonitor"
+ "_systemMonitor"
+ "screenState"
+ "setScreenStateChangedHandler:"
+ "setSystemMonitor:"
+ "systemMonitor"
- "'"
- "3"
- "<TVRXDevice %p> device is not in the connecting state, ignoring authentication challenge. Current state is %ld"
- "<TVRXDevice %p> device is not in the connecting state, ignoring notification. Current state is %ld"
- "Device was connected while lost, sending TVRCErrorCodeDeviceNotFoundError"
- "TB,R,N,V_isConnected"
- "_isConnected"
- "a"
- "isConnected"

```
