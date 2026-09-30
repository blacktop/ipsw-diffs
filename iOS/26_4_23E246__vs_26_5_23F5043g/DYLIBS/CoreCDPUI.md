## CoreCDPUI

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

-416.475.12.0.0
-  __TEXT.__text: 0x7c728
-  __TEXT.__auth_stubs: 0x20d0
-  __TEXT.__objc_methlist: 0x4618
-  __TEXT.__const: 0x40b4
+416.575.3.0.0
+  __TEXT.__text: 0x7d820
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__objc_methlist: 0x4630
+  __TEXT.__const: 0x4164
   __TEXT.__cstring: 0x5862
-  __TEXT.__oslogstring: 0x3912
+  __TEXT.__oslogstring: 0x3aa2
   __TEXT.__gcc_except_tab: 0xc3c
   __TEXT.__dlopen_cstrs: 0x28e
-  __TEXT.__constg_swiftt: 0x1748
-  __TEXT.__swift5_typeref: 0x8e9a
+  __TEXT.__constg_swiftt: 0x17dc
+  __TEXT.__swift5_typeref: 0x8ecc
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xc72
-  __TEXT.__swift5_fieldmd: 0xcd0
+  __TEXT.__swift5_reflstr: 0xcd2
+  __TEXT.__swift5_fieldmd: 0xd2c
   __TEXT.__swift5_assocty: 0x3c8
-  __TEXT.__swift5_proto: 0x110
-  __TEXT.__swift5_types: 0xe8
+  __TEXT.__swift5_proto: 0x114
+  __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_capture: 0x548
-  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x1e68
+  __TEXT.__unwind_info: 0x1ea0
   __TEXT.__eh_frame: 0x420
-  __TEXT.__objc_classname: 0x10a8
-  __TEXT.__objc_methname: 0xcfb3
-  __TEXT.__objc_methtype: 0x3115
-  __TEXT.__objc_stubs: 0x9340
-  __DATA_CONST.__got: 0xd88
+  __TEXT.__objc_classname: 0x10e8
+  __TEXT.__objc_methname: 0xd053
+  __TEXT.__objc_methtype: 0x3135
+  __TEXT.__objc_stubs: 0x9380
+  __DATA_CONST.__got: 0xd90
   __DATA_CONST.__const: 0x1300
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3108
+  __DATA_CONST.__objc_selrefs: 0x3120
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x140
-  __AUTH_CONST.__auth_got: 0x1078
-  __AUTH_CONST.__const: 0x2178
+  __AUTH_CONST.__auth_got: 0x10a0
+  __AUTH_CONST.__const: 0x21e8
   __AUTH_CONST.__cfstring: 0x2a20
-  __AUTH_CONST.__objc_const: 0x101e0
-  __AUTH.__objc_data: 0x2038
-  __AUTH.__data: 0x11d0
+  __AUTH_CONST.__objc_const: 0x10300
+  __AUTH.__objc_data: 0x2048
+  __AUTH.__data: 0x12a0
   __DATA.__objc_ivar: 0x3a8
-  __DATA.__data: 0x24f8
+  __DATA.__data: 0x2508
   __DATA.__objc_stublist: 0x10
   __DATA.__bss: 0x2440
-  __DATA.__common: 0x58
+  __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 574FEE70-C69A-3B76-9B7D-C73D815A4A24
-  Functions: 2946
-  Symbols:   6850
-  CStrings:  3580
+  UUID: F90EEFF8-3310-3DD1-8EFE-0CBFFBFC4242
+  Functions: 2969
+  Symbols:   6872
+  CStrings:  3596
 
Symbols:
+ _OBJC_CLASS_$_AKWalrusController
+ __DATA__TtC9CoreCDPUI25ADPFlowAbandonmentTracker
+ __IVARS__TtC9CoreCDPUI25ADPFlowAbandonmentTracker
+ __METACLASS_DATA__TtC9CoreCDPUI25ADPFlowAbandonmentTracker
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy72_8
+ _block_copy_helper.1
+ _block_copy_helper.81
+ _block_descriptor.3
+ _block_descriptor.83
+ _block_destroy_helper.2
+ _block_destroy_helper.82
+ _objc_msgSend$beginADPFlowWithID:altDSID:completion:
+ _objc_msgSend$completeADPFlowWithID:success:completion:
+ _swift_getErrorValue
+ _symbolic $s9CoreCDPUI17WalrusControllingP
+ _symbolic _____ 9CoreCDPUI25ADPFlowAbandonmentTrackerC
+ _symbolic ______pyc 9CoreCDPUI17WalrusControllingP
- ___swift_memcpy64_8
- _block_copy_helper.80
- _block_descriptor.82
- _block_destroy_helper.81
CStrings:
+ "ADP flow completion registered with AuthKit"
+ "ADP flow tracking completed: flowID=%s, success=%{bool}d"
+ "ADP flow tracking registered with AuthKit"
+ "ADP flow tracking started: flowID=%s"
+ "Cannot begin ADP flow tracking: no altDSID available"
+ "Failed to begin ADP flow tracking: %s"
+ "Failed to complete ADP flow tracking: %s"
+ "No active ADP flow to complete"
+ "_TtC9CoreCDPUI25ADPFlowAbandonmentTracker"
+ "adpTracker"
+ "beginADPFlowWithID:altDSID:completion:"
+ "completeADPFlowTrackingWithSuccess:"
+ "completeADPFlowWithID:success:completion:"
+ "currentFlowID"
+ "walrusControllerFactory"

```
