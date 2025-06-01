## AppSupport

> `/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`

```diff

-2622.0.0.0.0
-  __TEXT.__text: 0x2e9d4
+2627.0.0.0.0
+  __TEXT.__text: 0x2ebb4
   __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x1218
+  __TEXT.__objc_methlist: 0x1298
   __TEXT.__cstring: 0x5252
   __TEXT.__const: 0x4d80
-  __TEXT.__oslogstring: 0xba8
+  __TEXT.__oslogstring: 0xbdd
   __TEXT.__gcc_except_tab: 0x1f4
   __TEXT.__dlopen_cstrs: 0x12c
-  __TEXT.__unwind_info: 0xbd8
-  __TEXT.__objc_classname: 0x2ad
-  __TEXT.__objc_methname: 0x381f
-  __TEXT.__objc_methtype: 0x8b5
-  __TEXT.__objc_stubs: 0x2e80
+  __TEXT.__unwind_info: 0xbe4
+  __TEXT.__objc_classname: 0x2dc
+  __TEXT.__objc_methname: 0x38d1
+  __TEXT.__objc_methtype: 0x8bf
+  __TEXT.__objc_stubs: 0x2f40
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xb08
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c20
-  __DATA_CONST.__objc_selrefs: 0xf88
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_const: 0x1e70
+  __DATA_CONST.__objc_selrefs: 0xfb0
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__cfstring: 0x3d80
   __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__objc_const: 0xaa8
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_const: 0xb38
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH.__objc_data: 0x438
+  __AUTH.__objc_data: 0x488
   __AUTH.__data: 0x38
-  __DATA.__objc_classrefs: 0x1d8
-  __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x258
-  __DATA.__data: 0x4b1
+  __DATA.__objc_ivar: 0x25c
+  __DATA.__data: 0x511
   __DATA.__bss: 0x250
   __DATA_DIRTY.__objc_data: 0x488
   __DATA_DIRTY.__data: 0x189

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 91EB22B4-467A-3B6C-96BA-921D029516CC
-  Functions: 1150
-  Symbols:   3623
-  CStrings:  2110
+  UUID: EB47BB50-A5BF-3141-9A7A-3EE97A7414BA
+  Functions: 1159
+  Symbols:   3667
+  CStrings:  2120
 
Symbols:
+ +[ALSCTrivialGreenClient _skuRegionCode]
+ -[ALSCTrivialGreenClient _initWithSKURegionCode:key2EnablingSKURegionCodes:]
+ -[ALSCTrivialGreenClient calculatedKey2Value]
+ -[ALSCTrivialGreenClient init]
+ -[ALSCTrivialGreenClient key1Value]
+ -[ALSCTrivialGreenClient key2Value]
+ -[ALSCTrivialGreenClient key3Value]
+ -[ALSCTrivialGreenClient setCalculatedKey2Value:]
+ -[ALSCTrivialGreenClient valuesFinalized]
+ _OBJC_CLASS_$_ALSCTrivialGreenClient
+ _OBJC_IVAR_$_ALSCTrivialGreenClient._calculatedKey2Value
+ _OBJC_METACLASS_$_ALSCTrivialGreenClient
+ __OBJC_$_CLASS_METHODS_ALSCTrivialGreenClient
+ __OBJC_$_INSTANCE_METHODS_ALSCTrivialGreenClient
+ __OBJC_$_INSTANCE_VARIABLES_ALSCTrivialGreenClient
+ __OBJC_$_PROP_LIST_ALSCGreenClientProtocol
+ __OBJC_$_PROP_LIST_ALSCTrivialGreenClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ALSCGreenClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ALSCGreenClientProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ALSCGreenClient
+ __OBJC_CLASS_PROTOCOLS_$_ALSCTrivialGreenClient
+ __OBJC_CLASS_RO_$_ALSCTrivialGreenClient
+ __OBJC_LABEL_PROTOCOL_$_ALSCGreenClientProtocol
+ __OBJC_METACLASS_RO_$_ALSCTrivialGreenClient
+ __OBJC_PROTOCOL_$_ALSCGreenClientProtocol
+ _objc_msgSend$_initWithSKURegionCode:key2EnablingSKURegionCodes:
+ _objc_msgSend$_skuRegionCode
+ _objc_msgSend$calculatedKey2Value
+ _objc_msgSend$containsObject:
+ _objc_msgSend$release
+ _objc_msgSend$setCalculatedKey2Value:
CStrings:
+ "@\"<ALSCGreenClientProtocol>\""
+ "ALSCGreenClientProtocol"
+ "ALSCTrivialGreenClient"
+ "TB,N,V_calculatedKey2Value"
+ "Trivial green calculated value %d for region code %@"
+ "_calculatedKey2Value"
+ "_initWithSKURegionCode:key2EnablingSKURegionCodes:"
+ "_skuRegionCode"
+ "calculatedKey2Value"
+ "containsObject:"
+ "setCalculatedKey2Value:"
- "@\"ALSCGreenClient\""

```
