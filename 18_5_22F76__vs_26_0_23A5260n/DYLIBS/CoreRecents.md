## CoreRecents

> `/System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents`

```diff

-1212.500.41.0.0
-  __TEXT.__text: 0x7d64
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xd84
-  __TEXT.__cstring: 0x922
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__oslogstring: 0x2b5
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x2452
-  __TEXT.__objc_methtype: 0x69f
-  __TEXT.__objc_stubs: 0x1da0
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x650
-  __DATA_CONST.__objc_classlist: 0x58
+1222.100.4.0.0
+  __TEXT.__text: 0xcb68
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x11dc
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x9de
+  __TEXT.__oslogstring: 0x7e8
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__objc_classname: 0x245
+  __TEXT.__objc_methname: 0x2917
+  __TEXT.__objc_methtype: 0x836
+  __TEXT.__objc_stubs: 0x2040
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa8
+  __DATA_CONST.__objc_selrefs: 0xb88
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0xca0
-  __AUTH_CONST.__objc_const: 0x11c8
-  __DATA.__objc_ivar: 0x90
-  __DATA.__data: 0x198
-  __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__objc_const: 0x1800
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__data: 0x258
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6002A510-66DA-3886-A013-9E6F6973B690
-  Functions: 309
-  Symbols:   1287
-  CStrings:  782
+  UUID: DC36F21C-1195-3D7F-917D-5391A99527A6
+  Functions: 403
+  Symbols:   1605
+  CStrings:  873
 
Symbols:
+ +[CRRecentContactSorting sortRecents:forQuery:]
+ +[CRRecentContactsDomainSupportedAccess supportedDomains]
+ +[CRRecentContactsDomainSupportedAccess supportedDomains].cold.1
+ +[CRRecentContactsLibrary(FactoryMethods) _recentEventForGroupMembers:displayName:date:weight:metadata:options:]
+ +[CRRecentContactsLibrary(FactoryMethods) _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.1
+ +[CRRecentContactsLibrary(FactoryMethods) _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.2
+ +[CRRecentContactsLibrary(FactoryMethods) _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.3
+ +[CRRecentContactsLibrary(FactoryMethods) explicitGroupEventForGroupMembers:displayName:date:metadata:options:]
+ +[CRRecentContactsLibrary(FactoryMethods) groupMemberWithAddress:displayName:kind:]
+ +[CRRecentContactsLibrary(FactoryMethods) groupMemberWithAddress:displayName:kind:].cold.1
+ +[CRRecentContactsLibrary(FactoryMethods) groupMemberWithAddress:displayName:kind:].cold.2
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForAddress:displayName:kind:date:]
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForAddress:displayName:kind:date:metadata:]
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForAddress:displayName:kind:date:weight:metadata:]
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForAddress:displayName:kind:date:weight:metadata:options:]
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForEmailAddress:displayName:metadata:]
+ +[CRRecentContactsLibrary(FactoryMethods) recentEventForPhoneNumber:displayName:metadata:]
+ +[CRRecentContactsLibraryDiagnosticAccessDecorator makeSerialNumber]
+ +[CRRecentContactsLibraryDiagnosticAccessDecorator makeSerialNumber].cold.1
+ -[CRRecentContactsDomainSupportedAccess .cxx_destruct]
+ -[CRRecentContactsDomainSupportedAccess countForQuery:error:]
+ -[CRRecentContactsDomainSupportedAccess createContactEvents:domain:sendingAddress:source:error:]
+ -[CRRecentContactsDomainSupportedAccess daemonProcessIdentifier]
+ -[CRRecentContactsDomainSupportedAccess deleteAllRecentContactsWithCompletion:]
+ -[CRRecentContactsDomainSupportedAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]
+ -[CRRecentContactsDomainSupportedAccess deleteUsingQuery:error:]
+ -[CRRecentContactsDomainSupportedAccess executeSearch:completion:]
+ -[CRRecentContactsDomainSupportedAccess executeSearch:error:]
+ -[CRRecentContactsDomainSupportedAccess implementationForDomain:]
+ -[CRRecentContactsDomainSupportedAccess initWithSupportedDomainAccess:]
+ -[CRRecentContactsDomainSupportedAccess initWithSupportedDomainAccess:unsupportedDomainAccess:]
+ -[CRRecentContactsDomainSupportedAccess invalidate]
+ -[CRRecentContactsDomainSupportedAccess isSupportedDomain:]
+ -[CRRecentContactsDomainSupportedAccess recentContactsWithIdentifiers:error:]
+ -[CRRecentContactsDomainSupportedAccess restorePreviouslyDeletedRecentContacts:error:]
+ -[CRRecentContactsDomainSupportedAccess start]
+ -[CRRecentContactsDomainSupportedAccess supportedDomainAccess]
+ -[CRRecentContactsDomainSupportedAccess supportedVersionOfQuery:]
+ -[CRRecentContactsDomainSupportedAccess unsupportedDomainAccess]
+ -[CRRecentContactsLibrary .cxx_destruct]
+ -[CRRecentContactsLibrary countOfRecentContactsForQuery:error:]
+ -[CRRecentContactsLibrary recentContactsWithIDs:error:]
+ -[CRRecentContactsLibrary recordAcceptedContactEvents:sendingAddress:source:completion:]
+ -[CRRecentContactsLibrary restorePreviouslyDeletedRecentContacts:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator .cxx_destruct]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator access]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator countForQuery:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator createContactEvents:domain:sendingAddress:source:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator createContactEvents:domain:sendingAddress:source:error:].cold.1
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator daemonProcessIdentifier]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator deleteAllRecentContactsWithCompletion:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator deleteUsingQuery:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator executeSearch:completion:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator executeSearch:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator initWithAccess:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator invalidate]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator recentContactsWithIdentifiers:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator restorePreviouslyDeletedRecentContacts:error:]
+ -[CRRecentContactsLibraryDiagnosticAccessDecorator start]
+ -[CRRecentContactsLibraryRemoteAccess .cxx_destruct]
+ -[CRRecentContactsLibraryRemoteAccess connection]
+ -[CRRecentContactsLibraryRemoteAccess countForQuery:error:]
+ -[CRRecentContactsLibraryRemoteAccess createContactEvents:domain:sendingAddress:source:error:]
+ -[CRRecentContactsLibraryRemoteAccess daemonProcessIdentifier]
+ -[CRRecentContactsLibraryRemoteAccess deleteAllRecentContactsWithCompletion:]
+ -[CRRecentContactsLibraryRemoteAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]
+ -[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]
+ -[CRRecentContactsLibraryRemoteAccess executeSearch:completion:]
+ -[CRRecentContactsLibraryRemoteAccess executeSearch:error:]
+ -[CRRecentContactsLibraryRemoteAccess initWithConnection:]
+ -[CRRecentContactsLibraryRemoteAccess invalidate]
+ -[CRRecentContactsLibraryRemoteAccess makeConnection]
+ -[CRRecentContactsLibraryRemoteAccess recentContactsWithIdentifiers:error:]
+ -[CRRecentContactsLibraryRemoteAccess restorePreviouslyDeletedRecentContacts:error:]
+ -[CRRecentContactsLibraryRemoteAccess start]
+ -[CRRecentContactsLibraryUnavailableAccess countForQuery:error:]
+ -[CRRecentContactsLibraryUnavailableAccess countForQuery:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess createContactEvents:domain:sendingAddress:source:error:]
+ -[CRRecentContactsLibraryUnavailableAccess createContactEvents:domain:sendingAddress:source:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess daemonProcessIdentifier]
+ -[CRRecentContactsLibraryUnavailableAccess daemonProcessIdentifier].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess deleteAllRecentContactsWithCompletion:]
+ -[CRRecentContactsLibraryUnavailableAccess deleteAllRecentContactsWithCompletion:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]
+ -[CRRecentContactsLibraryUnavailableAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess deleteUsingQuery:error:]
+ -[CRRecentContactsLibraryUnavailableAccess deleteUsingQuery:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess executeSearch:completion:]
+ -[CRRecentContactsLibraryUnavailableAccess executeSearch:completion:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess executeSearch:error:]
+ -[CRRecentContactsLibraryUnavailableAccess executeSearch:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess invalidate]
+ -[CRRecentContactsLibraryUnavailableAccess recentContactsWithIdentifiers:error:]
+ -[CRRecentContactsLibraryUnavailableAccess recentContactsWithIdentifiers:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess restorePreviouslyDeletedRecentContacts:error:]
+ -[CRRecentContactsLibraryUnavailableAccess restorePreviouslyDeletedRecentContacts:error:].cold.1
+ -[CRRecentContactsLibraryUnavailableAccess start]
+ GCC_except_table1
+ GCC_except_table12
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table27
+ GCC_except_table6
+ GCC_except_table9
+ _CFAllocatorAllocateTyped
+ _CRAcceptedIntroductionsDidChangeNotification
+ _CRRecentsDomainAcceptedIntroductions
+ _OBJC_CLASS_$_CRRecentContactSorting
+ _OBJC_CLASS_$_CRRecentContactsDomainSupportedAccess
+ _OBJC_CLASS_$_CRRecentContactsLibraryDiagnosticAccessDecorator
+ _OBJC_CLASS_$_CRRecentContactsLibraryRemoteAccess
+ _OBJC_CLASS_$_CRRecentContactsLibraryUnavailableAccess
+ _OBJC_IVAR_$_CRRecentContactsDomainSupportedAccess._supportedDomainAccess
+ _OBJC_IVAR_$_CRRecentContactsDomainSupportedAccess._unsupportedDomainAccess
+ _OBJC_IVAR_$_CRRecentContactsLibrary._access
+ _OBJC_IVAR_$_CRRecentContactsLibrary._deprecatedFutureSupportScheduler
+ _OBJC_IVAR_$_CRRecentContactsLibraryDiagnosticAccessDecorator._access
+ _OBJC_IVAR_$_CRRecentContactsLibraryRemoteAccess._connection
+ _OBJC_METACLASS_$_CRRecentContactSorting
+ _OBJC_METACLASS_$_CRRecentContactsDomainSupportedAccess
+ _OBJC_METACLASS_$_CRRecentContactsLibraryDiagnosticAccessDecorator
+ _OBJC_METACLASS_$_CRRecentContactsLibraryRemoteAccess
+ _OBJC_METACLASS_$_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_$_CLASS_METHODS_CRRecentContactSorting
+ __OBJC_$_CLASS_METHODS_CRRecentContactsDomainSupportedAccess
+ __OBJC_$_CLASS_METHODS_CRRecentContactsLibrary(FactoryMethods)
+ __OBJC_$_CLASS_METHODS_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_$_INSTANCE_METHODS_CRRecentContactsDomainSupportedAccess
+ __OBJC_$_INSTANCE_METHODS_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_$_INSTANCE_METHODS_CRRecentContactsLibraryRemoteAccess
+ __OBJC_$_INSTANCE_METHODS_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_$_INSTANCE_VARIABLES_CRRecentContactsDomainSupportedAccess
+ __OBJC_$_INSTANCE_VARIABLES_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_$_INSTANCE_VARIABLES_CRRecentContactsLibraryRemoteAccess
+ __OBJC_$_PROP_LIST_CRRecentContactsDomainSupportedAccess
+ __OBJC_$_PROP_LIST_CRRecentContactsLibraryAccess
+ __OBJC_$_PROP_LIST_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_$_PROP_LIST_CRRecentContactsLibraryRemoteAccess
+ __OBJC_$_PROP_LIST_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRRecentContactsLibraryAccess
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRRecentContactsLibraryAccess
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_CRRecentContactsLibraryAccess
+ __OBJC_CLASS_PROTOCOLS_$_CRRecentContactsDomainSupportedAccess
+ __OBJC_CLASS_PROTOCOLS_$_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_CLASS_PROTOCOLS_$_CRRecentContactsLibraryRemoteAccess
+ __OBJC_CLASS_PROTOCOLS_$_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_CLASS_RO_$_CRRecentContactSorting
+ __OBJC_CLASS_RO_$_CRRecentContactsDomainSupportedAccess
+ __OBJC_CLASS_RO_$_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_CLASS_RO_$_CRRecentContactsLibraryRemoteAccess
+ __OBJC_CLASS_RO_$_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_LABEL_PROTOCOL_$_CRRecentContactsLibraryAccess
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_CRRecentContactSorting
+ __OBJC_METACLASS_RO_$_CRRecentContactsDomainSupportedAccess
+ __OBJC_METACLASS_RO_$_CRRecentContactsLibraryDiagnosticAccessDecorator
+ __OBJC_METACLASS_RO_$_CRRecentContactsLibraryRemoteAccess
+ __OBJC_METACLASS_RO_$_CRRecentContactsLibraryUnavailableAccess
+ __OBJC_PROTOCOL_$_CRRecentContactsLibraryAccess
+ __OBJC_PROTOCOL_$_NSCopying
+ ___53-[CRRecentContactsLibraryRemoteAccess makeConnection]_block_invoke
+ ___53-[CRRecentContactsLibraryRemoteAccess makeConnection]_block_invoke.20
+ ___57+[CRRecentContactsDomainSupportedAccess supportedDomains]_block_invoke
+ ___59-[CRRecentContactsLibraryRemoteAccess countForQuery:error:]_block_invoke
+ ___59-[CRRecentContactsLibraryRemoteAccess countForQuery:error:]_block_invoke.8
+ ___59-[CRRecentContactsLibraryRemoteAccess countForQuery:error:]_block_invoke.cold.1
+ ___59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke
+ ___59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke.6
+ ___59-[CRRecentContactsLibraryRemoteAccess executeSearch:error:]_block_invoke.cold.1
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke.10
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke.cold.1
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke_2
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke_3
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke_4
+ ___62-[CRRecentContactsLibraryRemoteAccess deleteUsingQuery:error:]_block_invoke_4.cold.1
+ ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.35
+ ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.35.cold.1
+ ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.37
+ ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.38
+ ___64-[CRRecentContactsLibraryRemoteAccess executeSearch:completion:]_block_invoke
+ ___64-[CRRecentContactsLibraryRemoteAccess executeSearch:completion:]_block_invoke.7
+ ___64-[CRRecentContactsLibraryRemoteAccess executeSearch:completion:]_block_invoke.cold.1
+ ___65-[CRRecentContactsDomainSupportedAccess supportedVersionOfQuery:]_block_invoke
+ ___68+[CRRecentContactsLibraryDiagnosticAccessDecorator makeSerialNumber]_block_invoke
+ ___75-[CRRecentContactsLibraryRemoteAccess recentContactsWithIdentifiers:error:]_block_invoke
+ ___75-[CRRecentContactsLibraryRemoteAccess recentContactsWithIdentifiers:error:]_block_invoke.5
+ ___75-[CRRecentContactsLibraryRemoteAccess recentContactsWithIdentifiers:error:]_block_invoke.cold.1
+ ___77-[CRRecentContactsLibraryDiagnosticAccessDecorator executeSearch:completion:]_block_invoke
+ ___77-[CRRecentContactsLibraryRemoteAccess deleteAllRecentContactsWithCompletion:]_block_invoke
+ ___77-[CRRecentContactsLibraryRemoteAccess deleteAllRecentContactsWithCompletion:]_block_invoke.14
+ ___77-[CRRecentContactsLibraryRemoteAccess deleteAllRecentContactsWithCompletion:]_block_invoke.cold.1
+ ___84-[CRRecentContactsLibraryRemoteAccess restorePreviouslyDeletedRecentContacts:error:]_block_invoke
+ ___84-[CRRecentContactsLibraryRemoteAccess restorePreviouslyDeletedRecentContacts:error:]_block_invoke.3
+ ___84-[CRRecentContactsLibraryRemoteAccess restorePreviouslyDeletedRecentContacts:error:]_block_invoke.cold.1
+ ___86-[CRRecentContactsDomainSupportedAccess restorePreviouslyDeletedRecentContacts:error:]_block_invoke
+ ___90-[CRRecentContactsLibraryDiagnosticAccessDecorator deleteAllRecentContactsWithCompletion:]_block_invoke
+ ___94-[CRRecentContactsLibraryRemoteAccess createContactEvents:domain:sendingAddress:source:error:]_block_invoke
+ ___94-[CRRecentContactsLibraryRemoteAccess createContactEvents:domain:sendingAddress:source:error:]_block_invoke.2
+ ___94-[CRRecentContactsLibraryRemoteAccess createContactEvents:domain:sendingAddress:source:error:]_block_invoke.cold.1
+ ___97-[CRRecentContactsLibraryRemoteAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]_block_invoke
+ ___97-[CRRecentContactsLibraryRemoteAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]_block_invoke.13
+ ___97-[CRRecentContactsLibraryRemoteAccess deleteRecentContactsWithIdentifiers:syncKeys:domain:error:]_block_invoke.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e25_B16?0"CRRecentContact"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0q8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSString"8"NSArray"16ls32l8r40l8
+ ___block_descriptor_56_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.19
+ ___block_literal_global.22
+ ___block_literal_global.31
+ ___block_literal_global.61
+ ___defaultDecayer_block_invoke
+ __os_log_fault_impl
+ __searchRecentsUsingQuery:completion:.cn_once_object_1
+ __searchRecentsUsingQuery:completion:.cn_once_token_1
+ _client.cn_once_object_1
+ _client.cn_once_token_1
+ _defaultInstance.cn_once_object_0
+ _defaultInstance.cn_once_token_0
+ _log.cn_once_object_0
+ _log.cn_once_token_0
+ _makeSerialNumber.cn_once_object_0
+ _makeSerialNumber.cn_once_token_0
+ _objc_msgSend$_cn_filter:
+ _objc_msgSend$connection
+ _objc_msgSend$countForQuery:error:
+ _objc_msgSend$countRecentsUsingQuery:completion:
+ _objc_msgSend$createContactEvents:domain:sendingAddress:source:error:
+ _objc_msgSend$currentEnvironment
+ _objc_msgSend$daemonProcessIdentifier
+ _objc_msgSend$deleteAllRecentContactsWithCompletion:
+ _objc_msgSend$deleteRecentContactsWithIdentifiers:syncKeys:domain:error:
+ _objc_msgSend$deleteUsingQuery:error:
+ _objc_msgSend$domains
+ _objc_msgSend$executeSearch:completion:
+ _objc_msgSend$executeSearch:error:
+ _objc_msgSend$implementationForDomain:
+ _objc_msgSend$initWithAccess:
+ _objc_msgSend$initWithSupportedDomainAccess:unsupportedDomainAccess:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isSupportedDomain:
+ _objc_msgSend$makeConnection
+ _objc_msgSend$makeSerialNumber
+ _objc_msgSend$newSerialSchedulerWithName:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$performBlock:
+ _objc_msgSend$recentContactsWithIDs:completion:
+ _objc_msgSend$recentContactsWithIdentifiers:error:
+ _objc_msgSend$removeRecentContactsWithRecentIDs:syncKeys:domain:completion:
+ _objc_msgSend$restorePreviouslyDeletedRecentContacts:error:
+ _objc_msgSend$schedulerProvider
+ _objc_msgSend$sortRecents:forQuery:
+ _objc_msgSend$supportedDomainAccess
+ _objc_msgSend$supportedDomains
+ _objc_msgSend$supportedVersionOfQuery:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$unsupportedDomainAccess
+ _objc_release_x1
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
+ _supportedDomains.cn_once_object_0
+ _supportedDomains.cn_once_token_0
- +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:]
- +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.1
- +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.2
- +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.3
- +[CRRecentContactsLibrary explicitGroupEventForGroupMembers:displayName:date:metadata:options:]
- +[CRRecentContactsLibrary groupMemberWithAddress:displayName:kind:]
- +[CRRecentContactsLibrary groupMemberWithAddress:displayName:kind:].cold.1
- +[CRRecentContactsLibrary groupMemberWithAddress:displayName:kind:].cold.2
- +[CRRecentContactsLibrary recentEventForAddress:displayName:kind:date:]
- +[CRRecentContactsLibrary recentEventForAddress:displayName:kind:date:metadata:]
- +[CRRecentContactsLibrary recentEventForAddress:displayName:kind:date:weight:metadata:]
- +[CRRecentContactsLibrary recentEventForAddress:displayName:kind:date:weight:metadata:options:]
- -[CRRecentContactsLibrary _newConnection]
- -[CRRecentContactsLibrary _remoteLibraryWithErrorHandler:]
- -[CRRecentContactsLibrary _removeRecentContactsWithRecentIDs:syncKeys:recentsDomain:error:].cold.1
- -[CRRecentContactsLibrary _searchRecentsUsingQuery:]
- GCC_except_table58
- _CFAllocatorAllocate
- _OBJC_CLASS_$_CNFoundationError
- _OBJC_CLASS_$_CNFuture
- _OBJC_IVAR_$_CRRecentContactsLibrary._connection
- _OUTLINED_FUNCTION_2
- __OBJC_$_CLASS_METHODS_CRRecentContactsLibrary
- ___109-[CRRecentContactsLibrary _recordContactEvents:recentsDomain:sendingAddress:source:userInitiated:completion:]_block_invoke
- ___32-[CRRecentContactsLibrary start]_block_invoke
- ___32-[CRRecentContactsLibrary start]_block_invoke.70
- ___52-[CRRecentContactsLibrary _searchRecentsUsingQuery:]_block_invoke
- ___52-[CRRecentContactsLibrary _searchRecentsUsingQuery:]_block_invoke.86
- ___52-[CRRecentContactsLibrary _searchRecentsUsingQuery:]_block_invoke.cold.1
- ___62-[CRRecentContactsLibrary _removeRecentContactsMatchingQuery:]_block_invoke_2
- ___62-[CRRecentContactsLibrary _removeRecentContactsMatchingQuery:]_block_invoke_3
- ___62-[CRRecentContactsLibrary _removeRecentContactsMatchingQuery:]_block_invoke_4
- ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.77
- ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.78
- ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.80
- ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.80.cold.1
- ___63-[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:]_block_invoke.81
- ___66-[CRRecentContactsLibrary _removeAllRecentContactsWithCompletion:]_block_invoke
- ___66-[CRRecentContactsLibrary _removeAllRecentContactsWithCompletion:]_block_invoke_2
- ___66-[CRRecentContactsLibrary restorePreviouslyDeletedRecentContacts:]_block_invoke.117
- ___66-[CRRecentContactsLibrary restorePreviouslyDeletedRecentContacts:]_block_invoke.117.cold.1
- ___block_descriptor_32_e17_v16?0"NSArray"8l
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_32_e29_"<CNFuture>"16?0"NSError"8l
- ___block_descriptor_40_e8_32b_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32b_e8_v16?08ls32l8
- ___block_descriptor_40_e8_32o_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32o40b_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32o40r_e30_v24?0"NSString"8"NSArray"16ls32l8r40l8
- ___block_descriptor_56_e8_32o40b_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_56_e8_32o40b_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32o40b_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32o40o48b_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_80_e8_32o40o48o56b64b_e29_v24?0"NSArray"8"NSError"16ls56l8s32l8s64l8s40l8s48l8
- ___block_literal_global.101
- ___block_literal_global.112
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.197
- ___block_literal_global.201
- ___block_literal_global.68
- ___block_literal_global.74
- ___block_literal_global.98
- ___defaultDecayer_block_invoke_2
- __searchRecentsUsingQuery:completion:.cn_once_object_7
- __searchRecentsUsingQuery:completion:.cn_once_token_7
- _client.cn_once_object_2
- _client.cn_once_token_2
- _defaultInstance.cn_once_object_1
- _defaultInstance.cn_once_token_1
- _log.cn_once_object_1
- _log.cn_once_token_1
- _objc_msgSend$_newConnection
- _objc_msgSend$_remoteLibraryWithErrorHandler:
- _objc_msgSend$_searchRecentsUsingQuery:
- _objc_msgSend$addFailureBlock:
- _objc_msgSend$addSuccessBlock:
- _objc_msgSend$errorOnlyCompletionHandlerAdapter
- _objc_msgSend$futureWithError:
- _objc_msgSend$futureWithResult:
- _objc_msgSend$isTimeoutError:
- _objc_msgSend$recover:
- _objc_msgSend$removeRecentContactsWithRecentIDs:syncKeys:domain:
- _objc_msgSend$resultWithTimeout:error:
- _objc_msgSend$serviceName
- _sReplaceTimeoutError_block_invoke
CStrings:
+ "@\"<CNScheduler>\""
+ "@\"<CRRecentContactsLibraryAccess>\""
+ "@\"NSArray\"32@0:8@\"CRSearchQuery\"16^@24"
+ "@\"NSArray\"32@0:8@\"NSArray\"16^@24"
+ "@32@0:8@16o^@24"
+ "B16@?0@\"CRRecentContact\"8"
+ "B16@?0@\"NSString\"8"
+ "B48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40^@48"
+ "B56@0:8@16@24@32@40^@48"
+ "CRRecentContactSorting"
+ "CRRecentContactsDomainSupportedAccess"
+ "CRRecentContactsLibrary+Factories.m"
+ "CRRecentContactsLibraryAccess"
+ "CRRecentContactsLibraryDiagnosticAccessDecorator"
+ "CRRecentContactsLibraryRemoteAccess"
+ "CRRecentContactsLibraryUnavailableAccess"
+ "Connection invalidated"
+ "CoreRecents is unsupported on this platform"
+ "Error removing recent contacts for domain %{public}@: %{public}@"
+ "FactoryMethods"
+ "NSCopying"
+ "Recording accepted contact events"
+ "T@\"<CRRecentContactsLibraryAccess>\",R,V_access"
+ "T@\"<CRRecentContactsLibraryAccess>\",R,V_supportedDomainAccess"
+ "T@\"<CRRecentContactsLibraryAccess>\",R,V_unsupportedDomainAccess"
+ "T@\"NSXPCConnection\",R,V_connection"
+ "Ti,R"
+ "XPC error while servicing request: %{public}@"
+ "[%04llx] - Query: %{private}@"
+ "[%04llx] - Query: %{public}@ %{private}@"
+ "[%04llx] Deleted recents for query %{public}@ (%{public}@"
+ "[%04llx] Did count %ld recent contacts (%{public}@)"
+ "[%04llx] Did create %lu events (%{public}@)"
+ "[%04llx] Did delete recents (%{public}@)"
+ "[%04llx] Did fetch %lu recent contacts (%{public}@)"
+ "[%04llx] Did fetch recent contacts by ID (%{public}@)"
+ "[%04llx] Did receive error for query %{public}@ (%{public}@): %{public}@"
+ "[%04llx] Did receive reply with %lu for query %{public}@ (%{public}@)"
+ "[%04llx] Did remove all recents (%{public}@)"
+ "[%04llx] Did remove all recents (%{public}@): %{public}@"
+ "[%04llx] Did restore recents (%{public}@)"
+ "[%04llx] Error counting recents: %{public}@ (%{public}@)"
+ "[%04llx] Error creating events: %{public}@"
+ "[%04llx] Error deleting recents (%{public}@): %{public}@"
+ "[%04llx] Error deleting recents for query %{public}@ (%{public}@): %{public}@"
+ "[%04llx] Error fetching recents by ID: %{public}@ (%{public}@)"
+ "[%04llx] Error fetching recents: %{public}@ (%{public}@)"
+ "[%04llx] Error restoring recents: %{public}@ (%{public}@)"
+ "[%04llx] Will count recent contacts"
+ "[%04llx] Will create %lu events for %{private}@"
+ "[%04llx] Will delete recents for query %{public}@"
+ "[%04llx] Will delete recents with identifiers"
+ "[%04llx] Will fetch %lu recent contacts by ID"
+ "[%04llx] Will fetch recent contacts"
+ "[%04llx] Will remove all recents"
+ "[%04llx] Will restore %lu recents which were previously deleted"
+ "[%04llx] Will send request for recent contacts"
+ "_access"
+ "_access == NULL && \"attempt to start connection multiple times.\""
+ "_cn_filter:"
+ "_deprecatedFutureSupportScheduler"
+ "_supportedDomainAccess"
+ "_unsupportedDomainAccess"
+ "access"
+ "com.apple.corerecents.AcceptedIntroductionsChanged"
+ "com.apple.corerecents.deprecated-support"
+ "com.apple.introductions.accepted"
+ "com.apple.recentstool"
+ "connection"
+ "countForQuery:error:"
+ "countOfRecentContactsForQuery:error:"
+ "countRecentsUsingQuery:completion:"
+ "createContactEvents:domain:sendingAddress:source:error:"
+ "currentEnvironment"
+ "daemonProcessIdentifier"
+ "deleteAllRecentContactsWithCompletion:"
+ "deleteRecentContactsWithIdentifiers:syncKeys:domain:error:"
+ "deleteUsingQuery:error:"
+ "executeSearch:completion:"
+ "executeSearch:error:"
+ "implementationForDomain:"
+ "initWithAccess:"
+ "initWithConnection:"
+ "initWithSupportedDomainAccess:"
+ "initWithSupportedDomainAccess:unsupportedDomainAccess:"
+ "isEqualToArray:"
+ "isSupportedDomain:"
+ "makeConnection"
+ "makeSerialNumber"
+ "newSerialSchedulerWithName:"
+ "numberWithInteger:"
+ "performBlock:"
+ "q32@0:8@\"CRSearchQuery\"16^@24"
+ "q32@0:8@16^@24"
+ "recentContactsWithIDs:completion:"
+ "recentContactsWithIDs:error:"
+ "recentContactsWithIdentifiers:error:"
+ "recentEventForEmailAddress:displayName:metadata:"
+ "recentEventForPhoneNumber:displayName:metadata:"
+ "recordAcceptedContactEvents:sendingAddress:source:completion:"
+ "removeRecentContactsWithRecentIDs:syncKeys:domain:completion:"
+ "restorePreviouslyDeletedRecentContacts:error:"
+ "schedulerProvider"
+ "sortRecents:forQuery:"
+ "supportedDomainAccess"
+ "supportedDomains"
+ "supportedVersionOfQuery:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "unsupportedDomainAccess"
+ "v24@?0q8@\"NSError\"16"
+ "v32@0:8@\"CRSearchQuery\"16@?<v@?q@\"NSError\">24"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "@\"<CNFuture>\"16@?0@\"NSError\"8"
- "Could not remove recents: %{public}@"
- "Did execute query %{public}@ (%{public}@)"
- "Did remove recents"
- "Did restore recents"
- "Error restoring recents: %{public}@"
- "Mach service '%{public}@' not found."
- "Query %{public}@ failed: %{public}@"
- "Will execute query %{public}@"
- "Will remove %lu recents from %{public}@ domain"
- "Will restore %lu recents which were previously deleted"
- "_connection == NULL && \"attempt to start connection multiple times.\""
- "_newConnection"
- "_remoteLibraryWithErrorHandler:"
- "_searchRecentsUsingQuery:"
- "addFailureBlock:"
- "addSuccessBlock:"
- "errorOnlyCompletionHandlerAdapter"
- "futureWithError:"
- "futureWithResult:"
- "isTimeoutError:"
- "recover:"
- "removeRecentContactsWithRecentIDs:syncKeys:domain:"
- "resultWithTimeout:error:"
- "serviceName"
- "v16@?0@\"NSArray\"8"
- "v16@?0@8"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSString\"32"

```
