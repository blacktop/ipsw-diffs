## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/Versions/A/HomeKitEventRouter`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x18d14
+1520.2.7.4.1
+  __TEXT.__text: 0x18d0c
   __TEXT.__objc_methlist: 0x15dc
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x49c
Functions:
~ ___50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke : 608 -> 600
~ -[HMEMessageDatagramClient _removeRetryTimer] -> __50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke.10 : 116 -> 840
~ __50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke.10 -> -[HMEMessageDatagramClient _didDisconnect] : 840 -> 156
~ -[HMEMessageDatagramClient _didDisconnect] -> -[HMEMessageDatagramClient _enableRetryTimer] : 156 -> 588
~ -[HMEMessageDatagramClient _enableRetryTimer] -> ___copy_helper_block_e8_32s40b48w : 588 -> 84
~ ___copy_helper_block_e8_32s40b48w -> ___destroy_helper_block_e8_32s40s48w : 84 -> 68
~ ___destroy_helper_block_e8_32s40s48w -> -[HMEMessageDatagramClient _performRequestWithBlock:] : 68 -> 200
~ -[HMEMessageDatagramClient _performRequestWithBlock:] -> ___62-[HMEMessageDatagramClient _performChangeRegistrationsRequest]_block_invoke : 200 -> 808
~ ___62-[HMEMessageDatagramClient _performChangeRegistrationsRequest]_block_invoke -> -[HMEMessageDatagramClient _removeRetryTimer] : 808 -> 116
```
