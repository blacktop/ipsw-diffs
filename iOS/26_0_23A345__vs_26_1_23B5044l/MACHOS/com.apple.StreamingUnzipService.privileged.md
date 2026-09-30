## com.apple.StreamingUnzipService.privileged

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0x1552c
+244.0.0.0.0
+  __TEXT.__text: 0x15bb0
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0xeb4
+  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methlist: 0xecc
   __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x2db1
-  __TEXT.__oslogstring: 0x3608
+  __TEXT.__gcc_except_tab: 0x58
+  __TEXT.__cstring: 0x2f52
+  __TEXT.__oslogstring: 0x36e5
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x2d8b
+  __TEXT.__objc_methname: 0x2ddf
   __TEXT.__objc_methtype: 0xca9
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c8
   __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__cfstring: 0x1940
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__cfstring: 0x1960
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA.__objc_const: 0x1e00
-  __DATA.__objc_selrefs: 0xa08
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_const: 0x1e30
+  __DATA.__objc_selrefs: 0xa18
+  __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x370
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 471E1A91-E58D-33D4-B323-8555B7399000
-  Functions: 294
+  UUID: 6EA8F7F5-352D-3183-9163-19433205AE4D
+  Functions: 301
   Symbols:   221
-  CStrings:  1409
+  CStrings:  1421
 
Symbols:
+ _dispatch_group_notify
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "-[StreamingUnzipper _runTeardownCompletionWhenAsyncWorkFinishes:]"
+ "-[StreamingUnzipper supplyBytes:withReply:]"
+ "07:24:03"
+ "NO == self.teardownInitiated"
+ "Sep  5 2025"
+ "TB,N,V_teardownInitiated"
+ "Teardown has been started for this extractor, but the client has made another concurrent call to this extractor while its teardown is pending. Concurrently calling methods on a SZExtractor instance is not supported."
+ "Teardown has been started for this extractor, but the client has made another concurrent call to this extractor while its teardown is pending. Concurrently calling methods on a SZExtractor instance is not supported. : %@"
+ "_teardownInitiated"
+ "com.apple.StreamingZip.AsyncWorkNotifyQueue"
+ "setTeardownInitiated:"
+ "teardownInitiated"
+ "v16@?0@\"NSError\"8"
- "21:14:16"
- "Aug  2 2025"

```
