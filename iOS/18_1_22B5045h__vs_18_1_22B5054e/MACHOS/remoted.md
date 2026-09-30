## remoted

> `/usr/libexec/remoted`

```diff

-166.0.0.0.0
-  __TEXT.__text: 0x3d9f4
+167.0.0.0.0
+  __TEXT.__text: 0x3de44
   __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x1340
+  __TEXT.__objc_stubs: 0x2200
+  __TEXT.__objc_methlist: 0x1358
   __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x7fa5
-  __TEXT.__cstring: 0x1e8b
-  __TEXT.__objc_methname: 0x2226
-  __TEXT.__objc_classname: 0x279
+  __TEXT.__oslogstring: 0x8096
+  __TEXT.__cstring: 0x1ec8
+  __TEXT.__objc_methname: 0x229d
+  __TEXT.__objc_classname: 0x27b
   __TEXT.__objc_methtype: 0x6e6
-  __TEXT.__gcc_except_tab: 0x1270
-  __TEXT.__unwind_info: 0xdb0
+  __TEXT.__gcc_except_tab: 0x12b0
+  __TEXT.__unwind_info: 0xdc8
   __DATA_CONST.__auth_got: 0xc08
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x1298
-  __DATA_CONST.__cfstring: 0xc80
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2400
-  __DATA.__objc_selrefs: 0x8a0
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_const: 0x2420
+  __DATA.__objc_selrefs: 0x8b8
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x670
   __DATA.__bss: 0x392

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1337
-  Symbols:   484
-  CStrings:  1705
+  Functions: 1344
+  Symbols:   485
+  CStrings:  1716
 
Symbols:
+ _OBJC_CLASS_$_SecureConfigParameters
CStrings:
+ "_researchInfraEnforcementDisabled"
+ "SecureConfig parameter '%!{(MISSING)public}@' has unexpected type"
+ "SecureConfig parameter '%!{(MISSING)public}@' not present"
+ "%!{(MISSING)public}@> Treating ncm host as trusted on research VM"
+ "Failed to load SecureConfig parameters: %!{(MISSING)public}@"
+ "research_disableAppleInfrastructureEnforcement"
+ "isTrusted"
+ "\x13"
+ "SecureConfigDB not available."
+ "loadContentsAndReturnError:"
+ "com.apple.pcc.research.disableAppleInfrastructureEnforcement"

```
