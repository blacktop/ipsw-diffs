## dyld

> `/usr/lib/dyld`

```diff

-1378.0.0.0.0
-  __TEXT.__text: 0x9173c
-  __TEXT.__const: 0x2088
-  __TEXT.__cstring: 0xffdb
+1385.0.0.0.0
+  __TEXT.__text: 0x9175c
+  __TEXT.__const: 0x20d8
+  __TEXT.__cstring: 0x1000d
   __TEXT.__unwind_info: 0x4f0
   __DATA_CONST.__const: 0x4c08
   __AUTH_CONST.__const: 0x24a0

   __DATA_DIRTY.__common: 0x1120
   __TPRO_CONST.__data: 0xe1
   __TPRO_CONST.__allocator: 0x20000
-  UUID: 41DE795B-9283-37FD-917E-D674BB73F541
+  UUID: 2EA6D832-370C-319F-959D-58183FBB4E2D
   Functions: 2991
   Symbols:   4135
-  CStrings:  2000
+  CStrings:  2001
 
Symbols:
- __block_descriptor_tmp.257
Functions:
~ __ZNK5dyld313MachOAnalyzer21forEachRebase_OpcodesER11DiagnosticsRKNS_11MachOLoaded12LinkEditInfoEPKN6mach_o12UnsafeHeader11SegmentInfoEU13block_pointerFvPKcS6_SB_bjhyNS0_6RebaseERbE : 1052 -> 1080
~ _ccsha384_vng_arm_hw_compress : 8 -> 12
CStrings:
+ "1385"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Fri May 15 22:47:30 PDT 2026; root:libignition-58~38062/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Fri May 15 22:47:30 PDT 2026; root:libignition-58~38062/libignition_core/RELEASE_ARM64E"
+ "missing REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB"
- "1378"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Apr 23 20:24:30 PDT 2026; root:libignition-58~37838/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Apr 23 20:24:30 PDT 2026; root:libignition-58~37838/libignition_core/RELEASE_ARM64E"

```
