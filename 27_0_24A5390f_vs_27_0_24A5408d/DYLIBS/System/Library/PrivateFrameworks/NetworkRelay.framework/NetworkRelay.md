## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-914.0.22.0.1
-  __TEXT.__text: 0x79568
-  __TEXT.__objc_methlist: 0x1f64
+914.0.34.0.4
+  __TEXT.__text: 0x7b824
+  __TEXT.__objc_methlist: 0x1fc4
   __TEXT.__const: 0x240
   __TEXT.__gcc_except_tab: 0xb60
-  __TEXT.__cstring: 0x10178
+  __TEXT.__cstring: 0x104d4
   __TEXT.__oslogstring: 0x13a9
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__const: 0xd70
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b8
+  __DATA_CONST.__objc_selrefs: 0x10e0
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x1f8
   __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x5140
-  __AUTH_CONST.__objc_const: 0x5170
+  __AUTH_CONST.__cfstring: 0x51e0
+  __AUTH_CONST.__objc_const: 0x5200
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a0
-  __DATA.__objc_ivar: 0x554
+  __DATA.__objc_ivar: 0x560
   __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x268
+  __DATA.__bss: 0x270
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1048
-  Symbols:   2647
-  CStrings:  1974
+  Functions: 1064
+  Symbols:   2673
+  CStrings:  1997
 
Symbols:
+ -[NRDeviceInfo deviceType]
+ -[NRDeviceInfo isEnabled]
+ -[NRDeviceInfo isRegistered]
+ -[NRDeviceInfo setDeviceType:]
+ -[NRDeviceInfo setIsEnabled:]
+ -[NRDeviceInfo setIsRegistered:]
+ -[NRDeviceManager copyAllDevicesWithQueue:completionBlock:]
+ -[NRDeviceManager unregisterMesh:queue:completionBlock:]
+ GCC_except_table456
+ GCC_except_table467
+ GCC_except_table703
+ GCC_except_table711
+ GCC_except_table716
+ GCC_except_table720
+ GCC_except_table730
+ GCC_except_table734
+ GCC_except_table738
+ GCC_except_table742
+ GCC_except_table765
+ GCC_except_table768
+ GCC_except_table772
+ GCC_except_table781
+ GCC_except_table783
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table790
+ GCC_except_table846
+ GCC_except_table848
+ GCC_except_table863
+ _NRDeviceManagerErrorMeshIdentifierKey
+ _OBJC_IVAR_$_NRDeviceInfo._deviceType
+ _OBJC_IVAR_$_NRDeviceInfo._isEnabled
+ _OBJC_IVAR_$_NRDeviceInfo._isRegistered
+ ___34-[NRDeviceManager unregisterMesh:]_block_invoke
+ ___56-[NRDeviceManager unregisterMesh:queue:completionBlock:]_block_invoke
+ ___76-[NRDeviceManager registerMesh:operationalProperties:queue:completionBlock:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v32?0q8"NSString"16"NSString"24ls32l8s40l8
+ ___nrXPCCopyAllDevices_block_invoke
+ ___nrXPCRegisterMesh_block_invoke_2
+ ___nrXPCSendAsyncMeshResult_block_invoke
+ _nrXPCCopyAllDevices
+ _nrXPCEntitlementMeshMonitor_block_invoke_2.sNRXPCConnection
+ _nrXPCKeyAllDevices
+ _nrXPCRegisterMesh
+ _nrXPCUnregisterMesh
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$setIsEnabled:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$unregisterMesh:queue:completionBlock:
- GCC_except_table450
- GCC_except_table461
- GCC_except_table697
- GCC_except_table705
- GCC_except_table710
- GCC_except_table714
- GCC_except_table718
- GCC_except_table728
- GCC_except_table732
- GCC_except_table736
- GCC_except_table759
- GCC_except_table762
- GCC_except_table766
- GCC_except_table771
- GCC_except_table773
- GCC_except_table775
- GCC_except_table782
- GCC_except_table784
- GCC_except_table835
- GCC_except_table837
- GCC_except_table852
- _nrXPCEntitlementMeshMonitor_block_invoke.sNRXPCConnection
- _nrXPCKeyPersistentMesh
- _nrXPCSetPersistentMesh
CStrings:
+ " type:%@ %sregistered %sabled"
+ "%s called with null meshIdentifier"
+ "%s%.30s:%-4d Failed to register mesh %@: %@"
+ "%s%.30s:%-4d Failed to unregister mesh %@: %@"
+ "%s%.30s:%-4d Registered mesh %@"
+ "%s%.30s:%-4d Unregistered mesh %@"
+ "-[NRDeviceManager copyAllDevicesWithQueue:completionBlock:]"
+ "-[NRDeviceManager registerMesh:operationalProperties:queue:completionBlock:]_block_invoke"
+ "-[NRDeviceManager unregisterMesh:]_block_invoke"
+ "-[NRDeviceManager unregisterMesh:queue:completionBlock:]"
+ "-[NRDeviceManager unregisterMesh:queue:completionBlock:]_block_invoke"
+ "AllDevices"
+ "CopyAllDevices"
+ "Failed to deserialize all devices: %@"
+ "Missing all devices data in XPC response"
+ "NRDeviceManagerErrorMeshIdentifierKey"
+ "RegisterMesh"
+ "UnregisterMesh"
+ "isEnabled"
+ "nrXPCCopyAllDevices"
+ "nrXPCCopyAllDevices_block_invoke"
+ "nrXPCRegisterMesh"
+ "nrXPCSendAsyncMeshResult"
+ "nrXPCSendAsyncMeshResult_block_invoke"
+ "nrXPCUnregisterMesh"
+ "v32@?0q8@\"NSString\"16@\"NSString\"24"
- "PersistentMesh"
- "SetPersistentMesh"
- "nrXPCSetPersistentMesh"
```
