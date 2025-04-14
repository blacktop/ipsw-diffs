## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-396.35.2.11.14
-  __TEXT.__text: 0x744a8
+396.35.2.11.17
+  __TEXT.__text: 0x73b20
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xb214
-  __TEXT.__cstring: 0x66c7
+  __TEXT.__objc_methlist: 0xadf4
+  __TEXT.__cstring: 0x65a7
   __TEXT.__const: 0x3e8
-  __TEXT.__gcc_except_tab: 0x1c34
-  __TEXT.__oslogstring: 0x7668
+  __TEXT.__gcc_except_tab: 0x1c1c
+  __TEXT.__oslogstring: 0x7728
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x25e8
+  __TEXT.__unwind_info: 0x2580
   __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x1326
-  __TEXT.__objc_methname: 0x125bd
-  __TEXT.__objc_methtype: 0x38f3
-  __TEXT.__objc_stubs: 0xa820
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x2048
-  __DATA_CONST.__objc_classlist: 0x420
-  __DATA_CONST.__objc_protolist: 0x1d0
+  __TEXT.__objc_classname: 0x1281
+  __TEXT.__objc_methname: 0x1260e
+  __TEXT.__objc_methtype: 0x386a
+  __TEXT.__objc_stubs: 0xa880
+  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__const: 0x2060
+  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x39a8
-  __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x358
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__auth_ptr: 0x120
-  __AUTH_CONST.__const: 0xc10
+  __AUTH_CONST.__const: 0xbb0
   __AUTH_CONST.__cfstring: 0x5980
-  __AUTH_CONST.__objc_const: 0x13140
+  __AUTH_CONST.__objc_const: 0x12860
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0xdf4
-  __DATA.__data: 0x1650
-  __DATA.__bss: 0x600
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0xd8c
+  __DATA.__data: 0x1530
+  __DATA.__bss: 0x5f0
   __DATA_DIRTY.__objc_data: 0x2590
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x380

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4153
-  Symbols:   4704
-  CStrings:  5119
+  Functions: 4070
+  Symbols:   4613
+  CStrings:  5108
 
Symbols:
- _OBJC_CLASS_$_SPIntentSession
- _OBJC_CLASS_$_SPIntentSessionContext
- _OBJC_CLASS_$_SPUnifiedBeacon
- _OBJC_METACLASS_$_SPIntentSession
- _OBJC_METACLASS_$_SPIntentSessionContext
- _OBJC_METACLASS_$_SPUnifiedBeacon
- _SPIntentSessionErrorDomain
- _SPUnifiedSupportErrorDomain
CStrings:
+ "\x15\x11\x11$\x18,"
+ "<%@: %p %ld:%@ %@>"
+ "B16@?0@\"NSOrderedCollectionChange\"8"
+ "SPOwnerSession: registered for task info updates on this beacon: %@, subscribed: %i, error %@"
+ "SPOwnerSession: stopped all task info updates on this beacon: %@, stopped: %i, error %@"
+ "SPOwnerSession: task info updated beacon: %@, changes: %lu, error %@"
+ "T@\"NSDate\",C,N,V_lockedTimestamp"
+ "T@\"NSDate\",C,N,V_wipedTimestamp"
+ "T@\"NSString\",C,N,V_formattedName"
+ "T@\"NSString\",C,N,V_rawDeviceModel"
+ "_formattedName"
+ "_lockedTimestamp"
+ "_rawDeviceModel"
+ "_wipedTimestamp"
+ "fm_filter:"
+ "formattedName"
+ "handleWithString:formattedName:"
+ "initWithType:destination:formattedName:"
+ "lockedTimestamp"
+ "rawDeviceModel"
+ "setFormattedName:"
+ "setLockedTimestamp:"
+ "setRawDeviceModel:"
+ "setWipedTimestamp:"
+ "wipedTimestamp"
- "\x15\x11\x11$\x16+"
- "\x1b\x11\x16"
- "-[SPUnifiedSupportSession startUpdatingBeaconsWithContext:collectionDifference:completion:]"
- "-[SPUnifiedSupportSession stopUpdatingBeaconsWithCompletion:]"
- "<%@: %p %ld:%@>"
- "@\"<SPIntentSessionProtocol>\""
- "@\"NSArray\"16@0:8"
- "@\"SPIntentSessionContext\""
- "@24@0:8Q16"
- "SPIntentSession"
- "SPIntentSessionClientXPCProtocol"
- "SPIntentSessionContext"
- "SPIntentSessionProtocol"
- "SPOwnerSession: notifiedBeaconsChangedBlock: %@"
- "SPUnifiedBeacon"
- "SPUnifiedSupportProtocol"
- "SPUnifiedSupportSession"
- "T@\"<SPIntentSessionProtocol>\",&,N,V_proxy"
- "T@\"SPIntentSessionContext\",&,N,V_context"
- "TQ,N,V_useCase"
- "_useCase"
- "com.apple.SPOwner.SPUnifiedSupport.ErrorDomain"
- "com.apple.SPOwner.SPUnifiedSupportSession"
- "com.apple.icloud.searchpartyd.SPIntentSession.ErrorDomain"
- "com.apple.icloud.searchpartyd.intentsession"
- "deviceListUseCase"
- "initWithUseCase:"
- "itemListUseCase"
- "setUseCase:"
- "startSessionWithContext:completion:"
- "stopSessionWithCompletion:"
- "stopSessionWithContext:completion:"
- "unifiedBeaconContext"
- "unifiedBeacons"
- "unifiedSupport"
- "unifiedSupportSession"
- "useCase"
- "v16@?0@\"FMFuture\"8"
- "v32@0:8@\"SPIntentSessionContext\"16@?<v@?@\"NSError\">24"

```
