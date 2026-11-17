## BoardServices

> `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`

```diff

 827.2.3.0.0
-  __TEXT.__text: 0x7d574
+  __TEXT.__text: 0x7d594
   __TEXT.__objc_methlist: 0x255c
   __TEXT.__const: 0x1af8
   __TEXT.__constg_swiftt: 0x94c
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[BSXPCServiceConnection activeMessageBatch] : 84 -> 80
~ -[BSXPCServiceConnection _lock_disconnect] : 464 -> 460
~ -[BSXPCServiceConnection shouldSendMessage:] : 1164 -> 1160
~ -[BSXPCServiceConnection sendBarrierBlock:] : 840 -> 836
~ sub_18f8b75a8 -> sub_18f96e598 : 316 -> 352
~ sub_18f8c9488 -> sub_18f98049c : 112 -> 124
```
