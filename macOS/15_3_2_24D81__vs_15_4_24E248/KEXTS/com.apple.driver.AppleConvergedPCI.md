## com.apple.driver.AppleConvergedPCI

> `com.apple.driver.AppleConvergedPCI`

```diff

-110.0.0.0.0
+126.0.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7049
-  __TEXT_EXEC.__text: 0x3f7d4
+  __TEXT.__cstring: 0x707c
+  __TEXT_EXEC.__text: 0x40098
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x2d0

   __DATA_CONST.__got: 0x108
   __DATA_CONST.__mod_init_func: 0x68
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x6ea8
+  __DATA_CONST.__const: 0x6eb8
   __DATA_CONST.__kalloc_type: 0x1380
-  UUID: 9C9690EC-8C8C-3D2A-A484-7BB64FB80F4B
-  Functions: 1084
-  Symbols:   1743
-  CStrings:  895
+  UUID: 90846EFF-2EAB-34F5-B4C1-67113D9FD152
+  Functions: 1076
+  Symbols:   1742
+  CStrings:  898
 
Symbols:
+ __ZN24AppleConvergedIPCControl13setFatalErrorEb
+ __ZN24AppleConvergedIPCControl21isMMIOCoreDumpAllowedEv
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2747
+ __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2771
+ __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2788
- _ZN12ACIPCControl11mmioReadOTPEjPhjb.cold.3
- _ZN12ACIPCControl14mmioReadMemoryEPVhPhjb.cold.2
- _ZN23AppleConvergedIPCLogger9logBinaryE13ACIPCLogLevelS0_bPKcS2_PKvjS2_.cold.1
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2738
- __ZZN24AppleConvergedIPCControl16handlePCIMessageEjE21kalloc_type_view_2762
- __ZZN24AppleConvergedIPCControl20pciMessageThreadCallEPvS0_E21kalloc_type_view_2779
CStrings:
+ "%s::%s: setFatalError %u\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4399.cpp"
+ "fatalerror"
+ "setFatalError"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCInterface.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/AppleConvergedIPCLogger.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCIOCommand.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryCommand.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCMemoryPolicy.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/Memory/AppleConvergedIPCRequest.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCControlUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedIPCControl/UserClient/AppleConvergedIPCUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/AppleConvergedPCI/AppleConvergedPCI.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCChip.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCControl.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/ACIPCPort.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4388.cpp"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleConvergedIPC/Core/OLYBT/Chips/ACIPCChip4399.cpp"

```
