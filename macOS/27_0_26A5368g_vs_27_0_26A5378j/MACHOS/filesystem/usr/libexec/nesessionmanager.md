## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-  __TEXT.__text: 0xbf1a0
+  __TEXT.__text: 0xbf3d8
   __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__objc_stubs: 0x8920
+  __TEXT.__objc_stubs: 0x8960
   __TEXT.__objc_methlist: 0x3d84
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x2428
-  __TEXT.__objc_methname: 0x947b
-  __TEXT.__oslogstring: 0x10dc9
+  __TEXT.__gcc_except_tab: 0x2450
+  __TEXT.__objc_methname: 0x949c
+  __TEXT.__oslogstring: 0x10e87
   __TEXT.__cstring: 0x56d7
   __TEXT.__objc_classname: 0xb3b
   __TEXT.__objc_methtype: 0x1be5
-  __TEXT.__unwind_info: 0x1738
-  __DATA_CONST.__const: 0x22e8
+  __TEXT.__unwind_info: 0x1740
+  __DATA_CONST.__const: 0x2328
   __DATA_CONST.__cfstring: 0x2b20
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_intobj: 0x240
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xe78
-  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__got: 0x798
   __DATA.__objc_const: 0x8280
-  __DATA.__objc_selrefs: 0x2470
+  __DATA.__objc_selrefs: 0x2480
   __DATA.__objc_ivar: 0x7bc
   __DATA.__objc_data: 0x19a0
   __DATA.__data: 0xeb8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2005
-  Symbols:   681
-  CStrings:  4515
+  Functions: 2008
+  Symbols:   682
+  CStrings:  4521
 
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
+ "start"
+ "stopWithCompletionHandler:"

```
