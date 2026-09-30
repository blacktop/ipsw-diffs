## AttributeGraph

> `/System/Library/PrivateFrameworks/AttributeGraph.framework/Versions/A/AttributeGraph`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-8.0.64.0.0
-  __TEXT.__text: 0x3b9e0
+8.0.76.0.0
+  __TEXT.__text: 0x3ba44
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x14f0
-  __TEXT.__gcc_except_tab: 0x11f0
-  __TEXT.__cstring: 0x17d6
-  __TEXT.__oslogstring: 0xd8
+  __TEXT.__gcc_except_tab: 0x11f8
+  __TEXT.__cstring: 0x17b6
+  __TEXT.__oslogstring: 0xfd
   __TEXT.__ustring: 0x38
   __TEXT.__swift5_typeref: 0x310
   __TEXT.__constg_swiftt: 0x510

   __AUTH_CONST.__auth_got: 0x760
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x50
-  __DATA.__data: 0x268
+  __DATA.__data: 0x258
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1690
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x3d8
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__data: 0x3e8
   __DATA_DIRTY.__bss: 0x6e0
-  __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__common: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1722
+  Functions: 1723
   Symbols:   1696
-  CStrings:  337
+  CStrings:  336
 
Functions:
~ __ZNK2AG5Graph11print_cycleENS_4data3ptrINS_4NodeEEE : 652 -> 700
~ __ZN2AG12_GLOBAL__N_115cycle_verbosityEv : 64 -> 60
~ _ZNK2AG5Graph11print_cycleENS_4data3ptrINS_4NodeEEE.cold.1 : 80 -> 76
+ _ZNK2AG5Graph11print_cycleENS_4data3ptrINS_4NodeEEE.cold.3
CStrings:
+ "Cycle detected through attribute: %u"
- "=== Evaluation stack ===\n"
- "cycle detected through attribute: %u"
```
