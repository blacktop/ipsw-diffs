## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-558.0.0.0.0
-  __TEXT.__text: 0x51b08
+558.120.7.0.0
+  __TEXT.__text: 0x51b48
   __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_stubs: 0x30a0
   __TEXT.__objc_methlist: 0x1384
   __TEXT.__const: 0x2628
   __TEXT.__objc_methname: 0x3eba
-  __TEXT.__oslogstring: 0x12d4
-  __TEXT.__cstring: 0x2c00
+  __TEXT.__oslogstring: 0x12a4
+  __TEXT.__cstring: 0x2c30
   __TEXT.__objc_classname: 0x38f
   __TEXT.__objc_methtype: 0xade
   __TEXT.__gcc_except_tab: 0x228

   __DATA_CONST.__auth_got: 0x858
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x2da0
-  __DATA_CONST.__cfstring: 0x1ca0
+  __DATA_CONST.__const: 0x2dc8
+  __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D0C7A00-0509-3EF5-9161-109270009B38
+  UUID: AB7A7251-9E3E-3189-8EE7-DF145646D879
   Functions: 3042
   Symbols:   332
-  CStrings:  1504
+  CStrings:  1507
 
CStrings:
+ "%@;"
+ "Abort after %d consecutive errors"
+ "Cannot upload nil payload"
+ "Fetched %lu tokens for aggregator %@."
+ "Skipping donation to Bitacora; malformed Trial deployment ID %@ for collection ID %@. Deployment ID must be an integer"
+ "Token fetching timeout after %lld sec."
- "%@; "
- "Failed to fetch a token after %lld sec timeout."
- "Failed to fetch a token after %lld sec timeout; "
- "Fetched %lld tokens for aggregator %@."
- "Skipping donation to Bitacora; malformed Trial deployment ID %@ for colletion ID %@. Deployment ID must be an integer"

```
