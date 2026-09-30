## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

-537.4.20.1.0
-  __TEXT.__text: 0x26dfd8
+537.5.2.0.0
+  __TEXT.__text: 0x26fb24
   __TEXT.__auth_stubs: 0x2860
-  __TEXT.__objc_stubs: 0x10840
-  __TEXT.__objc_methlist: 0x99c0
+  __TEXT.__objc_stubs: 0x109e0
+  __TEXT.__objc_methlist: 0x9a60
   __TEXT.__const: 0x3b80
-  __TEXT.__cstring: 0xd92c
-  __TEXT.__oslogstring: 0x1ae2b
+  __TEXT.__cstring: 0xda0c
+  __TEXT.__oslogstring: 0x1b2db
   __TEXT.__gcc_except_tab: 0x21b8
-  __TEXT.__objc_methname: 0x1aa08
+  __TEXT.__objc_methname: 0x1abf8
   __TEXT.__objc_classname: 0x1f22
   __TEXT.__objc_methtype: 0x510f
   __TEXT.__constg_swiftt: 0x2b8c

   __TEXT.__swift_as_ret: 0x3d8
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__unwind_info: 0x69e0
+  __TEXT.__unwind_info: 0x6a08
   __TEXT.__eh_frame: 0xef70
   __DATA_CONST.__auth_got: 0x1440
-  __DATA_CONST.__got: 0x1338
-  __DATA_CONST.__auth_ptr: 0x718
-  __DATA_CONST.__const: 0xea50
-  __DATA_CONST.__cfstring: 0x4ae0
+  __DATA_CONST.__got: 0x1358
+  __DATA_CONST.__auth_ptr: 0x758
+  __DATA_CONST.__const: 0xea78
+  __DATA_CONST.__cfstring: 0x4b20
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x528

   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x1ccc0
-  __DATA.__objc_selrefs: 0x5350
+  __DATA.__objc_const: 0x1cd78
+  __DATA.__objc_selrefs: 0x53c0
   __DATA.__objc_ivar: 0x7e8
   __DATA.__objc_data: 0x4340
   __DATA.__data: 0x85a8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7964
-  Symbols:   1390
-  CStrings:  7750
+  Functions: 7985
+  Symbols:   1394
+  CStrings:  7789
 
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
