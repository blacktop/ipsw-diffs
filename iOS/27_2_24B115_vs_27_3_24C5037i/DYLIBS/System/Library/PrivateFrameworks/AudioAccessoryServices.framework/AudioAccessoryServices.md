## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-41.7.0.0.0
-  __TEXT.__text: 0x4ec70
-  __TEXT.__objc_methlist: 0x60a4
+42.4.1.0.0
+  __TEXT.__text: 0x502ac
+  __TEXT.__objc_methlist: 0x6224
   __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x18c0
-  __TEXT.__cstring: 0xf3e1
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__gcc_except_tab: 0x190c
+  __TEXT.__cstring: 0xf7e6
+  __TEXT.__unwind_info: 0x1e90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1288
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29a8
+  __DATA_CONST.__objc_selrefs: 0x29f0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x170
-  __DATA_CONST.__got: 0x1f8
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2b60
-  __AUTH_CONST.__objc_const: 0xad78
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__got: 0x208
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0xb088
   __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0xa50
-  __DATA.__data: 0x10b8
+  __DATA.__objc_ivar: 0xa74
+  __DATA.__data: 0x1128
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__data: 0x1c0

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2734
-  Symbols:   3814
-  CStrings:  2016
+  Functions: 2791
+  Symbols:   3884
+  CStrings:  2038
 
Symbols:
+ +[AAAccessoryUsageEvent supportsSecureCoding]
+ +[AAAccessoryUsageHistoryManager supportsSecureCoding]
+ -[AAAccessoryUsageEvent .cxx_destruct]
+ -[AAAccessoryUsageEvent description]
+ -[AAAccessoryUsageEvent encodeWithCoder:]
+ -[AAAccessoryUsageEvent initWithCoder:]
+ -[AAAccessoryUsageEvent initWithUsed:timestamp:]
+ -[AAAccessoryUsageEvent isUsed]
+ -[AAAccessoryUsageEvent timestamp]
+ -[AAAccessoryUsageHistoryManager .cxx_destruct]
+ -[AAAccessoryUsageHistoryManager _activate]
+ -[AAAccessoryUsageHistoryManager _ensureXPCStarted]
+ -[AAAccessoryUsageHistoryManager _interrupted]
+ -[AAAccessoryUsageHistoryManager _invalidated]
+ -[AAAccessoryUsageHistoryManager _reportError:]
+ -[AAAccessoryUsageHistoryManager activateWithCompletion:]
+ -[AAAccessoryUsageHistoryManager clientID]
+ -[AAAccessoryUsageHistoryManager description]
+ -[AAAccessoryUsageHistoryManager dispatchQueue]
+ -[AAAccessoryUsageHistoryManager encodeWithCoder:]
+ -[AAAccessoryUsageHistoryManager initWithCoder:]
+ -[AAAccessoryUsageHistoryManager init]
+ -[AAAccessoryUsageHistoryManager invalidate]
+ -[AAAccessoryUsageHistoryManager setClientID:]
+ -[AAAccessoryUsageHistoryManager setDispatchQueue:]
+ -[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]
+ _OBJC_CLASS_$_AAAccessoryUsageEvent
+ _OBJC_CLASS_$_AAAccessoryUsageHistoryManager
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_IVAR_$_AAAccessoryUsageEvent._isUsed
+ _OBJC_IVAR_$_AAAccessoryUsageEvent._timestamp
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._activateCalled
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._activateCompletion
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._clientID
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._dispatchQueue
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._invalidateCalled
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._invalidateDone
+ _OBJC_IVAR_$_AAAccessoryUsageHistoryManager._xpcCnx
+ _OBJC_METACLASS_$_AAAccessoryUsageEvent
+ _OBJC_METACLASS_$_AAAccessoryUsageHistoryManager
+ __OBJC_$_CLASS_METHODS_AAAccessoryUsageEvent
+ __OBJC_$_CLASS_METHODS_AAAccessoryUsageHistoryManager
+ __OBJC_$_CLASS_PROP_LIST_AAAccessoryUsageEvent
+ __OBJC_$_CLASS_PROP_LIST_AAAccessoryUsageHistoryManager
+ __OBJC_$_INSTANCE_METHODS_AAAccessoryUsageEvent
+ __OBJC_$_INSTANCE_METHODS_AAAccessoryUsageHistoryManager
+ __OBJC_$_INSTANCE_VARIABLES_AAAccessoryUsageEvent
+ __OBJC_$_INSTANCE_VARIABLES_AAAccessoryUsageHistoryManager
+ __OBJC_$_PROP_LIST_AAAccessoryUsageEvent
+ __OBJC_$_PROP_LIST_AAAccessoryUsageHistoryManager
+ __OBJC_CLASS_PROTOCOLS_$_AAAccessoryUsageEvent
+ __OBJC_CLASS_PROTOCOLS_$_AAAccessoryUsageHistoryManager
+ __OBJC_CLASS_RO_$_AAAccessoryUsageEvent
+ __OBJC_CLASS_RO_$_AAAccessoryUsageHistoryManager
+ __OBJC_METACLASS_RO_$_AAAccessoryUsageEvent
+ __OBJC_METACLASS_RO_$_AAAccessoryUsageHistoryManager
+ ___36-[AAAccessoryUsageEvent description]_block_invoke
+ ___43-[AAAccessoryUsageHistoryManager _activate]_block_invoke
+ ___43-[AAAccessoryUsageHistoryManager _activate]_block_invoke_2
+ ___43-[AAAccessoryUsageHistoryManager _activate]_block_invoke_3
+ ___44-[AAAccessoryUsageHistoryManager invalidate]_block_invoke
+ ___51-[AAAccessoryUsageHistoryManager _ensureXPCStarted]_block_invoke
+ ___51-[AAAccessoryUsageHistoryManager _ensureXPCStarted]_block_invoke_2
+ ___57-[AAAccessoryUsageHistoryManager activateWithCompletion:]_block_invoke
+ ___69-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke
+ ___69-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke_2
+ ___69-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke_3
+ _description.sFormatter
+ _description.sOnce
+ _gLogCategory_AAAccessoryUsageHistoryManager
CStrings:
+ "### Fetch XPC error: %{error}"
+ "### Fetch failed: %{error}"
+ "### Fetch failed: already invalidated"
+ "### Fetch failed: not activated"
+ "-[AAAccessoryUsageHistoryManager _activate]"
+ "-[AAAccessoryUsageHistoryManager _activate]_block_invoke_2"
+ "-[AAAccessoryUsageHistoryManager _activate]_block_invoke_3"
+ "-[AAAccessoryUsageHistoryManager _interrupted]"
+ "-[AAAccessoryUsageHistoryManager _invalidated]"
+ "-[AAAccessoryUsageHistoryManager _reportError:]"
+ "-[AAAccessoryUsageHistoryManager activateWithCompletion:]_block_invoke"
+ "-[AAAccessoryUsageHistoryManager invalidate]_block_invoke"
+ "-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke"
+ "-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke_2"
+ "-[AAAccessoryUsageHistoryManager usageHistoryForInterval:completion:]_block_invoke_3"
+ "AAAccessoryUsageEvent, isUsed %d, timestamp %@"
+ "AAAccessoryUsageHistoryManager"
+ "AAAccessoryUsageHistoryManager, CID 0x%X"
+ "Fetch completed: %zu event(s)"
+ "Fetching usage history for interval %@"
+ "ts"
+ "used"
+ "yyyy-MM-dd HH:mm:ss.SSS ZZZ"
- "%@-Seed-mov"
```
