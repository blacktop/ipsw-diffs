## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

```diff

-12.1.17.0.0
-  __TEXT.__text: 0x82b14
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0xabfc
-  __TEXT.__const: 0x2d0
+12.2.9.1.0
+  __TEXT.__text: 0x83964
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_methlist: 0xacdc
+  __TEXT.__const: 0x360
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__cstring: 0x5330
-  __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_typeref: 0x26
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x31
+  __TEXT.__cstring: 0x53e8
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_typeref: 0x59
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x64
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__oslogstring: 0x4720
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_fieldmd: 0x50
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__oslogstring: 0x487a
   __TEXT.__gcc_except_tab: 0x1048
-  __TEXT.__unwind_info: 0x2728
+  __TEXT.__unwind_info: 0x2768
+  __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x18ac
-  __TEXT.__objc_methname: 0x145b8
-  __TEXT.__objc_methtype: 0x34f0
-  __TEXT.__objc_stubs: 0x8700
-  __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x2788
+  __TEXT.__objc_methname: 0x147d9
+  __TEXT.__objc_methtype: 0x3534
+  __TEXT.__objc_stubs: 0x87c0
+  __DATA_CONST.__got: 0x628
+  __DATA_CONST.__const: 0x2800
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4400
+  __DATA_CONST.__objc_selrefs: 0x4460
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6800
-  __AUTH_CONST.__objc_const: 0x15740
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0x68e0
+  __AUTH_CONST.__objc_const: 0x15848
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x16d0
-  __DATA.__objc_ivar: 0xd34
+  __DATA.__objc_ivar: 0xd44
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_ivar: 0x19c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 19A07092-E4E7-3AED-9829-54F74D76B1A9
-  Functions: 4337
-  Symbols:   13225
-  CStrings:  6346
+  UUID: 732FE96A-0EBE-3EF0-90B1-335FE5718DE7
+  Functions: 4372
+  Symbols:   13298
+  CStrings:  6379
 
Symbols:
+ -[ASDAppCapabilityMetadata isCustomBrowserEngineApp]
+ -[ASDAppCapabilityMetadata setIsCustomBrowserEngineApp:]
+ -[ASDAppCapabilityMetadata setSupportsAlternativeAppDistribution:]
+ -[ASDAppCapabilityMetadata setUsesNonWebKitBrowserEngines:]
+ -[ASDAppCapabilityMetadata setUsesNonWebKitBrowserEnginesAsSteward:]
+ -[ASDAppCapabilityMetadata setusesNonWebKitBrowserEngines:]
+ -[ASDAppCapabilityMetadata supportsAlternativeAppDistribution]
+ -[ASDAppCapabilityMetadata usesNonWebKitBrowserEnginesAsSteward]
+ -[ASDAppCapabilityMetadata usesNonWebKitBrowserEngines]
+ -[ASDAppStoreService revokeAppConsentForAccountID:itemID:account:completionBlock:]
+ -[ASDPurchaseHistoryApp hasAnyVersionThatRunsOnIntel]
+ -[ASDPurchaseHistoryApp setHasAnyVersionThatRunsOnIntel:]
+ -[ASDSystemAppMetadata ageRatingValue]
+ -[ASDSystemAppMetadata isDefaultBrowser]
+ -[ASDSystemAppMetadata setAgeRatingValue:]
+ -[ASDSystemAppMetadata setIsDefaultBrowser:]
+ -[ASDSystemAppMetadata setShouldAskForRatingException:]
+ -[ASDSystemAppMetadata shouldAskForRatingException]
+ _OBJC_IVAR_$_ASDAppCapabilityMetadata._usesNonWebKitBrowserEngines
+ _OBJC_IVAR_$_ASDPurchaseHistoryApp._hasAnyVersionThatRunsOnIntel
+ _OBJC_IVAR_$_ASDSystemAppMetadata._ageRatingValue
+ _OBJC_IVAR_$_ASDSystemAppMetadata._isDefaultBrowser
+ _OBJC_IVAR_$_ASDSystemAppMetadata._shouldAskForRatingException
+ ___75-[ASDAppStoreService _handleNotificationRefresh:addedBadges:removedBadges:]_block_invoke.60
+ ___75-[ASDAppStoreService _handleNotificationRefresh:addedBadges:removedBadges:]_block_invoke.63
+ ___82-[ASDAppStoreService revokeAppConsentForAccountID:itemID:account:completionBlock:]_block_invoke
+ ___82-[ASDAppStoreService revokeAppConsentForAccountID:itemID:account:completionBlock:]_block_invoke.31
+ ___82-[ASDAppStoreService revokeAppConsentForAccountID:itemID:account:completionBlock:]_block_invoke.32
+ ___82-[ASDAppStoreService revokeAppConsentForAccountID:itemID:account:completionBlock:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e70_v24?0"<ASDAppStoreServiceProtocol><NSXPCProxyCreating>"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___swift_memcpy25_8
+ __swiftEmptyArrayStorage
+ _get_enum_tag_for_layout_string So24ASDAppCapabilityMetadataC14AppStoreDaemonE0B0O
+ _objc_msgSend$revokeAppConsentForAccountID:itemID:account:completionHandler:
+ _objc_msgSend$setIsCustomBrowserEngineApp:
+ _objc_msgSend$setSupportsAlternativeAppDistribution:
+ _objc_msgSend$setUsesNonWebKitBrowserEngines:
+ _objc_msgSend$supportsAlternativeAppDistribution
+ _objc_msgSend$usesNonWebKitBrowserEngines
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _symbolic SS
+ _symbolic SS_SaySSGt
+ _symbolic So24ASDAppCapabilityMetadataC
+ _symbolic _____ So24ASDAppCapabilityMetadataC14AppStoreDaemonE0B0O
+ _type_layout_string So24ASDAppCapabilityMetadataC14AppStoreDaemonE0B0O
- _OBJC_IVAR_$_ASDAppCapabilityMetadata._supportsFeatureC
- ___75-[ASDAppStoreService _handleNotificationRefresh:addedBadges:removedBadges:]_block_invoke.55
- ___75-[ASDAppStoreService _handleNotificationRefresh:addedBadges:removedBadges:]_block_invoke.58
CStrings:
+ "AFE"
+ "AR"
+ "DB"
+ "TB,N,V_usesNonWebKitBrowserEngines"
+ "TB,V_hasAnyVersionThatRunsOnIntel"
+ "[%{public}@] FRevoked consent failed for rescindDSID: %{public}@ itemID: %{public}@ error: %{public}@"
+ "[%{public}@] Revoked consent failed for rescindDSID: %{public}@ itemID: %{public}@ error: %{public}@"
+ "[%{public}@] Revoked consent failed with error: %{public}@"
+ "[%{public}@] Revoked consent success for rescindDSID: %{public}@ itemID: %{public}@"
+ "_hasAnyVersionThatRunsOnIntel"
+ "_usesNonWebKitBrowserEngines"
+ "first-party-non-webkit-browser-engine"
+ "first-party-uses-non-webkit-browser-engine"
+ "hasAnyVersionThatRunsOnIntel"
+ "revokeAppConsentForAccountID:itemID:account:completionBlock:"
+ "revokeAppConsentForAccountID:itemID:account:completionHandler:"
+ "setHasAnyVersionThatRunsOnIntel:"
+ "setIsCustomBrowserEngineApp:"
+ "setSupportsAlternativeAppDistribution:"
+ "setUsesNonWebKitBrowserEngines:"
+ "setUsesNonWebKitBrowserEnginesAsSteward:"
+ "setusesNonWebKitBrowserEngines:"
+ "supportsAlternativeAppDistribution"
+ "third-party-non-webkit-browser-engine"
+ "third-party-uses-non-webkit-browser-engine"
+ "usesNonWebKitBrowserEngines"
+ "usesNonWebKitBrowserEnginesAsSteward"
+ "v48@0:8@\"NSNumber\"16@\"NSNumber\"24@\"ACAccount\"32@?<v@?B@\"NSError\">40"
- "TB,N,V_supportsFeatureC"
- "_supportsFeatureC"

```
