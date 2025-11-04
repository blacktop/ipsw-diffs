## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3804.200.81.2.3
-  __TEXT.__text: 0x1ba8bc
-  __TEXT.__auth_stubs: 0x3360
-  __TEXT.__objc_methlist: 0x1aff8
+3804.300.12.2.1
+  __TEXT.__text: 0x1bb5d0
+  __TEXT.__auth_stubs: 0x3340
+  __TEXT.__objc_methlist: 0x1b150
   __TEXT.__const: 0x24b0
-  __TEXT.__gcc_except_tab: 0x3a84
-  __TEXT.__cstring: 0xcae2
-  __TEXT.__dlopen_cstrs: 0x86e
-  __TEXT.__oslogstring: 0xc10a
+  __TEXT.__gcc_except_tab: 0x3bbc
+  __TEXT.__cstring: 0xcb02
+  __TEXT.__dlopen_cstrs: 0x8ba
+  __TEXT.__oslogstring: 0xc23a
   __TEXT.__ustring: 0x12
   __TEXT.__constg_swiftt: 0xdc4
   __TEXT.__swift5_typeref: 0xea1

   __TEXT.__swift5_capture: 0x5d4
   __TEXT.__swift_as_entry: 0x68
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0x7f30
+  __TEXT.__unwind_info: 0x7f80
   __TEXT.__eh_frame: 0x2550
-  __TEXT.__objc_classname: 0x446d
-  __TEXT.__objc_methname: 0x2ba95
-  __TEXT.__objc_methtype: 0x544d
-  __TEXT.__objc_stubs: 0x1ed60
-  __DATA_CONST.__got: 0x1b90
-  __DATA_CONST.__const: 0x61b0
-  __DATA_CONST.__objc_classlist: 0x1100
+  __TEXT.__objc_classname: 0x44c0
+  __TEXT.__objc_methname: 0x2ba55
+  __TEXT.__objc_methtype: 0x5426
+  __TEXT.__objc_stubs: 0x1ede0
+  __DATA_CONST.__got: 0x1ba0
+  __DATA_CONST.__const: 0x61e8
+  __DATA_CONST.__objc_classlist: 0x1118
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x308
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9840
+  __DATA_CONST.__objc_selrefs: 0x9860
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x9c8
+  __DATA_CONST.__objc_superrefs: 0x9c0
   __DATA_CONST.__objc_arraydata: 0x268
-  __AUTH_CONST.__auth_got: 0x19c0
-  __AUTH_CONST.__const: 0x6ab8
-  __AUTH_CONST.__cfstring: 0xdba0
-  __AUTH_CONST.__objc_const: 0x2c010
+  __AUTH_CONST.__auth_got: 0x19b0
+  __AUTH_CONST.__const: 0x6b38
+  __AUTH_CONST.__cfstring: 0xdaa0
+  __AUTH_CONST.__objc_const: 0x2c1b0
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x5728
+  __AUTH.__objc_data: 0x5868
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0x128c
-  __DATA.__data: 0x2d10
-  __DATA.__bss: 0x2450
+  __DATA.__objc_ivar: 0x1284
+  __DATA.__data: 0x2cb0
+  __DATA.__bss: 0x24a0
   __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x5e10
+  __DATA_DIRTY.__objc_data: 0x5dc0
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x1090
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 326826E2-1DF9-31EA-9223-33E9E40B5129
-  Functions: 12512
-  Symbols:   36719
-  CStrings:  12921
+  UUID: 2B858FE2-C77B-3DD6-89E6-E54A80FF6695
+  Functions: 12557
+  Symbols:   36848
+  CStrings:  12914
 
Symbols:
+ +[CN(PropertyDescription) deviceNameDescription]
+ +[CN(PropertyDescription) deviceNameDescription].cold.1
+ +[CN(PropertyDescription) expiryDateDescription]
+ +[CN(PropertyDescription) expiryDateDescription].cold.1
+ +[CN(PropertyDescription) isSharingPairedDescription]
+ +[CN(PropertyDescription) isSharingPairedDescription].cold.1
+ +[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithCompletion:]
+ +[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithCompletion:].cold.1
+ +[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithTimeout:error:]
+ +[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithTimeout:error:].cold.1
+ +[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithTimeout:error:].cold.2
+ -[CNContact deviceName]
+ -[CNContact expiryDate]
+ -[CNContact isSharingPaired]
+ -[CNDeviceNameDescription CNValueForContact:]
+ -[CNDeviceNameDescription decodeUsingCoder:contact:]
+ -[CNDeviceNameDescription encodeUsingCoder:contact:]
+ -[CNDeviceNameDescription init]
+ -[CNDeviceNameDescription isEqualForContact:other:]
+ -[CNDeviceNameDescription setCNValue:onContact:]
+ -[CNDeviceNameDescription valueClass]
+ -[CNDeviceNameDescription(iOSAB) ABValueForABPerson:]
+ -[CNDeviceNameDescription(iOSAB) setABValue:onABPerson:error:]
+ -[CNExpiryDateDescription CNValueForContact:]
+ -[CNExpiryDateDescription decodeUsingCoder:contact:]
+ -[CNExpiryDateDescription encodeUsingCoder:contact:]
+ -[CNExpiryDateDescription init]
+ -[CNExpiryDateDescription isEqualForContact:other:]
+ -[CNExpiryDateDescription setCNValue:onContact:]
+ -[CNExpiryDateDescription valueClass]
+ -[CNExpiryDateDescription(iOSAB) ABValueForABPerson:]
+ -[CNExpiryDateDescription(iOSAB) setABValue:onABPerson:error:]
+ -[CNIsSharingPairedDescription CNValueForContact:]
+ -[CNIsSharingPairedDescription decodeUsingCoder:contact:]
+ -[CNIsSharingPairedDescription encodeUsingCoder:contact:]
+ -[CNIsSharingPairedDescription init]
+ -[CNIsSharingPairedDescription isEqualForContact:other:]
+ -[CNIsSharingPairedDescription setCNValue:onContact:]
+ -[CNIsSharingPairedDescription valueClass]
+ -[CNIsSharingPairedDescription(iOSAB) ABValueForABPerson:]
+ -[CNIsSharingPairedDescription(iOSAB) setABValue:onABPerson:error:]
+ -[CNMutableContact deviceName]
+ -[CNMutableContact expiryDate]
+ -[CNMutableContact isSharingPaired]
+ -[CNMutableContact setDeviceName:]
+ -[CNMutableContact setExpiryDate:]
+ -[CNMutableContact setIsSharingPaired:]
+ GCC_except_table149
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table203
+ GCC_except_table213
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table240
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table252
+ GCC_except_table256
+ _CNContactDeviceNameKey
+ _CNContactExpiryDateKey
+ _CNContactIsSharingPairedKey
+ _CNSharingPairedContactsFetcherLog
+ _CNSharingPairedContactsFetcherLog.cn_once_object_0
+ _CNSharingPairedContactsFetcherLog.cn_once_token_0
+ _CNSharingPairedContactsFetcherLog.cold.1
+ _OBJC_CLASS_$_CNDeviceNameDescription
+ _OBJC_CLASS_$_CNExpiryDateDescription
+ _OBJC_CLASS_$_CNIsSharingPairedDescription
+ _OBJC_CLASS_$_CNSharingPairedContactsFetcher
+ _OBJC_IVAR_$_CNContact._deviceName
+ _OBJC_IVAR_$_CNContact._expiryDate
+ _OBJC_IVAR_$_CNContact._isSharingPaired
+ _OBJC_METACLASS_$_CNDeviceNameDescription
+ _OBJC_METACLASS_$_CNExpiryDateDescription
+ _OBJC_METACLASS_$_CNIsSharingPairedDescription
+ _OBJC_METACLASS_$_CNSharingPairedContactsFetcher
+ _SharingLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_CNSharingPairedContactsFetcher
+ __OBJC_$_INSTANCE_METHODS_CNDeviceNameDescription(iOSAB)
+ __OBJC_$_INSTANCE_METHODS_CNExpiryDateDescription(iOSAB)
+ __OBJC_$_INSTANCE_METHODS_CNIsSharingPairedDescription(iOSAB)
+ __OBJC_$_PROP_LIST_CNDeviceNameDescription
+ __OBJC_$_PROP_LIST_CNExpiryDateDescription
+ __OBJC_$_PROP_LIST_CNIsSharingPairedDescription
+ __OBJC_CLASS_PROTOCOLS_$_CNDeviceNameDescription
+ __OBJC_CLASS_PROTOCOLS_$_CNExpiryDateDescription
+ __OBJC_CLASS_PROTOCOLS_$_CNIsSharingPairedDescription
+ __OBJC_CLASS_RO_$_CNDeviceNameDescription
+ __OBJC_CLASS_RO_$_CNExpiryDateDescription
+ __OBJC_CLASS_RO_$_CNIsSharingPairedDescription
+ __OBJC_CLASS_RO_$_CNSharingPairedContactsFetcher
+ __OBJC_METACLASS_RO_$_CNDeviceNameDescription
+ __OBJC_METACLASS_RO_$_CNExpiryDateDescription
+ __OBJC_METACLASS_RO_$_CNIsSharingPairedDescription
+ __OBJC_METACLASS_RO_$_CNSharingPairedContactsFetcher
+ ___48+[CN(PropertyDescription) deviceNameDescription]_block_invoke
+ ___48+[CN(PropertyDescription) expiryDateDescription]_block_invoke
+ ___53+[CN(PropertyDescription) isSharingPairedDescription]_block_invoke
+ ___69-[CNDataMapperContactStore contactsForFetchRequest:matchInfos:error:]_block_invoke.83
+ ___75+[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithCompletion:]_block_invoke
+ ___75+[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithCompletion:]_block_invoke.cold.1
+ ___75+[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithCompletion:]_block_invoke.cold.2
+ ___78+[CNSharingPairedContactsFetcher fetchSharingPairedContactsWithTimeout:error:]_block_invoke
+ ___78-[CNDataMapperContactStore executeFetchRequest:progressiveResults:completion:]_block_invoke.91
+ ___79-[CNDataMapperContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.59
+ ___79-[CNDataMapperContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.64
+ ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.68
+ ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.68.cold.1
+ ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.80
+ ___CNSharingPairedContactsFetcherLog_block_invoke
+ ___SharingLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.257
+ ___block_literal_global.406
+ ___block_literal_global.409
+ ___block_literal_global.412
+ ___block_literal_global.493
+ ___block_literal_global.497
+ ___block_literal_global.67
+ ___block_literal_global.814
+ ___block_literal_global.86
+ ___block_literal_global.874
+ ___block_literal_global.883
+ ___block_literal_global.97
+ ___getSFCreatePairedContactManagerSymbolLoc_block_invoke
+ _audit_stringSharing
+ _deviceNameDescription.cn_once_object_99
+ _deviceNameDescription.cn_once_token_99
+ _expiryDateDescription.cn_once_object_98
+ _expiryDateDescription.cn_once_token_98
+ _getSFCreatePairedContactManagerSymbolLoc.ptr
+ _isSharingPairedDescription.cn_once_object_97
+ _isSharingPairedDescription.cn_once_token_97
+ _objc_msgSend$deviceName
+ _objc_msgSend$deviceNameDescription
+ _objc_msgSend$expiryDate
+ _objc_msgSend$expiryDateDescription
+ _objc_msgSend$fetchAllContactsWithCompletion:
+ _objc_msgSend$fetchSharingPairedContactsWithCompletion:
+ _objc_msgSend$isSharingPaired
+ _objc_msgSend$isSharingPairedDescription
+ _objc_msgSend$newDefaultLibraryWithBundle:error:
+ _objc_msgSend$setDeviceName:
+ _objc_msgSend$setExpiryDate:
+ _objc_msgSend$setIsSharingPaired:
- -[CNDataMapperContactStore queryAnalyticsLogger]
- -[CNQueryAnalyticsLogger .cxx_destruct]
- -[CNQueryAnalyticsLogger assumedIdentity]
- -[CNQueryAnalyticsLogger auditToken]
- -[CNQueryAnalyticsLogger initWithAuditToken:assumedIdentity:]
- -[CNQueryAnalyticsLogger keyboardStateMonitor]
- -[CNQueryAnalyticsLogger processIdentity]
- -[CNQueryAnalyticsLogger recordQueryWithFetchRequest:]
- -[CNQueryAnalyticsLogger setAssumedIdentity:]
- -[CNQueryAnalyticsLogger setAuditToken:]
- -[CNQueryAnalyticsLogger setKeyboardStateMonitor:]
- -[CNQueryAnalyticsLogger setProcessIdentity:]
- -[CNiOSAddressBookDataMapper shouldCaptureMetricsForQueries]
- GCC_except_table180
- GCC_except_table187
- GCC_except_table189
- GCC_except_table192
- GCC_except_table194
- GCC_except_table199
- GCC_except_table204
- GCC_except_table214
- GCC_except_table219
- GCC_except_table222
- GCC_except_table224
- GCC_except_table226
- GCC_except_table228
- GCC_except_table230
- GCC_except_table233
- GCC_except_table235
- GCC_except_table237
- GCC_except_table239
- GCC_except_table241
- GCC_except_table243
- GCC_except_table247
- GCC_except_table249
- GCC_except_table251
- GCC_except_table253
- GCC_except_table257
- _AnalyticsSendEventLazy
- _OBJC_CLASS_$_CNQueryAnalyticsLogger
- _OBJC_IVAR_$_CNDataMapperContactStore._queryAnalyticsLogger
- _OBJC_IVAR_$_CNQueryAnalyticsLogger._assumedIdentity
- _OBJC_IVAR_$_CNQueryAnalyticsLogger._auditToken
- _OBJC_IVAR_$_CNQueryAnalyticsLogger._keyboardStateMonitor
- _OBJC_IVAR_$_CNQueryAnalyticsLogger._processIdentity
- _OBJC_METACLASS_$_CNQueryAnalyticsLogger
- __OBJC_$_INSTANCE_METHODS_CNQueryAnalyticsLogger
- __OBJC_$_INSTANCE_VARIABLES_CNQueryAnalyticsLogger
- __OBJC_$_PROP_LIST_CNQueryAnalyticsLogger
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNQueryAnalyticsLogger
- __OBJC_$_PROTOCOL_METHOD_TYPES_CNQueryAnalyticsLogger
- __OBJC_$_PROTOCOL_REFS_CNQueryAnalyticsLogger
- __OBJC_CLASS_PROTOCOLS_$_CNQueryAnalyticsLogger
- __OBJC_CLASS_RO_$_CNQueryAnalyticsLogger
- __OBJC_LABEL_PROTOCOL_$_CNQueryAnalyticsLogger
- __OBJC_METACLASS_RO_$_CNQueryAnalyticsLogger
- __OBJC_PROTOCOL_$_CNQueryAnalyticsLogger
- ___41-[CNQueryAnalyticsLogger processIdentity]_block_invoke
- ___54-[CNQueryAnalyticsLogger recordQueryWithFetchRequest:]_block_invoke
- ___69-[CNDataMapperContactStore contactsForFetchRequest:matchInfos:error:]_block_invoke.86
- ___78-[CNDataMapperContactStore executeFetchRequest:progressiveResults:completion:]_block_invoke.94
- ___79-[CNDataMapperContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.62
- ___79-[CNDataMapperContactStore unifiedContactsMatchingPredicate:keysToFetch:error:]_block_invoke.67
- ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.71
- ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.71.cold.1
- ___91-[CNDataMapperContactStore enumerateContactsAndMatchInfoWithFetchRequest:error:usingBlock:]_block_invoke.83
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.495
- ___block_literal_global.499
- ___block_literal_global.805
- ___block_literal_global.856
- ___block_literal_global.865
- ___block_literal_global.92
- _objc_msgSend$cn_hasHighSpecificity
- _objc_msgSend$newDefaultLibrary
- _objc_msgSend$processIdentity
- _objc_msgSend$processName
- _objc_msgSend$processNameForAuditToken:
- _objc_msgSend$queryAnalyticsLogger
- _objc_msgSend$recordQueryWithFetchRequest:
- _objc_msgSend$shouldCaptureMetricsForQueries
- _tcc_object_copy_description
CStrings:
+ "@32@0:8d16^@24"
+ "CNDeviceNameDescription"
+ "CNExpiryDateDescription"
+ "CNIsSharingPairedDescription"
+ "CNSharingPairedContactsFetcher"
+ "Error fetching sharing paired contacts: %@"
+ "Exception while fetching sharing paired contacts: %@"
+ "SFCreatePairedContactManager"
+ "Sharing Paired Contact feature flag not enabled (fetchSharingPairedContactsWithTimeout)."
+ "Successfully fetched %lu sharing paired contacts"
+ "Timeout while fetching sharing paired contacts"
+ "Timeout while fetching sharing paired contacts (timeout: %.2fs)"
+ "_deviceName"
+ "_expiryDate"
+ "_isSharingPaired"
+ "deviceName"
+ "deviceNameDescription"
+ "expiryDate"
+ "expiryDateDescription"
+ "fetchAllContactsWithCompletion:"
+ "fetchSharingPairedContactsWithCompletion:"
+ "fetchSharingPairedContactsWithTimeout:error:"
+ "isSharingPaired"
+ "isSharingPairedDescription"
+ "newDefaultLibraryWithBundle:error:"
+ "setDeviceName:"
+ "setExpiryDate:"
+ "setIsSharingPaired:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/Sharing.framework/Sharing"
- "(Null)"
- "@\"<CNQueryAnalyticsLogger>\""
- "@\"CNAuditToken\""
- "@\"CNPair\""
- "CNQueryAnalyticsLogger"
- "INVALID"
- "NonUI"
- "NotShowing"
- "Showing"
- "T@\"<CNKeyboardStateMonitor>\",&,N,V_keyboardStateMonitor"
- "T@\"<CNQueryAnalyticsLogger>\",R,N,V_queryAnalyticsLogger"
- "T@\"CNAuditToken\",&,N,V_auditToken"
- "T@\"CNPair\",C,N,V_processIdentity"
- "Unknown"
- "_auditToken"
- "_processIdentity"
- "_queryAnalyticsLogger"
- "b"
- "com.apple.contacts.api.query"
- "hasHighSpecificity"
- "newDefaultLibrary"
- "p"
- "predicateClass"
- "processIdentity"
- "processIdentityType"
- "processName"
- "processNameForAuditToken:"
- "queryAnalyticsLogger"
- "recordQueryWithFetchRequest:"
- "setAuditToken:"
- "setProcessIdentity:"
- "shouldCaptureMetricsForQueries"
- "u"

```
