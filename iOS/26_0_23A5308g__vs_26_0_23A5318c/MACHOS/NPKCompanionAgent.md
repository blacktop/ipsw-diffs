## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1274.1.0.0.0
-  __TEXT.__text: 0x42a08
+1276.0.0.0.0
+  __TEXT.__text: 0x42ac8
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x7760
-  __TEXT.__objc_methlist: 0x33a0
+  __TEXT.__objc_stubs: 0x77a0
+  __TEXT.__objc_methlist: 0x3380
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x12a4
-  __TEXT.__cstring: 0x268a
-  __TEXT.__objc_methname: 0xbbc5
-  __TEXT.__oslogstring: 0x91ce
+  __TEXT.__cstring: 0x26a7
+  __TEXT.__objc_methname: 0xbca2
+  __TEXT.__oslogstring: 0x9233
   __TEXT.__objc_classname: 0x6c1
-  __TEXT.__objc_methtype: 0x3487
+  __TEXT.__objc_methtype: 0x3478
   __TEXT.__unwind_info: 0xdd8
   __DATA_CONST.__auth_got: 0x698
   __DATA_CONST.__got: 0x6c8

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x5a48
-  __DATA.__objc_selrefs: 0x2718
+  __DATA.__objc_const: 0x5a30
+  __DATA.__objc_selrefs: 0x2728
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc00

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6CFB26B-FFAE-31C2-BFE6-BB0BBBD1A741
+  UUID: 08A5F6AB-93EA-3A2D-AF94-FF1B98E56DA5
   Functions: 1108
   Symbols:   441
   CStrings:  2769
Functions:
~ sub_100010d58 : 400 -> 452
~ sub_100010ee8 -> sub_100010f1c : 516 -> 536
~ sub_1000110ec -> sub_100011134 : 244 -> 264
~ sub_1000111e0 -> sub_10001123c : 892 -> 912
~ sub_100013ee4 -> sub_100013f54 : 152 -> 176
~ sub_10002a8b4 -> sub_10002a93c : 344 -> 380
~ sub_10002defc -> sub_10002dfa8 : 380 -> 400
CStrings:
+ "-[NPKRemoteAdminConnectionServiceAgent handleCredentialsUpdate:forUniqueID:paymentApplicationIdentifier:completion:]"
+ "Notice: (PKAppletSubcredential set) Got updated credentials %@ for pass with unique ID %@, paymentApplicationIdentifier: %@. Processing subject to first unlock and paired sync."
+ "Notice: Got credentials: %@ for pass with unique ID %@, paymentApplicationIdentifier %@; sending to %@"
+ "Notice: Request to update credentials %@, for unique ID: %@, paymentApplicationIdentifier: %@, completion %@"
+ "handleCredentialsUpdate:forUniqueID:paymentApplicationIdentifier:completion:"
+ "npkRelevancyShouldSuppressLiveActivity"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:forPaymentApplicationIdentifier:completion:"
+ "setShouldSuppressLiveActivity:"
+ "setSubcredentials:forPassWithUniqueID:paymentApplicationIdentifier:"
+ "updateCredentials:forUniqueID:paymentApplicationIdentifier:completion:"
+ "v48@0:8@\"NSSet\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSSet\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "-[NPKRemoteAdminConnectionServiceAgent handleCredentialsUpdate:forUniqueID:completion:]"
- "Notice: (PKAppletSubcredential set) Got updated credentials %@ for pass with unique ID %@. Processing subject to first unlock and paired sync."
- "Notice: Got credentials: %@ for pass with unique ID %@; sending to %@"
- "Notice: Request to update credentials %@, for unique ID: %@, completion %@"
- "handleCredentialsUpdate:forUniqueID:completion:"
- "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:"
- "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:completion:"
- "setSubcredentials:forPassWithUniqueID:"
- "updateCredentials:forUniqueID:completion:"
- "v32@0:8q16@?<v@?>24"
- "v32@0:8q16@?<v@?q>24"
- "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSSet\"24@?<v@?@\"NSError\">32"

```
