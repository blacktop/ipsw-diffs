## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-70.0.0.0.0
-  __TEXT.__text: 0xfdcc
-  __TEXT.__objc_methlist: 0xfa0
+73.0.0.0.2
+  __TEXT.__text: 0x10988
+  __TEXT.__objc_methlist: 0xfe0
   __TEXT.__const: 0x5b0
-  __TEXT.__cstring: 0x16fc
+  __TEXT.__cstring: 0x180c
   __TEXT.__gcc_except_tab: 0x250
   __TEXT.__oslogstring: 0x7f3
   __TEXT.__ustring: 0x1bc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0xae0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x1d8
-  __AUTH_CONST.__const: 0x389
-  __AUTH_CONST.__cfstring: 0x19e0
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x3a9
+  __AUTH_CONST.__cfstring: 0x1b80
   __AUTH_CONST.__objc_const: 0x1d50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78

   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x488
-  __DATA.__bss: 0x690
+  __DATA.__bss: 0x6a0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 452
-  Symbols:   1445
-  CStrings:  287
+  Functions: 461
+  Symbols:   1467
+  CStrings:  301
 
Symbols:
+ +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]
+ +[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _familyControlsOverrideCommandForURL:state:]
+ +[WCRBrowserEngineClient _isSensitiveURL:usingBloomFilter:]
+ +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]
+ -[WCRBloomFilter isSensitive:]
+ -[WCRBrowserEngineClient _presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:]
+ -[WCRBrowserEngineClient allowURLWithFamilyControls:referrerURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]
+ -[WCRBrowserEngineClient userRequestedDeviceApproval:isSensitive:]
+ -[WCRRemoteAskToViewController configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:isSensitive:overridePolicy:iframe:]
+ -[WCRRemoteAskToViewController userRequestedDeviceApproval:isSensitive:]
+ -[WCRRemoteDeviceApprovalViewController setURL:isSensitive:]
+ -[WCRShieldState initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:isSensitive:]
+ -[WCRShieldState isSensitive]
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table7
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table88
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_IVAR_$_WCRShieldState._isSensitive
+ ___113-[WCRBrowserEngineClient _presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:]_block_invoke
+ ___113-[WCRBrowserEngineClient _presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:]_block_invoke_2
+ ___113-[WCRBrowserEngineClient _presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:]_block_invoke_3
+ ___118+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]_block_invoke
+ ___119+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]_block_invoke
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke_3
+ ___59-[WCRBrowserEngineClient _fetchAndCacheAgeVerificationText]_block_invoke_3
+ ___66-[WCRBrowserEngineClient userRequestedDeviceApproval:isSensitive:]_block_invoke
+ ___66-[WCRBrowserEngineClient userRequestedDeviceApproval:isSensitive:]_block_invoke_2
+ ___83-[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]_block_invoke
+ ___83-[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e8_v16?0Q8ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_40_e8_32bs_e19_v20?0B8"NSData"12ls32l8
+ ___block_descriptor_41_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_57_e8_32s40s48s_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v12?0B8ls32l8s40l8s48l8s56l8s64l8
+ __fetchAndCacheAgeVerificationText.loadOnce
+ _objc_msgSend$URL
+ _objc_msgSend$_blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:
+ _objc_msgSend$_evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:
+ _objc_msgSend$_isSensitiveURL:usingBloomFilter:
+ _objc_msgSend$_presentAskToBrowseMenuForURL:state:presentingView:presentingViewController:completion:
+ _objc_msgSend$componentsWithString:
+ _objc_msgSend$configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:isSensitive:overridePolicy:iframe:
+ _objc_msgSend$evaluateNonSensitiveURL:withCompletion:onCompletionQueue:
+ _objc_msgSend$initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:isSensitive:
+ _objc_msgSend$isSensitive
+ _objc_msgSend$isSensitive:
+ _objc_msgSend$loadAndReturnError:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setURL:isSensitive:
+ _objc_msgSend$shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:
+ _objc_msgSend$userRequestedDeviceApproval:isSensitive:
- +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:]
- +[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]
- +[WCRBrowserEngineClient allowURLWithFamilyControls:referrerURL:withCompletion:]
- +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:]
- -[WCRBrowserEngineClient askToBrowseURL]
- -[WCRBrowserEngineClient setAskToBrowseURL:]
- -[WCRBrowserEngineClient userRequestedDeviceApproval]
- -[WCRRemoteAskToViewController configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:overridePolicy:iframe:]
- -[WCRRemoteAskToViewController userRequestedDeviceApproval]
- -[WCRRemoteDeviceApprovalViewController setURL:]
- -[WCRShieldState initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:]
- GCC_except_table44
- GCC_except_table50
- GCC_except_table6
- GCC_except_table77
- GCC_except_table79
- GCC_except_table81
- _OBJC_IVAR_$_WCRBrowserEngineClient._askToBrowseURL
- ___106+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:]_block_invoke
- ___107+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:]_block_invoke
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_2
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_3
- ___53-[WCRBrowserEngineClient userRequestedDeviceApproval]_block_invoke
- ___53-[WCRBrowserEngineClient userRequestedDeviceApproval]_block_invoke_2
- ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke
- ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke_2
- ___85-[WCRBrowserEngineClient askToBrowseContextMenu:presentingView:state:withCompletion:]_block_invoke_3
- ___block_descriptor_40_e28_"NSString"16?0"NSString"8l
- ___block_descriptor_48_e8_32s40s_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v12?0B8ls32l8s40l8s48l8s56l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e8_v16?0Q8ls32l8s40l8s48l8s56l8s72l8s64l8
- _objc_msgSend$_blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:
- _objc_msgSend$_evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:
- _objc_msgSend$askToBrowseURL
- _objc_msgSend$configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:overridePolicy:iframe:
- _objc_msgSend$initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:
- _objc_msgSend$setAskToBrowseURL:
- _objc_msgSend$shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:
- _objc_msgSend$userRequestedDeviceApproval
CStrings:
+ "%@/0/%@/%@"
+ "/System/Library/PrivateFrameworks/FamilyCircle.framework"
+ "0"
+ "AV: Failed to load FamilyCircle.framework: %@"
+ "AV: Loaded FamilyCircle.framework"
+ "WCRAuthenticationSites-2026-07-19.plist"
+ "displayURL"
+ "http://0.0.0.0/webfilter.local"
+ "isSensitive"
+ "showBadge"
+ "subtitle"
+ "symbol"
+ "title"
+ "url"
+ "v20@?0B8@\"NSData\"12"
+ "x-apple-content-filter://unblock?context=%@&shield=%@&isSensitive=%@"
- "WCRAuthenticationSites-2026-06-03.plist"
- "x-apple-content-filter://unblock?context=%@&shield=%@"
```
