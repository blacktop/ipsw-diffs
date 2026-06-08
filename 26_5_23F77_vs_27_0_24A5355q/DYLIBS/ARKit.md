## ARKit

> `/System/Library/Frameworks/ARKit.framework/ARKit`

```diff

-746.100.4.0.0
-  __TEXT.__text: 0xb54
-  __TEXT.__auth_stubs: 0x1a0
+779.0.0.0.5
+  __TEXT.__text: 0xab0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x111
   __TEXT.__oslogstring: 0xb
   __TEXT.__ustring: 0x5a
   __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_methname: 0xd2
-  __TEXT.__objc_stubs: 0x160
-  __DATA_CONST.__got: 0x30
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
-  - /System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
-  - /System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI
+  - /System/Library/SubFrameworks/ARKitCore.framework/ARKitCore
+  - /System/Library/SubFrameworks/ARKitFoundation.framework/ARKitFoundation
+  - /System/Library/SubFrameworks/ARKitUI.framework/ARKitUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5135DD85-BA18-3CD0-9E84-42A2E1BB0D4A
+  UUID: 214BD0A5-832B-3342-B326-2BB897164631
   Functions: 26
-  Symbols:   95
-  CStrings:  43
+  Symbols:   94
+  CStrings:  32
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ ___ARFileDescriptorIsTTY_block_invoke : 140 -> 128
~ __printFormat : 260 -> 212
~ __ARLogGeneral : 84 -> 68
~ __printMessageWithColor : 332 -> 288
~ __printError : 232 -> 224
~ __printInfo : 232 -> 224
~ __printWarning : 232 -> 224
~ _ARPrintToiTerm : 140 -> 132
~ _ARKitBuildVersionString : 144 -> 132
CStrings:
- "UTF8String"
- "_bundleWithIdentifier:andLibraryName:"
- "base64EncodedStringWithOptions:"
- "environment"
- "infoDictionary"
- "initWithFormat:arguments:"
- "length"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "processInfo"
- "stringWithFormat:"

```
