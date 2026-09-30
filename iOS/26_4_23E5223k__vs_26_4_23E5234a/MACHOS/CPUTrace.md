## CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/CPUTrace`

```diff

 134.100.20.0.0
-  __TEXT.__text: 0x2b50
-  __TEXT.__auth_stubs: 0x750
+  __TEXT.__text: 0x2b34
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_stubs: 0x640
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x284
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x8a6
+  __TEXT.__cstring: 0x763
   __TEXT.__objc_methname: 0x738
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methtype: 0x22e
   __TEXT.__gcc_except_tab: 0x314
   __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x7c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libhwtrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 483E8F7D-75EE-34D6-806E-4AE8FE8AA249
+  UUID: 430709A3-59D4-36D1-99A3-161B7389A4C0
   Functions: 56
-  Symbols:   162
-  CStrings:  269
+  Symbols:   161
+  CStrings:  268
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_ea4 : 144 -> 116
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"

```
