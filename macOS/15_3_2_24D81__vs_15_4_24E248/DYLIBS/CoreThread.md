## CoreThread

> `/System/Library/PrivateFrameworks/CoreThread.framework/Versions/A/CoreThread`

```diff

-265.0.53.0.0
-  __TEXT.__text: 0x2770
+275.0.104.0.0
+  __TEXT.__text: 0x2784
   __TEXT.__auth_stubs: 0xd0
-  __TEXT.__objc_methlist: 0x560
+  __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x5a
   __TEXT.__cstring: 0x100
   __TEXT.__oslogstring: 0x29
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x110
   __TEXT.__objc_classname: 0x124
   __TEXT.__objc_methname: 0xb27
   __TEXT.__objc_methtype: 0x21e

   __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x13a0
+  __AUTH_CONST.__objc_const: 0x1348
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F81D115-AAAE-3726-8B02-B59285C769A3
-  Functions: 103
-  Symbols:   357
+  UUID: AF8475EA-E7B9-3447-9EEE-E19557639EF2
+  Functions: 104
+  Symbols:   358
   CStrings:  209
 
Symbols:
+ THLogHandleForCategory.cold.1
Functions:
~ -[THThreadNetworkCredentialsStoreRecord initWithCoder:] : 528 -> 532
~ -[THPreferredThreadNetwork initWithCoder:] : 460 -> 464
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:] : 672 -> 676
~ -[THNetworkSignature initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:] : 260 -> 264
~ _THLogHandleForCategory : 100 -> 84

```
