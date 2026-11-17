## Radio

> `/System/Library/PrivateFrameworks/Radio.framework/Radio`

```diff

 4026.300.4.0.0
-  __TEXT.__text: 0x20c24
+  __TEXT.__text: 0x20c0c
   __TEXT.__objc_methlist: 0x1b40
   __TEXT.__cstring: 0x165b
   __TEXT.__const: 0x65
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[RadioAvailabilityController isRadioAvailable] : 60 -> 56
~ ___95-[RadioAvailabilityController _updateRadioAvailabilityWithStoreURLBag:error:completionHandler:]_block_invoke : 368 -> 364
~ -[RadioAvailabilityController environmentMonitorDidChangeNetworkReachability:] : 96 -> 92
~ -[RadioAvailabilityController hasLoadedRadioAvailability] : 68 -> 64
~ -[RadioAvailabilityController getRadioAvailabilityWithCompletionHandler:] : 236 -> 232
~ ___54-[RadioAvailabilityController _reloadRadioRestriction]_block_invoke : 104 -> 100
```
