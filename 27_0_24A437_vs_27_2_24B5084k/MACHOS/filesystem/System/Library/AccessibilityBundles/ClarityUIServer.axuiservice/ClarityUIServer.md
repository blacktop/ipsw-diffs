## ClarityUIServer

> `/System/Library/AccessibilityBundles/ClarityUIServer.axuiservice/ClarityUIServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__objc_stublist`

```diff

-168.2.0.0.0
-  __TEXT.__text: 0xcfc4
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x840
+170.3.0.0.0
+  __TEXT.__text: 0xe6d4
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x314
-  __TEXT.__const: 0x95a
+  __TEXT.__const: 0x96a
   __TEXT.__swift5_typeref: 0x529
   __TEXT.__swift5_capture: 0xe8
   __TEXT.__cstring: 0x3ab
   __TEXT.__objc_methtype: 0x57b
-  __TEXT.__oslogstring: 0x674
+  __TEXT.__oslogstring: 0xdd4
   __TEXT.__constg_swiftt: 0x1d4
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x99

   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x3f8
-  __TEXT.__eh_frame: 0x390
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__auth_got: 0x5f8
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x228
   __DATA.__objc_const: 0x318

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 266
-  Symbols:   180
-  CStrings:  237
+  Functions: 267
+  Symbols:   182
+  CStrings:  255
 
Symbols:
+ _objc_retain_x22
+ _objc_retain_x25
CStrings:
+ "AA: StartFlow - Blocked entering ClarityBoard: SIM PIN not supported."
+ "AA: StartFlow - Blocked entering ClarityBoard: Screen Time device unlock required."
+ "AA: StartFlow - Blocked entering ClarityBoard: alphanumeric passcode not supported."
+ "AA: StartFlow - Blocked entering ClarityBoard: device hasn't been unlocked since boot."
+ "AA: StartFlow - Blocked entering ClarityBoard: not set up."
+ "AA: StartFlow - Calling addContentViewController for blank view controller: %{public}s"
+ "AA: StartFlow - Checking %ld SIMs..."
+ "AA: StartFlow - ClarityUI loading screen frozen; calling setClarityBoardEnabled(true)."
+ "AA: StartFlow - Could not get profile connection"
+ "AA: StartFlow - Dismiss animation of existing presenting view controller completed; removing its content view controller."
+ "AA: StartFlow - Entering ClarityBoard."
+ "AA: StartFlow - Found SIM with PIN."
+ "AA: StartFlow - Found no SIMs."
+ "AA: StartFlow - Loading view presented; waiting to freeze ClarityUI loading screen."
+ "AA: StartFlow - No existing presenting view controller; attempting to present passcode for the first time."
+ "AA: StartFlow - No validation warnings; proceeding to enter ClarityBoard."
+ "AA: StartFlow - Passcode is correct: %{bool}d"
+ "AA: StartFlow - Passcode was already presented (existingPresentingViewController: %{public}s). Dismissing it."
+ "AA: StartFlow - Passcode was dismissed with reason: %ld"
+ "AA: StartFlow - Passcode was hidden."
+ "AA: StartFlow - Passcode was shown."
+ "AA: StartFlow - Presenting AXUIPasscodeViewController with parent: %{public}s"
+ "AA: StartFlow - Presenting passcode."
+ "AA: StartFlow - Received attempt-to-enter-ClarityBoard message from client: %{public}s"
+ "AA: StartFlow - Received restrictions PIN entry notification; success: %{bool}d"
+ "AA: StartFlow - Screen Time restrictions passcode is enabled; activating remote PIN UI."
+ "AA: StartFlow - Tried to show loading screen, but had no presenting view controller."
+ "AA: StartFlow - Unable to enter ClarityUI: %s"
+ "AA: StartFlow - Unable to fetch whether SIM had PIN: %@"
+ "AA: StartFlow - Unable to get info about SIMs: %@"
+ "AA: StartFlow - addContentViewController completion fired; blank view controller is now attached."
+ "AA: StartFlow - setClarityBoardEnabled(true) succeeded."
- "Checking %ld SIMs..."
- "Could not get profile connection"
- "Found SIM with PIN."
- "Found no SIMs."
- "Passcode is correct: %{bool}d"
- "Passcode was already presented. Dismissing it."
- "Passcode was dismissed with reason: %ld"
- "Passcode was hidden."
- "Passcode was shown."
- "Presenting passcode."
- "Tried to show loading screen, but had no presenting view controller."
- "Unable to enter ClarityUI: %s"
- "Unable to fetch whether SIM had PIN: %@"
- "Unable to get info about SIMs: %@"
```
