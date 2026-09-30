## DeviceDiscoveryExtension

> `/System/Library/Frameworks/DeviceDiscoveryExtension.framework/DeviceDiscoveryExtension`

```diff

-315.1.0.0.0
-  __TEXT.__text: 0x6734
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x49c
-  __TEXT.__cstring: 0x5e3
+320.33.1.4.0
+  __TEXT.__text: 0x6624
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x4fc
+  __TEXT.__cstring: 0x613
   __TEXT.__const: 0x1a2
   __TEXT.__swift5_typeref: 0x14c
   __TEXT.__oslogstring: 0x1bd

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1b0
-  __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0xc43
+  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__objc_classname: 0xb2
+  __TEXT.__objc_methname: 0xe4a
   __TEXT.__objc_methtype: 0x20f
-  __TEXT.__objc_stubs: 0x820
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__objc_stubs: 0x8c0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x1f8
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0x808
+  __AUTH_CONST.__cfstring: 0x960
+  __AUTH_CONST.__objc_const: 0x8c8
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x388
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  UUID: 923C955E-AFED-3D33-9EAE-72E22A7E4054
-  Functions: 162
-  Symbols:   520
-  CStrings:  417
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 372C3F57-8AFB-3E4A-86CF-7BD440269F50
+  Functions: 170
+  Symbols:   546
+  CStrings:  448
 
Symbols:
+ -[DDDevice setWifiAwareModelName:]
+ -[DDDevice setWifiAwareServiceName:]
+ -[DDDevice setWifiAwareServiceRole:]
+ -[DDDevice setWifiAwareVendorName:]
+ -[DDDevice wifiAwareModelName]
+ -[DDDevice wifiAwareServiceName]
+ -[DDDevice wifiAwareServiceRole]
+ -[DDDevice wifiAwareVendorName]
+ _OBJC_CLASS_$_DADiscoveryConfiguration
+ _OBJC_CLASS_$_DAPropertyCompareString
+ _OBJC_IVAR_$_DDDevice._wifiAwareModelName
+ _OBJC_IVAR_$_DDDevice._wifiAwareServiceName
+ _OBJC_IVAR_$_DDDevice._wifiAwareServiceRole
+ _OBJC_IVAR_$_DDDevice._wifiAwareVendorName
+ ___unnamed_2
+ ___unnamed_7
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DeviceDiscoveryExtension
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_DeviceDiscoveryExtension
+ _objc_msgSend$initWithString:compareOptions:
+ _objc_msgSend$setDiscoveryConfiguration:
+ _objc_msgSend$setWifiAwareModelNameMatch:
+ _objc_msgSend$setWifiAwareServiceName:
+ _objc_msgSend$setWifiAwareServiceType:
+ _swift_coroFrameAlloc
- ___unnamed_1
- ___unnamed_6
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DeviceDiscoveryExtension
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DeviceDiscoveryExtension
- _objc_retain_x24
- _swift_bridgeObjectRelease
CStrings:
+ "'%@'"
+ "'%ld'"
+ "T@\"NSString\",C,N,V_wifiAwareModelName"
+ "T@\"NSString\",C,N,V_wifiAwareServiceName"
+ "T@\"NSString\",C,N,V_wifiAwareVendorName"
+ "Tq,N,V_wifiAwareServiceRole"
+ "Wi-Fi Aware '%@'"
+ "_wifiAwareModelName"
+ "_wifiAwareServiceName"
+ "_wifiAwareServiceRole"
+ "_wifiAwareVendorName"
+ "initWithString:compareOptions:"
+ "setDiscoveryConfiguration:"
+ "setWifiAwareModelName:"
+ "setWifiAwareModelNameMatch:"
+ "setWifiAwareServiceName:"
+ "setWifiAwareServiceRole:"
+ "setWifiAwareServiceType:"
+ "setWifiAwareVendorName:"
+ "wFMn"
+ "wFSn"
+ "wFSt"
+ "wFVn"
+ "wifiAwareModelName"
+ "wifiAwareServiceName"
+ "wifiAwareServiceRole"
+ "wifiAwareVendorName"

```
