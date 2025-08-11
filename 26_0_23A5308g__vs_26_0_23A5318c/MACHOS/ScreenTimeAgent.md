## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-601.0.0.0.0
-  __TEXT.__text: 0x2585f4
-  __TEXT.__auth_stubs: 0x2de0
-  __TEXT.__objc_stubs: 0x11520
-  __TEXT.__objc_methlist: 0x9fd8
-  __TEXT.__const: 0x5bd8
+604.2.0.0.0
+  __TEXT.__text: 0x25a6e4
+  __TEXT.__auth_stubs: 0x2df0
+  __TEXT.__objc_stubs: 0x11500
+  __TEXT.__objc_methlist: 0xa020
+  __TEXT.__const: 0x5c18
   __TEXT.__gcc_except_tab: 0x218c
-  __TEXT.__cstring: 0xe52c
-  __TEXT.__oslogstring: 0x1cadb
-  __TEXT.__objc_methname: 0x1c10e
+  __TEXT.__cstring: 0xe62c
+  __TEXT.__oslogstring: 0x1cc5b
+  __TEXT.__objc_methname: 0x1c263
   __TEXT.__objc_classname: 0x2019
-  __TEXT.__objc_methtype: 0x54fc
-  __TEXT.__constg_swiftt: 0x32d8
-  __TEXT.__swift5_typeref: 0x3090
+  __TEXT.__objc_methtype: 0x5523
+  __TEXT.__constg_swiftt: 0x32e8
+  __TEXT.__swift5_typeref: 0x30d2
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x2454
-  __TEXT.__swift5_fieldmd: 0x178c
-  __TEXT.__swift5_capture: 0x2cd0
+  __TEXT.__swift5_reflstr: 0x2474
+  __TEXT.__swift5_fieldmd: 0x1798
+  __TEXT.__swift5_capture: 0x2d10
   __TEXT.__swift5_assocty: 0x368
   __TEXT.__swift5_proto: 0x31c
   __TEXT.__swift5_types: 0x1bc
-  __TEXT.__swift_as_entry: 0x454
-  __TEXT.__swift_as_ret: 0x438
+  __TEXT.__swift_as_entry: 0x460
+  __TEXT.__swift_as_ret: 0x44c
   __TEXT.__swift5_protos: 0x9c
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x75e8
-  __TEXT.__eh_frame: 0xffe0
-  __DATA_CONST.__auth_got: 0x1700
-  __DATA_CONST.__got: 0x16d0
+  __TEXT.__unwind_info: 0x7680
+  __TEXT.__eh_frame: 0x102a8
+  __DATA_CONST.__auth_got: 0x1708
+  __DATA_CONST.__got: 0x16f0
   __DATA_CONST.__auth_ptr: 0x7a0
-  __DATA_CONST.__const: 0xb440
+  __DATA_CONST.__const: 0xb510
   __DATA_CONST.__cfstring: 0x4ac0
   __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1f048
-  __DATA.__objc_selrefs: 0x5818
+  __DATA.__objc_const: 0x1f070
+  __DATA.__objc_selrefs: 0x5860
   __DATA.__objc_ivar: 0x800
-  __DATA.__objc_data: 0x4a20
-  __DATA.__data: 0x7da8
+  __DATA.__objc_data: 0x4a30
+  __DATA.__data: 0x7db8
   __DATA.__bss: 0x4fb0
   __DATA.__common: 0x130
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1072ACDE-A6EB-3FEF-A988-C5030A59C9BF
-  Functions: 7841
-  Symbols:   1611
-  CStrings:  8719
+  UUID: 5D0AD47F-2FB7-3C5F-AB40-1B55CEC54D44
+  Functions: 7881
+  Symbols:   1616
+  CStrings:  8740
 
Symbols:
+ _$s15ScreenTimeSwift19STUserNotificationsV16NotificationTypeO16appRatingChangedyAESS_SaySSGtcAEmFWC
+ _$sSi10FoundationEySiSo8NSNumberChcfC
+ _OBJC_CLASS_$_STRegionRatings
+ _OBJC_CLASS_$_STRegionRatingsRequestOptions
+ _STRegionRatingsLeastRestrictiveValue
CStrings:
+ "B28@0:8B16B20B24"
+ "InitialManagedSettingsApplied"
+ "Managed Settings have not been applied. Running processBlueprintChanges to trigger ManagedSettingsApplicator."
+ "Should denyHistoryClearing and denyPrivateBrowsing: %{bool,public}d."
+ "User is managed: %{bool,public}d. User has Web Content Filter enabled: %{bool,public}d. User has passcode set: %{bool,public}d."
+ "[notifyUser] Error attempting to fetch local user"
+ "[notifyUser] No closest match for restriction value %@"
+ "[notifyUser] No localized string for restriction value %@"
+ "[notifyUser] Not notifying for restriction value of %@"
+ "_applyManagedSettingsIfNeeded"
+ "applySafariSettingsRestrictions:"
+ "appsRating"
+ "com.apple.STExceptionServer.appRatingChanged"
+ "getClosestRestrictionMatch:within:forPayloadKey:"
+ "initWithUnrated:userDSID:"
+ "loadRegionRatingsWithOptions:completionHandler:"
+ "localizedAppRatingsForRegion:"
+ "notifyUserOfAppRatingChange:completionHandler:"
+ "preferredRegion"
+ "shouldRestrictSafariSettingsWithIsPasscodeSet:isUserManaged:isWebContentFilterEnabled:"
+ "v24@?0@\"STRegionRatings\"8@\"NSError\"16"
+ "v24@?0@\"STRestrictions\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "SafariStore"
- "User is a managed child: %{BOOL}u or User has Web Content Filter enabled: %{BOOL}u and has passcode set: %{BOOL}u. Should enable denyHistoryClearing and denyPrivateBrowsing: %{public}d"
- "processBlueprintChangesInstallOnly:"

```
