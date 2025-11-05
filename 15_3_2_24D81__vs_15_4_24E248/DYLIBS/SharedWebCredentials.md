## SharedWebCredentials

> `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/Versions/A/SharedWebCredentials`

```diff

 1021.2.0.0.0
-  __TEXT.__text: 0x16dd0
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0xe60
-  __TEXT.__gcc_except_tab: 0x26b0
+  __TEXT.__text: 0x16d58
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0xf9c
   __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x264c
   __TEXT.__cstring: 0x1569
   __TEXT.__oslogstring: 0x896
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__unwind_info: 0xa40
   __TEXT.__objc_classname: 0x214
   __TEXT.__objc_methname: 0x2b85
   __TEXT.__objc_methtype: 0xb22
   __TEXT.__objc_stubs: 0x1e60
   __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__objc_const: 0x1780
+  __AUTH_CONST.__objc_const: 0x1548
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x50
+  __AUTH.__thread_vars: 0x18
   __AUTH.__thread_data: 0x4
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x1c8
   __DATA.__common: 0x90
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__thread_vars: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17CDB19E-E3F8-38C5-870E-7D8617E814C0
+  UUID: D4E926B0-20B8-3698-858A-E9E7C2907EFD
   Functions: 409
-  Symbols:   1245
+  Symbols:   1236
   CStrings:  1027
 
Symbols:
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB8nn190102EPKcm
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ __block_literal_global.275
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE4findB8nn180100EPKcm
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn180100EPKvm
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- __block_literal_global.274
- _strncmp
Functions:
~ -[_SWCPattern init] : 48 -> 16
~ -[_SWCPattern initWithDictionary:defaults:] : 1728 -> 1752
~ -[_SWCPattern dealloc] : 84 -> 88
~ -[_SWCPattern isBlocking] : 36 -> 44
~ -[_SWCPattern evaluateWithURLComponents:substitutionVariables:auditToken:] : 220 -> 216
~ __ZNK17SWCPatternStorage8evaluateEP15NSURLComponentsPK10SWCFNMatchPK13audit_token_t : 2064 -> 2080
~ +[_SWCPatternList patternListWithArray:] : 640 -> 636
~ -[_SWCPatternList enumeratePatternsWithBlock:] : 232 -> 236
~ -[_SWCPatternList evaluateWithURLComponents:substitutionVariables:auditToken:matchingPattern:index:] : 352 -> 348
~ -[_SWCPatternList initWithCoder:] : 1432 -> 1448
~ ___68+[_SWCSubstitutionVariableList cheapBuiltInSubstitutionVariableList]_block_invoke : 632 -> 640
~ __ZNK23SWCSubstitutionVariable7getSizeEv : 92 -> 96
~ +[_SWCSubstitutionVariableList substitutionVariableListWithDictionary:] : 536 -> 524
~ ___71+[_SWCSubstitutionVariableList substitutionVariableListWithDictionary:]_block_invoke : 1412 -> 1432
~ -[_SWCSubstitutionVariableList enumerateSubstitutionVariablesWithBlock:] : 248 -> 252
~ -[_SWCSubstitutionVariableList initWithCoder:] : 1496 -> 1512
~ __ZNK23SWCSubstitutionVariable13getNameNoCopyEv : 100 -> 112
~ __ZN17SWCPatternStorage15_EvaluateStringEP8NSStringRKNSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEPK10SWCFNMatchib : 996 -> 1000
~ __ZN17SWCPatternStorage22_ReconstituteQueryJSONERKNSt3__117basic_string_viewIcNS0_11char_traitsIcEEEE : 464 -> 468
~ __Z20SWCGetFastUTF8StringILm1024EENSt3__18optionalINS0_17basic_string_viewIcNS0_11char_traitsIcEEEEEEP8NSStringRNS0_5arrayIcXT_EEE : 204 -> 224
~ ____ZN17SWCPatternStorage18_EvaluateQueryJSONEP7NSArrayIP14NSURLQueryItemERKNSt3__117basic_string_viewIcNS5_11char_traitsIcEEEEPK10SWCFNMatchi_block_invoke : 172 -> 176
~ __ZL34SWCGetNSStringFromStringViewNoCopyRKNSt3__117basic_string_viewIcNS_11char_traitsIcEEEE : 96 -> 108
~ __ZL29SWCEnumerateStructureSequenceI23SWCSubstitutionVariableZNK10SWCFNMatch12_getVariableERKNSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEE3$_0EvPKT_RKT0_ : 1164 -> 1156
~ __ZNK10SWCFNMatch8_executeERKNSt3__117basic_string_viewIcNS0_11char_traitsIcEEEES6_i : 2216 -> 2188
~ __ZNK10SWCFNMatch20_decodeUTF8CharacterEPKcS1_ : 392 -> 404
~ -[_SWCServiceSettings commitReturningError:] : 568 -> 564
~ ___44-[_SWCServiceSettings commitReturningError:]_block_invoke_2 : 172 -> 176
~ +[_SWCServiceSettings(Removal) removeObjectsForKeys:serviceType:error:] : 696 -> 688
~ +[_SWCServiceSettings(Removal) removeObjectsForKeys:serviceSpecifier:error:] : 696 -> 688
~ -[_SWCChatterboxResolver init] : 48 -> 16
~ -[_SWCPrefs isAppleInternal] : 68 -> 72
~ -[_SWCApplicationIdentifier init] : 48 -> 16
~ -[_SWCApplicationIdentifier UUIDRepresentation] : 380 -> 376
~ __SWCFieldsLogDebugDescription : 584 -> 596
~ __SWCServiceApprovalStateGetDebugDescription : 116 -> 112
~ __SWCCanAuditTokenConnect : 104 -> 100
~ -[_SWCServiceDetails init] : 48 -> 16
~ -[_SWCServiceDetails(SWCServiceApproval) setUserApprovalState:error:] : 536 -> 528
~ __69-[_SWCServiceDetails(SWCServiceApproval) setUserApprovalState:error:]_block_invoke.57 : 148 -> 152
~ -[_SWCServiceDetails(SWCExtendedServiceDetails) isEnabledByDefault] : 80 -> 92
~ ___110+[_SWCServiceDetails(Private) _serviceDetailsWithServiceSpecifier:URLComponents:limit:callerAuditToken:error:]_block_invoke_2 : 156 -> 144
~ -[_SWCPatternMatchingEngine init] : 48 -> 16
~ -[_SWCPatternMatchingResult init] : 48 -> 16
~ -[_SWCTrackingDomainInfo init] : 48 -> 16
~ +[_SWCTrackingDomainInfo trackingDomainInfoWithDomains:] : 844 -> 848
~ -[_SWCDomain init] : 48 -> 16
~ -[_SWCDomain initWithString:] : 1304 -> 1300
~ -[_SWCDomain rawValue] : 396 -> 400
~ -[_SWCDomain encompassesDomain:] : 708 -> 712
~ -[_SWCDomain nonWildcardDomain] : 96 -> 100
~ -[_SWCDomain wildcardDomain] : 96 -> 100
~ -[_SWCDomain redactedDescription] : 1044 -> 1048
CStrings:
+ "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"
- "void SWCWithFastBuffer(NSUInteger, const FunctionType &) [ElementType = char, ArraySize = 128UL, FunctionType = (lambda at /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SharedWebCredentials/Sources/SWCPattern.mm:2001:65)]"

```
