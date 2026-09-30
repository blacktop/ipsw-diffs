## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-2005.0.13.0.0
-  __TEXT.__text: 0x3c16c
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x3680
+2005.0.31.0.0
+  __TEXT.__text: 0x3c168
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_stubs: 0x36c0
   __TEXT.__objc_methlist: 0x1a0c
   __TEXT.__const: 0x1350
-  __TEXT.__objc_methname: 0x4758
-  __TEXT.__cstring: 0x49d0
+  __TEXT.__objc_methname: 0x4789
+  __TEXT.__cstring: 0x49da
   __TEXT.__objc_classname: 0x6cc
-  __TEXT.__objc_methtype: 0x1f58
+  __TEXT.__objc_methtype: 0x1f5b
   __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__oslogstring: 0x17b3
-  __TEXT.__unwind_info: 0xca0
-  __DATA_CONST.__auth_got: 0x738
+  __TEXT.__unwind_info: 0xc98
+  __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x21f0
+  __DATA_CONST.__const: 0x2220
   __DATA_CONST.__cfstring: 0xe00
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x178

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA.__objc_const: 0x79e0
-  __DATA.__objc_selrefs: 0x1130
+  __DATA.__objc_selrefs: 0x1140
   __DATA.__objc_ivar: 0x188
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x1ab8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C6B49E3-D868-3448-B174-67B46EAA44F8
+  UUID: 78427601-F27D-349E-B89D-5868692DC69C
   Functions: 1465
-  Symbols:   394
-  CStrings:  1929
+  Symbols:   395
+  CStrings:  1932
 
Symbols:
+ _LACBiomeEvaluationRatchetStateFromLACDTORatchetStateRawValue
Functions:
~ sub_10000d740 : 460 -> 392
~ sub_10000d90c -> sub_10000d8c8 : 192 -> 236
~ sub_10001e154 -> sub_10001e13c : 212 -> 232
CStrings:
+ "/.exclave"
+ "_collectBiomeAnalyticsForRequest:dtoState:ratchetState:result:"
+ "initWithPolicy:errorCode:biometry:passcode:dtoState:ratchetState:callerBundleID:"
+ "ratchetState"
+ "rawValue"
+ "v48@0:8@16q24q32@40"
- "_collectBiomeAnalyticsForRequest:dtoState:result:"
- "initWithPolicy:errorCode:biometry:passcode:ratchet:callerBundleID:"
- "v40@0:8@16q24@32"

```
