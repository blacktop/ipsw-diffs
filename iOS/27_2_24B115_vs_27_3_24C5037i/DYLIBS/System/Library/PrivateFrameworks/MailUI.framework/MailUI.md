## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/MailUI`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0x35ca80
-  __TEXT.__objc_methlist: 0x9fbc
-  __TEXT.__cstring: 0xeff9
-  __TEXT.__const: 0x11654
+3901.300.26.0.0
+  __TEXT.__text: 0x37667c
+  __TEXT.__objc_methlist: 0xa14c
+  __TEXT.__cstring: 0x100f9
+  __TEXT.__const: 0x11744
   __TEXT.__gcc_except_tab: 0xe98
-  __TEXT.__oslogstring: 0x7880
+  __TEXT.__oslogstring: 0x7ad0
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__ustring: 0x2e2
-  __TEXT.__swift5_typeref: 0x19466
-  __TEXT.__swift5_capture: 0x5ae8
-  __TEXT.__constg_swiftt: 0x49c4
-  __TEXT.__swift5_builtin: 0x550
-  __TEXT.__swift5_reflstr: 0x3df3
-  __TEXT.__swift5_fieldmd: 0x37a8
-  __TEXT.__swift5_assocty: 0x11f8
-  __TEXT.__swift5_proto: 0x698
-  __TEXT.__swift5_types: 0x57c
+  __TEXT.__swift5_typeref: 0x19666
+  __TEXT.__swift5_capture: 0x5f64
+  __TEXT.__constg_swiftt: 0x49f4
+  __TEXT.__swift5_builtin: 0x564
+  __TEXT.__swift5_reflstr: 0x3e33
+  __TEXT.__swift5_fieldmd: 0x3800
+  __TEXT.__swift5_assocty: 0x1210
+  __TEXT.__swift5_proto: 0x6a0
+  __TEXT.__swift5_types: 0x584
   __TEXT.__swift_as_entry: 0x194
-  __TEXT.__swift_as_ret: 0x160
-  __TEXT.__swift_as_cont: 0x270
+  __TEXT.__swift_as_ret: 0x168
+  __TEXT.__swift_as_cont: 0x290
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0xee28
-  __TEXT.__eh_frame: 0x33dc
+  __TEXT.__unwind_info: 0xf290
+  __TEXT.__eh_frame: 0x363c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3070
-  __DATA_CONST.__objc_classlist: 0x5a0
-  __DATA_CONST.__objc_catlist: 0xd0
+  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x66b8
+  __DATA_CONST.__objc_selrefs: 0x67e0
   __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x2058
-  __AUTH_CONST.__const: 0x132e0
-  __AUTH_CONST.__cfstring: 0x48a0
-  __AUTH_CONST.__objc_const: 0x146f0
-  __AUTH_CONST.__objc_intobj: 0x1c8
+  __DATA_CONST.__got: 0x20e0
+  __AUTH_CONST.__const: 0x13e08
+  __AUTH_CONST.__cfstring: 0x4b80
+  __AUTH_CONST.__objc_const: 0x14908
+  __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x31c0
-  __AUTH.__objc_data: 0x1db0
-  __AUTH.__data: 0x15d0
-  __DATA.__objc_ivar: 0x9ac
-  __DATA.__data: 0x74d0
+  __AUTH_CONST.__auth_got: 0x32d0
+  __AUTH.__objc_data: 0x1e70
+  __AUTH.__data: 0x1680
+  __DATA.__objc_ivar: 0x9b4
+  __DATA.__data: 0x7670
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x3f0
   __DATA_DIRTY.__objc_data: 0x3058
-  __DATA_DIRTY.__data: 0x35b8
+  __DATA_DIRTY.__data: 0x3608
   __DATA_DIRTY.__bss: 0x59f0
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
+  - /System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI
   - /System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch
   - /System/Library/PrivateFrameworks/MIME.framework/MIME
   - /System/Library/PrivateFrameworks/MailSupport.framework/MailSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/Message.framework/Message
   - /System/Library/PrivateFrameworks/MessageSupport.framework/MessageSupport
   - /System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI
   - /System/Library/PrivateFrameworks/ProactiveSummarizationClient.framework/ProactiveSummarizationClient

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15807
-  Symbols:   8786
-  CStrings:  2100
+  Functions: 16083
+  Symbols:   8877
+  CStrings:  2182
 
Symbols:
+ +[CSSuggestion(MailUI) mui_dateRangeSuggestionForUserTypedText:currentSuggestion:fromDate:toDate:displayText:]
+ +[MFMailboxUid(Utilities) iconForType:]
+ +[MFMailboxUid(Utilities) iconNameForType:]
+ +[MFMailboxUid(Utilities) shorcutIconNameForMailboxType:]
+ +[MUILocalizedMessageListStrings snippetHighlightCcAddressFormat]
+ +[MUILocalizedMessageListStrings snippetHighlightFromAddressFormat]
+ +[MUILocalizedMessageListStrings snippetHighlightToAddressFormat]
+ +[MailAccount(Utilities) accountImageForAccount:]
+ -[MFMailboxUid(MobileMailEditing) mv_isEditable]
+ -[MFMailboxUid(MobileMailEditing) mv_isSelectable]
+ -[MFMailboxUid(Utilities) foundInDescriptionIncludingAccount:]
+ -[MFMailboxUid(Utilities) iconName]
+ -[MFMailboxUid(Utilities) icon]
+ -[MFMailboxUid(Utilities) tinyDisplayIconWithColor:]
+ -[UITraitCollection(MailUI) mui_isVerticalBarActive]
+ -[UITraitCollection(MailUI) mui_isVerticalBarOnLeadingEdge]
+ -[_MFIconCacheItem .cxx_destruct]
+ -[_MFIconCacheItem cachedImage]
+ -[_MFIconCacheItem filename]
+ -[_MFIconCacheItem initWithFilename:]
+ -[_MFIconCacheItem setCachedImage:]
+ _MFImageGlyphArchiveMailbox
+ _MFImageGlyphDraftMailbox
+ _MFImageGlyphGenericMailbox
+ _MFImageGlyphInboxMailbox
+ _MFImageGlyphJunkMailbox
+ _MFImageGlyphOutboxMailbox
+ _MFImageGlyphSentMailbox
+ _MFImageGlyphSentMailboxFilled
+ _MFImageGlyphTrashMailbox
+ _OBJC_CLASS_$_MFMailboxUid
+ _OBJC_CLASS_$_MUIOneTimeCodeTTR
+ _OBJC_CLASS_$_MailAccount
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$__MFIconCacheItem
+ _OBJC_IVAR_$__MFIconCacheItem._cachedImage
+ _OBJC_IVAR_$__MFIconCacheItem._filename
+ _OBJC_METACLASS_$_MUIOneTimeCodeTTR
+ _OBJC_METACLASS_$__MFIconCacheItem
+ __CLASS_METHODS_MUIOneTimeCodeTTR
+ __DATA_MUIOneTimeCodeTTR
+ __INSTANCE_METHODS_MUIOneTimeCodeTTR
+ __METACLASS_DATA_MUIOneTimeCodeTTR
+ __OBJC_$_CATEGORY_CLASS_METHODS_MFMailboxUid_$_Utilities
+ __OBJC_$_CATEGORY_CLASS_METHODS_MailAccount_$_Utilities
+ __OBJC_$_CATEGORY_MFMailboxUid_$_Utilities
+ __OBJC_$_CATEGORY_MailAccount_$_Utilities
+ __OBJC_$_INSTANCE_METHODS_MFMailboxUid(Utilities|MobileMailEditing)
+ __OBJC_$_INSTANCE_METHODS__MFIconCacheItem
+ __OBJC_$_INSTANCE_VARIABLES__MFIconCacheItem
+ __OBJC_$_PROP_LIST__MFIconCacheItem
+ __OBJC_CLASS_RO_$__MFIconCacheItem
+ __OBJC_METACLASS_RO_$__MFIconCacheItem
+ __UIEnhancedLandscapeBarEnabled
+ ___110+[CSSuggestion(MailUI) mui_dateRangeSuggestionForUserTypedText:currentSuggestion:fromDate:toDate:displayText:]_block_invoke
+ __folderNameFormatString
+ _accountImageForAccount:.__accountIcons
+ _accountImageForAccount:.bundle
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO0A10AttributesV04LinkE0OAaBHPyHC
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA5GroupVyAA012_ConditionalD0Vy04MailB0021DonationVisualizationD4View33_5E5E9DA319EBC5204010E8DA17B46F05LLVAA012SubscriptionJ0Vy7Combine10PublishersO11AutoconnectCy_So7NSTimerC10FoundationE14TimerPublisherCGACyAA6VStackVyAA05TupleD0VyAA08ProgressJ0VyAA05EmptyJ0VA4_G_AA4TextVQPGGAA16_FlexFrameLayoutVGGGGAA25_AppearanceActionModifierVGA17_GAA0J0HPA18_AAA20_HPA15_AAA20_HPA14_AAA20_HPAkAA20_HPyHC_A13_AAA20_HPyHCHC_HC_A17_AA0J8ModifierHPyHCHC_A17_AAA21_HPyHCHC
+ _iconNameForType:.mailboxImages
+ _mui_dateRangeSuggestionForUserTypedText:currentSuggestion:fromDate:toDate:displayText:.fmt
+ _mui_dateRangeSuggestionForUserTypedText:currentSuggestion:fromDate:toDate:displayText:.onceToken
+ _mui_dateScopeDict
+ _shorcutIconNameForMailboxType:._mailboxAppShortcutIconNames
+ _symbolic SaySny_____GG 10Foundation16AttributedStringV5IndexV
+ _symbolic Say_____G 10Foundation16AttributedStringV17FormattingOptionsV
+ _symbolic Say_____G 10Foundation16AttributedStringV4RunsV3RunV
+ _symbolic ScCyxSg_____G s5NeverO
+ _symbolic Shy_____GIegg_ s5Int64V
+ _symbolic Shy_____GSg s5Int64V
+ _symbolic Sny_____GSg 10Foundation16AttributedStringV5IndexV
+ _symbolic So17MUIOneTimeCodeTTRCXMT
+ _symbolic So23EMContentRepresentationCSgSbIeggd_
+ _symbolic So23EMContentRepresentationCSgSbIegnd_
+ _symbolic _____ 10Foundation15AttributeScopesO0A10AttributesV
+ _symbolic _____ 10Foundation15AttributeScopesO0A10AttributesV04LinkB0O
+ _symbolic _____ 6MailUI20MessageContentLoaderC15SiriBudgetState33_3D154AA94633874686D627706095E8D1LLV
+ _symbolic _____ 6MailUI36MUIOneTimeCodeTTRRadarContentBuilderV
+ _symbolic _____ So14EMNetworkUsageV
+ _symbolic _____ s15ContinuousClockV7InstantV
+ _symbolic _____Sg s15ContinuousClockV7InstantV
+ _symbolic _____SgSbIegnd_ 10AppIntents10IntentFileV
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _symbolic _____yAAy_____y_____y__________y_____y______GAAy_____y_____y_____y_____ALG______QPGG_____GGGG_____GAVG 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V 04MailB0021DonationVisualizationD4View33_5E5E9DA319EBC5204010E8DA17B46F05LLV AA012SubscriptionJ0V 7Combine10PublishersO11AutoconnectC So7NSTimerC10FoundationE14TimerPublisherC AA6VStackV AA05TupleD0V AA08ProgressJ0V AA05EmptyJ0V AA4TextV AA16_FlexFrameLayoutV AA25_AppearanceActionModifierV
+ _symbolic _____ySaySny_____GGG s16IndexingIteratorV 10Foundation16AttributedStringV5IndexV
+ _symbolic _____ySay_____GG s16IndexingIteratorV 12HybridSearch10ScanResultV
+ _symbolic _____yScTyyt_____GSgG 7SwiftUI5StateV s5NeverO
+ _symbolic _____yScTyyt_____GSgG 7SwiftUI9LazyStateV s5NeverO
+ _symbolic _____yScTyyt_____GSg_G 7SwiftUI9LazyStateV7StorageO s5NeverO
+ _symbolic _____yShy_____GSgG 7SwiftUI5StateV s5Int64V
+ _symbolic _____yShy_____GSgG 7SwiftUI9LazyStateV s5Int64V
+ _symbolic _____yShy_____GSg_G 7SwiftUI9LazyStateV7StorageO s5Int64V
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 6MailUI20MessageContentLoaderC15SiriBudgetState33_3D154AA94633874686D627706095E8D1LLV
+ _symbolic _____y_____G s10ArraySliceV s5Int64V
+ _symbolic _____y__________G s7KeyPathC 10Foundation15AttributeScopesO0C10AttributesV AG04LinkD0O
+ _type_layout_string 6MailUI20MessageContentLoaderC15SiriBudgetState33_3D154AA94633874686D627706095E8D1LLV
- _get_witness_table 7SwiftUI15ModifiedContentVyAA5GroupVyAA012_ConditionalD0Vy04MailB0021DonationVisualizationD4View33_5E5E9DA319EBC5204010E8DA17B46F05LLVAA012SubscriptionJ0Vy7Combine10PublishersO11AutoconnectCy_So7NSTimerC10FoundationE14TimerPublisherCGACyAA6VStackVyAA05TupleD0VyAA08ProgressJ0VyAA05EmptyJ0VA4_G_AA4TextVQPGGAA16_FlexFrameLayoutVGGGGAA25_AppearanceActionModifierVGAA0J0HPA15_AAA19_HPA14_AAA19_HPAkAA19_HPyHC_A13_AAA19_HPyHCHC_HC_A17_AA0J8ModifierHPyHCHC
- _symbolic ScCySo23EMContentRepresentationCSg_____G s5NeverO
- _symbolic ScCy_____Sg_____G 10AppIntents10IntentFileV s5NeverO
- _symbolic _____ 6MailUI20MessageContentLoaderC18loadRepresentationySo09EMContentG0CSgSo9EMMessageCYaFZyScCyAGs5NeverOGXEfU_5StateL_V
- _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 6MailUI20MessageContentLoaderC18loadRepresentationySo09EMContentK0CSgSo9EMMessageCYaFZyScCyAJs5NeverOGXEfU_5StateL_V
- _type_layout_string 6MailUI20MessageContentLoaderC18loadRepresentationySo09EMContentG0CSgSo9EMMessageCYaFZyScCyAGs5NeverOGXEfU_5StateL_V
CStrings:
+ "\nGlobal Message ID: "
+ " may be able to summarize this type of content."
+ " may be able to summarize this type of content. These messages will need to be sent to "
+ " may be able to summarize this type of content. This message will need to be sent to "
+ " · AI Generated"
+ "#SiriMail %s exceeded the Siri turn budget; cancelling"
+ "#SiriMail %s skipping attachment — expected size %lld exceeds %llu byte limit"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
+ "AI Generated"
+ "Additional Notes:\n\n1. Which website/app were you autofilling into?\n\n2. What email provider does the account that received the code use (Gmail, Outlook, iCloud, etc.)?\n\n=== Problem Report ===\n\nMail was checking for a one-time code when the user copied something from a message. There may have been a one-time code detection issue.\n\n=== Visible Message ===\nDate: "
+ "After"
+ "Alert message for when the user is prompted to use Snowflake to generate summaries and they haven't onboarded to Snowflake yet. The argument is the provider name."
+ "Alert message for when the user is prompted to use Snowflake to generate summaries. Both the arguments are the provider name."
+ "Alert message for when the user is prompted to use Snowflake to generate summaries. The argument is the provider name"
+ "Alert title for when Mail can't summarize a message"
+ "Alert title for when Mail can't summarize messages"
+ "BOX_SUFFIX"
+ "Before"
+ "Button to dismiss the missed one-time code autofill report alert without reporting."
+ "Button to proceed to the missed one-time code autofill report sheet."
+ "CSSuggestion does not respond to initWithUserString:currentSuggestion:suggestionTokenResult:"
+ "Cancel button title for the alert that is presented when using external intelligence."
+ "Cancelled the external summarization flow."
+ "Confirm button title for the alert that is presented when confirming using Snowflake to generate summaries. Argument is the provider name."
+ "Confirm button title for the alert that is presented when deciding to onboard onto Snowfkale to generate summaries. Argument is the provider name."
+ "DATE_FROM"
+ "DATE_TO"
+ "Date"
+ "Did display external summarization alert, tryFlow: %{bool}d"
+ "DonationVisualization"
+ "Error message for when Mail can't summarize a message"
+ "Error message for when Mail can't summarize a message and a third-party has provided the error information. First argument is the provider name and the second is the error message."
+ "Error message for when Mail can't summarize a message because an issue with the input."
+ "Error message for when Mail can't summarize a message because of an issue with the output."
+ "Error message shown when Mail can't summarize a message because the on-device safety mechanism is out of date. Apple Intelligence & Siri Settings is a tappable link to the Apple Intelligence and Siri settings pane."
+ "FOLDER_SUFFIX"
+ "FOUND_IN_MAILBOX_FORMAT"
+ "If the expected code was not offered for AutoFill, please file a radar."
+ "Label below an email summary telling the reader that it was generated by a model"
+ "Label below an email summary written by a third-party model. The argument is the provider name."
+ "Localizable-AIChina"
+ "MAILBOX_SUFFIX"
+ "Mail DB shows this as donated, but GLP has no record of it."
+ "Mail summarization is temporarily restricted due to triggering safety alerts multiple times."
+ "Message of the alert offering to report a missed one-time code autofill."
+ "Missing from GLP"
+ "Negative value is not representable"
+ "Not Now"
+ "Notice shown alongside the message list telling the reader that the message summaries were generated by a model"
+ "OneTimeCodeTTR"
+ "Open Tap-to-Radar"
+ "Opening tap-to-radar for OTC autofill miss"
+ "QUERY"
+ "Response from "
+ "Safety mechanism update required. You can see the status in [Apple Intelligence & Siri Settings](mailsettings)."
+ "Skip showing external summarization onboarding, because we are already showing onboarding."
+ "SnippetHighlightCcAddress%1$@"
+ "SnippetHighlightFromAddress%1$@"
+ "SnippetHighlightToAddress%1$@"
+ "Summary is AI Generated"
+ "TEXT"
+ "TOKEN"
+ "Title of the alert offering to report a missed one-time code autofill."
+ "Try "
+ "Unable to Summarize These Messages"
+ "Unable to Summarize This Message"
+ "Unable to create a summary from this content."
+ "Unable to present onboarding view, no presentingViewController."
+ "Unable to proceed. This content may not comply with laws and regulations."
+ "Use "
+ "[%{public}s] GLP batch scan failed, excluding %ld ids from the mismatch check: %{public}s"
+ "[%{public}s] GLP/Mail DB mismatch: %ld of %ld checked Mail-DB-donated messages have no matching GLP record"
+ "[Internal Only] Security Code AutoFill Issue"
+ "[OTC TTR] One-time code was not displayed for autofill"
+ "_SHORT"
+ "_WITH_ACCOUNT"
+ "attachment load"
+ "content load"
+ "en_US_POSIX"
+ "extractAttachments(networkUsage:deadline:)"
+ "kQPTokenDate"
+ "loadAttachmentsConcurrently(from:networkUsage:deadline:)"
+ "requestAttachmentRepresentation(for:networkUsage:deadline:)"
+ "suggestionDescriptionKey"
+ "suggestionTextKey"
+ "suggestionTokensKey"
+ "suggestionTypeKey"
+ "withSiriTurnBudget(label:deadline:_:)"
+ "yyyy-MM-dd'T'HH:mm:ss"
- "#SiriMail content load exceeded %fs (Siri turn budget); cancelling"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/System/Library/PrivateFrameworks/Email.framework/Headers/EMContentRequestOptions.h"
- "CSSuggestion does not respond to senderContainsSuggestionWithUserString:currentSuggestion:"
- "extractAttachments()"
- "loadAttachmentsConcurrently(from:)"
- "loadRepresentation(_:)"
- "requestAttachmentRepresentation(for:)"
```
