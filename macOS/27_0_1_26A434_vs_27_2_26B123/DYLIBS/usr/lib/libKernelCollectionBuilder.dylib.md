## libKernelCollectionBuilder.dylib

> `/usr/lib/libKernelCollectionBuilder.dylib`

```diff

-27062.0.0.0.0
-  __TEXT.__text: 0x48ae0
+27104.0.0.0.0
+  __TEXT.__text: 0x48c4c
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x394
-  __TEXT.__cstring: 0xa164
+  __TEXT.__cstring: 0xa21a
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xe80
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1393
-  Symbols:   1765
-  CStrings:  1038
+  Functions: 1394
+  Symbols:   1766
+  CStrings:  1042
 
Symbols:
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
Functions:
~ ___ZN15AppCacheBuilder30assignSegmentRegionsAndOffsetsEv_block_invoke.72 : 80 -> 92
~ __ZNK6mach_o6Header19parse_dylib_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE : 292 -> 352
~ __ZNK6mach_o6Header20parse_string_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE : 220 -> 260
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb1EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2416 -> 2424
~ __ZNK6mach_o6Header27validSemanticsSingleSegmentILb0EEENS_5ErrorERKNS_6PolicyEyNSt3__14spanIKhLm18446744073709551615EEE : 2380 -> 2388
~ __ZNK6mach_o6Header29stringFromOffsetInLoadCommandERKNS0_15LoadCommandInfoEjPNS_5ErrorE : 308 -> 344
+ __ZNK6mach_o6Header22parse_dylinker_commandERKNS0_15LoadCommandInfoEPNS_5ErrorE
~ ____ZNK6mach_o6Header9dylibInfoEv_block_invoke : 124 -> 148
CStrings:
+ "load command #%d %.*s name offset too small"
+ "load command #%d %.*s not a dylib load command"
+ "load command #%d %.*s path offset too small"
+ "load command #%d string start offset too small"
```
