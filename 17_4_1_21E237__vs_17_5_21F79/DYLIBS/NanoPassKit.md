## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1163.8.0.0.0
-  __TEXT.__text: 0x2125b8
+1163.14.2.0.0
+  __TEXT.__text: 0x213bf4
   __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x20464
+  __TEXT.__objc_methlist: 0x204fc
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x165f7
-  __TEXT.__oslogstring: 0x28649
-  __TEXT.__gcc_except_tab: 0x3c80
+  __TEXT.__cstring: 0x1660b
+  __TEXT.__oslogstring: 0x28903
+  __TEXT.__gcc_except_tab: 0x3ca0
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
-  __TEXT.__unwind_info: 0x7ebc
+  __TEXT.__unwind_info: 0x7ea4
   __TEXT.__objc_classname: 0x6451
-  __TEXT.__objc_methname: 0x3b8b4
-  __TEXT.__objc_methtype: 0x96d9
-  __TEXT.__objc_stubs: 0x20180
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0x6490
+  __TEXT.__objc_methname: 0x3bb58
+  __TEXT.__objc_methtype: 0x971f
+  __TEXT.__objc_stubs: 0x20240
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x64e0
   __DATA_CONST.__objc_classlist: 0x1098
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x394e8
-  __DATA_CONST.__objc_selrefs: 0xb5e8
+  __DATA_CONST.__objc_const: 0x396c8
+  __DATA_CONST.__objc_selrefs: 0xb630
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_classrefs: 0x1438
+  __DATA_CONST.__objc_classrefs: 0x1430
   __DATA_CONST.__objc_superrefs: 0xfd8
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__cfstring: 0xe160
+  __AUTH_CONST.__cfstring: 0xe180
   __AUTH_CONST.__objc_const: 0xc2d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__const: 0xcc0

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xc00
-  __AUTH.__objc_data: 0xa5a0
-  __DATA.__objc_ivar: 0x1a74
+  __AUTH.__objc_data: 0xa550
+  __DATA.__objc_ivar: 0x1a84
   __DATA.__data: 0x1bd0
   __DATA.__bss: 0x360
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CEF46BE6-8418-397C-9CB6-14EA9CDF6F0D
-  Functions: 13029
-  Symbols:   39045
-  CStrings:  16097
+  UUID: 43AB4CD3-D415-39F9-92DE-6D5CCD770FAA
+  Functions: 13045
+  Symbols:   39088
+  CStrings:  16123
 
Symbols:
+ +[PKPass(NanoPassKit) npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:commutePlanFields:]
+ +[PKPass(NanoPassKit) npkHandleTransitValuePendingExpiryDate:forCommutePlanField:passWithUniqueID:]
+ -[NPKBalanceField rawCountValue]
+ -[NPKCommutePlanField initWithLabel:detailLabel:formattedValue:rawCountValue:usageDateRange:identifier:details:action:isDeviceBound:pendingUpdateExpireDate:]
+ -[NPKCommutePlanField isActive]
+ -[NPKCommutePlanField isDeviceBound]
+ -[NPKCommutePlanField rawCountValue]
+ -[NPKPassAssociatedInfoManager refreshInfoForPass:]
+ -[NPKPassAssociatedInfoManager setPendingExpirationDate:forCommutePlanField:passWithUniqueID:]
+ -[NPKPassAssociatedInfoModel _fieldForCommutePlan:action:isLegacyPass:balancedByID:]
+ -[NPKPassAssociatedInfoModel _rawCountValueWithCommutePlan:balancesByID:]
+ -[NPKPassAssociatedInfoModel hasDeviceBoundCommutePlans]
+ -[PKPass(NanoPassKit) _hasPlanUpdatedWithFieldIdentifier:fieldInfo:renewalDate:expiryDate:rawCountValue:]
+ -[PKPass(NanoPassKit) npkPendingAddValueStateExpireDateForCommutePlanFieldWithIdentifier:expiryDate:rawCountValue:]
+ GCC_except_table30
+ _OBJC_IVAR_$_NPKBalanceField._rawCountValue
+ _OBJC_IVAR_$_NPKCommutePlanField._isDeviceBound
+ _OBJC_IVAR_$_NPKCommutePlanField._pendingUpdateExpireDate
+ _OBJC_IVAR_$_NPKCommutePlanField._rawCountValue
+ __OBJC_$_PROP_LIST_NPKBalanceField.154
+ __OBJC_$_PROP_LIST_NPKCommutePlanField.211
+ ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.543
+ ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.550
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.370
+ ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.388
+ ___51-[NPKPassAssociatedInfoManager refreshInfoForPass:]_block_invoke
+ ___61-[NPKPassAssociatedInfoManager _fetchMostRecentTilesForPass:]_block_invoke.74
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.75
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.78
+ ___67-[NPKPassAssociatedInfoModel _commutePlanWithFelicaPassProperties:]_block_invoke.100
+ ___73-[NPKPassAssociatedInfoModel _rawCountValueWithCommutePlan:balancesByID:]_block_invoke
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.525
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.527
+ ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.528
+ ___87-[NPKPassAssociatedInfoManager _fetchMostRecentTransitPropertiesAndAppletStateForPass:]_block_invoke.72
+ ___94-[NPKPassAssociatedInfoManager setPendingExpirationDate:forCommutePlanField:passWithUniqueID:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e28_v32?0"PKPassField"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e37_v32?0"PKTransitCommutePlan"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.519
+ ___block_literal_global.524
+ _objc_msgSend$_fieldForCommutePlan:action:isLegacyPass:balancedByID:
+ _objc_msgSend$_hasPlanUpdatedWithFieldIdentifier:fieldInfo:renewalDate:expiryDate:rawCountValue:
+ _objc_msgSend$_rawCountValueWithCommutePlan:balancesByID:
+ _objc_msgSend$associatedPlan
+ _objc_msgSend$hasExpiredPlanDate
+ _objc_msgSend$initWithLabel:detailLabel:formattedValue:rawCountValue:usageDateRange:identifier:details:action:isDeviceBound:pendingUpdateExpireDate:
+ _objc_msgSend$isDeviceBound
+ _objc_msgSend$npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:commutePlanFields:
+ _objc_msgSend$npkHandleTransitValuePendingExpiryDate:forCommutePlanField:passWithUniqueID:
+ _objc_msgSend$npkPendingAddValueStateExpireDateForCommutePlanFieldWithIdentifier:expiryDate:rawCountValue:
+ _objc_msgSend$rawCountValue
+ _objc_msgSend$serviceProviderLocalizedDisplayName
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$updateWithCommutePlanDetail:
- +[PKPass(NanoPassKit) npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:]
- -[NPKCommutePlanField initWithLabel:detailLabel:formattedValue:usageDateRange:identifier:details:action:]
- _OBJC_CLASS_$_NSCountedSet
- _PKTransitAppletDataFormatNavigo
- __OBJC_$_PROP_LIST_NPKBalanceField.147
- __OBJC_$_PROP_LIST_NPKCommutePlanField.198
- ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.535
- ___111-[NPKContactlessPaymentSessionManager _handleRKEActionRequestedForPass:action:function:withSession:completion:]_block_invoke.542
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.362
- ___152-[NPKContactlessPaymentSessionManagerTransactionContext updateWithConcreteTransactions:ephemeralTransaction:updatedPassTransitItems:paymentApplication:]_block_invoke.380
- ___61-[NPKPassAssociatedInfoManager _fetchMostRecentTilesForPass:]_block_invoke.73
- ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.76
- ___67-[NPKPassAssociatedInfoModel _commutePlanWithFelicaPassProperties:]_block_invoke.104
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.517
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.519
- ___83-[NPKContactlessPaymentSessionManager passesDataSource:didUpdatePasses:withStates:]_block_invoke.520
- ___87-[NPKPassAssociatedInfoManager _fetchMostRecentTransitPropertiesAndAppletStateForPass:]_block_invoke.71
- ___block_descriptor_73_e8_32s40s48s56s64s_e37_v32?0"PKTransitCommutePlan"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.511
- ___block_literal_global.516
- _objc_msgSend$countForObject:
- _objc_msgSend$descriptionText
- _objc_msgSend$initWithLabel:detailLabel:formattedValue:usageDateRange:identifier:details:action:
- _objc_msgSend$npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:
- _objc_msgSend$setDescriptionText:
- _objc_msgSend$setExpiryDate:
- _objc_msgSend$setStartDate:
- _objc_msgSend$setTitleText:
CStrings:
+ "\x01\x18"
+ "@\"NSNumber\"16@0:8"
+ "@44@0:8@16@24B32@36"
+ "@92@0:8@16@24@32@40@48@56@64@72B80@84"
+ "B56@0:8@16@24@32@40@48"
+ "D3581A95-1F64-4EBD-8F71-0CD6B696D766"
+ "Notice: Creating commute plan field with label: %@, tripCount: %@, pendingUpdateExpireDate: %@"
+ "Notice: NPKPassAssociatedInfoManager: Requested refresh for pass with uniqueID %@"
+ "Notice: NPKPassAssociatedInfoManager: setExpirationDate:%@ forCommutePlanField:%@ passWithUniqueID:%@"
+ "Notice: PendingAddValueStateExpireDate for field:%@ expiryDateDidUpdate:%d tripCountDidUpdate: %d"
+ "Notice: PendingAddValueStateExpireDate: %@ for pass %@ field:%@ planUpdated:%d renewalDate: %@"
+ "Notice: Session source is requesting AssistiveTouch enabled alert presentation"
+ "Notice: addValuePending: expiration date or trip count is greater than before pening renew, clearing value pending state"
+ "Notice: addValuePending: npkHandleTransitValuePendingExpiryDate %@ withField:%@ forPassWithID %@ currentExpiry: %@, tripCount: %@"
+ "T@\"NSArray\",&,N,V_dynamicPlans"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSNumber\",R,N,V_rawCountValue"
+ "TB,R,N,V_isDeviceBound"
+ "_fieldForCommutePlan:action:isLegacyPass:balancedByID:"
+ "_hasPlanUpdatedWithFieldIdentifier:fieldInfo:renewalDate:expiryDate:rawCountValue:"
+ "_isDeviceBound"
+ "_rawCountValue"
+ "_rawCountValueWithCommutePlan:balancesByID:"
+ "associatedPlan"
+ "hasDeviceBoundCommutePlans"
+ "hasExpiredPlanDate"
+ "initWithLabel:detailLabel:formattedValue:rawCountValue:usageDateRange:identifier:details:action:isDeviceBound:pendingUpdateExpireDate:"
+ "isDeviceBound"
+ "npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:commutePlanFields:"
+ "npkHandleTransitValuePendingExpiryDate:forCommutePlanField:passWithUniqueID:"
+ "npkPendingAddValueStateExpireDateForCommutePlanFieldWithIdentifier:expiryDate:rawCountValue:"
+ "planExpiry"
+ "planTripCount"
+ "rawCountValue"
+ "refreshInfoForPass:"
+ "serviceProviderLocalizedDisplayName"
+ "setPendingExpirationDate:forCommutePlanField:passWithUniqueID:"
+ "uniqueIdentifier"
+ "updateWithCommutePlanDetail:"
- "\x01\x16"
- "-%lu"
- "941BF1D3-6386-46BB-982F-7C1165FECAAA"
- "@72@0:8@16@24@32@40@48@56@64"
- "Notice: NPKPassAssociatedInfoModel: detected duplicated commute plan identifier:%@. making it unique:%@"
- "T@\"NSSet\",&,N,V_dynamicPlans"
- "countForObject:"
- "descriptionText"
- "initWithLabel:detailLabel:formattedValue:usageDateRange:identifier:details:action:"
- "npkClearTransitValuePendingStateIfNecessaryForPassWithID:withBalanceFields:"
- "setDescriptionText:"
- "setExpiryDate:"
- "setStartDate:"
- "setTitleText:"

```
