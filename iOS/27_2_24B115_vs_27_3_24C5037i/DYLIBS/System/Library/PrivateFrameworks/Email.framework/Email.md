## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0xd4188
-  __TEXT.__objc_methlist: 0xce84
-  __TEXT.__const: 0x18c2
-  __TEXT.__gcc_except_tab: 0x1ada0
-  __TEXT.__cstring: 0xc379
+3901.300.26.0.0
+  __TEXT.__text: 0xd60a4
+  __TEXT.__objc_methlist: 0xd08c
+  __TEXT.__const: 0x18d8
+  __TEXT.__gcc_except_tab: 0x1b050
+  __TEXT.__cstring: 0xc569
   __TEXT.__ustring: 0x170
-  __TEXT.__oslogstring: 0x67a3
+  __TEXT.__oslogstring: 0x6903
   __TEXT.__dlopen_cstrs: 0x160
-  __TEXT.__swift5_typeref: 0x4aa
-  __TEXT.__constg_swiftt: 0x538
+  __TEXT.__swift5_typeref: 0x4b2
+  __TEXT.__constg_swiftt: 0x540
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x41f
   __TEXT.__swift5_fieldmd: 0x610

   __TEXT.__swift5_capture: 0x48
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8518
+  __TEXT.__unwind_info: 0x8648
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x45d8
-  __DATA_CONST.__objc_classlist: 0x580
+  __DATA_CONST.__const: 0x4670
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6178
+  __DATA_CONST.__objc_selrefs: 0x6208
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__got: 0xc90
   __AUTH_CONST.__const: 0x1f40
-  __AUTH_CONST.__cfstring: 0xa400
-  __AUTH_CONST.__objc_const: 0x16c30
+  __AUTH_CONST.__cfstring: 0xa680
+  __AUTH_CONST.__objc_const: 0x17018
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH.__objc_data: 0x200
+  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH.__objc_data: 0x2f0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xc4c
-  __DATA.__data: 0x28e0
-  __DATA_DIRTY.__objc_data: 0x3768
+  __DATA.__objc_ivar: 0xc68
+  __DATA.__data: 0x2900
+  __DATA_DIRTY.__objc_data: 0x3770
   __DATA_DIRTY.__data: 0x380
   __DATA_DIRTY.__bss: 0xad0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5161
-  Symbols:   8931
-  CStrings:  2150
+  Functions: 5205
+  Symbols:   9008
+  CStrings:  2176
 
Symbols:
+ +[EMAccountMatchResult supportsSecureCoding]
+ +[EMEnterOneTimeCodeFieldResponse supportsSecureCoding]
+ +[EMOneTimeCodeAccelerator maskCharacter]
+ +[EMOneTimeCodeFieldContext supportsSecureCoding]
+ -[EMAccountMatchResult accountIsActive]
+ -[EMAccountMatchResult description]
+ -[EMAccountMatchResult encodeWithCoder:]
+ -[EMAccountMatchResult initWithCoder:]
+ -[EMAccountMatchResult initWithMatch:accountIsActive:]
+ -[EMAccountMatchResult match]
+ -[EMAccountRepository bestAccountMatchForMaskedEmailAddress:]
+ -[EMEnterOneTimeCodeFieldResponse accountIsActive]
+ -[EMEnterOneTimeCodeFieldResponse accountMatchResult]
+ -[EMEnterOneTimeCodeFieldResponse description]
+ -[EMEnterOneTimeCodeFieldResponse encodeWithCoder:]
+ -[EMEnterOneTimeCodeFieldResponse initWithAccountMatch:]
+ -[EMEnterOneTimeCodeFieldResponse initWithAccountMatchResult:accountIsActive:]
+ -[EMEnterOneTimeCodeFieldResponse initWithCoder:]
+ -[EMFetchController expectingOneTimeCodeUntilDateWithReply:]
+ -[EMFetchController startExpectingOneTimeCode]
+ -[EMFetchController stopExpectingOneTimeCode]
+ -[EMMessageTransferAction initWithQuery:origin:actor:destinationMailbox:flagChange:copyMessages:]
+ -[EMOneTimeCodeAccelerator didEnterOneTimeCodeFieldWithContext:completion:]
+ -[EMOneTimeCodeFieldContext .cxx_destruct]
+ -[EMOneTimeCodeFieldContext canReportUnfocus]
+ -[EMOneTimeCodeFieldContext copyWithZone:]
+ -[EMOneTimeCodeFieldContext description]
+ -[EMOneTimeCodeFieldContext emailAddress]
+ -[EMOneTimeCodeFieldContext encodeWithCoder:]
+ -[EMOneTimeCodeFieldContext initWithCoder:]
+ -[EMOneTimeCodeFieldContext initWithEmailAddress:canReportUnfocus:provenance:]
+ -[EMOneTimeCodeFieldContext provenance]
+ -[EMOutgoingMessageRepository canCancelLastDelayedMessage:]
+ _EMStringForAccountMatch
+ _EMUserDefaultHideDebugMenuInViewOptions
+ _OBJC_CLASS_$_EMAccountMatchResult
+ _OBJC_CLASS_$_EMEnterOneTimeCodeFieldResponse
+ _OBJC_CLASS_$_EMOneTimeCodeFieldContext
+ _OBJC_IVAR_$_EMAccountMatchResult._accountIsActive
+ _OBJC_IVAR_$_EMAccountMatchResult._match
+ _OBJC_IVAR_$_EMEnterOneTimeCodeFieldResponse._accountIsActive
+ _OBJC_IVAR_$_EMEnterOneTimeCodeFieldResponse._accountMatchResult
+ _OBJC_IVAR_$_EMOneTimeCodeFieldContext._canReportUnfocus
+ _OBJC_IVAR_$_EMOneTimeCodeFieldContext._emailAddress
+ _OBJC_IVAR_$_EMOneTimeCodeFieldContext._provenance
+ _OBJC_METACLASS_$_EMAccountMatchResult
+ _OBJC_METACLASS_$_EMEnterOneTimeCodeFieldResponse
+ _OBJC_METACLASS_$_EMOneTimeCodeFieldContext
+ __OBJC_$_CLASS_METHODS_EMAccountMatchResult
+ __OBJC_$_CLASS_METHODS_EMEnterOneTimeCodeFieldResponse
+ __OBJC_$_CLASS_METHODS_EMOneTimeCodeFieldContext
+ __OBJC_$_CLASS_PROP_LIST_EMAccountMatchResult
+ __OBJC_$_CLASS_PROP_LIST_EMEnterOneTimeCodeFieldResponse
+ __OBJC_$_CLASS_PROP_LIST_EMOneTimeCodeFieldContext
+ __OBJC_$_INSTANCE_METHODS_EMAccountMatchResult
+ __OBJC_$_INSTANCE_METHODS_EMEnterOneTimeCodeFieldResponse
+ __OBJC_$_INSTANCE_METHODS_EMOneTimeCodeFieldContext
+ __OBJC_$_INSTANCE_VARIABLES_EMAccountMatchResult
+ __OBJC_$_INSTANCE_VARIABLES_EMEnterOneTimeCodeFieldResponse
+ __OBJC_$_INSTANCE_VARIABLES_EMOneTimeCodeFieldContext
+ __OBJC_$_PROP_LIST_EMAccountMatchResult
+ __OBJC_$_PROP_LIST_EMEnterOneTimeCodeFieldResponse
+ __OBJC_$_PROP_LIST_EMOneTimeCodeFieldContext
+ __OBJC_CLASS_PROTOCOLS_$_EMAccountMatchResult
+ __OBJC_CLASS_PROTOCOLS_$_EMEnterOneTimeCodeFieldResponse
+ __OBJC_CLASS_PROTOCOLS_$_EMOneTimeCodeFieldContext
+ __OBJC_CLASS_RO_$_EMAccountMatchResult
+ __OBJC_CLASS_RO_$_EMEnterOneTimeCodeFieldResponse
+ __OBJC_CLASS_RO_$_EMOneTimeCodeFieldContext
+ __OBJC_METACLASS_RO_$_EMAccountMatchResult
+ __OBJC_METACLASS_RO_$_EMEnterOneTimeCodeFieldResponse
+ __OBJC_METACLASS_RO_$_EMOneTimeCodeFieldContext
+ ___61-[EMAccountRepository bestAccountMatchForMaskedEmailAddress:]_block_invoke
+ ___61-[EMAccountRepository bestAccountMatchForMaskedEmailAddress:]_block_invoke_2
+ ___75-[EMOneTimeCodeAccelerator didEnterOneTimeCodeFieldWithContext:completion:]_block_invoke
+ ___block_descriptor_40_ea8_32bs_e30_v16?0"EMAccountMatchResult"8ls32l8
+ ___block_descriptor_40_ea8_32s_e30_v16?0"EMAccountMatchResult"8ls32l8
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV6PolicyV
- -[EMFetchController performFetchForOTC]
CStrings:
+ "(none)"
+ "<%@: %p> accountMatchResult: %@, accountIsActive: %d"
+ "<%@: %p> emailAddress: %@, canReportUnfocus: %d, provenance: %@"
+ "<%@: %p> match: %@, accountIsActive: %d"
+ "AuthenticatorApp"
+ "Device isChinaRegion=%{bool}d"
+ "EFPropertyKey_accountIsActive"
+ "EFPropertyKey_accountMatchResult"
+ "EFPropertyKey_canReportUnfocus"
+ "EFPropertyKey_emailAddress"
+ "EFPropertyKey_match"
+ "EFPropertyKey_provenance"
+ "Email"
+ "Exact"
+ "Failed to match the masked email address to an account, due to error: %{public}@"
+ "HideDebugMenuInViewOptions"
+ "No email address to match; reporting Unknown without checking accounts"
+ "NoAccountsConfigured"
+ "One Time Code field has been entered with context %{public}@"
+ "Partial"
+ "Received one-time code response: %{public}@"
+ "Skipped looking for best account match for email address since no completion handler was provided"
+ "TextMessage"
+ "Unavailable"
+ "Unknown (%ld)"
+ "Unmatched"
+ "v16@?0@\"EMAccountMatchResult\"8"
- "One Time Code field has been entered."
```
