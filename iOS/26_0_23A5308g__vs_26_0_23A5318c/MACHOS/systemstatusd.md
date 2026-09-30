## systemstatusd

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd`

```diff

-247.0.0.0.0
-  __TEXT.__text: 0xacc
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x400
+248.100.0.0.0
+  __TEXT.__text: 0xc4c
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x4c
   __TEXT.__const: 0x48
-  __TEXT.__objc_methname: 0x33d
-  __TEXT.__cstring: 0x140
+  __TEXT.__objc_methname: 0x377
+  __TEXT.__cstring: 0x199
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x88
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x110
-  __DATA.__objc_selrefs: 0x120
+  __DATA.__objc_selrefs: 0x130
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B324589D-9C3A-30E2-AAEB-A296E2DF7DC5
-  Functions: 15
-  Symbols:   63
-  CStrings:  63
+  UUID: E6BE0750-0764-36A2-AB7B-F76CE7F9480E
+  Functions: 18
+  Symbols:   66
+  CStrings:  68
 
Symbols:
+ _BSDispatchQueueCreateSerialWithQoS
+ _OBJC_CLASS_$_STDataAccessStatusDomainDataProviderTransformer
+ _dispatch_async
Functions:
~ sub_1000011ac : 1192 -> 1392
CStrings:
+ "com.apple.systemstatus.data-access.async-queue"
+ "initWithDataProvider:publisherServerHandle:"
+ "internalQueuePublisherServerHandle"
+ "setDataChangedHandler:"
+ "v20@?0@\"STDataAccessStatusDomainData\"8B16"
- "initWithServerHandle:publisherServerHandle:"

```
