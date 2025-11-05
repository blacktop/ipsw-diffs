## BackgroundAssets

> `/System/Library/Frameworks/BackgroundAssets.framework/Versions/A/BackgroundAssets`

```diff

-182.0.0.0.0
-  __TEXT.__text: 0x13234
+186.100.4.0.0
+  __TEXT.__text: 0x12dfc
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0xabc
+  __TEXT.__objc_methlist: 0xea8
   __TEXT.__const: 0x288
-  __TEXT.__gcc_except_tab: 0x364
+  __TEXT.__gcc_except_tab: 0x398
   __TEXT.__cstring: 0x32b3
   __TEXT.__oslogstring: 0x4d4
-  __TEXT.__swift5_typeref: 0x168
+  __TEXT.__swift5_typeref: 0x16a
   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_reflstr: 0x47

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__swift_as_entry: 0x10
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x5a8
   __TEXT.__eh_frame: 0x140
   __TEXT.__objc_classname: 0x310
   __TEXT.__objc_methname: 0x2398

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f8
+  __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x6f8
   __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x2338
+  __AUTH_CONST.__objc_const: 0x1c40
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x710

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4B1CB878-BEA1-32F0-9C40-40A50B4A617A
-  Functions: 487
-  Symbols:   1217
+  UUID: 300A256F-EE64-364D-979E-33757CD2B5B2
+  Functions: 535
+  Symbols:   1270
   CStrings:  900
 
Symbols:
+ +[BADownload(VeryPrivate) classesForSerialization].cold.1
+ +[BADownloadManager sharedManager].cold.1
+ -[BAAgentClientProxy _setupConnection].cold.1
+ -[BAAgentClientProxy _setupConnection].cold.2
+ -[BADownload initPrivatelyWithApplicationGroupIdentifier:].cold.1
+ -[BADownload setClientSpecifiedFileSize:].cold.2
+ -[BADownloadManager cancelDownload:error:].cold.2
+ -[BADownloadManager initWithApplicationIdentifier:].cold.2
+ -[BADownloadManager performWithExclusiveControl:].cold.2
+ -[BADownloadManager performWithExclusiveControl:].cold.3
+ -[BADownloadManager performWithExclusiveControlBeforeDate:performHandler:].cold.3
+ -[BADownloadManager performWithExclusiveControlBeforeDate:performHandler:].cold.4
+ -[BADownloadManager scheduleDownload:error:].cold.4
+ -[BADownloadManager(XPCDownloadSync) syncDownloads:].cold.1
+ BAClientConnectionLogObject.cold.1
+ BAClientLogObject.cold.1
+ BASystemLogObject.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _symbolic _____So15NSURLCredentialCSgIeghyg_ So36NSURLSessionAuthChallengeDispositionV
+ _symbolic _____So15NSURLCredentialCSgIeyBhyy_ So36NSURLSessionAuthChallengeDispositionV
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.1
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.2
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.3
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.4
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.5
- -[BADownloadManager(XPCDownloadSync) downloadIdentifierDidFinish:sandboxExtensionToken:wasHandled:].cold.6
- _symbolic _____So15NSURLCredentialCSgIegyg_ So36NSURLSessionAuthChallengeDispositionV
- _symbolic _____So15NSURLCredentialCSgIeyByy_ So36NSURLSessionAuthChallengeDispositionV

```
