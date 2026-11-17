## SharedWebCredentials

> `/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials`

```diff

-1040.1.0.0.0
-  __TEXT.__text: 0x143a4
+1040.2.0.0.0
+  __TEXT.__text: 0x14390
   __TEXT.__objc_methlist: 0xf8c
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x2458
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ -[_SWCChatterboxResolver resolveWithCompletionHandler:] : 884 -> 880
~ +[_SWCChatterboxResolver(Private) _session] : 252 -> 248
~ +[_SWCChatterboxResolver(Private) _resolverForTask:] : 148 -> 144
~ +[_SWCChatterboxResolver(Private) _setResolver:forTask:] : 216 -> 212
~ +[_SWCChatterboxResolver(Private) _invokeCompletionHandlerForTask:result:error:] : 628 -> 624
```
