## com.apple.security.BootPolicy

> `com.apple.security.BootPolicy`

```diff

-265.80.1.0.0
+265.100.17.0.0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x173a
-  __TEXT_EXEC.__text: 0x256c
+  __TEXT.__cstring: 0x173c
+  __TEXT_EXEC.__text: 0x25cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x14a8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: CB221B55-D712-3BD9-8FDA-EEBEDB90CCBF
+  UUID: 8BFEDD6D-2BE9-3EC0-92C4-9F9FD22B3390
   Functions: 45
   Symbols:   421
   CStrings:  56
Functions:
~ __ZN20BootPolicyUserClient4freeEv : 28 -> 32
~ __ZN20BootPolicyUserClient14externalMethodEjP31IOExternalMethodArgumentsOpaque : 72 -> 92
~ __ZN20BootPolicyUserClient18validateSEPCommandEP18IOMemoryDescriptorP24BootPolicyCommandContext : 728 -> 732
~ __ZN10BootPolicy14sendSEPCommandEhiPvmS0_Pjb : 824 -> 872
~ __ZN10BootPolicy18setPowerStateGatedEPm -> __ZN10BootPolicy8lockItemEPjj : 280 -> 268
~ __ZN10BootPolicy8lockItemEPjj -> __ZN10BootPolicy10unlockItemEPj : 268 -> 152
~ __ZN10BootPolicy10unlockItemEPj -> __ZN10BootPolicy16handleSEPMessageEPvS0_ : 160 -> 312
~ __ZN10BootPolicy16handleSEPMessageEPvS0_ -> __ZN10BootPolicy17readFromSEPBufferEPvm : 312 -> 356
~ __ZN10BootPolicy16writeToSEPBufferEPvm -> __ZN10BootPolicy14sendSEPMessageEPvhit : 356 -> 192
~ __ZN10BootPolicy14sendSEPMessageEPvhit -> __ZN10BootPolicy14getSEPEndpointEv : 192 -> 1160
~ __ZN10BootPolicy14getSEPEndpointEv -> __ZN10BootPolicy9MetaClassD0Ev : 1144 -> 8
~ __ZN10BootPolicy9MetaClassD0Ev -> _GLOBAL__sub_I_BootPolicy.cpp : 8 -> 80
~ _GLOBAL__sub_I_BootPolicy.cpp -> __GLOBAL__D_a : 80 -> 16
~ __GLOBAL__D_a -> __start : 16 -> 36
~ __stop -> __ZN10BootPolicy18setPowerStateGatedEPm : 36 -> 292
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/BootPolicy_kext/kext/BootPolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/BootPolicy_kext/kext/BootPolicyUserClient.cpp"
+ "nullptr != cmd"
+ "nullptr != input"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/BootPolicy_kext/kext/BootPolicy.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/BootPolicy_kext/kext/BootPolicyUserClient.cpp"
- "__null != cmd"
- "__null != input"

```
