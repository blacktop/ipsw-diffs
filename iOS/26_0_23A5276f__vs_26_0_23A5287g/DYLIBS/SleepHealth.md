## SleepHealth

> `/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth`

```diff

-6087.1.2.1.0
+6093.0.0.0.0
   __TEXT.__text: 0x5358
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x62c

   __TEXT.__cstring: 0x83c
   __TEXT.__gcc_except_tab: 0x124
   __TEXT.__oslogstring: 0x36c
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x14e
   __TEXT.__objc_methname: 0x1e33
   __TEXT.__objc_methtype: 0x3d1

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 167C8266-710E-33D1-8E70-2DAF1F71AD80
+  UUID: AABC035F-4F86-3342-A7BA-F557ADAC0E16
   Functions: 106
   Symbols:   630
   CStrings:  484
Functions:
~ _HDSleepHealthDaemonPluginServerInterface -> +[HKSleepHealthStore taskIdentifier] : 172 -> 40
~ -[HKSleepHealthStore remoteInterface] -> _HKSleepHealthStoreInterface : 4 -> 20
~ _HKSleepHealthStoreInterface -> _HDSleepHealthDaemonPluginServerInterface : 20 -> 172
~ +[HKSleepHealthStore taskIdentifier] -> -[HKSleepHealthStore remoteInterface] : 40 -> 4

```
