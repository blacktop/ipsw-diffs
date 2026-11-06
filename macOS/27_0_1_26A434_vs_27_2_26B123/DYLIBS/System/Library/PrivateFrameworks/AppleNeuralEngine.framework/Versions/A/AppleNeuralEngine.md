## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x5fdec
-  __TEXT.__objc_methlist: 0x2c3c
+382.101.2.0.0
+  __TEXT.__text: 0x60684
+  __TEXT.__objc_methlist: 0x2c54
   __TEXT.__const: 0x2c0
-  __TEXT.__oslogstring: 0xbb5f
-  __TEXT.__cstring: 0x3ac1
-  __TEXT.__gcc_except_tab: 0x6bb0
+  __TEXT.__oslogstring: 0xbcba
+  __TEXT.__cstring: 0x3ade
+  __TEXT.__gcc_except_tab: 0x6c28
   __TEXT.__ustring: 0xb76
-  __TEXT.__unwind_info: 0x15a0
+  __TEXT.__unwind_info: 0x15c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1a88
+  __DATA_CONST.__objc_selrefs: 0x1ab0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x128
-  __DATA_CONST.__got: 0x300
-  __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x50a0
+  __DATA_CONST.__got: 0x308
+  __AUTH_CONST.__const: 0xe10
+  __AUTH_CONST.__cfstring: 0x50c0
   __AUTH_CONST.__objc_const: 0x3d88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x460
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x720
-  __DATA.__bss: 0x188
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA.__data: 0x728
+  __DATA.__bss: 0x1a8
+  __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1806
-  Symbols:   3013
-  CStrings:  1493
+  Functions: 1810
+  Symbols:   3031
+  CStrings:  1499
 
Symbols:
+ +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:]
+ +[_ANEVirtualClient assetTransferLockForUUID:]
+ -[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table137
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table190
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table204
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table88
+ GCC_except_table93
+ GCC_except_table94
+ _OBJC_CLASS_$_NSLock
+ __75-[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:]_block_invoke
+ __75-[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:]_block_invoke_2
+ __ZZ46+[_ANEVirtualClient assetTransferLockForUUID:]E10locksGuard
+ __ZZ46+[_ANEVirtualClient assetTransferLockForUUID:]E5locks
+ __ZZ46+[_ANEVirtualClient assetTransferLockForUUID:]E9onceToken
+ ___46+[_ANEVirtualClient assetTransferLockForUUID:]_block_invoke
+ ___75-[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:]_block_invoke
+ ___75-[_ANEVirtualClient transferAssetsToHostAtPathUnlocked:withUUID:modelType:]_block_invoke_2
+ _kANEFModelMutableClusterIndexKey
+ _mach_timebase_info
+ _objc_msgSend$assetTransferLockForUUID:
+ _objc_msgSend$lock
+ _objc_msgSend$transferAssetsToHostAtPathUnlocked:withUUID:modelType:
+ _objc_msgSend$tryLock
+ _objc_msgSend$unlock
+ _proc_pid_rusage
+ cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:.s_tb
- +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:]
- GCC_except_table110
- GCC_except_table111
- GCC_except_table115
- GCC_except_table116
- GCC_except_table117
- GCC_except_table122
- GCC_except_table123
- GCC_except_table131
- GCC_except_table132
- GCC_except_table133
- GCC_except_table140
- GCC_except_table161
- GCC_except_table162
- GCC_except_table163
- GCC_except_table180
- GCC_except_table187
- GCC_except_table191
- GCC_except_table192
- GCC_except_table193
- GCC_except_table201
- GCC_except_table51
- GCC_except_table56
- GCC_except_table57
- GCC_except_table62
- GCC_except_table69
- GCC_except_table71
- GCC_except_table85
- GCC_except_table86
- GCC_except_table90
- GCC_except_table91
- GCC_except_table95
- GCC_except_table96
- GCC_except_table97
- __67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke
- __67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke_2
- ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke
- ___67-[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:]_block_invoke_2
CStrings:
+ "%@: Created shared IOSurface with ioSID=%u (size=%u) for all file transfers at path=%@"
+ "%@: copyfile DONE useClone=%d flags=0x%x elapsed_ms=%llu bytes_written=%llu src=%s"
+ "%@: createDirectoryAtPath ok=%d elapsed_ms=%llu path=%@"
+ "%@: removeItemAtPath existed=%d ok=%d elapsed_ms=%llu path=%@"
+ "%@: waiting for in-flight transfer of assetTransferUUID=%@"
+ "ANEFModelMutableClusterIndex"
```
