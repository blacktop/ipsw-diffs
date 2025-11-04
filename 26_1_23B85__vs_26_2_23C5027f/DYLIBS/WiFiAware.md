## WiFiAware

> `/System/Library/Frameworks/WiFiAware.framework/WiFiAware`

```diff

-835.7.0.0.0
-  __TEXT.__text: 0x2ce78
-  __TEXT.__auth_stubs: 0x1170
+835.8.0.0.0
+  __TEXT.__text: 0x2db44
+  __TEXT.__auth_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x17c
-  __TEXT.__const: 0x58f0
-  __TEXT.__cstring: 0xb95
+  __TEXT.__const: 0x5a40
+  __TEXT.__cstring: 0xce5
+  __TEXT.__swift5_typeref: 0x12f0
+  __TEXT.__constg_swiftt: 0x1160
+  __TEXT.__swift5_fieldmd: 0x1024
+  __TEXT.__swift5_reflstr: 0x5ec
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_proto: 0x588
+  __TEXT.__swift5_types: 0x1d4
   __TEXT.__oslogstring: 0x3a
-  __TEXT.__swift5_typeref: 0x12ba
-  __TEXT.__swift5_reflstr: 0x5cc
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__constg_swiftt: 0x10ec
-  __TEXT.__swift5_fieldmd: 0xfec
-  __TEXT.__swift5_proto: 0x578
-  __TEXT.__swift5_types: 0x1cc
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0xec
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1080
-  __TEXT.__eh_frame: 0x1234
+  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__eh_frame: 0x127c
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0x3f4
   __TEXT.__objc_methtype: 0xde
-  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x8b8
-  __AUTH_CONST.__const: 0x2e88
+  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__const: 0x2fe8
   __AUTH_CONST.__objc_const: 0x590
   __AUTH.__objc_data: 0x128
   __AUTH.__data: 0x9a0
-  __DATA.__data: 0x1128
-  __DATA.__common: 0xb8
-  __DATA.__bss: 0xaf00
+  __DATA.__data: 0x1158
+  __DATA.__bss: 0xb100
+  __DATA.__common: 0xd0
   __DATA_DIRTY.__data: 0x150
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 39971B49-C2CD-346F-BBE2-91120E2298EB
-  Functions: 1542
-  Symbols:   737
-  CStrings:  170
+  UUID: D69D0657-46B6-3EF5-8BF3-F08486BF3489
+  Functions: 1558
+  Symbols:   746
+  CStrings:  177
 
Symbols:
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _associated conformance 9WiFiAware0abC12EntitlementsV0abC10CapabilityOSHAASQ
+ _swift_getForeignTypeMetadata
+ _symbolic SaySSG
+ _symbolic _____ 9WiFiAware0abC12EntitlementsV
+ _symbolic _____ 9WiFiAware0abC12EntitlementsV0abC10CapabilityO
+ _symbolic _____ySbG s23_ContiguousArrayStorageC
+ _symbolic _____y_____GSg s9UnmanagedV So10CFErrorRefa
CStrings:
+ " needed for this operation."
+ "Crashing: App is trying to use Wi-Fi Aware, but is missing one or more capabilities: "
+ "Crashing: App is trying to use Wi-Fi Aware, but unable to verify App has the Wi-Fi Aware capabilities: "
+ "Publish"
+ "Subscribe"
+ "WiFiAware/Entitlements.swift"
+ "com.apple.developer.wifi-aware"

```
