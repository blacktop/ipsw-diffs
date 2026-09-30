## AGXMetalG18P

> `/System/Library/Extensions/AGXMetalG18P.bundle/AGXMetalG18P`

```diff

-350.40.0.0.0
-  __TEXT.__text: 0x91c040
+351.1.0.0.0
+  __TEXT.__text: 0x91c06c
   __TEXT.__auth_stubs: 0x1210
   __TEXT.__objc_methlist: 0xabec
   __TEXT.__const: 0xed48

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E18BBB09-19F0-3E16-8B00-F125A9DE9EDB
+  UUID: 7199CC38-A8F8-3C97-8492-0649FFD49362
   Functions: 7870
   Symbols:   22750
   CStrings:  5895
Functions:
~ __ZN3AGX6DeviceINS_6HAL3008EncodersENS1_7ClassesENS1_10ObjClassesEE20setupHWResourcePoolsEP19AGXG18PFamilyDevicePP22IOGPUMetalResourcePool : 564 -> 568
~ -[AGXG18PFamilyTexture updateBindDataWithAddresses:cpuMetadataAddress:gpuVirtualAddress:isCompressible:shouldInitMetadata:] : 672 -> 692
~ -[AGXG18PFamilyTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:] : 3852 -> 3872

```
