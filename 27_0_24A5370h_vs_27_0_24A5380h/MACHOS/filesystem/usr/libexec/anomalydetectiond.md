## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-  __TEXT.__text: 0x36b4ac
-  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__text: 0x36d0e4
+  __TEXT.__auth_stubs: 0x1840
   __TEXT.__objc_stubs: 0x9480
   __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x10438
-  __TEXT.__const: 0xfaae
-  __TEXT.__cstring: 0x1c836
-  __TEXT.__oslogstring: 0x11809
+  __TEXT.__gcc_except_tab: 0x10470
+  __TEXT.__const: 0xfaee
+  __TEXT.__cstring: 0x1c8dd
+  __TEXT.__oslogstring: 0x118e6
   __TEXT.__objc_classname: 0x1070
   __TEXT.__objc_methtype: 0x5f66
   __TEXT.__objc_methname: 0xc218
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc730
+  __TEXT.__unwind_info: 0xc7a8
   __TEXT.__eh_frame: 0x670
-  __DATA_CONST.__const: 0x27450
+  __DATA_CONST.__const: 0x27530
   __DATA_CONST.__cfstring: 0x6a40
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0xc78
-  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__got: 0x678
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x10660
   __DATA.__objc_selrefs: 0x3050

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 17112
-  Symbols:   616
-  CStrings:  10279
+  Functions: 17147
+  Symbols:   608
+  CStrings:  10295
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- __ZN6motion19AnomalyFMEmbeddings7predictERKNSt3__13mapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_2fm9ArrayDataENS1_4lessIS8_EENS6_INS1_4pairIKS8_SA_EEEEEENS1_8functionIFvNS1_10shared_ptrIKNS9_16PredictionResultEEEEEE
- __ZN6motion19AnomalyFMEmbeddingsC1EPU28objcproto17OS_dispatch_queue8NSObject
- __ZNSt3__118condition_variable10notify_oneEv
- __ZNSt3__118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
- __ZNSt3__118condition_variableD1Ev
- __ZNSt3__15mutex4lockEv
- __ZNSt3__15mutex6unlockEv
- __ZNSt3__15mutexD1Ev
CStrings:
+ "AnomalyFM_adaptor"
+ "[%s] Error encountered when running adaptor: %s"
+ "[%s] adaptor timed out"
+ "[%s] base model timed out"
+ "[%s] dump adaptor input: [%s]"
+ "[%s] dump base model input: [%s]"
+ "[%s] response_arrays size: %zu"
+ "accelBias0"
+ "accelBias1"
+ "buttonPress"
+ "ch < kColsInBaseModel"
+ "com.apple.fm.coremotion.anomalyfm.sideload.adapter"
+ "com.apple.fm.coremotion.anomalyfm.sideload.base"
+ "deltaPositionAltimeterZ"
+ "down"
+ "dumpBaseModelRow"
+ "invalid channel"
+ "usage"
+ "usagePage"
+ "yOffset"
+ "{\"msg%{public}.0s\":\"invalid channel\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "[%s] Error encountered when running transit model %s"
- "[%s] dump adapter input': [%s]"
- "[%s] result_arrays size: %zu"
- "com.apple.fm.coremotion.anomalyfm"
- "com.apple.fm.coremotion.anomalyfm.adaptor"

```
