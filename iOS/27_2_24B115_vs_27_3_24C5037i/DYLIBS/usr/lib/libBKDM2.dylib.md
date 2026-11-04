## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-980.40.13.0.1
-  __TEXT.__text: 0x87f74
+980.60.9.0.0
+  __TEXT.__text: 0x8870c
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0x61d4
+  __TEXT.__objc_methlist: 0x620c
   __TEXT.__const: 0xd802
-  __TEXT.__cstring: 0x83b3
-  __TEXT.__oslogstring: 0x52f6
+  __TEXT.__cstring: 0x8419
+  __TEXT.__oslogstring: 0x534b
   __TEXT.__gcc_except_tab: 0x1a88
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__unwind_info: 0x1a58
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40b8
+  __DATA_CONST.__objc_selrefs: 0x40f0
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x4e8
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__got: 0x4b0
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x6cc0
-  __AUTH_CONST.__objc_const: 0xa490
+  __AUTH_CONST.__cfstring: 0x6d00
+  __AUTH_CONST.__objc_const: 0xa4f0
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xbb4
+  __DATA.__objc_ivar: 0xbc0
   __DATA.__data: 0x884
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x7d0

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3156
-  Symbols:   4582
-  CStrings:  1833
+  - /usr/lib/libtailspin.dylib
+  Functions: 3165
+  Symbols:   4595
+  CStrings:  1840
 
Symbols:
+ +[BLHelper writeTailspinToFile:]
+ -[BioLog logTailspin]
+ -[BiometricKitXPCServerPearl avcMatchSeqTypeFromSecureFaceDetectMatchSeqType:]
+ -[BiometricKitXPCServerPearl avcMatchTriggerFromSecureFaceDetectMatchTrigger:]
+ GCC_except_table240
+ GCC_except_table250
+ GCC_except_table266
+ GCC_except_table270
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table292
+ _OBJC_IVAR_$_BioLog._firstFrameLogged
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectMatchSeqType
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectMatchTrigger
+ _TSPDumpOptions_Symbolicate
+ ___21-[BioLog logTailspin]_block_invoke
+ _close
+ _open
+ _tailspin_dump_output_with_options_sync
+ _unlink
- GCC_except_table238
- GCC_except_table248
- GCC_except_table264
- GCC_except_table268
- GCC_except_table271
- GCC_except_table274
- GCC_except_table280
- GCC_except_table281
- GCC_except_table287
- GCC_except_table290
CStrings:
+ "(void *)fidLog - data.bytes + sizeof(*fidLog) <= data.length"
+ "(void *)fidLog >= data.bytes"
+ ".tailspin"
+ "fidLog"
+ "fidLog->length <= sizeof(fidLog->data)"
+ "fidLog->length > 0"
+ "logTailspin > %@\n"
+ "logTailspin not captured\n"
+ "processSecureFaceDetectRequestMessage: start:<%{public}@> sequenceNumber:%u matchRetryType:%u periocularMatchState:0x%x matchTrigger:%u predictedMatchSeqType:%u\n"
+ "seq-%05d%@"
- "fidLogPtr - data.bytes + fidLogSize <= data.length"
- "fidLogPtr >= data.bytes"
- "processSecureFaceDetectRequestMessage: start:<%{public}@> sequenceNumber:%u matchRetryType:%u periocularMatchState:0x%x\n"
```
