## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x5881c
+382.100.2.0.0
+  __TEXT.__text: 0x58d10
   __TEXT.__objc_methlist: 0x2c3c
   __TEXT.__const: 0x2b8
-  __TEXT.__oslogstring: 0xba7b
-  __TEXT.__cstring: 0x3a7f
-  __TEXT.__gcc_except_tab: 0x6b7c
+  __TEXT.__oslogstring: 0xbb9b
+  __TEXT.__cstring: 0x3a9c
+  __TEXT.__gcc_except_tab: 0x6b8c
   __TEXT.__ustring: 0xb76
   __TEXT.__unwind_info: 0x1de0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x5060
+  __AUTH_CONST.__cfstring: 0x5080
   __AUTH_CONST.__objc_const: 0x3d88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x23c
-  __DATA.__data: 0x720
+  __DATA.__data: 0x728
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
   Functions: 1751
-  Symbols:   2945
-  CStrings:  1487
+  Symbols:   2949
+  CStrings:  1492
 
Symbols:
+ +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:]
+ _cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:.s_tb
+ _kANEFModelMutableClusterIndexKey
+ _mach_timebase_info
+ _proc_pid_rusage
- +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:]
Functions:
~ -[_ANEVirtualClient transferAssetsToHostAtPath:withUUID:modelType:] : 2788 -> 3004
~ +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:] -> +[_ANECloneHelper cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:] : 2400 -> 3452
CStrings:
+ "%@: Created shared IOSurface with ioSID=%u (size=%u) for all file transfers at path=%@"
+ "%@: copyfile DONE useClone=%d flags=0x%x elapsed_ms=%llu bytes_written=%llu src=%s"
+ "%@: createDirectoryAtPath ok=%d elapsed_ms=%llu path=%@"
+ "%@: removeItemAtPath existed=%d ok=%d elapsed_ms=%llu path=%@"
+ "ANEFModelMutableClusterIndex"
```
