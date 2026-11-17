## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4838.60.42.0.0
-  __TEXT.__text: 0xa643d8
-  __TEXT.__objc_methlist: 0x9bbc
-  __TEXT.__const: 0x2e690
-  __TEXT.__cstring: 0x50175
-  __TEXT.__oslogstring: 0x21b32
-  __TEXT.__gcc_except_tab: 0xda40
+4838.60.55.0.0
+  __TEXT.__text: 0xa6ae20
+  __TEXT.__objc_methlist: 0x9c3c
+  __TEXT.__const: 0x2e6a0
+  __TEXT.__cstring: 0x50215
+  __TEXT.__oslogstring: 0x21cc2
+  __TEXT.__gcc_except_tab: 0xdac0
   __TEXT.__ustring: 0x180e
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__constg_swiftt: 0x14a08
+  __TEXT.__constg_swiftt: 0x14a40
   __TEXT.__swift5_typeref: 0x14d8a
   __TEXT.__swift5_builtin: 0x910
-  __TEXT.__swift5_reflstr: 0xfb3d
-  __TEXT.__swift5_fieldmd: 0xd31c
+  __TEXT.__swift5_reflstr: 0xfb6d
+  __TEXT.__swift5_fieldmd: 0xd334
   __TEXT.__swift5_mpenum: 0x154
   __TEXT.__swift5_assocty: 0x29f0
-  __TEXT.__swift5_capture: 0x1ab3c
+  __TEXT.__swift5_capture: 0x1ad24
   __TEXT.__swift5_proto: 0x1cc4
   __TEXT.__swift5_types: 0xc64
   __TEXT.__swift5_types2: 0x8

   __TEXT.__swift_as_ret: 0x188
   __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x1c138
-  __TEXT.__eh_frame: 0x2d0b0
+  __TEXT.__unwind_info: 0x1c1d8
+  __TEXT.__eh_frame: 0x2d178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6478
+  __DATA_CONST.__objc_selrefs: 0x64e0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2a8
-  __DATA_CONST.__objc_arraydata: 0x138
+  __DATA_CONST.__objc_arraydata: 0x140
   __DATA_CONST.__got: 0x1948
-  __AUTH_CONST.__const: 0x4cc20
-  __AUTH_CONST.__cfstring: 0x7940
-  __AUTH_CONST.__objc_const: 0x28438
+  __AUTH_CONST.__const: 0x4cfa8
+  __AUTH_CONST.__cfstring: 0x79a0
+  __AUTH_CONST.__objc_const: 0x28540
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x3180
+  __AUTH_CONST.__auth_got: 0x3190
   __AUTH.__objc_data: 0x1ca8
   __AUTH.__data: 0x28a8
-  __DATA.__objc_ivar: 0xc0c
+  __DATA.__objc_ivar: 0xc18
   __DATA.__data: 0x82a0
   __DATA.__common: 0x21b
-  __DATA_DIRTY.__objc_data: 0x34b0
-  __DATA_DIRTY.__data: 0x10eb0
+  __DATA_DIRTY.__objc_data: 0x34d0
+  __DATA_DIRTY.__data: 0x10ee0
   __DATA_DIRTY.__bss: 0x10198
   __DATA_DIRTY.__common: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31855
-  Symbols:   12761
-  CStrings:  8366
+  Functions: 31922
+  Symbols:   12780
+  CStrings:  8375
 
Symbols:
+ -[FPDDomainIndexerState donatedRootKey]
+ -[FPDDomainIndexerState setDonatedRootKey:]
+ -[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:additionalProviders:]
+ -[FPDExtensionManager _updateProviderListForMatchingExtensionRecords:offloadedExtensionRecords:]
+ -[FPDExtensionManager offloadedExtensionRecords]
+ -[FPDExtensionManager offloadedProvidersForExtensionRecords:]
+ -[FPDProvider _refreshDomainRootsIfDomainNameVisibilityChangedFrom:]
+ -[FPDProviderDescriptor initWithPlaceholderExtensionRecord:]
+ -[FPDProviderDescriptor owningApplicationIsOffloaded]
+ -[FPDProviderDescriptor setOwningApplicationIsOffloaded:]
+ GCC_except_table97
+ _FPFeatureFlagIndexDomainRootLocationsIsEnabled
+ _FPIsFileProviderExtensionRecordIncludingOffloaded
+ _OBJC_IVAR_$_FPDDomainIndexerState._donatedRootKeyURL
+ _OBJC_IVAR_$_FPDExtensionManager._offloadedProviderUUIDs
+ _OBJC_IVAR_$_FPDProviderDescriptor._owningApplicationIsOffloaded
+ ___49-[FPDExtensionManager synchronousProviderUpdate:]_block_invoke_3
+ ___61-[FPDExtensionManager offloadedProvidersForExtensionRecords:]_block_invoke
+ ___87-[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:additionalProviders:]_block_invoke
+ ___87-[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:additionalProviders:]_block_invoke_2
+ ___96-[FPDExtensionManager _updateProviderListForMatchingExtensionRecords:offloadedExtensionRecords:]_block_invoke
+ ___block_descriptor_99_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ ___swift_closure_destructor.100Tm
+ ___swift_closure_destructor.113Tm
+ ___swift_closure_destructor.121Tm
+ ___swift_closure_destructor.141Tm
+ ___swift_closure_destructor.151Tm
+ ___swift_closure_destructor.155Tm
+ ___swift_closure_destructor.1591Tm
+ ___swift_closure_destructor.160Tm
+ ___swift_closure_destructor.172Tm
+ ___swift_closure_destructor.1733Tm
+ ___swift_closure_destructor.1753Tm
+ ___swift_closure_destructor.1760Tm
+ ___swift_closure_destructor.1776Tm
+ ___swift_closure_destructor.185Tm
+ ___swift_closure_destructor.189Tm
+ ___swift_closure_destructor.1958Tm
+ ___swift_closure_destructor.210Tm
+ ___swift_closure_destructor.217Tm
+ ___swift_closure_destructor.224Tm
+ ___swift_closure_destructor.231Tm
+ ___swift_closure_destructor.244Tm
+ ___swift_closure_destructor.2518Tm
+ ___swift_closure_destructor.256Tm
+ ___swift_closure_destructor.263Tm
+ ___swift_closure_destructor.266Tm
+ ___swift_closure_destructor.281Tm
+ ___swift_closure_destructor.2825Tm
+ ___swift_closure_destructor.2938Tm
+ ___swift_closure_destructor.293Tm
+ ___swift_closure_destructor.302Tm
+ ___swift_closure_destructor.3075Tm
+ ___swift_closure_destructor.3082Tm
+ ___swift_closure_destructor.3095Tm
+ ___swift_closure_destructor.3169Tm
+ ___swift_closure_destructor.317Tm
+ ___swift_closure_destructor.3200Tm
+ ___swift_closure_destructor.3306Tm
+ ___swift_closure_destructor.332Tm
+ ___swift_closure_destructor.3444Tm
+ ___swift_closure_destructor.3474Tm
+ ___swift_closure_destructor.347Tm
+ ___swift_closure_destructor.3550Tm
+ ___swift_closure_destructor.3566Tm
+ ___swift_closure_destructor.3642Tm
+ ___swift_closure_destructor.3648Tm
+ ___swift_closure_destructor.3657Tm
+ ___swift_closure_destructor.377Tm
+ ___swift_closure_destructor.392Tm
+ ___swift_closure_destructor.401Tm
+ ___swift_closure_destructor.4143Tm
+ ___swift_closure_destructor.4187Tm
+ ___swift_closure_destructor.4193Tm
+ ___swift_closure_destructor.4305Tm
+ ___swift_closure_destructor.440Tm
+ ___swift_closure_destructor.4521Tm
+ ___swift_closure_destructor.4528Tm
+ ___swift_closure_destructor.4609Tm
+ ___swift_closure_destructor.4635Tm
+ ___swift_closure_destructor.464Tm
+ ___swift_closure_destructor.4674Tm
+ ___swift_closure_destructor.4790Tm
+ ___swift_closure_destructor.4796Tm
+ ___swift_closure_destructor.481Tm
+ ___swift_closure_destructor.5011Tm
+ ___swift_closure_destructor.5199Tm
+ ___swift_closure_destructor.52Tm
+ ___swift_closure_destructor.5472Tm
+ ___swift_closure_destructor.5504Tm
+ ___swift_closure_destructor.5807Tm
+ ___swift_closure_destructor.6018Tm
+ ___swift_closure_destructor.609Tm
+ ___swift_closure_destructor.615Tm
+ ___swift_closure_destructor.6321Tm
+ ___swift_closure_destructor.6335Tm
+ ___swift_closure_destructor.6541Tm
+ ___swift_closure_destructor.6548Tm
+ ___swift_closure_destructor.6573Tm
+ ___swift_closure_destructor.6693Tm
+ ___swift_closure_destructor.688Tm
+ ___swift_closure_destructor.715Tm
+ ___swift_closure_destructor.768Tm
+ ___swift_closure_destructor.855Tm
+ ___swift_closure_destructor.899Tm
+ ___swift_closure_destructor.96Tm
+ _symbolic SSSgIegg_
- -[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:]
- -[FPDExtensionManager _updateProviderListForMatchingExtensionRecords:]
- __ZL27containingApplicationRecordP8NSString
- ___67-[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:]_block_invoke
- ___67-[FPDExtensionManager _updateProviderListForFilteredFPDExtensions:]_block_invoke_2
- ___70-[FPDExtensionManager _updateProviderListForMatchingExtensionRecords:]_block_invoke
- ___block_descriptor_99_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___swift_closure_destructor.103Tm
- ___swift_closure_destructor.115Tm
- ___swift_closure_destructor.145Tm
- ___swift_closure_destructor.154Tm
- ___swift_closure_destructor.1588Tm
- ___swift_closure_destructor.171Tm
- ___swift_closure_destructor.1730Tm
- ___swift_closure_destructor.174Tm
- ___swift_closure_destructor.1750Tm
- ___swift_closure_destructor.1757Tm
- ___swift_closure_destructor.1773Tm
- ___swift_closure_destructor.182Tm
- ___swift_closure_destructor.188Tm
- ___swift_closure_destructor.1955Tm
- ___swift_closure_destructor.214Tm
- ___swift_closure_destructor.221Tm
- ___swift_closure_destructor.228Tm
- ___swift_closure_destructor.241Tm
- ___swift_closure_destructor.2515Tm
- ___swift_closure_destructor.253Tm
- ___swift_closure_destructor.278Tm
- ___swift_closure_destructor.2822Tm
- ___swift_closure_destructor.2935Tm
- ___swift_closure_destructor.296Tm
- ___swift_closure_destructor.3072Tm
- ___swift_closure_destructor.3079Tm
- ___swift_closure_destructor.3089Tm
- ___swift_closure_destructor.314Tm
- ___swift_closure_destructor.3166Tm
- ___swift_closure_destructor.3197Tm
- ___swift_closure_destructor.329Tm
- ___swift_closure_destructor.3303Tm
- ___swift_closure_destructor.3441Tm
- ___swift_closure_destructor.3471Tm
- ___swift_closure_destructor.3547Tm
- ___swift_closure_destructor.3557Tm
- ___swift_closure_destructor.3639Tm
- ___swift_closure_destructor.3645Tm
- ___swift_closure_destructor.3654Tm
- ___swift_closure_destructor.374Tm
- ___swift_closure_destructor.389Tm
- ___swift_closure_destructor.395Tm
- ___swift_closure_destructor.4140Tm
- ___swift_closure_destructor.4184Tm
- ___swift_closure_destructor.4190Tm
- ___swift_closure_destructor.425Tm
- ___swift_closure_destructor.4302Tm
- ___swift_closure_destructor.43Tm
- ___swift_closure_destructor.4515Tm
- ___swift_closure_destructor.4522Tm
- ___swift_closure_destructor.4606Tm
- ___swift_closure_destructor.461Tm
- ___swift_closure_destructor.4632Tm
- ___swift_closure_destructor.4671Tm
- ___swift_closure_destructor.467Tm
- ___swift_closure_destructor.4787Tm
- ___swift_closure_destructor.478Tm
- ___swift_closure_destructor.4793Tm
- ___swift_closure_destructor.5008Tm
- ___swift_closure_destructor.5196Tm
- ___swift_closure_destructor.5469Tm
- ___swift_closure_destructor.5501Tm
- ___swift_closure_destructor.5804Tm
- ___swift_closure_destructor.6015Tm
- ___swift_closure_destructor.606Tm
- ___swift_closure_destructor.612Tm
- ___swift_closure_destructor.6318Tm
- ___swift_closure_destructor.6332Tm
- ___swift_closure_destructor.6538Tm
- ___swift_closure_destructor.6545Tm
- ___swift_closure_destructor.6570Tm
- ___swift_closure_destructor.6690Tm
- ___swift_closure_destructor.685Tm
- ___swift_closure_destructor.68Tm
- ___swift_closure_destructor.712Tm
- ___swift_closure_destructor.765Tm
- ___swift_closure_destructor.78Tm
- ___swift_closure_destructor.852Tm
- ___swift_closure_destructor.896Tm
- ___swift_closure_destructor.95Tm
- ___swift_closure_destructor.97Tm
CStrings:
+ "      donated-root-key: %@\n"
+ "Cannot refresh the domain root donation: %@"
+ "[DEBUG] Updating extensions: %@ -> %@ (held: %@ -> %@, offloaded: %@ -> %@)"
+ "[DEBUG] [installation held or offloaded] Initializing disconnected provider for %@"
+ "[ERROR] [Indexer] Can't persist donated root key, error: %@"
+ "[NOTICE] Registering offloaded provider %{public}@ of %{public}@"
+ "[WARNING] Failed to create descriptor for placeholder extension %@"
+ "_owningApplicationIsOffloaded"
+ "donated-root-key"
+ "indexOneBatch(completionHandler:)"
+ "refreshDomainRootForIndexing(completionHandler:)"
+ "🧲 no root display name: empty display name for %s"
+ "🧲 no root display name: no provider domain for %s"
- "Precondition throwed error "
- "[DEBUG] Updating extensions: %@ -> %@ (held: %@ -> %@)"
- "[DEBUG] [installation held] Initializing disconnected provider for %@"
- "\xf1"
```
