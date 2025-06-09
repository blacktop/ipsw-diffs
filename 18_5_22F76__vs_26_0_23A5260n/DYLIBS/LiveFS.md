## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-531.120.18.0.2
-  __TEXT.__text: 0x1d750
+737.0.2.0.1
+  __TEXT.__text: 0x1d758
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x1f8c
+  __TEXT.__objc_methlist: 0x2004
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1038
+  __TEXT.__cstring: 0x1029
   __TEXT.__oslogstring: 0x1483
-  __TEXT.__gcc_except_tab: 0xd00
+  __TEXT.__gcc_except_tab: 0xcf4
   __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methname: 0x42d9
-  __TEXT.__objc_methtype: 0x2aac
+  __TEXT.__objc_methname: 0x4376
+  __TEXT.__objc_methtype: 0x2a91
   __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1030
+  __DATA_CONST.__objc_selrefs: 0x1080
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x860
-  __AUTH_CONST.__objc_const: 0x2a88
-  __AUTH.__objc_data: 0x780
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0x2ad8
+  __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0x200
-  __DATA.__data: 0x728
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA.__data: 0x720
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEBF5649-2948-3E2E-AE19-F8C02BDE9C73
-  Functions: 781
-  Symbols:   2673
-  CStrings:  1363
+  UUID: EF8423D9-11D5-3B69-B84D-4B078250C7FF
+  Functions: 791
+  Symbols:   2690
+  CStrings:  1376
 
Symbols:
+ -[LiveFSSharedMutableBuffer capacity]
+ -[LiveFSSharedMutableBuffer isIOWMD]
+ -[LiveFSSharedMutableBuffer memMap]
+ -[LiveFSSharedMutableBuffer mp]
+ -[LiveFSSharedMutableBuffer setCapacity:]
+ -[LiveFSSharedMutableBuffer setIsIOWMD:]
+ -[LiveFSSharedMutableBuffer setMemMap:]
+ -[LiveFSSharedMutableBuffer setMp:]
+ -[LiveFSSharedMutableBuffer setVma:]
+ -[LiveFSSharedMutableBuffer vma]
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.75
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.75.cold.1
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.77
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.77.cold.1
+ ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.78
- _LiveFSMounterDomainContainsPhotos
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.78
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.78.cold.1
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.80
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.80.cold.1
- ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.81
CStrings:
+ "@\"NSObject<LiveFSMounterClient>\""
+ "T@\"LiveFSMemoryMap\",&,V_memMap"
+ "TB,V_isIOWMD"
+ "TI,V_mp"
+ "TQ,V_capacity"
+ "TQ,V_vma"
+ "capacity"
+ "isIOWMD"
+ "memMap"
+ "mp"
+ "setCapacity:"
+ "setIsIOWMD:"
+ "setMemMap:"
+ "setMp:"
+ "setVma:"
+ "vma"
- "@\"NSObject<LiveFSMounterClient><LiveFSMounterClientHelper>\""
- "containsPhotos"

```
