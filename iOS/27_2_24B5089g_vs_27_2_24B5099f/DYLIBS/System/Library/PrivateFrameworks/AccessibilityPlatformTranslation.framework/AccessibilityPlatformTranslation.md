## AccessibilityPlatformTranslation

> `/System/Library/PrivateFrameworks/AccessibilityPlatformTranslation.framework/AccessibilityPlatformTranslation`

```diff

-591.4.2.0.0
-  __TEXT.__text: 0x151e4
-  __TEXT.__objc_methlist: 0x11dc
+591.4.4.0.0
+  __TEXT.__text: 0x1626c
+  __TEXT.__objc_methlist: 0x1354
   __TEXT.__const: 0x5d8
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__gcc_except_tab: 0x2a0
-  __TEXT.__cstring: 0x26ae
-  __TEXT.__oslogstring: 0x6ab
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__cstring: 0x26b1
+  __TEXT.__oslogstring: 0x726
+  __TEXT.__unwind_info: 0x640
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe70
+  __DATA_CONST.__objc_selrefs: 0xf18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x4b8
-  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__got: 0x390
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x2680
-  __AUTH_CONST.__objc_const: 0x1430
+  __AUTH_CONST.__objc_const: 0x17c0
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x108
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 429
-  Symbols:   933
-  CStrings:  406
+  Functions: 458
+  Symbols:   992
+  CStrings:  408
 
Symbols:
+ -[AXPRemoteCacheManager _runtimeDelegateToken]
+ -[AXPRemoteCacheManager dealloc]
+ -[AXPRemoteCacheManager set_runtimeDelegateToken:]
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
+ GCC_except_table225
+ GCC_except_table235
+ GCC_except_table243
+ GCC_except_table347
+ _OBJC_CLASS_$_AXPRuntimeDelegateRegistration
+ _OBJC_CLASS_$_AXPTokenDelegateRegistration
+ _OBJC_IVAR_$_AXPRemoteCacheManager.__runtimeDelegateToken
+ _OBJC_IVAR_$_AXPRuntimeDelegateRegistration._cachedTreeClientType
+ _OBJC_IVAR_$_AXPRuntimeDelegateRegistration._delegate
+ _OBJC_IVAR_$_AXPRuntimeDelegateRegistration._requestResolvingBehavior
+ _OBJC_IVAR_$_AXPTokenDelegateRegistration._cachedTreeClientType
+ _OBJC_IVAR_$_AXPTokenDelegateRegistration._delegate
+ _OBJC_IVAR_$_AXPTokenDelegateRegistration._requestResolvingBehavior
+ _OBJC_IVAR_$_AXPTranslator._authoritativeBridgeDelegateToken
+ _OBJC_IVAR_$_AXPTranslator._authoritativeRuntimeDelegateToken
+ _OBJC_IVAR_$_AXPTranslator._bridgeDelegateAuthorityGeneration
+ _OBJC_IVAR_$_AXPTranslator._bridgeDelegateTokenToRegistrationLookup
+ _OBJC_IVAR_$_AXPTranslator._registrationLookupLock
+ _OBJC_IVAR_$_AXPTranslator._runtimeDelegateAuthorityGeneration
+ _OBJC_IVAR_$_AXPTranslator._runtimeDelegateTokenToRegistrationLookup
+ _OBJC_METACLASS_$_AXPRuntimeDelegateRegistration
+ _OBJC_METACLASS_$_AXPTokenDelegateRegistration
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
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table223
- GCC_except_table227
- GCC_except_table240
- GCC_except_table318
CStrings:
+ "Bridge delegate for token %@ is registered but has been deallocated!"
+ "No delegate available to service request for token %@"
+ "r\""
- "\"\""
```
