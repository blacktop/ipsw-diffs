## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-618.1.15.10.15
-  __TEXT.__text: 0x16ffc0
-  __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0xf9f8
-  __TEXT.__const: 0x56690
-  __TEXT.__gcc_except_tab: 0x196c8
-  __TEXT.__cstring: 0x19fc8
-  __TEXT.__ustring: 0xd374
-  __TEXT.__oslogstring: 0xf1bd
+618.2.12.10.9
+  __TEXT.__text: 0x16ed28
+  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__objc_methlist: 0xf9e8
+  __TEXT.__const: 0x569d0
+  __TEXT.__gcc_except_tab: 0x19440
+  __TEXT.__cstring: 0x1a160
+  __TEXT.__ustring: 0xd3d8
+  __TEXT.__oslogstring: 0xeefa
   __TEXT.__dlopen_cstrs: 0x1b3
-  __TEXT.__unwind_info: 0xa798
+  __TEXT.__unwind_info: 0xa61c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x2ed9
-  __TEXT.__objc_methname: 0x3010a
-  __TEXT.__objc_methtype: 0xbb48
-  __TEXT.__objc_stubs: 0x1a3c0
-  __DATA_CONST.__got: 0x510
+  __TEXT.__objc_methname: 0x3011e
+  __TEXT.__objc_methtype: 0xba88
+  __TEXT.__objc_stubs: 0x1a2a0
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__const: 0x13ac0
   __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x190d0
+  __DATA_CONST.__objc_const: 0x190c0
   __DATA_CONST.__objc_selrefs: 0x9010
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_classrefs: 0xc48
   __DATA_CONST.__objc_superrefs: 0x870
   __DATA_CONST.__objc_arraydata: 0xc18
-  __AUTH_CONST.__cfstring: 0x17140
-  __AUTH_CONST.__const: 0x2a48
+  __AUTH_CONST.__cfstring: 0x17200
+  __AUTH_CONST.__const: 0x2a28
   __AUTH_CONST.__objc_const: 0x82d8
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0xdb8
+  __AUTH_CONST.__auth_got: 0xd60
   __AUTH.__objc_data: 0x37a0
   __DATA.__got_weak: 0x8
-  __DATA.__objc_ivar: 0x1370
+  __DATA.__objc_ivar: 0x1368
   __DATA.__data: 0x2da8
-  __DATA.__bss: 0x7f0
+  __DATA.__bss: 0x7e8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4357964E-C408-38E6-B7D3-C9F64457E0D6
-  Functions: 8792
-  Symbols:   30014
-  CStrings:  15044
+  UUID: 54E0DF18-6A23-3DCB-BA8D-A9DFDE909225
+  Functions: 8766
+  Symbols:   29921
+  CStrings:  15033
 
Symbols:
+ +[WBSAutoFillInternalFeedbackController isRegressionOptionText]
+ +[WBSAutoFillInternalFeedbackController knownWorkingBuildPlaceholderText]
+ -[NSString(SafariSharedExtras) safari_stringByRedactingStrings:withReplacement:]
+ -[WBSAutoFillInternalFeedbackController isRegression]
+ -[WBSAutoFillInternalFeedbackController knownWorkingBuild]
+ -[WBSAutoFillInternalFeedbackController setKnownWorkingBuild:]
+ -[WBSAutoFillInternalFeedbackController setRegression:]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData sensitiveValuesForRedaction]
+ -[WBSAutoFillInternalFeedbackDiagnosticsData setSensitiveValuesForRedaction:]
+ -[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:withKnownSensitiveValues:]
+ -[WBSQuickWebsiteSearchProvider debugDescription]
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._knownWorkingBuild
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackController._regression
+ _OBJC_IVAR_$_WBSAutoFillInternalFeedbackDiagnosticsData._sensitiveValuesForRedaction
+ ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke.55
+ ___80-[NSString(SafariSharedExtras) safari_stringByRedactingStrings:withReplacement:]_block_invoke
+ ___93-[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:withKnownSensitiveValues:]_block_invoke
+ ___block_descriptor_40_e8_32s_e46_"NSMutableDictionary"16?0"WBSFormMetadata"8ls32l8
+ ___block_descriptor_48_ea8_32s40s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8
+ ___block_literal_global.498
+ _objc_msgSend$addIndexesInRange:
+ _objc_msgSend$dictionaryRepresentationRedactingSensitiveValues:withKnownSensitiveValues:
+ _objc_msgSend$enumerateRangesWithOptions:usingBlock:
+ _objc_msgSend$indexSet
+ _objc_msgSend$safari_stringByRedactingStrings:withReplacement:
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration]
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration].cold.1
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration].cold.2
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration].cold.3
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration].cold.4
- -[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration].cold.5
- -[WBSEncryptedCloudKeyValueStore _dsidForPrimaryAccount]
- -[WBSEncryptedCloudKeyValueStore _objectForKey:ofClass:]
- -[WBSEncryptedCloudKeyValueStore _objectForKey:ofClass:].cold.1
- -[WBSEncryptedCloudKeyValueStore _objectForKey:ofClass:].cold.2
- -[WBSEncryptedCloudKeyValueStore _objectForKey:ofClass:].cold.3
- -[WBSEncryptedCloudKeyValueStore _pcsIdentitySet]
- -[WBSEncryptedCloudKeyValueStore _pcsShareProtection]
- -[WBSEncryptedCloudKeyValueStore _setObject:forKey:]
- -[WBSEncryptedCloudKeyValueStore _setObject:forKey:].cold.1
- -[WBSEncryptedCloudKeyValueStore _setObject:forKey:].cold.2
- -[WBSEncryptedCloudKeyValueStore _setPCSIdentitySet:]
- -[WBSEncryptedCloudKeyValueStore _setPCSShareProtection:]
- -[WBSEncryptedCloudKeyValueStore dealloc]
- -[WBSEncryptedCloudKeyValueStore decryptEntry:]
- -[WBSEncryptedCloudKeyValueStore decryptEntry:].cold.1
- -[WBSEncryptedCloudKeyValueStore decryptEntry:].cold.2
- -[WBSEncryptedCloudKeyValueStore decryptEntry:].cold.3
- -[WBSEncryptedCloudKeyValueStore decryptEntry:].cold.4
- -[WBSEncryptedCloudKeyValueStore encryptPropertyList:]
- -[WBSEncryptedCloudKeyValueStore encryptPropertyList:].cold.1
- -[WBSEncryptedCloudKeyValueStore encryptPropertyList:].cold.2
- -[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:]
- _ACAccountStoreDidChangeNotification
- _ACAccountTypeIdentifierAppleAccount
- _CFRetain
- _OBJC_IVAR_$_WBSEncryptedCloudKeyValueStore._accountUpdateObserver
- _OBJC_IVAR_$_WBSEncryptedCloudKeyValueStore._dsid
- _OBJC_IVAR_$_WBSEncryptedCloudKeyValueStore._pcsIdentitySet
- _OBJC_IVAR_$_WBSEncryptedCloudKeyValueStore._pcsShareProtection
- _OBJC_IVAR_$_WBSEncryptedCloudKeyValueStore._serializedPCSObject
- _PCSFPAddPublicIdentity
- _PCSFPCopyDecryptedData
- _PCSFPCopyEncryptedData
- _PCSFPCopyExported
- _PCSFPShouldRoll
- _PCSIdentitySetCopyCurrentPublicIdentityWithError
- _PCSIdentitySetCreate
- _PCSIdentitySetIsICDP
- _PCSObjectCreateFromExportedWithIdentities
- _PCSShareProtectionCreate
- __ZL16isEncryptedEntryP11objc_object
- __ZZ56-[WBSEncryptedCloudKeyValueStore _dsidForPrimaryAccount]E19accountObserverOnce
- ___47-[WBSEncryptedCloudKeyValueStore decryptEntry:]_block_invoke
- ___56-[WBSEncryptedCloudKeyValueStore _dsidForPrimaryAccount]_block_invoke
- ___56-[WBSEncryptedCloudKeyValueStore _dsidForPrimaryAccount]_block_invoke_2
- ___58-[WBSEncryptedCloudKeyValueStore _currentPCSConfiguration]_block_invoke
- ___58-[WBSEncryptedCloudKeyValueStore dictionaryRepresentation]_block_invoke
- ___68-[WBSFormMetadata dictionaryRepresentationRedactingSensitiveValues:]_block_invoke
- ___72+[WBSFrequentlyVisitedSitesController newRadarProblemURLForHistoryItem:]_block_invoke.52
- ___block_descriptor_32_e46_"NSMutableDictionary"16?0"WBSFormMetadata"8l
- ___block_descriptor_40_ea8_32s_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_52_ea8_32s40s_e15_v32?0816^B24ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
- ___block_literal_global.492
- _kPCSServiceLiverpool
- _kPCSSetupDSID
- _objc_msgSend$_currentPCSConfiguration
- _objc_msgSend$_dsidForPrimaryAccount
- _objc_msgSend$_objectForKey:ofClass:
- _objc_msgSend$_setObject:forKey:
- _objc_msgSend$_setPCSIdentitySet:
- _objc_msgSend$_setPCSShareProtection:
- _objc_msgSend$accountProperties
- _objc_msgSend$accountTypeWithAccountTypeIdentifier:
- _objc_msgSend$accountsWithAccountType:
- _objc_msgSend$decryptEntry:
- _objc_msgSend$encryptPropertyList:
- _objc_msgSend$setDictionary:forKey:
- _objc_msgSend$synchronize
- _objc_msgSend$synchronizeWithCompletionHandler:
CStrings:
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__hash_table"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/deque"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/string_view"
+ "/AppleInternal/Library/BuildRoots/0c8284c3-07b0-11ef-bffa-fa87d3da4027/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.5.Internal.sdk/usr/include/c++/v1/vector"
+ "1804822"
+ "<%@: %p; display name = %@>"
+ "<redacted>"
+ "@28@0:8B16@20"
+ "AutoFill previously worked on this page"
+ "Last working build (if known)"
+ "Marked as regression by filer as last working in %@."
+ "Marked as regression by filer with no last known working version."
+ "REGRESSION "
+ "REGRESSION(last worked in %@) "
+ "Safari AutoFill [in-app feedback]: %@%@ on %@ (%@)"
+ "T@\"NSSet\",C,N,V_sensitiveValuesForRedaction"
+ "T@\"NSString\",C,N,V_knownWorkingBuild"
+ "TB,N,GisRegression,V_regression"
+ "The URL (%@) will be included in the report. When selected, the contents of the page can contain sensitive information. Page contents are sanitized to remove values the page currently has in form fields, but the Radar attachments may still contain other or similar sensitive information. On pages with any sensitive information provided by you or the page you should review the draft and its attachments in Tap-to-Radar before filing."
+ "_knownWorkingBuild"
+ "_regression"
+ "_sensitiveValuesForRedaction"
+ "addIndexesInRange:"
+ "address-level1"
+ "address-level2"
+ "dictionaryRepresentationRedactingSensitiveValues:withKnownSensitiveValues:"
+ "enumerateRangesWithOptions:usingBlock:"
+ "indexSet"
+ "isRegression"
+ "isRegressionOptionText"
+ "knownWorkingBuild"
+ "knownWorkingBuildPlaceholderText"
+ "percentageOfFieldsAutoFilledThenClearedOverFieldsEverAutoFilled"
+ "percentageOfFieldsAutofilledThenModifiedOverFieldsEverAutoFilled"
+ "regression"
+ "safari_stringByRedactingStrings:withReplacement:"
+ "sensitiveValuesForRedaction"
+ "setKnownWorkingBuild:"
+ "setRegression:"
+ "setSensitiveValuesForRedaction:"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__hash_table"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/__utility/exception_guard.h"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/deque"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/string_view"
- "/AppleInternal/Library/BuildRoots/bf02bd17-e2a8-11ee-bddc-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/include/c++/v1/vector"
- "@32@0:8@16#24"
- "Data was not an instance of %{public}@"
- "Decryption failed: wrapped key was present, but no data."
- "Encrypted data found when not expecting it"
- "Encrypted storage failed"
- "Exception from ACAccountStore: [%{public}@] [%{private}@] [%{private}@]"
- "Failed to create PCS identity set"
- "Failed to create PCS identity set: %{public}@"
- "Failed to encrypt data"
- "Failed to get public identity from valid identity set: %{public}@"
- "Invalid type for encrypted data"
- "Safari AutoFill [in-app feedback]: %@ on %@ (%@)"
- "T^{_OpaquePCSShareProtection=},N,G_pcsShareProtection,S_setPCSShareProtection:,V_pcsShareProtection"
- "T^{_PCSIdentitySetData=},N,G_pcsIdentitySet,S_setPCSIdentitySet:,V_pcsIdentitySet"
- "The URL (%@) will be included in the report. When selected, the contents of the page may contain sensitive information like your username, but does not include information filled into form fields by you or Safari."
- "Unable to decrypt data: %{public}@"
- "Unable to encrypt KVS data: %{public}@"
- "Unable to recover wrapped key: %{public}@"
- "Unable to serialize data for encryption: %{public}@"
- "Unable to serialize the wrapped PCS object: %{public}@"
- "Unabled to create share protection: %{public}@"
- "WBSDebugForcePCSKeyValueStoragePreferenceKey"
- "^{_OpaquePCSShareProtection=}"
- "^{_OpaquePCSShareProtection=}16@0:8"
- "^{_PCSIdentitySetData=}"
- "^{_PCSIdentitySetData=}16@0:8"
- "_accountUpdateObserver"
- "_currentPCSConfiguration"
- "_dsid"
- "_dsidForPrimaryAccount"
- "_objectForKey:ofClass:"
- "_pcsIdentitySet"
- "_pcsShareProtection"
- "_serializedPCSObject"
- "_setObject:forKey:"
- "_setPCSIdentitySet:"
- "_setPCSShareProtection:"
- "accountProperties"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "com.apple.Safari.EncryptedKVS.PCSEncryptedData"
- "com.apple.Safari.EncryptedKVS.PCSObject"
- "decryptEntry:"
- "encryptPropertyList:"
- "pcsIdentitySet"
- "pcsShareProtection"
- "percentageOfFieldsAutoFilledThenCleared"
- "percentageOfFieldsAutofilledThenModified"
- "personID"
- "primaryAccount"
- "v24@0:8^{_OpaquePCSShareProtection=}16"
- "v24@0:8^{_PCSIdentitySetData=}16"
- "v32@?0@8@16^B24"

```
