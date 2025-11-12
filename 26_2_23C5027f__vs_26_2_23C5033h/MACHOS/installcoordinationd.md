## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-784.60.4.0.0
-  __TEXT.__text: 0xa74a4
+784.60.4.502.5
+  __TEXT.__text: 0xa8b04
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_stubs: 0xaee0
-  __TEXT.__objc_methlist: 0x5d74
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x18f5c
-  __TEXT.__objc_methname: 0x10e8a
-  __TEXT.__objc_classname: 0xa1d
-  __TEXT.__objc_methtype: 0x23e4
-  __TEXT.__oslogstring: 0xe02b
-  __TEXT.__gcc_except_tab: 0x32fc
-  __TEXT.__ustring: 0x1a68
+  __TEXT.__objc_stubs: 0xb0a0
+  __TEXT.__objc_methlist: 0x5e04
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x194ee
+  __TEXT.__objc_methname: 0x11020
+  __TEXT.__objc_classname: 0xa38
+  __TEXT.__objc_methtype: 0x242b
+  __TEXT.__oslogstring: 0xe3f2
+  __TEXT.__gcc_except_tab: 0x3314
+  __TEXT.__ustring: 0x1b68
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x26d0
+  __TEXT.__unwind_info: 0x2710
   __DATA_CONST.__auth_got: 0x8c0
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d40
-  __DATA_CONST.__cfstring: 0x9dc0
-  __DATA_CONST.__objc_classlist: 0x250
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x2d48
+  __DATA_CONST.__cfstring: 0xb5e0
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__objc_intobj: 0x198
+  __DATA_CONST.__objc_arraydata: 0x4210
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc4c0
-  __DATA.__objc_selrefs: 0x33a8
+  __DATA_CONST.__objc_dictobj: 0x6dd8
+  __DATA.__objc_const: 0xc578
+  __DATA.__objc_selrefs: 0x3418
   __DATA.__objc_ivar: 0x4a4
-  __DATA.__objc_data: 0x1720
+  __DATA.__objc_data: 0x1770
   __DATA.__data: 0x6b0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x270

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D312E76-C93C-34C9-8B76-FC10C2A5BF04
-  Functions: 3360
-  Symbols:   432
-  CStrings:  6838
+  UUID: 67418C00-C9BF-32AE-9B15-705EA40A3A6A
+  Functions: 3383
+  Symbols:   434
+  CStrings:  7261
 
Symbols:
+ _OBJC_CLASS_$_RDEstimate
+ _kRegulatoryDomainUpdateNotification
CStrings:
+ "%@-%@"
+ "%s: Bundle %@ has no metadata for region %@"
+ "%s: Cannot save nil region"
+ "%s: Failed to construct MIStoreMetadata from metadata dictionary %@ for %@"
+ "%s: Failed to deserialize previous region plist from %@: %@"
+ "%s: Failed to get current region metadata for %@ due to nil region code"
+ "%s: Failed to save current region %@ to disk"
+ "%s: Failed to update iTunes Metadata for %@: %@"
+ "%s: Failed to update the iTunesMetadata for %@ because coordinators already existed: %@"
+ "%s: Failed to write previous region to %@: %@"
+ "%s: Last known estimates for current regions not found"
+ "%s: No metadata exists for bundleID: %@"
+ "%s: Previous region value is not a string"
+ "%s: Skipping updating iTunesMetadata for SAD apps because the region has not changed from %@"
+ "%s: Skipping updating iTunesMetadata for SAD apps due to failure in fetching the current region"
+ "%s: Successfully saved previous region '%@' to %@"
+ "%s: Updating iTunesMetadata for SAD apps because the region has changed from %@ to %@"
+ "(none)"
+ "+[IXSSADStoreMetadataManager _currentRegionCode]"
+ "+[IXSSADStoreMetadataManager _currentRegionMetadataForBundleID:currentRegion:]"
+ "+[IXSSADStoreMetadataManager currentRegionMetadataForBundleID:]"
+ "+[IXSSADStoreMetadataManager readPreviousRegion]"
+ "+[IXSSADStoreMetadataManager savePreviousRegion:]"
+ "+[IXSSADStoreMetadataManager updateMetadata]"
+ "+[IXSSADStoreMetadataManager updateMetadata]_block_invoke"
+ "14:01:48"
+ "AE"
+ "AF"
+ "AG"
+ "AI"
+ "AL"
+ "AM"
+ "AO"
+ "AR"
+ "AT"
+ "AU"
+ "AZ"
+ "At least one side button app is required on iPhone."
+ "BA"
+ "BB"
+ "BE"
+ "BF"
+ "BG"
+ "BH"
+ "BJ"
+ "BM"
+ "BN"
+ "BO"
+ "BR"
+ "BS"
+ "BT"
+ "BW"
+ "BY"
+ "BZ"
+ "CA"
+ "CD"
+ "CG"
+ "CH"
+ "CI"
+ "CL"
+ "CM"
+ "CN"
+ "CO"
+ "CR"
+ "CV"
+ "CY"
+ "CZ"
+ "DE"
+ "DEFAULT_APP_DOWNLOAD_SIDE_BUTTON_APP_BODY_SECOND"
+ "DEFAULT_APP_DOWNLOAD_SIDE_BUTTON_APP_UI_ALERT_BODY_FIRST"
+ "DEFAULT_APP_SELECT_SIDE_BUTTON_APP_BODY"
+ "DEFAULT_APP_SIDE_BUTTON_NOT_AVAILABLE_DELETE_APP_UI_ALERT_TITLE"
+ "DEFAULT_APP_SIDE_BUTTON_SELECT_DELETE_APP_UI_ALERT_TITLE"
+ "DK"
+ "DM"
+ "DO"
+ "DZ"
+ "EC"
+ "EE"
+ "EG"
+ "ES"
+ "FI"
+ "FJ"
+ "FM"
+ "FR"
+ "GA"
+ "GB"
+ "GD"
+ "GE"
+ "GH"
+ "GM"
+ "GR"
+ "GT"
+ "GW"
+ "GY"
+ "HK"
+ "HN"
+ "HR"
+ "HU"
+ "ID"
+ "IE"
+ "IL"
+ "IN"
+ "IQ"
+ "IS"
+ "IT"
+ "IXSSADStoreMetadataManager"
+ "JM"
+ "JO"
+ "JP"
+ "KE"
+ "KG"
+ "KH"
+ "KN"
+ "KR"
+ "KW"
+ "KY"
+ "KZ"
+ "LA"
+ "LB"
+ "LC"
+ "LK"
+ "LR"
+ "LT"
+ "LU"
+ "LV"
+ "LY"
+ "MA"
+ "MD"
+ "ME"
+ "MG"
+ "MK"
+ "ML"
+ "MM"
+ "MN"
+ "MO"
+ "MR"
+ "MS"
+ "MT"
+ "MU"
+ "MV"
+ "MW"
+ "MX"
+ "MY"
+ "MZ"
+ "NA"
+ "NE"
+ "NG"
+ "NI"
+ "NL"
+ "NO"
+ "NP"
+ "NR"
+ "NZ"
+ "Nov 10 2025"
+ "OM"
+ "PA"
+ "PE"
+ "PG"
+ "PH"
+ "PK"
+ "PL"
+ "PT"
+ "PW"
+ "PY"
+ "PreviousRegion"
+ "PreviousRegion.plist"
+ "QA"
+ "RO"
+ "RS"
+ "RU"
+ "RW"
+ "SA"
+ "SB"
+ "SC"
+ "SE"
+ "SG"
+ "SI"
+ "SK"
+ "SL"
+ "SN"
+ "SR"
+ "ST"
+ "SV"
+ "SZ"
+ "Select Another Default Side Button App"
+ "Side Button App Required"
+ "SideButton"
+ "TC"
+ "TD"
+ "TH"
+ "TJ"
+ "TM"
+ "TN"
+ "TO"
+ "TR"
+ "TT"
+ "TW"
+ "TZ"
+ "UA"
+ "UG"
+ "US"
+ "UY"
+ "UZ"
+ "VC"
+ "VE"
+ "VG"
+ "VN"
+ "VU"
+ "XK"
+ "YE"
+ "ZA"
+ "ZM"
+ "ZW"
+ "_currentRegionCode"
+ "_currentRegionMetadataForBundleID:currentRegion:"
+ "_remote_iTunesMetadataForRemovableSystemAppWithIdentity:completion:"
+ "bundleIDToMetadata"
+ "countryCode"
+ "currentRegionMetadataForBundleID:"
+ "initWithDictionary:"
+ "lastKnownEstimates"
+ "previousRegionFilePath"
+ "rank"
+ "rating"
+ "readPreviousRegion"
+ "regulatoryDomainUpdateDarwinNotification"
+ "savePreviousRegion:"
+ "settings-navigation://com.apple.Settings.SideButton"
+ "sideButtonLocalizedStringForKey:withFormatHint:"
+ "updateMetadata"
+ "v32@0:8@\"IXApplicationIdentity\"16@?<v@?@\"MIStoreMetadata\"@\"NSError\">24"
- "01:53:45"
- "Oct 23 2025"

```
