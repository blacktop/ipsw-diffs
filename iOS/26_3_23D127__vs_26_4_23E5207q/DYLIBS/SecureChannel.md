## SecureChannel

> `/System/Library/PrivateFrameworks/SecureChannel.framework/SecureChannel`

```diff

 1.0.67.0.0
-  __TEXT.__text: 0x884
-  __TEXT.__auth_stubs: 0x170
+  __TEXT.__text: 0x89c
+  __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x148
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0xad

   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xa8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x338

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B79FEC94-97AA-3C34-A9C9-5EF20B6CF8BC
+  UUID: B7D7B8E5-6236-3CD8-91B8-C1DA5238472C
   Functions: 23
-  Symbols:   146
+  Symbols:   143
   CStrings:  73
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_release_x24
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
Functions:
~ +[SecureChannelController actionForURL:completion:] : 264 -> 268
~ ___51+[SecureChannelController actionForURL:completion:]_block_invoke : 136 -> 132
~ +[SecureChannelServiceProxy sharedInstance] : 68 -> 84
~ -[SecureChannelServiceProxy init] : 200 -> 204
~ -[SecureChannelAction initWithURL:title:message:] : 188 -> 172
~ -[SecureChannelAction encodeWithCoder:] : 128 -> 136
~ -[SecureChannelAction initWithCoder:] : 240 -> 252

```
