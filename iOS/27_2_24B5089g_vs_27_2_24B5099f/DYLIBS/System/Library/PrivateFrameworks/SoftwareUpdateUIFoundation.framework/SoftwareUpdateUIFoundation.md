## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-772.40.11.0.0
-  __TEXT.__text: 0xad350
+772.40.12.0.0
+  __TEXT.__text: 0xad560
   __TEXT.__objc_methlist: 0x22f4
   __TEXT.__const: 0x23c0
-  __TEXT.__cstring: 0x6d98
+  __TEXT.__cstring: 0x6db8
   __TEXT.__gcc_except_tab: 0x2500
   __TEXT.__oslogstring: 0xad07
   __TEXT.__swift5_typeref: 0x785

   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__got: 0x460
   __AUTH_CONST.__const: 0x1790
-  __AUTH_CONST.__cfstring: 0x3f80
+  __AUTH_CONST.__cfstring: 0x4000
   __AUTH_CONST.__objc_const: 0x6a10
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__auth_got: 0x910

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2099
   Symbols:   2310
-  CStrings:  975
+  CStrings:  978
 
Functions:
~ _SUUIAnalyticsEventTypeToString : 128 -> 192
~ -[SUUIAnalyticsEvent initWithCoder:] : 544 -> 540
~ -[SUUIAnalyticsEvent descriptionDictionary] : 756 -> 876
~ +[SUUIAudienceTypeUtilities description:] : 180 -> 244
~ +[SUUIDownloadPhaseUtilities description:] : 180 -> 244
~ +[SUUIMDMSoftwareUpdatePathUtilities description:] : 224 -> 288
~ +[SUUISoftwareUpdateTypeUtilities description:] : 268 -> 332
~ +[SUUISoftwareUpdateVersionTypeUtilities description:] : 180 -> 244
~ _SUUIUserDefaultsEntryTypeToString : 348 -> 376
CStrings:
+ "<unknown %@: %lld>"
+ "path"
+ "phase"
```
