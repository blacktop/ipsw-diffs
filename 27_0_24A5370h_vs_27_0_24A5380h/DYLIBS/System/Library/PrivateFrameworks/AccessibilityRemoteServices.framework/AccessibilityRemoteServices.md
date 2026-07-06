## AccessibilityRemoteServices

> `/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices`

```diff

-  __TEXT.__text: 0x4ba8
+  __TEXT.__text: 0x4c3c
   __TEXT.__objc_methlist: 0x2e0
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__cstring: 0xd61
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__cstring: 0xd4c
   __TEXT.__oslogstring: 0x30a
   __TEXT.__unwind_info: 0x1a8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x6e0
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x54

   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 105
-  Symbols:   559
-  CStrings:  300
+  Symbols:   561
+  CStrings:  299
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _RPOptionStatusFlags
+ _SCDynamicStoreCopyComputerName
Functions:
~ -[AXRemoteReceiver initWithEventID:delegate:] : 920 -> 1068
CStrings:
+ "Q"
- "UserAssignedDeviceName"

```
