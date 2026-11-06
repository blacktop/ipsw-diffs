## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/askpermissiond`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-130.0.29.0.0
-  __TEXT.__text: 0x357dc
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x45e0
-  __TEXT.__objc_methlist: 0x27e8
-  __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x1cf8
+130.1.7.1.1
+  __TEXT.__text: 0x38c2c
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x4a20
+  __TEXT.__objc_methlist: 0x2940
+  __TEXT.__const: 0x2c6
+  __TEXT.__cstring: 0x1ee8
   __TEXT.__objc_classname: 0x4e0
-  __TEXT.__objc_methname: 0x6159
-  __TEXT.__oslogstring: 0x3bc3
-  __TEXT.__objc_methtype: 0x150a
+  __TEXT.__objc_methname: 0x65fe
+  __TEXT.__oslogstring: 0x44c9
+  __TEXT.__objc_methtype: 0x15a8
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__swift5_typeref: 0x134
+  __TEXT.__swift5_typeref: 0x144
   __TEXT.__constg_swiftt: 0x130
   __TEXT.__swift5_reflstr: 0x38
   __TEXT.__swift5_fieldmd: 0x5c
-  __TEXT.__swift5_capture: 0x180
+  __TEXT.__swift5_capture: 0x188
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__info_plist: 0x589
-  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__info_plist: 0x595
+  __TEXT.__unwind_info: 0xaf0
   __TEXT.__eh_frame: 0x398
-  __DATA_CONST.__const: 0x10e0
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__cfstring: 0x2a80
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x53b0
-  __DATA.__objc_selrefs: 0x1640
-  __DATA.__objc_ivar: 0x364
+  __DATA.__objc_const: 0x5590
+  __DATA.__objc_selrefs: 0x1760
+  __DATA.__objc_ivar: 0x388
   __DATA.__objc_data: 0x11b8
   __DATA.__data: 0x460
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x118
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
+  - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 928
-  Symbols:   258
-  CStrings:  1758
+  Functions: 963
+  Symbols:   266
+  CStrings:  1858
 
Symbols:
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _AMSAccountMediaTypeAppStoreSandbox
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_STAppExceptionsManager
+ _OBJC_CLASS_$_STExceptionApp
CStrings:
+ "%{public}@: Checking response for exception approval. Request ID: %{public}@"
+ "%{public}@: Connection interrupted (entitlements)"
+ "%{public}@: Could not fetch FamilyCircle to find a single approver. Error: %{public}@"
+ "%{public}@: Could not look up a single approver to pre-fill. Error: %{public}@"
+ "%{public}@: Could not resolve a single approver with a username to pre-fill. Approver count: %{public}lu"
+ "%{public}@: Error notifying Screen Time of the exception: %{public}@"
+ "%{public}@: Failed to handle Sandbox remote notification. Error: %{public}@"
+ "%{public}@: Family has multiple approvers; not pre-filling. Approver count: %{public}lu"
+ "%{public}@: Fetching FamilyCircle to find a single approver"
+ "%{public}@: Found a single approver to pre-fill"
+ "%{public}@: Getting SANDBOX Store Accounts"
+ "%{public}@: Getting Sandbox user. Action: %{public}ld"
+ "%{public}@: Handled Sandbox remote notification succesfully"
+ "%{public}@: Handling Sandbox request in Pending state"
+ "%{public}@: Handling Sandbox request in Unknown state"
+ "%{public}@: Ignoring pending request."
+ "%{public}@: Missing adamId, can’t submit exception approval."
+ "%{public}@: Missing bundle identifier, can’t submit exception approval."
+ "%{public}@: Missing created date, can’t submit exception approval."
+ "%{public}@: Missing rating value, can’t submit exception approval."
+ "%{public}@: Missing requestID, can’t submit exception approval."
+ "%{public}@: Missing requester DSID, can’t submit exception approval."
+ "%{public}@: Missing server result - %{public}@"
+ "%{public}@: No active Sandbox account"
+ "%{public}@: No sandbox store accounts"
+ "%{public}@: No single approver to pre-fill; prompting for the full Apple ID"
+ "%{public}@: No store OR sandbox accounts - will not progress any further"
+ "%{public}@: Notifying Screen Time of the exception. Bundle ID: %{public}@ | adamID: %llu | distributorID: %{public}@ | ratingValue: %llu | exceptionApp = %{public}@"
+ "%{public}@: Payload missing request DSID - will not progress any further"
+ "%{public}@: Payload request DSID doesn't match any active store or sandbox DSIDs - will not progress any further"
+ "%{public}@: Request is NOT an exception - nothing to submit."
+ "%{public}@: Starting requester remote notification task (Sandbox: %d). Payload: %{public}@"
+ "%{public}@: Successfully notified Screen Time of the exception."
+ "%{public}@: Unable to decode server result - %{public}@"
+ "%{public}@: Unable to send via AskTo - request has no UUID - Checking if we can send via PeopleClient"
+ "01:46:58"
+ "@240@0:8@16@24@32@40@48@56@64@72@80@88B96B100@104@112@120@128@136@144@152@160@168B176@180@188@196q204B212@216@224@232"
+ "@28@0:8^@16B24"
+ "@36@0:8@16B24^@28"
+ "@36@0:8q16B24^@28"
+ "@40@0:8@16@24B32B36"
+ "@76@0:8@16@24@32B40@44@52@60q68"
+ "Could not fetch FamilyCircle"
+ "Family error"
+ "Family has multiple approvers"
+ "Family has no approver with a username to pre-fill"
+ "ISO8601DateFormatter"
+ "No active Sandbox account"
+ "No approver to pre-fill"
+ "No single approver"
+ "Oct  8 2026"
+ "Server Response Error"
+ "T@\"NSNumber\",R,V_requesterDSID"
+ "T@\"NSString\",C"
+ "T@\"NSString\",C,Vusername"
+ "TB,R,V_isSandbox"
+ "TB,V_isSandbox"
+ "UTC"
+ "Unable to decode server result"
+ "VIEW_SERVICE_CONNECTION_LOST_ERROR_BODY"
+ "_activeSandboxStoreDSIDs"
+ "_handleRequesterNotification:withRequesterDSID:andSuppressDialog:"
+ "_handleSandboxNotification:withRequesterDSID:"
+ "_handleSandboxRequest"
+ "_isApprover:"
+ "_isSandbox"
+ "_notifyScreenTimeIfNeededForApprovalForRequestWithID:response:"
+ "_presentErrorAlertWithTitle:body:errorCode:correlationId:responseBody:requesterDSID:"
+ "_requestInfoForIndentifier:isSandbox:withError:"
+ "_serverRequestWithError:isSandbox:"
+ "_serverRequestWithUser:isSandbox:error:"
+ "_singleApproverUsernameWithFamilyRequest:"
+ "addAppException:completionHandler:"
+ "ams_iTunesSandboxAccounts"
+ "approvalRequestWithRequestIdentifier:isSandbox:"
+ "arrayForKey:"
+ "askForExceptionWithUuid:type:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:badgeIconBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
+ "askToBadgeIconBundleIdentifier"
+ "askToBuyWithUuid:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:badgeIconBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
+ "bagForProfile:profileVersion:processInfo:"
+ "bundleURL"
+ "bundleWithIdentifier:"
+ "calendarWithIdentifier:"
+ "com.apple.Music"
+ "com.apple.iBooks"
+ "com.apple.private.applemediaservices"
+ "createdDateISO8601"
+ "dateFormatter"
+ "domain"
+ "initWithDate:requestIdentifier:uniqueIdentifier:isSandbox:itemIdentifier:localizations:offerName:status:"
+ "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:ageRatingValue:approverDSID:requesterDSID:requesterAltDSID:createdDate:modifiedDate:isException:isSandbox:itemBundleID:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:originatedOnThisDevice:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:uuid:"
+ "initWithPayload:requesterDSID:isSandbox:andSuppressDialog:"
+ "initWithRequesterDSID:bundleIdentifier:adamID:distributorID:ratingValue:"
+ "is-sandbox"
+ "isSandbox"
+ "isSandboxRequest"
+ "manage-sandbox-account-url"
+ "manageSandboxAccountURL"
+ "members"
+ "modifiedDateISO8601"
+ "presentDialogWithTitle:body:buttons:showIcon:completion:"
+ "primaryiCloudUserWithAction:isSandbox:keychainError:"
+ "sandboxBag"
+ "setCalendar:"
+ "setFormatOptions:"
+ "setIconBundleURL:"
+ "setIsSandbox:"
+ "setTimeZone:"
+ "singleApproverUsername"
+ "subscription"
+ "timeZoneWithAbbreviation:"
+ "trustedDomains"
+ "unsignedLongLongValue"
+ "v136@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSDate\"80@\"NSString\"88@\"NSString\"96@\"APAskToAgeRestrictionMetadata\"104@\"NSURL\"112@?<v@?B@\"NSError\">120@?<v@?B@\"NSError\">128"
+ "v144@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSDate\"88@\"NSString\"96@\"NSString\"104@\"APAskToAgeRestrictionMetadata\"112@\"NSURL\"120@?<v@?B@\"NSError\">128@?<v@?B@\"NSError\">136"
+ "v36@0:8@16@24B32"
+ "v52@0:8@16@24@32B40@?44"
+ "v64@0:8@16@24q32@40@48@56"
+ "valueForEntitlement:"
+ "yyyy-MM-dd'T'HH:mm:ss.SZZZ"
- "%{public}@: Payload request DSID doesn't match store DSIDs: %@"
- "%{public}@: Starting requester remote notification task. Payload: %{public}@"
- "22:13:13"
- "@\"NSUUID\"16@0:8"
- "@236@0:8@16@24@32@40@48@56@64@72@80@88B96@100@108@116@124@132@140@148@156@164B172@176@184@192q200B208@212@220@228"
- "@72@0:8@16@24@32@40@48@56q64"
- "Aug  8 2026"
- "T@\"NSUUID\",R"
- "YYYY-MM-dd'T'HH:mm:ss.SZZZ"
- "_handleRequesterNotification:andSuppressDialog:"
- "_serverRequestWithUser:error:"
- "askForExceptionWithUuid:type:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
- "askToBuyWithUuid:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
- "initWithDate:requestIdentifier:uniqueIdentifier:itemIdentifier:localizations:offerName:status:"
- "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:ageRatingValue:approverDSID:requesterDSID:requesterAltDSID:createdDate:modifiedDate:isException:itemBundleID:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:originatedOnThisDevice:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:uuid:"
- "initWithPayload:andSuppressDialog:"
- "presentDialogWithTitle:body:buttons:completion:"
- "primaryiCloudUserWithAction:keychainError:"
- "v128@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSDate\"80@\"NSString\"88@\"APAskToAgeRestrictionMetadata\"96@\"NSURL\"104@?<v@?B@\"NSError\">112@?<v@?B@\"NSError\">120"
- "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSDate\"88@\"NSString\"96@\"APAskToAgeRestrictionMetadata\"104@\"NSURL\"112@?<v@?B@\"NSError\">120@?<v@?B@\"NSError\">128"
```
