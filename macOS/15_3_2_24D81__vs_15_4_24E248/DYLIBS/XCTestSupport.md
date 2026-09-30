## XCTestSupport

> `/System/Library/PrivateFrameworks/XCTestSupport.framework/Versions/A/XCTestSupport`

```diff

-23196.3.0.0.0
-  __TEXT.__text: 0xd34
+23790.0.0.0.0
+  __TEXT.__text: 0xe80
   __TEXT.__auth_stubs: 0xb0
-  __TEXT.__objc_methlist: 0x1ec
+  __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x1c7
   __TEXT.__unwind_info: 0xd0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x928
+  __AUTH_CONST.__objc_const: 0x640
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x180

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C7D2D0D-4898-3EA6-BAAE-285455A75F99
-  Functions: 37
-  Symbols:   151
+  UUID: 505FFB65-E99E-32AE-8BE0-BBDC859D7D7C
+  Functions: 42
+  Symbols:   156
   CStrings:  144
 
Symbols:
+ -[XCTCapabilitiesBuilder registerCapability:version:].cold.1
+ -[XCTCapabilitiesBuilder registerCapability:version:].cold.2
+ -[XCTCapabilitiesBuilder upgradeCapability:toVersion:].cold.1
+ XCTMakeSubcapability.cold.1
+ XCTMakeSubcapability.cold.2
Functions:
~ _XCTMakeSubcapability : 384 -> 160
~ -[XCTCapabilitiesBuilder registerCapability:version:] : 336 -> 212
~ -[XCTCapabilitiesBuilder upgradeCapability:toVersion:] : 232 -> 172

```
