## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-148.6.0.0.0
-  __TEXT.__text: 0xaaea4
-  __TEXT.__auth_stubs: 0x20d0
-  __TEXT.__objc_methlist: 0xac94
+148.7.0.0.0
+  __TEXT.__text: 0xab554
+  __TEXT.__auth_stubs: 0x20f0
+  __TEXT.__objc_methlist: 0xace4
   __TEXT.__const: 0xe44
   __TEXT.__oslogstring: 0x2bfc
-  __TEXT.__cstring: 0x6d57
+  __TEXT.__cstring: 0x6d87
   __TEXT.__gcc_except_tab: 0x1f70
   __TEXT.__ustring: 0x8a
   __TEXT.__constg_swiftt: 0x2dc

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_fieldmd: 0x134
-  __TEXT.__unwind_info: 0x2f48
+  __TEXT.__unwind_info: 0x2f50
   __TEXT.__eh_frame: 0x1e0
   __TEXT.__objc_classname: 0x1852
-  __TEXT.__objc_methname: 0x1eb7b
+  __TEXT.__objc_methname: 0x1ec6b
   __TEXT.__objc_methtype: 0x3f65
-  __TEXT.__objc_stubs: 0x13f60
+  __TEXT.__objc_stubs: 0x14040
   __DATA_CONST.__got: 0xec8
   __DATA_CONST.__const: 0x1aa0
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7178
+  __DATA_CONST.__objc_selrefs: 0x71b0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x8a8
-  __AUTH_CONST.__auth_got: 0x1078
+  __AUTH_CONST.__auth_got: 0x1088
   __AUTH_CONST.__const: 0x1948
-  __AUTH_CONST.__cfstring: 0x8fe0
+  __AUTH_CONST.__cfstring: 0x9000
   __AUTH_CONST.__objc_const: 0xf198
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 78B7D4A6-4ADC-33CB-A2B1-37B848ACC281
-  Functions: 4284
-  Symbols:   15109
-  CStrings:  8140
+  UUID: 68D63DA7-5B29-3630-8ECB-B0A7C8CAE7D2
+  Functions: 4291
+  Symbols:   15132
+  CStrings:  8149
 
Symbols:
+ +[CACPreferences hashedKeyForCommand:parameter:]
+ -[CACPreferences _migrateLegacyUserHintsHistoryIfNeeded]
+ -[CACPreferences cleanUpLegacyUserHintsHistory]
+ -[CACPreferences setUserHintsHistoryHashed:]
+ -[CACPreferences setUserHintsHistoryLegacy:]
+ -[CACPreferences userHintsHistoryHashed]
+ -[CACPreferences userHintsHistoryLegacy]
+ -[CACUserHintsManager _currentLocaleHintsHistory]
+ -[CACUserHintsManager _currentNormalizedLocale]
+ -[CACUserHintsManager _setCurrentLocaleHintsHistory:]
+ GCC_except_table77
+ GCC_except_table78
+ _CC_SHA256
+ ___block_literal_global.396
+ ___block_literal_global.401
+ ___block_literal_global.472
+ ___block_literal_global.736
+ _objc_msgSend$_currentLocaleHintsHistory
+ _objc_msgSend$_currentNormalizedLocale
+ _objc_msgSend$_migrateLegacyUserHintsHistoryIfNeeded
+ _objc_msgSend$_setCurrentLocaleHintsHistory:
+ _objc_msgSend$cleanUpLegacyUserHintsHistory
+ _objc_msgSend$hashedKeyForCommand:parameter:
+ _objc_msgSend$setUserHintsHistoryHashed:
+ _objc_msgSend$userHintsHistoryHashed
+ _objc_msgSend$userHintsHistoryLegacy
+ _strlen
- -[CACPreferences setUserHintsHistory:]
- -[CACPreferences userHintsHistory]
- -[CACUserHintsManager clearHistory]
- GCC_except_table72
- ___block_literal_global.399
- ___block_literal_global.404
- ___block_literal_global.463
- ___block_literal_global.722
- _objc_msgSend$setUserHintsHistory:
- _objc_msgSend$userHintsHistory
CStrings:
+ "%02x%02x%02x%02x%02x%02x%02x%02x"
+ "CACUserHintsHistoryHashed"
+ "_currentLocaleHintsHistory"
+ "_currentNormalizedLocale"
+ "_migrateLegacyUserHintsHistoryIfNeeded"
+ "_setCurrentLocaleHintsHistory:"
+ "cleanUpLegacyUserHintsHistory"
+ "hashedKeyForCommand:parameter:"
+ "setUserHintsHistoryHashed:"
+ "setUserHintsHistoryLegacy:"
+ "userHintsHistoryHashed"
+ "userHintsHistoryLegacy"
- "_%@"
- "clearHistory"
- "setUserHintsHistory:"
- "userHintsHistory"

```
