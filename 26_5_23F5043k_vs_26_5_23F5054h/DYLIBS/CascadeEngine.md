## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-209.16.0.0.0
-  __TEXT.__text: 0x1ea9c
+209.17.0.1.0
+  __TEXT.__text: 0x1ead0
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x1674
   __TEXT.__const: 0xc8

   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__unwind_info: 0x7f0
   __TEXT.__objc_classname: 0x431
-  __TEXT.__objc_methname: 0x5383
+  __TEXT.__objc_methname: 0x53be
   __TEXT.__objc_methtype: 0x10f5
-  __TEXT.__objc_stubs: 0x4580
-  __DATA_CONST.__got: 0x280
+  __TEXT.__objc_stubs: 0x45c0
+  __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1E1ABB2-068D-3036-94B4-1943C718EE36
+  UUID: 203A03DA-9F8E-3680-8EFA-784FB4BDE154
   Functions: 615
-  Symbols:   2579
-  CStrings:  1607
+  Symbols:   2582
+  CStrings:  1609
 
Symbols:
+ _OBJC_CLASS_$_CCDatabaseSetStateVectorBuilder
+ _objc_msgSend$build
+ _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:
+ _objc_msgSend$enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:
+ _objc_msgSend$initWithDeviceMapping:missingAtomsImplied:trackCompactedAtoms:
- _objc_msgSend$constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:
- _objc_msgSend$enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:
Functions:
~ -[CCSetVersionedMergeable mergeableDeltasForMetadata:atomBatchVersion:error:] : 1312 -> 1304
~ -[CCSetVersionedMergeable stateVector] : 476 -> 536
CStrings:
+ "build"
+ "constructStateVectorsFromDatabaseWithDeviceMapping:contentStateVectorBuilder:metaContentStateVectorBuilder:error:"
+ "enumeratePresentContentProvenanceForStateVector:deviceMapping:error:usingBlock:"
+ "initWithDeviceMapping:missingAtomsImplied:trackCompactedAtoms:"
- "constructStateVectorsFromDatabaseWithDeviceMapping:outContent:outMetaContent:error:"
- "enumerateContentProvenanceRecordsForStateVector:selectAtomsInState:skipOverAtomsInState:deviceMapping:error:usingBlock:"

```
