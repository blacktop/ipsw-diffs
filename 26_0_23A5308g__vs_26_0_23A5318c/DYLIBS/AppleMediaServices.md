## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.0.76.0.0
-  __TEXT.__text: 0x70565c
+9.0.81.2.4
+  __TEXT.__text: 0x708abc
   __TEXT.__auth_stubs: 0x4900
-  __TEXT.__objc_methlist: 0x21b6c
+  __TEXT.__objc_methlist: 0x21d24
   __TEXT.__const: 0x587c8
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2a92e
+  __TEXT.__cstring: 0x2ac5d
   __TEXT.__swift5_typeref: 0x5aad
-  __TEXT.__swift5_reflstr: 0x3124
+  __TEXT.__swift5_reflstr: 0x3144
   __TEXT.__swift5_assocty: 0xe88
   __TEXT.__constg_swiftt: 0x4750
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_fieldmd: 0x3f70
+  __TEXT.__swift5_fieldmd: 0x3f7c
   __TEXT.__swift5_proto: 0xe60
   __TEXT.__swift5_types: 0x528
   __TEXT.__swift_as_entry: 0x628

   __TEXT.__swift5_capture: 0x2c70
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__oslogstring: 0x2edd0
-  __TEXT.__gcc_except_tab: 0x5c2c
+  __TEXT.__oslogstring: 0x2f506
+  __TEXT.__gcc_except_tab: 0x5ca0
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xfd60
-  __TEXT.__eh_frame: 0x12468
-  __TEXT.__objc_classname: 0x3f0d
-  __TEXT.__objc_methname: 0x434b0
+  __TEXT.__unwind_info: 0x102b8
+  __TEXT.__eh_frame: 0x12464
+  __TEXT.__objc_classname: 0x3f22
+  __TEXT.__objc_methname: 0x43835
   __TEXT.__objc_methtype: 0x77f1
-  __TEXT.__objc_stubs: 0x2dd40
-  __DATA_CONST.__got: 0x19a8
-  __DATA_CONST.__const: 0xbfe8
-  __DATA_CONST.__objc_classlist: 0x13e8
+  __TEXT.__objc_stubs: 0x2e020
+  __DATA_CONST.__got: 0x19b0
+  __DATA_CONST.__const: 0xc0d0
+  __DATA_CONST.__objc_classlist: 0x13f0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xecb0
+  __DATA_CONST.__objc_selrefs: 0xed80
   __DATA_CONST.__objc_protorefs: 0x210
-  __DATA_CONST.__objc_superrefs: 0xc90
+  __DATA_CONST.__objc_superrefs: 0xc98
   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x2498
-  __AUTH_CONST.__const: 0x2af88
-  __AUTH_CONST.__cfstring: 0x219e0
-  __AUTH_CONST.__objc_const: 0x3ad40
-  __AUTH_CONST.__objc_intobj: 0xc48
+  __AUTH_CONST.__const: 0x2b048
+  __AUTH_CONST.__cfstring: 0x21c00
+  __AUTH_CONST.__objc_const: 0x3aed0
+  __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x8b88
-  __AUTH.__data: 0x1e08
-  __DATA.__objc_ivar: 0x1868
-  __DATA.__data: 0x6990
-  __DATA.__bss: 0x174f9
+  __AUTH.__objc_data: 0x8bd8
+  __AUTH.__data: 0x1e18
+  __DATA.__objc_ivar: 0x1878
+  __DATA.__data: 0x6980
+  __DATA.__bss: 0x17519
   __DATA.__common: 0xb60
   __DATA_DIRTY.__objc_ivar: 0x69c
   __DATA_DIRTY.__objc_data: 0x5ac0
-  __DATA_DIRTY.__data: 0x2080
-  __DATA_DIRTY.__bss: 0x41e0
+  __DATA_DIRTY.__data: 0x2070
+  __DATA_DIRTY.__bss: 0x41d0
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC162F89-4539-3D65-934B-CC7D0A1D86D0
-  Functions: 24269
-  Symbols:   50062
-  CStrings:  24949
+  UUID: 7B477ADF-2053-397A-950F-C198861693DE
+  Functions: 24327
+  Symbols:   50234
+  CStrings:  25043
 
Symbols:
+ +[AMSFollowUpItem backingIdentifierForIdentifier:DSID:]
+ +[AMSHardwareOfferItem latestExpirationDateFromItems:]
+ +[AMSHardwareOfferItem shouldBadgeAppWithItems:]
+ +[AMSHardwareOfferItem shouldBadgeRowWithItems:]
+ +[AMSHardwareOfferItem supportsSecureCoding]
+ -[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:]
+ -[AMSFollowUp _clearGroupedHardwareFollowUps]
+ -[AMSFollowUp _clearNonGroupedFollowUpWithBackingIdentifier:]
+ -[AMSFollowUp _date:isLaterThanDate:]
+ -[AMSFollowUp _dateIsInThePast:]
+ -[AMSFollowUp _dropExpiredItems:]
+ -[AMSFollowUp _dsidFromBackingIdentifier:]
+ -[AMSFollowUp _groupedHardwareFollowUpItemBackingIdentifierForDSID:]
+ -[AMSFollowUp _isGroupedHardwareOfferWithBackingIdentifier:]
+ -[AMSFollowUp _isHardwareOfferFollowUpGroupingEnabled]
+ -[AMSFollowUp _itemIsExpired:]
+ -[AMSFollowUp _loadGroupedHardwareOfferFollowUpItemsForDSID:]
+ -[AMSFollowUp _makeGroupedHardwareFollowUpItemFromItems:DSID:]
+ -[AMSFollowUp _postGroupedFollowUpItem:]
+ -[AMSFollowUp _postNonGroupedFollowUpItem:]
+ -[AMSFollowUp _updateGroupedHardwareFollowUpItemWithItems:DSID:error:]
+ -[AMSFollowUp migrateHardwareFollowUpsIfNeeded]
+ -[AMSHardwareOfferItem .cxx_destruct]
+ -[AMSHardwareOfferItem backingIdentifier]
+ -[AMSHardwareOfferItem encodeWithCoder:]
+ -[AMSHardwareOfferItem expiration]
+ -[AMSHardwareOfferItem initWithAMSFollowUpItem:]
+ -[AMSHardwareOfferItem initWithCoder:]
+ -[AMSHardwareOfferItem initWithFollowUpItem:]
+ -[AMSHardwareOfferItem omitAppBadge]
+ -[AMSHardwareOfferItem omitBadge]
+ -[AMSHardwareOfferItem setBackingIdentifier:]
+ -[AMSHardwareOfferItem setExpiration:]
+ -[AMSHardwareOfferItem setOmitAppBadge:]
+ -[AMSHardwareOfferItem setOmitBadge:]
+ _AMSBagKeyFollowUpHardwareFollowUpGroupingEnabled
+ _OBJC_CLASS_$_AMSHardwareOfferItem
+ _OBJC_CLASS_$_FLFollowUpAction
+ _OBJC_IVAR_$_AMSHardwareOfferItem._backingIdentifier
+ _OBJC_IVAR_$_AMSHardwareOfferItem._expiration
+ _OBJC_IVAR_$_AMSHardwareOfferItem._omitAppBadge
+ _OBJC_IVAR_$_AMSHardwareOfferItem._omitBadge
+ _OBJC_METACLASS_$_AMSHardwareOfferItem
+ __OBJC_$_CLASS_METHODS_AMSHardwareOfferItem
+ __OBJC_$_CLASS_PROP_LIST_AMSHardwareOfferItem
+ __OBJC_$_INSTANCE_METHODS_AMSHardwareOfferItem
+ __OBJC_$_INSTANCE_VARIABLES_AMSHardwareOfferItem
+ __OBJC_$_PROP_LIST_AMSHardwareOfferItem
+ __OBJC_CLASS_PROTOCOLS_$_AMSHardwareOfferItem
+ __OBJC_CLASS_RO_$_AMSHardwareOfferItem
+ __OBJC_METACLASS_RO_$_AMSHardwareOfferItem
+ ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.309
+ ___40-[AMSFollowUp _postGroupedFollowUpItem:]_block_invoke
+ ___43-[AMSFollowUp _postNonGroupedFollowUpItem:]_block_invoke
+ ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke
+ ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke.111
+ ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke
+ ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.14
+ ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.18
+ ___48+[AMSHardwareOfferItem shouldBadgeAppWithItems:]_block_invoke
+ ___48+[AMSHardwareOfferItem shouldBadgeRowWithItems:]_block_invoke
+ ___54+[AMSHardwareOfferItem latestExpirationDateFromItems:]_block_invoke
+ ___54-[AMSFollowUp _isHardwareOfferFollowUpGroupingEnabled]_block_invoke
+ ___58-[AMSFollowUp _clearGroupedFollowUpWithBackingIdentifier:]_block_invoke
+ ___60-[AMSFollowUp _isGroupedHardwareOfferWithBackingIdentifier:]_block_invoke
+ ___60-[AMSFollowUp _isGroupedHardwareOfferWithBackingIdentifier:]_block_invoke_2
+ ___61-[AMSFollowUp _clearNonGroupedFollowUpWithBackingIdentifier:]_block_invoke
+ ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.291
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.301
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.304
+ ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.330
+ ___block_descriptor_32_e24_16?0"FLFollowUpItem"8l
+ ___block_descriptor_32_e24_B16?0"FLFollowUpItem"8l
+ ___block_descriptor_32_e30_B16?0"AMSHardwareOfferItem"8l
+ ___block_descriptor_40_e8_32r_e47_v32?0"NSString"8"AMSHardwareOfferItem"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e38_"AMSBinaryPromise"16?0"AMSBoolean"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e32_"AMSPromise"16?0"AMSBoolean"8ls32l8s40l8
+ ___block_literal_global.113
+ _getFLFollowUpControllerClass.softClass
+ _getFLGroupIdentifierAppleServices
+ _getFLGroupIdentifierAppleServicesSymbolLoc.ptr
+ _kFollowUpBackingIdentifierComponentDSID
+ _objc_msgSend$_clearGroupedFollowUpWithBackingIdentifier:
+ _objc_msgSend$_clearGroupedHardwareFollowUps
+ _objc_msgSend$_clearNonGroupedFollowUpWithBackingIdentifier:
+ _objc_msgSend$_date:isLaterThanDate:
+ _objc_msgSend$_dateIsInThePast:
+ _objc_msgSend$_dropExpiredItems:
+ _objc_msgSend$_dsidFromBackingIdentifier:
+ _objc_msgSend$_groupedHardwareFollowUpItemBackingIdentifierForDSID:
+ _objc_msgSend$_isGroupedHardwareOfferWithBackingIdentifier:
+ _objc_msgSend$_isHardwareOfferFollowUpGroupingEnabled
+ _objc_msgSend$_itemIsExpired:
+ _objc_msgSend$_loadGroupedHardwareOfferFollowUpItemsForDSID:
+ _objc_msgSend$_makeGroupedHardwareFollowUpItemFromItems:DSID:
+ _objc_msgSend$_postGroupedFollowUpItem:
+ _objc_msgSend$_postNonGroupedFollowUpItem:
+ _objc_msgSend$_updateGroupedHardwareFollowUpItemWithItems:DSID:error:
+ _objc_msgSend$backingIdentifierForIdentifier:DSID:
+ _objc_msgSend$initWithAMSFollowUpItem:
+ _objc_msgSend$latestExpirationDateFromItems:
+ _objc_msgSend$omitAppBadge
+ _objc_msgSend$omitBadge
+ _objc_msgSend$shouldBadgeAppWithItems:
+ _objc_msgSend$shouldBadgeRowWithItems:
- ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.306
- ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.288
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.298
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.301
- ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.327
CStrings:
+ "%{public}@: Cleared grouped hardware follow ups"
+ "%{public}@: Dropping expired hardware follow up from internal tracking list. Backing identifier: %{public}@"
+ "%{public}@: Failed to %{public}@ grouped hardware offer follow up with identifier: %{public}@. Reason: %{public}@"
+ "%{public}@: Failed to clear grouped hardware follow ups. Error: %@"
+ "%{public}@: Failed to clear old hardware follow after migration to grouped follow ups. Error: %@"
+ "%{public}@: Failed to decode active hardware offers. Assuming no existing offers were present. Error: %@"
+ "%{public}@: Failed to group individual hardware follow ups into a grouped follow up."
+ "%{public}@: Failed to load active hardware offers. Assuming no existing offers were present. Error: %@"
+ "%{public}@: Failed to load active hardware offers. userInfo is missing %@ key. Assuming no existing offers were present."
+ "%{public}@: Failed to post follow up item with identifier %{public}@; Error: %@"
+ "%{public}@: Failed to run hardware follow up migration. Loading pending follow up items failed with error: %@"
+ "%{public}@: Failed to save grouped hardware offer follow up items: %@"
+ "%{public}@: Finished grouping hardware follow ups"
+ "%{public}@: Follow up is a hardware offer. Removing it from grouped hardware follow up items list."
+ "%{public}@: Follow up with identifier %{public}@ is a hardware offer. Adding/updating it to grouped hardware follow up items list."
+ "%{public}@: Grouped hardware follow ups feature flag is disabled. Running clear..."
+ "%{public}@: Hardware offer grouping enabled: OS: %@, bag: %@"
+ "%{public}@: No grouped hardware follow ups to clear"
+ "%{public}@: No hardware follow ups to migrate"
+ "%{public}@: No hardware offer follow ups remaining. Clearing grouped hardware offer follow up item."
+ "%{public}@: Posting grouped hardware offer follow up notification"
+ "%{public}@: Posting/updating grouped hardware offer follow up item"
+ "%{public}@: Successfully  %{public}@ed grouped hardware offer follow up with identifier %{public}@"
+ "%{public}@: Successfully added follow up with identifier: %{public}@ to grouped hardware follow ups"
+ "%{public}@Not Logging Payment Sheet Performance Metrics due to sampling."
+ "@\"AMSPromise\"16@?0@\"AMSBoolean\"8"
+ "@16@?0@\"FLFollowUpItem\"8"
+ "AMSFollowUpGroupedFollowUpItemsKey"
+ "AMSFollowUpGroupedHardwareOfferFollowUpIdentifier"
+ "AMSHardwareOfferItem"
+ "B16@?0@\"AMSHardwareOfferItem\"8"
+ "B16@?0@\"FLFollowUpItem\"8"
+ "Grouped hardware offer follow up action failed"
+ "Grouped hardware offer follow up action failed for unknown reason"
+ "HardwareOfferFollowUpGrouping"
+ "SERVICES_MULTI_FOLLOW_LIST_TITLE"
+ "Services Included with Purchase"
+ "T@\"NSString\",C,N,V_backingIdentifier"
+ "TB,N,V_omitAppBadge"
+ "TB,N,V_omitBadge"
+ "_clearGroupedFollowUpWithBackingIdentifier:"
+ "_clearGroupedHardwareFollowUps"
+ "_clearNonGroupedFollowUpWithBackingIdentifier:"
+ "_date:isLaterThanDate:"
+ "_dateIsInThePast:"
+ "_dropExpiredItems:"
+ "_dsidFromBackingIdentifier:"
+ "_groupedHardwareFollowUpItemBackingIdentifierForDSID:"
+ "_isGroupedHardwareOfferWithBackingIdentifier:"
+ "_isHardwareOfferFollowUpGroupingEnabled"
+ "_itemIsExpired:"
+ "_loadGroupedHardwareOfferFollowUpItemsForDSID:"
+ "_makeGroupedHardwareFollowUpItemFromItems:DSID:"
+ "_omitAppBadge"
+ "_omitBadge"
+ "_postGroupedFollowUpItem:"
+ "_postNonGroupedFollowUpItem:"
+ "_updateGroupedHardwareFollowUpItemWithItems:DSID:error:"
+ "ams-ui://amsui.apple.com/dynamic/marketing#route=hardwareOffers"
+ "backingIdentifierForIdentifier:DSID:"
+ "follow-up-hardware-follow-up-grouping-enabled"
+ "initWithAMSFollowUpItem:"
+ "kAMSHardwareOfferItemExpirationKey"
+ "kAMSHardwareOfferItemIdentifierKey"
+ "kAMSHardwareOfferItemOmitAppBadgeKey"
+ "kAMSHardwareOfferItemOmitBadgeKey"
+ "latestExpirationDateFromItems:"
+ "metrics/performance/samplingPercentageUsersDialogPageRender"
+ "metrics/performance/sessionDurationDialogPageRender"
+ "migrateHardwareFollowUpsIfNeeded"
+ "paymentDialog"
+ "paymentDialogRender"
+ "plain"
+ "post"
+ "setOmitAppBadge:"
+ "setOmitBadge:"
+ "shouldBadgeAppWithItems:"
+ "shouldBadgeRowWithItems:"
+ "v32@?0@\"NSString\"8@\"AMSHardwareOfferItem\"16^B24"
- "%{public}@Logging Payment Sheet Performance Metrics"
- "%{public}@Not Logging Payment Sheet Performance Metrics due to error reading sampling percentage: %{public}@"
- "%{public}@Not Logging Payment Sheet Performance Metrics due to sampling. Random value %f higher than sampling percentage of %f."
- "metrics/paymentSheetPerformanceSamplingPercentage"

```
