## IOHIDPointerScrollFilter

> `/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/Contents/MacOS/IOHIDPointerScrollFilter`

```diff

-2104.80.4.0.0
-  __TEXT.__text: 0x867c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__gcc_except_tab: 0x800
+2115.100.21.0.0
+  __TEXT.__text: 0x84c4
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__gcc_except_tab: 0x810
   __TEXT.__const: 0x406
   __TEXT.__cstring: 0x6d2
   __TEXT.__oslogstring: 0x41f
   __TEXT.__unwind_info: 0x438
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_got: 0x370
+  __DATA_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0x5b0
   __AUTH_CONST.__cfstring: 0x9a0
   __AUTH.__data: 0x78

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AA3BADD3-0B4E-3A8A-8482-F81E28BE2D6F
+  UUID: 8AA1CB7E-A11A-30E9-8A34-CA09F361F35C
   Functions: 197
-  Symbols:   233
+  Symbols:   234
   CStrings:  201
 
Symbols:
+ _memcpy
Functions:
~ __ZN22IOHIDScrollAccelerator10accelerateEPdmy : 728 -> 732
~ __ZN27IOHIDParametricAcceleration8GetCurveEPK14__CFDictionary : 192 -> 172
~ __ZN27IOHIDParametricAcceleration20CreateWithParametersEPK9__CFArrayddd : 1616 -> 1544
~ __ZN22IOHIDTableAcceleration15CreateWithTableEPK8__CFDataddd : 1672 -> 1648
~ sub_371c -> sub_2958 : 728 -> 732
~ __ZN22IOHIDTableAcceleration23CreateOriginalWithTableEPK8__CFDataddd : 1360 -> 1252
~ __ZNK22IOHIDTableAcceleration9serializeEP14__CFDictionary : 624 -> 620
~ sub_4db0 -> sub_3f80 : 408 -> 412
~ __ZNK17ACCEL_TABLE_ENTRY12accelerationIdEET_v : 28 -> 16
~ __ZNK17ACCEL_TABLE_ENTRY1xIdEET_j : 32 -> 20
~ __ZNK17ACCEL_TABLE_ENTRY1yIdEET_j : 32 -> 20
~ __ZNK17ACCEL_TABLE_ENTRY5pointEj : 48 -> 32
~ __ZNK11ACCEL_TABLE5scaleIdEET_v : 28 -> 16
~ __ZlsRNSt3__113basic_ostreamIcNS_11char_traitsIcEEEERK11ACCEL_TABLE : 368 -> 356
~ sub_5368 -> sub_44f0 : 588 -> 552
~ sub_55b4 -> sub_4718 : 428 -> 432
~ sub_58f4 -> sub_4a5c : 172 -> 164
~ __ZN24IOHIDPointerScrollFilterC2EPK8__CFUUID : 244 -> 228
~ __ZN24IOHIDPointerScrollFilter17setupAccelerationEv : 480 -> 464
~ __ZNK24IOHIDPointerScrollFilter9serializeEP14__CFDictionary : 1652 -> 1736
~ __ZN24IOHIDPointerScrollFilter15accelerateEventEP12__IOHIDEvent : 1064 -> 1068
~ __ZN24IOHIDPointerScrollFilter27createPointerTableAlgorithmEi : 280 -> 268
~ __ZN24IOHIDPointerScrollFilter32createPointerParametricAlgorithmEi : 340 -> 316
~ __ZNK24IOHIDPointerScrollFilter18copyCachedPropertyEPK10__CFString : 116 -> 120
~ sub_782c -> sub_69a4 : 56 -> 60
~ __ZN24IOHIDPointerScrollFilter26createScrollTableAlgorithmEmii : 380 -> 364
~ __ZN24IOHIDPointerScrollFilter31createScrollParametricAlgorithmEmii : 344 -> 312
~ __ZN24IOHIDPointerScrollFilter24setupPointerAccelerationEd : 3128 -> 3076
~ __ZN24IOHIDPointerScrollFilter23setupScrollAccelerationEd : 2280 -> 2256
~ __ZNK24IOHIDPointerScrollFilter30getAccelerationAlgorithmStringEh : 40 -> 36
~ sub_9784 -> sub_8880 : 180 -> 172
~ sub_99dc -> sub_8ad0 : 28 -> 16
~ sub_99f8 -> sub_8ae0 : 16 -> 28
~ sub_9a80 -> sub_8b74 : 68 -> 140
~ sub_9b38 -> sub_8c74 : 140 -> 68

```
