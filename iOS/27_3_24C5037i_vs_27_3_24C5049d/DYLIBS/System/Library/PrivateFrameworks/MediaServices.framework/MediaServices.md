## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`

```diff

 4026.300.6.0.0
-  __TEXT.__text: 0x582c8
+  __TEXT.__text: 0x582bc
   __TEXT.__objc_methlist: 0x57a4
   __TEXT.__const: 0x3bc
   __TEXT.__dlopen_cstrs: 0xd4
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[MSVSonicBackgroundTaskProvider beginTaskWithName:expirationHandler:] : 932 -> 928
~ -[MSVSonicBackgroundTaskProvider endTask:] : 476 -> 472
~ -[MSVSonicBackgroundTaskProvider _taskDidTimeout:] : 344 -> 340
~ -[MSVExtendableBackgroundTaskProvider beginTaskWithName:expirationHandler:] : 624 -> 620
~ -[MSVExtendableBackgroundTaskProvider endTask:] : 360 -> 356
~ -[MSVExtendableBackgroundTaskProvider _taskDidTimeout:] : 252 -> 248
~ -[MSVExtendableBackgroundTaskProvider _assertionInvalidated:error:] : 280 -> 276
~ ___63-[MSVExtendableBackgroundTaskProvider _locked_releaseAssertion]_block_invoke : 248 -> 244
~ sub_1b6053b14 -> sub_1b61beaf4 : 268 -> 288
```
