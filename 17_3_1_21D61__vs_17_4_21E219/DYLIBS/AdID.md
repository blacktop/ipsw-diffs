## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-608.0.0.0.0
-  __TEXT.__text: 0x18344
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xdcc
+618.0.0.0.0
+  __TEXT.__text: 0x183cc
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0xdc4
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x4dc
-  __TEXT.__cstring: 0x6692
-  __TEXT.__unwind_info: 0x564
+  __TEXT.__gcc_except_tab: 0x518
+  __TEXT.__cstring: 0x6698
+  __TEXT.__unwind_info: 0x56c
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x3f1b
+  __TEXT.__objc_methname: 0x3ef5
   __TEXT.__objc_methtype: 0x6f2
-  __TEXT.__objc_stubs: 0x3f80
+  __TEXT.__objc_stubs: 0x3f20
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0xa28
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2388
-  __DATA_CONST.__objc_selrefs: 0x11f8
+  __DATA_CONST.__objc_const: 0x2398
+  __DATA_CONST.__objc_selrefs: 0x11f0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x4060
   __AUTH_CONST.__objc_const: 0x6f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x2b0
-  __DATA.__objc_superrefs: 0x58
   __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 406
-  Symbols:   1915
-  CStrings:  1367
+  Functions: 404
+  Symbols:   1903
+  CStrings:  1368
 
Symbols:
+ -[ADClientDPIDManager setIsDPIDLocalTo:]
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table7
+ ___block_literal_global.488
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$adprivacydBag
+ _objc_msgSend$isDPIDLocal
+ _objc_msgSend$setIsDPIDLocal:
+ _objc_msgSend$setIsDPIDLocalTo:
+ _objc_retain_x24
+ _objc_retain_x27
- +[ADAMSBagManager bagKeySet]
- GCC_except_table10
- GCC_except_table40
- GCC_except_table43
- _OBJC_CLASS_$_AMSBag
- _OBJC_CLASS_$_AMSBagKeySet
- _OBJC_CLASS_$_AMSEphemeralDefaults
- _OBJC_CLASS_$_AMSMutableBagKeySet
- ___28+[ADAMSBagManager bagKeySet]_block_invoke
- ___41+[ADAMSBagManager createBagForSubProfile]_block_invoke
- ___block_literal_global.14
- ___block_literal_global.19
- ___block_literal_global.482
- ___block_literal_global.9
- _bagKeySet.bagKeySet
- _bagKeySet.onceToken
- _createBagForSubProfile.onceToken
- _objc_msgSend$addBagKey:valueType:
- _objc_msgSend$bagForProfile:profileVersion:
- _objc_msgSend$bagKeySet
- _objc_msgSend$bagSubProfile
- _objc_msgSend$bagSubProfileVersion
- _objc_msgSend$registerBagKeySet:forProfile:profileVersion:
- _objc_msgSend$setHARLoggingEnabled:
CStrings:
+ "DPID %@ Already exists, checking for isDPIDLocal flag"
+ "T@\"AMSBagKeySet\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "We need to sync with iCloud"
+ "adprivacydBag"
+ "isDPIDLocal"
+ "isDPIDLocal flag is %d"
+ "setIsDPIDLocal:"
+ "setIsDPIDLocalTo:"
- "DPID Already exists, not creating one %@"
- "T@\"AMSBagKeySet\",R,N"
- "addBagKey:valueType:"
- "bagForProfile:profileVersion:"
- "isSponsoredAdsEnabled"
- "isSponsoredAdsEnabledForAdTrackingd"
- "registerBagKeySet:forProfile:profileVersion:"
- "setHARLoggingEnabled:"

```
