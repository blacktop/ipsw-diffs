## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-71.454.0.0.0
-  __TEXT.__text: 0xe6e4
+71.455.0.0.0
+  __TEXT.__text: 0xece0
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x1554
+  __TEXT.__objc_methlist: 0x168c
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x9eb
-  __TEXT.__cstring: 0xce8
-  __TEXT.__gcc_except_tab: 0x264
+  __TEXT.__oslogstring: 0xa14
+  __TEXT.__cstring: 0xdaf
+  __TEXT.__gcc_except_tab: 0x260
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x548
-  __TEXT.__objc_classname: 0x28f
-  __TEXT.__objc_methname: 0x32fa
+  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_classname: 0x2aa
+  __TEXT.__objc_methname: 0x359c
   __TEXT.__objc_methtype: 0x7b5
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__objc_stubs: 0x2560
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x928
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0xf90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xc80
-  __AUTH_CONST.__objc_const: 0x2e18
-  __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x14c
+  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__objc_const: 0x3068
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x308
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 517
-  Symbols:   2096
-  CStrings:  993
+  Functions: 543
+  Symbols:   2175
+  CStrings:  1045
 
Symbols:
+ +[AAAFollowUpAnalyticsInfo supportsSecureCoding]
+ +[AAFKeybagLockAssertion lockWithError:].cold.3
+ -[AAAFollowUpAnalyticsInfo .cxx_destruct]
+ -[AAAFollowUpAnalyticsInfo cfuReasonAnalyticsEvent]
+ -[AAAFollowUpAnalyticsInfo cfuType]
+ -[AAAFollowUpAnalyticsInfo client]
+ -[AAAFollowUpAnalyticsInfo copyWithZone:]
+ -[AAAFollowUpAnalyticsInfo deviceSessionID]
+ -[AAAFollowUpAnalyticsInfo encodeWithCoder:]
+ -[AAAFollowUpAnalyticsInfo eventName]
+ -[AAAFollowUpAnalyticsInfo flowID]
+ -[AAAFollowUpAnalyticsInfo hasProxiedDevice]
+ -[AAAFollowUpAnalyticsInfo initWithCoder:]
+ -[AAAFollowUpAnalyticsInfo postDidSucceed]
+ -[AAAFollowUpAnalyticsInfo postedReasonError]
+ -[AAAFollowUpAnalyticsInfo proxiedBundleID]
+ -[AAAFollowUpAnalyticsInfo setCfuType:]
+ -[AAAFollowUpAnalyticsInfo setClient:]
+ -[AAAFollowUpAnalyticsInfo setDeviceSessionID:]
+ -[AAAFollowUpAnalyticsInfo setEventName:]
+ -[AAAFollowUpAnalyticsInfo setFlowID:]
+ -[AAAFollowUpAnalyticsInfo setHasProxiedDevice:]
+ -[AAAFollowUpAnalyticsInfo setPostDidSucceed:]
+ -[AAAFollowUpAnalyticsInfo setPostedReasonError:]
+ -[AAAFollowUpAnalyticsInfo setProxiedBundleID:]
+ -[AAFKeybagLockAssertion unlock].cold.1
+ _OBJC_CLASS_$_AAAFollowUpAnalyticsInfo
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._cfuType
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._client
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._deviceSessionID
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._eventName
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._flowID
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._hasProxiedDevice
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._postDidSucceed
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._postedReasonError
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._proxiedBundleID
+ _OBJC_METACLASS_$_AAAFollowUpAnalyticsInfo
+ __OBJC_$_CLASS_METHODS_AAAFollowUpAnalyticsInfo
+ __OBJC_$_INSTANCE_METHODS_AAAFollowUpAnalyticsInfo
+ __OBJC_$_INSTANCE_VARIABLES_AAAFollowUpAnalyticsInfo
+ __OBJC_$_PROP_LIST_AAAFollowUpAnalyticsInfo
+ __OBJC_CLASS_RO_$_AAAFollowUpAnalyticsInfo
+ __OBJC_METACLASS_RO_$_AAAFollowUpAnalyticsInfo
+ _kAAFFollowUpFlowID
+ _kAAFollowUpClient
+ _kAAFollowUpDeviceSessionID
+ _kAAFollowUpEventName
+ _kAAFollowUpHasProxiedDevice
+ _kAAFollowUpPostDidSucceed
+ _kAAFollowUpProxiedBundleID
+ _kAAFollowUpType
+ _kPostFollowupReasonEvent
+ _objc_msgSend$populateUnderlyingErrorsStartingWithRootError:
CStrings:
+ "\t"
+ "AAAFollowUpAnalyticsInfo"
+ "T@\"NSError\",C,N,V_postedReasonError"
+ "T@\"NSNumber\",C,N,V_hasProxiedDevice"
+ "T@\"NSNumber\",C,N,V_postDidSucceed"
+ "T@\"NSString\",C,N,V_cfuType"
+ "T@\"NSString\",C,N,V_client"
+ "T@\"NSString\",C,N,V_deviceSessionID"
+ "T@\"NSString\",C,N,V_eventName"
+ "T@\"NSString\",C,N,V_flowID"
+ "T@\"NSString\",C,N,V_proxiedBundleID"
+ "Taking device lock assertion for 10 mins"
+ "_cfuType"
+ "_client"
+ "_deviceSessionID"
+ "_flowID"
+ "_hasProxiedDevice"
+ "_postDidSucceed"
+ "_postedReasonError"
+ "_proxiedBundleID"
+ "cfuReasonAnalyticsEvent"
+ "cfuType"
+ "client"
+ "com.apple.aaa.followUpPosted"
+ "didSuceed"
+ "hasProxiedDevice"
+ "postDidSucceed"
+ "postedReasonError"
+ "proxiedBundleID"
+ "proxiedBundleId"
+ "setCfuType:"
+ "setClient:"
+ "setDeviceSessionID:"
+ "setEventName:"
+ "setFlowID:"
+ "setHasProxiedDevice:"
+ "setPostDidSucceed:"
+ "setPostedReasonError:"
+ "setProxiedBundleID:"

```
