## LaunchServices

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices`

```diff

-  __TEXT.__text: 0x250708
-  __TEXT.__objc_methlist: 0xed74
-  __TEXT.__const: 0xaa8
-  __TEXT.__cstring: 0x33142
-  __TEXT.__oslogstring: 0x22005
-  __TEXT.__gcc_except_tab: 0x33f8c
+  __TEXT.__text: 0x2520f8
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_methlist: 0xeda4
+  __TEXT.__const: 0xac0
+  __TEXT.__cstring: 0x33372
+  __TEXT.__oslogstring: 0x220fd
+  __TEXT.__gcc_except_tab: 0x342f8
   __TEXT.__ustring: 0x1be
   __TEXT.__dof_LSFSNode: 0x2b6
-  __TEXT.__unwind_info: 0xea40
+  __TEXT.__unwind_info: 0xeac8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3e58
+  __DATA_CONST.__const: 0x3e80
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e50
+  __DATA_CONST.__objc_selrefs: 0x6e68
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x638
   __DATA_CONST.__objc_arraydata: 0xa10
-  __DATA_CONST.__got: 0xdb8
-  __AUTH_CONST.__const: 0xa9b8
-  __AUTH_CONST.__cfstring: 0x1dda0
-  __AUTH_CONST.__objc_const: 0x16598
+  __DATA_CONST.__got: 0xe40
+  __AUTH_CONST.__const: 0xaa38
+  __AUTH_CONST.__cfstring: 0x1dea0
+  __AUTH_CONST.__objc_const: 0x16658
   __AUTH_CONST.__weak_auth_got: 0x30
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1ed8
-  __AUTH.__objc_data: 0x3b10
+  __AUTH_CONST.__auth_got: 0x1ee0
+  __AUTH.__objc_data: 0x3b60
   __AUTH.__data: 0x248
-  __DATA.__objc_ivar: 0xc58
-  __DATA.__data: 0x15f0
+  __DATA.__objc_ivar: 0xc68
+  __DATA.__data: 0x15f4
   __DATA.__bss: 0x1a78
   __DATA.__common: 0x5
-  __DATA_DIRTY.__objc_data: 0x1180
+  __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0xc00

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/Versions/A/AppServerSupport
   - /System/Library/PrivateFrameworks/CoreServicesStore.framework/Versions/A/CoreServicesStore
-  - /System/Library/PrivateFrameworks/Ecosystem.framework/Versions/A/Ecosystem
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/Versions/A/InstalledContentLibrary
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 11119
-  Symbols:   24517
-  CStrings:  11708
+  Functions: 11138
+  Symbols:   24563
+  CStrings:  11731
 
Sections:
~ __TEXT.__dof_LSFSNode : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[LSBundleRecordBuilder contentDescriptors]
+ -[LSBundleRecordBuilder secondaryGenreID]
+ -[LSiTunesMetadata contentDescriptors]
+ -[LSiTunesMetadata secondaryGenreIdentifier]
+ GCC_except_table172
+ GCC_except_table367
+ OBJC_IVAR_$_LSBundleRecordBuilder._contentDescriptors
+ OBJC_IVAR_$_LSBundleRecordBuilder._secondaryGenreID
+ OBJC_IVAR_$_LSiTunesMetadata._contentDescriptors
+ OBJC_IVAR_$_LSiTunesMetadata._secondaryGenreIdentifier
+ _OBJC_CLASS_$_ECORosettaPreferenceNotificationClient$lazyGOT
+ _OBJC_CLASS_$_ECORosettaPreferenceNotificationClient$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_ECOUnsupportedApplicationListClient$lazyGOT
+ _OBJC_CLASS_$_ECOUnsupportedApplicationListClient$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_MIStoreMetadataContentDescriptor
+ _OUTLINED_FUNCTION_38
+ _Z47copyLSApplicationInformationKeysWhichAreDynamicv
+ _ZL32_LSRebuildNodeIsSignatureTrustedP6FSNode
+ _ZN14BindingDecoderC2EPK8__CFDataj
+ _ZN14BindingManager14CreateWithDataEPK8__CFDatabj
+ __LSAuditTokensAreEqual
+ __LSDefaultAppCategoryIsValid
+ __LSPluginNotificationPayloadGetSessionKey
+ __LSPluginNotificationPayloadSetSessionKey
+ __LSRegisterBundleNodeForRebuildIfNecessary
+ __Z21CFDictionaryCopyValuePK14__CFDictionaryPKv
+ __Z22CFArrayCreateWithItemsPKvS0_S0_S0_S0_S0_S0_S0_S0_S0_
+ __Z47copyLSApplicationInformationKeysWhichAreDynamicv
+ __ZL32_LSDetermineTrustForRegistrationP6FSNodePU15__autoreleasingP7NSError
+ __ZL32_LSRebuildNodeIsSignatureTrustedP6FSNode
+ __ZN14BindingDecoderC1EPK8__CFDataj
+ __ZN14BindingDecoderC2EPK8__CFDataj
+ __ZN14BindingManager14CreateWithDataEPK8__CFDatabj
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE7reserveEm
+ __ZZ47copyLSApplicationInformationKeysWhichAreDynamicvE10sResultRef
+ __ZZ47copyLSApplicationInformationKeysWhichAreDynamicvE5sOnce
+ __ZZL40notifyServerSideAboutLaunchedApplication11LSSessionIDPK14__CFDictionaryiS2_RK13audit_token_tbPS2_E17invalidAuditToken
+ ___48-[LSiTunesMetadata _initWithContext:bundleData:]_block_invoke
+ ____Z47copyLSApplicationInformationKeysWhichAreDynamicv_block_invoke
+ ____ZL26setContainsAnItemFromArrayPK7__CFSetPK9__CFArray_block_invoke
+ ___block_descriptor_32_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_32_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_32_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
+ ___block_descriptor_368_ea8_32r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_40_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
+ ___block_descriptor_40_ea8_32s_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_44_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_48_ea8_32bs_e375_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
+ ___block_descriptor_56_ea8_32bs40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32bs40rc_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32r40r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32s40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_56_ea8_32s40s_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_640_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32bs40r48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ ___block_descriptor_72_ea8_32s40s48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
+ __dyld_lazy_load
+ __kLSApplicationCanBeIgnoredForParentExitDetectionKey
+ _lazyLoadFlag$Ecosystem
- _LSCopyApplicationInformationItem
- _ZN14BindingDecoderC2EPK8__CFData
- _ZN14BindingManager14CreateWithDataEPK8__CFDatab
- __Z26CFDictionaryCreateWithItemPKvS0_
- __Z34CFArrayGetValueAtIndexAsDictionaryPK9__CFArrayl
- __ZGVZL26_LSAddBundleExecutableInfoP17_LSBundleProviderP18LSRegistrationInfoP14__CFDictionaryP15ICLBundleRecordE12archPriority
- __ZN14BindingDecoderC1EPK8__CFData
- __ZN14BindingDecoderC2EPK8__CFData
- __ZN14BindingManager14CreateWithDataEPK8__CFDatab
- __ZZL26_LSAddBundleExecutableInfoP17_LSBundleProviderP18LSRegistrationInfoP14__CFDictionaryP15ICLBundleRecordE12archPriority
- ___LSApplicationWorkspacePluginsChangedCallback_block_invoke_2
- ___block_descriptor_32_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_32_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_32_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
- ___block_descriptor_368_ea8_32r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_40_e381_B36?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28l
- ___block_descriptor_40_ea8_32s_e378_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_44_e378_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_48_ea8_32bs_e375_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20l
- ___block_descriptor_48_ea8_32s_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32bs40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32bs40rc_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32r40r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_56_ea8_32s40bs_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_628_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32l
- ___block_descriptor_72_e8_32bs40r48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
- ___block_descriptor_72_ea8_32s40s48r_e365_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20l
CStrings:
+ "#LSDatabaseBuilder %@ already has an up-to-date registration"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSContainerHelpers.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPersonaAssociationMutation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "B36@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28"
+ "BOOL _LSRegisterBundleNodeForRebuildIfNecessary(LSContext *, FSNode *__strong, LSRegisterOptions, LSInstallInfo *__strong, Boolean *, NSError *__autoreleasing *)"
+ "Could not determine local session for %@; processing anyway: %@"
+ "Could not determine trust for %{private}@ during rebuild: %@"
+ "ISIconRef.mm"
+ "Ignoring %@ from session %@; this process reflects session %@"
+ "Invalid default app category"
+ "LSASN:{0x%x-0x%x}"
+ "LSApplicationCanBeIgnoredForParentExitDetectionKey"
+ "LSPluginNotificationSessionKey"
+ "OSStatus GetIconRefFromFileInfo(const FSRef *, UniCharCount, const UniChar *, FSCatalogInfoBitmap, const FSCatalogInfo *, IconServicesUsageFlags, IconRef *, SInt16 *)"
+ "_LSRegisterBundleNodeForRebuildIfNecessary"
+ "contentDescriptors"
+ "isSystemSession"
+ "outIconRef must not be NULL"
+ "secondaryGenreID"
+ "secondaryGenreId"
+ "secondaryGenreIdentifier"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1498:63)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
+ "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20"
+ "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9vE1e5/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/FSUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSAESupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Base/LSValidationToken.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSAlias.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/DefaultApps/LSDefaultAppsCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCapability.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSClaimedTypes.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSCryptexUtils.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSDataContainerPersonality.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSEligibility.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternal.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSExternalPriv.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSInternetLocator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSOpenWithMenu.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistrants.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSRegistration.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSURLPropertyProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSLaunchRunningBoard.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCall.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenCore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenGenericReadMe.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSOpenNewWorld.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Open/LSTranslocation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSApplicationRecordEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSServiceEnumerator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationExtensionRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSBundleRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSDatabaseContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSExtensionPointRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSServiceRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Record/UTTypeRecord.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/RunIdentity/LSApplicationIdentity.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/CodeEvaluation/LSCodeEvaluationClientManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSDTrustedSignatureService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignature.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Security/LSTrustedSignatureDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDeviceEncryptionService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDDisseminationClient.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSDXPCClient.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Server/LSServerInterface.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLinkPlugIn.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationRestrictionsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleProxy.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleWrapper.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSContainerHelpers.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDefaultApplicationQuery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDiskUsage.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPersonaAssociationMutation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQuery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithURL.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQuery.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSStatePlist.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/LSTranslocationHelpers.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Workspace/NSCoder+LaunchServicesAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationCreation.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/TemplateApplications/LSTemplateApplicationLaunch.mm"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "B36@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20*28"
- "LSASN:{hi=0x%x;lo=0x%x}"
- "LSArchitecturePriorityIsForged"
- "forged-arch-priority"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1498:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1529:65)]"
- "static id LaunchServices::PrefsStorage::_GetValueInPrefsArrayWithPredicate(NSArray *__strong, __unsafe_unretained Class, const Pred &) [Pred = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1536:65)]"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIICCII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIICCCCCCCCCC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IIQQI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}Ii{LSVersionNumber=[32C]}QQIIIIIIIIIIQIQQQIQQIIIQIQIIQIIIIIIIIIIIIIIIICCC[0I]IIiIIIIII}12*20"
- "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tEErKh/Sources/CoreServicesSubFrameworks/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"

```
