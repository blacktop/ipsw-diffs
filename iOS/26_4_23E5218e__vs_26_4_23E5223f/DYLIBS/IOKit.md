## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100231.100.17.0.0
-  __TEXT.__text: 0xa27a4
+100231.100.18.0.1
+  __TEXT.__text: 0xa273c
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104a4
   __TEXT.__oslogstring: 0x5302
-  __TEXT.__cstring: 0xbc64
-  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__cstring: 0xbc33
+  __TEXT.__unwind_info: 0x21b0
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xa3
   __TEXT.__objc_methtype: 0x1ad5

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 14BE0DBD-DBA9-352C-9121-733E3104D994
+  UUID: 20757387-6C59-34C5-94CF-6423E68A6A81
   Functions: 3533
   Symbols:   6841
-  CStrings:  3508
+  CStrings:  3507
 
Symbols:
+ ___IOHIDDeviceNoopReportCallback
+ ___IOHIDTransactionNoopCallback
- _IOHIDTransactionCommitWithCallback.cold.1
- _IOHIDTransactionCommitWithCallback.cold.2
CStrings:
+ "OSKEXT_BUILD_DATE 01:03:49 Feb 23 2026"
- "OSKEXT_BUILD_DATE 00:42:17 Feb 13 2026"
- "assertion failure: Callback Function is Required"

```
