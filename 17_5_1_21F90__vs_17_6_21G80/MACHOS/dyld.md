## dyld

> `/usr/lib/dyld`

```diff

-1162.0.0.0.0
-  __TEXT.__text: 0x7c484
-  __TEXT.__const: 0x1c10
-  __TEXT.__cstring: 0xd4f2
+1165.3.0.0.0
+  __TEXT.__text: 0x7ce68
+  __TEXT.__const: 0x1c70
+  __TEXT.__cstring: 0xd4f4
   __TEXT.__unwind_info: 0x478
   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__const: 0x50f8

   __DATA_DIRTY.__data: 0x5c
   __DATA_DIRTY.__common: 0x1120
   __DATA_DIRTY.__bss: 0x1bc0
-  UUID: 71846EAC-EE65-3697-BF7D-790B6A07DCDB
+  UUID: 52039C94-4DA1-3638-BD52-020A0B5FA399
   Functions: 2920
   Symbols:   3408
   CStrings:  1714
Symbols:
+ _ZN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE12reserveExactEy.cold.1
+ __ZN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE12reserveExactEy
+ __ZN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE7reserveEy
- _ZN3lsl6VectorIN5dyld418AuthenticatedValueIPKNS1_6LoaderEEEE12reserveExactEy.cold.1
- __ZN3lsl6VectorIN5dyld418AuthenticatedValueIPKNS1_6LoaderEEEE12reserveExactEy
- __ZN3lsl6VectorIN5dyld418AuthenticatedValueIPKNS1_6LoaderEEEE7reserveEy
CStrings:
+ "1165.3"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri Jul  5 18:11:22 PDT 2024; root:libignition-56~32003/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Fri Jul  5 18:11:22 PDT 2024; root:libignition-56~32003/libignition_core/RELEASE_ARM64E"
- "1162"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed May  1 20:15:26 PDT 2024; root:libignition-56~24447/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed May  1 20:15:26 PDT 2024; root:libignition-56~24447/libignition_core/RELEASE_ARM64E"

```
