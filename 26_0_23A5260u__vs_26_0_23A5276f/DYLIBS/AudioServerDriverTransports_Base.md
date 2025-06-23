## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-300.65.0.0.0
-  __TEXT.__text: 0x3f9cc
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x33cc
-  __TEXT.__gcc_except_tab: 0x6330
+300.68.0.0.0
+  __TEXT.__text: 0x3fb10
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x33f4
+  __TEXT.__gcc_except_tab: 0x635c
   __TEXT.__const: 0x50e
-  __TEXT.__cstring: 0x13f0
-  __TEXT.__oslogstring: 0x2fc4
-  __TEXT.__unwind_info: 0x1fe0
+  __TEXT.__cstring: 0x1400
+  __TEXT.__oslogstring: 0x2fde
+  __TEXT.__unwind_info: 0x1ff0
   __TEXT.__objc_classname: 0x6a1
-  __TEXT.__objc_methname: 0x6dd1
+  __TEXT.__objc_methname: 0x6e71
   __TEXT.__objc_methtype: 0x1013
-  __TEXT.__objc_stubs: 0x6500
+  __TEXT.__objc_stubs: 0x6560
   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__const: 0x758
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cc8
+  __DATA_CONST.__objc_selrefs: 0x1ce0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x450
   __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x51d0
+  __AUTH_CONST.__objc_const: 0x5200
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x314
+  __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x840
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48BB429A-6B3D-33C1-8641-2A93612A95DC
-  Functions: 1678
-  Symbols:   5701
-  CStrings:  2291
+  UUID: 39598854-50E2-3012-BF0F-ACABD10EAF92
+  Functions: 1681
+  Symbols:   5698
+  CStrings:  2298
 
Symbols:
+ -[ASDTExclavesStream nonSecureStreamStarted]
+ -[ASDTExclavesStream setNonSecureStreamStarted:]
+ -[ASDTExclavesStream unexpectedSensorStatus:]
+ _OBJC_IVAR_$_ASDTExclavesStream._nonSecureStreamStarted
+ _objc_getProperty
+ _objc_msgSend$nonSecureStreamStarted
+ _objc_msgSend$setNonSecureStreamStarted:
+ _objc_msgSend$unexpectedSensorStatus:
+ _objc_setProperty_atomic
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "%@: %s : resulting status: [%u] %s (%sexpected)"
+ "%@: current status: [%u] %s (%sexpected)"
+ "300.68"
+ "T@\"ASDTIOService\",&,V_ioService"
+ "TB,N,V_nonSecureStreamStarted"
+ "[%u] %s (%sexpected)"
+ "_nonSecureStreamStarted"
+ "nonSecureStreamStarted"
+ "setNonSecureStreamStarted:"
+ "un"
+ "unexpectedSensorStatus:"
- "%@: %s : resulting status: [%u] %s"
- "%@: current status: [%u] %s"
- "300.65"
- "[%u] %s"

```
