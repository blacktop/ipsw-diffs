## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-805.0.10.0.0
-  __TEXT.__text: 0x45af0
+805.0.15.0.0
+  __TEXT.__text: 0x467b0
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x442c
+  __TEXT.__objc_methlist: 0x4514
   __TEXT.__gcc_except_tab: 0x1670
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x2b1f
-  __TEXT.__oslogstring: 0x33fd
+  __TEXT.__cstring: 0x2b48
+  __TEXT.__oslogstring: 0x3487
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0x1688
-  __TEXT.__objc_classname: 0xc00
-  __TEXT.__objc_methname: 0x8913
-  __TEXT.__objc_methtype: 0x2166
-  __TEXT.__objc_stubs: 0x6680
-  __DATA_CONST.__got: 0x5d8
-  __DATA_CONST.__const: 0x16a8
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__objc_classname: 0xc19
+  __TEXT.__objc_methname: 0x8b0c
+  __TEXT.__objc_methtype: 0x2182
+  __TEXT.__objc_stubs: 0x67c0
+  __DATA_CONST.__got: 0x5e0
+  __DATA_CONST.__const: 0x16b0
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2088
+  __DATA_CONST.__objc_selrefs: 0x20d8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x2540
-  __AUTH_CONST.__objc_const: 0x84b8
+  __AUTH_CONST.__cfstring: 0x2560
+  __AUTH_CONST.__objc_const: 0x8648
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x558
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x570
   __DATA.__data: 0xe48
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D71CFEB-2DA6-3AB9-8D4A-EB028A5A1D4F
-  Functions: 1915
-  Symbols:   6809
-  CStrings:  3039
+  UUID: 209D5FE5-CE0A-3A97-802A-40A72703499F
+  Functions: 1938
+  Symbols:   6880
+  CStrings:  3063
 
Symbols:
+ +[TKRegisteredTokenManager sharedInstance]
+ -[TKExtensionClientTokenSession _clearCredentialIfNeededForTokenID:inContext:]
+ -[TKExtensionClientTokenSession _clearCredentialIfNeededForTokenID:inContext:].cold.1
+ -[TKExtensionClientTokenSession _updatePINInitialStateWithContext:forToken:]
+ -[TKExtensionClientTokenSession handleErrorForRegisteredSmartcards:forToken:]
+ -[TKExtensionClientTokenSession handleErrorForRegisteredSmartcards:forToken:].cold.1
+ -[TKExtensionClientTokenSession lastUsedRegisteredTokenID]
+ -[TKExtensionClientTokenSession setLastUsedRegisteredTokenID:]
+ -[TKExtensionClientTokenSession setWasPINCredentialInitiallySet:]
+ -[TKExtensionClientTokenSession setWasPINCredentialProvidedByPINUI:]
+ -[TKExtensionClientTokenSession wasPINCredentialInitiallySet]
+ -[TKExtensionClientTokenSession wasPINCredentialProvidedByPINUI]
+ -[TKRegisteredTokenManager .cxx_destruct]
+ -[TKRegisteredTokenManager init]
+ -[TKRegisteredTokenManager lastUsedRegisteredTokenID]
+ -[TKRegisteredTokenManager setLastUsedRegisteredTokenID:]
+ -[TKRegisteredTokenManager setWasPINCredentialInitiallySet:]
+ -[TKRegisteredTokenManager setWasPINCredentialProvidedByPINUI:]
+ -[TKRegisteredTokenManager wasPINCredentialInitiallySet]
+ -[TKRegisteredTokenManager wasPINCredentialProvidedByPINUI]
+ -[TKTokenSession finalizeAuthOperation:evaluatedAuthOperation:reply:].cold.2
+ GCC_except_table43
+ GCC_except_table53
+ GCC_except_table60
+ _OBJC_CLASS_$_TKRegisteredTokenManager
+ _OBJC_IVAR_$_TKExtensionClientTokenSession._authenticationContextWasProvidedByCaller
+ _OBJC_IVAR_$_TKExtensionClientTokenSession._tokenManager
+ _OBJC_IVAR_$_TKRegisteredTokenManager._lastUsedRegisteredTokenID
+ _OBJC_IVAR_$_TKRegisteredTokenManager._lock
+ _OBJC_IVAR_$_TKRegisteredTokenManager._wasPINCredentialInitiallySet
+ _OBJC_IVAR_$_TKRegisteredTokenManager._wasPINCredentialProvidedByPINUI
+ _OBJC_METACLASS_$_TKRegisteredTokenManager
+ _TKClientTokenParameterAuthenticationContextProvidedBySecCaller
+ __OBJC_$_CLASS_METHODS_TKRegisteredTokenManager
+ __OBJC_$_INSTANCE_METHODS_TKRegisteredTokenManager
+ __OBJC_$_INSTANCE_VARIABLES_TKRegisteredTokenManager
+ __OBJC_$_PROP_LIST_TKRegisteredTokenManager
+ __OBJC_CLASS_RO_$_TKRegisteredTokenManager
+ __OBJC_METACLASS_RO_$_TKRegisteredTokenManager
+ ___42+[TKRegisteredTokenManager sharedInstance]_block_invoke
+ ___block_descriptor_80_e8_32s40s48bs56r64r_e40_32?0"<TKClientTokenProtocol>"8q16^24ls32l8s48l8r56l8r64l8s40l8
+ ___block_literal_global.115
+ ___block_literal_global.177
+ _objc_msgSend$_clearCredentialIfNeededForTokenID:inContext:
+ _objc_msgSend$_updatePINInitialStateWithContext:forToken:
+ _objc_msgSend$handleErrorForRegisteredSmartcards:forToken:
+ _objc_msgSend$lastUsedRegisteredTokenID
+ _objc_msgSend$setLastUsedRegisteredTokenID:
+ _objc_msgSend$setWasPINCredentialInitiallySet:
+ _objc_msgSend$setWasPINCredentialProvidedByPINUI:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$wasPINCredentialInitiallySet
+ _objc_msgSend$wasPINCredentialProvidedByPINUI
+ _sharedInstance.onceToken
+ _sharedInstance.shared
- GCC_except_table34
- GCC_except_table37
- GCC_except_table38
- ___block_descriptor_72_e8_32s40bs48r56r_e40_32?0"<TKClientTokenProtocol>"8q16^24ls32l8s40l8r48l8r56l8
- ___block_literal_global.114
- ___block_literal_global.160
CStrings:
+ "@\"TKRegisteredTokenManager\""
+ "Deleting set PIN credential due to auth error: %@"
+ "Deleting set PIN credential due to tokenID change"
+ "PIN was set for registered smart card"
+ "T@\"NSString\",C,N"
+ "TKRegisteredTokenManager"
+ "_authenticationContextWasProvidedByCaller"
+ "_clearCredentialIfNeededForTokenID:inContext:"
+ "_lastUsedRegisteredTokenID"
+ "_lock"
+ "_tokenManager"
+ "_updatePINInitialStateWithContext:forToken:"
+ "_wasPINCredentialInitiallySet"
+ "_wasPINCredentialProvidedByPINUI"
+ "authenticationContextProvidedBySecCaller"
+ "handleErrorForRegisteredSmartcards:forToken:"
+ "lastUsedRegisteredTokenID"
+ "setLastUsedRegisteredTokenID:"
+ "setWasPINCredentialInitiallySet:"
+ "setWasPINCredentialProvidedByPINUI:"
+ "sharedInstance"
+ "wasPINCredentialInitiallySet"
+ "wasPINCredentialProvidedByPINUI"

```
