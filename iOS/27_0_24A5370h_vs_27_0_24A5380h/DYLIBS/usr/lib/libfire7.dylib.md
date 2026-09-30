## libfire7.dylib

> `/usr/lib/libfire7.dylib`

```diff

-  __TEXT.__text: 0x283c78
+  __TEXT.__text: 0x2836f8
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x2cd1c
-  __TEXT.__cstring: 0x3fe95
-  __TEXT.__gcc_except_tab: 0x54f0
-  __TEXT.__unwind_info: 0x5728
+  __TEXT.__cstring: 0x3ffaa
+  __TEXT.__gcc_except_tab: 0x54c8
+  __TEXT.__unwind_info: 0x5718
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x84a0
   __DATA_CONST.__weak_got: 0x8

   __DATA_DIRTY.__bss: 0x9c
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 7336
-  Symbols:   18790
-  CStrings:  6185
+  Functions: 7333
+  Symbols:   18783
+  CStrings:  6193
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ GCC_except_table112
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table202
+ GCC_except_table211
+ GCC_except_table220
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table269
+ __ZN18FireMessageHandler11stopRequestENS_11RequestTypeE
+ __ZN18FireMessageHandler12startRequestENS_11RequestTypeE
- GCC_except_table149
- GCC_except_table158
- GCC_except_table167
- GCC_except_table203
- GCC_except_table212
- GCC_except_table221
- GCC_except_table239
- GCC_except_table245
- GCC_except_table247
- GCC_except_table251
- GCC_except_table272
- __ZN18FireMessageHandler11stopRequestENS_7RequestE
- __ZN18FireMessageHandler12startRequestENS_7RequestEPN7BlueFin9GlRequestE
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIN18FireMessageHandler7RequestEPN7BlueFin9GlRequestEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE4findIS3_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIN18FireMessageHandler7RequestEPN7BlueFin9GlRequestEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEED2Ev
- __ZZNSt3__112__hash_tableINS_17__hash_value_typeIN18FireMessageHandler7RequestEPN7BlueFin9GlRequestEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__emplace_uniqueB9fqe220106IJRKNS_21piecewise_construct_tENS_5tupleIJRSA_EEENSQ_IJEEEEEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ENKUlSR_SP_OSS_OST_E_clESR_SP_S14_S15_
CStrings:
+ "#fftd,periodic,sendStart,failed"
+ "#fftd,response,fail,%d,%s"
+ "#fftd,rft,sendStart,failed,%d"
+ "#fftd,tm,sendOneShortRequest,failed"
+ "#fftd,tm,sendStopRequest,failed"
+ "#fmh,eraseRequest,request,%p,%d,age,%.1f,pf,%p,meas,%p,sync,%p"
+ "#fmh,startRequest,%d,createFailed"
+ "#fmh,startRequest,%p,%d,alreadyExist,age,%.1f"
+ "EngineAlreadyInRun,engine,%p,pf,%p,sync,%p"
+ "FIRE@135.0.4 GLL@653695"
+ "GlReqOnStart,request,ok,%p,pf,%p,sync,%p"
+ "Jun 23 2026, 02:00:11"
+ "fftd,recordIQ,sendStart,failed"
+ "fmh,StartRequest,request,%p,%d,pf,%p,sync,%p"
+ "startRequest"
- "#fmh,eraseRequest,request,%p,%d,size,%zu"
- "#fmh,startRequest,%p,%d,alreadyExist"
- "EngineAlreadyInRun,engine,%p,reqSize,%zu"
- "FIRE@135.0.3 GLL@653695"
- "GlReqOnStart,request,ok,%p,size,%zu"
- "Jun 12 2026, 22:35:31"
- "fmh,StartRequest,request,%p,%d,size,%zu"

```
