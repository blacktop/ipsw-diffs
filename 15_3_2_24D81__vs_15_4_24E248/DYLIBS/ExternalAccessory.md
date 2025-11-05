## ExternalAccessory

> `/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`

```diff

   __TEXT.__objc_methlist: 0x12c0
   __TEXT.__cstring: 0x4a97
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methname: 0x391f
   __TEXT.__objc_methtype: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F7A819C-ECCB-36E1-B969-602D22710742
-  Functions: 431
-  Symbols:   1365
+  UUID: 1BAF04AB-0A51-36CA-B5B7-8E291EA5B42E
+  Functions: 433
+  Symbols:   1368
   CStrings:  1458
 
Symbols:
+ +[EAAccessoryManager sharedAccessoryManager].cold.1
+ -[EAAccessoryInternal init].cold.1
+ -[EAAccessoryManager _initFromSingletonCreationMethod].cold.1
Functions:
~ -[EAAccessoryManager _initFromSingletonCreationMethod] : 1384 -> 1368
~ +[EAAccessoryManager sharedAccessoryManager] : 68 -> 56
~ ___76-[EAAccessoryManager _notifyObserversThatAccessoryDisconnectedWithUserInfo:]_block_invoke : 228 -> 224
~ -[EAAccessoryManager _findExtraAccessoriesContainedOnlyIniAP:] : 532 -> 528
~ -[EAAccessoryManager _externalAccessoryConnected:] : 1248 -> 1240
~ ___50-[EAAccessoryManager _externalAccessoryConnected:]_block_invoke : 464 -> 460
~ ___50-[EAAccessoryManager _externalAccessoryConnected:]_block_invoke_2 : 192 -> 188
~ -[EAAccessoryManager _externalAccessoryUpdated:] : 256 -> 248
~ -[EAAccessoryManager closeInputStreamForEASessionUUID:] : 84 -> 76
~ -[EAOutputStream initWithAccessory:forSession:socket:] : 356 -> 360
~ -[EAOutputStream open] : 300 -> 304
~ -[EAOutputStream scheduleInRunLoop:forMode:] : 392 -> 396
~ -[EAOutputStream write:maxLength:] : 488 -> 496
~ -[EAOutputStream hasSpaceAvailable] : 116 -> 108
~ -[EAInputStream open] : 688 -> 700
~ -[EASession initWithAccessory:forProtocol:] : 1176 -> 1184
~ ___43-[EASession initWithAccessory:forProtocol:]_block_invoke : 180 -> 172
~ -[EAAccessory description] : 424 -> 420
~ -[EAAccessory _endSession:] : 284 -> 288
~ -[EAAccessory getNMEASentence:] : 472 -> 468
~ -[EAAccessory addNMEASentence:withTimestamps:] : 340 -> 336
~ -[EAAccessory getEphemerisRecommendRefreshInterval:] : 120 -> 116
~ -[EAAccessory getEphemerisExpirationInterval:] : 120 -> 116
~ -[EAAccessoryInternal init] : 192 -> 176
~ ___HandleForSource : 572 -> 596
- sub_1aebf31bc
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessory.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessoryManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAInputStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAOutputStream.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EASession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessory.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessoryManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAInputStream.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAOutputStream.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EASession.m"

```
