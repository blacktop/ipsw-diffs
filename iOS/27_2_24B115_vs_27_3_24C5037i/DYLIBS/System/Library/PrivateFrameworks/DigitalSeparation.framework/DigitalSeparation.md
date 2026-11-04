## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-653.0.10.0.0
-  __TEXT.__text: 0x3a090
-  __TEXT.__objc_methlist: 0x202c
-  __TEXT.__cstring: 0x1927
+653.0.15.0.0
+  __TEXT.__text: 0x3b110
+  __TEXT.__objc_methlist: 0x2144
+  __TEXT.__cstring: 0x195d
   __TEXT.__const: 0xbc8
   __TEXT.__gcc_except_tab: 0xb8c
-  __TEXT.__oslogstring: 0x2844
+  __TEXT.__oslogstring: 0x28d4
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_typeref: 0x51c
   __TEXT.__swift5_capture: 0x1c8

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x90
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x11e8
   __TEXT.__eh_frame: 0xd10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdb8
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
-  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x1630
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__got: 0x588
   __AUTH_CONST.__const: 0xef8
   __AUTH_CONST.__cfstring: 0x1660
-  __AUTH_CONST.__objc_const: 0x4ed8
+  __AUTH_CONST.__objc_const: 0x5360
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x908
-  __AUTH.__objc_data: 0xd8
-  __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x194
-  __DATA.__data: 0x7b0
+  __AUTH_CONST.__auth_got: 0x930
+  __AUTH.__objc_data: 0x148
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x198
+  __DATA.__data: 0x880
   __DATA_DIRTY.__objc_data: 0x938
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0xb8

   - /System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/RelevanceServices.framework/RelevanceServices
   - /System/Library/PrivateFrameworks/RemotePairingDevice.framework/RemotePairingDevice
   - /System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices
   - /System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1275
-  Symbols:   1843
-  CStrings:  477
+  Functions: 1298
+  Symbols:   1875
+  CStrings:  480
 
Symbols:
+ -[DSAppSharing isThirdPartyApp:]
+ -[DSXPCSharingPermissions contactProvider]
+ -[DSXPCSharingPermissions initWithSharing:withDSMe:contactProvider:]
+ -[DSXPCSharingPermissions setContactProvider:]
+ GCC_except_table10
+ GCC_except_table18
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table40
+ _NRDevicePropertyMarketingProductName
+ _NRDevicePropertyName
+ _NRDevicePropertyPairedDate
+ _NRDevicePropertySerialNumber
+ _OBJC_CLASS_$_DSSiriRecapViewModel
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$_DSXPCSharingPermissions._contactProvider
+ _OBJC_METACLASS_$_DSSiriRecapViewModel
+ __DATA_DSSiriRecapViewModel
+ __INSTANCE_METHODS_DSSiriRecapViewModel
+ __IVARS_DSSiriRecapViewModel
+ __METACLASS_DATA_DSSiriRecapViewModel
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSContactProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSSiriRecapInterfacing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSContactProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSSiriRecapInterfacing
+ __OBJC_$_PROTOCOL_REFS_DSContactProviding
+ __OBJC_CLASS_PROTOCOLS_$_DSContactProvider
+ __OBJC_LABEL_PROTOCOL_$_DSContactProviding
+ __OBJC_LABEL_PROTOCOL_$_DSSiriRecapInterfacing
+ __OBJC_PROTOCOL_$_DSContactProviding
+ __OBJC_PROTOCOL_$_DSSiriRecapInterfacing
+ __PROPERTIES_DSSiriRecapViewModel
+ __PROTOCOLS_DSSiriRecapViewModel
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s48l8s32l8s40l8
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_DigitalSeparation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_DigitalSeparation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_DigitalSeparation
- -[DSXPCSharingPermissions setDSMe:]
- -[DSXPCSharingPermissions setSharing:]
- GCC_except_table17
- GCC_except_table28
- GCC_except_table32
- GCC_except_table39
- GCC_except_table9
- ___35-[DSXPCSharingPermissions setDSMe:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
CStrings:
+ "DigitalSeparation/DSSiriRecapViewModel.swift"
+ "Error determining whether %@ is a third party app: %@"
+ "Not resetting file access for %@ because it is a first party app and doing so would cause a crash"
```
