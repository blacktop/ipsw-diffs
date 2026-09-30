## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.80.19.0.0
-  __TEXT.__text: 0x215478
+61901.80.22.0.0
+  __TEXT.__text: 0x2154ac
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_stubs: 0x2500
   __TEXT.__objc_methlist: 0x276c
   __TEXT.__const: 0xab00
-  __TEXT.__cstring: 0x18dad
-  __TEXT.__objc_methname: 0x759a
+  __TEXT.__cstring: 0x18dbd
+  __TEXT.__objc_methname: 0x75cf
   __TEXT.__oslogstring: 0xa7fa
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x3790

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA.__objc_const: 0x6920
-  __DATA.__objc_selrefs: 0x1cd0
+  __DATA.__objc_selrefs: 0x1ce0
   __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x2a20
   __DATA.__data: 0x7ab0

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6757C706-E364-3870-9C59-C5D95A24E89D
+  UUID: CF2465FD-D747-3E5F-883B-7ED6ACFCCE0A
   Functions: 8126
   Symbols:   512
-  CStrings:  3444
+  CStrings:  3446
 
Functions:
~ sub_1001ca8b4 : 2000 -> 2052
CStrings:
+ "escrowCheck(passcodeGeneration:requiresEscrowCheck:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:reply:)"
+ "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:daysLeftOnRateLimit:reply:"
+ "setDaysLeftOnRateLimit:"
+ "setRateLimitState:"
- "escrowCheck(passcodeGeneration:requiresEscrowCheck:knownFederations:isBackgroundCheck:flowID:deviceSessionID:rateLimit:reply:)"
- "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:rateLimit:reply:"

```
