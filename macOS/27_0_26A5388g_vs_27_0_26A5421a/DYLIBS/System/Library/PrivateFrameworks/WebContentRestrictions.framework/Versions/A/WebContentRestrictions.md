## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/Versions/A/WebContentRestrictions`

```diff

-70.0.0.0.0
-  __TEXT.__text: 0x10efc
-  __TEXT.__objc_methlist: 0xc20
+73.0.0.0.2
+  __TEXT.__text: 0x11508
+  __TEXT.__objc_methlist: 0xc60
   __TEXT.__const: 0x670
-  __TEXT.__cstring: 0x15a1
+  __TEXT.__cstring: 0x15d1
   __TEXT.__gcc_except_tab: 0x1cc
   __TEXT.__oslogstring: 0x4c6
   __TEXT.__ustring: 0x1bc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__unwind_info: 0x488
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x8c8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x1b0
-  __AUTH_CONST.__const: 0x609
-  __AUTH_CONST.__cfstring: 0x1900
-  __AUTH_CONST.__objc_const: 0x1540
+  __AUTH_CONST.__const: 0x669
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x1570
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x4e8
   __AUTH.__objc_data: 0x4a0
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x2a8
   __DATA.__bss: 0x690
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 432
-  Symbols:   1275
-  CStrings:  264
+  Functions: 442
+  Symbols:   1293
+  CStrings:  266
 
Symbols:
+ +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]
+ +[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _familyControlsOverrideCommandForURL:state:]
+ +[WCRBrowserEngineClient _isSensitiveURL:usingBloomFilter:]
+ +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]
+ -[WCRBloomFilter isSensitive:]
+ -[WCRBrowserEngineClient allowURLWithFamilyControls:referrerURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:]
+ -[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]
+ -[WCRBrowserEngineClient userRequestedDeviceApproval:isSensitive:]
+ -[WCRRemoteAskToViewController configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:isSensitive:overridePolicy:iframe:]
+ -[WCRRemoteAskToViewController userRequestedDeviceApproval:isSensitive:]
+ -[WCRRemoteDeviceApprovalViewController setURL:isSensitive:]
+ -[WCRShieldState initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:isSensitive:]
+ -[WCRShieldState isSensitive]
+ GCC_except_table61
+ OBJC_IVAR_$_WCRShieldState._isSensitive
+ __305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke
+ __83-[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]_block_invoke
+ ___118+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:]_block_invoke
+ ___119+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:]_block_invoke
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___305+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:]_block_invoke_3
+ ___83-[WCRBrowserEngineClient evaluateNonSensitiveURL:withCompletion:onCompletionQueue:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e8_v16?0Q8l
+ ___block_descriptor_40_e8_32bs_e19_v20?0B8"NSData"12l
+ ___block_descriptor_41_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b
+ ___destroy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ _objc_msgSend$_blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:
+ _objc_msgSend$_evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:generateBlockPage:withCompletion:onCompletionQueue:
+ _objc_msgSend$_familyControlsOverrideCommandForURL:state:
+ _objc_msgSend$_isSensitiveURL:usingBloomFilter:
+ _objc_msgSend$evaluateNonSensitiveURL:withCompletion:onCompletionQueue:
+ _objc_msgSend$initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:isSensitive:
+ _objc_msgSend$isSensitive
+ _objc_msgSend$isSensitive:
+ _objc_msgSend$shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:isSensitive:language:
+ _objc_msgSend$userRequestedDeviceApproval:isSensitive:
- +[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:]
- +[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]
- +[WCRBrowserEngineClient allowURLWithFamilyControls:referrerURL:withCompletion:]
- +[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:]
- -[WCRBrowserEngineClient userRequestedDeviceApproval]
- -[WCRRemoteAskToViewController configureWithURL:symbol:title:subtitle:displayURL:showBadge:shieldType:overridePolicy:iframe:]
- -[WCRRemoteAskToViewController userRequestedDeviceApproval]
- -[WCRRemoteDeviceApprovalViewController setURL:]
- -[WCRShieldState initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:]
- GCC_except_table49
- __287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke
- ___106+[WCRBrowserEngineClient shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:]_block_invoke
- ___107+[WCRBrowserEngineClient _blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:]_block_invoke
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_2
- ___287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_3
- ___block_descriptor_40_e28_"NSString"16?0"NSString"8l
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e8_v16?0Q8l
- ___copy_helper_block_e8_32s40s48s56s64s72b
- ___destroy_helper_block_e8_32s40s48s56s64s72s
- _objc_msgSend$_blockPageForURL:inLanguage:shieldType:overridePolicy:iframe:ageVerificationText:
- _objc_msgSend$_evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:
- _objc_msgSend$initWithSymbol:title:subtitle:displayURL:showBadge:buttons:shieldType:overridePolicy:iframe:
- _objc_msgSend$shieldStateForURL:shieldType:overridePolicy:iframe:ageVerificationText:language:
- _objc_msgSend$userRequestedDeviceApproval
CStrings:
+ "WCRAuthenticationSites-2026-07-19.plist"
+ "isSensitive"
+ "v20@?0B8@\"NSData\"12"
+ "x-apple-content-filter://unblock?context=%@&shield=%@&isSensitive=%@"
- "WCRAuthenticationSites-2026-06-03.plist"
- "x-apple-content-filter://unblock?context=%@&shield=%@"
```
