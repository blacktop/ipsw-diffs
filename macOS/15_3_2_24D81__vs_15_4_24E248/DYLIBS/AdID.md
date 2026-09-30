## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/Versions/A/AdID`

```diff

-632.0.0.0.0
-  __TEXT.__text: 0x1b180
+636.4.0.0.0
+  __TEXT.__text: 0x1b4c0
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0xd04
+  __TEXT.__objc_methlist: 0xfdc
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x6dc
-  __TEXT.__cstring: 0x662c
+  __TEXT.__gcc_except_tab: 0x6d8
+  __TEXT.__cstring: 0x66f1
   __TEXT.__unwind_info: 0x5a8
   __TEXT.__objc_classname: 0x19f
-  __TEXT.__objc_methname: 0x3c18
+  __TEXT.__objc_methname: 0x3c48
   __TEXT.__objc_methtype: 0x6cc
-  __TEXT.__objc_stubs: 0x3dc0
+  __TEXT.__objc_stubs: 0x3e00
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1258
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x25d0
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x20f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B792AD02-3279-3621-9999-382595B6DDC9
-  Functions: 425
-  Symbols:   1457
-  CStrings:  1845
+  UUID: 0B12D6CB-7C93-3B1F-BD78-464CFCC40790
+  Functions: 431
+  Symbols:   1466
+  CStrings:  1857
 
Symbols:
+ +[ADAMSBagManager bagSubProfileVersion].cold.1
+ +[ADAMSBagManager bagSubProfile].cold.1
+ +[ADAdTrackingSchedulingManager sharedInstance].cold.1
+ +[ADClientDPIDManager sharedInstance].cold.1
+ -[ADAdTrackingSchedulingManager setSessionManagementDefaults]
+ -[ADIDManager(Private) rotateAccountToken]
+ -[ADJingleRequest init:withCompletion:].cold.1
+ GCC_except_table36
+ _objc_msgSend$rotateAccountToken
+ _objc_msgSend$setSessionManagementDefaults
- GCC_except_table35
CStrings:
+ "AccountStateUUID"
+ "PersonalizedAdsStateUUID"
+ "[%@]: Setting UUID - %@ for account DSID state."
+ "[%@]: Setting UUID - %@ for session management state"
+ "[%@]: Setting UUID - %@ for session management state."
+ "rotateAccountToken"
+ "setSessionManagementDefaults"

```
