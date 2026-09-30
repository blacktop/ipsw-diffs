## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-1084.40.3.0.1
-  __TEXT.__text: 0x785e8
-  __TEXT.__objc_methlist: 0x63fc
+1084.40.6.0.0
+  __TEXT.__text: 0x789d0
+  __TEXT.__objc_methlist: 0x640c
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x7d45
+  __TEXT.__cstring: 0x7d46
   __TEXT.__oslogstring: 0xba9e
-  __TEXT.__gcc_except_tab: 0xb84
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__unwind_info: 0x25a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x178
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f40
+  __DATA_CONST.__objc_selrefs: 0x2f50
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x770
   __DATA_CONST.__got: 0x7a0
   __AUTH_CONST.__const: 0x640
   __AUTH_CONST.__cfstring: 0x6c60
-  __AUTH_CONST.__objc_const: 0xdb70
+  __AUTH_CONST.__objc_const: 0xdbb0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xa58
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0xa60
+  __DATA.__objc_ivar: 0xa68
   __DATA.__data: 0x1388
   __DATA_DIRTY.__objc_data: 0x2210
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2825
-  Symbols:   6219
+  Functions: 2826
+  Symbols:   6225
   CStrings:  1860
 
Symbols:
+ -[RBProcessMonitorObserver _lock_shouldSendState:forHandle:]
+ GCC_except_table27
+ GCC_except_table31
+ _OBJC_IVAR_$_RBProcessMonitorObserver._hasVisibilityOnlyConfig
+ _OBJC_IVAR_$_RBProcessMonitorObserver._lastVisibleByIdentity
+ _objc_msgSend$_lock_shouldSendState:forHandle:
+ _objc_msgSend$wantsVisibilityChangesOnly
- GCC_except_table26
Functions:
~ ___66-[RBProcessMonitorObserver processMonitor:didChangeProcessStates:]_block_invoke : 824 -> 984
~ -[RBProcessMonitorObserver _lock_addConfigurationStatesToPending:] : 708 -> 828
~ -[RBProcessMonitorObserver _lock_rebuildConfiguration] : 492 -> 540
~ -[RBProcessMonitorObserver initWithMonitor:forProcess:connection:] : 416 -> 440
~ -[RBProcessMonitorObserver .cxx_destruct] : 148 -> 160
~ -[RBProcessMonitorObserver invalidate] : 112 -> 120
+ -[RBProcessMonitorObserver _lock_shouldSendState:forHandle:]
```
