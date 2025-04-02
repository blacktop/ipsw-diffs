## AudioServerDriver

> `/System/Library/PrivateFrameworks/AudioServerDriver.framework/AudioServerDriver`

```diff

-1040.10.0.0.0
-  __TEXT.__text: 0x5fccc
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x3554
-  __TEXT.__gcc_except_tab: 0x30cc
+1050.4.1.0.0
+  __TEXT.__text: 0x60574
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x35bc
+  __TEXT.__gcc_except_tab: 0x3138
   __TEXT.__const: 0x7ac
-  __TEXT.__cstring: 0x3768
-  __TEXT.__oslogstring: 0x26d2
+  __TEXT.__cstring: 0x38c3
+  __TEXT.__oslogstring: 0x26f1
   __TEXT.__dof_ASDInterf: 0xe5f
-  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__unwind_info: 0x1ea8
   __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0x3c6
-  __TEXT.__objc_methname: 0x5f48
+  __TEXT.__objc_classname: 0x3c7
+  __TEXT.__objc_methname: 0x5fa0
   __TEXT.__objc_methtype: 0x22cb
-  __TEXT.__objc_stubs: 0x3da0
+  __TEXT.__objc_stubs: 0x3dc0
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1600
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x7a8
   __AUTH_CONST.__const: 0x750
-  __AUTH_CONST.__cfstring: 0x22e0
-  __AUTH_CONST.__objc_const: 0x6078
+  __AUTH_CONST.__cfstring: 0x2300
+  __AUTH_CONST.__objc_const: 0x60a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4bc
+  __DATA.__objc_ivar: 0x4c0
   __DATA.__data: 0x3c8
   __DATA.__bss: 0xe8
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2131
-  Symbols:   2724
-  CStrings:  2127
+  Functions: 2149
+  Symbols:   2750
+  CStrings:  2137
 
Symbols:
+ __ZN18ASDDSPStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
+ __ZN18ASDDSPStreamHelper9DSPStream17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
+ __ZN18ASDDSPStreamHelper9DSPStreamC1E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_U13block_pointerFiyjS5_E
+ __ZN18ASDDSPStreamHelper9DSPStreamC2E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_U13block_pointerFiyjS5_E
+ __ZN18ASDSRCStreamHelper17readIsolatedInputEyjPK28AudioServerPlugInIOCycleInfo
- __ZN18ASDDSPStreamHelper9DSPStreamC1E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_
- __ZN18ASDDSPStreamHelper9DSPStreamC2E18ASDStreamDirection24CAStreamBasicDescriptionU13block_pointerFijPK28AudioServerPlugInIOCycleInfoPvS6_jES8_
- _objc_retain_x4
CStrings:
+ "\x06\x12\x123\xf0\x1f\x01"
+ " Failed bypassed DSP readInput"
+ "%@|    Supports Isolated IO: %@\n"
+ "-[ASDDSPStream readIsolatedInputBlock]_block_invoke"
+ "-[ASDSRCStream readIsolatedInputBlock]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/a8fb6168-0667-11f0-a4eb-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
+ "NULL == inIOCycleInfo"
+ "TB,N,V_supportsIsolatedIO"
+ "_supportsIsolatedIO"
+ "i28@?0Q8I16r^{AudioServerPlugInIOCycleInfo=QI{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}(?=dd)d}20"
+ "setSupportsIsolatedIO:"
+ "supportsIsolatedIO"
+ "\xf0\xf0\xf0Q"
- "\x06\x12\x123\xff\x01"
- "/AppleInternal/Library/BuildRoots/f42a321a-fb9b-11ef-8bf4-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/System/Library/PrivateFrameworks/AudioToolboxCore.framework/PrivateHeaders/DSPGraph_Box.h"
- "\xf0\xf0\xf0A"

```
