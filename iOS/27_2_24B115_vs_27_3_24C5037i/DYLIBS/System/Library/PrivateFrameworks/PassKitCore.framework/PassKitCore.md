## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1696.2.9.0.0
-  __TEXT.__text: 0x8f29c0
-  __TEXT.__objc_methlist: 0x72a68
+1696.3.2.0.0
+  __TEXT.__text: 0x8f66e4
+  __TEXT.__objc_methlist: 0x72bf8
   __TEXT.__const: 0x2d780
   __TEXT.__swift5_typeref: 0x8da0
-  __TEXT.__cstring: 0x74218
+  __TEXT.__cstring: 0x7441c
   __TEXT.__constg_swiftt: 0x7588
   __TEXT.__swift5_reflstr: 0x664d
   __TEXT.__swift5_fieldmd: 0x7de0

   __TEXT.__swift5_assocty: 0xe28
   __TEXT.__swift5_proto: 0x13f0
   __TEXT.__swift5_types: 0x7f8
-  __TEXT.__swift5_capture: 0x543c
-  __TEXT.__oslogstring: 0x3cc99
+  __TEXT.__swift5_capture: 0x5454
+  __TEXT.__oslogstring: 0x3cc7a
   __TEXT.__swift_as_entry: 0x198
-  __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__swift_as_cont: 0x3b4
+  __TEXT.__swift_as_ret: 0x1bc
+  __TEXT.__swift_as_cont: 0x3ac
   __TEXT.__swift5_mpenum: 0x140
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x6ae8
-  __TEXT.__ustring: 0x1e6c
-  __TEXT.__unwind_info: 0x27270
-  __TEXT.__eh_frame: 0x8a08
+  __TEXT.__gcc_except_tab: 0x6bbc
+  __TEXT.__ustring: 0x1e76
+  __TEXT.__unwind_info: 0x27360
+  __TEXT.__eh_frame: 0x8978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x23898
+  __DATA_CONST.__const: 0x239e8
   __DATA_CONST.__objc_classlist: 0x3e48
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25408
+  __DATA_CONST.__objc_selrefs: 0x254f8
   __DATA_CONST.__objc_protorefs: 0x260
   __DATA_CONST.__objc_superrefs: 0x3158
-  __DATA_CONST.__objc_arraydata: 0x2810
+  __DATA_CONST.__objc_arraydata: 0x2870
   __DATA_CONST.__got: 0x53a0
-  __AUTH_CONST.__const: 0x27208
-  __AUTH_CONST.__cfstring: 0x7a540
-  __AUTH_CONST.__objc_const: 0xd07c0
+  __AUTH_CONST.__const: 0x27258
+  __AUTH_CONST.__cfstring: 0x7a740
+  __AUTH_CONST.__objc_const: 0xd08c0
   __AUTH_CONST.__objc_arrayobj: 0xd20
   __AUTH_CONST.__objc_intobj: 0x11d0
-  __AUTH_CONST.__objc_dictobj: 0x15b8
+  __AUTH_CONST.__objc_dictobj: 0x1608
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH_CONST.__auth_got: 0x3010
+  __AUTH_CONST.__auth_got: 0x3018
   __AUTH.__objc_data: 0x20b58
   __AUTH.__data: 0x59a8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x7348
+  __DATA.__objc_ivar: 0x735c
   __DATA.__data: 0xa2b0
-  __DATA.__common: 0xc49
+  __DATA.__common: 0xc39
   __DATA_DIRTY.__objc_ivar: 0x1f58
   __DATA_DIRTY.__objc_data: 0x7940
   __DATA_DIRTY.__data: 0x188

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 55940
-  Symbols:   79209
-  CStrings:  21823
+  Functions: 55997
+  Symbols:   79277
+  CStrings:  21835
 
Symbols:
+ +[PKPaymentCommutePlanDetail nextBoundaryDateForPlans:]
+ +[PKTransitCommutePlan(Utilities) activationPromptForCommutePlan:pass:balanceModel:]
+ +[PKTransitCommutePlan(Utilities) dateStringForDate:field:]
+ +[PKTransitCommutePlan(Utilities) displayDateStringForCommutePlan:pass:balanceModel:style:allowsActivationPrompt:]
+ +[PKTransitCommutePlan(Utilities) localizableStringsFromTickets:]
+ +[PKTransitCommutePlan(Utilities) routeStringFromDeparture:destination:bidirectional:]
+ +[PKTransitCommutePlan(Utilities) routeStringFromTicket:isReloadableTicketsPass:localizedStrings:]
+ +[PKTransitCommutePlan(Utilities) stationCodeFromTicket:stationType:localizedStrings:]
+ -[PKDataAccessor passLocalizedStringsForKeys:completion:]
+ -[PKFileDataAccessor passLocalizedStringsForKeys:completion:]
+ -[PKObject localizedStrings:completion:]
+ -[PKPassLibrary passLocalizedStringsForKeys:uniqueID:completion:]
+ -[PKPaymentCommutePlanDetail isActivatedValue]
+ -[PKPaymentCommutePlanDetail retirementDate]
+ -[PKPaymentCommutePlanDetail setIsActivatedValue:]
+ -[PKPaymentCommutePlanDetail setRetirementDate:]
+ -[PKPaymentCommutePlanDetail setTicketState:]
+ -[PKPaymentCommutePlanDetail ticketState]
+ -[PKPaymentDefaultDataProvider _schedulePlanRedelivery:forPassUniqueIdentifier:]
+ -[PKPaymentService(Identity) generateIdentityPrearmTrustKeyMaterialForDeviceID:completion:]
+ -[PKRemoteDataAccessor passLocalizedStringsForKeys:completion:]
+ -[PKTicketDetails transitStatus]
+ -[PKTransitBalanceModel _canStillUseHybridPlan:]
+ -[PKTransitBalanceModel _hasActiveTicketWindowForCommutePlan:]
+ -[PKTransitBalanceModel _summaryForCommutePlans:isExpired:]
+ -[PKTransitBalanceModel _ticketForCommutePlan:]
+ -[PKTransitBalanceModel commutePlanDetailForTicket:]
+ -[PKTransitBalanceModel getDisplayableCommutePlanDetailsForPlans:title:value:subtitle:isExpired:]
+ -[PKTransitBalanceModel getDisplayableTicketDetailsForTitle:value:subtitle:isExpired:]
+ -[PKTransitBalanceModel hasRemainingCommutePlanContent]
+ -[PKTransitBalanceModel hasTicketContent]
+ -[PKTransitBalanceModel isRetiredTicket:]
+ -[PKTransitBalanceModel localizedStatusForTicket:]
+ -[PKTransitBalanceModel localizedTicketStrings]
+ -[PKTransitBalanceModel localizedTransitStatusForTicket:]
+ -[PKTransitBalanceModel pulledOutCommutePlanWithRemainingPlans:]
+ -[PKTransitBalanceModel remainingCommutePlans]
+ -[PKTransitBalanceModel setLocalizedTicketStrings:]
+ -[PKTransitBalanceModel shouldCollectPlan:withAction:]
+ -[PKTransitBalanceModel transitStatusForTicket:]
+ GCC_except_table201
+ GCC_except_table233
+ GCC_except_table257
+ GCC_except_table294
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table305
+ GCC_except_table318
+ GCC_except_table327
+ GCC_except_table332
+ GCC_except_table339
+ GCC_except_table344
+ GCC_except_table368
+ GCC_except_table377
+ GCC_except_table399
+ GCC_except_table415
+ GCC_except_table477
+ GCC_except_table485
+ GCC_except_table490
+ GCC_except_table550
+ GCC_except_table558
+ GCC_except_table560
+ GCC_except_table584
+ GCC_except_table602
+ GCC_except_table702
+ GCC_except_table746
+ GCC_except_table754
+ _OBJC_IVAR_$_PKPaymentCommutePlanDetail._isActivatedValue
+ _OBJC_IVAR_$_PKPaymentCommutePlanDetail._retirementDate
+ _OBJC_IVAR_$_PKPaymentCommutePlanDetail._ticketState
+ _OBJC_IVAR_$_PKPaymentDefaultDataProvider._planBoundaryTimers
+ _OBJC_IVAR_$_PKTicketDetails._transitStatus
+ _OBJC_IVAR_$_PKTransitBalanceModel._localizedTicketStrings
+ _OBJC_IVAR_$_PKTransitBalanceModel._pulledOutCommutePlan
+ _OBJC_IVAR_$_PKTransitBalanceModel._remainingCommutePlans
+ _PKHowToUseWalletCapabilityStringHomeButton
+ _PKHowToUseWalletCapabilityStringSideButton
+ _PKISO23220_1_PhotoID_FamilyNameUnicode
+ _PKISO23220_1_PhotoID_GivenNameUnicode
+ _PKISO23220_1_PhotoID_IssuingAuthorityUnicode
+ _PKLocalizedTicketString
+ _PKRouteArrowBidirectional
+ _PKRouteArrowUnidirectional
+ _PKUnsetDisplayProperties
+ __PKCommutePlanExpiryString
+ __PKDictionaryByDeepMergingPrivateOverRoot
+ __PKFormatDateWithPassField
+ __PKOptionalJSONDictionaryAtURL
+ __Z19_PKGetPassWidthType6CGSizeS_
+ ___40-[PKObject localizedStrings:completion:]_block_invoke
+ ___40-[PKObject localizedStrings:completion:]_block_invoke_2
+ ___48-[PKFileDataAccessor passLocalizedStringForKey:]_block_invoke
+ ___52-[PKTransitCommutePlan updateWithCommutePlanDetail:]_block_invoke
+ ___61-[PKFileDataAccessor passLocalizedStringsForKeys:completion:]_block_invoke
+ ___62-[PKTransitBalanceModel _hasActiveTicketWindowForCommutePlan:]_block_invoke
+ ___65-[PKPassLibrary passLocalizedStringsForKeys:uniqueID:completion:]_block_invoke
+ ___73-[PKPaymentPassContent initWithDictionary:bundle:privateBundle:passType:]_block_invoke
+ ___73-[PKPaymentPassContent initWithDictionary:bundle:privateBundle:passType:]_block_invoke_2
+ ___80-[PKPaymentDefaultDataProvider _schedulePlanRedelivery:forPassUniqueIdentifier:]_block_invoke
+ ___80-[PKPaymentDefaultDataProvider _schedulePlanRedelivery:forPassUniqueIdentifier:]_block_invoke_2
+ ___80-[PKPaymentDefaultDataProvider _schedulePlanRedelivery:forPassUniqueIdentifier:]_block_invoke_3
+ ___83-[PKPaymentDefaultDataProvider plansForPaymentPassWithUniqueIdentifier:completion:]_block_invoke
+ ___91-[PKPaymentService(Identity) generateIdentityPrearmTrustKeyMaterialForDeviceID:completion:]_block_invoke
+ ___PKSetDisplayProperties_block_invoke
+ ___PKSetDisplayProperties_block_invoke_2
+ ____PKDictionaryByDeepMergingPrivateOverRoot_block_invoke
+ ___block_descriptor_40_e8_32s_e21_16?0"PKPassField"8ls32l8
+ ___block_descriptor_40_e8_32s_e36_B16?0"PKPaymentCommutePlanDetail"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e65_v24?0"PKAuxiliaryCapabilityRequirementKeyMaterial"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___swift_closure_destructor.60Tm
+ _malloc_type_calloc
- +[PKTransitBalanceModel shouldCollectPlan:withAction:]
- +[PKTransitCommutePlan(Utilities) routeStringFromTicket:isReloadableTicketsPass:]
- +[PKTransitCommutePlan(Utilities) stationCodeFromTicket:stationType:]
- -[PKFileDataAccessor _passLocalizedStringForKey:preferredLanguages:]
- -[PKObject localizedString:]
- -[PKTicketStationDetails boardingZone]
- -[PKTicketStationDetails platformBoardingPosition]
- -[PKTicketStationDetails platform]
- -[PKTransitBalanceModel getDisplayableCommutePlanDetailsForTitle:value:subtitle:isExpired:]
- GCC_except_table198
- GCC_except_table231
- GCC_except_table254
- GCC_except_table288
- GCC_except_table298
- GCC_except_table300
- GCC_except_table302
- GCC_except_table315
- GCC_except_table324
- GCC_except_table326
- GCC_except_table336
- GCC_except_table341
- GCC_except_table374
- GCC_except_table378
- GCC_except_table396
- GCC_except_table412
- GCC_except_table479
- GCC_except_table482
- GCC_except_table547
- GCC_except_table555
- GCC_except_table557
- GCC_except_table572
- GCC_except_table599
- GCC_except_table697
- GCC_except_table741
- GCC_except_table749
- _OBJC_IVAR_$_PKTicketStationDetails._boardingZone
- _OBJC_IVAR_$_PKTicketStationDetails._platform
- _OBJC_IVAR_$_PKTicketStationDetails._platformBoardingPosition
- __OBJC_$_CLASS_METHODS_PKTransitBalanceModel
- __PKFormatCommutePlanDate
- __PKNormalizedLanguageIdentifier
- __Z19_PKGetPassWidthType6CGSize
- ___displayPropertiesSet
- ___swift_closure_destructor.54Tm
CStrings:
+ " - "
+ "B16@?0@\"PKPaymentCommutePlanDetail\"8"
+ "COMMUTE_PLAN_COUNT_BASED_NUMBER_OF_RIDES_CROSSINGS"
+ "COMMUTE_PLAN_COUNT_BASED_NUMBER_OF_RIDES_EXCURSIONS"
+ "COMMUTE_PLAN_COUNT_BASED_NUMBER_OF_RIDES_JOURNEYS"
+ "Delegated payment request must not specify a merchant identifier"
+ "HomeButton"
+ "IsVirtualDevice"
+ "PKFieldUnitTypeNone, PKFieldUnitTypeDefault, PKFieldUnitTypeRides, PKFieldUnitTypeTickets, PKFieldUnitTypeLoyaltyPoints, PKFieldUnitTypeCrossings, PKFieldUnitTypeJourneys, PKFieldUnitTypeExcursions"
+ "PKPaymentRequest merchantIdentifier must not be set when isDelegatedRequest is true"
+ "SideButton"
+ "TICKET_STATUS_ACTIVE"
+ "TICKET_STATUS_PENDING"
+ "TICKET_STATUS_SUSPENDED"
+ "TICKET_TRANSIT_STATUS_CANCELLED"
+ "TICKET_TRANSIT_STATUS_DELAYED"
+ "TICKET_TRANSIT_STATUS_ON_TIME"
+ "[%s] Failed to remove pass %s locally: %@"
+ "cardHomeButtonTouchID"
+ "cardSideButtonTouchID"
+ "companionPreArmTrust"
+ "countRemaining"
+ "dot.list.bullet.page"
+ "isActivatedValue"
+ "retirementDate"
+ "ticketState"
+ "v24@?0@\"PKAuxiliaryCapabilityRequirementKeyMaterial\"8@\"NSError\"16"
+ "\u2068%@\u2069"
- "\r"
- "Attachment collection failed: "
- "Failed to launch TapToRadar: "
- "PKFieldUnitTypeNone, PKFieldUnitTypeDefault, PKFieldUnitTypeRides, PKFieldUnitTypeTickets, PKFieldUnitTypeLoyaltyPoints"
- "RemoteDeviceSelections"
- "TapToProvisionRefresh"
- "TapToRadar: URL generation failed: %@"
- "TapToRadar: attachment collection failed: %@"
- "TapToRadar: collected %ld attachment(s)"
- "boardingZone: %@; "
- "cardTouchID"
- "platform"
- "platform: %@; "
- "platformBoardingPosition"
- "platformBoardingPosition: %@; "
- "text.rectangle.page"
```
