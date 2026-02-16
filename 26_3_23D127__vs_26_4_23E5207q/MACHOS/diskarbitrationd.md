## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-535.80.3.0.0
-  __TEXT.__text: 0x1a38c
-  __TEXT.__auth_stubs: 0x16f0
+535.100.31.0.0
+  __TEXT.__text: 0x1ac3c
+  __TEXT.__auth_stubs: 0x16d0
   __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x2fb3
-  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x3243
+  __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x4da
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0xb88
+  __TEXT.__unwind_info: 0x5d8
+  __DATA_CONST.__auth_got: 0xb78
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xdc0
-  __DATA_CONST.__cfstring: 0x1fe0
+  __DATA_CONST.__const: 0xdc8
+  __DATA_CONST.__cfstring: 0x2120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130
   __DATA.__bss: 0xdb0
-  __DATA.__common: 0xc8
+  __DATA.__common: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7B2A79A5-3E9D-3C60-9199-FCDF8CB56D9F
-  Functions: 501
-  Symbols:   418
-  CStrings:  919
+  UUID: 00C78B48-E70D-37D3-AC53-8A5A5C7F642B
+  Functions: 517
+  Symbols:   416
+  CStrings:  948
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x8
CStrings:
+ "%s: Found recognized result bundleID %@"
+ "%s: Found usable but limited result bundleID %@"
+ "%s: full probe failed with FSMatchResultNotRecognized for bundleID %@"
+ "%s: full probe failed with FSMatchResultRecognized/UsableButLimited bundleID %@"
+ "Apple Fabric"
+ "DAHibernateUnmount"
+ "Failed to allocate retry context, falling through to cleanup"
+ "Fibre Channel Interface"
+ "FireWire"
+ "PCI"
+ "PCI-Express"
+ "SCSI Parallel Interface"
+ "USB"
+ "Virtual Interface"
+ "__DAProbeWithFSKit_block_invoke"
+ "__DAProbeWithFSKit_block_invoke_2"
+ "__FSKitProbeStatusCallback"
+ "interconnect_type"
+ "no usable probe result was found, but we have fallback of bundleID %@, with probe match %d, preform a full probe on it"

```
