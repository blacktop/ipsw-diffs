## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61901.60.29.0.0
-  __TEXT.__text: 0x1eafc
+61901.60.37.0.0
+  __TEXT.__text: 0x1eb94
   __TEXT.__auth_stubs: 0x670
   __TEXT.__delay_helper: 0x668
   __TEXT.__objc_methlist: 0x197c
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__cstring: 0x12e8
+  __TEXT.__cstring: 0x1348
   __TEXT.__oslogstring: 0x293e
   __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0x202

   __DATA_CONST.__objc_selrefs: 0xf50
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x24a8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18c

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A02199DF-5585-3468-866B-648A07801EEB
+  UUID: B9E3BFA0-C45D-38EA-A106-16B283F36094
   Functions: 558
-  Symbols:   1979
-  CStrings:  1309
+  Symbols:   1980
+  CStrings:  1319
 
Symbols:
+ ___chkstk_darwin
Functions:
~ -[OTEscrowCheckCallResult octagonTrusted] : 12 -> 8
~ -[OTEscrowCheckCallResult description] : 244 -> 360
~ -[OTInheritanceKey unwrapWithError:] : 768 -> 788
~ -[OTInheritanceKey wrapWithWrappingKey:error:] : 672 -> 692
CStrings:
+ "1"
+ "Tq,V_octagonTrusted"
+ "graph needs repair"
+ "not trusted in cuttlefish"
+ "not trusted on device"
+ "trusted"
+ "unknown trust status"
- "!"
- "TB,V_octagonTrusted"

```
