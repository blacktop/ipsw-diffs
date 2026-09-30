## Catalyst

> `/System/Library/PrivateFrameworks/Catalyst.framework/Versions/A/Catalyst`

```diff

-23.0.0.0.0
-  __TEXT.__text: 0x63d68
+24.0.0.0.0
+  __TEXT.__text: 0x63ddc
   __TEXT.__objc_methlist: 0x5760
   __TEXT.__const: 0xe48
   __TEXT.__cstring: 0x2ea4

   __DATA_CONST.__got: 0x5d8
   __AUTH_CONST.__const: 0x1d88
   __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0xb598
+  __AUTH_CONST.__objc_const: 0xb5b8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x958
-  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x1728
   __DATA.__bss: 0x940
   __DATA_DIRTY.__objc_data: 0x2530

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 2639
-  Symbols:   5066
+  Symbols:   5067
   CStrings:  526
 
Symbols:
+ OBJC_IVAR_$_CATSharingServiceTransport.mIsInvalidating
Functions:
~ -[CATSharingBroadcastConnection messageReceived:] : 288 -> 292
~ -[CATSharingDeviceSessionConnection didReceiveMessage:] : 288 -> 292
~ -[CATSharingServiceTransport invalidateConnection] : 108 -> 152
~ -[CATSharingServiceTransport connectionClosed:] : 172 -> 236
```
