## libGPUCompilerUtils.dylib

> `/System/Library/PrivateFrameworks/GPUCompiler.framework/Libraries/libGPUCompilerUtils.dylib`

```diff

-32023.864.0.0.0
-  __TEXT.__text: 0x4c44
+32023.878.0.0.0
+  __TEXT.__text: 0x4e98
   __TEXT.__auth_stubs: 0xd0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x15
+  __TEXT.__cstring: 0xd52
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__auth_got: 0x68
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 167D5204-1F05-3627-B102-476CF2C9F324
+  UUID: ECD3F966-CCA1-3639-8E7C-20EB67136E1E
   Functions: 20
   Symbols:   22
-  CStrings:  1
+  CStrings:  10
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _memset_pattern16
Functions:
~ _MTLGPUCompilerHashFunctionScript -> sub_25678c108 : 960 -> 1880
~ sub_2517ac518 -> _MTLGPUCompilerHashFragmentPipelineScript : 1860 -> 168
~ _MTLGPUCompilerHashComputePipelineScript -> sub_25678c908 : 168 -> 988
~ sub_2517acd04 -> _MTLGPUCompilerHashFunctionScript : 988 -> 960
~ _MTLGPUCompilerHashMeshPipelineScript -> sub_25678d1f4 : 168 -> 848
~ _MTLGPUCompilerHashFragmentPipelineScript -> sub_25678d544 : 168 -> 188
~ sub_2517ad380 -> sub_25678d600 : 856 -> 2976
~ sub_2517ad6d8 -> _MTLGPUCompilerTimeStamp : 188 -> 12
~ sub_2517ad794 -> _MTLGPUCompilerHashObjectPipelineScript : 16 -> 168
~ sub_2517ad7a4 -> _MTLGPUCompilerHashMeshPipelineScript : 2676 -> 168
~ sub_2517ae594 -> sub_25678e678 : 492 -> 488
~ sub_2517ae780 -> sub_25678e860 : 6564 -> 6856
~ sub_2517b0470 -> sub_256790674 : 2336 -> 2332
~ _MTLGPUCompilerTimeStamp -> sub_256790f90 : 12 -> 16
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9EugA6yGv3xZYDJvktpbPUObMWILu_B867_wQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "Jan 30 2026 21:43:46"
- "Jan 27 2026 22:28:13"

```
