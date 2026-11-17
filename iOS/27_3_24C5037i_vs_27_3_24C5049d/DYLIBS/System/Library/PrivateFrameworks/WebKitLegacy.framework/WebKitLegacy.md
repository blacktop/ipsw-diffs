## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-626.1.12.10.3
-  __TEXT.__text: 0x15d15c
+626.1.17.0.0
+  __TEXT.__text: 0x15d214
   __TEXT.__objc_methlist: 0xf5e8
   __TEXT.__const: 0x2e0
   __TEXT.__getClass_cstr: 0x12
   __TEXT.__dlsym_cstr: 0x39
-  __TEXT.__gcc_except_tab: 0x1327c
-  __TEXT.__cstring: 0x146b4
+  __TEXT.__gcc_except_tab: 0x13284
+  __TEXT.__cstring: 0x1475b
   __TEXT.__oslogstring: 0x14a
   __TEXT.__unwind_info: 0x9d50
   __TEXT.__eh_frame: 0x88

   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x1018
-  __AUTH_CONST.__const: 0x53a0
-  __AUTH_CONST.__cfstring: 0x10560
+  __AUTH_CONST.__const: 0x53c8
+  __AUTH_CONST.__cfstring: 0x10600
   __AUTH_CONST.__objc_const: 0xfe60
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x4798
+  __AUTH_CONST.__auth_got: 0x47a0
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x38
   __DATA.__objc_ivar: 0x4a0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7306
-  Symbols:   13084
-  CStrings:  2376
+  Functions: 7309
+  Symbols:   13087
+  CStrings:  2381
 
Symbols:
+ GCC_except_table550
+ GCC_except_table553
+ GCC_except_table608
+ GCC_except_table610
+ GCC_except_table622
+ GCC_except_table634
+ __ZN7WebCore17FrameLoaderClient23didNotifyUserActivationEN3WTF13MonotonicTimeENSt3__18optionalINS_16ProcessQualifiedINS1_23ObjectIdentifierGenericINS_30UserGestureTokenIdentifierTypeENS1_38ObjectIdentifierMainThreadAccessTraitsEEEEEEE
+ __ZN7WebCore17FrameLoaderClient29didRevokeForcedUserActivationENS_16ProcessQualifiedIN3WTF23ObjectIdentifierGenericINS_30UserGestureTokenIdentifierTypeENS2_38ObjectIdentifierMainThreadAccessTraitsEEEEE
+ __ZN7WebCore24DeprecatedGlobalSettings37setMediaResourceLoadTimeoutForTestingEj
+ __ZNK7WebCore12ChromeClient17devicePostureTypeEv
+ __ZNK7WebCore12ChromeClient18didDisplayCaptionsEON3WTF6VectorINS1_6StringELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEE
- GCC_except_table232
- GCC_except_table549
- GCC_except_table551
- GCC_except_table607
- GCC_except_table609
- GCC_except_table621
- GCC_except_table633
- __ZN7WebCore17FrameLoaderClient23didNotifyUserActivationEN3WTF13MonotonicTimeE
Functions:
+ __ZN7WebCore17FrameLoaderClient25didHandleFirstUserGestureEN3WTF13MonotonicTimeE
~ -[WebView(WebPrivate) initSimpleHTMLDocumentWithStyle:frame:preferences:groupName:] : 8236 -> 8232
~ -[WebView(WebViewEditing) setSmartInsertDeleteEnabled:] : 184 -> 176
+ __ZNK7WebCore12ChromeClient18didDisplayCaptionsEON3WTF6VectorINS1_6StringELm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEE
+ __ZNK15WebChromeClient31canShowDataListSuggestionLabelsEv
~ +[WebPreferences initialize] : 13792 -> 13808
~ +[WebPreferences(WebPrivateExperimentalFeatures) _experimentalFeatures] : 27720 -> 27944
~ +[WebPreferences(WebPrivateInternalFeatures) _internalFeatures] : 15284 -> 15160
~ -[WebView(WebViewInternalPreferencesChangedGenerated) _preferencesChangedGenerated:] : 25376 -> 25440
CStrings:
+ "Device Posture API"
+ "DevicePostureAPIEnabled"
+ "Enable the Device Posture API"
+ "Media Resource Load Timeout For Testing"
+ "MediaResourceLoadTimeoutForTesting"
+ "Test override for the timeout applied to each media resource load serviced by WebKit, in milliseconds (0 means use production default)"
+ "WebKitDevicePostureAPIEnabled"
+ "WebKitMediaResourceLoadTimeoutForTesting"
+ "WebKitRequiresUserGestureToStartAudiblePlaybackWhenHidden"
- "In two-up PDF display mode, align the trailing odd page to the same column as the first page instead of centering it"
- "Two-Up PDF Trailing Page Left Alignment"
- "TwoUpPDFTrailingPageLeftAlignmentEnabled"
- "WebKitTwoUpPDFTrailingPageLeftAlignmentEnabled"
```
