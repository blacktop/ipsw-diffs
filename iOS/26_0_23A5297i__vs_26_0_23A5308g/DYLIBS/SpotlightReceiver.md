## SpotlightReceiver

> `/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0x89a4
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x5fc
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x530
-  __TEXT.__cstring: 0x809
-  __TEXT.__oslogstring: 0x595
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methname: 0x1c4b
-  __TEXT.__objc_methtype: 0x3e5
-  __TEXT.__objc_stubs: 0x14c0
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x2e8
-  __DATA_CONST.__objc_classlist: 0x20
+2391.1.0.0.0
+  __TEXT.__text: 0x9bdc
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x714
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x5b8
+  __TEXT.__cstring: 0x8d9
+  __TEXT.__oslogstring: 0x61b
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_classname: 0xd1
+  __TEXT.__objc_methname: 0x208b
+  __TEXT.__objc_methtype: 0x493
+  __TEXT.__objc_stubs: 0x1820
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x7a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0xb00
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0xe80
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xac
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x160
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E063DAC-903F-3268-BEF3-B48CC532E39E
-  Functions: 186
-  Symbols:   853
-  CStrings:  565
+  UUID: 53F5D58E-C830-336C-8E3C-3EF0CA83E4C7
+  Functions: 214
+  Symbols:   987
+  CStrings:  646
 
Symbols:
+ -[CSReceiverConnection fetchableIdentifiersFromDonation:additionalAttributes:config:]
+ -[CSReceiverConnection fetchableIdentifiersFromDonation:additionalAttributes:config:].cold.1
+ -[CSReceiverConnection indexForBundleID:protectionClass:]
+ -[SpotlightReceiverDonation errorAttributeName]
+ -[SpotlightReceiverDonation errorCodeAttributeName]
+ -[SpotlightReceiverDonation initWithVersionName:versionValue:]
+ -[SpotlightReceiverDonation versionName]
+ -[SpotlightReceiverDonation versionValue]
+ -[SpotlightReceiverResponse .cxx_destruct]
+ -[SpotlightReceiverResponse donation]
+ -[SpotlightReceiverResponse error]
+ -[SpotlightReceiverResponse initWithDonation:]
+ -[SpotlightReceiverResponse setError:]
+ -[SpotlightReceiverResponse setStatus:]
+ -[SpotlightReceiverResponse setUpdate:forItem:]
+ -[SpotlightReceiverResponse status]
+ -[SpotlightReceiverResponse(Internal) donation]
+ -[SpotlightReceiverResponse(Internal) enumerateUpdatesUsingBlock:]
+ -[SpotlightReceiverUpdate .cxx_destruct]
+ -[SpotlightReceiverUpdate attributes]
+ -[SpotlightReceiverUpdate info]
+ -[SpotlightReceiverUpdate initWithStatus:info:attributes:]
+ -[SpotlightReceiverUpdate status]
+ GCC_except_table142
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table81
+ GCC_except_table85
+ _CFStringCreateWithBytesNoCopy
+ _CSDecodeObject
+ _OBJC_CLASS_$_CSCustomAttributeKey
+ _OBJC_CLASS_$_SpotlightReceiverResponse
+ _OBJC_CLASS_$_SpotlightReceiverUpdate
+ _OBJC_IVAR_$_CSReceiverConnection._indexes
+ _OBJC_IVAR_$_CSReceiverConnection._lock
+ _OBJC_IVAR_$_SpotlightReceiverDonation._errorAttributeName
+ _OBJC_IVAR_$_SpotlightReceiverDonation._errorCodeAttributeName
+ _OBJC_IVAR_$_SpotlightReceiverDonation._versionName
+ _OBJC_IVAR_$_SpotlightReceiverDonation._versionValue
+ _OBJC_IVAR_$_SpotlightReceiverResponse._donation
+ _OBJC_IVAR_$_SpotlightReceiverResponse._error
+ _OBJC_IVAR_$_SpotlightReceiverResponse._status
+ _OBJC_IVAR_$_SpotlightReceiverResponse._updates
+ _OBJC_IVAR_$_SpotlightReceiverUpdate._attributes
+ _OBJC_IVAR_$_SpotlightReceiverUpdate._info
+ _OBJC_IVAR_$_SpotlightReceiverUpdate._status
+ _OBJC_METACLASS_$_SpotlightReceiverResponse
+ _OBJC_METACLASS_$_SpotlightReceiverUpdate
+ _OUTLINED_FUNCTION_3
+ _SpotlightReceiverErrorDomain
+ _SpotlightReceiverMessageInfoKey
+ __MDPlistDictionaryIterate
+ __OBJC_$_INSTANCE_METHODS_SpotlightReceiverResponse(Internal)
+ __OBJC_$_INSTANCE_METHODS_SpotlightReceiverUpdate
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightReceiverResponse
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightReceiverUpdate
+ __OBJC_$_PROP_LIST_SpotlightReceiverResponse
+ __OBJC_$_PROP_LIST_SpotlightReceiverUpdate
+ __OBJC_CLASS_RO_$_SpotlightReceiverResponse
+ __OBJC_CLASS_RO_$_SpotlightReceiverUpdate
+ __OBJC_METACLASS_RO_$_SpotlightReceiverResponse
+ __OBJC_METACLASS_RO_$_SpotlightReceiverUpdate
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.455
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.455.cold.1
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.459
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2.460
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_3
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_3.462
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_4
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.386
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.469
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.470
+ ___85-[CSReceiverConnection fetchableIdentifiersFromDonation:additionalAttributes:config:]_block_invoke
+ ___block_descriptor_123_e8_32s40s48s56s64s72s80s88s96s104r112r_e54_v96?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r104l8r112l8
+ ___block_descriptor_155_e8_32s40s48s56s64s72s80s88s96s104r112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r104l8r112l8
+ ___block_descriptor_40_e8_32r_e30_v24?0"CSSearchableItem"8^B16lr32l8
+ ___block_descriptor_44_e8_32r_e8_v12?0i8lr32l8
+ ___block_descriptor_48_e8_32s40r_e35_v16?0"SpotlightReceiverResponse"8lr40l8s32l8
+ ___block_descriptor_52_e8_32s40r_e11_v20?0i8q12ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e26_v48?0r*8Q16{?=*Q{?=IC}}24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e17_v16?0"NSArray"8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e35_v16?0"SpotlightReceiverResponse"8lr64l8r72l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_literal_global.458
+ ___block_literal_global.544
+ _kCFAllocatorNull
+ _kCFNull
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$addAttributesFromDictionary:
+ _objc_msgSend$allKeys
+ _objc_msgSend$attributes
+ _objc_msgSend$donation
+ _objc_msgSend$enumerateUpdatesUsingBlock:
+ _objc_msgSend$errorAttributeName
+ _objc_msgSend$errorCodeAttributeName
+ _objc_msgSend$fetchableIdentifiersFromDonation:additionalAttributes:config:
+ _objc_msgSend$incrementAttributeValue:forKey:
+ _objc_msgSend$indexForBundleID:protectionClass:
+ _objc_msgSend$info
+ _objc_msgSend$initWithKeyName:searchable:searchableByDefault:unique:multiValued:
+ _objc_msgSend$initWithName:protectionClass:bundleIdentifier:
+ _objc_msgSend$initWithVersionName:versionValue:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$items
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$processDonation:completionHandler:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$setValue:forCustomKey:
+ _objc_msgSend$slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:
+ _objc_msgSend$status
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$versionName
+ _objc_msgSend$versionValue
+ _objc_retain_x24
+ _objc_retain_x26
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table134
- GCC_except_table71
- GCC_except_table79
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.445
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.445.cold.1
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.449
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2.450
- ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.385
- ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.456
- ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.457
- ___block_descriptor_104_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_131_e8_32s40s48s56s64s72s80r88r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
- ___block_descriptor_44_e8_32r_e20_v20?0i8"NSError"12lr32l8
- ___block_descriptor_99_e8_32s40s48s56s64s72s80r88r_e54_v96?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
- ___block_literal_global.448
- ___block_literal_global.525
- _objc_msgSend$handleDonation:completionHandler:
- _objc_msgSend$stringWithUTF8String:
CStrings:
+ "### SCHEDULED RECEIVER ignoring already processing item %@ [%@]"
+ "### SCHEDULED RECEIVER request timed out waiting for index validation"
+ "%@%@Error"
+ "%@%@ErrorCode"
+ "@\"<SpotlightReceiverInfo>\""
+ "@\"NSDictionary\""
+ "@\"NSError\""
+ "@\"SpotlightReceiverDonation\""
+ "@40@0:8@16@24@32"
+ "@40@0:8q16@24@32"
+ "Internal"
+ "SKG"
+ "SpotlightReceiverErrorDomain"
+ "SpotlightReceiverResponse"
+ "SpotlightReceiverUpdate"
+ "SpotlightResources"
+ "T@\"<SpotlightReceiverInfo>\",R,N,V_info"
+ "T@\"NSArray\",&,N,V_identifiers"
+ "T@\"NSArray\",&,N,V_items"
+ "T@\"NSDictionary\",R,N,V_attributes"
+ "T@\"NSError\",C,N,V_error"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",C,N,V_bundleIdentifier"
+ "T@\"NSString\",C,N,V_configName"
+ "T@\"NSString\",C,N,V_journalCookie"
+ "T@\"NSString\",C,N,V_protectionClass"
+ "T@\"SpotlightReceiverDonation\",R,N,V_donation"
+ "TQ,N,V_serialNumber"
+ "Tq,N,V_donationType"
+ "Tq,N,V_indexType"
+ "Tq,N,V_status"
+ "Tq,R,N,V_status"
+ "Version"
+ "_"
+ "_attributes"
+ "_donation"
+ "_error"
+ "_errorAttributeName"
+ "_errorCodeAttributeName"
+ "_indexes"
+ "_info"
+ "_lock"
+ "_status"
+ "_updates"
+ "addAttributesFromDictionary:"
+ "allKeys"
+ "attributes"
+ "donation"
+ "enumerateUpdatesUsingBlock:"
+ "error"
+ "errorAttributeName"
+ "errorCodeAttributeName"
+ "fetchableIdentifiersFromDonation:additionalAttributes:config:"
+ "incrementAttributeValue:forKey:"
+ "indexForBundleID:protectionClass:"
+ "info"
+ "initWithDonation:"
+ "initWithKeyName:searchable:searchableByDefault:unique:multiValued:"
+ "initWithName:protectionClass:bundleIdentifier:"
+ "initWithStatus:info:attributes:"
+ "initWithVersionName:versionValue:"
+ "isEqualToNumber:"
+ "messageInfoKey"
+ "mutableCopy"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "processDonation:completionHandler:"
+ "pstatus"
+ "removeAllObjects"
+ "removeObject:"
+ "setError:"
+ "setStatus:"
+ "setUpdate:forItem:"
+ "setValue:forCustomKey:"
+ "slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "uniqueIdentifier"
+ "v12@?0i8"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"SpotlightReceiverResponse\"8"
+ "v20@?0i8q12"
+ "v24@0:8@?16"
+ "v24@?0@\"CSSearchableItem\"8^B16"
+ "v48@?0r*8Q16{?=*Q{?=IC}}24"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "SenderUpdate"
- "T@\"NSArray\",R,N,V_identifiers"
- "T@\"NSArray\",R,N,V_items"
- "T@\"NSString\",R,N,V_bundleIdentifier"
- "T@\"NSString\",R,N,V_configName"
- "T@\"NSString\",R,N,V_journalCookie"
- "T@\"NSString\",R,N,V_protectionClass"
- "TQ,R,N,V_serialNumber"
- "Tq,R,N,V_donationType"
- "Tq,R,N,V_indexType"
- "stringWithUTF8String:"
- "v20@?0i8@\"NSError\"12"

```
