## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-313.0.0.0.0
-  __TEXT.__text: 0x6e9c
+314.0.0.0.0
+  __TEXT.__text: 0x6f84
   __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0xbe0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x137d
+  __TEXT.__cstring: 0x151d
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__unwind_info: 0x270
-  __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0x3267
-  __TEXT.__objc_methtype: 0x12c1
-  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_classname: 0x16c
+  __TEXT.__objc_methname: 0x32b8
+  __TEXT.__objc_methtype: 0x12c3
+  __TEXT.__objc_stubs: 0x2580
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd88
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xa20
-  __AUTH_CONST.__objc_const: 0x1348
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_const: 0x1368
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFC54385-8AC9-3848-BD7B-6D4CF20CEC50
+  UUID: 7962F203-8040-38AB-BC11-1C19CC564F44
   Functions: 176
-  Symbols:   971
-  CStrings:  875
+  Symbols:   975
+  CStrings:  893
 
Symbols:
+ _OBJC_IVAR_$_WSWebSheetView._javaScriptScrapeCredentialsCounter
+ ___block_descriptor_48_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_literal_global.324
+ ___block_literal_global.368
+ ___block_literal_global.757
+ _objc_msgSend$description
+ _objc_msgSend$redactedSensitiveContentForWiFi
+ _objc_msgSend$resourceType
- ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_literal_global.306
- ___block_literal_global.347
- ___block_literal_global.734
Functions:
~ -[WSWebSheetView _scrapeUserCredentialsUsingJavaScript] : 200 -> 248
~ ___55-[WSWebSheetView _scrapeUserCredentialsUsingJavaScript]_block_invoke : 216 -> 396
~ -[WSWebSheetView webView:didStartProvisionalNavigation:] : 212 -> 156
~ -[WSWebSheetView webView:resourceLoad:didCompleteWithError:response:] : 180 -> 240
CStrings:
+ "Completed user input event listener (counter=%ld, current=%ld)"
+ "Did complete resource load (type=%ld), error %@"
+ "FAILED to get user-entered value, returned fatal error (%@)"
+ "FAILED to get user-entered value, returned non-fatal error (%@)"
+ "Q"
+ "Registering user input event listener (counter=%ld)"
+ "Updated user-entered values (%@)"
+ "Will NOT re-register obsolete user input event listener (counter=%ld, current=%ld)"
+ "Will re-register user input event listener (counter=%ld, current=%ld)"
+ "_javaScriptScrapeCredentialsCounter"
+ "redactedSensitiveContentForWiFi"
+ "resourceType"
+ "\xf0\xf0\x91"
- "FAILED to scrape user-entered value, returned error (%@)"
- "\xf0\xf0\x81"

```
