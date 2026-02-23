## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`

```diff

-1147.100.12.0.0
-  __TEXT.__text: 0x62ff0
+1147.100.17.0.0
+  __TEXT.__text: 0x634a0
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x2e94
+  __TEXT.__objc_methlist: 0x2eb4
   __TEXT.__const: 0x378
   __TEXT.__cstring: 0x5d62
   __TEXT.__oslogstring: 0xbb7d
-  __TEXT.__gcc_except_tab: 0x964
+  __TEXT.__gcc_except_tab: 0x97c
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0xef0
+  __TEXT.__unwind_info: 0xf00
   __TEXT.__objc_classname: 0x474
-  __TEXT.__objc_methname: 0x8805
+  __TEXT.__objc_methname: 0x8883
   __TEXT.__objc_methtype: 0xff9
-  __TEXT.__objc_stubs: 0x5d40
+  __TEXT.__objc_stubs: 0x5de0
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__const: 0xea8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e60
+  __DATA_CONST.__objc_selrefs: 0x1e78
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0xab8
-  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x4460
-  __AUTH_CONST.__objc_const: 0x4c50
+  __AUTH_CONST.__objc_const: 0x4c80
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x45c
+  __DATA.__objc_ivar: 0x460
   __DATA.__data: 0x5e5
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x130

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 037D2719-06EE-3C0B-8401-80311AF402ED
-  Functions: 1881
-  Symbols:   6876
-  CStrings:  3917
+  UUID: DEAAF290-DE69-3957-A9D5-5A76821065F0
+  Functions: 1886
+  Symbols:   6895
+  CStrings:  3922
 
Symbols:
+ -[ACCTransportIOAccessoryManager registeredForHIDDevice]
+ -[ACCTransportIOAccessoryManager setRegisteredForHIDDevice:]
+ -[ACCTransportIOAccessorySharedManager _shouldAllowDeviceSettings:]
+ -[ACCTransportIOAccessorySharedManager _shouldAllowDeviceSettings:].cold.1
+ GCC_except_table102
+ GCC_except_table106
+ _OBJC_IVAR_$_ACCTransportIOAccessoryManager._registeredForHIDDevice
+ ___67-[ACCTransportIOAccessorySharedManager _shouldAllowDeviceSettings:]_block_invoke
+ ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.138
+ ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.139
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.144
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.144.cold.1
+ ___89-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataFinishedForEndpointUUID:]_block_invoke.165
+ ___block_literal_global.114
+ __shouldAllowDeviceSettings:.allowedAccessories
+ __shouldAllowDeviceSettings:.onceToken
+ _objc_msgSend$_shouldAllowDeviceSettings:
+ _objc_msgSend$idbusHIDDeviceIterator
+ _objc_msgSend$registeredForHIDDevice
+ _objc_msgSend$setIdbusHIDDeviceIterator:
+ _objc_msgSend$setRegisteredForHIDDevice:
- GCC_except_table100
- GCC_except_table104
- ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.133
- ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.134
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.139
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.139.cold.1
- ___89-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataFinishedForEndpointUUID:]_block_invoke.160
CStrings:
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "TB,V_registeredForHIDDevice"
+ "TI,V_idbusHIDDeviceIterator"
+ "T^{IONotificationPort=},V_ioAccessoryIDBusHIDDevicePortRef"
+ "_registeredForHIDDevice"
+ "_shouldAllowDeviceSettings:"
+ "registeredForHIDDevice"
+ "setRegisteredForHIDDevice:"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "TI,N,V_idbusHIDDeviceIterator"
- "T^{IONotificationPort=},N,V_ioAccessoryIDBusHIDDevicePortRef"

```
