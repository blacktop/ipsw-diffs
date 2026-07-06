## dyld

> `/usr/lib/dyld`

```diff

-  __TEXT.__text: 0x9175c
+  __TEXT.__text: 0x9195c
   __TEXT.__const: 0x20d8
-  __TEXT.__cstring: 0x1000d
+  __TEXT.__cstring: 0x10072
   __TEXT.__unwind_info: 0x4f0
   __DATA_CONST.__const: 0x4c08
   __AUTH_CONST.__const: 0x24a0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  Functions: 2991
-  Symbols:   7551
-  CStrings:  2001
+  Functions: 2995
+  Symbols:   7561
+  CStrings:  2005
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__all_image_info : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZNK5dyld412RuntimeState11isOsProgramEPKNS_17PrebuiltLoaderSetENSt3__18optionalI7CStringEERb
+ __ZNK5dyld412RuntimeState34allowProgramsToSaveUpdatedClosuresEPKNS_17PrebuiltLoaderSetENSt3__18optionalI7CStringEE
+ __ZNK5dyld415SyscallDelegate11isHostMacOSEv
+ __ZNK5dyld415SyscallDelegate16isPlatformBinaryERb
+ _csops
CStrings:
+ "/AppleInternal/"
+ "1387"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Jun 28 20:04:39 PDT 2026; root:libignition-58~38430/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sun Jun 28 20:04:39 PDT 2026; root:libignition-58~38430/libignition_core/RELEASE_ARM64E"
+ "csops() failure"
+ "missing code signature in <%s> '%s'"
+ "too many segments %llu (max 255)"
- "1385"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sun Jun 21 19:12:27 PDT 2026; root:libignition-58~38375/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Sun Jun 21 19:12:27 PDT 2026; root:libignition-58~38375/libignition_core/RELEASE_ARM64E"

```
