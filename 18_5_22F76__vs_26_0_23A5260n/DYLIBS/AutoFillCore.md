## AutoFillCore

> `/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore`

```diff

-35.0.0.0.0
-  __TEXT.__text: 0xa2b8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x4f4
+39.0.0.0.0
+  __TEXT.__text: 0xa154
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_methlist: 0x4fc
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x16ee
-  __TEXT.__gcc_except_tab: 0x620
+  __TEXT.__cstring: 0x170f
+  __TEXT.__gcc_except_tab: 0x59c
   __TEXT.__oslogstring: 0x3
-  __TEXT.__dlopen_cstrs: 0x3a6
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__dlopen_cstrs: 0x34a
+  __TEXT.__unwind_info: 0x370
   __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0x1a40
-  __TEXT.__objc_methtype: 0x3ae
-  __TEXT.__objc_stubs: 0x13e0
+  __TEXT.__objc_methname: 0x1bca
+  __TEXT.__objc_methtype: 0x3b4
+  __TEXT.__objc_stubs: 0x1560
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x710
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x288
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__cfstring: 0x1100
   __AUTH_CONST.__objc_const: 0x828
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0xd0
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F180310E-FCED-394F-9B7D-462A61B18CF0
-  Functions: 217
-  Symbols:   980
-  CStrings:  625
+  UUID: 860AB1FD-EB0C-3A41-A060-143BE2FC9B2D
+  Functions: 216
+  Symbols:   985
+  CStrings:  643
 
Symbols:
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.1
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.2
+ -[AFSuggestionGenerationManager authenticateIfNecessaryForSuggestion:documentTraits:withCompletionHandler:]
+ -[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:]
+ -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]
+ GCC_except_table16
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table55
+ _AFTextContentTypeCreditCardArt
+ _NSLog
+ _OBJC_CLASS_$_NSConstantArray
+ _PassKitCoreLibraryCore.frameworkLibrary
+ ___101-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]_block_invoke
+ ___101-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]_block_invoke_2
+ ___101-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]_block_invoke_3
+ ___101-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]_block_invoke_3.cold.1
+ ___103-[AFSuggestionGenerationManager authenticateIfNecessaryForSuggestion:documentTraits:completionHandler:]_block_invoke
+ ___115-[AFSuggestionGenerationManager generateContactAutoFillSuggestionsWithTextPrefix:documentTraits:completionHandler:]_block_invoke.98
+ ___125-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke
+ ___125-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke_2
+ ___141-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:]_block_invoke
+ ___141-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:]_block_invoke.56
+ ___141-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:]_block_invoke_2
+ ___PassKitCoreLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v24?0"PKAutoFillCardCredential"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ ___getPKAutoFillCardManagerClass_block_invoke
+ _audit_stringPassKitCore
+ _dispatch_group_notify
+ _getPKAutoFillCardManagerClass.softClass
+ _objc_msgSend$activeFPANCardsWithOptions:allowedCardTypes:completion:
+ _objc_msgSend$artwork
+ _objc_msgSend$authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:
+ _objc_msgSend$cardNickname
+ _objc_msgSend$cardholderName
+ _objc_msgSend$credentialForFPANCard:authorization:options:merchantHost:completion:
+ _objc_msgSend$credentialType
+ _objc_msgSend$displayableLastFour
+ _objc_msgSend$expirationDate
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$generateCreditCardAutoFillWithCompletionHandler:externalizedContext:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$primaryAccountNumber
+ _objc_msgSend$securityCode
+ _objc_msgSend$setWithArray:
- -[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]
- -[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.1
- -[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:].cold.2
- -[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:]
- -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:]
- -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.1
- -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.2
- -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.3
- -[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:].cold.4
- GCC_except_table21
- GCC_except_table22
- GCC_except_table48
- GCC_except_table49
- GCC_except_table57
- _OUTLINED_FUNCTION_3
- _SafariCoreLibrary
- _SafariCoreLibraryCore.frameworkLibrary
- ___115-[AFSuggestionGenerationManager generateContactAutoFillSuggestionsWithTextPrefix:documentTraits:completionHandler:]_block_invoke.70
- ___121-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:]_block_invoke
- ___121-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:]_block_invoke.41
- ___121-[AFSuggestionGenerationManager generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:]_block_invoke_2
- ___126-[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke
- ___126-[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]_block_invoke_2
- ___SafariCoreLibraryCore_block_invoke
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___getSFSafariCreditCardStoreClass_block_invoke
- ___getSFSafariCreditCardStoreClass_block_invoke.cold.1
- ___getWBSCreditCardTypeFromNumberSymbolLoc_block_invoke
- ___getWBSCreditCardTypeLocalizedNameForGeneratingCardNamesSymbolLoc_block_invoke
- _audit_stringSafariCore
- _getSFSafariCreditCardStoreClass.softClass
- _getWBSCreditCardTypeFromNumberSymbolLoc.ptr
- _getWBSCreditCardTypeLocalizedNameForGeneratingCardNamesSymbolLoc.ptr
- _objc_msgSend$_authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:
- _objc_msgSend$generateCreditCardAutoFillWithCompletionHandler:
- _objc_msgSend$savedCreditCardsWithError:
- _objc_msgSend$substringFromIndex:
CStrings:
+ "-[AFSuggestionGenerationManager authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]"
+ "-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:externalizedContext:]_block_invoke_3"
+ "Failed to retrieve card credential: %@"
+ "No active cards found"
+ "PKAutoFillCardManager"
+ "activeFPANCardsWithOptions:allowedCardTypes:completion:"
+ "artwork"
+ "authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:"
+ "authenticateIfNecessaryForSuggestion:documentTraits:withCompletionHandler:"
+ "cardNickname"
+ "cardholderName"
+ "cc-art"
+ "credentialForFPANCard:authorization:options:merchantHost:completion:"
+ "credentialType"
+ "displayableLastFour"
+ "expirationDate"
+ "externalizedContext"
+ "generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:externalizedContext:completionHandler:"
+ "generateCreditCardAutoFillWithCompletionHandler:externalizedContext:"
+ "localizedDescription"
+ "numberWithUnsignedInteger:"
+ "primaryAccountNumber"
+ "securityCode"
+ "setWithArray:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore"
+ "v12@?0B8"
+ "v24@?0@\"PKAutoFillCardCredential\"8@\"NSError\"16"
+ "v32@0:8@?16@24"
+ "v56@0:8Q16@24@32@40@?48"
- "%s Couldn't get credentials from Safari: %@"
- "-[AFSuggestionGenerationManager _authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:]"
- "-[AFSuggestionGenerationManager generateCreditCardAutoFillWithCompletionHandler:]"
- "SFSafariCreditCardStore"
- "WBSCreditCardTypeFromNumber"
- "WBSCreditCardTypeLocalizedNameForGeneratingCardNames"
- "_authenticateIfNecessaryForCreditCardSuggestion:withPayload:documentTraits:completionHandler:"
- "generateAutoFillSuggestionsWithAutoFillMode:textPrefix:documentTraits:completionHandler:"
- "generateCreditCardAutoFillWithCompletionHandler:"
- "savedCreditCardsWithError:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore"
- "substringFromIndex:"
- "v24@0:8@?16"
- "v48@0:8Q16@24@32@?40"

```
