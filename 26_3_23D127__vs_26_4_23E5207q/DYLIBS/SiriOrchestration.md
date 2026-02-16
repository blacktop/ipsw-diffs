## SiriOrchestration

> `/System/Library/PrivateFrameworks/SiriOrchestration.framework/SiriOrchestration`

```diff

 3404.2.1.0.0
-  __TEXT.__text: 0xaa4
-  __TEXT.__auth_stubs: 0x180
+  __TEXT.__text: 0xb2c
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x83
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x25
   __TEXT.__objc_methname: 0x287
   __TEXT.__objc_methtype: 0x50

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc8
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x1a0
   __AUTH.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5501B8CF-FE9C-3D89-A537-34FF2A79FA99
+  UUID: 8AC5C570-6323-3298-BEE4-CF7C10022FF0
   Functions: 20
-  Symbols:   115
+  Symbols:   114
   CStrings:  52
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x20
Functions:
~ -[MulticastMessageForwarder init] : 104 -> 108
~ -[MulticastMessageForwarder addReceiver:] : 264 -> 268
~ ___41-[MulticastMessageForwarder addReceiver:]_block_invoke : 72 -> 76
~ ___44-[MulticastMessageForwarder removeReceiver:]_block_invoke : 72 -> 76
~ -[MulticastMessageForwarder respondsToSelector:] : 292 -> 300
~ -[MulticastMessageForwarder methodSignatureForSelector:] : 352 -> 368
~ ___48-[MulticastMessageForwarder cleanupNilReceivers]_block_invoke : 108 -> 112
~ -[MulticastMessageForwarder setReceivers:] : 12 -> 64
~ -[MulticastMessageForwarder cleanupNilReceivers] : 212 -> 224
~ -[MulticastMessageForwarder removeReceiver:] : 208 -> 212
~ -[MulticastMessageForwarder forwardInvocation:] : 720 -> 744

```
