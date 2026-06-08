## AssistantCardServiceSupport

> `/System/Library/PrivateFrameworks/AssistantCardServiceSupport.framework/AssistantCardServiceSupport`

```diff

-3525.5.11.11.1
-  __TEXT.__text: 0x49c8
-  __TEXT.__auth_stubs: 0x260
+3600.49.31.1.6
+  __TEXT.__text: 0x44a0
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x220
   __TEXT.__oslogstring: 0x39
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0xd52
-  __TEXT.__objc_methtype: 0x185
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x160
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5d0
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x7c0
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x38

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A341B868-C196-3777-883E-D34CEF37F397
+  UUID: EF07AE51-6403-3FFC-96E5-415FFA07D60E
   Functions: 58
-  Symbols:   462
-  CStrings:  285
+  Symbols:   467
+  CStrings:  60
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ -[INAddTasksIntent(ACSCardRequesting) requestCard:reply:] : 1128 -> 1052
~ ___57-[INAddTasksIntent(ACSCardRequesting) requestCard:reply:]_block_invoke : 576 -> 544
~ -[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:] : 264 -> 244
~ ___76-[INCurrencyAmount(AssistantCardService) _acs_formattedStringIncludeSymbol:]_block_invoke : 120 -> 116
~ -[INCurrencyAmount(AssistantCardService) _acs_currencySymbol] : 100 -> 92
~ +[INCurrencyAmount(AssistantCardService) _acs_localeForCode:] : 388 -> 380
~ +[INCurrencyAmount(AssistantCardService) _acs_currencySymbolForCode:] : 224 -> 212
~ -[ACSCardService canSatisfyCardRequest:] : 172 -> 156
~ -[ACSCardService requestCard:reply:] : 712 -> 680
~ -[ACSCardService servicePriorityForRequest:] : 204 -> 184
~ -[INIntent(ACSCardRequesting) acs_needsTitleCardSection] : 68 -> 64
~ -[INIntent(ACSCardRequesting) requestCard:reply:] : 320 -> 312
~ -[INStartWorkoutIntent(ACSCardRequesting) requestCard:reply:] : 896 -> 828
~ -[CLPlacemark(AssistantCardService) acs_formattedNameOrStreetAddress] : 300 -> 272
~ -[INRequestPaymentIntent(ACSCardRequesting) requestCard:reply:] : 2180 -> 1988
~ +[SFCardSection(AssistantCardService) acs_uniquelyIdentifiedCardSection] : 128 -> 120
~ -[SFCardSection(AssistantCardService) acs_addParameter:] : 232 -> 216
~ -[SFCardSection(AssistantCardService) acs_parameterKeyPathFromParameter:] : 296 -> 272
~ +[SFNullCardSection(AssistantCardService) acs_wildCardSection] : 84 -> 80
~ -[INPriceRange(AssistantCardService) acs_formattedRangeString] : 412 -> 376
~ ___62-[INPriceRange(AssistantCardService) acs_formattedRangeString]_block_invoke : 200 -> 192
~ +[INPriceRange(AssistantCardService) _localeForCode:] : 388 -> 380
~ +[INPriceRange(AssistantCardService) _currencySymbolForCode:] : 224 -> 212
~ -[INPlayMediaIntent(ACSCardRequesting) requestCard:reply:] : 1496 -> 1376
~ -[INPaymentAccount(AssistantCardService) acs_formattedAccountName] : 168 -> 148
~ -[INSendPaymentIntent(ACSCardRequesting) requestCard:reply:] : 2180 -> 1988
~ -[INTextNoteContent(INCreateNoteIntentCardRequesting) acs_cardSection] : 116 -> 108
~ -[INImageNoteContent(INCreateNoteIntentCardRequesting) acs_cardSection] : 244 -> 232
~ -[INCreateNoteIntent(ACSCardRequesting) requestCard:reply:] : 608 -> 580
~ -[INCreateNoteIntent(ACSCardRequesting) _buildCardFromRequest:reply:] : 1488 -> 1388
~ ___69-[INCreateNoteIntent(ACSCardRequesting) _buildCardFromRequest:reply:]_block_invoke : 196 -> 188
~ -[INIntent(AssistantCardService) acs_utteranceForCardService] : 420 -> 380
~ +[ACSCardServiceHelper rowCardSectionFromLeadingText:trailingText:] : 200 -> 192
~ +[ACSCardServiceHelper formattedDateTimeStringFromDateComponents:] : 156 -> 144
~ +[ACSCardServiceHelper formattedDateTimeStringFromDate:] : 112 -> 108
~ +[ACSCardServiceHelper addParameterToSection:selectorStrings:class:] : 196 -> 184
~ -[INPerson(AssistantCardService) acs_formattedPersonName] : 108 -> 100
~ +[SFCard(AssistantCardService) acs_uniquelyIdentifiedCard] : 128 -> 120
~ -[SFCard(AssistantCardService) acs_setInteraction:] : 592 -> 520
~ -[SFCard(AssistantCardService) acs_interaction] : 236 -> 212
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACSCardRequesting"
- "ACSCardService"
- "ACSCardServiceHelper"
- "AssistantCardService"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<CRSCardRequesting>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CRSCardServing"
- "CRSIdentifiedServing"
- "CRSServing"
- "INCreateNoteIntentCardRequesting"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8@\"<CRSCardRequesting>\"16"
- "Q24@0:8@16"
- "T#,R"
- "T@\"INInteraction\",&,N,Sacs_setInteraction:"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_acs_currencySymbol"
- "_acs_currencySymbolForCode:"
- "_acs_formattedStringIncludeSymbol:"
- "_acs_localeForCode:"
- "_buildCardFromRequest:reply:"
- "_currencySymbolForCode:"
- "_intentInstanceDescription"
- "_localeForCode:"
- "_subscriptedKeyPath"
- "_title"
- "acs_addParameter:"
- "acs_cardSection"
- "acs_formattedAccountName"
- "acs_formattedAmountString"
- "acs_formattedNameOrStreetAddress"
- "acs_formattedPersonName"
- "acs_formattedRangeString"
- "acs_interaction"
- "acs_needsTitleCardSection"
- "acs_parameterKeyPathFromParameter:"
- "acs_setInteraction:"
- "acs_setParameters:"
- "acs_uniquelyIdentifiedCard"
- "acs_uniquelyIdentifiedCardSection"
- "acs_utteranceForCardService"
- "acs_wildCardSection"
- "addObject:"
- "addParameterToSection:selectorStrings:class:"
- "addedTasks"
- "amount"
- "appState"
- "applicationProxyForIdentifier:"
- "applicationProxyForSystemPlaceholder:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "artwork"
- "autorelease"
- "autoupdatingCurrentLocale"
- "availableLocaleIdentifiers"
- "backingStore"
- "bundleForClass:"
- "canSatisfyCardRequest:"
- "class"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "contents"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createdNote"
- "currencyAmount"
- "currencyCode"
- "currencySymbol"
- "currentCalendar"
- "data"
- "dateFromComponents:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "displayName"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "extensionBundleId"
- "feeAmount"
- "firstObject"
- "format"
- "formattedDateTimeStringFromDate:"
- "formattedDateTimeStringFromDateComponents:"
- "hash"
- "image"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithIntent:response:"
- "initWithIntentsImage:"
- "initWithLocaleIdentifier:"
- "intent"
- "intentHandlingStatus"
- "intentMessageData"
- "intentMessageName"
- "intentResponse"
- "intentResponseMessageData"
- "intentResponseMessageName"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSubclassOfClass:"
- "isValid"
- "launchId"
- "length"
- "localizedName"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "maximumPrice"
- "mediaContainer"
- "mediaItems"
- "minimumPrice"
- "modifiedTaskList"
- "name"
- "nickname"
- "note"
- "objectForKey:"
- "organizationName"
- "parameterClass"
- "parameterForClass:keyPath:"
- "parameterKeyPaths"
- "payee"
- "payer"
- "paymentRecord"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "protobufMessageData"
- "protobufMessageName"
- "release"
- "requestCard:reply:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rowCardSectionFromLeadingText:trailingText:"
- "self"
- "serviceIdentifier"
- "servicePriorityForCardRequest:"
- "servicePriorityForRequest:"
- "setButton:"
- "setCardId:"
- "setCardSectionId:"
- "setCardSections:"
- "setCornerRoundingStyle:"
- "setCurrencyCode:"
- "setCurrencySymbol:"
- "setDateStyle:"
- "setDescriptions:"
- "setFormattedTextPieces:"
- "setImages:"
- "setIndex:forSubKeyPath:"
- "setIntentMessageData:"
- "setIntentMessageName:"
- "setIntentResponseMessageData:"
- "setIntentResponseMessageName:"
- "setIsBold:"
- "setIsCentered:"
- "setIsSelected:"
- "setLeadingText:"
- "setLocale:"
- "setMaxLines:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setParameterKeyPaths:"
- "setProtobufMessageData:"
- "setProtobufMessageName:"
- "setSeparatorStyle:"
- "setSubtitle:"
- "setText:"
- "setTextColor:"
- "setThumbnail:"
- "setTimeStyle:"
- "setTitle:"
- "setTitleAlign:"
- "setTitleImage:"
- "setTitleWeight:"
- "setTrailingText:"
- "spokenPhrase"
- "status"
- "stringFromDate:"
- "stringFromNumber:"
- "stringWithFormat:"
- "stringWithString:"
- "subThoroughfare"
- "substringToIndex:"
- "superclass"
- "supportsSecureCoding"
- "taskType"
- "text"
- "textWithString:"
- "thoroughfare"
- "type"
- "underlyingInteraction"
- "v24@0:8@16"
- "v32@0:8@\"<CRSCardRequesting>\"16@?<v@?@\"<CRCard>\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24#32"
- "workoutName"
- "zone"

```
