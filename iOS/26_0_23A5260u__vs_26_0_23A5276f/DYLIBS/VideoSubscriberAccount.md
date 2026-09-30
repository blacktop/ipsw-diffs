## VideoSubscriberAccount

> `/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`

```diff

-587.0.0.0.0
-  __TEXT.__text: 0xd8b8c
+590.0.0.0.1
+  __TEXT.__text: 0xd87d4
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x895c
-  __TEXT.__const: 0x10f80
-  __TEXT.__cstring: 0x9f36
-  __TEXT.__oslogstring: 0x5baa
+  __TEXT.__objc_methlist: 0x88b4
+  __TEXT.__const: 0x10f90
+  __TEXT.__cstring: 0x9e76
+  __TEXT.__oslogstring: 0x5caa
   __TEXT.__gcc_except_tab: 0x1634
   __TEXT.__ustring: 0x178
   __TEXT.__dlopen_cstrs: 0x47

   __TEXT.__swift5_capture: 0x194
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2b38
+  __TEXT.__unwind_info: 0x2b28
   __TEXT.__eh_frame: 0xe18
-  __TEXT.__objc_classname: 0x1366
-  __TEXT.__objc_methname: 0x1252c
+  __TEXT.__objc_classname: 0x1364
+  __TEXT.__objc_methname: 0x122ad
   __TEXT.__objc_methtype: 0x1eb9
-  __TEXT.__objc_stubs: 0xbdc0
+  __TEXT.__objc_stubs: 0xbc60
   __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x2620
+  __DATA_CONST.__const: 0x2628
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4080
+  __DATA_CONST.__objc_selrefs: 0x4020
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xa40
   __AUTH_CONST.__const: 0x7cc8
-  __AUTH_CONST.__cfstring: 0x8300
-  __AUTH_CONST.__objc_const: 0x16738
+  __AUTH_CONST.__cfstring: 0x82a0
+  __AUTH_CONST.__objc_const: 0x165e8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x340
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x92c
+  __DATA.__objc_ivar: 0x910
   __DATA.__data: 0x1360
   __DATA.__bss: 0x1ea0
   __DATA.__common: 0xa38

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0BDAC8DE-6CBA-376A-8112-424DCE061A63
-  Functions: 4404
-  Symbols:   12208
-  CStrings:  6389
+  UUID: 5C1C7456-E77A-3A1D-8B50-DA59F8188103
+  Functions: 4386
+  Symbols:   12147
+  CStrings:  6361
 
Symbols:
+ -[VSBindingInfo requireExpectedConcurrency].cold.1
+ -[VSIdentityProviderInfoCenter _fetch:]
+ ___36-[VSIdentityProviderInfoCenter init]_block_invoke.52
+ ___36-[VSIdentityProviderInfoCenter init]_block_invoke.52.cold.1
+ ___39-[VSIdentityProviderInfoCenter _fetch:]_block_invoke
+ ___39-[VSIdentityProviderInfoCenter _fetch:]_block_invoke_2
+ ___39-[VSIdentityProviderInfoCenter _fetch:]_block_invoke_3
+ ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.98
+ ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.98.cold.1
+ ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.99
+ ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.99.cold.1
+ ___block_descriptor_40_e8_32bs_e55_v24?0"VSIdentityProviderInfoQueryResult"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e53_v32?0"VSIdentityProvider"8"NSString"16"NSError"24ls48l8s32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.48
+ _objc_msgSend$_fetch:
- -[VSIdentityProviderInfoCenter _refresh:]
- -[VSIdentityProviderInfoCenter cachedDesignatedAppBundleIdentifier]
- -[VSIdentityProviderInfoCenter cachedIdentityProvider]
- -[VSIdentityProviderInfoCenter cachedIsSetTopBox]
- -[VSIdentityProviderInfoCenter currentError]
- -[VSIdentityProviderInfoCenter ignoredFirstNotification]
- -[VSIdentityProviderInfoCenter serialQueue]
- -[VSIdentityProviderInfoCenter setCachedDesignatedAppBundleIdentifier:]
- -[VSIdentityProviderInfoCenter setCachedIdentityProvider:]
- -[VSIdentityProviderInfoCenter setCachedIsSetTopBox:]
- -[VSIdentityProviderInfoCenter setCurrentError:]
- -[VSIdentityProviderInfoCenter setIgnoredFirstNotification:]
- -[VSIdentityProviderInfoCenter setSerialQueue:]
- -[VSIdentityProviderInfoCenter setSetupCompleted:]
- -[VSIdentityProviderInfoCenter setupCompleted]
- GCC_except_table54
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._cachedDesignatedAppBundleIdentifier
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._cachedIdentityProvider
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._cachedIsSetTopBox
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._currentError
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._ignoredFirstNotification
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._serialQueue
- _OBJC_IVAR_$_VSIdentityProviderInfoCenter._setupCompleted
- ___36-[VSIdentityProviderInfoCenter init]_block_invoke.56
- ___36-[VSIdentityProviderInfoCenter init]_block_invoke.56.cold.1
- ___41-[VSIdentityProviderInfoCenter _refresh:]_block_invoke
- ___41-[VSIdentityProviderInfoCenter _refresh:]_block_invoke.88
- ___41-[VSIdentityProviderInfoCenter _refresh:]_block_invoke.88.cold.1
- ___41-[VSIdentityProviderInfoCenter _refresh:]_block_invoke_2
- ___41-[VSIdentityProviderInfoCenter _refresh:]_block_invoke_2.cold.1
- ___54-[VSIdentityProviderInfoCenter _accountStoreDidChange]_block_invoke
- ___59-[VSIdentityProviderInfoCenter _developerSettingsDidChange]_block_invoke
- ___63-[VSIdentityProviderInfoCenter enqueueInfoQueryWithCompletion:]_block_invoke_2
- ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.105
- ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.105.cold.1
- ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.106
- ___64-[VSIdentityProviderInfoCenter fetchAccountAndIdentityProvider:]_block_invoke.106.cold.1
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e53_v32?0"VSIdentityProvider"8"NSString"16"NSError"24ls32l8s40l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.52
- ___block_literal_global.59
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_VideoSubscriberAccount
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_VideoSubscriberAccount
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_VideoSubscriberAccount
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_VideoSubscriberAccount
- _objc_msgSend$_refresh:
- _objc_msgSend$cachedDesignatedAppBundleIdentifier
- _objc_msgSend$cachedIdentityProvider
- _objc_msgSend$currentError
- _objc_msgSend$ignoredFirstNotification
- _objc_msgSend$setCachedDesignatedAppBundleIdentifier:
- _objc_msgSend$setCachedIdentityProvider:
- _objc_msgSend$setCachedIsSetTopBox:
- _objc_msgSend$setCurrentError:
- _objc_msgSend$setIgnoredFirstNotification:
- _objc_msgSend$setSetupCompleted:
- _objc_msgSend$setupCompleted
CStrings:
+ "Running on underlying queue %@ instead of required underlying queue %@"
+ "_fetch:"
+ "v24@?0@\"VSIdentityProviderInfoQueryResult\"8@\"NSError\"16"
+ "will return identity provider info result: %@"
- "Error fetching STB profile %@"
- "Error fetching bundle ID %@"
- "IdentityProviderInfoCenter"
- "T@\"NSError\",&,N,V_currentError"
- "T@\"NSString\",&,N,V_cachedDesignatedAppBundleIdentifier"
- "T@\"VSIdentityProvider\",&,N,V_cachedIdentityProvider"
- "TB,N,V_cachedIsSetTopBox"
- "TB,N,V_ignoredFirstNotification"
- "TB,N,V_setupCompleted"
- "_cachedDesignatedAppBundleIdentifier"
- "_cachedIdentityProvider"
- "_cachedIsSetTopBox"
- "_currentError"
- "_ignoredFirstNotification"
- "_refresh:"
- "_setupCompleted"
- "cachedDesignatedAppBundleIdentifier"
- "cachedIdentityProvider"
- "cachedIsSetTopBox"
- "currentError"
- "ignoredFirstNotification"
- "setCachedDesignatedAppBundleIdentifier:"
- "setCachedIdentityProvider:"
- "setCachedIsSetTopBox:"
- "setCurrentError:"
- "setIgnoredFirstNotification:"
- "setSetupCompleted:"
- "setupCompleted"

```
