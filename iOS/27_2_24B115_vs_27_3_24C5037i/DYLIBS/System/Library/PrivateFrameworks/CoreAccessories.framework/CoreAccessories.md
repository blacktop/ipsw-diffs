## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1219.42.3.0.0
-  __TEXT.__text: 0x26e1c
-  __TEXT.__objc_methlist: 0x19e4
+1219.60.10.0.0
+  __TEXT.__text: 0x28ed4
+  __TEXT.__objc_methlist: 0x1a64
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x3e08
-  __TEXT.__oslogstring: 0x4235
+  __TEXT.__cstring: 0x4250
+  __TEXT.__oslogstring: 0x4326
   __TEXT.__gcc_except_tab: 0x820
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__unwind_info: 0xd70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2078
+  __DATA_CONST.__const: 0x21c8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf70
+  __DATA_CONST.__objc_selrefs: 0xfa8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__got: 0x148
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x3c40
-  __AUTH_CONST.__objc_const: 0x23a0
+  __AUTH_CONST.__cfstring: 0x3c80
+  __AUTH_CONST.__objc_const: 0x23c8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 839
-  Symbols:   1912
-  CStrings:  885
+  Functions: 870
+  Symbols:   1942
+  CStrings:  910
 
Symbols:
+ -[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]
+ -[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]
+ -[ACCHWComponentAuth displayAuthRefreshAccessState:completionHandler:]
+ -[ACCHWComponentAuth displayAuthUserNVMRead:key:completionHandler:]
+ -[ACCHWComponentAuth displayAuthUserNVMWrite:key:value:completionHandler:]
+ _OBJC_CLASS_$_NSError
+ ___64-[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]_block_invoke
+ ___64-[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]_block_invoke_2
+ ___67-[ACCHWComponentAuth displayAuthUserNVMRead:key:completionHandler:]_block_invoke
+ ___67-[ACCHWComponentAuth displayAuthUserNVMRead:key:completionHandler:]_block_invoke_2
+ ___70-[ACCHWComponentAuth displayAuthRefreshAccessState:completionHandler:]_block_invoke
+ ___70-[ACCHWComponentAuth displayAuthRefreshAccessState:completionHandler:]_block_invoke_2
+ ___74-[ACCHWComponentAuth displayAuthUserNVMWrite:key:value:completionHandler:]_block_invoke
+ ___74-[ACCHWComponentAuth displayAuthUserNVMWrite:key:value:completionHandler:]_block_invoke_2
+ ___91-[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]_block_invoke
+ ___91-[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v28?0Q8B16"NSError"20ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_58_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_66_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _kACCProperties_Endpoint_NFC_ShowEdgeCompensationAlert
+ _kCFACCProperties_Endpoint_NFC_ShowEdgeCompensationAlert
CStrings:
+ "%s"
+ "%s: authError %@"
+ "%s: can't invoke remote object %@"
+ "%s: no completion handler"
+ "%s: sessionRef:%d authError %@"
+ "%s: timed out"
+ "-[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]"
+ "-[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]_block_invoke"
+ "-[ACCHWComponentAuth displayAuthCloseSession:completionHandler:]_block_invoke_2"
+ "-[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]"
+ "-[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]_block_invoke"
+ "-[ACCHWComponentAuth displayAuthOpenSession:intermediateCertificate:key:completionHandler:]_block_invoke_2"
+ "-[ACCHWComponentAuth displayAuthRefreshAccessState:completionHandler:]"
+ "-[ACCHWComponentAuth displayAuthRefreshAccessState:completionHandler:]_block_invoke"
+ "-[ACCHWComponentAuth displayAuthUserNVMRead:key:completionHandler:]"
+ "-[ACCHWComponentAuth displayAuthUserNVMRead:key:completionHandler:]_block_invoke"
+ "-[ACCHWComponentAuth displayAuthUserNVMWrite:key:value:completionHandler:]"
+ "-[ACCHWComponentAuth displayAuthUserNVMWrite:key:value:completionHandler:]_block_invoke"
+ "ACCHWComponentAuth"
+ "NFC_ShowEdgeCompensationAlert"
+ "displayAuthRefreshAccessState authError %@"
+ "displayAuthUserNVMRead authError %@"
+ "displayAuthUserNVMWrite authError %@"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v28@?0Q8B16@\"NSError\"20"
```
