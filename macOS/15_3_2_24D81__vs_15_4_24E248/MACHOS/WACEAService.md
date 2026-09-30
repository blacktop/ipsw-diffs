## WACEAService

> `/System/Library/Frameworks/ExternalAccessory.framework/Versions/A/XPCServices/WACEAService.xpc/Contents/MacOS/WACEAService`

```diff

 453.0.0.0.0
-  __TEXT.__text: 0x1494
-  __TEXT.__auth_stubs: 0x140
+  __TEXT.__text: 0x14dc
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__objc_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0xb0
+  __TEXT.__objc_methlist: 0x6dc
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x10a1
-  __TEXT.__objc_methtype: 0x646
+  __TEXT.__objc_methname: 0x10c6
+  __TEXT.__objc_methtype: 0x67d
   __TEXT.__cstring: 0xca
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xa8
-  __DATA_CONST.__got: 0x20
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x1628
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_const: 0xa50
+  __DATA.__objc_selrefs: 0x490
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x2a8

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9783AB8-AA1E-3FF3-8053-E6D1735B58E8
+  UUID: A5BFC4DA-EA0D-30EC-BA77-0101A34DC8A5
   Functions: 24
-  Symbols:   305
-  CStrings:  233
+  Symbols:   297
+  CStrings:  236
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/ExternalAccessory/install/TempContent/Objects/ExternalAccessory.build/WACEAService.build/Objects-normal/arm64e/WACEAService.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/ExternalAccessory/install/TempContent/Objects/ExternalAccessory.build/WACEAService.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/WACEAService/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/ExternalAccessory/install/TempContent/Objects/ExternalAccessory.build/WACEAService.build/Objects-normal/arm64e/WACEAService.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/ExternalAccessory/install/TempContent/Objects/ExternalAccessory.build/WACEAService.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/WACEAService/
Functions:
~ -[ServiceDelegate listener:shouldAcceptNewConnection:] : 248 -> 256
~ -[WACEAService setup] : 232 -> 236
~ ___21-[WACEAService setup]_block_invoke : 288 -> 328
~ -[WACEAService reconfigureAccessory:withReply:] : 2228 -> 2244
~ ___47-[WACEAService reconfigureAccessory:withReply:]_block_invoke : 168 -> 160
~ __47-[WACEAService reconfigureAccessory:withReply:]_block_invoke.7 : 84 -> 76
~ -[WACEAService startSearchForAccessoriesNeedingReprovisioning] : 104 -> 120
~ -[WACEAService homeManagerDidUpdateHomes:] : 712 -> 728
~ _LoadHomeKit : 124 -> 120
~ ___LoadHomeKit_block_invoke : 100 -> 92
CStrings:
+ "home:didUpdateActionSet:isExecuting:"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v36@0:8@16@24B32"

```
