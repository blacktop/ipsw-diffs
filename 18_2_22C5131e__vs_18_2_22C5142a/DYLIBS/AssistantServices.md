## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3402.74.3.1.1
-  __TEXT.__text: 0x1a6430
+3402.74.3.11.4
+  __TEXT.__text: 0x1a7468
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x19c3c
+  __TEXT.__objc_methlist: 0x19cc4
   __TEXT.__const: 0x458
-  __TEXT.__gcc_except_tab: 0x2670
-  __TEXT.__cstring: 0x3c28a
-  __TEXT.__oslogstring: 0x103fe
+  __TEXT.__gcc_except_tab: 0x26c0
+  __TEXT.__cstring: 0x3c5bf
+  __TEXT.__oslogstring: 0x106f9
   __TEXT.__dlopen_cstrs: 0x484
-  __TEXT.__unwind_info: 0x7ac8
-  __TEXT.__objc_classname: 0x4e65
-  __TEXT.__objc_methname: 0x3a9d8
+  __TEXT.__unwind_info: 0x7b20
+  __TEXT.__objc_classname: 0x4e81
+  __TEXT.__objc_methname: 0x3aacc
   __TEXT.__objc_methtype: 0xa98c
-  __TEXT.__objc_stubs: 0x24220
-  __DATA_CONST.__got: 0x1618
-  __DATA_CONST.__const: 0x8320
-  __DATA_CONST.__objc_classlist: 0xdb8
+  __TEXT.__objc_stubs: 0x24360
+  __DATA_CONST.__got: 0x1620
+  __DATA_CONST.__const: 0x8348
+  __DATA_CONST.__objc_classlist: 0xdc0
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbfb8
+  __DATA_CONST.__objc_selrefs: 0xc008
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0xdc8
+  __DATA_CONST.__objc_superrefs: 0xdd0
   __DATA_CONST.__objc_arraydata: 0x1fa8
   __AUTH_CONST.__auth_got: 0xab8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x38c0
+  __AUTH_CONST.__const: 0x3940
   __AUTH_CONST.__cfstring: 0x26c20
-  __AUTH_CONST.__objc_const: 0x3a068
+  __AUTH_CONST.__objc_const: 0x3a138
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x7440
-  __AUTH.__data: 0x290
-  __DATA.__objc_ivar: 0x2554
+  __AUTH.__objc_data: 0x7490
+  __AUTH.__data: 0x2a8
+  __DATA.__objc_ivar: 0x2558
   __DATA.__data: 0x4108
-  __DATA.__bss: 0x1288
+  __DATA.__bss: 0x12d0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11672
-  Symbols:   13879
-  CStrings:  19040
+  Functions: 11700
+  Symbols:   13909
+  CStrings:  19085
 
Symbols:
+ _OBJC_CLASS_$_AFFamilyCircleStatusManager
+ _OBJC_METACLASS_$_AFFamilyCircleStatusManager
CStrings:
+ "%s #Montara"
+ "%s #Montara #FamilyCircle"
+ "%s #Montara #FamilyCircle Family members received: %@ in circle: %@"
+ "%s #Montara #FamilyCircle Unable to get FAFetchFamilyCircleRequest class"
+ "%s #Montara #FamilyCircle completed"
+ "%s #Montara #FamilyCircle failed to locate Me record"
+ "%s #Montara #FamilyCircle family circle is nil, skipping restriction check."
+ "%s #Montara #FamilyCircle received account change event account=%@ type=%d"
+ "%s #Montara #FamilyCircle setup ACDAccountStoreDidChangeNotification observer completed"
+ "%s #Montara #FamilyCircle setup ACDAccountStoreDidChangeNotification observer failed"
+ "%s #Montara #FamilyCircle setup ACXPCEventSubscriber"
+ "%s #Montara #FamilyCircle setup ACXPCEventSubscriber completed"
+ "%s #Montara #FamilyCircle setup FAFamilyUpdateNotification observer completed"
+ "%s #Montara #FamilyCircle setup FAFamilyUpdateNotification observer failed"
+ "%s #Montara #FamilyCircle there was an error determining child restriction status %@"
+ "%s #Montara #FamilyCircle user is a child"
+ "%s #Montara restrictions, mdm: %d, child: %d"
+ "%s #Montara restrictions, mdm: %d, child: skipped"
+ "-[AFFamilyCircleStatusManager _fetchChildAccountStatus]"
+ "-[AFFamilyCircleStatusManager _fetchChildAccountStatus]_block_invoke"
+ "-[AFFamilyCircleStatusManager _observeAccountChanges]"
+ "-[AFFamilyCircleStatusManager _observeAccountChanges]_block_invoke"
+ "-[AFFamilyCircleStatusManager _observeFamilyChanges]"
+ "-[AFFamilyCircleStatusManager dealloc]"
+ "-[AFFamilyCircleStatusManager fetchChildAccountStatus]"
+ "-[AFFamilyCircleStatusManager init]"
+ "/System/Library/Frameworks/Accounts.framework/Accounts"
+ "ACDAccountStoreDidChangeNotification"
+ "ACXPCEventSubscriber"
+ "AFFamilyCircleStatusManager"
+ "AFFamilyCircleStatusManager.m"
+ "AccountsLibrary"
+ "FAFamilyUpdateNotification"
+ "TB,V_childAccount"
+ "_HandleACDAccountStoreDidChange"
+ "_HandleFAFamilyUpdate"
+ "_childAccount"
+ "_fetchChildAccountStatus"
+ "_observeAccountChanges"
+ "_observeFamilyChanges"
+ "childAccount"
+ "classACXPCEventSubscriber"
+ "fetchChildAccountStatus"
+ "initACDAccountStoreDidChangeNotification_block_invoke"
+ "initACXPCEventSubscriber_block_invoke"
+ "initFAFamilyUpdateNotification_block_invoke"
+ "isChildAccount"
+ "registerAccountChangeEventHandler:"
+ "setChildAccount:"
+ "setQualityOfService:"
+ "sharedSubscriber"
+ "v20@?0@\"ACAccount\"8i16"
- "%s Montara: family circle is empty, skipping restriction check."
- "%s Montara: family circle is nil, skipping restriction check."
- "%s Montara: restrictions, mdm: %d, child: %d"
- "%s Montara: restrictions, mdm: %d, child: skipped"
- "%s Montara: there was an error determining child restriction status %@"
- "%s Montara: user is a child"
- "AFMontaraRestricted_block_invoke"

```
