## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-537.4.20.1.0
-  __TEXT.__text: 0x251940
+537.5.2.0.0
+  __TEXT.__text: 0x2531fc
   __TEXT.__auth_stubs: 0x2aa0
-  __TEXT.__objc_stubs: 0x10d80
-  __TEXT.__objc_methlist: 0x9af8
+  __TEXT.__objc_stubs: 0x10f20
+  __TEXT.__objc_methlist: 0x9ba8
   __TEXT.__const: 0x3e70
   __TEXT.__gcc_except_tab: 0x2140
-  __TEXT.__cstring: 0xd98c
-  __TEXT.__oslogstring: 0x1b2cb
-  __TEXT.__objc_methname: 0x1b441
+  __TEXT.__cstring: 0xda6c
+  __TEXT.__oslogstring: 0x1b76b
+  __TEXT.__objc_methname: 0x1b631
   __TEXT.__objc_classname: 0x1f9a
   __TEXT.__objc_methtype: 0x5207
   __TEXT.__constg_swiftt: 0x2bbc

   __TEXT.__swift_as_ret: 0x3dc
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__unwind_info: 0x7170
+  __TEXT.__unwind_info: 0x71b0
   __TEXT.__eh_frame: 0xf078
   __DATA_CONST.__auth_got: 0x1560
-  __DATA_CONST.__got: 0x1538
-  __DATA_CONST.__auth_ptr: 0x6f0
-  __DATA_CONST.__const: 0xe770
-  __DATA_CONST.__cfstring: 0x48c0
+  __DATA_CONST.__got: 0x1558
+  __DATA_CONST.__auth_ptr: 0x6e0
+  __DATA_CONST.__const: 0xe7c0
+  __DATA_CONST.__cfstring: 0x4900
   __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x538

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1d270
-  __DATA.__objc_selrefs: 0x5528
+  __DATA.__objc_const: 0x1d328
+  __DATA.__objc_selrefs: 0x5598
   __DATA.__objc_ivar: 0x7fc
   __DATA.__objc_data: 0x43e0
   __DATA.__data: 0x8748

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7878
-  Symbols:   1503
-  CStrings:  7842
+  Functions: 7899
+  Symbols:   1507
+  CStrings:  7881
 
Symbols:
+ _OBJC_CLASS_$_DMFPolicyMonitor
+ _OBJC_CLASS_$_STPasscodeActivityUserNotificationContext
+ _STUserDefaultsKeyIsPasscodeUseNotificationDisabled
+ _STUserDefaultsKeyIsWeeklyReportNotificationDisabled
CStrings:
+ "Blueprint missing id or hash. skipping it. id: %{public}@. hash: %{public}@"
+ "Did not send passcode activity payload"
+ "Failed to create passcode activity payload: %{public}@"
+ "Failed to fetch family members: %{public}@"
+ "Failed to fetch local user-device state to post passcode activity user notification: %{public}@"
+ "Failed to fetch or create user-device state for passcode activity: %{public}@"
+ "Failed to save passcode activity: %{public}@"
+ "Failed to send passcode activity to parents: %{public}@"
+ "Failed to update user-device state for %{private}@"
+ "Finished sending passcode activity payload"
+ "Handling passcode activity payload: %{public}@ from: %{private}@"
+ "Local user has no parents in their iCloud family, not sending passcode activity payload"
+ "Local user is not managed and is not eligible to send passcode activity"
+ "Nothing to save for passcode activity payload from %{private}@"
+ "Passcode use notification is disabled. Not posting user notification for passcode activity from %{private}@"
+ "RMUnifiedTransportPayloadTypePasscodeActivity"
+ "Received passcode activity payload"
+ "Successfully saved passcode activity from %{private}@"
+ "Successfully sent passcode activity to parents"
+ "Updated user-device state for %{private}@"
+ "Weekly report notification is disabled"
+ "_"
+ "_blueprintsForBudgetIdentifiers:fromBlueprints:"
+ "_filterForExpiredBlueprints:error:"
+ "_handlePasscodeActivityPayload:"
+ "_makeBudgetIdentifierFromBlueprints:"
+ "com.apple.ScreenTimeAgent.familyOrganizationController.handlePasscodeActivity"
+ "com.apple.ScreenTimeAgent.familyOrganizationController.sendPasscodeActivity"
+ "componentsSeparatedByString:"
+ "declarationServerHash"
+ "filterForExpiredBudgetIdentifiers:withError:"
+ "handlePasscodePayload:context:"
+ "initWithDeviceName:lastPasscodeUseDate:childDSID:"
+ "lastPasscodeUseDate"
+ "passcodePayloadWithContext:error:"
+ "passcode_activity"
+ "policyMonitor"
+ "sendPasscodeActivityToParentsWithCompletionHandler:"
+ "sendPasscodeActivityToParentsWithReplyHandler:"

```
