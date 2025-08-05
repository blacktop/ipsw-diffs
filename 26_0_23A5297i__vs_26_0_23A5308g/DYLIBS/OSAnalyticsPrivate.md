## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

```diff

-923.0.0.0.0
-  __TEXT.__text: 0x16880
+927.0.2.0.0
+  __TEXT.__text: 0x169b0
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0xe84
+  __TEXT.__objc_methlist: 0xe94
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x1429
+  __TEXT.__cstring: 0x1452
   __TEXT.__oslogstring: 0x222e
   __TEXT.__unwind_info: 0x360
   __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x2d36
+  __TEXT.__objc_methname: 0x2d57
   __TEXT.__objc_methtype: 0x1464
-  __TEXT.__objc_stubs: 0x2520
-  __DATA_CONST.__got: 0x250
+  __TEXT.__objc_stubs: 0x2540
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc78
+  __DATA_CONST.__objc_selrefs: 0xc80
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x2340
+  __AUTH_CONST.__cfstring: 0x2380
   __AUTH_CONST.__objc_const: 0x2698
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4D3BC2BC-3699-33C5-A0C8-BC0CEB7A8F4A
-  Functions: 300
-  Symbols:   1455
-  CStrings:  1509
+  UUID: BC7F3421-E932-33AD-A680-BCB4D2DC835A
+  Functions: 301
+  Symbols:   1459
+  CStrings:  1514
 
Symbols:
+ +[OSASubmitter taskingKeyForRouting:withConfig:]
+ +[OSASubmitter taskingKeyForRouting:withConfig:].cold.1
+ _kOSALogMetadataIncidentID
+ _objc_msgSend$taskingKeyForRouting:withConfig:
- -[OSASubmitter processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:].cold.1
Functions:
~ -[OSASubmitter processSubmissionJobs:usingConfig:summarize:] : 3032 -> 3072
~ -[OSASubmitter processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:] : 5796 -> 5844
~ -[OSASubmitter taskingNeedsRefreshForRouting:at:] : 272 -> 252
+ +[OSASubmitter taskingKeyForRouting:withConfig:]
- -[OSASubmitter processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:].cold.1
+ +[OSASubmitter taskingKeyForRouting:withConfig:].cold.1
CStrings:
+ "core-analytics-tasking-key"
+ "taskingKeyForRouting:withConfig:"
+ "x-incident-id"

```
