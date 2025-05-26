## ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

-656.100.20.0.0
-  __TEXT.__text: 0x1dc4c
+656.122.3.0.0
+  __TEXT.__text: 0x1e0fc
   __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_stubs: 0x2c00
+  __TEXT.__objc_stubs: 0x2ca0
   __TEXT.__objc_methlist: 0x8bc
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x46c4
-  __TEXT.__objc_methname: 0x2fb9
-  __TEXT.__oslogstring: 0x146b
+  __TEXT.__cstring: 0x46e4
+  __TEXT.__objc_methname: 0x304f
+  __TEXT.__oslogstring: 0x148f
   __TEXT.__objc_classname: 0x102
-  __TEXT.__objc_methtype: 0x7c6
-  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__objc_methtype: 0x7dd
+  __TEXT.__gcc_except_tab: 0x230
   __TEXT.__dlopen_cstrs: 0xa5
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x60

   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x928
-  __DATA_CONST.__cfstring: 0x6d20
+  __DATA_CONST.__cfstring: 0x6d80
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x158
+  __DATA_CONST.__objc_classrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_arraydata: 0x330
+  __DATA_CONST.__objc_arraydata: 0x340
+  __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_intobj: 0x450
-  __DATA_CONST.__objc_dictobj: 0x168
-  __DATA.__objc_const: 0x1968
-  __DATA.__objc_selrefs: 0xc08
-  __DATA.__objc_ivar: 0x208
+  __DATA.__objc_const: 0x19a8
+  __DATA.__objc_selrefs: 0xc30
+  __DATA.__objc_ivar: 0x210
   __DATA.__objc_data: 0x1f8
   __DATA.__data: 0x170
   __DATA.__crash_info: 0x40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 361
-  Symbols:   390
-  CStrings:  1762
+  Symbols:   391
+  CStrings:  1774
 
Symbols:
+ _OBJC_CLASS_$_OSAExclaveContainer
CStrings:
+ "@\"OSAExclaveContainer\""
+ "Q\x15\x11\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x81\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91!q\x12b\x16YW\x13\"\x144\""
+ "Thread %llu has only exclave frames"
+ "VNG_PERMISSIONS"
+ "_exclaveContainer"
+ "_exclaveThreadNumbers"
+ "exclave"
+ "exclaveScid"
+ "getFramesForThread:usingCatalog:"
+ "insertObject:atIndex:"
+ "parseKCdata:"
+ "setThreadId:withScId:"
+ "threadIdToScId"
- "Q\x15\x11\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x81\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91!q\x12b\x16YW\x13\"\x124\""

```
