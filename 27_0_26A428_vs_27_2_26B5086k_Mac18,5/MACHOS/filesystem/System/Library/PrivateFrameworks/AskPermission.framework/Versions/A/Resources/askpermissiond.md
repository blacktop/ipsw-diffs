## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/askpermissiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
+130.1.4.0.0
+  __TEXT.__text: 0x37308
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x4820
+  __TEXT.__objc_methlist: 0x2878
   __TEXT.__const: 0x2b6
-  __TEXT.__cstring: 0x1cf8
+  __TEXT.__cstring: 0x1df8
   __TEXT.__objc_classname: 0x4e0
-  __TEXT.__objc_methname: 0x6159
-  __TEXT.__oslogstring: 0x3bc3
-  __TEXT.__objc_methtype: 0x150a
+  __TEXT.__objc_methname: 0x63a9
+  __TEXT.__oslogstring: 0x4197
+  __TEXT.__objc_methtype: 0x1548
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
-  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__unwind_info: 0xac8
   __TEXT.__eh_frame: 0x398
-  __DATA_CONST.__const: 0x10e0
-  __DATA_CONST.__cfstring: 0x27c0
+  __DATA_CONST.__const: 0x1100
+  __DATA_CONST.__cfstring: 0x2920
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x53b0
-  __DATA.__objc_selrefs: 0x1640
-  __DATA.__objc_ivar: 0x364
+  __DATA.__objc_const: 0x53c8
+  __DATA.__objc_selrefs: 0x16d0
+  __DATA.__objc_ivar: 0x368
   __DATA.__objc_data: 0x11b8
   __DATA.__data: 0x460
   __DATA.__common: 0x28

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
-  CStrings:  1757
+  Functions: 943
+  Symbols:   264
+  CStrings:  1807
 
Symbols:
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_STAppExceptionsManager
+ _OBJC_CLASS_$_STExceptionApp
CStrings:
+ "%{public}@: Checking response for exception approval. Request ID: %{public}@"
+ "%{public}@: Could not fetch FamilyCircle to find a single approver. Error: %{public}@"
+ "%{public}@: Could not look up a single approver to pre-fill. Error: %{public}@"
+ "%{public}@: Could not resolve a single approver with a username to pre-fill. Approver count: %{public}lu"
+ "%{public}@: Error notifying Screen Time of the exception: %{public}@"
+ "%{public}@: Family has multiple approvers; not pre-filling. Approver count: %{public}lu"
+ "%{public}@: Fetching FamilyCircle to find a single approver"
+ "%{public}@: Found a single approver to pre-fill"
+ "%{public}@: Missing adamId, can’t submit exception approval."
+ "%{public}@: Missing bundle identifier, can’t submit exception approval."
+ "%{public}@: Missing created date, can’t submit exception approval."
+ "%{public}@: Missing rating value, can’t submit exception approval."
+ "%{public}@: Missing requestID, can’t submit exception approval."
+ "%{public}@: Missing requester DSID, can’t submit exception approval."
+ "%{public}@: No single approver to pre-fill; prompting for the full Apple ID"
+ "%{public}@: Notifying Screen Time of the exception. Bundle ID: %{public}@ | adamID: %llu | distributorID: %{public}@ | ratingValue: %llu | exceptionApp = %{public}@"
+ "%{public}@: Request is NOT an exception - nothing to submit."
+ "%{public}@: Successfully notified Screen Time of the exception."
+ "%{public}@: Unable to send via AskTo - request has no UUID - Checking if we can send via PeopleClient"
+ "Could not fetch FamilyCircle"
+ "Family error"
+ "Family has multiple approvers"
+ "Family has no approver with a username to pre-fill"
+ "No approver to pre-fill"
+ "No single approver"
+ "T@\"NSString\",C"
+ "T@\"NSString\",C,Vusername"
+ "UTC"
+ "VIEW_SERVICE_CONNECTION_LOST_ERROR_BODY"
+ "_isApprover:"
+ "_notifyScreenTimeIfNeededForApprovalForRequestWithID:response:"
+ "_presentErrorAlertWithTitle:body:errorCode:correlationId:responseBody:requesterDSID:"
+ "_singleApproverUsernameWithFamilyRequest:"
+ "addAppException:completionHandler:"
+ "askForExceptionWithUuid:type:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:badgeIconBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
+ "askToBadgeIconBundleIdentifier"
+ "askToBuyWithUuid:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:badgeIconBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
+ "bundleURL"
+ "bundleWithIdentifier:"
+ "calendarWithIdentifier:"
+ "com.apple.Music"
+ "com.apple.iBooks"
+ "domain"
+ "initWithRequesterDSID:bundleIdentifier:adamID:distributorID:ratingValue:"
+ "members"
+ "presentDialogWithTitle:body:buttons:showIcon:completion:"
+ "setCalendar:"
+ "setIconBundleURL:"
+ "setTimeZone:"
+ "singleApproverUsername"
+ "subscription"
+ "timeZoneWithAbbreviation:"
+ "unsignedLongLongValue"
+ "v136@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSDate\"80@\"NSString\"88@\"NSString\"96@\"APAskToAgeRestrictionMetadata\"104@\"NSURL\"112@?<v@?B@\"NSError\">120@?<v@?B@\"NSError\">128"
+ "v144@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSDate\"88@\"NSString\"96@\"NSString\"104@\"APAskToAgeRestrictionMetadata\"112@\"NSURL\"120@?<v@?B@\"NSError\">128@?<v@?B@\"NSError\">136"
+ "v52@0:8@16@24@32B40@?44"
+ "v64@0:8@16@24q32@40@48@56"
+ "yyyy-MM-dd'T'HH:mm:ss.SZZZ"
- "@\"NSUUID\"16@0:8"
- "T@\"NSUUID\",R"
- "YYYY-MM-dd'T'HH:mm:ss.SZZZ"
- "askForExceptionWithUuid:type:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
- "askToBuyWithUuid:title:message:bundleIdentifier:preApprove:postApprove:preDecline:postDecline:expirationDate:responseBundleIdentifier:metadata:fallbackURL:delegateCallback:completionHandler:"
- "presentDialogWithTitle:body:buttons:completion:"
- "v128@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSDate\"80@\"NSString\"88@\"APAskToAgeRestrictionMetadata\"96@\"NSURL\"104@?<v@?B@\"NSError\">112@?<v@?B@\"NSError\">120"
- "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSDate\"88@\"NSString\"96@\"APAskToAgeRestrictionMetadata\"104@\"NSURL\"112@?<v@?B@\"NSError\">120@?<v@?B@\"NSError\">128"
```
