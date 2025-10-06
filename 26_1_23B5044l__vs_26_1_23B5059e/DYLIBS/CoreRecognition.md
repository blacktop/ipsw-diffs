## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

```diff

-428.0.0.0.0
-  __TEXT.__text: 0x526ac
+430.0.0.0.0
+  __TEXT.__text: 0x526c0
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0x2204
   __TEXT.__const: 0x824
-  __TEXT.__gcc_except_tab: 0x80f0
+  __TEXT.__gcc_except_tab: 0x80fc
   __TEXT.__cstring: 0x3843
   __TEXT.__oslogstring: 0x52
   __TEXT.__ustring: 0x1282

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0C23A02-0879-346C-B123-4D7096097DB0
+  UUID: 49D5DF6C-0C10-357E-9487-76B9A61B89CE
   Functions: 1063
   Symbols:   4369
   CStrings:  4780
Functions:
~ -[CRAlignmentLayer layoutSublayers] : 2764 -> 2788
~ _tpThreadInit : 420 -> 400
~ __ZN14ThreadPoolAuto11setupCommonEP13TP_ThreadPooljjj : 488 -> 504
CStrings:
+ "***calloc failure\n"
+ "***tpThreadInit: calloc failure"
+ "calloc failure"
- "***malloc failure\n"
- "***tpThreadInit: malloc failure"
- "malloc failure"

```
