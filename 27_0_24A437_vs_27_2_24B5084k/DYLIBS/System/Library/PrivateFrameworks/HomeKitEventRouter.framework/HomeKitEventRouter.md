## HomeKitEventRouter

> `/System/Library/PrivateFrameworks/HomeKitEventRouter.framework/HomeKitEventRouter`

```diff

-1493.1.5.1.1
-  __TEXT.__text: 0x16958
+1514.0.0.0.1
+  __TEXT.__text: 0x16950
   __TEXT.__objc_methlist: 0x15dc
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x49c
Functions:
~ ___50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke : 572 -> 564
~ -[HMEMessageDatagramClient _removeRetryTimer] -> ___50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke.10 : 96 -> 764
~ ___50-[HMEMessageDatagramClient _performConnectRequest]_block_invoke.10 -> -[HMEMessageDatagramClient _didDisconnect] : 764 -> 148
~ -[HMEMessageDatagramClient _didDisconnect] -> -[HMEMessageDatagramClient _enableRetryTimer] : 148 -> 552
~ -[HMEMessageDatagramClient _enableRetryTimer] -> -[HMEMessageDatagramClient _performRequestWithBlock:] : 552 -> 188
~ -[HMEMessageDatagramClient _performRequestWithBlock:] -> ___62-[HMEMessageDatagramClient _performChangeRegistrationsRequest]_block_invoke : 188 -> 756
~ ___62-[HMEMessageDatagramClient _performChangeRegistrationsRequest]_block_invoke -> -[HMEMessageDatagramClient _removeRetryTimer] : 756 -> 96
```
