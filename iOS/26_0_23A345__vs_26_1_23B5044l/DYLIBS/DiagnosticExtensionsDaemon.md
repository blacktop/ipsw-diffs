## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-204.0.0.0.0
-  __TEXT.__text: 0x71ff0
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x6aac
+205.1.0.0.0
+  __TEXT.__text: 0x72688
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x6af4
   __TEXT.__const: 0x300
-  __TEXT.__cstring: 0x5335
-  __TEXT.__gcc_except_tab: 0x1dbc
-  __TEXT.__oslogstring: 0x8729
+  __TEXT.__cstring: 0x5345
+  __TEXT.__gcc_except_tab: 0x1db0
+  __TEXT.__oslogstring: 0x87d9
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x42

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1b18
+  __TEXT.__unwind_info: 0x1b10
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x892
-  __TEXT.__objc_methname: 0xf00c
+  __TEXT.__objc_classname: 0x894
+  __TEXT.__objc_methname: 0xf195
   __TEXT.__objc_methtype: 0x23a5
-  __TEXT.__objc_stubs: 0xbe40
+  __TEXT.__objc_stubs: 0xbf20
   __DATA_CONST.__got: 0x6d0
   __DATA_CONST.__const: 0x20b0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3978
+  __DATA_CONST.__objc_selrefs: 0x39b0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0xc40
-  __AUTH_CONST.__cfstring: 0x4d00
-  __AUTH_CONST.__objc_const: 0x12910
+  __AUTH_CONST.__cfstring: 0x4d20
+  __AUTH_CONST.__objc_const: 0x12970
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xfb0
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5b0
+  __DATA.__objc_ivar: 0x5b8
   __DATA.__data: 0xa70
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: ACEC0A62-10B3-387B-B584-744D69E8951A
-  Functions: 2761
-  Symbols:   9594
-  CStrings:  5140
+  UUID: 80477EF3-08E1-35D3-8085-88A6A02B61B7
+  Functions: 2769
+  Symbols:   9618
+  CStrings:  5156
 
Symbols:
+ -[DEDBugSession hasLocalizedTextDataInCache]
+ -[DEDBugSession populateLocalizedTextDataForExtensions:]
+ -[DEDBugSession populateLocalizedTextDataForExtensions:].cold.1
+ -[DEDBugSession populateLocalizedTextDataForExtensions:].cold.2
+ -[DEDBugSession setHasLocalizedTextDataInCache:]
+ -[DEDBugSession updateCachedExtensionsWithLocalizedTextData:]
+ -[DEDBugSession updateCachedExtensionsWithLocalizedTextData:].cold.1
+ -[DEDExtension localizedCustomerConsentText]
+ -[DEDExtension setLocalizedCustomerConsentText:]
+ GCC_except_table104
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table134
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table88
+ _OBJC_IVAR_$_DEDBugSession._hasLocalizedTextDataInCache
+ _OBJC_IVAR_$_DEDExtension._localizedCustomerConsentText
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ ___27-[DEDDaemon commitSession:]_block_invoke.149
+ ___27-[DEDDaemon commitSession:]_block_invoke.154
+ ___44-[DEDRadarFinisher processVerifyTaskResults]_block_invoke.173
+ ___44-[DEDRadarFinisher processVerifyTaskResults]_block_invoke.176
+ ___45-[DEDDaemon terminateExtension:info:session:]_block_invoke.124
+ ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.112
+ ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.112.cold.1
+ ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.119
+ ___54-[DEDController idsInbound_devicesChanged:completion:]_block_invoke.53
+ ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.142
+ ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.45
+ ___59-[DEDDaemon _syncSessionStatusWithSession:withIdentifiers:]_block_invoke.172
+ ___72-[DEDDaemon _startDiagnosticWithIdentifier:parameters:session:runSetup:]_block_invoke.114
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.63
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.63.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.78
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.78.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.80
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.84
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.84.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.88
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_2.86
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_3.87
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_literal_global.102
+ ___block_literal_global.116
+ ___block_literal_global.144
+ ___block_literal_global.145
+ ___block_literal_global.146
+ ___block_literal_global.204
+ ___block_literal_global.237
+ ___block_literal_global.329
+ _objc_msgSend$hasLocalizedTextDataInCache
+ _objc_msgSend$localizedCustomerConsentText
+ _objc_msgSend$localizedCustomerConsentTextWithLocalization:
+ _objc_msgSend$populateLocalizedTextDataForExtensions:
+ _objc_msgSend$setHasLocalizedTextDataInCache:
+ _objc_msgSend$setLocalizedCustomerConsentText:
+ _objc_msgSend$updateCachedExtensionsWithLocalizedTextData:
- GCC_except_table115
- GCC_except_table116
- GCC_except_table126
- GCC_except_table138
- GCC_except_table195
- GCC_except_table62
- GCC_except_table66
- GCC_except_table71
- GCC_except_table78
- ___27-[DEDDaemon commitSession:]_block_invoke.143
- ___27-[DEDDaemon commitSession:]_block_invoke.148
- ___44-[DEDRadarFinisher processVerifyTaskResults]_block_invoke.167
- ___44-[DEDRadarFinisher processVerifyTaskResults]_block_invoke.170
- ___45-[DEDDaemon terminateExtension:info:session:]_block_invoke.118
- ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.113.cold.1
- ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.114
- ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.120
- ___54-[DEDController idsInbound_devicesChanged:completion:]_block_invoke.54
- ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.139
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.46
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke_2.45
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke_6
- ___59-[DEDDaemon _syncSessionStatusWithSession:withIdentifiers:]_block_invoke.166
- ___72-[DEDDaemon _startDiagnosticWithIdentifier:parameters:session:runSetup:]_block_invoke.108
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.64
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.64.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.79
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.79.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.82
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.85.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.86
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.89
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_2.87
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_3.88
- ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
- ___block_literal_global.103
- ___block_literal_global.139
- ___block_literal_global.143
- ___block_literal_global.201
- ___block_literal_global.231
- ___block_literal_global.323
- _dispatch_group_async
CStrings:
+ "No localized text data available in cache yet, skipping population"
+ "Populating localized text data for extension [%{public}@] from cache"
+ "Session does not have capability %@"
+ "T@\"NSString\",&,V_localizedCustomerConsentText"
+ "TB,N,V_hasLocalizedTextDataInCache"
+ "Updating DE text on extension [%{public}@]"
+ "_hasLocalizedTextDataInCache"
+ "_localizedCustomerConsentText"
+ "hasLocalizedTextDataInCache"
+ "localizedCustomerConsentText"
+ "localizedCustomerConsentTextWithLocalization:"
+ "populateLocalizedTextDataForExtensions:"
+ "setHasLocalizedTextDataInCache:"
+ "setLocalizedCustomerConsentText:"
+ "updateCachedExtensionsWithLocalizedTextData:"
- "com.apple.DiagnosticExtensions.iOSExtension"

```
