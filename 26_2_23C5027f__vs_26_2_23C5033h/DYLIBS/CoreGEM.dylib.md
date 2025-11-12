## CoreGEM.dylib

> `/System/Library/PrivateFrameworks/CoreGEM.framework/CoreGEM.dylib`

```diff

-28.0.0.0.0
-  __TEXT.__text: 0xeef50
-  __TEXT.__auth_stubs: 0xb00
+29.0.0.0.0
+  __TEXT.__text: 0xf0680
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xb870
-  __TEXT.__gcc_except_tab: 0x4468
-  __TEXT.__cstring: 0x6749
-  __TEXT.__oslogstring: 0x8f9b
-  __TEXT.__unwind_info: 0x3f20
+  __TEXT.__const: 0xb880
+  __TEXT.__gcc_except_tab: 0x4510
+  __TEXT.__cstring: 0x6757
+  __TEXT.__oslogstring: 0x9240
+  __TEXT.__unwind_info: 0x3f38
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0xc6
   __TEXT.__objc_methtype: 0x34
   __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x49670
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x8e80
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x90

   __DATA.__common: 0x1051
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x6f0
-  __DATA_DIRTY.__common: 0x280
+  __DATA_DIRTY.__bss: 0x9f0
+  __DATA_DIRTY.__common: 0x580
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: FE01AD53-7305-3428-AA80-2ABF0C5CA026
+  UUID: DFD068F7-9BF6-311A-9C44-640E3E30E865
   Functions: 4013
-  Symbols:   229
-  CStrings:  1406
+  Symbols:   227
+  CStrings:  1418
 
Symbols:
- __DefaultRuneLocale
- ___toupper
CStrings:
+ "#gem,#lpp,#cplane, incoming corrId len,%d"
+ "#gem,#lpp,#cplane,empty PDU data or corellation ID"
+ "#gem,#lpp,#cplane,failed to allocate memory for add_data.msg"
+ "#gem,#lpp,#cplane,failed to allocate memory for gen_data.msg"
+ "#gem,#lpp,#cplane,invalid corrId parameters"
+ "#gem,#lpp,#cplane,invalid lppMsg parameters"
+ "#gem,#lpp,#cplane,sending lpp msg from bridge"
+ "#lpp,#cplane, CorrId is empty"
+ "#lpp,#cplane,#corrid,%{private}zu,of,%{private}zu,%{private}s,%{private}s"
+ "#posp,#lpp, active session found"
+ "#posp,#lpp, active session found for NR with higher length session ID"
+ "#posp,#lpp, no active session"
+ "#posp,#lpp, received sessionId,%d,type,%d"
+ "/AppleInternal/Library/BuildRoots/4~CBbqugCNV6iL9iyJ5UgPw1SgL-O9UOq9NjI-8x0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "handleCPlaneDlLppMsg,pduSize or correlationIdSize invalid"
+ "handleCPlaneDlLppMsg,pduSize,%d,corrIdSize,%d"
+ "handleCPlaneDlLppMsg,sn,%d,pdusize,%d,corrIdSize,%d"
- "/AppleInternal/Library/BuildRoots/4~CATAugAfxIy1ekBDgy99rfGafKx-KOyvIszlrso/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "0471001123"
- "handleCPlaneDlLppMsg,pduSize invalid"
- "handleCPlaneDlLppMsg,pduSize,%d"
- "handleCPlaneDlLppMsg,sn,%d,pdusize,%d"

```
