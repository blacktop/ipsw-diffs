## LiveSpeechUIService

> `/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_stublist`
- `__DATA.__common`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0xb67b8
-  __TEXT.__auth_stubs: 0x3960
-  __TEXT.__objc_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0xe70
+3240.3.0.0.0
+  __TEXT.__text: 0xb9748
+  __TEXT.__auth_stubs: 0x3980
+  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0xe78
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__const: 0x7178
-  __TEXT.__swift5_typeref: 0x13728
-  __TEXT.__constg_swiftt: 0x2474
-  __TEXT.__cstring: 0x1cc5
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x1cbf
-  __TEXT.__swift5_fieldmd: 0x18a4
+  __TEXT.__swift5_typeref: 0x134cc
+  __TEXT.__constg_swiftt: 0x2480
+  __TEXT.__cstring: 0x1d15
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_reflstr: 0x1cdf
+  __TEXT.__swift5_fieldmd: 0x18b0
   __TEXT.__swift5_assocty: 0x6b0
   __TEXT.__swift5_proto: 0x214
-  __TEXT.__swift5_types: 0x178
+  __TEXT.__swift5_types: 0x17c
   __TEXT.__objc_classname: 0x62b
-  __TEXT.__objc_methname: 0x4469
-  __TEXT.__swift5_capture: 0x10ec
+  __TEXT.__objc_methname: 0x4579
+  __TEXT.__swift5_capture: 0x1114
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_cont: 0x110
   __TEXT.__objc_methtype: 0x14da
+  __TEXT.__oslogstring: 0x24cf
   __TEXT.__swift_as_ret: 0x84
-  __TEXT.__oslogstring: 0x1f4f
   __TEXT.__swift5_protos: 0x8
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__unwind_info: 0x24f8
-  __TEXT.__eh_frame: 0x1e54
-  __DATA_CONST.__const: 0x42d0
+  __TEXT.__unwind_info: 0x24f0
+  __TEXT.__eh_frame: 0x1e5c
+  __DATA_CONST.__const: 0x4310
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__auth_got: 0x1cc0
-  __DATA_CONST.__got: 0xd98
-  __DATA_CONST.__auth_ptr: 0xcf0
-  __DATA.__objc_const: 0x26e8
-  __DATA.__objc_selrefs: 0xe10
+  __DATA_CONST.__auth_got: 0x1cd0
+  __DATA_CONST.__got: 0xdc8
+  __DATA_CONST.__auth_ptr: 0xcf8
+  __DATA.__objc_const: 0x26c8
+  __DATA.__objc_selrefs: 0xe70
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x1930
-  __DATA.__data: 0x4958
+  __DATA.__objc_data: 0x1920
+  __DATA.__data: 0x4a10
   __DATA.__objc_stublist: 0x18
-  __DATA.__bss: 0x4928
+  __DATA.__bss: 0x4918
   __DATA.__common: 0x230
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3439
-  Symbols:   405
-  CStrings:  1144
+  Functions: 3450
+  Symbols:   408
+  CStrings:  1168
 
Symbols:
+ _AVSystemController_CallIsActive
+ _AVSystemController_CallIsActiveDidChangeNotification
+ _AXAIWhiteGloveLoggingEnabled
+ _OBJC_CLASS_$_AVSystemController
- __AXSLiveTranscriptionSetEnabled
CStrings:
+ "AVSystemController CallIsActive changed: %{bool}d"
+ "AXLSTextEntryField"
+ "attributeForKey:"
+ "avSystemCallActive"
+ "frame"
+ "handleAVSystemCallIsActiveChanged:"
+ "initializeViewFromSavedUIState"
+ "isAppSwitcherVisible"
+ "isControlCenterVisible"
+ "isFirstResponder"
+ "isNotificationCenterVisible"
+ "kAXUILiveSpeechSceneClientIdentifier"
+ "rdar://134841355 keyboardDidShow observer fired viewFrame=%{public}s superviewClass=%{public}s windowLevel=%{public}s"
+ "rdar://134841355 restoreKeyboardFocus becomeFirstResponder returned %{bool,public}d"
+ "rdar://134841355 restoreKeyboardFocus enter inputMode=%{public}s presentTextField=%{bool,public}d hasWindow=%{bool,public}d"
+ "rdar://134841355 restoreKeyboardFocus found candidate class=%{public}s canBecomeFirstResponder=%{bool,public}d isFirstResponder=%{bool,public}d"
+ "rdar://134841355 restoreKeyboardFocus no UITextInput candidate found; skipping becomeFirstResponder"
+ "rdar://134841355 systemOverlay event type=%{public}s isVisible=%{bool,public}d inputMode=%{public}s presentTextField=%{bool,public}d"
+ "rdar://134841355 viewDidAppear animated=%{bool,public}d inputMode=%{public}s presentTextField=%{bool,public}d isHUDVisible=%{bool,public}d windowLevel=%{public}s"
+ "rdar://134841355 viewDidLoad displayID=%{public}u inputMode=%{public}s presentTextField=%{bool,public}d willBringToFront=%{bool,public}d"
+ "rdar://134841355 viewDidLoad liveSpeechViewToFront callback ran superviewClass=%{public}s windowLevel=%{public}s"
+ "rdar://134841355 viewWillTransition size=%{public}s shouldRestoreFocus=%{bool,public}d inputMode=%{public}s presentTextField=%{bool,public}d"
+ "setAccessibilityIdentifier:"
+ "setActiveSceneTrackingEnabled:forSceneClientIdentifier:"
+ "viewIfLoaded"
+ "window"
+ "windowLevel"
- "AppleLanguagePreferencesChangedNotification"
- "languageChanged"
- "lastKnownLanguage"
```
