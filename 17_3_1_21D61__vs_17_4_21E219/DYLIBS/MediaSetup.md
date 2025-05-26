## MediaSetup

> `/System/Library/Frameworks/MediaSetup.framework/MediaSetup`

```diff

-207.30.3.0.0
-  __TEXT.__text: 0x12cd4
+207.40.20.0.0
+  __TEXT.__text: 0x128fc
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x18ac
+  __TEXT.__objc_methlist: 0x184c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x26bb
+  __TEXT.__cstring: 0x25eb
   __TEXT.__gcc_except_tab: 0x190
   __TEXT.__oslogstring: 0x62e
-  __TEXT.__unwind_info: 0x654
-  __TEXT.__objc_classname: 0x45c
-  __TEXT.__objc_methname: 0x421d
-  __TEXT.__objc_methtype: 0xa48
-  __TEXT.__objc_stubs: 0x2c60
+  __TEXT.__unwind_info: 0x638
+  __TEXT.__objc_classname: 0x43f
+  __TEXT.__objc_methname: 0x41c5
+  __TEXT.__objc_methtype: 0xa5c
+  __TEXT.__objc_stubs: 0x2b80
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x8d0
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4120
-  __DATA_CONST.__objc_selrefs: 0xfa8
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0x1060
+  __DATA_CONST.__objc_const: 0x4098
+  __DATA_CONST.__objc_selrefs: 0xf88
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__objc_const: 0x1018
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x288
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x1c8
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x1f4
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x1f0
   __DATA.__data: 0x548
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 623
-  Symbols:   2484
-  CStrings:  1286
+  Functions: 614
+  Symbols:   2449
+  CStrings:  1275
 
Symbols:
+ -[MSServiceAppInfo initWithServiceName:serviceBundleID:useInHome:subscriptionStatus:]
+ -[MSServiceAppInfo subscriptionStatus]
+ -[MSServiceAppInfo useInHome]
+ _OBJC_IVAR_$_MSServiceAppInfo._subscriptionStatus
+ _OBJC_IVAR_$_MSServiceAppInfo._useInHome
+ ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.123
+ ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.123.cold.1
+ ___47-[MSServer listener:shouldAcceptNewConnection:]_block_invoke.129
+ ___54-[MediaServiceConfiguration thirdPartyMusicAvailable:]_block_invoke.131
+ ___block_literal_global.144
- +[MSAnalytics sendDefaultServiceChangedEvent:]
- -[MSDefaultServiceChangedEvent .cxx_destruct]
- -[MSDefaultServiceChangedEvent initWithOldServiceID:newServiceID:]
- -[MSDefaultServiceChangedEvent oldServiceID]
- -[MSDefaultServiceChangedEvent serviceID]
- -[MSDefaultServiceChangedEvent setOldServiceID:]
- -[MSDefaultServiceChangedEvent setServiceID:]
- -[MSSetupCompleteEvent openDefaultService]
- -[MSSetupCompleteEvent setOpenDefaultService:]
- -[MediaServiceConfiguration getResolvedServiceAndUser:sharedUserID:completion:]
- _OBJC_CLASS_$_MSDefaultServiceChangedEvent
- _OBJC_IVAR_$_MSDefaultServiceChangedEvent._oldServiceID
- _OBJC_IVAR_$_MSDefaultServiceChangedEvent._serviceID
- _OBJC_IVAR_$_MSSetupCompleteEvent._openDefaultService
- _OBJC_METACLASS_$_MSDefaultServiceChangedEvent
- __OBJC_$_INSTANCE_METHODS_MSDefaultServiceChangedEvent
- __OBJC_$_INSTANCE_VARIABLES_MSDefaultServiceChangedEvent
- __OBJC_$_PROP_LIST_MSDefaultServiceChangedEvent
- __OBJC_CLASS_RO_$_MSDefaultServiceChangedEvent
- __OBJC_METACLASS_RO_$_MSDefaultServiceChangedEvent
- ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.122
- ___43-[MediaServiceConfiguration initWithQueue:]_block_invoke.122.cold.1
- ___46+[MSAnalytics sendDefaultServiceChangedEvent:]_block_invoke
- ___47-[MSServer listener:shouldAcceptNewConnection:]_block_invoke.128
- ___54-[MediaServiceConfiguration thirdPartyMusicAvailable:]_block_invoke.130
- ___79-[MediaServiceConfiguration getResolvedServiceAndUser:sharedUserID:completion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e45_v24?0"MSServiceResolutionInfo"8"NSError"16ls32l8
- ___block_literal_global.143
- _kMediaSetupCADefaultServiceChangedEvent
- _objc_msgSend$oldServiceID
- _objc_msgSend$serviceAppInfo
- _objc_msgSend$serviceBundleID
- _objc_msgSend$setOldServiceID:
- _objc_msgSend$setOpenDefaultService:
- _objc_msgSend$sharedUserID
- _objc_msgSend$userAccountInfo
CStrings:
+ "@44@0:8@16@24B32q36"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_useInHome"
+ "Tq,R,N,V_subscriptionStatus"
+ "_subscriptionStatus"
+ "_useInHome"
+ "alternateBundleID"
+ "initWithServiceName:serviceBundleID:useInHome:subscriptionStatus:"
+ "subscriptionStatus"
+ "useInHome"
- "MSDefaultServiceChangedEvent"
- "T@\"NSString\",&,N,V_oldServiceID"
- "TB,N,V_openDefaultService"
- "ThirdPartyAlternateBundleIDS"
- "ThirdPartyServiceBundleID"
- "ThirdPartyServiceName"
- "_oldServiceID"
- "_openDefaultService"
- "com.apple.amp.agora.player"
- "com.apple.amp.agora.plaza"
- "com.apple.cloudmediaservices.defaultservicechanged"
- "getResolvedServiceAndUser:sharedUserID:completion:"
- "initWithOldServiceID:newServiceID:"
- "newServiceID"
- "oldServiceID"
- "openDefaultService"
- "sendDefaultServiceChangedEvent:"
- "setOldServiceID:"
- "setOpenDefaultService:"

```
