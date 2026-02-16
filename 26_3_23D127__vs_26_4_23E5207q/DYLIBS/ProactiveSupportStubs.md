## ProactiveSupportStubs

> `/System/Library/PrivateFrameworks/ProactiveSupportStubs.framework/ProactiveSupportStubs`

```diff

-415.1.0.0.0
-  __TEXT.__text: 0xd54
+418.0.0.0.0
+  __TEXT.__text: 0xdb0
   __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__gcc_except_tab: 0x168
   __TEXT.__cstring: 0x57
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x14

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 462D7DDD-56A2-33F5-B6DB-60459CEBF111
+  UUID: DD7CD562-A836-3730-AC45-A0247C96B098
   Functions: 19
   Symbols:   113
   CStrings:  29
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[_PASDeviceStateStub setCurrentOsBuild:] : 112 -> 116
~ +[_PASDeviceStateStub setDeviceFormattedForProtection:] : 100 -> 104
~ +[_PASDeviceStateStub setLockStateAKS:] : 392 -> 400
~ +[_PASDeviceStateStub setClassCLocked:] : 172 -> 176
~ +[_PASDeviceStateStub setLockState:] : 372 -> 380
~ +[_PASDeviceStateStub stopMockingSystem] : 168 -> 172
~ +[_PASDeviceStateStub startMockingSystem] : 248 -> 252
~ _registerOnceForFirstUnlock : 152 -> 156
~ _unregisterForAKSEvents : 184 -> 192
~ _registerForAKSEvents : 232 -> 236
~ _unregisterForLockStateChangesForDevice : 140 -> 144
~ _registerForLockStateChangesForDevice : 232 -> 236
~ _unregisterForLockStateChanges : 140 -> 144
~ _registerForLockStateChanges : 232 -> 236
~ _currentOsBuild : 228 -> 236
~ _deviceLockState : 76 -> 80
~ _lockState : 76 -> 80
~ _formattedForContentProtection : 76 -> 80
~ _unlockedSinceBoot : 80 -> 84

```
