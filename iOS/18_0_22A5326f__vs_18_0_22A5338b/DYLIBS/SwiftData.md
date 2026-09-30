## SwiftData

> `/System/Library/Frameworks/SwiftData.framework/SwiftData`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x10a220
-  __TEXT.__auth_stubs: 0x2710
+86.0.0.0.0
+  __TEXT.__text: 0x10f654
+  __TEXT.__auth_stubs: 0x2720
   __TEXT.__objc_methlist: 0x114
-  __TEXT.__cstring: 0x6748
-  __TEXT.__const: 0x6968
-  __TEXT.__constg_swiftt: 0x4740
-  __TEXT.__swift5_typeref: 0x2d6a
-  __TEXT.__swift5_reflstr: 0x1bc8
-  __TEXT.__swift5_fieldmd: 0x2158
+  __TEXT.__cstring: 0x67c8
+  __TEXT.__const: 0x6a08
+  __TEXT.__constg_swiftt: 0x49f8
+  __TEXT.__swift5_typeref: 0x2df8
+  __TEXT.__swift5_reflstr: 0x1be8
+  __TEXT.__swift5_fieldmd: 0x2178
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_capture: 0x73c
+  __TEXT.__swift5_capture: 0x7cc
   __TEXT.__swift5_assocty: 0x5c8
   __TEXT.__swift5_proto: 0x4c8
-  __TEXT.__swift5_types: 0x214
-  __TEXT.__oslogstring: 0x491
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__oslogstring: 0x923
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__unwind_info: 0x3918
-  __TEXT.__eh_frame: 0x6cc0
+  __TEXT.__unwind_info: 0x39a0
+  __TEXT.__eh_frame: 0x6de8
   __TEXT.__objc_methname: 0x1348
-  __DATA_CONST.__got: 0xb68
+  __DATA_CONST.__got: 0xb70
   __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x788
-  __AUTH_CONST.__auth_got: 0x1388
+  __AUTH_CONST.__auth_got: 0x1390
   __AUTH_CONST.__auth_ptr: 0xe10
-  __AUTH_CONST.__const: 0x44e8
+  __AUTH_CONST.__const: 0x46f8
   __AUTH_CONST.__objc_const: 0x3068
   __AUTH.__objc_data: 0x1b8
   __AUTH.__data: 0xb18
-  __DATA.__data: 0x1260
-  __DATA.__bss: 0x6f70
-  __DATA.__common: 0x28
+  __DATA.__data: 0x13a8
+  __DATA.__bss: 0x6ff0
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x288
-  __DATA_DIRTY.__data: 0x3d20
-  __DATA_DIRTY.__bss: 0x2410
-  __DATA_DIRTY.__common: 0x150
+  __DATA_DIRTY.__data: 0x3d40
+  __DATA_DIRTY.__bss: 0x2390
+  __DATA_DIRTY.__common: 0x148
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5051
-  Symbols:   378
-  CStrings:  903
+  Functions: 5127
+  Symbols:   382
+  CStrings:  917
 
Symbols:
+ _NSPersistentHistoryTokenKey
CStrings:
+ " illegally accessed before T.init(backingData:) set the backing data"
+ "%@ is attempting to flip a captured a temporary persistentIdentifier for %!s(MISSING) on %!s(MISSING)"
+ "%!s(MISSING): Unbinding from the main queue. This context was instantiated on the main queue but is being used off it. ModelContexts are not Sendable, consider using a ModelActor."
+ "Cannot fulfill future for %!s(MISSING) without a context %!s(MISSING)"
+ "Illegal attempt to create a full future for a temporary identifier. These won't be resolvable after the temporary object is deallocated: %!s(MISSING)"
+ "Illegal attempt to flip a temporary object to a future %!s(MISSING): %!s(MISSING)"
+ "Illegal attempt to flip relationships to IDs when not bound to a context."
+ "Illegal attempt to map a relationship containing temporary objects to its identifiers."
+ "Invalid access before setting the backing data"
+ "ModelContainerRemoteChange"
+ "Mutated models cannot turn their relationships in to futures."
+ "PersistentIdentifier %!s(MISSING) was remapped to a temporary identifier during save: %!s(MISSING). This is a fatal logic error in %!s(MISSING)"
+ "This backing data has no persistent identifier but is attempting to flip relationships? %!s(MISSING)"
+ "This backing data has no persistent identifier? %!s(MISSING)"
+ "This backing data has retained a temporary object ID beyond the mutations to the context %!s(MISSING)"
+ "_persistentModelID"
- " without a context "
- "Cannot fulfill future for "

```
