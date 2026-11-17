## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-626.1.12.10.3
-  __TEXT.__text: 0x30eb48
-  __TEXT.__objc_methlist: 0x1689c
-  __TEXT.__gcc_except_tab: 0x1ee98
-  __TEXT.__const: 0x80394
-  __TEXT.__cstring: 0x25ea4
+626.1.17.0.0
+  __TEXT.__text: 0x31bde4
+  __TEXT.__objc_methlist: 0x1690c
+  __TEXT.__gcc_except_tab: 0x1ef94
+  __TEXT.__const: 0x807f4
+  __TEXT.__cstring: 0x25fb4
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x17132
+  __TEXT.__oslogstring: 0x17252
   __TEXT.__dlopen_cstrs: 0x2b7
-  __TEXT.__swift5_typeref: 0x450a
-  __TEXT.__swift5_fieldmd: 0x264c
-  __TEXT.__constg_swiftt: 0x2b84
-  __TEXT.__swift5_reflstr: 0x233d
+  __TEXT.__swift5_typeref: 0x45be
+  __TEXT.__swift5_fieldmd: 0x276c
+  __TEXT.__constg_swiftt: 0x2c64
+  __TEXT.__swift5_reflstr: 0x23fd
   __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_assocty: 0x600
+  __TEXT.__swift5_assocty: 0x618
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__swift5_proto: 0x648
-  __TEXT.__swift5_types: 0x268
-  __TEXT.__swift5_capture: 0x1a28
+  __TEXT.__swift5_proto: 0x678
+  __TEXT.__swift5_types: 0x27c
+  __TEXT.__swift5_capture: 0x1a68
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__swift_as_entry: 0x238
-  __TEXT.__swift_as_ret: 0x240
-  __TEXT.__swift_as_cont: 0x4d4
-  __TEXT.__unwind_info: 0x13118
-  __TEXT.__eh_frame: 0x7ea0
+  __TEXT.__swift_as_entry: 0x23c
+  __TEXT.__swift_as_ret: 0x248
+  __TEXT.__swift_as_cont: 0x4e0
+  __TEXT.__unwind_info: 0x13370
+  __TEXT.__eh_frame: 0x80b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16948
+  __DATA_CONST.__const: 0x16ae0
   __DATA_CONST.__objc_classlist: 0xd10
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc408
+  __DATA_CONST.__objc_selrefs: 0xc480
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x978
   __DATA_CONST.__objc_arraydata: 0xb00
-  __DATA_CONST.__got: 0x23b8
-  __AUTH_CONST.__const: 0xddd8
-  __AUTH_CONST.__cfstring: 0x1b5a0
-  __AUTH_CONST.__objc_const: 0x29610
+  __DATA_CONST.__got: 0x23d0
+  __AUTH_CONST.__const: 0xe1b0
+  __AUTH_CONST.__cfstring: 0x1b620
+  __AUTH_CONST.__objc_const: 0x296d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x32d8
+  __AUTH_CONST.__auth_got: 0x3310
   __AUTH.__objc_data: 0x80a8
-  __AUTH.__data: 0x1eb0
-  __DATA.__objc_ivar: 0x1994
-  __DATA.__data: 0x64f8
-  __DATA.__common: 0xf8
+  __AUTH.__data: 0x1ed0
+  __DATA.__objc_ivar: 0x19a8
+  __DATA.__data: 0x65f8
+  __DATA.__common: 0xf0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x9
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16772
-  Symbols:   19866
-  CStrings:  6463
+  Functions: 16936
+  Symbols:   19928
+  CStrings:  6473
 
Symbols:
+ -[WBSOfflineSearchSuggestionsFetcher disconnectFromSearchHelperIfNecessary]
+ -[WBSSiriIntelligenceDonor _getItemCountForSearchQuery:withCompletionHandler:]
+ -[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]
+ -[WBSSiriIntelligenceDonor _reportDonationProgress]
+ -[WBSSiriIntelligenceDonor _scheduleDonationProgressReportAfterDelay:]
+ -[WBSSiriIntelligenceDonor _setKnownBookmarkCountForDonationProgress:]
+ -[WBSSiriIntelligenceDonor _setNeedsDonationProgressReport]
+ -[WBSSiriIntelligenceDonor startReportingDonationProgressWithProfileIdentifiersProvider:]
+ _OBJC_CLASS_$_CSDonationProgress
+ _OBJC_IVAR_$_WBSOfflineSearchSuggestionsFetcher._connectionGeneration
+ _OBJC_IVAR_$_WBSOfflineSearchSuggestionsFetcher._hasConnectionToSearchHelper
+ _OBJC_IVAR_$_WBSSiriIntelligenceDonor._donationProgressReportTimer
+ _OBJC_IVAR_$_WBSSiriIntelligenceDonor._knownBookmarkCountForDonationProgress
+ _OBJC_IVAR_$_WBSSiriIntelligenceDonor._profileIdentifiersProvider
+ _WBSOnboardingIdentifierWhatsNewInSafari
+ __ZL11sharedStore
+ ___44-[WBSCloudHistory _serverBackoffTimerFired:]_block_invoke
+ ___51-[WBSSiriIntelligenceDonor _reportDonationProgress]_block_invoke
+ ___59-[WBSSiriIntelligenceDonor _setNeedsDonationProgressReport]_block_invoke
+ ___60-[WBSHistory clearHistoryFromDate:toDate:completionHandler:]_block_invoke_4
+ ___70-[WBSSiriIntelligenceDonor _scheduleDonationProgressReportAfterDelay:]_block_invoke
+ ___70-[WBSSiriIntelligenceDonor _setKnownBookmarkCountForDonationProgress:]_block_invoke
+ ___78-[WBSSiriIntelligenceDonor _getItemCountForSearchQuery:withCompletionHandler:]_block_invoke
+ ___78-[WBSSiriIntelligenceDonor _getItemCountForSearchQuery:withCompletionHandler:]_block_invoke_2
+ ___78-[WBSSiriIntelligenceDonor _getItemCountForSearchQuery:withCompletionHandler:]_block_invoke_3
+ ___81-[WBSPerSitePreferenceManager setValue:ofPreference:forDomain:completionHandler:]_block_invoke_3
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke_2
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke_3
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke_4
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke_5
+ ___83-[WBSSiriIntelligenceDonor _reportDonationProgressForProfiles:includesAllProfiles:]_block_invoke_6
+ ___93-[WBSPerSitePreferencesSQLiteStore savePerSiteSettingCloudKitRecordToDisk:completionHandler:]_block_invoke
+ ___93-[WBSPerSitePreferencesSQLiteStore savePerSiteSettingCloudKitRecordToDisk:completionHandler:]_block_invoke_2
+ ___97-[WBSPerSitePreferenceManager removePreferenceValuesForDomains:fromPreference:completionHandler:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32r40r_e11_v24?0Q8Q16lr32l8r40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_ea8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r_e20_v24?0Q8"NSError"16lr48l8s40l8s32l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0lr40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e20_v24?0Q8"NSError"16lr56l8s32l8s48l8r64l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e20_v24?0q8"NSError"16ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8
+ ___swift_closure_destructor.156Tm
+ ___swift_closure_destructor.161Tm
+ ___swift_closure_destructor.192Tm
+ ___swift_memcpy9_8
+ _associated conformance 12SafariShared11WebsiteRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLVSHAASQ
+ _associated conformance 12SafariShared17AutoDarkModeQuirkOSHAASQ
+ _associated conformance 12SafariShared20WBSClusterReportDataV0cD8ItemInfoV18UserOrganizedStateOSHAASQ
+ _associated conformance 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLVSHAASQ
+ _keypath_get.37Tm
+ _symbolic SDySSShy_____GG 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic SDy_____SaySSGG 10Foundation4UUIDV
+ _symbolic _____ 12SafariShared11WebsiteRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____ 12SafariShared16WebsiteRuleIndex33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____ 12SafariShared17AutoDarkModeQuirkO
+ _symbolic _____ 12SafariShared18AutoDarkModeQuirksV
+ _symbolic _____ 12SafariShared20WBSClusterReportDataV0cD8ItemInfoV18UserOrganizedStateO
+ _symbolic _____ 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____Sg 12SafariShared18AutoDarkModeQuirksV
+ _symbolic ______SaySSGt 10Foundation4UUIDV
+ _symbolic _____ySSSgG s23_ContiguousArrayStorageC
+ _symbolic _____ySSShy_____GG s18_DictionaryStorageC 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 12SafariShared17AutoDarkModeQuirkO
+ _symbolic _____yShySSGG s11_SetStorageC
+ _symbolic _____yShySSGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s11_SetStorageC 12SafariShared11WebsiteRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____y_____G s11_SetStorageC 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _symbolic _____y_____SaySSGG s18_DictionaryStorageC 10Foundation4UUIDV
+ _type_layout_string 12SafariShared11WebsiteRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _type_layout_string 12SafariShared16WebsiteRuleIndex33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
+ _type_layout_string 12SafariShared8PathRule33_0A3DDE34CC0E3C82713961AF069B0CCDLLV
- -[WBSOfflineSearchSuggestionsFetcher dealloc]
- __ZZ54+[WBSUserDefinedContentBlockerSQLiteStore sharedStore]E11sharedStore
- ___79-[WBSSiriIntelligenceDonor _getItemExistsForSearchQuery:withCompletionHandler:]_block_invoke_2
- ___79-[WBSSiriIntelligenceDonor _getItemExistsForSearchQuery:withCompletionHandler:]_block_invoke_3
- ___block_descriptor_65_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___swift_closure_destructor.152Tm
- ___swift_closure_destructor.164Tm
- ___swift_closure_destructor.185Tm
- ___swift_closure_destructor.45Tm
- _keypath_get.28Tm
- _symbolic SDy__________G 10Foundation4UUIDV AA4DateV
- _symbolic SaySSGSg
- _symbolic ___________t 10Foundation4UUIDV AA4DateV
- _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV AC4DateV
CStrings:
+ "8626.1.17"
+ "Applying Dark Mode"
+ "CREATE TABLE IF NOT EXISTS deleted_cloudkit_records (record_name TEXT NOT NULL UNIQUE, sync_data BLOB)"
+ "DELETE FROM deleted_cloudkit_records"
+ "Failed to clear the deleted_cloudkit_records database table for Per-Site Settings: (%d)"
+ "Failed to count items when reporting Spotlight donation progress"
+ "Failed to report Spotlight donation progress with error: %{public}@"
+ "Failed to restore the deleted_cloudkit_records table: %{public}@ (%d)"
+ "Incompatible UI suppressed"
+ "Reporting Spotlight donation progress: %lu known items, %lu items needing donation, partial: %d"
+ "Saving deleted CloudKit sync data with record name: %{public}@."
+ "Unexpected User Organized value: "
+ "WhatsNewInSafari27C"
+ "domainIdentifier == \"%@\""
+ "suppress-incompatible-ui"
+ "v24@?0Q8Q16"
- "\v"
- "8626.1.12.10.3"
- "Adaptive Dark Mode On"
- "DROP TABLE IF EXISTS deleted_cloudkit_records"
- "Failed to drop deleted_cloudkit_records database table for Per-Site Settings: (%d)"
- "Saving deleted CloudKit sync data: %{sensitive, mask.hash}@ with record name: %{public}@."
```
