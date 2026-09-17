## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/Versions/A/AppleNeuralEngine`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x5eda0
+382.100.0.0.0
+  __TEXT.__text: 0x5f1d8
   __TEXT.__objc_methlist: 0x2c3c
   __TEXT.__const: 0x2c0
-  __TEXT.__oslogstring: 0xbb5f
-  __TEXT.__cstring: 0x3ac1
+  __TEXT.__oslogstring: 0xbc28
+  __TEXT.__cstring: 0x3ade
   __TEXT.__gcc_except_tab: 0x6bb0
   __TEXT.__ustring: 0xb76
   __TEXT.__unwind_info: 0x1e00

   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x300
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x50a0
+  __AUTH_CONST.__cfstring: 0x50c0
   __AUTH_CONST.__objc_const: 0x3d88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x720
+  __DATA.__data: 0x728
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   Functions: 1806
-  Symbols:   3013
-  CStrings:  1493
+  Symbols:   3017
+  CStrings:  1497
 
Symbols:
+ +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:]
+ _kANEFModelMutableClusterIndexKey
+ _mach_timebase_info
+ _proc_pid_rusage
+ cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:.s_tb
- +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:]
Functions:
~ +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:] -> +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:] : 2564 -> 3644
CStrings:
+ "%@: copyfile DONE useClone=%d flags=0x%x elapsed_ms=%llu bytes_written=%llu src=%s"
+ "%@: createDirectoryAtPath ok=%d elapsed_ms=%llu path=%@"
+ "%@: removeItemAtPath existed=%d ok=%d elapsed_ms=%llu path=%@"
+ "ANEFModelMutableClusterIndex"
```
