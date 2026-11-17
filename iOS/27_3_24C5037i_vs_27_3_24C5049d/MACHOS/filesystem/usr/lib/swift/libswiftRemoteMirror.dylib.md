## libswiftRemoteMirror.dylib

> `/usr/lib/swift/libswiftRemoteMirror.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-6.4.2.1.9
-  __TEXT.__text: 0xd3fa8
+6.4.4.3.15
+  __TEXT.__text: 0xd432c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x7122
-  __TEXT.__const: 0x7f0
-  __TEXT.__unwind_info: 0x1d58
+  __TEXT.__cstring: 0x717f
+  __TEXT.__const: 0x800
+  __TEXT.__unwind_info: 0x1d68
   __TEXT.__auth_stubs: 0x490
   __DATA_CONST.__const: 0xe68
   __DATA_CONST.__weak_got: 0x8

   __DATA.__common: 0x10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2092
-  Symbols:   2527
-  CStrings:  1643
+  Functions: 2096
+  Symbols:   2531
+  CStrings:  1645
 
Symbols:
+ __ZN20DemanglingForTypeRef25visitPackExpansionTypeRefEPKN5swift10reflection20PackExpansionTypeRefE
+ __ZN20DemanglingForTypeRef27substituteParentIntoContextEPN5swift8Demangle9__runtime4NodeES4_
+ __ZN20DemanglingForTypeRef29visitBuiltinFixedArrayTypeRefEPKN5swift10reflection24BuiltinFixedArrayTypeRefE
+ __ZN5swift8Demangle9__runtime11TypeDecoderINS_10reflection14TypeRefBuilderEE22isValueGenericArgumentEPNS1_4NodeE
CStrings:
+ "type where a Builtin.FixedArray count is required"
+ "unresolved Builtin.FixedArray element type"
```
