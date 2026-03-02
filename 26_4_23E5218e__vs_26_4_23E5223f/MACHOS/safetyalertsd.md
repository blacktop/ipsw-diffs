## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-67.0.1.0.0
-  __TEXT.__text: 0xfc9b8
+67.0.4.0.0
+  __TEXT.__text: 0xfb878
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x3160
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb04
-  __TEXT.__const: 0x9411
-  __TEXT.__gcc_except_tab: 0xf5b8
-  __TEXT.__cstring: 0x7e4c
-  __TEXT.__oslogstring: 0x3fa2e
+  __TEXT.__const: 0x9419
+  __TEXT.__gcc_except_tab: 0xf308
+  __TEXT.__cstring: 0x7ec0
+  __TEXT.__oslogstring: 0x3f1d8
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x3a6f
   __TEXT.__objc_methtype: 0x1b29
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4368
+  __TEXT.__unwind_info: 0x4338
   __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x85c8
-  __DATA_CONST.__cfstring: 0x6300
+  __DATA_CONST.__const: 0x85b8
+  __DATA_CONST.__cfstring: 0x6380
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D577EF00-8071-3A20-AE50-10CF0E08A996
-  Functions: 3503
+  UUID: 50A61FD6-201C-3A5C-AB07-808AE7651BBF
+  Functions: 3502
   Symbols:   452
-  CStrings:  5578
+  CStrings:  5585
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJl1ugATEavxPGChKPDfz47ZAy8Ll-OXuFFzjvE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "UserChangedAlwaysPlaySoundSwitch"
+ "UserChangedEarthquakeAlertsSwitch"
+ "UserChangedImprovedAlertDeliverySwitch"
+ "UserChangedOtherAlertsSwitch"
+ "doneWithEdMigration"
+ "{\"msg%{public}.0s\":\"#asset,MAqueryResult,highest version in catalog is nil\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersion\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInCatalog\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,assetInList\", \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,finalChoice\", \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,invalid content\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,invalid state\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,invalid version\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,preferThisAsset,assetWithLatestVersion is Nil\"}"
+ "{\"msg%{public}.0s\":\"#asset,getHighestVersionInternal,preferThisAsset,versionIsBetter\"}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable\", \"assetContentsData\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable\", \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable,empty asset\"}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable,invalid content\"}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable,url\", \"folder\":%{public, location:escape_only}@, \"url\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetFileReadable,valid\"}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetStateValid\", \"state\":%{public, location:escape_only}s, \"isStateValid\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#asset,isAssetStateValid,empty asset\"}"
+ "{\"msg%{public}.0s\":\"#asset,process_onAssetReceived,download competed\"}"
+ "{\"msg%{public}.0s\":\"#asset,process_onAssetReceived,download failed\"}"
+ "{\"msg%{public}.0s\":\"#asset,startDownloadResponse\", \"downloadResult\":%{public, location:escape_only}s, \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}@, \"isDownloadSuccessful\":%{public}hhd, \"isAssetReadable\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,already migrated\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,done\", \"wasEnhancedDeliveryPortingCompleted\":%{public}hhd, \"wasEdOn\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,first time\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,missed the buggy build,legacy ed enabled\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,missed the buggy ota,legacy ed enabled\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,handleEnhancedDeliverySwitchMigration,user has changed settings\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,hasUserChangedAlwaysPlaySoundSwitch\", \"userChanged\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,hasUserChangedEarthquakeAlertsSwitch\", \"userChanged\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,hasUserChangedImprovedAlertDeliverySwitch\", \"userChanged\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,hasUserChangedOtherAlertsSwitch\", \"userChanged\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isAboutPrivacySwitchVisible\", \"privacySwitchVisible MA\":%{public}hhd, \"privacySwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,setUserChangedAlwaysPlaySoundSwitch\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,setUserChangedEarthquakeAlertsSwitch\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,setUserChangedImprovedAlertDeliverySwitch\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,setUserChangedOtherAlertsSwitch\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateESASettings\", \"improvedAlertDeliveryStateOnDisk\":%{private}hhd, \"alwaysPlaySoundStateOnDisk\":%{private}hhd, \"otherAlertsStateOnDisk\":%{private}hhd, \"earthquakeAlertsStateOnDisk\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateESASettings\"}"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI8BugBzImOJacExWjk57V1EUdoJN2Rgw22P0d8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "isSafetyAlertsSwitchStateUpdatedFromMA"
- "{\"msg%{public}.0s\":\"#asset,getHighestVersion,assetInList\", \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#asset,getHighestVersion,finalChoice\", \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#asset,getHighestVersion,preferThisAsset,assetWithLatestVersion is Nil\"}"
- "{\"msg%{public}.0s\":\"#asset,getHighestVersion,preferThisAsset,versionIsBetter\"}"
- "{\"msg%{public}.0s\":\"#asset,startDownloadResponse\", \"downloadResult\":%{public, location:escape_only}s, \"var\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}s, \"state\":%{public, location:escape_only}s, \"version\":%{public}d, \"url\":%{public, location:escape_only}s, \"asset\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getAboutPrivacyLink\", \"aboutPrivacyLink MA\":%{public, location:escape_only}s, \"aboutPrivacyLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getAlwaysPlayMADefaultValue\", \"alwaysPlaySwitchState\":%{public}hhd, \"alwayPlaySoundSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getEarthquakeLearnMoreLink\", \"earthquakeLearnMoreLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getEarthquakeMADefaultValue\", \"earthquakeSwitchState MA\":%{public}hhd, \"earthquakeSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getImprovedAlertMADefaultValue\", \"improvedAlertSwitchState MA\":%{public}hhd, \"iadSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getOtherAlertsLearnMoreLink\", \"otherAlertsLearnMoreLink MA\":%{public, location:escape_only}s, \"OtherAlertLearnLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getOtherAlertsMADefaultValue\", \"OtherAlertsSwitchState MA\":%{public}hhd, \"OtherAlertsSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk empty dictionary\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk subDictionary or state invalid\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"AlwayPlaySound\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"EQ\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"ImprovedAlert\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"OtherAlerts\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"aboutPrivacy\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"emptyScreen\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"key\":%{public, location:escape_only}@, \"value\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"mainSwitch\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,isAboutPrivacySwitchVisible\", \"privacySwitchVisible\":%{public}hhd, \"privacySwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived,first run, copy old settings\", \"edState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived,first run, copy old settings\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast main switch is disabled\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"earthquakeAlertsState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"fIsAlwaysPlaySoundSwitchState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"fIsImprovedAlertDeliverySwitchState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"otherAlertsState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref test\", \"userSettings.mainSwitchVisible\":%{public}hhd, \"userSettings.earthquakeSwitchVisible\":%{public}hhd, \"userSettings.earthquakeSwitchState\":%{public}hhd, \"userSettings.otherAlertsSwitchVisible\":%{public}hhd, \"userSettings.otherAlertsSwitchState\":%{public}hhd, \"userSettings.improvedAlertSwitchVisible\":%{public}hhd, \"userSettings.improvedAlertSwitchState\":%{public}hhd, \"userSettings.alwaysPlaySwitchVisible\":%{public}hhd, \"userSettings.alwaysPlaySwitchState\":%{public}hhd, \"userSettings.emptyScreenSwitchVisible\":%{public}hhd, \"userSettings.aboutPrivacySwitchVisible\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution test\", \"userSettings.mainSwitchVisible\":%{public}hhd, \"userSettings.earthquakeSwitchVisible\":%{public}hhd, \"userSettings.earthquakeSwitchState\":%{public}hhd, \"userSettings.otherAlertsSwitchVisible\":%{public}hhd, \"userSettings.otherAlertsSwitchState\":%{public}hhd, \"userSettings.improvedAlertSwitchVisible\":%{public}hhd, \"userSettings.improvedAlertSwitchState\":%{public}hhd, \"userSettings.alwaysPlaySwitchVisible\":%{public}hhd, \"userSettings.alwaysPlaySwitchState\":%{public}hhd, \"userSettings.emptyScreenSwitchVisible\":%{public}hhd, \"userSettings.aboutPrivacySwitchVisible\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"alwaysPlaySoundState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"earthquakeAlertsState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"improvedAlertDeliveryState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"otherAlertsState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue\", \"mobileAssetSettingsConfig\":%{private, location:escape_only}@, \"isInSupportedCountry\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue,first SA init\"}"

```
