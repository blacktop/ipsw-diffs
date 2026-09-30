## MobileSystemServices

> `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0x30b4
-  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__text: 0x32d0
+  __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x820
   __TEXT.__cstring: 0xbc5
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methname: 0x82e
   __TEXT.__objc_methtype: 0x20b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x6a0
   __AUTH_CONST.__objc_const: 0x3f0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 814D0097-F640-3E85-9765-D3BD19A15C09
+  UUID: 4F468045-4097-3F48-BC01-AA99CAE502F2
   Functions: 65
-  Symbols:   381
+  Symbols:   377
   CStrings:  294
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
- _objc_retain_x9
Functions:
~ -[MOSplunkLogger _onQueue_loadConfiguration] : 352 -> 368
~ ___44-[MOSplunkLogger _onQueue_loadConfiguration]_block_invoke : 780 -> 816
~ -[MOSplunkLogger uploadEventsWithCompletion:] : 280 -> 284
~ ___45-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_2 : 872 -> 900
~ ___45-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_3 : 396 -> 404
~ -[MOSplunkLogger logEventNamed:value:] : 340 -> 348
~ ___38-[MOSplunkLogger logEventNamed:value:]_block_invoke : 204 -> 216
~ -[MOSplunkLogger URLSession:didReceiveChallenge:completionHandler:] : 460 -> 476
~ -[MOSplunkLogger setPath:] : 12 -> 64
~ -[MOSplunkLogger setEvents:] : 12 -> 64
~ -[MOSplunkLogger setQueue:] : 12 -> 64
~ -[MOSplunkLogger setVersion:] : 12 -> 64
~ -[MOSplunkLogger setSplunkUploadURL:] : 12 -> 64
~ -[MOSplunkLogger setConfigurationURL:] : 12 -> 64
~ -[MOSplunkLogger setSplunkTopic:] : 12 -> 64
~ -[MOSplunkLogger setSamplingPercentage:] : 12 -> 64
~ _MOLogGetLogLevel : 128 -> 124

```
