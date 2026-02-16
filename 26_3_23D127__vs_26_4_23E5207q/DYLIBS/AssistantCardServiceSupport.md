## AssistantCardServiceSupport

> `/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport`

```diff

-3515.12.1.0.0
-  __TEXT.__text: 0x449c
-  __TEXT.__auth_stubs: 0x2b0
+3520.88.6.1.4
+  __TEXT.__text: 0x49c8
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x220

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5d0
-  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__auth_got: 0x138
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x7c0

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D7DFADA-0761-31AD-B578-DFDA92F50153
+  UUID: 696026D9-E4F2-3312-A070-0F2B8F109602
   Functions: 58
-  Symbols:   467
+  Symbols:   462
   CStrings:  285
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[INAddTasksIntent(ACSCardRequesting) requestCard:reply:] : 1052 -> 1128
~ ___57-[INAddTasksIntent(ACSCardRequesting) requestCard:reply:]_block_invoke : 548 -> 576
~ -[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:] : 248 -> 264
~ ___76-[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:]_block_invoke : 116 -> 120
~ -[INCurrencyAmount(AssistantCardService) _acs_currencySymbol] : 92 -> 100
~ +[INCurrencyAmount(AssistantCardService) _acs_localeForCode:] : 376 -> 388
~ +[INCurrencyAmount(AssistantCardService) _acs_currencySymbolForCode:] : 212 -> 224
~ -[ACSCardService canSatisfyCardRequest:] : 156 -> 172
~ -[ACSCardService requestCard:reply:] : 680 -> 712
~ -[ACSCardService servicePriorityForRequest:] : 184 -> 204
~ -[INIntent(ACSCardRequesting) acs_needsTitleCardSection] : 64 -> 68
~ -[INIntent(ACSCardRequesting) requestCard:reply:] : 312 -> 320
~ -[INStartWorkoutIntent(ACSCardRequesting) requestCard:reply:] : 828 -> 896
~ -[CLPlacemark(AssistantCardService) acs_formattedNameOrStreetAddress] : 272 -> 300
~ -[INRequestPaymentIntent(ACSCardRequesting) requestCard:reply:] : 1988 -> 2180
~ +[SFCardSection(AssistantCardService) acs_uniquelyIdentifiedCardSection] : 120 -> 128
~ -[SFCardSection(AssistantCardService) acs_setParameters:] : 348 -> 352
~ -[SFCardSection(AssistantCardService) acs_addParameter:] : 216 -> 232
~ -[SFCardSection(AssistantCardService) acs_parameterKeyPathFromParameter:] : 272 -> 296
~ +[SFNullCardSection(AssistantCardService) acs_wildCardSection] : 80 -> 84
~ -[INPriceRange(AssistantCardService) acs_formattedRangeString] : 376 -> 412
~ ___62-[INPriceRange(AssistantCardService) acs_formattedRangeString]_block_invoke : 192 -> 200
~ +[INPriceRange(AssistantCardService) _localeForCode:] : 376 -> 388
~ +[INPriceRange(AssistantCardService) _currencySymbolForCode:] : 212 -> 224
~ -[INPlayMediaIntent(ACSCardRequesting) requestCard:reply:] : 1376 -> 1496
~ -[INPaymentAccount(AssistantCardService) acs_formattedAccountName] : 148 -> 168
~ -[INSendPaymentIntent(ACSCardRequesting) requestCard:reply:] : 1988 -> 2180
~ -[INTextNoteContent(INCreateNoteIntentCardRequesting) acs_cardSection] : 108 -> 116
~ -[INImageNoteContent(INCreateNoteIntentCardRequesting) acs_cardSection] : 232 -> 244
~ -[INCreateNoteIntent(ACSCardRequesting) requestCard:reply:] : 580 -> 608
~ -[INCreateNoteIntent(ACSCardRequesting) _buildCardFromRequest:reply:] : 1380 -> 1488
~ ___69-[INCreateNoteIntent(ACSCardRequesting) _buildCardFromRequest:reply:]_block_invoke : 188 -> 196
~ -[INIntent(AssistantCardService) acs_utteranceForCardService] : 388 -> 420
~ +[ACSCardServiceHelper rowCardSectionFromLeadingText:trailingText:] : 192 -> 200
~ +[ACSCardServiceHelper formattedDateTimeStringFromDateComponents:] : 144 -> 156
~ +[ACSCardServiceHelper formattedDateTimeStringFromDate:] : 108 -> 112
~ +[ACSCardServiceHelper addParameterToSection:selectorStrings:class:] : 184 -> 196
~ -[INPerson(AssistantCardService) acs_formattedPersonName] : 100 -> 108
~ +[SFCard(AssistantCardService) acs_uniquelyIdentifiedCard] : 120 -> 128
~ -[SFCard(AssistantCardService) acs_setInteraction:] : 520 -> 592
~ -[SFCard(AssistantCardService) acs_interaction] : 212 -> 236

```
