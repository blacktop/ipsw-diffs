## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/Versions/A/TextInputUI`

```diff

-9127.0.84.0.0
-  __TEXT.__text: 0x31fcc
-  __TEXT.__objc_methlist: 0x1eec
+9127.1.6.0.0
+  __TEXT.__text: 0x323b4
+  __TEXT.__objc_methlist: 0x1f14
   __TEXT.__const: 0xbe8
-  __TEXT.__cstring: 0x1b6f
-  __TEXT.__oslogstring: 0x1f2a
+  __TEXT.__cstring: 0x1c6f
+  __TEXT.__oslogstring: 0x1f7a
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x5e8
-  __TEXT.__constg_swiftt: 0x7ec
+  __TEXT.__constg_swiftt: 0x7f4
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0x3b5
   __TEXT.__swift5_fieldmd: 0x478

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x94
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1078
+  __TEXT.__unwind_info: 0x1088
   __TEXT.__eh_frame: 0xb78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11a0
+  __DATA_CONST.__objc_selrefs: 0x11d8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x520
   __AUTH_CONST.__const: 0xef0
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__cfstring: 0x1300
   __AUTH_CONST.__objc_const: 0x3b80
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x7b0
   __DATA.__common: 0x120
-  __DATA_DIRTY.__objc_data: 0xaf0
+  __DATA_DIRTY.__objc_data: 0xaf8
   __DATA_DIRTY.__data: 0x258
   __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x68

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1236
-  Symbols:   2006
-  CStrings:  360
+  Functions: 1241
+  Symbols:   2015
+  CStrings:  368
 
Symbols:
+ -[_TUIKeyboardCandidateContainer _arrayCountOrNilDebugDescription:]
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_TextInputUI
+ _objc_msgSend$_arrayCountOrNilDebugDescription:
+ _objc_msgSend$autocorrection
+ _objc_msgSend$containsAutofillCandidates
+ _objc_msgSend$emojiList
+ _objc_msgSend$hasOnlyProactiveCandidates
+ _objc_msgSend$isChinaPolicyEnabledForMailReply
CStrings:
+ "%@ {autocorrectionList: %@}"
+ "%@ {candidate resultset: %@}"
+ "%@, predictions: %@, emojis: %@, containsProactiveTriggers: %s, containsAutofillCandidates: %s"
+ "%tu"
+ "(nil)"
+ "Allowing smart reply generation without network access for on-device Mail replies"
+ "autocorrection: %tu, alternate correction: %tu"
+ "candidates: %@, hasOnlyProactiveCandidates: %s"
```
