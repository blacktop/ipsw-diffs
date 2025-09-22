## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-212.0.0.0.0
-  __TEXT.__text: 0x2d604
+212.40.4.0.0
+  __TEXT.__text: 0x2d568
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x3804
+  __TEXT.__objc_methlist: 0x37ec
   __TEXT.__const: 0x164
-  __TEXT.__cstring: 0x2b71
+  __TEXT.__cstring: 0x2b56
   __TEXT.__oslogstring: 0x215e
   __TEXT.__gcc_except_tab: 0x13f4
-  __TEXT.__unwind_info: 0xc70
-  __TEXT.__objc_classname: 0x74a
-  __TEXT.__objc_methname: 0x76bb
-  __TEXT.__objc_methtype: 0x1ac4
-  __TEXT.__objc_stubs: 0x5ae0
+  __TEXT.__unwind_info: 0xc80
+  __TEXT.__objc_classname: 0x748
+  __TEXT.__objc_methname: 0x7665
+  __TEXT.__objc_methtype: 0x1ac1
+  __TEXT.__objc_stubs: 0x5aa0
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xb90
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c48
+  __DATA_CONST.__objc_selrefs: 0x1c40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2bc0
-  __AUTH_CONST.__objc_const: 0x6250
+  __AUTH_CONST.__cfstring: 0x2ba0
+  __AUTH_CONST.__objc_const: 0x6200
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x11f8
-  __DATA.__objc_ivar: 0x39c
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x800
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F25ECA8F-E105-3D6B-ACEB-47FB1AA75B83
-  Functions: 1232
-  Symbols:   4500
-  CStrings:  2631
+  UUID: DFFB9844-98D5-3ADA-B0D3-3549F42FA09B
+  Functions: 1230
+  Symbols:   4492
+  CStrings:  2625
 
Symbols:
+ -[ASTRepairSessionProvider dealloc]
+ -[ASTSessionInfo initWithIsGuided:deviceSerialNumber:sessionType:]
+ -[ASTSessionInfo isGuidedSessionType]
+ _objc_msgSend$initWithIsGuided:deviceSerialNumber:sessionType:
+ _objc_msgSend$isGuidedSessionType
- -[ASTRepairSession connection]
- -[ASTRepairSession setConnection:]
- -[ASTSessionInfo _descriptionForQueuedSuiteType:]
- -[ASTSessionInfo initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:]
- -[ASTSessionInfo queuedSuiteType]
- _OBJC_IVAR_$_ASTRepairSession._connection
- _OBJC_IVAR_$_ASTSessionInfo._queuedSuiteType
- _objc_msgSend$_descriptionForQueuedSuiteType:
- _objc_msgSend$initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:
- _objc_msgSend$isGuided
- _objc_msgSend$queuedSuiteType
CStrings:
+ "@36@0:8B16@20q28"
+ "[ASTSessionInfo isGuided: %d, deviceSerialNumber: %@, sessionType: %@]"
+ "initWithIsGuided:deviceSerialNumber:sessionType:"
+ "isGuidedSessionType"
- "!"
- "@44@0:8q16B24@28q36"
- "Tq,R,N,V_queuedSuiteType"
- "[ASTSessionInfo queuedSuiteType: %@, isGuided: %d, deviceSerialNumber: %@, sessionType: %@]"
- "_descriptionForQueuedSuiteType:"
- "_queuedSuiteType"
- "initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:"
- "other"

```
