## com.apple.AUC

> `com.apple.AUC`

```diff

-562.3.0.0.0
+568.2.0.0.0
   __TEXT.__cstring: 0x93a
   __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x5b84
+  __TEXT_EXEC.__text: 0x5c88
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc5
   __DATA.__common: 0xd8

   __DATA_CONST.__const: 0x1c98
   __DATA_CONST.__kalloc_type: 0x240
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 81C894B6-DAAD-3568-AF37-B21A2D007182
+  UUID: 557F7011-E847-3024-A2E3-77739E14EF09
   Functions: 238
   Symbols:   661
   CStrings:  42
Functions:
~ __ZN3AUC43protectedIOSurfaceSeenRecentlyTimer_HandlerEP8OSObjectP18IOTimerEventSource : 416 -> 420
~ __ZN3AUC4stopEP9IOService : 408 -> 428
~ __ZN3AUC4initEP12OSDictionary : 176 -> 188
~ __ZN3AUC4freeEv : 232 -> 236
~ __ZN3AUC15read_edt_stringEP9IOServicePKcjPc : 400 -> 420
~ __ZN3AUC22getNextUserClientIndexEPj : 80 -> 84
~ __ZN3AUC13SetUserClientEP13AUCUserClientPj : 160 -> 168
~ __ZN3AUC26DPRemovedNotificationGatedEP9IOService : 324 -> 332
~ __ZL27auc_CreateAUPPacketCallbackP8OSObjectP6OSDataPv : 264 -> 272
~ __ZN3AUC14hdcp_get_replyEPhPm : 416 -> 436
~ __ZN3AUC29aucUpstreamConnectionCallbackE30UpstreamConnectionCallbackTypePv : 112 -> 116
~ __ZN3AUC34aucUpstreamConnectionStatusUpdatedEv : 96 -> 104
~ __ZN3AUC34aucUpstreamConnectionStatusChangedEv : 64 -> 68
~ __ZN3AUC47upstreamConnectionsGetCombinedStatusUpdatedFlagEv : 72 -> 84
~ __ZN13AUCUserClient29_DetachUserClientFromProviderEPS_PvP25IOExternalMethodArguments : 44 -> 52
~ __ZN13AUCUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 68 -> 88
~ __ZN13AUCUserClient8withTaskEP4task : 212 -> 232
~ __ZN13AUCUserClient4stopEP9IOService : 156 -> 160
~ __ZN13AUCUserClient28DetachUserClientFromProviderEv : 44 -> 52
~ __ZN13AUCUserClient23SetStatusChangeCallbackEP38_AUCKernelStatusChangeCallbackInStructP39_AUCKernelStatusChangeCallbackOutStructP8ipc_portPy : 132 -> 144
~ __ZN7AUCLockD2Ev : 56 -> 60
~ __ZN7AUCLockD1Ev : 56 -> 60
~ __ZN16AUCRecursiveLockD2Ev : 56 -> 60
~ __ZN16AUCRecursiveLockD1Ev : 56 -> 60
~ __ZN11AUCWorkloop4initEPc : 88 -> 92
~ __ZN11AUCWorkloop6createEPc : 196 -> 200
~ __ZN11AUCWorkloop4freeEv : 140 -> 144
~ __ZN24AUCAsynchronousScheduler24aucAsynchronousSchedulerEPFiPvS0_S0_S0_E : 208 -> 228
~ __ZN24AUCAsynchronousScheduler2goEPFiPvS0_S0_S0_EPjbS0_S0_S0_S0_ : 288 -> 308
~ __ZN24AUCAsynchronousScheduler21checkAndQueueArgumentEPNS_13ArgumentEntryE : 184 -> 200
~ __ZN24AUCAsynchronousScheduler11abortThreadEj : 320 -> 312
~ __ZN24AUCAsynchronousScheduler10joinThreadEjj : 148 -> 152
~ __ZN24AUCAsynchronousScheduler4initEv : 300 -> 320
~ __ZN24AUCAsynchronousScheduler20performActions_gatedEv : 600 -> 592
~ __ZN24AUCAsynchronousScheduler4freeEv : 184 -> 188
~ __ZN18ConnectionWatchdog4initEP3AUC17AULUpstreamFlavor : 280 -> 288
~ __ZN18ConnectionWatchdog19timer_handler_gatedEPvS0_S0_ : 252 -> 260
~ __ZN18ConnectionWatchdog27upstreamConnectionSetStatusEjbjb : 396 -> 392
~ __ZN18ConnectionWatchdog32setMessageTimerThresholdMS_gatedEj : 148 -> 152
~ __ZN18ConnectionWatchdog4freeEv : 248 -> 184
~ __ZN18ConnectionWatchdog29upstreamConnectionSendMessageEv : 268 -> 272
~ __ZN18ConnectionWatchdog17LocalAULGetReqMsgE17AULUpstreamFlavorPhPj : 88 -> 92
~ __ZN18ConnectionWatchdog28upstreamConnectionGetMessageEv : 296 -> 292
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/CoreAUCKext/Kernel/Embedded/AUC.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CoreAUCKext/Kernel/Embedded/AUC.cpp"

```
