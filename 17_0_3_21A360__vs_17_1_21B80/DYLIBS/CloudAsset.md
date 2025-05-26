## CloudAsset

> `/System/Library/PrivateFrameworks/CloudAsset.framework/CloudAsset`

```diff

-2100.171.0.0.0
-  __TEXT.__text: 0x51d30
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__const: 0x59e0
-  __TEXT.__constg_swiftt: 0x11b8
-  __TEXT.__swift5_typeref: 0x1424
+2120.14.0.0.0
+  __TEXT.__text: 0x571d8
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__const: 0x5af0
+  __TEXT.__constg_swiftt: 0x125c
+  __TEXT.__swift5_typeref: 0x1476
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x719
-  __TEXT.__swift5_fieldmd: 0xf4c
-  __TEXT.__swift5_types: 0x170
+  __TEXT.__swift5_reflstr: 0x769
+  __TEXT.__swift5_fieldmd: 0xf9c
+  __TEXT.__swift5_types: 0x174
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__cstring: 0xc7b
-  __TEXT.__swift5_proto: 0x5c8
-  __TEXT.__swift5_protos: 0x8
+  __TEXT.__cstring: 0xdab
+  __TEXT.__swift5_proto: 0x5d0
+  __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x1c8
-  __TEXT.__unwind_info: 0x247c
-  __TEXT.__eh_frame: 0x25d0
+  __TEXT.__swift5_capture: 0x208
+  __TEXT.__unwind_info: 0x2a48
+  __TEXT.__eh_frame: 0x2a78
   __TEXT.__objc_methname: 0x46
-  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x850
+  __DATA_CONST.__objc_const: 0x8d8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__const: 0x1eb8
-  __AUTH_CONST.__auth_ptr: 0xb8
-  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__const: 0x2010
+  __AUTH_CONST.__auth_ptr: 0xc0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH.__data: 0x528
   __AUTH.__objc_data: 0x50
   __DATA.__objc_classrefs: 0x10
-  __DATA.__data: 0x1570
+  __DATA.__data: 0x1638
   __DATA.__common: 0xf0
-  __DATA.__bss: 0xb900
-  __DATA_DIRTY.__const: 0x1570
+  __DATA.__bss: 0xba00
+  __DATA_DIRTY.__const: 0x1560
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xc88
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3288
-  Symbols:   981
-  CStrings:  106
+  Functions: 3409
+  Symbols:   989
+  CStrings:  112
 
Symbols:
+ _$s10CloudAsset16XPCMessageSenderC4sendyq_xYaKSERzs8SendableRzSeR_r0_lF
+ _$s10CloudAsset16XPCMessageSenderC4sendyq_xYaKSERzs8SendableRzSeR_r0_lFTu
+ _$s3XPC12XPCRichErrorV8canRetrySbvg
+ _$s3XPC12XPCRichErrorVMa
+ _$s3XPC12XPCRichErrorVMn
+ _$s3XPC12XPCRichErrorVs0C0AAMc
+ _$syycWV
+ _objc_release_x28
+ _objc_release_x8
+ _swift_allocateGenericClassMetadata
+ _swift_initClassMetadata2
- _$s10CloudAsset16XPCMessageSenderC4sendyq_xYaKSERzSeR_r0_lF
- _$s10CloudAsset16XPCMessageSenderC4sendyq_xYaKSERzSeR_r0_lFTu
- _swift_deallocPartialClassInstance
CStrings:
+ "[message id = %s] evict xpc session from cache as it is no longer usable"
+ "[message id = %s] failed to send message over XPC due to XPC error %@"
+ "[message id = %s] failed to send message over XPC due to non-XPC error %@"
+ "cachedSession"
+ "error received from xpc session is not XPC error type."
+ "incomingMessageHandler"
+ "machServiceName"
+ "received xpc error %@ from xpc session"
+ "xpc session cache deinit"
+ "xpcSessionCache"
- "[message id = %s] failed to send message over XPC with error %@"
- "message sender deinit"
- "received reply %@ from other side"
- "xpcSession"

```
