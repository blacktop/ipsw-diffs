## IdleTimerHosting

> `/System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting`

```diff

 41.0.0.0.0
-  __TEXT.__text: 0x2acc
+  __TEXT.__text: 0x2ab4
   __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x50a
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[ITAttentionAwareIdleTimer setDescriptor:resettingTimer:] : 376 -> 372
~ -[ITAttentionAwareIdleTimer descriptor] : 72 -> 68
~ -[ITAttentionAwareIdleTimer reset] : 140 -> 136
~ -[ITAttentionAwareIdleTimer client:attentionLostTimeoutDidExpire:forContext:] : 156 -> 152
~ -[ITAttentionAwareIdleTimer clientDidReset:forUserAttentionEvent:withContext:] : 192 -> 188
~ -[ITAttentionAwareIdleTimer _context] : 72 -> 68
```
