## BackgroundTasks

> `/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks`

```diff

-2467.60.9.0.0
-  __TEXT.__text: 0xae50
+2467.60.20.0.0
+  __TEXT.__text: 0xae30
   __TEXT.__objc_methlist: 0xed8
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x769
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[BGTask _setTaskCompletedWithSuccess:actionsIfNotAlreadyCompleted:] : 176 -> 172
~ -[BGTask dealloc] : 212 -> 208
~ -[BGTask _callExpirationHandlerWithReason:] : 180 -> 176
~ -[BGContinuedProcessingTask setTaskPaused] : 392 -> 388
~ -[BGContinuedProcessingTask setExpirationHandler:] : 160 -> 156
~ -[BGContinuedProcessingTask expirationHandler] : 120 -> 116
~ -[BGContinuedProcessingTask setExpirationHandlerWithReason:] : 156 -> 152
~ -[BGContinuedProcessingTask expirationHandlerWithReason] : 88 -> 84
```
