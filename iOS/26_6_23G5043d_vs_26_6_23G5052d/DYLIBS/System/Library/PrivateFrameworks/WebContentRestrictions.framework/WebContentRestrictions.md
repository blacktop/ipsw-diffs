## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-  __TEXT.__text: 0xaed4
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x75c
+  __TEXT.__text: 0xbaa0
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x7e8
   __TEXT.__const: 0x560
-  __TEXT.__cstring: 0xf5c
-  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__cstring: 0x128c
+  __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x1b3
   __TEXT.__swift5_typeref: 0x10c
   __TEXT.__constg_swiftt: 0x220

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x1860
-  __TEXT.__objc_methtype: 0x2d1
-  __TEXT.__objc_stubs: 0x1600
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x338
+  __TEXT.__objc_methname: 0x1b38
+  __TEXT.__objc_methtype: 0x2f4
+  __TEXT.__objc_stubs: 0x17e0
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x389
-  __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0xc90
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0xd28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x310
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x190
   __DATA.__bss: 0x690
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 296
-  Symbols:   1327
-  CStrings:  617
+  Functions: 312
+  Symbols:   1391
+  CStrings:  682
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[WCRBrowserEngineClient _blockPageForURL:inLanguage:withAllowButton:isAgeVerificationCriteriaMet:ageVerificationText:]
+ +[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:]
+ +[WCRBrowserEngineClient _isAgeVerificationCriteriaMet]
+ -[WCRBrowserEngineClient _reloadAgeVerificationCriteria]
+ -[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]
+ -[WCRBrowserEngineClient cachedAgeVerificationText]
+ -[WCRBrowserEngineClient dealloc]
+ -[WCRBrowserEngineClient isAgeVerificationCriteriaMet]
+ -[WCRBrowserEngineClient oseChangeNotifyToken]
+ -[WCRBrowserEngineClient setCachedAgeVerificationText:]
+ -[WCRBrowserEngineClient setIsAgeVerificationCriteriaMet:]
+ -[WCRBrowserEngineClient setOseChangeNotifyToken:]
+ -[WCRRemotePINEntryViewController openScreenTimeSettingsWithCompletion:]
+ GCC_except_table2
+ GCC_except_table37
+ GCC_except_table6
+ GCC_except_table7
+ _OBJC_CLASS_$_FAAgeRangeController
+ _OBJC_CLASS_$_OSEligibilityQuery
+ _OBJC_IVAR_$_WCRBrowserEngineClient._cachedAgeVerificationText
+ _OBJC_IVAR_$_WCRBrowserEngineClient._isAgeVerificationCriteriaMet
+ _OBJC_IVAR_$_WCRBrowserEngineClient._oseChangeNotifyToken
+ ___244+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke
+ ___244+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_2
+ ___244+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_3
+ ___54-[WCRBrowserEngineClient initWithConfigurationAtPath:]_block_invoke
+ ___56-[WCRBrowserEngineClient _reloadAgeVerificationCriteria]_block_invoke
+ ___56-[WCRBrowserEngineClient _reloadAgeVerificationCriteria]_block_invoke_2
+ ___89-[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]_block_invoke
+ ___89-[WCRBrowserEngineClient _requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e34_v24?0"NSDictionary"8"NSError"16lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32s40w_e30_v24?0"NSNumber"8"NSError"16ls32l8w40l8
+ _dispatch_get_global_queue
+ _notify_cancel
+ _objc_msgSend$_blockPageForURL:inLanguage:withAllowButton:isAgeVerificationCriteriaMet:ageVerificationText:
+ _objc_msgSend$_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:
+ _objc_msgSend$_isAgeVerificationCriteriaMet
+ _objc_msgSend$_reloadAgeVerificationCriteria
+ _objc_msgSend$_requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:
+ _objc_msgSend$answer
+ _objc_msgSend$cachedAgeVerificationText
+ _objc_msgSend$fetchDSIDWithCompletionHandler:
+ _objc_msgSend$getAgeVerificationInfoForDSID:completion:
+ _objc_msgSend$initWithDomain:error:
+ _objc_msgSend$isAgeVerificationCriteriaMet
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$openScreenTimeSettingsWithCompletion:
+ _objc_msgSend$oseChangeNotifyToken
+ _objc_msgSend$setCachedAgeVerificationText:
+ _objc_msgSend$setIsAgeVerificationCriteriaMet:
+ _objc_msgSend$stringValue
+ _objc_retain_x2
+ _objc_setProperty_atomic_copy
- +[WCRBrowserEngineClient _blockPageForURL:inLanguage:withAllowButton:]
- +[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]
- GCC_except_table31
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_2
- ___195+[WCRBrowserEngineClient _evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:]_block_invoke_3
- _objc_msgSend$_blockPageForURL:inLanguage:withAllowButton:
- _objc_msgSend$_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:
CStrings:
+ "@48@0:8@16@24B32B36@40"
+ "AGE_VERIFICATION_FALLBACK_VISIBILITY_NO_LOC"
+ "AGE_VERIFICATION_TEXT_NO_LOC"
+ "AGE_VERIFY_UNBLOCK_TITLE_VISIBILITY_NO_LOC"
+ "AV: Failed to fetch DSID for age verification: %@"
+ "AV: Fetching DSID..."
+ "AV: Getting AV Info..."
+ "AV: Got AV Info"
+ "AV: Got DSID"
+ "AV: getAgeVerificationInfo error: %@"
+ "Failed to connect to WCRUI for age verification Settings navigation: %@"
+ "Failed to open Screen Time Settings for age verification: %@"
+ "OSE Error: %@"
+ "OSE Response: %s"
+ "OSE change notification received, reloading age verification criteria"
+ "STANDARD_UNBLOCK_TITLE_VISIBILITY_NO_LOC"
+ "T@\"NSString\",C,V_cachedAgeVerificationText"
+ "TB,V_isAgeVerificationCriteriaMet"
+ "Ti,N,V_oseChangeNotifyToken"
+ "_blockPageForURL:inLanguage:withAllowButton:isAgeVerificationCriteriaMet:ageVerificationText:"
+ "_cachedAgeVerificationText"
+ "_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:isAgeVerificationCriteriaMet:ageVerificationText:withCompletion:onCompletionQueue:"
+ "_isAgeVerificationCriteriaMet"
+ "_oseChangeNotifyToken"
+ "_reloadAgeVerificationCriteria"
+ "_requestOpenScreenTimeSettingsForAgeVerificationWithCompletion:"
+ "ageAssuranceStringsMap"
+ "answer"
+ "cachedAgeVerificationText"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-required-screen-time"
+ "eligible"
+ "fetchDSIDWithCompletionHandler:"
+ "getAgeVerificationInfoForDSID:completion:"
+ "i16@0:8"
+ "ineligible"
+ "initWithDomain:error:"
+ "isAgeVerificationCriteriaMet"
+ "objectForKeyedSubscript:"
+ "openScreenTimeSettingsWithCompletion:"
+ "oseChangeNotifyToken"
+ "screenTimeWebContentFilterAdultVerificationReason"
+ "setCachedAgeVerificationText:"
+ "setIsAgeVerificationCriteriaMet:"
+ "setOseChangeNotifyToken:"
+ "stringValue"
+ "style=\"display:none\""
+ "v124@0:8@16Q24@32@40@48@56@64@72@80@88B96@100@?108@116"
+ "v20@0:8i16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "@36@0:8@16@24B32"
- "_blockPageForURL:inLanguage:withAllowButton:"
- "_evaluateURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:withCompletion:onCompletionQueue:"
- "v112@0:8@16Q24@32@40@48@56@64@72@80@88@?96@104"

```
