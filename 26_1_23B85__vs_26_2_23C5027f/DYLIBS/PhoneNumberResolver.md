## PhoneNumberResolver

> `/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver`

```diff

-39.30.9.7.3
-  __TEXT.__text: 0x6868
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x380
+40.32.10.16.1
+  __TEXT.__text: 0x6108
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x370
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x396
-  __TEXT.__oslogstring: 0x820
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__cstring: 0x3c6
+  __TEXT.__oslogstring: 0x767
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0xa1
-  __TEXT.__objc_methname: 0xed4
+  __TEXT.__objc_methname: 0xeb1
   __TEXT.__objc_methtype: 0x222
   __TEXT.__objc_stubs: 0xfc0
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__objc_arraydata: 0xb8
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x638
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x40
   __DATA.__data: 0x8

   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D46A36E9-BFE8-33BF-9AED-42C031753EA4
-  Functions: 109
-  Symbols:   564
+  UUID: 54582A29-9759-32C7-A4A3-2BE7FEFF78B4
+  Functions: 104
+  Symbols:   551
   CStrings:  392
 
Symbols:
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:]
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.1
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.2
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.3
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.4
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.5
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.6
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.7
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.8
+ -[PNRResourceManager _bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.9
+ -[PNRResourceManager lookupAssetSliceForPhoneNumber:logId:withResult:]
+ -[PNRResourceManager lookupISOCountryCodeFromNumber:logId:withResult:]
+ -[PNRResourceManager lookupStringForPhoneNumber:inSlice:countryCodeOfDevice:logId:withResult:]
+ -[PNRResourceManager openAssetSliceFileUsingLogId:withResult:]
+ -[PNRResourceManager openIntlFileUsingLogId:withResult:]
+ -[PNRResourceManager openPNRFilesForSlice:logId:withResult:]
+ -[PNRStringsFileReaderResult aggregateStringWhileInCountry:forLanguage:]
+ -[PNRStringsFileReaderResult shouldOrderCityFirstForLanguage:]
+ _OBJC_IVAR_$_PNRResourceManager._maCache
+ ___60-[PNRResourceManager openPNRFilesForSlice:logId:withResult:]_block_invoke
+ ___70-[PNRResourceManager lookupAssetSliceForPhoneNumber:logId:withResult:]_block_invoke
+ ___70-[PNRResourceManager lookupISOCountryCodeFromNumber:logId:withResult:]_block_invoke
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.73
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.75
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.75.cold.1
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.79
+ ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.79.cold.1
+ ___94-[PNRResourceManager lookupStringForPhoneNumber:inSlice:countryCodeOfDevice:logId:withResult:]_block_invoke
+ ___block_descriptor_64_e8_32s40bs48r56r_e30_v24?0"NSString"8"NSError"16lr48l8s32l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e43_v32?0"NSString"8"NSString"16"NSError"24lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e33_v32?0"NSString"8q16"NSError"24lr80l8s32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e43_v32?0"NSString"8"NSString"16"NSError"24ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
+ _objc_msgSend$_bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:
+ _objc_msgSend$aggregateStringWhileInCountry:forLanguage:
+ _objc_msgSend$characterDirectionForLanguage:
+ _objc_msgSend$groupingSeparator
+ _objc_msgSend$languageCode
+ _objc_msgSend$lookupAssetSliceForPhoneNumber:logId:withResult:
+ _objc_msgSend$lookupISOCountryCodeFromNumber:logId:withResult:
+ _objc_msgSend$lookupStringForPhoneNumber:inSlice:countryCodeOfDevice:logId:withResult:
+ _objc_msgSend$openAssetSliceFileUsingLogId:withResult:
+ _objc_msgSend$openIntlFileUsingLogId:withResult:
+ _objc_msgSend$openPNRFilesForSlice:logId:withResult:
+ _objc_msgSend$shouldOrderCityFirstForLanguage:
+ _objc_msgSend$substringWithRange:
- +[PNRUtils _countryCodeFromInternationalCode:result:]
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:]
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.1
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.2
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.3
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.4
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.5
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.6
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.7
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.8
- -[PNRResourceManager _bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:].cold.9
- -[PNRResourceManager lookupCCForPhoneNumber:logId:withResult:]
- -[PNRResourceManager lookupISOCountryCodeFromNANPNumber:logId:withResult:]
- -[PNRResourceManager lookupStringForPhoneNumber:inCC:countryCodeOfDevice:logId:withResult:]
- -[PNRResourceManager openCountryCodeFileUsingLogId:withResult:]
- -[PNRResourceManager openNANPFileUsingLogId:withResult:]
- -[PNRResourceManager openPNRFilesForPrefix:logId:withResult:]
- -[PNRStringsFileReaderResult aggregateStringWhileInCountry:forLanguage:ccOfNumber:]
- -[PNRStringsFileReaderResult shouldOrderCityFirstForLanguage:phoneNumberInCC:]
- GCC_except_table26
- _NSUnderlyingErrorKey
- _OBJC_IVAR_$_PNRResourceManager._maURLCache
- __PNCopyCountryCodeForInternationalCode
- ___61-[PNRResourceManager openPNRFilesForPrefix:logId:withResult:]_block_invoke
- ___62-[PNRResourceManager lookupCCForPhoneNumber:logId:withResult:]_block_invoke
- ___74-[PNRResourceManager lookupISOCountryCodeFromNANPNumber:logId:withResult:]_block_invoke
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.76
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.76.cold.1
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.80
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.80.cold.1
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.82
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.82.cold.1
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.83
- ___87-[PNRPhoneNumberResolver resolveFullyQualifiedPhoneNumber:inCountry:logId:resultBlock:]_block_invoke.83.cold.1
- ___91-[PNRResourceManager lookupStringForPhoneNumber:inCC:countryCodeOfDevice:logId:withResult:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64r72r80r88r96r_e30_v24?0"NSString"8"NSError"16ls32l8r64l8r72l8s40l8s48l8s56l8r80l8r88l8r96l8
- ___block_descriptor_104_e8_32s40s48s56s64s72r80r88r96r_e33_v32?0"NSString"8q16"NSError"24lr72l8s32l8s40l8s48l8r80l8s56l8r88l8s64l8r96l8
- ___block_descriptor_64_e8_32s40r48r56r_e30_v24?0"NSString"8"NSError"16lr40l8s32l8r48l8r56l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e30_v24?0"NSString"8"NSError"16lr48l8s32l8s40l8r56l8r64l8
- _objc_msgSend$_bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:
- _objc_msgSend$_countryCodeFromInternationalCode:result:
- _objc_msgSend$aggregateStringWhileInCountry:forLanguage:ccOfNumber:
- _objc_msgSend$code
- _objc_msgSend$domain
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$lookupCCForPhoneNumber:logId:withResult:
- _objc_msgSend$lookupISOCountryCodeFromNANPNumber:logId:withResult:
- _objc_msgSend$lookupStringForPhoneNumber:inCC:countryCodeOfDevice:logId:withResult:
- _objc_msgSend$openCountryCodeFileUsingLogId:withResult:
- _objc_msgSend$openNANPFileUsingLogId:withResult:
- _objc_msgSend$openPNRFilesForPrefix:logId:withResult:
- _objc_msgSend$shouldOrderCityFirstForLanguage:phoneNumberInCC:
CStrings:
+ " %@"
+ "%@ "
+ "@32@0:8@16@24"
+ "@40@0:8@16^v24^I32"
+ "INTL"
+ "MA cache"
+ "SLICE"
+ "SLYC"
+ "[%{public}@] ISO country code %{public}@ failed to resolve to a name {%@}"
+ "[%{public}@] ISO country code %{public}@ resolved to {%@}"
+ "[%{public}@] ISO country code lookup failure for number %{private}@ (%{public}@)"
+ "[%{public}@] determined slice %{public}@ for %{private}@"
+ "[%{public}@] using only ISO cc of %{public}@ for resolution"
+ "_bestStringForInCountryPhoneNumber:slice:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:"
+ "_maCache"
+ "aggregateStringWhileInCountry:forLanguage:"
+ "characterDirectionForLanguage:"
+ "groupingSeparator"
+ "intl"
+ "languageCode"
+ "lookupAssetSliceForPhoneNumber:logId:withResult:"
+ "lookupISOCountryCodeFromNumber:logId:withResult:"
+ "lookupStringForPhoneNumber:inSlice:countryCodeOfDevice:logId:withResult:"
+ "openAssetSliceFileUsingLogId:withResult:"
+ "openIntlFileUsingLogId:withResult:"
+ "openPNRFilesForSlice:logId:withResult:"
+ "shouldOrderCityFirstForLanguage:"
+ "slice"
+ "substringWithRange:"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSError\"24"
- ", "
- "B32@0:8@16@24"
- "B40@0:8@16^v24^I32"
- "CC"
- "COCO"
- "MA URL cache"
- "NANP"
- "PNLib"
- "[%{public}@] couldn't determine cc (%{public}@)"
- "[%{public}@] country lookup failure for NANP number %{private}@ (%{public}@)"
- "[%{public}@] country lookup failure for non-NANP number %{private}@ (%{public}@)"
- "[%{public}@] determined cc %{public}@ for %{private}@"
- "[%{public}@] didn't resolved %{private}@ : %{public}@"
- "[%{public}@] found result in db for phNo %{private}@"
- "[%{public}@] localized country name lookup failure for country code %{public}@ (%{public}@)"
- "[%{public}@] using only cc of %{public}@ for resolution"
- "_bestStringForInCountryPhoneNumber:phoneNumberCC:countryOfDevice:countryTrieData:countryStrings:logId:resultBlock:"
- "_countryCodeFromInternationalCode:result:"
- "_maURLCache"
- "aggregateStringWhileInCountry:forLanguage:ccOfNumber:"
- "code"
- "domain"
- "initWithDomain:code:userInfo:"
- "lookupCCForPhoneNumber:logId:withResult:"
- "lookupISOCountryCodeFromNANPNumber:logId:withResult:"
- "lookupStringForPhoneNumber:inCC:countryCodeOfDevice:logId:withResult:"
- "nanp"
- "openCountryCodeFileUsingLogId:withResult:"
- "openNANPFileUsingLogId:withResult:"
- "openPNRFilesForPrefix:logId:withResult:"
- "shouldOrderCityFirstForLanguage:phoneNumberInCC:"

```
