## AccessibilityPlatformTranslation

> `/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/Versions/A/AccessibilityPlatformTranslation`

```diff

-587.0.0.0.0
-  __TEXT.__text: 0x24968
-  __TEXT.__objc_methlist: 0x185c
-  __TEXT.__const: 0x618
+591.4.5.0.0
+  __TEXT.__text: 0x263c4
+  __TEXT.__objc_methlist: 0x19b4
+  __TEXT.__const: 0x620
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__oslogstring: 0x7d8
-  __TEXT.__cstring: 0x32ea
-  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__oslogstring: 0x853
+  __TEXT.__cstring: 0x32ec
+  __TEXT.__unwind_info: 0x708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x758
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x13b8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x4b8
-  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__got: 0x830
   __AUTH_CONST.__const: 0xae0
   __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x17a8
+  __AUTH_CONST.__objc_const: 0x1b08
   __AUTH_CONST.__objc_intobj: 0x15f0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x124
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x360
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   1901
-  CStrings:  539
+  Functions: 649
+  Symbols:   1971
+  CStrings:  541
 
Symbols:
+ -[AXPHostCacheManager dealloc]
+ -[AXPRuntimeDelegateRegistration .cxx_destruct]
+ -[AXPRuntimeDelegateRegistration cachedTreeClientType]
+ -[AXPRuntimeDelegateRegistration delegate]
+ -[AXPRuntimeDelegateRegistration requestResolvingBehavior]
+ -[AXPRuntimeDelegateRegistration setCachedTreeClientType:]
+ -[AXPRuntimeDelegateRegistration setDelegate:]
+ -[AXPRuntimeDelegateRegistration setRequestResolvingBehavior:]
+ -[AXPTokenDelegateRegistration .cxx_destruct]
+ -[AXPTokenDelegateRegistration cachedTreeClientType]
+ -[AXPTokenDelegateRegistration delegate]
+ -[AXPTokenDelegateRegistration requestResolvingBehavior]
+ -[AXPTokenDelegateRegistration setCachedTreeClientType:]
+ -[AXPTokenDelegateRegistration setDelegate:]
+ -[AXPTokenDelegateRegistration setRequestResolvingBehavior:]
+ -[AXPTranslator bridgeDelegateTokenToRegistrationLookup]
+ -[AXPTranslator broadcastNotification:data:associatedObject:]
+ -[AXPTranslator hasRegisteredRuntimeDelegates]
+ -[AXPTranslator registerBridgeTokenDelegate:requestResolvingBehavior:cachedTreeClientType:forToken:]
+ -[AXPTranslator registerRuntimeDelegate:requestResolvingBehavior:cachedTreeClientType:forToken:]
+ -[AXPTranslator requestResolvingBehaviorForBridgeDelegateToken:]
+ -[AXPTranslator runtimeDelegateTokenToRegistrationLookup]
+ -[AXPTranslator setBridgeDelegateTokenToRegistrationLookup:]
+ -[AXPTranslator setRuntimeDelegateTokenToRegistrationLookup:]
+ -[AXPTranslator tokenDelegateForBridgeDelegateToken:]
+ -[AXPTranslator unregisterBridgeDelegateForToken:]
+ -[AXPTranslator unregisterRuntimeDelegateForToken:]
+ GCC_except_table448
+ GCC_except_table535
+ GCC_except_table602
+ OBJC_IVAR_$_AXPRuntimeDelegateRegistration._cachedTreeClientType
+ OBJC_IVAR_$_AXPRuntimeDelegateRegistration._delegate
+ OBJC_IVAR_$_AXPRuntimeDelegateRegistration._requestResolvingBehavior
+ OBJC_IVAR_$_AXPTokenDelegateRegistration._cachedTreeClientType
+ OBJC_IVAR_$_AXPTokenDelegateRegistration._delegate
+ OBJC_IVAR_$_AXPTokenDelegateRegistration._requestResolvingBehavior
+ OBJC_IVAR_$_AXPTranslator._authoritativeBridgeDelegateToken
+ OBJC_IVAR_$_AXPTranslator._authoritativeRuntimeDelegateToken
+ OBJC_IVAR_$_AXPTranslator._bridgeDelegateAuthorityGeneration
+ OBJC_IVAR_$_AXPTranslator._bridgeDelegateTokenToRegistrationLookup
+ OBJC_IVAR_$_AXPTranslator._registrationLookupLock
+ OBJC_IVAR_$_AXPTranslator._runtimeDelegateAuthorityGeneration
+ OBJC_IVAR_$_AXPTranslator._runtimeDelegateTokenToRegistrationLookup
+ _NSAccessibilityIncrementorRole
+ _OBJC_CLASS_$_AXPRuntimeDelegateRegistration
+ _OBJC_CLASS_$_AXPTokenDelegateRegistration
+ _OBJC_METACLASS_$_AXPRuntimeDelegateRegistration
+ _OBJC_METACLASS_$_AXPTokenDelegateRegistration
+ __AXUIElementCopyElementAtPositionInHostedCoordinatesWithParams
+ __OBJC_$_INSTANCE_METHODS_AXPRuntimeDelegateRegistration
+ __OBJC_$_INSTANCE_METHODS_AXPTokenDelegateRegistration
+ __OBJC_$_INSTANCE_VARIABLES_AXPRuntimeDelegateRegistration
+ __OBJC_$_INSTANCE_VARIABLES_AXPTokenDelegateRegistration
+ __OBJC_$_PROP_LIST_AXPRuntimeDelegateRegistration
+ __OBJC_$_PROP_LIST_AXPTokenDelegateRegistration
+ __OBJC_CLASS_RO_$_AXPRuntimeDelegateRegistration
+ __OBJC_CLASS_RO_$_AXPTokenDelegateRegistration
+ __OBJC_METACLASS_RO_$_AXPRuntimeDelegateRegistration
+ __OBJC_METACLASS_RO_$_AXPTokenDelegateRegistration
+ _objc_msgSend$bridgeDelegateTokenToRegistrationLookup
+ _objc_msgSend$broadcastNotification:data:associatedObject:
+ _objc_msgSend$delegate
+ _objc_msgSend$hasRegisteredRuntimeDelegates
+ _objc_msgSend$registerBridgeTokenDelegate:requestResolvingBehavior:cachedTreeClientType:forToken:
+ _objc_msgSend$requestResolvingBehaviorForBridgeDelegateToken:
+ _objc_msgSend$runtimeDelegateTokenToRegistrationLookup
+ _objc_msgSend$setBridgeDelegateTokenToRegistrationLookup:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setRuntimeDelegateTokenToRegistrationLookup:
+ _objc_msgSend$tokenDelegateForBridgeDelegateToken:
+ _objc_msgSend$unregisterBridgeDelegateForToken:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table422
- GCC_except_table509
- GCC_except_table575
CStrings:
+ "Bridge delegate for token %@ is registered but has been deallocated!"
+ "No delegate available to service request for token %@"
+ "r\""
- "\"\""
```
