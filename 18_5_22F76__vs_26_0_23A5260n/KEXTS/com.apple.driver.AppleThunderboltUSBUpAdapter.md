## com.apple.driver.AppleThunderboltUSBUpAdapter

> `com.apple.driver.AppleThunderboltUSBUpAdapter`

```diff

-124.0.0.0.0
-  __TEXT.__cstring: 0x15cf
-  __TEXT.__os_log: 0x1234
-  __TEXT_EXEC.__text: 0x87d4
+128.0.0.0.0
+  __TEXT.__cstring: 0x1902
+  __TEXT.__os_log: 0x1605
+  __TEXT_EXEC.__text: 0x9bb8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x780
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 59894A9B-01AD-30C1-8408-6FC9E7D6CF41
-  Functions: 55
+  UUID: 603B3108-8541-3CB7-8945-514B2513571F
+  Functions: 56
   Symbols:   0
-  CStrings:  127
+  CStrings:  141
 
Functions:
~ __ZN28AppleThunderboltUSBUpAdapter5startEP9IOService : 5616 -> 8032
~ __ZN28AppleThunderboltUSBUpAdapter8finalizeEj : 964 -> 1184
~ __ZN28AppleThunderboltUSBUpAdapter13activateAsyncEv : 748 -> 1960
~ __ZN28AppleThunderboltUSBUpAdapter12activateSyncEv : 812 -> 816
~ __ZN28AppleThunderboltUSBUpAdapter16activateInternalEP28IOThunderboltDispatchContext : 4992 -> 5148
~ __ZN28AppleThunderboltUSBUpAdapter12suspendAsyncEv : 748 -> 752
~ __ZN28AppleThunderboltUSBUpAdapter11suspendSyncEv : 812 -> 816
~ __ZN28AppleThunderboltUSBUpAdapter15suspendInternalEP28IOThunderboltDispatchContext : 1096 -> 1100
~ __ZN28AppleThunderboltUSBUpAdapter15deactivateAsyncEv : 748 -> 788
~ __ZN28AppleThunderboltUSBUpAdapter14deactivateSyncEv : 812 -> 816
~ __ZN28AppleThunderboltUSBUpAdapter18deactivateInternalEP28IOThunderboltDispatchContext : 3892 -> 3872
~ __ZN28AppleThunderboltUSBUpAdapter4wakeEv : 320 -> 316
~ __ZN28AppleThunderboltUSBUpAdapter9earlyWakeEv : 872 -> 876
+ __ZN28AppleThunderboltUSBUpAdapter7messageEjP9IOServicePv
CStrings:
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fIsAsleep=0x%d\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d fUpSwitchUSBUpAdapter->fIsPendingActivation=%d\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d status=0x%llx\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateAsync fActivated=%d\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - before setting tunnel source and dest ports, status = 0x%x fUSBDownPort = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fUSBDownPort = %p fUpSwitchUSBUpPort = %p status=0x%llx \n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - our_switch = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - parent_switch = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - up_switch_up_adapter = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_parent_port = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_port = %p\n"
+ "%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x\n"
+ "%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activateAsync\n"
+ "%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling deactivateAsync\n"
+ "121111121222121211122222212111111221122"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync\n"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateAsync\n"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fUSBDownPort = %p"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - our_switch = %p"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - parent_switch = %p"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_parent_port = %p"
- "%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_port = %p"
- "1211111212221212111222222121111221122"

```
