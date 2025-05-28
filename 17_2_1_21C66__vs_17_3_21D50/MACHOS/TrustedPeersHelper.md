## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61040.62.1.0.0
-  __TEXT.__text: 0x1f1000
+61040.80.10.0.1
+  __TEXT.__text: 0x1f1c50
   __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_stubs: 0x28c0
-  __TEXT.__objc_methlist: 0x28c4
-  __TEXT.__const: 0x9508
-  __TEXT.__objc_methname: 0x7b2b
-  __TEXT.__cstring: 0x1c372
+  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_methlist: 0x28e4
+  __TEXT.__const: 0x9510
+  __TEXT.__objc_methname: 0x7bc0
+  __TEXT.__cstring: 0x1c392
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x30d4
   __TEXT.__swift5_typeref: 0x32a2

   __TEXT.__swift5_proto: 0x878
   __TEXT.__swift5_types: 0x268
   __TEXT.__objc_classname: 0x44b
-  __TEXT.__objc_methtype: 0x1d8d
+  __TEXT.__objc_methtype: 0x1da1
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x3208
+  __TEXT.__swift5_capture: 0x322c
   __TEXT.__gcc_except_tab: 0x114
   __TEXT.__swift5_protos: 0x18
   __TEXT.__dlopen_cstrs: 0x216
   __TEXT.__oslogstring: 0x2cc
-  __TEXT.__unwind_info: 0x5ec0
+  __TEXT.__unwind_info: 0x5ec8
   __TEXT.__eh_frame: 0x5e80
   __DATA_CONST.__auth_got: 0xde0
   __DATA_CONST.__got: 0x408

   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x7458
-  __DATA.__objc_selrefs: 0x1d68
+  __DATA.__objc_const: 0x7488
+  __DATA.__objc_selrefs: 0x1d80
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x388
   __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x298
+  __DATA.__objc_ivar: 0x29c
   __DATA.__objc_data: 0x2828
   __DATA.__data: 0xee38
   __DATA.__objc_stublist: 0x98

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10161
+  Functions: 10164
   Symbols:   462
-  CStrings:  3092
+  CStrings:  3097
 
CStrings:
+ "@56@0:8@16@24@32B40@44B52"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "TB,V_canSendMetrics"
+ "_canSendMetrics"
+ "canSendMetrics"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "join(voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:canSendMetrics:reply:"
+ "permittedToSendMetrics"
+ "setCanSendMetrics:"
+ "v100@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80B88@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">92"
+ "v100@0:8@16@24@32@40@48@56@64@72@80B88@?92"
+ "v92@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSString\"64@\"NSString\"72B80@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">84"
+ "v92@0:8@16@24@32@40@48@56@64@72B80@?84"
+ "vouch(peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:canSendMetrics:reply:"
- "@52@0:8@16@24@32B40@44"
- "@68@0:8@16@24@32@40@48B56@60"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
- "join(voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:reply:)"
- "joinWithSpecificUser:voucherData:voucherSig:ckksKeys:tlkShares:preapprovedKeys:flowID:deviceSessionID:reply:"
- "v88@0:8@\"TPSpecificUser\"16@\"NSData\"24@\"NSData\"32@\"NSArray\"40@\"NSArray\"48@\"NSArray\"56@\"NSString\"64@\"NSString\"72@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">80"
- "v88@0:8@16@24@32@40@48@56@64@72@?80"
- "v96@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSData\"56@\"NSArray\"64@\"NSString\"72@\"NSString\"80@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
- "vouch(peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:altDSID:flowID:deviceSessionID:reply:)"
- "vouchWithSpecificUser:peerID:permanentInfo:permanentInfoSig:stableInfo:stableInfoSig:ckksKeys:flowID:deviceSessionID:reply:"

```
