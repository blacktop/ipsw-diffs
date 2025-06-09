## DAEAS

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Frameworks/DAEAS.framework/DAEAS`

```diff

-2067.40.1.0.0
-  __TEXT.__text: 0x94184
-  __TEXT.__auth_stubs: 0x1c50
+2072.0.0.0.0
+  __TEXT.__text: 0x94198
+  __TEXT.__auth_stubs: 0x1c60
   __TEXT.__objc_methlist: 0xa58c
   __TEXT.__const: 0x700
   __TEXT.__gcc_except_tab: 0xe48
-  __TEXT.__cstring: 0x8e18
+  __TEXT.__cstring: 0x8e5c
   __TEXT.__oslogstring: 0x560b
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__unwind_info: 0x19d0
   __TEXT.__objc_classname: 0xea5
   __TEXT.__objc_methname: 0x13092
   __TEXT.__objc_methtype: 0x1f4c
   __TEXT.__objc_stubs: 0xec80
-  __DATA_CONST.__got: 0xb68
+  __DATA_CONST.__got: 0xb70
   __DATA_CONST.__const: 0xa80
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x50

   __DATA_CONST.__objc_selrefs: 0x4870
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x378
-  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__auth_got: 0xe40
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x74a0
   __AUTH_CONST.__objc_const: 0x16a58

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 88D26CB2-4134-3453-840F-FC488803BB02
+  UUID: 02D394BF-C0B0-33FF-8522-A557CD6CBCD2
   Functions: 3418
-  Symbols:   12904
-  CStrings:  6595
+  Symbols:   12906
+  CStrings:  6597
 
Symbols:
+ __os_feature_enabled_impl
+ _kConsumerEASEndPoint
Functions:
~ -[ASAccount autodiscoverV2Task:completedWithStatus:authorizationURI:easEndPoint:issuer:error:] : 1852 -> 1876
~ -[ASEvent saveToCalendarWithExistingRecord:intoCalendar:shouldMergeProperties:outMergeDidChooseLocalProperties:account:] : 9672 -> 9688
~ -[ASTask attemptRetryWithStatus:error:] : 324 -> 304
CStrings:
+ "AccountsUI"
+ "ModernAddFlow"
+ "https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize/"
- "https://eas.outlook.com"

```
