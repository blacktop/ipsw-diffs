## AppSSOUI

> `/System/Library/PrivateFrameworks/AppSSOUI.framework/Versions/A/AppSSOUI`

```diff

-  __TEXT.__text: 0x9230
+  __TEXT.__text: 0x9338
   __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0xb0
-  __TEXT.__oslogstring: 0x8ab
-  __TEXT.__cstring: 0xdd6
-  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__oslogstring: 0x902
+  __TEXT.__cstring: 0xe09
+  __TEXT.__gcc_except_tab: 0x2e8
   __TEXT.__dlopen_cstrs: 0x1fc
   __TEXT.__unwind_info: 0x308
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x1a78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1b0

   - /usr/lib/libobjc.A.dylib
   Functions: 184
   Symbols:   736
-  CStrings:  160
+  CStrings:  163
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[SOAgent connectionInvalidated] : 144 -> 192
~ -[SOAgent authorization:didCompleteWithCredential:error:] : 520 -> 568
~ -[SOAgent _extensionCleanup] : 288 -> 456
CStrings:
+ "client connection invalidated during authorization"
+ "firing orphaned _authorizationCompletion — client/extension disconnected during auth"

```
