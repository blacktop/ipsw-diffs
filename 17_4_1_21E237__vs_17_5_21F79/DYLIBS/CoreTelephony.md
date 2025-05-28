## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-11523.1.0.0.0
-  __TEXT.__text: 0xf47c0
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0xc238
+11594.0.0.0.0
+  __TEXT.__text: 0xf4aa4
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0xc258
   __TEXT.__const: 0xfaf
-  __TEXT.__gcc_except_tab: 0x91ec
-  __TEXT.__cstring: 0x197af
+  __TEXT.__gcc_except_tab: 0x920c
+  __TEXT.__cstring: 0x19866
   __TEXT.__oslogstring: 0x3d9f
-  __TEXT.__unwind_info: 0x53a0
+  __TEXT.__unwind_info: 0x53dc
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1ce2
-  __TEXT.__objc_methname: 0x169a4
+  __TEXT.__objc_classname: 0x1ce5
+  __TEXT.__objc_methname: 0x16a5c
   __TEXT.__objc_methtype: 0x6f42
-  __TEXT.__objc_stubs: 0xe960
+  __TEXT.__objc_stubs: 0xe9a0
   __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x6850
+  __DATA_CONST.__const: 0x6858
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12940
-  __DATA_CONST.__objc_selrefs: 0x4df0
+  __DATA_CONST.__objc_const: 0x12990
+  __DATA_CONST.__objc_selrefs: 0x4e10
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__objc_const: 0x7038
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__cfstring: 0x15840
+  __AUTH_CONST.__cfstring: 0x158a0
   __AUTH_CONST.__const: 0x1a10
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__auth_got: 0xc30
   __AUTH.__objc_data: 0x1f40
-  __DATA.__objc_ivar: 0xd28
+  __DATA.__objc_ivar: 0xd2c
   __DATA.__data: 0x1e50
   __DATA.__bss: 0x100
   __DATA.__common: 0x0

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6771
-  Symbols:   21449
-  CStrings:  9669
+  Functions: 6774
+  Symbols:   21461
+  CStrings:  9682
 
Symbols:
+ -[CTRemotePlan primaryAccount]
+ -[CTRemotePlan setPrimaryAccount:]
+ -[CoreTelephonyClient(CellularPlanManager) sendTravelBuddyCAEvent:carrierName:error:]
+ _OBJC_IVAR_$_CTRemotePlan._primaryAccount
+ __ZN14CSIPhoneNumber26setMatchedEmMetricListTypeE23CallMetricEmNumListType
+ __ZNK14CSIPhoneNumber26getMatchedEmMetricListTypeEv
+ ___85-[CoreTelephonyClient(CellularPlanManager) sendTravelBuddyCAEvent:carrierName:error:]_block_invoke
+ ___85-[CoreTelephonyClient(CellularPlanManager) sendTravelBuddyCAEvent:carrierName:error:]_block_invoke_2
+ ___block_literal_global.1137
+ ___block_literal_global.1142
+ ___block_literal_global.1146
+ _kCTSMSCellBroadcastAlertMessageID
+ _objc_msgSend$primaryAccount
+ _objc_msgSend$sendTravelBuddyCAEventWithCompletion:carrierName:completion:
+ _puts
- __ZN14CSIPhoneNumber19setMatchingListTypeENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK14CSIPhoneNumber19getMatchingListTypeEv
- __ZNSt3__123__optional_storage_baseINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EE16__construct_fromB8un170006IRKNS_20__optional_copy_baseIS6_Lb0EEEEEvOT_
- __ZNSt3__18optionalINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB8un170006IRS6_vEERS7_OT_
- ___block_literal_global.1136
- ___block_literal_global.1141
- ___block_literal_global.1145
CStrings:
+ "\x03\x11"
+ " primary-account-holder:\""
+ " primaryAccount=%d"
+ "11594"
+ "11594~15"
+ "AlertMessageID"
+ "T@\"NSNumber\",&,N,V_primaryAccount"
+ "_primaryAccount"
+ "calling for sendTravelBuddyCAEventWithCompletion"
+ "in completion handler for sendTravelBuddyCAEventWithCompletion"
+ "primaryAccount"
+ "sendTravelBuddyCAEvent:carrierName:error:"
+ "sendTravelBuddyCAEventWithCompletion:carrierName:completion:"
+ "setPrimaryAccount:"
- "11523.1"
- "11523.1~85"

```
