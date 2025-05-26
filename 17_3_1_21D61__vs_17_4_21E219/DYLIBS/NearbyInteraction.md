## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-417.0.4.0.0
-  __TEXT.__text: 0x2419c
+420.0.12.0.0
+  __TEXT.__text: 0x24308
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2828
-  __TEXT.__cstring: 0x3275
+  __TEXT.__objc_methlist: 0x2850
+  __TEXT.__cstring: 0x329a
   __TEXT.__const: 0xf9
-  __TEXT.__gcc_except_tab: 0x3900
+  __TEXT.__gcc_except_tab: 0x3918
   __TEXT.__oslogstring: 0x102e
-  __TEXT.__unwind_info: 0x15a0
+  __TEXT.__unwind_info: 0x15a4
   __TEXT.__objc_classname: 0x43f
-  __TEXT.__objc_methname: 0x6691
+  __TEXT.__objc_methname: 0x66b3
   __TEXT.__objc_methtype: 0x1118
   __TEXT.__objc_stubs: 0x41c0
   __DATA_CONST.__got: 0x68

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x46b0
-  __DATA_CONST.__objc_selrefs: 0x1678
+  __DATA_CONST.__objc_const: 0x46e0
+  __DATA_CONST.__objc_selrefs: 0x1680
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__objc_const: 0x1120
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x3860
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x338
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x4a8
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   __DATA.__common: 0xba
   __DATA_DIRTY.__const: 0x8
-  __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 988
-  Symbols:   3752
-  CStrings:  2002
+  Functions: 993
+  Symbols:   3766
+  CStrings:  2005
 
Symbols:
+ +[NIPlatformInfo supportsARKit]
+ -[NIDevicePresenceConfiguration _internalIsCameraAssistanceEnabled]
+ -[NIDevicePresenceConfiguration isCameraAssistanceEnabled]
+ -[NIDevicePresenceConfiguration setCameraAssistanceEnabled:]
+ _OBJC_IVAR_$_NIDevicePresenceConfiguration._cameraAssistanceEnabled
+ __ZNKSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ue170006IPKhS6_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ __ZZ31+[NIPlatformInfo supportsARKit]E13supportsARKit
+ __ZZ31+[NIPlatformInfo supportsARKit]E9onceToken
+ ___18-[NISession pause]_block_invoke.706
+ ___31+[NIPlatformInfo supportsARKit]_block_invoke
+ ___34-[NISession runWithConfiguration:]_block_invoke.699
+ ___34-[NISession runWithConfiguration:]_block_invoke.704
+ ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.651
+ ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.761
+ ___Block_byref_object_copy_.708
+ ___Block_byref_object_dispose_.709
+ ___block_literal_global.1185
+ ___block_literal_global.1189
+ ___block_literal_global.1193
+ ___block_literal_global.1197
+ ___block_literal_global.1294
+ ___block_literal_global.1298
+ ___block_literal_global.1303
+ ___block_literal_global.1308
+ ___block_literal_global.1310
+ ___block_literal_global.20
- __ZNKSt3__16vectorI33UWBSessionInterruptionBookkeepingNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI33UWBSessionInterruptionBookkeepingEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2IPKhLi0EEET_S7_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___18-[NISession pause]_block_invoke.679
- ___34-[NISession runWithConfiguration:]_block_invoke.672
- ___34-[NISession runWithConfiguration:]_block_invoke.677
- ___48-[NISession _initAndConnectToServerWithOptions:]_block_invoke.624
- ___57-[NISession uwbSessionInterruptionReasonEnded:timestamp:]_block_invoke.734
- ___Block_byref_object_copy_.681
- ___Block_byref_object_dispose_.682
- ___block_literal_global.1157
- ___block_literal_global.1161
- ___block_literal_global.1165
- ___block_literal_global.1169
- ___block_literal_global.1266
- ___block_literal_global.1270
- ___block_literal_global.1275
- ___block_literal_global.1280
- ___block_literal_global.1282
CStrings:
+ "4"
+ "<innerboundary: %@, outerboundary: %@, allowedDevices: %s, monitoringOption: %s>, isCameraAssistanceEnabled: %s"
+ "T@\"NSString\",?,R,C"
+ "arkit"
+ "supportsARKit"
- "$"
- "<innerboundary: %@, outerboundary: %@, allowedDevices: %s, monitoringOption: %s>"

```
