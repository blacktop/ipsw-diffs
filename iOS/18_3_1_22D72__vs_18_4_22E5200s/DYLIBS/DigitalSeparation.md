## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-423.0.58.0.0
-  __TEXT.__text: 0x1de94
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x114c
-  __TEXT.__cstring: 0x1038
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x89c
-  __TEXT.__oslogstring: 0x19e6
+425.0.98.0.0
+  __TEXT.__text: 0x1f484
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x143c
+  __TEXT.__cstring: 0x110c
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x898
+  __TEXT.__oslogstring: 0x1b1f
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x628
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3a42
+  __TEXT.__objc_methname: 0x3b8c
   __TEXT.__objc_methtype: 0x86a
-  __TEXT.__objc_stubs: 0x3400
+  __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xb40
+  __DATA_CONST.__const: 0xba0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf38
+  __DATA_CONST.__objc_selrefs: 0x1020
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x1040
-  __AUTH_CONST.__objc_const: 0x2a38
+  __AUTH_CONST.__cfstring: 0x11a0
+  __AUTH_CONST.__objc_const: 0x2560
   __AUTH.__objc_data: 0x640
   __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x1e8

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing
   - /System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 518
-  Symbols:   822
-  CStrings:  1055
+  Functions: 566
+  Symbols:   867
+  CStrings:  1085
 
Symbols:
+ _AnalyticsSendEventLazy
+ _DSLocalizationTypeSharedNamedResource
+ _DSSourceErrorDomain
+ _MGGetBoolAnswer
+ _NumResourcesNamedInDetailText
- _objc_retain_x25
CStrings:
+ "\"%@\""
+ "%@_NAME_TRUNCATION"
+ "2 resource types are not supported for enumeration: %{public}@"
+ "@\"NSDictionary\"8@?0"
+ "Failed to convert %@ into a cn phone number"
+ "Found matching contact %{private}@ based on email %{private}@"
+ "Found matching contact %{private}@ based on phone number %{private}@"
+ "Found potential contact match by name: %{private}@"
+ "No loc key present matching %@"
+ "Nullifying allowlist because it's not in use right now"
+ "Optimal contact is nil, selecting the fallback contact"
+ "RESOURCE_DISPLAY_NAME"
+ "WITH_NAME"
+ "\\s+"
+ "com.apple.DigitalSeparation.DSSourceErrorDomain"
+ "com.apple.DigitalSeparation.FinishedFetch"
+ "com.apple.DigitalSeparation.NamedResources"
+ "contactMatchingIdentity:"
+ "ds_formattedPhoneNumberForString:"
+ "ds_presentableErrorsByLocalizedAppName"
+ "errorCode"
+ "errorDomain"
+ "formattedInternationalStringValue"
+ "green-tea"
+ "initWithString:"
+ "isAllowListEnabled"
+ "isString:likeString:"
+ "localizedResourceNamesForPerson:"
+ "lowercaseString"
+ "nullifyReplicatorAllowlist"
+ "numberWithLong:"
+ "setAllowList:"
+ "sourceName"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
- "Choosing contact %{private}@ because it has a name and image data"
- "Making contact %{private}@ the current best choice"
- "STOP_BY_PERSON_OUTGOING_SINGLE_%@_WITH_NAME"
- "contactMatchingPredicates:"

```
