## MechTouchId

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/Contents/MacOS/MechTouchId`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2319.0.46.0.0
-  __TEXT.__text: 0x491c
+2319.0.63.0.0
+  __TEXT.__text: 0x4b38
   __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x3ac
+  __TEXT.__objc_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x3c4
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__cstring: 0x264
-  __TEXT.__objc_methname: 0x10b2
-  __TEXT.__oslogstring: 0x2c4
+  __TEXT.__objc_methname: 0x1151
+  __TEXT.__oslogstring: 0x302
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methtype: 0x2af
   __TEXT.__unwind_info: 0x188

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__got: 0x220
   __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x5d8
+  __DATA.__objc_selrefs: 0x610
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2a0

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 67
-  Symbols:   102
-  CStrings:  306
+  Functions: 70
+  Symbols:   104
+  CStrings:  314
 
Symbols:
+ _LACEventPushButton
+ _OBJC_CLASS_$_LACACMHelper
CStrings:
+ "%{public}@ failed to query push button credential: %{public}@"
+ "_hasDoublePressPrecondition"
+ "_runWithHints:eventHandler:"
+ "acmContext"
+ "canRecoverFromError:"
+ "error:hasCode:subcode:"
+ "initWithACMContext:"
+ "isCredentialOfTypeSet:error:"
+ "preCompanion"
- "_runWithHints"
```
