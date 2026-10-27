## com.apple.driver.AppleMultitouchDriver

> `com.apple.driver.AppleMultitouchDriver`

```diff

-10400.44.0.0.0
+10410.4.0.0.0
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x1e89
-  __TEXT.__os_log: 0x3400
-  __TEXT_EXEC.__text: 0x1ad38
-  __TEXT_EXEC.__auth_stubs: 0x630
+  __TEXT.__cstring: 0x1e88
+  __TEXT.__os_log: 0x345f
+  __TEXT_EXEC.__text: 0x1ae30
+  __TEXT_EXEC.__auth_stubs: 0x610
   __DATA.__data: 0xca
   __DATA.__common: 0x1d0
   __DATA.__bss: 0x11

   __DATA_CONST.__const: 0x55c0
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__kalloc_type: 0x7c0
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x118
   Functions: 524
   Symbols:   1394
-  CStrings:  476
+  CStrings:  477
 
Symbols:
+ __ZN24IOBufferMemoryDescriptor17inTaskWithOptionsEP4taskjmm
+ __ZZN31AppleMultitouchDeviceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptorE11_os_log_fmt_0
+ _kernel_task
- _IOFreeAligned
- _IOMallocAligned
- __ZN18IOMemoryDescriptor11withAddressEPvyj
Functions:
~ __ZN31AppleMultitouchDeviceUserClientD2Ev : 204 -> 244
~ __ZN31AppleMultitouchDeviceUserClientD1Ev : 204 -> 244
~ __ZNK31AppleMultitouchDeviceUserClient9MetaClass5allocEv : 120 -> 56
~ __ZN31AppleMultitouchDeviceUserClientC1Ev : 104 -> 8
~ __ZN31AppleMultitouchDeviceUserClient11injectFrameEi : 376 -> 460
~ __ZN31AppleMultitouchDeviceUserClient12initWithTaskEP4taskPvjP12OSDictionary : 464 -> 500
~ __ZN31AppleMultitouchDeviceUserClient4freeEv : 232 -> 252
~ __ZN31AppleMultitouchDeviceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 464 -> 652
CStrings:
+ "12111112122212121111111111111222222222111111122"
+ "[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _injectionMemory in clientMemoryForType\n"
- "121111121222121211111111111112222222221111112122"
```
