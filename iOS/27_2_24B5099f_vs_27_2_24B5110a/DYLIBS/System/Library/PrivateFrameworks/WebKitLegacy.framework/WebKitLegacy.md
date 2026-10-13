## WebKitLegacy

> `/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0x160ed8
+625.2.8.10.4
+  __TEXT.__text: 0x160f78
   __TEXT.__objc_methlist: 0xf5e8
   __TEXT.__const: 0x294
   __TEXT.__getClass_cstr: 0x12
   __TEXT.__dlsym_cstr: 0x39
-  __TEXT.__gcc_except_tab: 0x131bc
-  __TEXT.__cstring: 0x1c8e0
+  __TEXT.__gcc_except_tab: 0x131c0
+  __TEXT.__cstring: 0x1c9db
   __TEXT.__oslogstring: 0x14a
   __TEXT.__unwind_info: 0x9d30
   __TEXT.__eh_frame: 0x88

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x1018
   __AUTH_CONST.__const: 0x5370
-  __AUTH_CONST.__cfstring: 0xf600
+  __AUTH_CONST.__cfstring: 0xf680
   __AUTH_CONST.__objc_const: 0xfe60
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /usr/lib/libsqlite3.dylib
   Functions: 7314
   Symbols:   13060
-  CStrings:  2306
+  CStrings:  2310
 
Symbols:
+ __ZN7WebCore24DeprecatedGlobalSettings37setMediaResourceLoadTimeoutForTestingEj
- _objc_release_x28
Functions:
~ +[WebPreferences initialize] : 13028 -> 13044
~ +[WebPreferences(WebPrivateInternalFeatures) _internalFeatures] : 14664 -> 14788
~ -[WebView(WebViewInternalPreferencesChangedGenerated) _preferencesChangedGenerated:] : 23948 -> 23968
CStrings:
+ "Media Resource Load Timeout For Testing"
+ "MediaResourceLoadTimeoutForTesting"
+ "Test override for the timeout applied to each media resource load serviced by WebKit, in milliseconds (0 means use production default)"
+ "WebKitMediaResourceLoadTimeoutForTesting"
```
