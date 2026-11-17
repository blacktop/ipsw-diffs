## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

 1153.3.2.0.0
-  __TEXT.__text: 0x823bc
+  __TEXT.__text: 0x82320
   __TEXT.__objc_methlist: 0x5b10
   __TEXT.__const: 0x2dc
   __TEXT.__cstring: 0xb551
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[FBProcess bootstrapWithDelegate:] : 152 -> 148
~ -[FBProcess _updateStateWithBlock:] : 600 -> 596
~ ___30-[FBProcess _bootstrapAndExec]_block_invoke.116 : 236 -> 232
~ -[FBProcess _rebuildState:] : 268 -> 264
~ -[FBProcess _setSceneLifecycleState:] : 184 -> 180
~ -[FBProcess _startWatchdogTimerForContext:] : 216 -> 212
~ -[FBProcess _newWatchdogForContext:completion:] : 492 -> 488
~ -[FBProcess applicationInfo] : 276 -> 268
~ -[FBProcess delegate] : 72 -> 68
~ -[FBProcess isPendingExit] : 60 -> 56
~ -[FBProcess _executeBlockAfterLaunchCompletes:] : 228 -> 224
~ -[FBProcess _launchDidComplete:finalizeBlock:] : 1100 -> 1096
~ ___47-[FBProcess _newWatchdogForContext:completion:]_block_invoke : 508 -> 504
~ -[FBProcess descriptionBuilderWithMultilinePrefix:] : 192 -> 188
~ ___46-[FBProcess _launchDidComplete:finalizeBlock:]_block_invoke_2 : 116 -> 112
~ -[FBProcess isForeground] : 68 -> 64
~ -[FBProcess isBeingDebugged] : 92 -> 88
~ -[FBProcess isRunning] : 68 -> 64
~ -[FBProcess state] : 72 -> 68
~ -[FBProcess isFinishedLaunching] : 60 -> 56
~ -[FBProcess _notePendingExitForReason:] : 628 -> 624
~ -[FBProcess _processDidExitWithContext:] : 620 -> 616
~ -[FBProcess invalidate] : 160 -> 156
~ ___40-[FBProcess _processDidExitWithContext:]_block_invoke_2 : 316 -> 312
~ -[FBProcess exitContext] : 72 -> 68
~ -[FBProcess executableLivesOnSystemPartition] : 108 -> 104
~ -[FBProcess taskState] : 68 -> 64
~ -[FBProcess visibility] : 68 -> 64
~ -[FBProcess isPlatformBinary] : 184 -> 180
~ -[FBProcess _executeBlockAfterBootstrap:] : 268 -> 264
~ -[FBProcess _rebuildState] : 68 -> 64
~ -[FBProcess _shouldWatchdogWithDeclineReason:] : 248 -> 244
~ -[FBProcess _terminateWithRequest:completion:] : 732 -> 728
~ -[FBProcess _lock_consumeLock_performGracefulKill] : 1740 -> 1736
~ ___50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.312 : 120 -> 116
~ -[FBProcess _terminateWithRequest:forWatchdog:] : 200 -> 196
~ -[FBProcess _watchdog:shouldTerminateWithDeclineReason:] : 300 -> 296
~ ___50-[FBProcess _lock_consumeLock_performGracefulKill]_block_invoke.cold.1 : 392 -> 388
```
