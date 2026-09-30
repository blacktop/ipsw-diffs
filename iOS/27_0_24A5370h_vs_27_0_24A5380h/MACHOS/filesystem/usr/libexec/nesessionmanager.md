## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-  __TEXT.__text: 0xb6ce0
+  __TEXT.__text: 0xb6ef8
   __TEXT.__auth_stubs: 0x1e10
-  __TEXT.__objc_stubs: 0x8a20
+  __TEXT.__objc_stubs: 0x8a60
   __TEXT.__objc_methlist: 0x3fc4
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x2394
-  __TEXT.__objc_methname: 0x9b2f
-  __TEXT.__oslogstring: 0x1138b
-  __TEXT.__cstring: 0x5a86
+  __TEXT.__gcc_except_tab: 0x23c0
+  __TEXT.__objc_methname: 0x9b50
+  __TEXT.__oslogstring: 0x11449
+  __TEXT.__cstring: 0x5a93
   __TEXT.__objc_classname: 0xbc4
   __TEXT.__objc_methtype: 0x2270
-  __TEXT.__unwind_info: 0x1730
-  __DATA_CONST.__const: 0x1e48
+  __TEXT.__unwind_info: 0x1738
+  __DATA_CONST.__const: 0x1e88
   __DATA_CONST.__cfstring: 0x2a40
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x158

   __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xf18
-  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x8738
-  __DATA.__objc_selrefs: 0x2640
+  __DATA.__objc_selrefs: 0x2650
   __DATA.__objc_ivar: 0x7f4
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0x1040

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1958
-  Symbols:   711
-  CStrings:  4656
+  Functions: 1961
+  Symbols:   712
+  CStrings:  4662
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NEGuardProxyManager
CStrings:
+ "%@: Deregister last Filter Session calling stopGuardProxyManager: %@"
+ "%@: Started guard proxy."
+ "NESessionManager: starting guard proxy manager."
+ "NESessionManager: stopping guard proxy manager."
+ "missionCritical-9500"
+ "start"
+ "stopWithCompletionHandler:"
- "mc-9500"

```
