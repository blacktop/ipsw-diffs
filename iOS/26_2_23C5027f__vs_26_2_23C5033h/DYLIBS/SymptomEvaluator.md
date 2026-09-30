## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2158.60.2.0.0
-  __TEXT.__text: 0x279910
+2158.60.3.0.0
+  __TEXT.__text: 0x279db0
   __TEXT.__auth_stubs: 0x2c70
-  __TEXT.__objc_methlist: 0x17768
+  __TEXT.__objc_methlist: 0x17788
   __TEXT.__cstring: 0x25199
   __TEXT.__const: 0xf80
-  __TEXT.__oslogstring: 0x4303f
+  __TEXT.__oslogstring: 0x4311f
   __TEXT.__gcc_except_tab: 0x53c4
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x304

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6950
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x6a48
+  __TEXT.__unwind_info: 0x6a50
   __TEXT.__eh_frame: 0x698
-  __TEXT.__objc_classname: 0x1d5b
-  __TEXT.__objc_methname: 0x3c6bf
+  __TEXT.__objc_classname: 0x1d5c
+  __TEXT.__objc_methname: 0x3c741
   __TEXT.__objc_methtype: 0x6c5b
-  __TEXT.__objc_stubs: 0x259e0
+  __TEXT.__objc_stubs: 0x25a00
   __DATA_CONST.__got: 0xf50
   __DATA_CONST.__const: 0x66f0
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca50
+  __DATA_CONST.__objc_selrefs: 0xca68
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x8c0
   __AUTH_CONST.__auth_got: 0x1650
   __AUTH_CONST.__const: 0x2c30
   __AUTH_CONST.__cfstring: 0x1cec0
-  __AUTH_CONST.__objc_const: 0x3c128
+  __AUTH_CONST.__objc_const: 0x3c168
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x938
   __AUTH_CONST.__objc_intobj: 0x840

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x15b0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x2d38
+  __DATA.__objc_ivar: 0x2d40
   __DATA.__data: 0x1e08
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A2A614F4-E77A-3FC4-BA63-BEEB8B279CDC
-  Functions: 11302
-  Symbols:   36469
-  CStrings:  26583
+  UUID: DF6D50A4-89E4-387C-A86D-261875ED0665
+  Functions: 11305
+  Symbols:   36478
+  CStrings:  26592
 
Symbols:
+ -[NetworkAnalyticsEngine _getDNSSeqnoStateDetails]
+ -[NetworkAnalyticsEngine _isOutOfOrderDNSSymptomInEvent:forServer:]
+ -[NetworkAnalyticsEngine _resetDNSSeqnoState]
+ GCC_except_table157
+ GCC_except_table204
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table272
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table331
+ GCC_except_table368
+ GCC_except_table382
+ GCC_except_table393
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._dnsSeqnoByPIDAndServer
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._lastDNSSymptomPID
+ _objc_msgSend$_isOutOfOrderDNSSymptomInEvent:forServer:
- GCC_except_table202
- GCC_except_table237
- GCC_except_table244
- GCC_except_table245
- GCC_except_table246
- GCC_except_table269
- GCC_except_table273
- GCC_except_table274
- GCC_except_table275
- GCC_except_table283
- GCC_except_table284
- GCC_except_table328
- GCC_except_table365
- GCC_except_table379
- GCC_except_table390
CStrings:
+ "Cannot extract eventData from %@"
+ "Event (%@) or server (%@) is nil, returning"
+ "OOO DNS symptom detected [pid %llu, server %{private}@ received seqno %u (expected > %u), diff %d]"
+ "PID changed [%llu -> %llu], cleared old seqno state"
+ "_dnsSeqnoByPIDAndServer"
+ "_getDNSSeqnoStateDetails"
+ "_isOutOfOrderDNSSymptomInEvent:forServer:"
+ "_lastDNSSymptomPID"
+ "_resetDNSSeqnoState"

```
