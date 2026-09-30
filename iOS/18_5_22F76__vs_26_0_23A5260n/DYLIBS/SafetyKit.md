## SafetyKit

> `/System/Library/Frameworks/SafetyKit.framework/SafetyKit`

```diff

-125.0.17.0.0
-  __TEXT.__text: 0x1073c
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0xe2c
+143.0.0.0.0
+  __TEXT.__text: 0x10ec4
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0xe44
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x18f6
-  __TEXT.__oslogstring: 0x1ce3
-  __TEXT.__gcc_except_tab: 0x6ec
-  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__cstring: 0x1955
+  __TEXT.__oslogstring: 0x1ddd
+  __TEXT.__gcc_except_tab: 0x7b4
+  __TEXT.__unwind_info: 0x5f8
   __TEXT.__objc_classname: 0x2da
-  __TEXT.__objc_methname: 0x2aae
+  __TEXT.__objc_methname: 0x2adb
   __TEXT.__objc_methtype: 0xaee
   __TEXT.__objc_stubs: 0x2380
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__const: 0x700
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
+  __DATA_CONST.__objc_selrefs: 0xb30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x1b0
-  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__cfstring: 0xa40
   __AUTH_CONST.__objc_const: 0x2680
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x3c0

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2F5FA82-E01B-361C-B5AD-0BC4028DFF3C
-  Functions: 415
-  Symbols:   1848
-  CStrings:  981
+  UUID: 52CD1FA5-BA37-3E59-BE34-A592857B235B
+  Functions: 420
+  Symbols:   1863
+  CStrings:  991
 
Symbols:
+ -[CSKappaConnection sendTestAOI:]
+ -[CSKappaConnection sendTestAOI:].cold.1
+ -[CSKappaConnection testSensorAccessQueryWithReply:]
+ -[CSKappaConnection testSensorAccessQueryWithReply:].cold.1
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ _CSKappaConnectionTestAOIName
+ _CSKappaConnectionTestSensorAccessQuery
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__115allocate_sharedB8ne200100I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryIP8NSStringP11objc_objectEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEU8__strongP8NSNumberELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne200100IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne200100IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne200100IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryIP8NSStringP11objc_objectEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne200100IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEU8__strongP8NSNumberES3_Li0EEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ ___52-[CSKappaConnection testSensorAccessQueryWithReply:]_block_invoke
+ ___52-[CSKappaConnection testSensorAccessQueryWithReply:]_block_invoke.cold.1
+ ___52-[CSKappaConnection testSensorAccessQueryWithReply:]_block_invoke.cold.2
+ ___block_descriptor_40_ea8_32bs_e85_v24?0{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}8ls32l8
+ ___block_literal_global.48
- GCC_except_table25
- GCC_except_table30
- GCC_except_table31
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__115allocate_sharedB8ne190102I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I19CLConnectionMessageNS_9allocatorIS1_EEJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEU8__strongP8NSNumberELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne190102IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne190102IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEERU8__strongP12NSDictionaryES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B8ne190102IJNS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEU8__strongP8NSNumberES3_Li0EEES3_DpOT_
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __Znwm
- ___block_literal_global.42
CStrings:
+ "CSKappaConnectionTestSensorAccessQuery"
+ "SensorAccess"
+ "com.apple.anomalydetectiond.kappa.aoi.test"
+ "sendTestAOI:"
+ "testSensorAccessQueryWithReply:"
+ "{\"msg%{public}.0s\":\"sendTestAOISignal\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"testSensorAccessQuery\", \"name\":%{public, location:escape_only}s, \"value\":%{public, location:escape_only}@}"

```
