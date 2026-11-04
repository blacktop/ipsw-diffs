## backboardd

> `/usr/libexec/backboardd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-877.2.2.0.0
-  __TEXT.__text: 0x585a4
-  __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_stubs: 0x9fc0
-  __TEXT.__objc_methlist: 0x4b24
+877.3.5.0.0
+  __TEXT.__text: 0x59288
+  __TEXT.__auth_stubs: 0x1580
+  __TEXT.__objc_stubs: 0xa020
+  __TEXT.__objc_methlist: 0x4b44
   __TEXT.__const: 0x320
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__gcc_except_tab: 0x770
-  __TEXT.__objc_methname: 0xdc67
+  __TEXT.__gcc_except_tab: 0x760
+  __TEXT.__objc_methname: 0xdd39
   __TEXT.__objc_classname: 0x13fd
-  __TEXT.__cstring: 0x4d19
-  __TEXT.__objc_methtype: 0x2ee4
-  __TEXT.__oslogstring: 0x72cb
-  __TEXT.__unwind_info: 0x1ba0
-  __DATA_CONST.__const: 0x3348
+  __TEXT.__cstring: 0x4d3e
+  __TEXT.__objc_methtype: 0x2ec3
+  __TEXT.__oslogstring: 0x738d
+  __TEXT.__unwind_info: 0x1bd0
+  __DATA_CONST.__const: 0x3398
   __DATA_CONST.__cfstring: 0x5080
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_protolist: 0x248

   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__objc_intobj: 0x1f8
+  __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xac8
-  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__auth_got: 0xad0
+  __DATA_CONST.__got: 0x8a0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xb0f8
-  __DATA.__objc_selrefs: 0x3118
-  __DATA.__objc_ivar: 0x800
+  __DATA.__objc_const: 0xb1a0
+  __DATA.__objc_selrefs: 0x3128
+  __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x2080
   __DATA.__data: 0x1be8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 1929
-  Symbols:   620
-  CStrings:  4111
+  Functions: 1940
+  Symbols:   621
+  CStrings:  4122
 
Symbols:
+ _NSStringFromBKSHIDUISensorDisplayState
CStrings:
+ "%{public}@ blanked: %{BOOL}u (UI sensor display state: %{public}@)"
+ "%{public}@: ignoring display state %{public}@ from non-shell mode: %{public}@"
+ "@16@?0@\"BKHIDUISensorController\"8"
+ "_blankedLock"
+ "_blankedLock_litDisplayUUIDKeys"
+ "_capsLockStateExpirationInterval"
+ "_lock_allKeyboardsBySenderID"
+ "_lock_countOfKeyboardsRequiringAllSmartCoverHESDisengagedForOpen"
+ "_lock_downModifierKeys"
+ "_lock_eventRecognizers"
+ "_lock_expireCapsLockStateForProductIdentifier:generation:"
+ "_lock_globalActiveModifiers"
+ "_lock_keyCommandsToAuthenticate"
+ "_lock_keyDownToEventSequence"
+ "_lock_keyboardGeneration"
+ "_lock_keyboardLayout"
+ "_lock_keyboardObserverAssertion"
+ "_lock_primaryKeyboardInfo"
+ "_lock_productIdentifierWithCapsLockActiveToGeneration"
+ "_lock_senderIDToKeysDown"
+ "_lock_senderIDsWithModifiersOnly"
+ "_lock_usableKeyboards"
+ "_sensorDisplayUUIDKeys"
+ "_sensorObservations"
+ "allDisplaysAreBlanked"
+ "expiring caps lock state for keyboard %{public}@"
+ "setDisplayState:"
- "_allKeyboardsBySenderID"
- "_countOfKeyboardsRequiringAllSmartCoverHESDisengagedForOpen"
- "_downModifierKeys"
- "_eventRecognizers"
- "_globalActiveModifiers"
- "_keyCommandsToAuthenticate"
- "_keyDownToEventSequence"
- "_keyboardGeneration"
- "_keyboardObserverAssertion"
- "_primaryKeyboardInfo"
- "_probeCoverSensorsFromContext:deviceUsagePage:deviceUsage:available:engaged:attached:unknownState:"
- "_productIdentifierWithCapsLockActiveToGeneration"
- "_senderIDToKeysDown"
- "_senderIDsWithModifiersOnly"
- "_usableKeyboards"
- "v64@0:8@16I24I28^Q32^Q40^B48^B56"
```
