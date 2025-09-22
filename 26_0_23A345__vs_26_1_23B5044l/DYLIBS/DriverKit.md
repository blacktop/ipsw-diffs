## DriverKit

> `/System/Library/Frameworks/DriverKit.framework/DriverKit`

```diff

-445.0.0.0.0
-  __TEXT.__text: 0x36590
+451.0.0.0.0
+  __TEXT.__text: 0x367a0
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x5d44
-  __TEXT.__cstring: 0x2e46
+  __TEXT.__cstring: 0x2e7d
   __TEXT.__oslogstring: 0xe
   __TEXT.__unwind_info: 0x190
   __DATA_CONST.__got: 0x48

   __AUTH_CONST.__const: 0x5698
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x170
-  __DATA.__bss: 0x438
+  __DATA.__bss: 0x440
   __DATA_DIRTY.__common: 0x300
   __DATA_DIRTY.__bss: 0x1008
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 2F6E13B6-724D-348E-BC0E-A095CA502043
+  UUID: C5496F7D-B60A-3EB7-B615-F57BBECF2B29
   Functions: 1528
-  Symbols:   2926
-  CStrings:  468
+  Symbols:   2927
+  CStrings:  470
 
Symbols:
+ __ZL7gServer
+ ____ZL8LockTesti_block_invoke.221
+ ____ZL8LockTesti_block_invoke.225
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.161
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.248
+ ___block_descriptor_tmp.249
- ____ZL8LockTesti_block_invoke.219
- ____ZL8LockTesti_block_invoke.223
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.196
- ___block_descriptor_tmp.217
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.246
- ___block_descriptor_tmp.247
Functions:
~ __ZL16OSObjectAllocateP11OSMetaClasstPP8OSObject : 420 -> 448
~ __Z12OSObjectFreeP15OSMetaClassBase : 532 -> 560
~ __ZL15OSCopyInObjectsP18IOUserServer_IVarsP16IORPCMessageMachP12IORPCMessageb : 440 -> 448
~ _IOUserServerMain : 1532 -> 1576
~ __ZN9IOService4freeEv : 72 -> 180
~ __ZN35IOServiceNotificationDispatchSource4initEv : 68 -> 84
~ __ZThn24_N35IOServiceNotificationDispatchSource4initEv : 72 -> 88
~ __ZN35IOServiceNotificationDispatchSource4freeEv : 72 -> 136
~ ____ZN35IOServiceNotificationDispatchSource20DeliverNotificationsEU13block_pointerFvyP9IOServiceyE_block_invoke : 256 -> 372
~ __ZN9IOService4initEv : 152 -> 240
~ ____ZN9IOService9Stop_ImplEPS__block_invoke : 224 -> 236
CStrings:
+ "CopyNextNotification ret 0x%x\n"
+ "ret == kIOReturnSuccess"

```
