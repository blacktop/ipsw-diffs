## LegacyHandle

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/LegacyHandle.framework/LegacyHandle`

```diff

-2205.3.1.0.0
-  __TEXT.__text: 0x72c sha256:a20e193d3cdbc3b7ff21f9a53c02ca57972ceecd1bd931bf7daf9e08fb69ed1d
-  __TEXT.__auth_stubs: 0xb0 sha256:079d8735d4bd17120bcf9810a2b7ed028347a0f0abcc5b90367202dfc9d995e1
+2235.48.1.0.0
+  __TEXT.__text: 0x760 sha256:480933c932a9bf896afc1d877cdec7c01811934d1a6922d25812048619cb1b24
   __TEXT.__const: 0x40 sha256:c3534644460ec67efdccf7f4b13b3ea6d04bd6afcb4622f93964b8bdf3c62e3d
-  __TEXT.__unwind_info: 0x70 sha256:3051ca8ad76156a81f2929c03471f159081f8a55d61243502cd8f2b3a6590f2e
-  __AUTH_CONST.__auth_got: 0x58 sha256:10eef285deef7a4b7c82b22aa53589b7833df29de3814649c772bbd5c832f365
+  __TEXT.__unwind_info: 0x78 sha256:5753bdead838eba679484e7640d8a4de4c7bf1e1ac1656520994c26c393bbc6f
+  __TEXT.__auth_stubs: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0xe70 sha256:3a9fd4e62b635f1f7990b7b14f4e0e21b9ec68e3b832f19c43daf1dbe642b75d
   __DATA_DIRTY.__bss: 0x630 sha256:c87499548f9efbd98c824a95a664af38f414efb1c9eede544e55e019473d6b24
   - /usr/lib/libSystem.B.dylib
-  UUID: 0B073F08-2021-3C27-BDD8-7AC6D3D77ACB
+  UUID: 562B1997-3A14-38E0-A4DB-72F34B572526
   Functions: 6
   Symbols:   27
   CStrings:  0
Functions:
~ _CloseAllHandles -> _CheckInHandleDebug : 124 -> 336
~ _CreateHandle -> _CheckOutHandleDebug : 516 -> 588
~ _CheckInHandleDebug -> _CloseAllHandles : 332 -> 124
~ _CheckOutHandleDebug -> _CreateHandle : 560 -> 532
~ _FindHandle : sha256 98f18f7b1713c52151ceff24ba3e9d14e78c44998a341a95108b39a6fb9b042a -> 57d860dd10a9982b01f1cbaeb1dd128175b549cbec45d36cb7f07afde72f4cf0
~ _GetNumHandles : 16 -> 20

```
