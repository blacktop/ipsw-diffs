## com.apple.driver.AppleConvergedIPCOLYBTControl

> `com.apple.driver.AppleConvergedIPCOLYBTControl`

```diff

-110.0.0.0.0
-  __TEXT.__cstring: 0x7fae
+126.0.0.0.0
+  __TEXT.__cstring: 0x8008
   __TEXT.__const: 0x90
-  __TEXT_EXEC.__text: 0x488c0
+  __TEXT_EXEC.__text: 0x49184
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
-  __DATA_CONST.__const: 0x7268
+  __DATA_CONST.__const: 0x7298
   __DATA_CONST.__kalloc_type: 0xc40
   __DATA_CONST.__kalloc_var: 0x500
-  UUID: BFCCB93A-E3B7-3FDA-A494-9DCCB88200C4
-  Functions: 974
-  Symbols:   1724
-  CStrings:  998
+  UUID: 34E0C594-B41D-3B86-A88B-C7ED7C59B767
+  Functions: 968
+  Symbols:   1727
+  CStrings:  1001
 
Symbols:
+ __ZN14ACIPCBTIDevice21isMMIOCoreDumpAllowedEv
+ __ZN17ACIPCOLYBTControl20dumpPMNIIDMRegistersEb
+ __ZN23AppleConvergedIPCDevice21isMMIOCoreDumpAllowedEv
+ __ZN24AppleConvergedIPCControl13setFatalErrorEb
+ __ZN24AppleConvergedIPCControl21isMMIOCoreDumpAllowedEv
+ __ZN26AppleConvergedIPCBTIDevice21isMMIOCoreDumpAllowedEv
- _ZN14ACIPCRTIDevice19publishSharedMemoryEP26acipcRTISharedMemoryParams.cold.1
- _ZN29AppleConvergedIPCOLYBTControl14publishOTPDataEv.cold.4
- __ZN17ACIPCOLYBTControl20dumpPMNIIDMRegistersEv
CStrings:
+ "%s::%s: MMIO coredump not allowed\n"
+ "%s::%s: _imageSent %u _state %s\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"
+ "isMMIOCoreDumpAllowed"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCDevice.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCBTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCOLYBTControlReporter.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/OLYBT/AppleConvergedIPCRTIInterface.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTCoreDumpProvider.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCOLYBTDebug/AppleConvergedIPCOLYBTLogProvider.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCBTIPipe.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCOLYBTControl.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIDevice.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/ACIPCRTIPipe.cpp"

```
