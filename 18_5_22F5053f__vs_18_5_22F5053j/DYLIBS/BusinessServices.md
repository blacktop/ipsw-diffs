## BusinessServices

> `/System/Library/PrivateFrameworks/BusinessServices.framework/BusinessServices`

```diff

-30095.35.3.18.2
-  __TEXT.__text: 0x21064
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x6bc
+30095.35.3.18.3
+  __TEXT.__text: 0x21938
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x7a4
   __TEXT.__swift5_typeref: 0x8ba
-  __TEXT.__const: 0x1170
+  __TEXT.__const: 0x1178
   __TEXT.__swift5_reflstr: 0x661
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_fieldmd: 0x6ec
   __TEXT.__constg_swiftt: 0xda0
-  __TEXT.__cstring: 0xd84
+  __TEXT.__cstring: 0xde9
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_proto: 0xb8

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_capture: 0x2ec
-  __TEXT.__oslogstring: 0x9a1
-  __TEXT.__unwind_info: 0x8f0
+  __TEXT.__oslogstring: 0xa1a
+  __TEXT.__unwind_info: 0x918
   __TEXT.__eh_frame: 0x9a0
-  __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methname: 0xc38
-  __TEXT.__objc_methtype: 0x338
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x130
+  __TEXT.__objc_classname: 0xc8
+  __TEXT.__objc_methname: 0xefc
+  __TEXT.__objc_methtype: 0x3a3
+  __TEXT.__objc_stubs: 0x760
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x650
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__auth_ptr: 0x268
-  __AUTH_CONST.__const: 0x11b8
+  __AUTH_CONST.__const: 0x11d8
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x1390
+  __AUTH_CONST.__objc_const: 0x14f0
   __AUTH.__objc_data: 0x830
   __AUTH.__data: 0xba0
-  __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x568
+  __DATA.__objc_ivar: 0x28
+  __DATA.__data: 0x5c8
   __DATA.__bss: 0xf80
   __DATA.__common: 0x40
   __DATA_DIRTY.__data: 0x198

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 889
-  Symbols:   761
-  CStrings:  371
+  Functions: 905
+  Symbols:   833
+  CStrings:  413
 
Symbols:
+ -[BSCoreTelephonyUtilities .cxx_destruct]
+ -[BSCoreTelephonyUtilities activeSubscriptionsDidChange]
+ -[BSCoreTelephonyUtilities coreTelephonyClient]
+ -[BSCoreTelephonyUtilities coreTelephonyQueue]
+ -[BSCoreTelephonyUtilities defaultSubscriptionContextFromSubscriptionInfo]
+ -[BSCoreTelephonyUtilities dualSimCapabilityDidChange]
+ -[BSCoreTelephonyUtilities init]
+ -[BSCoreTelephonyUtilities isRCSChatBot:]
+ -[BSCoreTelephonyUtilities lock]
+ -[BSCoreTelephonyUtilities setCoreTelephonyClient:]
+ -[BSCoreTelephonyUtilities setCoreTelephonyQueue:]
+ -[BSCoreTelephonyUtilities setLock:]
+ -[BSCoreTelephonyUtilities setSubscriptionInfo:]
+ -[BSCoreTelephonyUtilities subscriptionContextForSimID:]
+ -[BSCoreTelephonyUtilities subscriptionFilterPredicate]
+ -[BSCoreTelephonyUtilities subscriptionInfoDidChange]
+ -[BSCoreTelephonyUtilities subscriptionInfo]
+ -[BSCoreTelephonyUtilities subscriptionsFromInfo:]
+ _OBJC_CLASS_$_BSCoreTelephonyUtilities
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_BSCoreTelephonyUtilities._coreTelephonyClient
+ _OBJC_IVAR_$_BSCoreTelephonyUtilities._coreTelephonyQueue
+ _OBJC_IVAR_$_BSCoreTelephonyUtilities._lock
+ _OBJC_IVAR_$_BSCoreTelephonyUtilities._subscriptionInfo
+ _OBJC_METACLASS_$_BSCoreTelephonyUtilities
+ __NSConcreteGlobalBlock
+ __OBJC_$_INSTANCE_METHODS_BSCoreTelephonyUtilities
+ __OBJC_$_INSTANCE_VARIABLES_BSCoreTelephonyUtilities
+ __OBJC_$_PROP_LIST_BSCoreTelephonyUtilities
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BSCoreTelephonyUtilities
+ __OBJC_CLASS_RO_$_BSCoreTelephonyUtilities
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientDelegate
+ __OBJC_METACLASS_RO_$_BSCoreTelephonyUtilities
+ __OBJC_PROTOCOL_$_CoreTelephonyClientDelegate
+ ___55-[BSCoreTelephonyUtilities subscriptionFilterPredicate]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e58_B24?0"CTXPCServiceSubscriptionContext"8"NSDictionary"16l
+ ___block_literal_global
+ __os_log_debug_impl
+ __os_log_default
+ __os_log_error_impl
+ _dispatch_queue_create
+ _objc_enumerationMutation
+ _objc_msgSend$boolValue
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getSubscriptionInfoWithError:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$isSimHidden
+ _objc_msgSend$labelID
+ _objc_msgSend$lock
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$subscriptionFilterPredicate
+ _objc_msgSend$subscriptionInfo
+ _objc_msgSend$subscriptionsFromInfo:
+ _objc_msgSend$subscriptionsInUse
+ _objc_msgSend$unlock
+ _objc_msgSend$userDefaultVoice
- -[IMSharedUtilitiesSoftLinkingWrapper defaultSubscriptionContextFromSubscriptionInfo]
- -[IMSharedUtilitiesSoftLinkingWrapper isRCSChatBot:]
- -[IMSharedUtilitiesSoftLinkingWrapper subscriptionContextForSimID:]
- _OBJC_CLASS_$_IMSharedUtilitiesSoftLinkingWrapper
- _OBJC_METACLASS_$_IMSharedUtilitiesSoftLinkingWrapper
- __OBJC_$_INSTANCE_METHODS_IMSharedUtilitiesSoftLinkingWrapper
- __OBJC_CLASS_RO_$_IMSharedUtilitiesSoftLinkingWrapper
- __OBJC_METACLASS_RO_$_IMSharedUtilitiesSoftLinkingWrapper
CStrings:
+ "\x04"
+ "@\"CTXPCServiceSubscriptionInfo\""
+ "@\"CoreTelephonyClient\""
+ "@\"NSLock\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "B24@?0@\"CTXPCServiceSubscriptionContext\"8@\"NSDictionary\"16"
+ "BSCoreTelephonyUtilities"
+ "CoreTelephonyClientDelegate"
+ "Failed to get subscription info from CoreTelephony"
+ "Found subscription context %@ for SIM ID: %@ "
+ "SIM ID given is nil %@ "
+ "T@\"CTXPCServiceSubscriptionInfo\",&,N,V_subscriptionInfo"
+ "T@\"CoreTelephonyClient\",&,N,V_coreTelephonyClient"
+ "T@\"NSLock\",&,N,V_lock"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_coreTelephonyQueue"
+ "_coreTelephonyClient"
+ "_coreTelephonyQueue"
+ "_lock"
+ "_subscriptionInfo"
+ "activeSubscriptionsDidChange"
+ "boolValue"
+ "com.apple.businessservicesd.coretelephony"
+ "coreTelephonyClient"
+ "coreTelephonyQueue"
+ "countByEnumeratingWithState:objects:count:"
+ "dualSimCapabilityDidChange"
+ "filteredArrayUsingPredicate:"
+ "isSimHidden"
+ "lock"
+ "predicateWithBlock:"
+ "setCoreTelephonyClient:"
+ "setCoreTelephonyQueue:"
+ "setLock:"
+ "setSubscriptionInfo:"
+ "simLessSubscriptionsDidChange"
+ "subscriptionFilterPredicate"
+ "subscriptionInfo"
+ "subscriptionInfoDidChange"
+ "subscriptionsFromInfo:"
+ "subscriptionsInUse"
+ "unlock"
+ "userDefaultVoice"
+ "v24@0:8@16"
- "IMSharedUtilitiesSoftLinkingWrapper"

```
