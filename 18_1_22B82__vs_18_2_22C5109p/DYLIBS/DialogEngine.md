## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

```diff

-3401.5.1.0.0
-  __TEXT.__text: 0x4fa170
+3402.29.1.0.0
+  __TEXT.__text: 0x4fb88c
   __TEXT.__auth_stubs: 0x2050
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0x317c
-  __TEXT.__gcc_except_tab: 0x3b690
-  __TEXT.__const: 0x1b4d3
-  __TEXT.__cstring: 0x64a62
+  __TEXT.__gcc_except_tab: 0x3b880
+  __TEXT.__const: 0x1b503
+  __TEXT.__cstring: 0x64bcf
   __TEXT.__ustring: 0xaa
   __TEXT.__oslogstring: 0x27c
-  __TEXT.__unwind_info: 0x140c8
-  __TEXT.__objc_classname: 0x4a8
+  __TEXT.__unwind_info: 0x14120
+  __TEXT.__objc_classname: 0x4a4
   __TEXT.__objc_methname: 0x66fc
   __TEXT.__objc_methtype: 0x6374
   __TEXT.__objc_stubs: 0x3e80

   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__auth_got: 0x1040
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x12478
+  __AUTH_CONST.__const: 0x124c8
   __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x5f80
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15577
-  Symbols:   17894
-  CStrings:  28008
+  Functions: 15587
+  Symbols:   17912
+  CStrings:  28016
 
Symbols:
+ _OBJC_CLASS_$_DELog
+ _OBJC_METACLASS_$_DELog
+ __ZN4siri12dialogengine16FormatXMLElementERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_
+ __ZN4siri12dialogengine21FormatMarkElementSSMLEPNS0_7ContextEPKNS0_8ChunkTagE
+ __ZN4siri12dialogengine23CollectIteratorsVisitor13ProcessChunksERKNSt3__16vectorINS2_10shared_ptrINS0_9ChunkTextEEENS2_9allocatorIS6_EEEE
+ __ZN4siri12dialogengine23CollectIteratorsVisitor21GetIteratorAttributesERKNS0_15SpeakableStringE
+ __ZN4siri12dialogengine23CollectIteratorsVisitor5VisitERKNS0_4TextE
+ __ZN4siri12dialogengine23CollectIteratorsVisitor5VisitERKNS0_6DialogE
+ __ZNK4siri12dialogengine23CollectIteratorsVisitor12GetIteratorsEv
+ __ZTIN4siri12dialogengine23CollectIteratorsVisitorE
+ __ZTSN4siri12dialogengine23CollectIteratorsVisitorE
+ __ZTVN4siri12dialogengine23CollectIteratorsVisitorE
- _OBJC_CLASS_$_DELogging
- _OBJC_METACLASS_$_DELogging
- __ZN4siri12dialogengine26ConvertItemFormatSSMLToTagERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
CStrings:
+ "\"mark\" element has both attributes \"name\" and \"value\"; The \"value\" value will be ignored"
+ "\"mark\" element should not have any content; behavior will be as if the content follows the element"
+ "' is the same as existing parameter of the same name"
+ "3402.29.1"
+ "5.2"
+ "CAT Request (Dialog Engine 3402.29.1)"
+ "DELog"
+ "SSML mark element requires 'name' or 'value' attribute."
+ "Unhandled ssml mode: %!d(MISSING)"
+ "Variable is not a string: '"
+ "mrk=name="
- "3401.5.1"
- "CAT Request (Dialog Engine 3401.5.1)"
- "DELogging"

```
