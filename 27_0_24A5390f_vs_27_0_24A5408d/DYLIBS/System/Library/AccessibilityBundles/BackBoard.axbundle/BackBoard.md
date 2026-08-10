## BackBoard

> `/System/Library/AccessibilityBundles/BackBoard.axbundle/BackBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x27e4c
-  __TEXT.__objc_methlist: 0x22d4
+3048.0.0.0.0
+  __TEXT.__text: 0x281ec
+  __TEXT.__objc_methlist: 0x232c
   __TEXT.__dlopen_cstrs: 0x2d9
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x2317
-  __TEXT.__oslogstring: 0x1e62
+  __TEXT.__cstring: 0x2369
+  __TEXT.__oslogstring: 0x1fc0
   __TEXT.__constg_swiftt: 0x2e0
   __TEXT.__swift5_typeref: 0x17e
   __TEXT.__swift5_reflstr: 0x115

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x18
   __TEXT.__gcc_except_tab: 0x698
-  __TEXT.__unwind_info: 0xd08
+  __TEXT.__unwind_info: 0xd10
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd8
+  __DATA_CONST.__objc_selrefs: 0x1c08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__got: 0x6a8
-  __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x1d60
-  __AUTH_CONST.__objc_const: 0x3038
+  __AUTH_CONST.__const: 0xfc0
+  __AUTH_CONST.__cfstring: 0x1da0
+  __AUTH_CONST.__objc_const: 0x3098
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xc58
+  __AUTH_CONST.__auth_got: 0xc68
   __AUTH.__objc_data: 0x260
-  __DATA.__objc_ivar: 0x158
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x3b8
   __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0xdd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1017
-  Symbols:   2826
-  CStrings:  486
+  Functions: 1027
+  Symbols:   2846
+  CStrings:  492
 
Symbols:
+ -[AXBAccessibilityManager _commonEventRepForTouchEventWithType:location:force:flags:contextId:displayId:]
+ -[AXBAccessibilityManager _sendFingerEvent:location:force:flags:contextId:displayId:]
+ -[AXBAccessibilityManager _sendStylusEvent:location:force:altitude:azimuth:flags:contextId:displayId:]
+ -[AXBLiveCaptionsManager .cxx_destruct]
+ -[AXBLiveCaptionsManager handleLanguagePreferencesChanged]
+ -[AXBLiveCaptionsManager handleSpringBoardFinishedStartup]
+ -[AXBLiveCaptionsManager lastKnownLanguage]
+ -[AXBLiveCaptionsManager setLastKnownLanguage:]
+ -[AXBLiveCaptionsManager setShouldRestoreLiveCaptionsAfterLanguageChange:]
+ -[AXBLiveCaptionsManager shouldRestoreLiveCaptionsAfterLanguageChange]
+ GCC_except_table479
+ GCC_except_table530
+ GCC_except_table576
+ GCC_except_table605
+ GCC_except_table622
+ GCC_except_table635
+ GCC_except_table647
+ GCC_except_table680
+ GCC_except_table718
+ GCC_except_table732
+ GCC_except_table806
+ _CFPreferencesCopyAppValue
+ _OBJC_IVAR_$_AXBLiveCaptionsManager._lastKnownLanguage
+ _OBJC_IVAR_$_AXBLiveCaptionsManager._shouldRestoreLiveCaptionsAfterLanguageChange
+ __AXSLiveTranscriptionSetEnabled
+ ___58-[AXBLiveCaptionsManager handleSpringBoardFinishedStartup]_block_invoke
+ __axbLiveCaptionsLanguagePreferencesChanged
+ __axbLiveCaptionsSpringBoardFinishedStartup
+ _objc_msgSend$_commonEventRepForTouchEventWithType:location:force:flags:contextId:displayId:
+ _objc_msgSend$_sendFingerEvent:location:force:flags:contextId:displayId:
+ _objc_msgSend$_sendStylusEvent:location:force:altitude:azimuth:flags:contextId:displayId:
+ _objc_msgSend$handleLanguagePreferencesChanged
+ _objc_msgSend$handleSpringBoardFinishedStartup
+ _objc_msgSend$lastKnownLanguage
+ _objc_msgSend$setLastKnownLanguage:
+ _objc_msgSend$setShouldRestoreLiveCaptionsAfterLanguageChange:
+ _objc_msgSend$shouldRestoreLiveCaptionsAfterLanguageChange
- -[AXBAccessibilityManager _commonEventRepForTouchEventWithType:location:force:flags:contextId:]
- -[AXBAccessibilityManager _sendFingerEvent:location:force:flags:contextId:]
- -[AXBAccessibilityManager _sendStylusEvent:location:force:altitude:azimuth:flags:contextId:]
- GCC_except_table471
- GCC_except_table520
- GCC_except_table566
- GCC_except_table595
- GCC_except_table612
- GCC_except_table625
- GCC_except_table637
- GCC_except_table670
- GCC_except_table708
- GCC_except_table722
- GCC_except_table796
- _objc_msgSend$_commonEventRepForTouchEventWithType:location:force:flags:contextId:
- _objc_msgSend$_sendFingerEvent:location:force:flags:contextId:
- _objc_msgSend$_sendStylusEvent:location:force:altitude:azimuth:flags:contextId:
CStrings:
+ "AppleLanguagePreferencesChangedNotification"
+ "Primary language changed while Live Captions enabled; disabling for the duration of the language change"
+ "Restoring Live Captions after language change"
+ "SpringBoard finished startup after language change; Live Captions not supported for new language, leaving disabled"
+ "SpringBoard finished startup after language change; restoring Live Captions in %.0fs"
+ "com.apple.springboard.finishedstartup"
```
