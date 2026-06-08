## Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

-1.5.6.0.0
-  __TEXT.__text: 0x748c
-  __TEXT.__auth_stubs: 0xb30
+2.0.26.0.0
+  __TEXT.__text: 0x786c
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x124
   __TEXT.__const: 0x428

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x18
   __TEXT.__objc_methname: 0x3fd
-  __TEXT.__oslogstring: 0x4e3
+  __TEXT.__oslogstring: 0x538
   __TEXT.__swift5_types2: 0xc
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__eh_frame: 0x1e8
-  __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__auth_ptr: 0x178
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__eh_frame: 0x210
   __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_ptr: 0x170
   __DATA.__objc_const: 0x2b0
   __DATA.__objc_selrefs: 0x130
   __DATA.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 915CDD81-8F61-3363-B34B-27EBA782CB4C
-  Functions: 141
-  Symbols:   140
-  CStrings:  111
+  UUID: 56D68D7B-5FCF-3654-8EE6-12E299C522D2
+  Functions: 142
+  Symbols:   154
+  CStrings:  112
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _swift_release_x1
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
- _objc_retain_x24
- _objc_retain_x25
- _swift_retain
CStrings:
+ "Accepting a connection request from “%{public}s”…"
+ "Rejecting a connection request from “%{public}s”…"
+ "The helper service received a connection request from “%{public}s”."
+ "The helper service was launched as root, which isn’t supported. Switching to mobile…"
- "Accepting a session request from “%{public}s”…"
- "Rejecting a session request from “%{public}s”…"
- "The Helper Service was launched as root, which isn’t supported. Switching to mobile…"

```
